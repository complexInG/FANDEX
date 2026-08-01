# GitHub Actions 工作流配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

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

## 作业配置

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
