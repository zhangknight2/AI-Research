# AceCamp 文章抓取器

每天定时从 [AceCamp](https://www.acecamptech.com/search) 下载文章，按分类保存为 Markdown 格式。

## 快速开始

### 1. 安装依赖

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### 2. 配置凭据

编辑 `.env` 文件，填入你的账号密码：

```
ACECAMP_USERNAME=你的账号
ACECAMP_PASSWORD=你的密码
```

### 3. 首次运行（调试模式）

先用 `--discover` 查看能发现哪些文章：

```bash
python3 scraper.py --discover
```

如果需要看到浏览器窗口来调试：

```bash
python3 scraper.py --discover --no-headless
```

调试截图和页面HTML会保存在 `debug/` 目录。

### 4. 正常抓取

```bash
python3 scraper.py
```

文章会保存到 `articles/<分类>/文章标题.md`。

### 5. 设置定时任务（东京时间每晚 23:30）

东京时间 23:30 = UTC 14:30

```bash
# 编辑 crontab
crontab -e

# 添加以下行（每天 UTC 14:30 执行，即东京时间 23:30）
30 14 * * * /home/user/AI-Research/run.sh >> /home/user/AI-Research/logs/cron.log 2>&1
```

## 文件结构

```
.
├── scraper.py         # 主抓取脚本
├── config.yaml        # 配置文件
├── .env               # 登录凭据（不提交到git）
├── .env.example       # 凭据模板
├── run.sh             # 运行脚本
├── requirements.txt   # Python 依赖
├── articles/          # 下载的文章（按分类）
│   ├── 分类A/
│   │   └── 文章标题.md
│   └── 分类B/
│       └── 文章标题.md
├── data/
│   └── downloaded.json  # 已下载记录（避免重复下载）
├── logs/              # 日志
└── debug/             # 调试截图和HTML
```

## 命令行参数

| 参数 | 说明 |
|------|------|
| `--discover` | 仅发现文章列表，不下载 |
| `--no-headless` | 显示浏览器窗口 |
| `--skip-login` | 跳过登录 |
| `--config FILE` | 使用自定义配置文件 |
