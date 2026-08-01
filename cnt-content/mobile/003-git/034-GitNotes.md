# git notes 备注命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 添加备注

**基本用法:为提交添加备注**
`git notes add -m "<内容>" <提交>`

```bash
# 给指定提交添加备注(不修改原提交)
git notes add -m "代码审查通过" a1b2c3d

# 给最新提交添加备注
git notes add -m "上线前补充测试"
```

---

**基本用法:追加备注**
`git notes append -m "<内容>" <提交>`

```bash
# 在已有备注后追加
git notes append -m "补充说明:已修复" a1b2c3d
```

---

## 查看备注

**基本用法:查看某提交备注**
`git notes show <提交>`

```bash
# 查看指定提交的备注
git notes show a1b2c3d

# 在 log 中显示备注
git log --show-notes
```

---

**基本用法:列出所有有备注的提交**
`git notes list`

```bash
# 列出所有备注及其对应提交
git notes list

# 列出某提交树上的备注
git notes list a1b2c3d
```

---

## 管理备注

**基本用法:编辑备注**
`git notes edit <提交>`

```bash
# 调用编辑器修改备注
git notes edit a1b2c3d
```

---

**基本用法:复制备注**
`git notes copy <源提交> <目标提交>`

```bash
# 把备注从 A 复制到 B
git notes copy a1b2c3d d4e5f6g
```

---

**基本用法:删除备注**
`git notes remove <提交>`

```bash
# 删除指定提交的备注
git notes remove a1b2c3d

# 删除所有备注
git notes prune
```

---

## 共享备注

**基本用法:推送备注到远程**
`git push origin refs/notes/commits`

```bash
# 推送备注到远程仓库
git push origin refs/notes/commits

# 拉取他人备注
git fetch origin refs/notes/*:refs/notes/*
```

---