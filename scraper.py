#!/usr/bin/env python3
"""
AceCamp 文章抓取器
从 https://www.acecamptech.com/search 抓取文章，按分类保存为 Markdown。
使用 Playwright 处理 JavaScript SPA 渲染。
支持登录认证。

用法:
    python scraper.py                  # 正常抓取（增量下载新文章）
    python scraper.py --discover       # 仅发现文章，不下载（用于调试）
    python scraper.py --no-headless    # 显示浏览器窗口（用于调试）
    python scraper.py --config other.yaml  # 使用自定义配置文件
"""

import argparse
import json
import os
import re
import logging
import hashlib
import shutil
import random
import time
from datetime import datetime, timezone, timedelta
from urllib.parse import urljoin, urlparse

import yaml
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
from markdownify import markdownify as md


# 东京时区
JST = timezone(timedelta(hours=9))


def setup_logging(log_file: str) -> logging.Logger:
    """配置日志"""
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("acecamp_scraper")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(log_file, encoding="utf-8")
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


def load_config(config_path: str = "config.yaml") -> dict:
    """加载配置文件"""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_env(env_path: str = ".env") -> dict:
    """加载 .env 文件"""
    env = {}
    if not os.path.exists(env_path):
        return env
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env[key.strip()] = value.strip()
    return env


def load_history(history_file: str) -> dict:
    """加载已下载文章的历史记录"""
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"downloaded": {}}


def save_history(history_file: str, history: dict):
    """保存下载历史"""
    os.makedirs(os.path.dirname(history_file), exist_ok=True)
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def article_id(url: str) -> str:
    """根据URL生成文章唯一ID"""
    return hashlib.md5(url.encode()).hexdigest()


def sanitize_filename(name: str) -> str:
    """将标题转换为安全的文件名（限制60字符，避免文件名过长）"""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip()
    if len(name) > 60:
        name = name[:60]
    return name or "untitled"


# ============================================================
# 登录
# ============================================================

