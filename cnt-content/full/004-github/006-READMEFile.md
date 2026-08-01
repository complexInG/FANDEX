---
order: 50
title: README文件
module: github
category: GitHub
difficulty: beginner
description: 'GitHub README文件编写规范：结构设计、内容要素与最佳实践。'
author: fanquanpp
updated: '2026-08-01'
related:
  - github/SSH与HTTPS远程配置
  - github/协作开发规范
  - github/分支模型与分支保护规则
  - github/Gitignore配置
prerequisites:
  - github/GitHub概述
---

## 1. README 概述

### 1.1 为什么 README 很重要

README 是项目的**门面**，是访客看到的第一份文档。一个好的 README 可以：

- 让访客在 30 秒内理解项目
- 降低新贡献者的上手门槛
- 提高项目的可发现性和可信度

### 1.2 README 的核心要素

| 要素               | 优先级 | 说明                   |
| :----------------- | :----- | :--------------------- |
| **项目名称与描述** | 必须   | 一句话说清楚项目是什么 |
| **安装说明**       | 必须   | 如何安装和运行         |
| **使用示例**       | 必须   | 快速上手代码           |
| **许可证**         | 必须   | 开源协议               |
| **徽章**           | 推荐   | 状态一览               |
| **贡献指南**       | 推荐   | 如何参与               |
| **常见问题**       | 可选   | FAQ                    |

## 2. README 结构模板

```markdown
# 项目名称

![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-2.0.0-green)

简短的项目描述，一句话说明项目做什么。

## 功能特性

- 功能一：简短描述
- 功能二：简短描述
- 功能三：简短描述

## 快速开始

### 安装

\`\`\`bash
npm install my-project
\`\`\`

### 使用

\`\`\`javascript
import { createApp } from 'my-project';

const app = createApp({
target: '#app',
props: { title: 'Hello' }
});
\`\`\`

## 文档

完整文档请访问 [docs.example.com](https://docs.example.com)

## 开发

\`\`\`bash
git clone https://github.com/user/repo.git
cd repo
npm install
npm run dev
\`\`\`

## 贡献

欢迎贡献！请阅读 [贡献指南](CONTRIBUTING.md)

## 许可证

[MIT](LICENSE)
```

## 3. 徽章（Badges）

### 3.1 常用徽章

```markdown
![License](https://img.shields.io/badge/license-MIT-blue)
![npm version](https://img.shields.io/npm/v/my-package)
![Build Status](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/user/repo)
![Downloads](https://img.shields.io/npm/dm/my-package)
```

### 3.2 自定义徽章

```markdown
![Custom](https://img.shields.io/badge/状态-开发中-yellow)
![Platform](https://img.shields.io/badge/platform-Web%20%7C%20Mobile-blue)
```

## 4. 视觉元素

### 4.1 截图和 GIF

```markdown
## 预览

![Demo](docs/images/demo.gif)

<details>
<summary>更多截图</summary>

![Screenshot 1](docs/images/screenshot1.png)
![Screenshot 2](docs/images/screenshot2.png)

</details>
```

### 4.2 架构图

使用 Mermaid 绘制架构图：

````markdown
```mermaid
graph TD
    A[用户] --> B[前端]
    B --> C[API 网关]
    C --> D[用户服务]
    C --> E[订单服务]
```
````

## 5. 最佳实践

- README 控制在 200 行以内，详细内容放 Wiki
- 代码示例要**可运行**
- 安装步骤要**完整**，包括前置依赖
- 使用目录导航长文档
- 定期更新 README 与代码保持同步

## 参考文献

GitHub 文档：https://docs.github.com/zh
GitHub Actions 文档：https://docs.github.com/zh/actions
GitHub REST API：https://docs.github.com/zh/rest
GitHub GraphQL API：https://docs.github.com/zh/graphql

## 延伸阅读

GitHub Actions CI/CD，见 004-github 模块 Actions 文档。
Git 协作基础，见 003-git 模块。
DevOps 自动化，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 GitHub 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitHub Actions 深入

事件驱动：push、pull_request、schedule、workflow_dispatch；on 支持过滤路径与分支。
上下文：github（事件数据）、env、secrets、needs（任务依赖）；表达式与函数。
安全：第三方 action 固定 SHA；权限默认最小；OIDC 换取云凭证。
缓存与性能：actions/cache、并发控制、矩阵并行。

### 13.2 开源协作治理

CONTRIBUTING 定义贡献路径；Issue 标签（good first issue）引导新手。
维护者时间管理：合并队列、自动化 triage、定期发布。
社区健康：行为准则执行、讨论区沉淀、感谢贡献。
安全披露：SECURITY.md + 私密漏洞报告流程。
