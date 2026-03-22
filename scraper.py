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
    """将标题转换为安全的文件名"""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = name.strip()
    if len(name) > 100:
        name = name[:100]
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
        page.goto(login_url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)
    except PlaywrightTimeout:
        logger.warning("登录页面加载超时，继续尝试...")

    # 保存登录页截图用于调试
    os.makedirs("debug", exist_ok=True)
    page.screenshot(path="debug/login_page.png", full_page=True)

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

def scrape_article_content(page, url: str, base_url: str, logger: logging.Logger) -> dict | None:
    """抓取单篇文章内容，返回结构化数据"""
    try:
        page.goto(url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)
    except PlaywrightTimeout:
        logger.warning(f"加载超时: {url}")
        return None
    except Exception as e:
        logger.error(f"加载失败: {url} - {e}")
        return None

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

    # 获取正文 HTML
    content_html = ""
    for sel in ['article', '.article-content', '.post-content',
                '[class*="article-body"]', '[class*="post-body"]',
                '[class*="content"]', '.entry-content', 'main', '.main-content']:
        try:
            el = page.query_selector(sel)
            if el:
                html = el.inner_html()
                if len(html) > 200:
                    content_html = html
                    break
        except Exception:
            continue

    if not content_html:
        try:
            content_html = page.query_selector("body").inner_html()
        except Exception:
            logger.warning(f"无法获取文章内容: {url}")
            return None

    # 清理并转换为 Markdown
    soup = BeautifulSoup(content_html, "html.parser")
    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'iframe', 'noscript']):
        tag.decompose()
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src and not src.startswith(('http://', 'https://', 'data:')):
            img['src'] = urljoin(base_url, src)

    content_md = md(str(soup), heading_style="ATX", bullets="-")
    content_md = re.sub(r'\n{3,}', '\n\n', content_md)

    # 获取分类
    category = "未分类"
    for sel in ['[class*="category"] a', '[class*="breadcrumb"] a', '.tag a', '[class*="label"]']:
        try:
            el = page.query_selector(sel)
            if el:
                cat_text = (el.inner_text() or "").strip()
                if cat_text and len(cat_text) < 30:
                    category = cat_text
                    break
        except Exception:
            continue

    return {
        "title": title,
        "content_md": content_md,
        "date": pub_date,
        "category": category,
        "url": url
    }


def save_article_as_markdown(article: dict, output_dir: str, logger: logging.Logger) -> str:
    """保存文章为 Markdown 文件，按分类创建子目录"""
    category_dir = os.path.join(output_dir, sanitize_filename(article["category"]))
    os.makedirs(category_dir, exist_ok=True)

    filename = sanitize_filename(article["title"]) + ".md"
    filepath = os.path.join(category_dir, filename)

    now_jst = datetime.now(JST).strftime("%Y-%m-%d %H:%M:%S JST")

    md_content = f"""---
title: "{article['title']}"
source: "{article['url']}"
category: "{article['category']}"
date: "{article.get('date', '')}"
downloaded: "{now_jst}"
---

# {article['title']}

{article['content_md']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

    logger.info(f"已保存: {filepath}")
    return filepath


# ============================================================
# 主流程
# ============================================================

def run_discovery(page, config: dict, logger: logging.Logger) -> list[dict]:
    """访问搜索页面，发现所有文章链接"""
    search_url = config["search_url"]
    base_url = config["base_url"]
    browser_cfg = config.get("browser", {})

    logger.info(f"正在访问搜索页面: {search_url}")
    try:
        page.goto(search_url, wait_until="networkidle",
                  timeout=browser_cfg.get("timeout", 30000))
        page.wait_for_timeout(browser_cfg.get("wait_after_load", 3000))
    except PlaywrightTimeout:
        logger.warning("搜索页面加载超时，继续尝试...")

    scroll_to_load_all(page, logger)
    categories = discover_categories(page, base_url, logger)
    articles = discover_articles(page, base_url, logger)

    # 如果搜索页面文章较少，从分类页获取
    if len(articles) < 5 and categories:
        logger.info("搜索页面文章较少，尝试从分类页面获取...")
        for cat in categories:
            try:
                page.goto(cat["url"], wait_until="networkidle", timeout=30000)
                page.wait_for_timeout(2000)
                scroll_to_load_all(page, logger, max_scrolls=10)
                cat_articles = discover_articles(page, base_url, logger)
                for art in cat_articles:
                    art["category"] = cat["name"]
                    if art["url"] not in [a["url"] for a in articles]:
                        articles.append(art)
            except Exception as e:
                logger.warning(f"访问分类页面失败: {cat['url']} - {e}")

    return articles


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
        launch_kwargs = {"headless": headless}
        if chromium_path and os.path.exists(chromium_path):
            launch_kwargs["executable_path"] = chromium_path
            logger.info(f"使用浏览器: {chromium_path}")

        # 支持代理配置
        proxy_cfg = browser_cfg.get("proxy")
        if proxy_cfg:
            launch_kwargs["proxy"] = proxy_cfg
            logger.info(f"使用代理: {proxy_cfg.get('server', '')}")

        browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(
            viewport={"width": 1280, "height": 800},
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

        # 第2步：逐篇抓取
        for i, art_info in enumerate(articles):
            aid = article_id(art_info["url"])

            if aid in history["downloaded"]:
                skip_count += 1
                logger.info(f"[{i+1}/{len(articles)}] 跳过已下载: {art_info['title']}")
                continue

            logger.info(f"[{i+1}/{len(articles)}] 正在抓取: {art_info['title']}")
            article = scrape_article_content(page, art_info["url"], base_url, logger)
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
