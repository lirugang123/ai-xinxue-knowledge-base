name: Pull Request
description: 创建Pull Request
title: "[PR]: "
labels: ["pull request"]
body:
  - type: markdown
    attributes:
      value: |
        感谢你的贡献！请填写以下信息。
  - type: input
    id: related
    attributes:
      label: 相关Issue
      description: 这个PR关联的Issue编号
      placeholder: "#123"
  - type: textarea
    id: description
    attributes:
      label: 变更说明
      description: 描述你做了什么变更
      placeholder: 详细说明变更内容...
  - type: dropdown
    id: type
    attributes:
      label: 变更类型
      options:
        - feat: 新功能
        - fix: Bug修复
        - docs: 文档更新
        - refactor: 代码重构
        - test: 测试更新
        - chore: 其他
  - type: textarea
    id: changes
    attributes:
      label: 变更文件
      description: 列出的变更文件
      placeholder: |
        - src/file1.py
        - tests/test_file1.py
  - type: textarea
    id: testing
    attributes:
      label: 测试验证
      description: 你是如何测试的？
      placeholder: 描述测试方法和结果...
  - type: checkboxes
    id: checklist
    attributes:
      label: 检查清单
      options:
        - label: 代码遵循项目规范
        - label: 已添加必要的测试
        - label: 已更新相关文档
        - label: 自测通过
  - type: textarea
    id: additional
    attributes:
      label: 补充信息
      description: 其他需要说明的内容
      placeholder: 截图、备注等...