def do_login(page, config: dict, env: dict, logger: logging.Logger) -> bool:
    """
    登录 AceCamp 网站。
    自动检测登录表单并填入凭据。
    返回 True 表示登录成功。
    """
    username = env.get("ACECAMP_USERNAME", "")
    password = env.get("ACECAMP_PASSWORD", "")

    if not username or not password:
        logger.error("未配置登录凭据！请在 .env 文件中设置 ACECAMP_USERNAME 和 ACECAMP_PASSWORD")
        return False

    base_url = config["base_url"]
    login_url = config.get("login_url", f"{base_url}/login")

    logger.info(f"正在登录: {login_url}")

    try:
        page.goto(login_url, wait_until="domcontentloaded", timeout=30000)
    except PlaywrightTimeout:
        logger.warning("登录页面加载超时，继续尝试...")
    except Exception as e:
        logger.warning(f"登录页面加载异常: {e}，尝试重新加载...")
        try:
            page.goto(login_url, wait_until="commit", timeout=30000)
        except Exception as e2:
            logger.error(f"重试加载登录页面仍然失败: {e2}")
            return False

    # SPA 需要等待 JS 渲染完成，等待输入框出现
    logger.info("等待登录表单渲染...")
    try:
        page.wait_for_selector(
            'input[type="text"], input[type="email"], input[type="password"], input[name="username"], input[name="account"]',
            timeout=15000
        )
        logger.info("登录表单已出现")
    except PlaywrightTimeout:
        logger.warning("等待登录表单超时，继续尝试...")
        page.wait_for_timeout(5000)

    # 保存登录页截图用于调试
    os.makedirs("debug", exist_ok=True)
    page.screenshot(path="debug/login_page.png", full_page=True)

    # 如果默认是验证码登录模式，先切换到密码登录
    password_mode_selectors = [
        'div.link:has-text("Login via password")',
        'div.link:has-text("密码登录")',
        ':text("Login via password")',
        ':text("密码登录")',
        'a:has-text("Login via password")',
        'a:has-text("密码登录")',
    ]
    for sel in password_mode_selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                logger.info(f"已切换到密码登录模式 (选择器: {sel})")
                page.wait_for_timeout(2000)
                page.screenshot(path="debug/login_page_password_mode.png", full_page=True)
                break
        except Exception:
            continue

    # 自动检测用户名输入框
    username_selectors = [
        'input[name="username"]',
        'input[name="email"]',
        'input[name="account"]',
        'input[name="user"]',
        'input[name="loginName"]',
        'input[name="login"]',
        'input[type="email"]',
        'input[type="text"][placeholder*="邮箱"]',
        'input[type="text"][placeholder*="用户"]',
        'input[type="text"][placeholder*="账号"]',
        'input[type="text"][placeholder*="email"]',
        'input[type="text"][placeholder*="user"]',
        'input[placeholder*="邮箱"]',
        'input[placeholder*="用户"]',
        'input[placeholder*="账号"]',
        'input[placeholder*="手机"]',
        # 通用回退：页面上第一个 text/email 输入框
        'input[type="text"]',
        'input[type="email"]',
    ]

    password_selectors = [
        'input[name="password"]',
        'input[name="passwd"]',
        'input[name="pass"]',
        'input[type="password"]',
    ]

    submit_selectors = [
        'button[type="submit"]',
        'input[type="submit"]',
        'button:has-text("登录")',
        'button:has-text("Login")',
        'button:has-text("Sign in")',
        'button:has-text("登 录")',
        '[class*="login"] button',
        '[class*="submit"] button',
        'form button',
    ]

    # 填入用户名
    username_filled = False
    for sel in username_selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                el.fill(username)
                username_filled = True
                logger.info(f"已填入用户名 (选择器: {sel})")
                break
        except Exception:
            continue

    if not username_filled:
        logger.error("未找到用户名输入框！已保存截图到 debug/login_page.png")
        return False

    # 填入密码
    password_filled = False
    for sel in password_selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                el.fill(password)
                password_filled = True
                logger.info(f"已填入密码 (选择器: {sel})")
                break
        except Exception:
            continue

    if not password_filled:
        logger.error("未找到密码输入框！已保存截图到 debug/login_page.png")
        return False

    # 勾选服务条款复选框（如果存在）
    tos_selectors = [
        'input[type="checkbox"]',
        '.ant-checkbox-input',
        '.ant-checkbox',
        'label:has-text("Terms") input',
        'label:has-text("agree") input',
    ]
    for sel in tos_selectors:
        try:
            el = page.query_selector(sel)
            if el:
                if not el.is_checked():
                    el.click()
                    logger.info(f"已勾选服务条款 (选择器: {sel})")
                else:
                    logger.info("服务条款已勾选")
                break
        except Exception:
            continue

    # 点击登录按钮
    submitted = False
    for sel in submit_selectors:
        try:
            el = page.query_selector(sel)
            if el and el.is_visible():
                el.click()
                submitted = True
                logger.info(f"已点击登录按钮 (选择器: {sel})")
                break
        except Exception:
            continue

    if not submitted:
        # 回退：按 Enter 提交
        logger.info("未找到登录按钮，尝试按 Enter 提交")
        page.keyboard.press("Enter")

    # 等待登录完成
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
        page.wait_for_timeout(3000)
    except PlaywrightTimeout:
        pass

    # 保存登录后截图
    page.screenshot(path="debug/after_login.png", full_page=True)

    # 检查是否登录成功
    current_url = page.url
    logger.info(f"登录后URL: {current_url}")

    # 如果还在登录页面，可能登录失败
    if "/login" in current_url.lower() or "/signin" in current_url.lower():
        # 检查是否有错误提示
        error_selectors = [
            '[class*="error"]', '[class*="alert"]', '[class*="warning"]',
            '[class*="msg"]', '.toast'
        ]
        for sel in error_selectors:
            try:
                el = page.query_selector(sel)
                if el and el.is_visible():
                    error_text = (el.inner_text() or "").strip()
                    if error_text:
                        logger.error(f"登录失败，错误信息: {error_text}")
                        return False
            except Exception:
                continue
        logger.warning("可能登录失败（仍在登录页面），但继续尝试...")
        return False

    logger.info("登录成功！")
    return True


