# GitHub Actions 复用工作流速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 可调用工作流

**基本用法:定义可复用工作流**
`on: workflow_call` (`.github/workflows/reusable.yml`)

```yaml
name: Reusable Build

on:
  workflow_call:
    # 输入参数
    inputs:
      environment:
        type: string
        required: true
      debug:
        type: boolean
        default: false
    # 密钥参数
    secrets:
      DEPLOY_KEY:
        required: true

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "Building for ${{ inputs.environment }}"
      - if: ${{ inputs.debug }}
        run: echo "Debug mode"
      - run: deploy.sh ${{ secrets.DEPLOY_KEY }}
```

---

## 调用工作流

**基本用法:同一仓库内调用**
`uses: ./.github/workflows/<文件>`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/reusable.yml
    with:
      environment: production
      debug: true
    secrets:
      DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
```

---

**基本用法:跨仓库调用**
`uses: <owner>/<repo>/.github/workflows/<文件>@<引用>`

```yaml
jobs:
  call-external:
    uses: org/shared-workflows/.github/workflows/build.yml@main
    with:
      environment: staging
    secrets: inherit
```

---

**基本用法:传递全部密钥**
`secrets: inherit`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/deploy.yml
    with:
      env: production
    secrets: inherit
```

---

## 串联与并联

**基本用法:依赖可调用工作流**
`needs:`

```yaml
jobs:
  call-build:
    uses: ./.github/workflows/build.yml
  call-deploy:
    needs: call-build
    uses: ./.github/workflows/deploy.yml
    secrets: inherit
```

---