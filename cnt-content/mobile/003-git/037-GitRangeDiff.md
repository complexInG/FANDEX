# git range-diff 范围对比命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 对比提交范围

**基本用法:对比两段提交序列**
`git range-diff <旧基准>..<旧终点> <新基准>..<新终点>`

```bash
# 对比重排前后的分支提交
git range-diff main..old-feature main..new-feature

# 简写:用旧 tip 与新 tip 对比同一基准
git range-diff main...feature@{1} main...feature
```

---

**基本用法:rebase 前后对比**
`git range-diff <upstream> <分支>@{1} <分支>`

```bash
# 查看上次 rebase 后提交的变化
git range-diff main feature@{1} feature
```

---

## 创建与对比选项

**基本用法:控制输出**
`git range-diff --creation-factor=<百分比>`

```bash
# 调整视为新增的阈值(默认 60%)
git range-diff --creation-factor=80 main..old main..new

# 双向显示
git range-diff --dual-color main..old main..new
```

---

## 实战场景

**基本用法:检查 cherry-pick 后差异**
`git range-diff`

```bash
# 对比 cherry-pick 前后的提交差异
git range-diff main..original main..cherry-picked
```

---