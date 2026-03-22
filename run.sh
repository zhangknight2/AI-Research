#!/bin/bash
# AceCamp 文章抓取器 - 运行脚本
# 用法:
#   ./run.sh              # 正常抓取
#   ./run.sh --discover   # 仅发现文章（调试用）
#   ./run.sh --no-headless # 显示浏览器

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 激活虚拟环境（如果存在）
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
fi

python3 scraper.py "$@"
