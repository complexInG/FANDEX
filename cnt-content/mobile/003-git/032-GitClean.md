# git clean 清理命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 预演与清理

**基本用法:预览将删除的文件**
`git clean -n`

```bash
# 干跑模式,只显示不删除
git clean -n
```

---

**基本用法:删除未跟踪文件**
`git clean -f`

```bash
# 强制删除未跟踪文件
git clean -f

# 删除未跟踪目录
git clean -fd

# 同时删除被忽略的文件
git clean -fdx
```

---

## 选择性清理

**基本用法:限定路径**
`git clean -f <路径>`

```bash
# 仅清理指定目录
git clean -f build/

# 排除指定模式
git clean -fd -e "*.log"
```

---

**基本用法:交互式确认**
`git clean -i`

```bash
# 交互式逐个确认删除
git clean -id
```

---

## 常见组合

**基本用法:彻底清理工作区**
`git clean -fdx`

```bash
# 删除所有未跟踪文件、目录与被忽略文件
git clean -fdx

# 配合重置回到干净状态
git reset --hard && git clean -fdx
```

---

## 与 reset 配合回滚

**基本用法:彻底放弃所有改动**
`git reset --hard && git clean -fd`

```bash
# 已跟踪改动用 reset,未跟踪文件用 clean
git reset --hard origin/main
git clean -fd
```

---