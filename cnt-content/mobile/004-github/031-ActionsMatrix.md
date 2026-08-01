# GitHub Actions 矩阵策略速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础矩阵

**基本用法:定义矩阵**
`strategy.matrix`

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [16, 18, 20]
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

---

## 矩阵组合与排除

**基本用法:排除特定组合**
`strategy.matrix.exclude`

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [18, 20]
    exclude:
      # 跳过 Windows + Node18
      - os: windows-latest
        node: 18
```

---

**基本用法:额外包含组合**
`strategy.matrix.include`

```yaml
strategy:
  matrix:
    node: [18, 20]
    include:
      # 给 node 20 额外加一个变量
      - node: 20
        experimental: true
      # 追加一个完全独立的组合
      - node: 22
        os: ubuntu-latest
```

---

## 失败策略

**基本用法:控制失败行为**
`strategy:`

```yaml
strategy:
  fail-fast: false      # 一个失败不取消其他
  max-parallel: 4       # 最大并行数
  matrix:
    node: [16, 18, 20]
```

---

## 动态矩阵

**基本用法:从 JSON 输出动态生成**
`strategy.matrix: ${{ fromJSON(...) }}`

```yaml
jobs:
  dynamic:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: echo "matrix=[\"a\",\"b\",\"c\"]" >> $GITHUB_OUTPUT

  use:
    needs: dynamic
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: ${{ fromJSON(needs.dynamic.outputs.matrix) }}
    steps:
      - run: echo ${{ matrix.target }}
```

---