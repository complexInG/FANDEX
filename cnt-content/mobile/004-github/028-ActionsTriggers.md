# GitHub Actions 触发器速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 单一触发

**基本用法:push 触发**
`on: push`

```yaml
on:
  push:
    branches:
      - main
      - 'release/*'
    paths:
      - 'src/**'
      - 'package.json'
    tags:
      - 'v*'
```

---

**基本用法:pull_request 触发**
`on: pull_request`

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened]
    branches:
      - main
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

---

## 定时触发

**基本用法:定时任务**
`on: schedule`

```yaml
on:
  schedule:
    # 每天 UTC 00:00 执行
    - cron: '0 0 * * *'
    # 每周一 9 点
    - cron: '0 9 * * 1'
```

---

## 手动触发

**基本用法:手动触发**
`on: workflow_dispatch`

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署环境'
        required: true
        type: choice
        options:
          - staging
          - production
        default: staging
      version:
        description: '版本号'
        required: false
        default: '1.0.0'
```

---

## 仓库事件触发

**基本用法:issue 与 release**
`on: <事件>`

```yaml
on:
  issues:
    types: [opened, labeled]
  issue_comment:
    types: [created]
  release:
    types: [published]
  push:
    branches: [main]
```

---

## 工作流调用

**基本用法:被其他工作流调用**
`on: workflow_call`

```yaml
on:
  workflow_call:
    inputs:
      target:
        type: string
        required: true
    secrets:
      DEPLOY_KEY:
        required: true
```

---

## 触发过滤组合

**基本用法:多触发组合**
`on: [<事件>]`

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:
```

---