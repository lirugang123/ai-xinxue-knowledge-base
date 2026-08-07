name: Feature Request
description: 提出新功能建议
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        提出新功能建议，帮助我们改进项目！
  - type: textarea
    id: problem
    attributes:
      label: 问题描述
      description: 这个功能解决什么问题？
      placeholder: 描述问题背景...
  - type: textarea
    id: solution
    attributes:
      label: 建议方案
      description: 你建议如何实现？
      placeholder: 描述你的解决方案...
  - type: textarea
    id: alternatives
    attributes:
      label: 替代方案
      description: 你考虑过哪些替代方案？
      placeholder: 其他可能的方案...
  - type: textarea
    id: additional
    attributes:
      label: 补充信息
      description: 其他相关信息
      placeholder: 截图、链接等...
