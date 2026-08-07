# 贡献指南

感谢你对我们的项目感兴趣！本指南将帮助你了解如何贡献代码。

## 开发环境

### 前置要求
- Python 3.11+
- Git
- pip

### 安装依赖
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 开发流程

### 1. Fork仓库
点击GitHub右上角的Fork按钮。

### 2. 克隆仓库
```bash
git clone git@github.com:你的用户名/仓库名.git
cd 仓库名
```

### 3. 创建分支
```bash
git checkout -b feature/你的功能名称
# 或
git checkout -b fix/问题编号
```

### 4. 编写代码
- 遵循项目的代码规范
- 添加必要的测试
- 更新相关文档

### 5. 运行测试
```bash
pytest tests/ -v
```

### 6. 提交代码
```bash
git add .
git commit -m "feat: 添加新功能"
# 或
git commit -m "fix: 修复问题"
```

### 7. 推送分支
```bash
git push origin feature/你的功能名称
```

### 8. 创建Pull Request
在GitHub上创建Pull Request，填写详细说明。

## 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat:` 新功能
- `fix:` Bug修复
- `docs:` 文档更新
- `style:` 代码格式（不影响逻辑）
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

## 代码规范

### Python代码
- 遵循PEP 8规范
- 使用flake8检查
- 添加类型注解
- 编写docstring

### 测试代码
- 测试文件命名：`test_*.py`
- 测试函数命名：`test_*`
- 使用pytest框架
- 覆盖率达到80%以上

## 文档规范

- 使用Markdown格式
- 标题层级清晰
- 包含代码示例
- 保持文档更新

## 问题反馈

如发现Bug或提出建议，请创建Issue并选择相应模板。

## License

本项目采用MIT许可证。