# ============================================================
# 文章发现
# ============================================================

def discover_categories(page, base_url: str, logger: logging.Logger) -> list[dict]:
    """发现网站上的文章分类"""
    logger.info("正在发现文章分类...")
    categories = []

    category_selectors = [
        'nav a[href*="categ"]', 'nav a[href*="search"]',
        '.category a', '.categories a',
        '.sidebar a', '.filter a', '.tag a',
        '[class*="category"] a', '[class*="filter"] a',
        '[class*="tab"] a', '[class*="tag"] a', '[class*="nav"] a',
        'a[href*="/category/"]', 'a[href*="/tag/"]', 'a[href*="/topics/"]',
    ]

    for selector in category_selectors:
        try:
            elements = page.query_selector_all(selector)
            for el in elements:
                text = (el.inner_text() or "").strip()
                href = el.get_attribute("href")
                if text and href:
                    full_url = urljoin(base_url, href)
                    if full_url not in [c["url"] for c in categories]:
                        categories.append({"name": text, "url": full_url})
        except Exception:
            continue

    if not categories:
        logger.info("未找到明确分类，将使用页面自动检测的分组")

    logger.info(f"发现 {len(categories)} 个分类")
    for cat in categories:
        logger.info(f"  - {cat['name']}: {cat['url']}")

    return categories


def discover_articles(page, base_url: str, logger: logging.Logger) -> list[dict]:
    """从当前页面发现文章链接"""
    articles = []
    article_selectors = [
        'article a', '.article-item a', '.post-item a',
        '[class*="article"] a', '[class*="post"] a',
        '[class*="card"] a', '[class*="item"] a[href]',
        '[class*="list"] a[href]', '.content a[href]', 'main a[href]',
    ]

    seen_urls = set()

    for selector in article_selectors:
        try:
            elements = page.query_selector_all(selector)
            for el in elements:
                href = el.get_attribute("href")
                if not href:
                    continue

                full_url = urljoin(base_url, href)
                parsed = urlparse(full_url)

                if parsed.netloc and base_url and parsed.netloc not in base_url:
                    continue

                skip_patterns = [
                    '/search', '/login', '/register', '/about',
                    '/contact', '/privacy', '/terms', '#',
                    'javascript:', 'mailto:', '/api/'
                ]
                if any(p in full_url.lower() for p in skip_patterns):
                    continue

                if full_url in seen_urls:
                    continue

                # 只保留文章详情页（排除非文章链接如导航、广告等）
                if '/detail/' not in full_url:
                    continue

                seen_urls.add(full_url)

                title = (el.inner_text() or "").strip()
                if not title:
                    title = el.get_attribute("title") or ""
                title = title.strip()

                if not title or len(title) < 2:
                    continue

                category = "未分类"
                try:
                    parent = el.evaluate("""el => {
                        let node = el.closest('[class*="category"], [data-category], [class*="section"]');
                        if (node) {
                            return node.getAttribute('data-category') ||
                                   node.className.match(/category[_-]?(\\w+)/)?.[1] || '';
                        }
                        return '';
                    }""")
                    if parent:
                        category = parent
                except Exception:
                    pass

                articles.append({
                    "title": title,
                    "url": full_url,
                    "category": category
                })
        except Exception:
            continue

    logger.info(f"发现 {len(articles)} 篇文章")
    return articles


