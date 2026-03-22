# AI硬件产业链投资研究知识库

基于 Claude Code 的AI硬件和基础设施产业链投资研究系统，用文件系统实现持久化记忆和历史回溯。

## 目录结构

```
research/
├── knowledge_base/
│   ├── portfolio.md          # 持仓跟踪
│   ├── core_assumptions.md   # 核心变量与假设
│   ├── summary.md            # 项目汇总（增量迭代）
│   └── index.md              # 材料分析索引
├── materials/                # 原始材料（不提交git）
│   ├── 纪要/
│   ├── 研报/
│   ├── 财报/
│   ├── 新闻/
│   └── 其他/
├── analysis/                 # 分析输出
└── archive/                  # 已过时内容
acecamp-articles/ → 软链接到爬虫仓库的 articles/
```

## 使用方式

在 Claude Code 中打开本项目，CLAUDE.md 会自动加载。三种输入方式：

1. **直接粘贴** — 在对话中贴材料文字，最常用
2. **放文件到 inbox** — 将 PDF/Word/MD 放入 `research/inbox/`，然后说"处理inbox"
3. **AceCamp 自动抓取** — 说"筛选新文章"触发批量筛选

所有渠道的材料都会自动归档到 `research/materials/`，分析结果保存到 `research/analysis/`。

## 初始设置

```bash
# 配置 AceCamp 文章源（软链接到爬虫仓库）
ln -s ~/AI-Research-Scraper/articles acecamp-articles
```

## 关注领域

存储 / 算力 / 光通信 / AI系统架构 / 上游供给 / 需求侧 / AI能源
