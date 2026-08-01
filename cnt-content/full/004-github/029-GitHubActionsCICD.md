---
order: 90
tags:
  - github
  - devops
difficulty: intermediate
title: 'GitHub Actions 与 CI/CD'
module: github
category: 'GitHub Advanced'
description: 'GitHub Actions workflow 语法、市场使用、CI/CD 示例（Node/Java/Python）。'
author: Anonymous
related:
  - github/PullRequest完整协作流程
  - github/GitHubPages多站点方案
  - github/Actions触发器
  - github/常见问题排查
prerequisites:
  - github/GitHub概述
updated: '2026-08-01'
---

# GitHub Actions 工作流配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 1. 背景

**GitHub Actions** 是内置于仓库的 **CI/CD（持续集成/持续交付）** 引擎：用 **YAML** 描述 **workflow（工作流）**，在 **runner（运行器）** 上执行 **job（任务）**。**GitHub Marketplace** 提供可复用的 **Action（动作）** 封装常见步骤。
核心概念：**on** 触发条件、**jobs** 并行或依赖、**steps** 顺序执行、**${{ secrets.XXX }}** 读取密钥。

## 2. GitHub Actions 核心概念

### 2.1 工作流（Workflow）

工作流是一个可配置的自动化流程，由一个或多个任务（jobs）组成，定义在 `.github/workflows/` 目录下的 YAML 文件中。

### 2.2 任务（Job）

任务是工作流中的一个独立单元，包含一系列步骤（steps）。任务默认并行执行，但可以通过 `needs` 关键字定义依赖关系。

### 2.3 步骤（Step）

步骤是任务中的一个操作，可以是：

- 使用市场中的 Action（`uses`）
- 执行 shell 命令（`run`）

### 2.4 运行器（Runner）

运行器是执行工作流的服务器，可以是：

- GitHub 托管的运行器（如 `ubuntu-latest`、`windows-latest`、`macos-latest`）
- 自托管运行器（自己搭建的服务器）

### 2.5 动作（Action）

动作是可复用的代码单元，封装了常见的步骤，可在 GitHub Marketplace 中找到。

## 3. 工作流配置详解

### 3.1 触发条件（on）

```yaml
 # 基本触发条件
 on:
  push:
  branches: [main, develop]
  paths-ignore: ['README.md', 'docs/**']
  pull_request:
  branches: [main]
  # 定时触发
  schedule:
  - cron: '0 0 * * *' # 每天 UTC 时间 00:00 触发
  # 手动触发
  workflow_dispatch:
  inputs:
  environment:
  description: '环境'
  required:
  default: 'staging'
  # 其他工作流触发
  workflow_run:
  workflows: ['Build']
  types: [completed]
```

### 3.2 任务配置（jobs）

```yaml
 jobs:
  # 任务名称
  build:
  # 运行器环境
  runs-on: ubuntu-latest
  # 环境变量
  env:
  NODE_ENV: production
  # 矩阵策略
  strategy:
  matrix:
  node-version: [18.x, 20.x]
  os: [ubuntu-latest, windows-latest]
  # 快速失败
  fail-fast:
  # 任务依赖
  needs: [lint, test]
  # 步骤
  steps:
  - name: Checkout code
  uses: actions/checkout@v4
  with:
  fetch-depth: 0 # 完整克隆，包括标签
  - name: Setup Node.js
  uses: actions/setup-node@v4
  with:
  node-version: ${{ matrix.node-version }}
  cache: npm
  - name: Install dependencies
  run: npm ci
  - name: Build
  run: npm run build
```

### 3.3 步骤配置（steps）

```yaml
 steps:
  # 使用市场中的 Action
  - name: Checkout code
  uses: actions/checkout@v4
  # 带参数的 Action
  - name: Setup Python
  uses: actions/setup-python@v5
  with:
  python-version: '3.11'
  # 执行 shell 命令
  - name: Install dependencies
  run: |
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  # 条件执行
  - name: Deploy to production
  if: github.ref == 'refs/heads/main'
  run: ./deploy.sh
  # 上传 artifact
  - name: Upload build artifacts
  uses: actions/upload-artifact@v4
  with:
  name: build
  path: dist/
```

