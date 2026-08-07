name: Question
description: 提出问题
title: "[Question]: "
labels: ["question"]
body:
  - type: markdown
    attributes:
      value: |
        有问题？欢迎提问！
  - type: textarea
    id: question
    attributes:
      label: 问题内容
      description: 你的问题是什么？
      placeholder: 详细描述你的问题...
  - type: textarea
    id: context
    attributes:
      label: 上下文
      description: 提供相关背景信息
      placeholder: 使用场景、环境等...
  - type: input
    id: version
    attributes:
      label: 版本
      description: 你使用的版本
      placeholder: v1.0.0