def scroll_to_load_all(page, logger: logging.Logger, max_scrolls: int = 20):
    """滚动页面以加载所有内容（处理无限滚动）"""
    logger.info("滚动页面加载更多内容...")
    previous_height = 0
    for i in range(max_scrolls):
        current_height = page.evaluate("document.body.scrollHeight")
        if current_height == previous_height:
            logger.info(f"滚动 {i} 次后内容已全部加载")
            break
        previous_height = current_height
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1500)


# ============================================================
# 文章内容抓取
# ============================================================

def scrape_article_content(page, url: str, base_url: str, logger: logging.Logger,
                           fallback_title: str = "", source_category: str = "") -> dict | None:
    """抓取单篇文章内容，返回结构化数据。source_category 是从标签页传入的分类（纪要/观点）"""
    try:
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)
    except PlaywrightTimeout:
        logger.warning(f"加载超时: {url}")
        return None
    except Exception as e:
        logger.error(f"加载失败: {url} - {e}")
        return None

    # 对纪要文章，等待 VIP 内容渲染，并尝试切换到中文
    if '/article/detail/' in url:
        # 额外等待确保 SPA 内容渲染完成
        page.wait_for_timeout(3000)
        try:
            for cn_text in ['Chinese', '中文', '原文']:
                el = page.query_selector(f'text="{cn_text}"')
                if el and el.is_visible():
                    el.click()
                    page.wait_for_timeout(3000)
                    logger.info(f"已点击 '{cn_text}' 切换到中文")
                    break
        except Exception:
            pass

    # 获取标题
    title = ""
    for sel in ['h1', 'article h1', '.article-title', '.post-title',
                '[class*="title"] h1', '[class*="title"] h2', 'main h1']:
        try:
            el = page.query_selector(sel)
            if el:
                title = (el.inner_text() or "").strip()
                if title:
                    break
        except Exception:
            continue
    if not title:
        title = page.title() or "untitled"

    # 获取发布日期
    pub_date = ""
    for sel in ['time', '[class*="date"]', '[class*="time"]',
                '[class*="publish"]', 'meta[property="article:published_time"]']:
        try:
            el = page.query_selector(sel)
            if el:
                pub_date = (
                    el.get_attribute("datetime") or
                    el.get_attribute("content") or
                    el.inner_text() or ""
                ).strip()
                if pub_date:
                    break
        except Exception:
            continue

    # 获取正文：优先用 HTML 选择器，否则用纯文本
    content_html = ""
    for sel in ['article', '.article-content', '.post-content',
                '[class*="article-body"]', '[class*="post-body"]',
                '.entry-content']:
        try:
            el = page.query_selector(sel)
            if el:
                html = el.inner_html()
                if len(html) > 500:
                    content_html = html
                    break
        except Exception:
            continue

    if content_html:
        # HTML 模式：清理并转换为 Markdown
        soup = BeautifulSoup(content_html, "html.parser")
        for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'iframe', 'noscript']):
            tag.decompose()
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src and not src.startswith(('http://', 'https://', 'data:')):
                img['src'] = urljoin(base_url, src)
        content_md = md(str(soup), heading_style="ATX", bullets="-")
    else:
        # 纯文本模式：SPA 页面无法匹配标准 HTML 选择器，直接提取纯文本
        try:
            content_md = page.inner_text("body") or ""
            logger.info(f"使用纯文本模式提取内容 ({len(content_md)} 字符)")
        except Exception:
            logger.warning(f"无法获取文章内容: {url}")
            return None

    content_md = re.sub(r'\n{3,}', '\n\n', content_md)

    # 清理文末无效内容：免责声明、评论区、推荐文章、页脚等
    cleanup_markers = [
        'Solemn statement:',
        '郑重声明：',
        '免责声明',
        '投资有风险',
        '仅供参考',
        '风险提示',
        '\nComments\n',
        '\nPublished\n',
        '\nNo Data\n',
        '\nFor You\n',
        '\nAPP Download\n',
        'APP Download',
        'Android & iOS',
        'WeChat Official Account',
        'AceCampTech\n\nCorporate Address',
        'Copyright©',
        '京ICP备',
        '\n智能追问\n',
        '\n专家简介',
        '\n预约专家1对1访谈\n',
        '\n评论\n',
        '\n已发布',
        '\n为你推荐\n',
        '\n下载APP\n',
    ]
    for marker in cleanup_markers:
        idx = content_md.find(marker)
        if idx > 0:
            content_md = content_md[:idx].rstrip()

    # 清理文章开头的导航和元数据（纯文本模式下会包含整个页面的文本）
    # 纪要文章：查找正文起始标记
    content_start_markers = [
        '以下为专家观点：', '以下为专家观点',
        '已享VIP免费\n', 'VIP Free\n',
        'Below are expert opinions',
    ]
    for marker in content_start_markers:
        idx = content_md.find(marker)
        if idx > 0:
            content_md = content_md[idx + len(marker):].strip()
            break
    else:
        # 如果没找到特定标记，尝试去掉导航栏头部（从"首页"到标题之后的元数据）
        content_md = re.sub(
            r'^.*?(?:预约专家1对1访谈|Expert 1-on-1|行业专家|独立研究|Industry Expert|Independent Research)\n+(?:中文\n+EN\n+)?(?:The original version is in Chinese FYI\n+)?',
            '', content_md, count=1, flags=re.DOTALL
        )

    # 去掉 VIP/行业 信息行和 阅读/点赞 行
    content_md = re.sub(r'^VIP.*?[行I].*?[：:].+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^阅读\s+\d+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^点赞\s+\d+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^Views\s+\d+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^Likes\s+\d+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^AI 速览.*?\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^Quick-Q\n+', '', content_md, flags=re.MULTILINE)
    # 去掉观点文章开头的元数据
    content_md = re.sub(r'^\d+\s+(?:Followers?|关注者)(?:Follow|关注)\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^(?:Industry|行业)[：:].+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^(?:Creation time|创建时间)[：:].+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^(?:Update time|更新时间)[：:].+\n+', '', content_md, flags=re.MULTILINE)
    content_md = re.sub(r'^\d+[\.\d]*[WwKk万]?\+?\s*(?:Views?|阅读)\|?\d*\s*(?:Favorites?|收藏)\n+', '', content_md, flags=re.MULTILINE)
    # 清理尾部的按钮文本
    content_md = re.sub(r'\n+\d+\n+(?:差评|好评)\n+\d+\n+分享\s*$', '', content_md)
    content_md = re.sub(r'\n+\d+\n+\d+\n+(?:Share|分享)\n+(?:Favorite|收藏)\s*$', '', content_md)
    content_md = re.sub(r'\n+(?:Fold|收起)\s*$', '', content_md)

    content_md = re.sub(r'\n{3,}', '\n\n', content_md).strip()

    # 通用标题列表（页面未渲染真实标题时的占位符）
    generic_titles = {"article details", "insight details", "insights", "untitled", "",
                      "文章详情", "观点详情", "纪要详情", "详情"}

    # 如果标题是通用的，尝试从正文提取真实标题
    if title.lower() in generic_titles:
        lines = content_md.strip().split('\n')
        for line in lines:
            line = line.strip().lstrip('#').strip()
            if line and len(line) >= 4 and line.lower() not in generic_titles:
                title = line[:200]
                break

    # 如果仍然是通用标题，使用搜索页发现的标题作为后备
    if title.lower() in generic_titles and fallback_title:
        # 清理 fallback_title（搜索页的标题可能包含序号前缀如 "5.\n"）
        clean_fallback = re.sub(r'^\d+\.\s*', '', fallback_title).strip()
        # 去掉多行，只取第一行有意义的部分
        first_line = clean_fallback.split('\n')[0].strip()
        if first_line and first_line.lower() not in generic_titles:
            title = first_line

    # 根据标签页来源分类（优先），或根据 URL 判断
    if source_category == "观点" or '/viewpoint/detail/' in url:
        category = "观点"
        # 去掉观点标题前的情绪标签
        sentiment_labels = ["Cautious", "Neutral", "Positive", "Negative", "Bullish", "Bearish",
                           "谨慎", "中性", "正面", "负面", "看多", "看空"]
        for label in sentiment_labels:
            if title.startswith(label):
                title = title[len(label):].strip()
                break
    elif source_category == "纪要" or '/article/detail/' in url:
        # 检查是否为共享纪要：页面中是否包含 "Shared Transcript" / "共享" 标记
        is_shared = False
        try:
            page_text = page.inner_text("body")
            if "Shared Transcript" in page_text or "共享纪要" in page_text:
                is_shared = True
        except Exception:
            pass
        if not is_shared:
            try:
                shared_el = page.query_selector('a:has-text("Shared Transcript"), a:has-text("共享")')
                if shared_el:
                    is_shared = True
            except Exception:
                pass
        category = "共享纪要" if is_shared else "本营纪要"
    else:
        category = "未分类"

    return {
        "title": title,
        "content_md": content_md,
        "date": pub_date,
        "category": category,
        "url": url
    }