## 4. GitHub Marketplace 指南

### 4.1 查找 Action

1. 访问 [GitHub Marketplace](https://github.com/marketplace?type=actions)
2. 使用搜索功能找到需要的 Action
3. 查看 Action 的文档和使用示例

### 4.2 常用 Action

- **actions/checkout**：检出代码仓库
- **actions/setup-node**：设置 Node.js 环境
- **actions/setup-java**：设置 Java 环境
- **actions/setup-python**：设置 Python 环境
- **actions/upload-artifact**：上传构建产物
- **actions/download-artifact**：下载构建产物
- **actions/cache**：缓存依赖
- **peaceiris/actions-gh-pages**：部署到 GitHub Pages
- **docker/login-action**：登录 Docker 仓库
- **docker/build-push-action**：构建和推送 Docker 镜像

### 4.3 自定义 Action

可以创建自己的 Action：

1. 在仓库中创建 `action.yml` 文件
2. 定义 Action 的输入、输出和运行环境
3. 发布到 GitHub Marketplace

## 5. 完整 CI/CD 示例

### 5.1 Node.js 项目完整 CI/CD

```yaml
 name: Node.js CI/CD
 on:
  push:
  branches: [main, develop]
  pull_request:
  branches: [main, develop]
 jobs:
  lint:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
  with:
  node-version: '20.x'
  cache: npm
  - run: npm ci
  - run: npm run lint
  test:
  runs-on: ubuntu-latest
  strategy:
  matrix:
  node-version: [18.x, 20.x]
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
  with:
  node-version: ${{ matrix.node-version }}
  cache: npm
  - run: npm ci
  - run: npm test
  build:
  runs-on: ubuntu-latest
  needs: [lint, test]
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
  with:
  node-version: '20.x'
  cache: npm
  - run: npm ci
  - run: npm run build
  - uses: actions/upload-artifact@v4
  with:
  name: build
  path: dist/
  deploy:
  runs-on: ubuntu-latest
  needs: build
  if: github.ref == 'refs/heads/main'
  steps:
  - uses: actions/checkout@v4
  - uses: actions/download-artifact@v4
  with:
  name: build
  path: dist/
  - name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v4
  with:
  github_token: ${{ secrets.GITHUB_TOKEN }}
  publish_dir: ./dist
```

### 5.2 Java 项目完整 CI/CD

```yaml
 name: Java CI/CD
 on:
  push:
  branches: [main, develop]
  pull_request:
  branches: [main, develop]
 jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-java@v4
  with:
  distribution: temurin
  java-version: '17'
  cache: maven
  - name: Build with Maven
  run: mvn -B package --file pom.xml
  - uses: actions/upload-artifact@v4
  with:
  name: jar
  path: target/*.jar
  deploy:
  runs-on: ubuntu-latest
  needs: build
  if: github.ref == 'refs/heads/main'
  steps:
  - uses: actions/download-artifact@v4
  with:
  name: jar
  path: target/
  - name: Deploy to server
  run: |
  # 部署脚本
  echo "Deploying to production server"
  # scp target/*.jar user@server:/path/to/deploy/
```

### 5.3 Python 项目完整 CI/CD

```yaml
 name: Python CI/CD
 on:
  push:
  branches: [main, develop]
  pull_request:
  branches: [main, develop]
 jobs:
  lint:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
  with:
  python-version: '3.11'
  - run: |
  python -m pip install --upgrade pip
  pip install flake8
  flake8 .
  test:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
  with:
  python-version: '3.11'
  - run: |
  python -m pip install --upgrade pip
  pip install pytest
  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
  pytest
  deploy:
  runs-on: ubuntu-latest
  needs: [lint, test]
  if: github.ref == 'refs/heads/main'
  steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
  with:
  python-version: '3.11'
  - run: |
  python -m pip install --upgrade pip
  pip install setuptools wheel twine
  python setup.py sdist bdist_wheel
  twine upload --repository pypi dist/* -u ${{ secrets.PYPI_USERNAME }} -p ${{ secrets.PYPI_PASSWORD }}
```

## 6. 环境变量与密钥管理

### 6.1 环境变量

```yaml
# 工作流级环境变量
env:
  NODE_ENV: production
  API_URL: https://api.example.com
jobs:
  build:
  # 任务级环境变量
  env:
  BUILD_VERSION: 1.0.0
  steps:
    - name: Print environment variables
  run: |
  echo "NODE_ENV: $NODE_ENV"
  echo "API_URL: $API_URL"
  echo "BUILD_VERSION: $BUILD_VERSION"
  # 使用 GitHub 上下文
  echo "Repository: ${{ github.repository }}"
  echo "Branch: ${{ github.ref }}"
```

### 6.2 密钥管理

1. **Repository secrets**：在仓库的 **Settings → Secrets and variables → Actions** 中设置
2. **Environment secrets**：在环境的设置中设置，更安全
3. **使用密钥**：

```yaml
 steps:
  - name: Deploy
  run: ./deploy.sh
  env:
  API_KEY: ${{ secrets.API_KEY }}
  DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

## 7. 常见问题与解决方案

### 7.1 构建失败

#### 7.1.1 依赖安装失败

- **问题**：依赖安装超时或失败
- **解决方案**：

1.  使用缓存减少依赖安装时间
2.  检查网络连接
3.  确认依赖源是否可用
4.  增加超时时间

#### 7.1.2 测试失败

- **问题**：测试用例失败
- **解决方案**：

1.  查看测试日志，了解失败原因
2.  修复代码中的问题
3.  确保测试环境与开发环境一致

### 7.2 性能问题

#### 7.2.1 构建时间过长

- **问题**：构建时间超过限制或影响开发效率
- **解决方案**：

1.  使用缓存
2.  并行执行任务
3.  优化构建脚本
4.  使用自托管运行器

#### 7.2.2 缓存失效

- **问题**：依赖变更后缓存未更新
- **解决方案**：

1.  使用动态缓存键
2.  定期清理缓存
3.  依赖变更时更新缓存键

### 7.3 权限问题

#### 7.3.1 密钥权限不足

- **问题**：构建过程中无法访问密钥
- **解决方案**：

1.  确认密钥已正确设置
2.  检查 workflow 权限设置
3.  确保密钥名称正确

#### 7.3.2 访问外部服务失败

- **问题**：无法访问外部 API 或服务
- **解决方案**：

1.  检查网络连接
2.  确认 API 密钥有效
3.  检查外部服务状态

## 8. 最佳实践

### 8.1 工作流设计

- **模块化**：将不同功能拆分为多个工作流
- **并行执行**：利用矩阵策略和并行任务提高效率
- **依赖管理**：使用 `needs` 明确任务依赖关系
- **条件执行**：使用 `if` 条件控制任务执行

### 8.2 安全性

- **密钥管理**：使用 Repository secrets 或 Environment secrets
- **权限控制**：最小化 workflow 权限
- **代码扫描**：集成 CodeQL 等代码扫描工具
- **安全依赖**：使用 Dependabot 自动更新依赖

### 8.3 可维护性

- **版本固定**：固定 Action 版本，避免意外变更
- **注释**：为复杂工作流添加注释
- **文档**：记录工作流的用途和维护指南
- **测试**：测试工作流的各个部分

### 8.4 性能优化

- **缓存**：缓存依赖和构建产物
- **并行**：并行执行测试和构建
- **最小化**：只执行必要的步骤
- **自托管运行器**：对于大型项目使用自托管运行器

## 9. 实际应用案例

### 9.1 开源项目案例

#### 9.1.1 案例描述

- **项目**：一个前端库
- **需求**：自动测试、构建和发布

#### 9.1.2 实现

1. **测试**：在 PR 时运行单元测试和集成测试
2. **构建**：合并到 main 分支时构建
3. **发布**：打标签时自动发布到 npm

### 9.2 企业项目案例

#### 9.2.1 案例描述

- **项目**：企业内部应用
- **需求**：自动测试、构建、部署到多环境

#### 9.2.2 实现

1. **测试**：PR 时运行测试
2. **构建**：合并到 develop 分支时构建
3. **部署**：

- 合并到 develop 分支：部署到开发环境
- 合并到 main 分支：部署到测试环境
- 打标签：部署到生产环境

## 10. GitHub Pages 部署

### 10.1 启用 GitHub Pages

1. 进入仓库 **Settings** > **Pages**
2. 选择源分支（通常是 `gh-pages` 或 `main`）
3. 选择目录（通常是 `/` 或 `/docs`）
4. 点击 **Save**

### 10.2 自动部署到 GitHub Pages

```yaml
 name: Deploy to GitHub Pages
 on:
  push:
  branches: [ main ]
 jobs:
  deploy:
  runs-on: ubuntu-latest
  permissions:
  contents: write
  steps:
  - uses: actions/checkout@v4
  - name: Set up Node.js
  uses: actions/setup-node@v4
  with:
  node-version: 20
  cache: 'npm'
  - name: Install dependencies
  run: npm install
  - name: Build
  run: npm run build
  - name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v4
  with:
  github_token: ${{ secrets.GITHUB_TOKEN }}
  publish_dir: ./dist
```

### 10.3 使用 GitHub Actions 官方 Pages 部署

```yaml
 name: Deploy Pages
 on:
  push:
  branches: [ main ]
 permissions:
  contents: read
  pages: write
  id-token: write
 jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - uses: actions/checkout@v4
  - uses: actions/configure-pages@v5
  - uses: actions/upload-pages-artifact@v3
  with:
  path: ./dist
  deploy:
  needs: build
  runs-on: ubuntu-latest
  environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
  steps:
  - uses: actions/deploy-pages@v4
  id: deployment
```

## 11. 与其他 CI/CD 工具对比

| 工具           | 优势                                   | 劣势                 |
| -------------- | -------------------------------------- | -------------------- |
| GitHub Actions | 与 GitHub 集成紧密、易于配置、市场丰富 | 私有仓库有分钟数限制 |
| Jenkins        | 高度可定制、插件丰富、无限制           | 搭建和维护成本高     |
| GitLab CI/CD   | 与 GitLab 集成紧密、功能强大           | 学习曲线较陡         |
| CircleCI       | 速度快、配置简单、支持 Docker          | 价格较高             |
| Travis CI      | 配置简单、历史悠久                     | 功能相对有限         |

## 11. 延伸阅读

- [Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) <!-- nofollow -->
- [GitHub Actions documentation](https://docs.github.com/en/actions) <!-- nofollow -->
- [GitHub Marketplace](https://github.com/marketplace?type=actions) <!-- nofollow -->
- [Security hardening for GitHub Actions](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions) <!-- nofollow -->

## 工作流文件结构

**基本写法：工作流文件命名**
`.github/workflows/<名称>.yml`
```bash
# 工作流文件必须放在此目录下
mkdir -p .github/workflows
```

---

**基本写法：基本工作流定义**
`name: <工作流名称>`
```yaml
# 工作流名称
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Hello"
```

---

**基本写法：触发条件配置**
`on: <触发事件>`
```yaml
# push 时触发
on:
  push:
    branches: [ main, develop ]
```

---

**基本写法：多事件触发**
`on: [<事件1>, <事件2>]`
```yaml
# 多种事件触发工作流
on: [push, pull_request, workflow_dispatch]
```

---

**基本写法：手动触发**
`on: workflow_dispatch`
```yaml
# 允许手动触发工作流
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '部署环境'
        default: 'staging'
```

---

**基本写法：定时触发**
`on: schedule`
```yaml
# 每天凌晨 2 点执行（UTC 时间）
on:
  schedule:
    - cron: '0 2 * * *'
```

---

## 知识讲解与要点分析（原作业配置）

**基本写法：指定运行环境**
`runs-on: <操作系统>`
```yaml
# 在最新版 Ubuntu 上运行
runs-on: ubuntu-latest
```

---

**基本写法：多操作系统矩阵**
`strategy: matrix`
```yaml
# 在多个操作系统上运行测试
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
runs-on: ${{ matrix.os }}
```

---

**基本写法：多版本矩阵**
`strategy: matrix`
```yaml
# 在多个 Node.js 版本上测试
strategy:
  matrix:
    node-version: [18, 20, 22, 24]
```

---

**基本写法：失败时继续**
`strategy: fail-fast`
```yaml
# 矩阵中一个失败不取消其他
strategy:
  fail-fast: false
  max-parallel: 4
```

---

**基本写法：作业依赖关系**
`needs: <作业名>`
```yaml
# deploy 作业依赖 build 作业
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "build"
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "deploy"
```

---

## 步骤与动作

**基本写法：检出代码**
`uses: actions/checkout@v4`
```yaml
# 检出仓库代码到工作目录
steps:
  - uses: actions/checkout@v4
```

---

**基本写法：设置 Node.js 环境**
`uses: actions/setup-node@v4`
```yaml
# 配置 Node.js 运行环境
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: '22'
      cache: 'npm'
```

---

**基本写法：设置 Python 环境**
`uses: actions/setup-python@v5`
```yaml
# 配置 Python 运行环境
steps:
  - uses: actions/setup-python@v5
    with:
      python-version: '3.13'
```

---

**基本写法：设置 Java 环境**
`uses: actions/setup-java@v4`
```yaml
# 配置 JDK 环境
steps:
  - uses: actions/setup-java@v4
    with:
      distribution: 'temurin'
      java-version: '21'
```

---

**基本写法：运行命令**
`run: <命令>`
```yaml
# 执行 shell 命令
steps:
  - run: npm install
  - run: npm test
```

---

**基本写法：多行命令**
`run: |`
```yaml
# 执行多行命令
steps:
  - run: |
      npm install
      npm run build
      npm test
```

---

**基本写法：指定 shell 类型**
`shell: <shell>`
```yaml
# 指定使用 PowerShell 运行
steps:
  - run: Write-Host "Hello"
    shell: pwsh
```

---

## 环境变量与密钥

**基本写法：设置环境变量**
`env: <变量名>: <值>`
```yaml
# 设置工作流级环境变量
env:
  NODE_ENV: production
jobs:
  build:
    env:
      CI: true
```

---

**基本写法：使用密钥**
`secrets.<密钥名>`
```yaml
# 使用仓库配置的密钥
steps:
  - run: npm publish
    env:
      NODE_AUTH_TOKEN: ${{ secrets.NPM_TOKEN }}
```

---

**基本写法：步骤级环境变量**
`run: <命令> env: <变量>: <值>`
```yaml
# 仅在特定步骤设置环境变量
steps:
  - run: echo $SECRET_VALUE
    env:
      SECRET_VALUE: ${{ secrets.MY_SECRET }}
```

---

**基本写法：使用上下文变量**
`${{ <上下文> }}`
```yaml
# 使用 GitHub 上下文信息
steps:
  - run: echo "Branch is ${{ github.ref }}"
  - run: echo "Actor is ${{ github.actor }}"
```

---

## 缓存与产物

**基本写法：缓存依赖**
`uses: actions/cache@v4`
```yaml
# 缓存 npm 依赖加速构建
steps:
  - uses: actions/cache@v4
    with:
      path: ~/.npm
      key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

---

**基本写法：上传构建产物**
`uses: actions/upload-artifact@v4`
```yaml
# 上传构建结果
steps:
  - uses: actions/upload-artifact@v4
    with:
      name: build-output
      path: dist/
```

---

**基本写法：下载产物**
`uses: actions/download-artifact@v4`
```yaml
# 下载之前上传的产物
steps:
  - uses: actions/download-artifact@v4
    with:
      name: build-output
```

---

**基本写法：条件步骤**
`if: <条件>`
```yaml
# 仅在 main 分支执行
steps:
  - run: npm run deploy
    if: github.ref == 'refs/heads/main'
```

---

## gh CLI 管理工作流

**基本写法：查看工作流列表**
`gh workflow list`
```bash
# 列出仓库的所有工作流
gh workflow list
```

---

**基本写法：查看工作流详情**
`gh workflow view <工作流名>`
```bash
# 查看指定工作流的详情
gh workflow view CI
```

---

**基本写法：查看工作流文件**
`gh workflow view <工作流名> --yaml`
```bash
# 查看工作流的 YAML 内容
gh workflow view CI --yaml
```

---

**基本写法：手动触发工作流**
`gh workflow run <工作流>`
```bash
# 手动触发指定工作流
gh workflow run CI
```

---

**基本写法：指定分支触发**
`gh workflow run <工作流> --ref <分支>`
```bash
# 在指定分支上触发工作流
gh workflow run CI --ref develop
```

---

**基本写法：带参数触发**
`gh workflow run <工作流> -f <参数>=<值>`
```bash
# 传入参数触发工作流
gh workflow run deploy.yml -f environment=production
```

---

**基本写法：禁用工作流**
`gh workflow disable <工作流>`
```bash
# 禁用指定工作流
gh workflow disable CI
```

---

**基本写法：启用工作流**
`gh workflow enable <工作流>`
```bash
# 启用被禁用的工作流
gh workflow enable CI
```

---

## 运行记录管理

**基本写法：查看运行列表**
`gh run list`
```bash
# 列出工作流运行记录
gh run list
```

---

**基本写法：按工作流筛选**
`gh run list --workflow <工作流>`
```bash
# 查看指定工作流的运行记录
gh run list --workflow CI
```

---

**基本写法：按状态筛选**
`gh run list --status <状态>`
```bash
# 查看失败的运行记录
gh run list --status failure
```

---

**基本写法：限制返回数量**
`gh run list --limit <数量>`
```bash
# 限制返回的运行记录数量
gh run list --limit 10
```

---

**基本写法：查看运行详情**
`gh run view <运行ID>`
```bash
# 查看指定运行的详细信息
gh run view 123456
```

---

**基本写法：查看失败日志**
`gh run view <运行ID> --log-failed`
```bash
# 查看运行失败的日志
gh run view 123456 --log-failed
```

---

**基本写法：查看完整日志**
`gh run view <运行ID> --log`
```bash
# 查看运行的完整日志
gh run view 123456 --log
```

---

**基本写法：实时监控运行**
`gh run watch <运行ID>`
```bash
# 实时监控运行直到完成
gh run watch 123456
```

---

**基本写法：重新运行**
`gh run rerun <运行ID>`
```bash
# 重新运行指定的工作流
gh run rerun 123456
```

---

**基本写法：仅重跑失败的作业**
`gh run rerun <运行ID> --failed`
```bash
# 仅重新运行失败的作业
gh run rerun 123456 --failed
```

---

**基本写法：取消运行中的工作流**
`gh run cancel <运行ID>`
```bash
# 取消正在运行的工作流
gh run cancel 123456
```

---

**基本写法：删除运行记录**
`gh run delete <运行ID>`
```bash
# 删除指定的工作流运行记录
gh run delete 123456
```
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

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| GitHub 概述 | 001-GitHubOverview | 本文的前置基础 |
| 账户注册与双因素认证（2FA） | 002-AccountRegister2FA2FA | 本文的并列主题 |
| 仓库创建、克隆、归档、删除 | 003-RepositoryCreateCloneArchiveDelete | 本文的并列主题 |
| SSH 与 HTTPS 远程配置 | 004-SSHHTTPS | 本文的并列主题 |
| 协作开发规范 | 005-CollaborationDevelopmentStandard | 本文的并列主题 |
| README文件 | 006-READMEFile | 本文的并列主题 |
| 分支模型与分支保护规则 | 007-BranchModelBranchRule | 本文的并列主题 |
| Gitignore配置 | 008-GitignoreConfig | 本文的并列主题 |
| 开源许可证选择 | 009-OpenSourceLicense | 本文的并列主题 |
| 依赖安全选项 | 010-DependencySecurityOptions | 本文的安全延伸 |
| Fork工作流 | 011-ForkWorkflow | 本文的并列主题 |
| Projects看板 | 012-ProjectsBoard | 本文的并列主题 |
| Wikis | 013-Wikis | 本文的并列主题 |
| Discussions | 014-Discussions | 本文的并列主题 |
| GitHub-Copilot | 015-GitHubCopilot | 本文的并列主题 |
| Dependabot | 016-Dependabot | 本文的并列主题 |
| Issues 模板、标签与里程碑 | 017-IssuesTemplateTagMilestone | 本文的并列主题 |
| 密钥扫描 | 018-SecretScanning | 本文的并列主题 |
| CodeQL代码扫描 | 019-CodeQLCodeScanning | 本文的并列主题 |
| GitHub-CLI | 020-GitHubCLI | 本文的并列主题 |
| REST与GraphQL-API | 021-RESTGraphQLAPI | 本文的并列主题 |
| Webhooks | 022-Webhooks | 本文的并列主题 |
| GitHub-Packages | 023-GitHubPackages | 本文的并列主题 |
| Codespaces | 024-Codespaces | 本文的并列主题 |
| CODEOWNERS | 025-CODEOWNERS | 本文的并列主题 |
| 社区健康文件 | 026-CommunityHealthFile | 本文的并列主题 |
| Pull Request 完整协作流程 | 027-PullRequestCompleteCollaborationFlow | 本文的并列主题 |
| GitHub Pages 多站点方案 | 028-GitHubPagesMultiSolution | 本文的并列主题 |
| GitHub Actions 与 CI/CD | 029-GitHubActionsCICD | 本文自身 |
| Actions触发器 | 030-ActionsTrigger | 本文的并列主题 |
| 常见问题排查 | 031-FAQTroubleshoot | 本文的并列主题 |
| Actions矩阵构建 | 032-ActionsMatrixBuild | 本文的并列主题 |
| Actions缓存依赖 | 033-ActionsCacheDependency | 本文的并列主题 |
| Actions自托管运行器 | 034-ActionsSelfHostedRunner | 本文的并列主题 |
| Actions制品传递 | 035-ActionsArtifact | 本文的并列主题 |
| Actions环境部署 | 036-ActionsEnvironmentDeploy | 本文的前置基础 |
| GitHub 仓库初始化 | 037-GitRepoInit | 本文的并列主题 |
| GitHub 提交与推送 | 038-GitCommitPush | 本文的并列主题 |
| GitHub 拉取与获取 | 039-GitPullFetch | 本文的并列主题 |
| GitHub 合并与变基 | 040-GitMergeRebase | 本文的并列主题 |
| GitHub 冲突解决 | 041-GitConflictResolve | 本文的并列主题 |
| GitHub 标签管理 | 042-GitTagManage | 本文的并列主题 |
| GitHub 远程仓库管理 | 043-GitRemoteManage | 本文的并列主题 |
| GitHub 历史与日志 | 044-GitHistoryLog | 本文的并列主题 |
| GitHub 暂存与回退 | 045-GitStashReset | 本文的并列主题 |
| GitHub CLI 认证配置 | 046-GhCliAuth | 本文的并列主题 |
| GitHub CLI PR 管理 | 047-GhPrManage | 本文的并列主题 |
| GitHub CLI Issue 管理 | 048-GhIssueManage | 本文的并列主题 |
| GitHub CLI 仓库管理 | 049-GhRepoManage | 本文的并列主题 |
| gh release 发布命令速查手册 | 050-GhRelease | 本文的并列主题 |
| gh workflow 工作流命令速查手册 | 051-GhWorkflow | 本文的并列主题 |
| gh gist 代码片段命令速查手册 | 052-GhGist | 本文的并列主题 |
| gh extension 扩展命令速查手册 | 053-GhExtension | 本文的并列主题 |
| gh api 调用命令速查手册 | 054-GhApi | 本文的并列主题 |
| gh search 搜索命令速查手册 | 055-GhSearch | 本文的并列主题 |
| gh label 与 alias/config 命令速查手册 | 056-GhLabel | 本文的并列主题 |
| gh alias 与 config 命令速查手册 | 057-GhAliasConfig | 本文的并列主题 |
