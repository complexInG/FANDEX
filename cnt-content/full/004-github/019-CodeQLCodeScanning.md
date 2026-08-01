---
order: 61
title: CodeQL代码扫描
module: github
category: GitHub
difficulty: intermediate
description: 'GitHub CodeQL代码扫描：静态分析、查询编写与安全漏洞检测。'
author: fanquanpp
updated: '2026-08-01'
related:
  - 'github/Issues模板-标签与里程碑'
  - github/密钥扫描
  - github/命令行工具
  - 'github/REST与GraphQL-API'
prerequisites:
  - github/GitHub概述
---

## 1. CodeQL 概述

### 1.1 什么是 CodeQL

CodeQL 是 GitHub 的**静态代码分析引擎**，通过将代码转换为数据库并运行查询来发现安全漏洞和代码缺陷。

### 1.2 工作原理

```
源代码 → CodeQL 数据库 → 运行查询 → 发现问题
```

## 2. 配置代码扫描

### 2.1 使用默认配置

```yaml
# .github/workflows/codeql.yml
name: CodeQL
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 1' # 每周一

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3
```

### 2.2 支持的语言

| 语言                      | 分析类型    |
| :------------------------ | :---------- |
| **JavaScript/TypeScript** | 安全 + 质量 |
| **Python**                | 安全 + 质量 |
| **Java**                  | 安全 + 质量 |
| **C/C++**                 | 安全 + 质量 |
| **C#**                    | 安全 + 质量 |
| **Go**                    | 安全 + 质量 |
| **Ruby**                  | 安全        |
| **Swift**                 | 安全        |
| **Kotlin**                | 安全        |

### 2.3 自定义配置

```yaml
# .github/codeql/codeql-config.yml
name: Custom CodeQL Config
paths:
  - src
  - lib
paths-ignore:
  - '**/test/**'
  - '**/tests/**'
queries:
  - uses: security-and-quality
  - uses: ./custom-queries
```

## 3. 查看扫描结果

### 3.1 Security 选项卡

仓库 → Security → Code scanning alerts

### 3.2 告警级别

| 级别        | 说明           |
| :---------- | :------------- |
| **Error**   | 确定的安全漏洞 |
| **Warning** | 潜在的安全问题 |
| **Note**    | 建议性改进     |

### 3.3 常见检测

- SQL 注入
- XSS（跨站脚本）
- 路径遍历
- 不安全的反序列化
- 硬编码凭证
- 不安全的随机数

## 4. 自定义查询

### 4.1 CodeQL 查询语法

```ql
/**
 * @name SQL injection
 * @description Detects SQL injection vulnerabilities
 * @kind path-problem
 * @security-severity 9.0
 */

import python

from Call call, StrConst sql
where
  call.getFunc().hasName("execute") and
  sql = call.getArg(0) and
  exists(Call format |
    format.getFunc().hasName("format") and
    format = sql.getAChild*()
  )
select call, "Potential SQL injection"
```

### 4.2 查询套件

```yaml
# codeql-suite.yml
name: Custom Query Suite
queries:
  - uses: security-and-quality
  - uses: ./custom-queries/sql-injection.ql
```

## 5. 最佳实践

- 在 PR 中运行代码扫描，及早发现问题
- 定期运行全量扫描（schedule）
- 关注高严重性告警
- 将误报标记为已忽略并说明原因
- 结合其他安全工具（Dependabot、密钥扫描）

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