# AI 相关关键词（用于筛选 AI 行业文章）
# 需要词边界匹配的短关键词（防止误匹配）
AI_KEYWORDS_WORD_BOUNDARY = [
    'AI', 'GPU', 'LLM', 'GPT', 'HBM', 'NVL', 'CPO', 'CUDA',
]
# 较长关键词直接子串匹配即可
AI_KEYWORDS_SUBSTRING = [
    '人工智能', '大模型', '算力', 'NVIDIA', '英伟达', 'Ascend', '昇腾',
    '寒武纪', 'Cambricon', 'DeepSeek', 'OpenAI', 'NVLink',
    '机器学习', '深度学习', 'Transformer', '光互联',
    '数据中心', 'data center', '智算', '算力芯片',
    'Hygon', '海光', 'inference', '推理训练',
    'ChatGPT', 'Claude', 'Anthropic', '大语言模型',
]


def extract_date_from_str(date_str: str) -> str:
    """从日期字符串中提取 YYYY-MM-DD 格式的日期"""
    if not date_str:
        return datetime.now(JST).strftime("%Y-%m-%d")
    # 匹配 YYYY/MM/DD 或 YYYY-MM-DD
    m = re.search(r'(\d{4})[/\-](\d{1,2})[/\-](\d{1,2})', date_str)
    if m:
        return f"{m.group(1)}-{m.group(2).zfill(2)}-{m.group(3).zfill(2)}"
    return datetime.now(JST).strftime("%Y-%m-%d")


