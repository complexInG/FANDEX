# git bundle 打包命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 bundle

**基本用法:打包整个仓库**
`git bundle create <文件> <引用>`

```bash
# 打包所有分支与标签
git bundle create repo.bundle --all

# 仅打包指定分支
git bundle create feature.bundle feature

# 打包指定区间提交
git bundle create diff.bundle main..feature
```

---

**基本用法:打包指定范围**
`git bundle create <文件> <旧提交>..<新提交>`

```bash
# 打包自上次同步以来的提交
git bundle create updates.bundle origin/main..main

# 打包最近 7 天的提交
git bundle create week.bundle --since="7 days ago" main
```

---

## 校验 bundle

**基本用法:校验 bundle 可用性**
`git bundle verify <文件>`

```bash
# 检查 bundle 是否包含所需引用
git bundle verify repo.bundle
```

---

**基本用法:查看 bundle 包含的引用**
`git bundle list-heads <文件>`

```bash
# 列出 bundle 中的所有分支头
git bundle list-heads repo.bundle
```

---

## 从 bundle 恢复

**基本用法:从 bundle 克隆**
`git clone <文件> <目录>`

```bash
# 从 bundle 克隆新仓库(离线传输)
git clone repo.bundle my-project
```

---

**基本用法:从 bundle 拉取**
`git fetch <文件> <引用>`

```bash
# 把 bundle 当作远程拉取
git fetch repo.bundle main:incoming-main
```

---