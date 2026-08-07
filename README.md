# 核心大脑：AI心学知识图谱与思维链

> 定位：AI的"良知"底座

---

## 📖 项目简介

本仓库是AI的心学知识底座，专门用于投喂王阳明心学核心著作，构建结构化知识图谱。

**核心理念：**
- 知行合一 - 知识必须与实践结合
- 致良知 - 通过实践唤醒内在良知
- 心即理 - 宇宙法则存在于心中

## 🏗️ 项目结构

```
ai-xinxue-knowledge-base/
├── knowledge/           # 知识图谱数据
│   ├── texts/          # 原始文本（传习录、大学问等）
│   ├── graph/          # 知识图谱数据
│   ├── prompts/        # Prompt模板
│   └── resolutions/    # 概念解析
├── scripts/            # 处理脚本
│   ├── crawler/        # 文本爬取
│   ├── parser/         # 文本解析
│   ├── analyzer/       # 知识分析
│   └── visualizer/     # 图谱可视化
├── tests/              # 测试套件
├── examples/           # 使用示例
├── docs/               # 文档
├── config/             # 配置文件
└── .github/workflows/  # CI/CD
```

## 🎯 核心功能

### 1. 知识图谱构建
- 实体识别：人物、概念、事件
- 关系抽取：师徒、传承、对立
- 图谱存储：Neo4j/GraphDB

### 2. 智能解析
- 文本解析：文言文→现代文
- 概念解析：深层含义挖掘
- 关联分析：跨文本关联

### 3. 应用接口
- 知识问答：基于图谱的智能问答
- 概念解释：心学概念深度解析
- 实践指导：知行合一场景应用

## 📚 核心典籍

### 《传习录》
- 上卷：徐爱录
- 中卷：陆澄录
- 下卷：钱德洪录

### 《大学问》
- 致良知
- 格物致知
- 诚意正心

### 《教条示龙场诸生》
- 立志
- 勤学
- 改过
- 责善

## 🚀 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 运行文本解析
python scripts/parser/transmit_record.py

# 构建知识图谱
python scripts/analyzer/build_graph.py

# 启动知识问答
python scripts/analyzer/knowledge_qa.py
```

## 📖 学习资源

- [心学概论](docs/introduction.md)
- [传习录解读](docs/chuanxi_record.md)
- [知识图谱构建指南](docs/knowledge_graph.md)
- [API文档](docs/api.md)

## 🤝 贡献指南

欢迎贡献！请参考 [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 许可证

MIT License

---

**核心理念：知行合一，致良知**