def is_ai_related(title: str, content: str) -> bool:
    """检查文章标题是否与 AI 相关（仅检查标题，避免误匹配）"""
    # 主要检查标题（更精确），辅助检查内容开头
    title_lower = title.lower()
    text = (title + " " + content[:1500]).lower()

    # 短关键词需要词边界匹配
    for kw in AI_KEYWORDS_WORD_BOUNDARY:
        if re.search(r'\b' + re.escape(kw.lower()) + r'\b', text):
            return True

    # 长关键词子串匹配
    for kw in AI_KEYWORDS_SUBSTRING:
        if kw.lower() in text:
            return True

    return False


def save_article_as_markdown(article: dict, output_dir: str, logger: logging.Logger) -> str:
    """保存文章为 Markdown 文件，文件名格式：【分类】日期_标题.md"""
    os.makedirs(output_dir, exist_ok=True)

    category = article["category"]  # 共享纪要 / 本营纪要 / 观点
    date_str = extract_date_from_str(article.get("date", ""))
    title_part = sanitize_filename(article["title"])

    # 使用 URL 末尾的 ID 确保文件名唯一
    url_id = article["url"].rstrip("/").split("/")[-1]
    filename = f"【{category}】{date_str}_{title_part}_{url_id}.md"
    filepath = os.path.join(output_dir, filename)

    now_jst = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S JST")

    md_content = f"""---
title: "{article['title']}"
source: "{article['url']}"
category: "{category}"
date: "{article.get('date', '')}"
downloaded: "{now_jst}"
---

# {article['title']}

{article['content_md']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

    logger.info(f"已保存: {filepath}")

    # AI 相关文章额外复制到 AI industry 文件夹
    if is_ai_related(article["title"], article.get("content_md", "")):
        ai_dir = os.path.join(output_dir, "AI industry")
        os.makedirs(ai_dir, exist_ok=True)
        ai_filepath = os.path.join(ai_dir, filename)
        shutil.copy2(filepath, ai_filepath)
        logger.info(f"AI相关文章已复制到: {ai_filepath}")

    return filepath


# ============================================================
# 主流程
# ============================================================

def run_discovery(page, config: dict, logger: logging.Logger) -> list[dict]:
    """分别访问纪要和观点标签页，发现文章链接"""
    base_url = config["base_url"]
    browser_cfg = config.get("browser", {})
    category_urls = config.get("category_urls", {
        "纪要": f"{base_url}/search?type=minutes",
        "观点": f"{base_url}/search?type=articles",
    })

    all_articles = []
    seen_urls = set()

    for category_name, category_url in category_urls.items():
        logger.info(f"正在访问【{category_name}】标签页: {category_url}")
        try:
            page.goto(category_url, wait_until="networkidle",
                      timeout=browser_cfg.get("timeout", 30000))
            page.wait_for_timeout(browser_cfg.get("wait_after_load", 3000))
        except PlaywrightTimeout:
            logger.warning(f"【{category_name}】页面加载超时，继续尝试...")

        scroll_to_load_all(page, logger)
        articles = discover_articles(page, base_url, logger)

        # 给每篇文章标记来源分类
        for art in articles:
            if art["url"] not in seen_urls:
                art["category"] = category_name
                all_articles.append(art)
                seen_urls.add(art["url"])

        logger.info(f"【{category_name}】发现 {len(articles)} 篇文章")

    return all_articles


def save_debug_snapshot(page, logger: logging.Logger):
    """保存当前页面的截图和HTML，用于调试"""
    debug_dir = "debug"
    os.makedirs(debug_dir, exist_ok=True)
    timestamp = datetime.now(JST).strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"{debug_dir}/page_{timestamp}.png", full_page=True)
    html_content = page.content()
    with open(f"{debug_dir}/page_{timestamp}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    logger.info(f"已保存调试快照到 {debug_dir}/page_{timestamp}.*")


def main():
    parser = argparse.ArgumentParser(description="AceCamp 文章抓取器")
    parser.add_argument("--config", default="config.yaml", help="配置文件路径")
    parser.add_argument("--discover", action="store_true", help="仅发现文章，不下载（调试用）")
    parser.add_argument("--no-headless", action="store_true", help="显示浏览器窗口（调试用）")
    parser.add_argument("--skip-login", action="store_true", help="跳过登录步骤")
    args = parser.parse_args()

    config = load_config(args.config)
    env = load_env()

    logger = setup_logging(config.get("log_file", "logs/scraper.log"))
    logger.info("=" * 60)
    logger.info("AceCamp 文章抓取器启动")
    logger.info(f"当前时间 (JST): {datetime.now(JST).strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 60)

    output_dir = config.get("output_dir", "articles")
    history_file = config.get("history_file", "data/downloaded.json")
    base_url = config["base_url"]
    browser_cfg = config.get("browser", {})

    history = load_history(history_file)
    new_count = 0
    skip_count = 0

    headless = browser_cfg.get("headless", True) and not args.no_headless

    # 查找可用的 chromium 路径
    chromium_path = browser_cfg.get("executable_path", "")
    if not chromium_path:
        # 自动检测已安装的 playwright chromium
        import glob
        candidates = sorted(
            glob.glob(os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux/chrome")),
            reverse=True
        )
        if candidates:
            chromium_path = candidates[0]

    with sync_playwright() as p:
        launch_kwargs = {
            "headless": headless,
            "args": ["--disable-http2", "--no-sandbox", "--disable-blink-features=AutomationControlled"],
        }
        if chromium_path and os.path.exists(chromium_path):
            launch_kwargs["executable_path"] = chromium_path
            logger.info(f"使用浏览器: {chromium_path}")

        # 支持代理配置：优先使用 config.yaml，否则从环境变量读取
        proxy_cfg = browser_cfg.get("proxy")
        if not proxy_cfg:
            env_proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") or \
                        os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy")
            if env_proxy:
                # 解析 http://user:pass@host:port 格式
                from urllib.parse import urlparse
                parsed = urlparse(env_proxy)
                proxy_cfg = {"server": f"{parsed.scheme}://{parsed.hostname}:{parsed.port}"}
                if parsed.username:
                    proxy_cfg["username"] = parsed.username
                if parsed.password:
                    proxy_cfg["password"] = parsed.password
        if proxy_cfg:
            launch_kwargs["proxy"] = proxy_cfg
            logger.info(f"使用代理: {proxy_cfg.get('server', '')}")

        browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
            ignore_https_errors=True,
            locale="zh-CN",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()

        # 第0步：登录
        if not args.skip_login:
            login_ok = do_login(page, config, env, logger)
            if not login_ok:
                logger.error("登录失败，请检查 .env 中的凭据和 debug/ 目录下的截图")
                save_debug_snapshot(page, logger)
                browser.close()
                return
        else:
            logger.info("已跳过登录")

        # 第1步：发现文章
        articles = run_discovery(page, config, logger)
        logger.info(f"共发现 {len(articles)} 篇文章")

        if not articles:
            logger.warning("未发现任何文章！")
            save_debug_snapshot(page, logger)
            browser.close()
            return

        # 仅发现模式：打印文章列表后退出
        if args.discover:
            logger.info("--- 发现的文章列表 ---")
            for i, art in enumerate(articles):
                logger.info(f"  [{i+1}] [{art['category']}] {art['title']}")
                logger.info(f"       {art['url']}")
            save_debug_snapshot(page, logger)
            browser.close()
            return

        # 第2步：逐篇抓取（加入随机延迟，防止触发反爬机制）
        for i, art_info in enumerate(articles):
            aid = article_id(art_info["url"])

            if aid in history["downloaded"]:
                skip_count += 1
                logger.info(f"[{i+1}/{len(articles)}] 跳过已下载: {art_info['title']}")
                continue

            # 随机延迟，避免触发反频繁点击机制
            if i > 0:
                delay_min = config.get("scrape_delay_min", 3)
                delay_max = config.get("scrape_delay_max", 8)
                delay = random.uniform(delay_min, delay_max)
                logger.info(f"等待 {delay:.1f} 秒...")
                time.sleep(delay)

            logger.info(f"[{i+1}/{len(articles)}] 正在抓取: {art_info['title']}")
            article = scrape_article_content(page, art_info["url"], base_url, logger,
                                             fallback_title=art_info.get("title", ""),
                                             source_category=art_info.get("category", ""))
            if not article:
                logger.warning(f"抓取失败，跳过: {art_info['url']}")
                continue

            if article["category"] == "未分类" and art_info.get("category", "未分类") != "未分类":
                article["category"] = art_info["category"]

            filepath = save_article_as_markdown(article, output_dir, logger)

            history["downloaded"][aid] = {
                "title": article["title"],
                "url": art_info["url"],
                "category": article["category"],
                "downloaded_at": datetime.now(JST).isoformat(),
                "filepath": filepath
            }
            save_history(history_file, history)
            new_count += 1

        browser.close()

    logger.info("=" * 60)
    logger.info(f"抓取完成！新下载: {new_count} 篇，跳过: {skip_count} 篇")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
