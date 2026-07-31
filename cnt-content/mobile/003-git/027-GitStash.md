# git stash 暂存命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础暂存

**基本用法:暂存当前改动**
`git stash [push]`

```bash
# 暂存已跟踪文件的改动(含暂存区与工作区)
git stash

# 添加描述信息
git stash push -m "WIP: 登录功能未完成"

# 仅暂存已暂存内容
git stash --keep-index
```

---

**基本用法:暂存含未跟踪文件**
`git stash -u`

```bash
# 包含未跟踪文件(untracked)
git stash -u

# 包含忽略文件
git stash -a
```

---

## 查看与恢复

**基本用法:查看暂存列表**
`git stash list`

```bash
# 列出所有 stash
git stash list

# 查看某个 stash 的内容差异
git stash show stash@{0}

# 查看完整差异
git stash show -p stash@{1}
```

---

**基本用法:恢复暂存**
`git stash pop [stash@{N}]`

```bash
# 恢复最近 stash 并删除
git stash pop

# 恢复指定 stash 并删除
git stash pop stash@{2}

# 恢复但保留 stash
git stash apply stash@{0}
```

---

## 管理暂存

**基本用法:删除暂存**
`git stash drop <stash@{N}>`

```bash
# 删除指定 stash
git stash drop stash@{1}

# 清空所有 stash
git stash clear
```

---

**基本用法:从 stash 创建分支**
`git stash branch <分支名> [stash@{N}]`

```bash
# 基于 stash 创建并切换分支
git stash branch hotfix-branch stash@{0}
```

---

## 局部暂存

**基本用法:交互式暂存**
`git stash -p`

```bash
# 逐块选择暂存内容
git stash -p
```

---