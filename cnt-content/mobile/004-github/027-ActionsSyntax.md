# GitHub Actions 工作流语法速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 工作流基本结构

**基本用法:定义工作流**
`name: <名称>` (`.github/workflows/*.yml`)

```yaml
# 工作流名称
name: CI

# 触发条件
on: [push, pull_request]

# 任务集合
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install
      - run: npm test
```

---

## jobs 任务定义

**基本用法:定义任务依赖**
`jobs.<id>.needs`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "test"
  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy"
```

---

**基本用法:设置运行环境**
`jobs.<id>.runs-on`

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    # 自定义环境变量
    env:
      NODE_ENV: production
    # 超时设置
    timeout-minutes: 30
    # 失败时继续
    continue-on-error: false
```

---

## steps 步骤

**基本用法:引用 Action**
`uses: <action>@<版本>`

```yaml
steps:
  # 检出代码
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
  # 设置 Node 环境
  - uses: actions/setup-node@v4
    with:
      node-version: '20'
      cache: 'npm'
  # 缓存依赖
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
```

---

**基本用法:运行命令**
`run: <命令>`

```yaml
steps:
  - name: 安装依赖
    run: npm ci

  - name: 多行命令
    run: |
      npm run build
      npm run test

  - name: 条件执行
    if: github.ref == 'refs/heads/main'
    run: npm run deploy

  - name: 设置环境变量
    run: echo "VERSION=1.0" >> $GITHUB_ENV
```

---

## with 传参

**基本用法:给 Action 传参**
`with: <键>: <值>`

```yaml
- uses: actions/checkout@v4
  with:
    ref: develop
    submodules: true

- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7
```

---

## 权限与并发

**基本用法:设置权限**
`permissions:`

```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
```

---

**基本用法:并发控制**
`concurrency:`

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

---