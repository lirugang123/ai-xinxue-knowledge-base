name: Bug Report
description: 报告Bug
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        感谢报告Bug！请填写以下信息帮助我们定位问题。
  - type: input
    id: version
    attributes:
      label: 版本
      description: 使用的版本（如v1.0.0）
      placeholder: v1.0.0
  - type: textarea
    id: description
    attributes:
      label: 问题描述
      description: 清晰简洁地描述问题
      placeholder: 描述你遇到的问题...
  - type: textarea
    id: steps
    attributes:
      label: 复现步骤
      description: 如何复现这个问题？
      placeholder: |
        1. 第一步
        2. 第二步
        3. 第三步
  - type: textarea
    id: expected
    attributes:
      label: 期望结果
      description: 你期望发生什么？
      placeholder: 期望的行为...
  - type: textarea
    id: actual
    attributes:
      label: 实际结果
      description: 实际发生了什么？
      placeholder: 实际的行为...
  - type: textarea
    id: logs
    attributes:
      label: 错误日志
      description: 粘贴相关错误日志
      render: bash
  - type: input
    id: env
    attributes:
      label: 环境信息
      description: 操作系统、Python版本等
      placeholder: Ubuntu 22.04, Python 3.11
