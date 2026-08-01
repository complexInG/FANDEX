# git mv 文件移动命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 重命名文件

**基本用法:重命名**
`git mv <源文件> <目标文件>`

```bash
# 重命名文件(自动记录为重命名)
git mv old_name.js new_name.js

# 移动文件到新目录
git mv src/utils.js src/helpers/utils.js
```

---

**基本用法:移动目录**
`git mv <源目录> <目标目录>`

```bash
# 移动整个目录
git mv old_dir/ new_dir/

# 批量移动目录下所有文件
git mv old_dir/* new_dir/
```

---

## 强制覆盖

**基本用法:覆盖已存在文件**
`git mv -f <源> <目标>`

```bash
# 强制覆盖目标文件
git mv -f temp.js existing.js
```

---

## 干跑预览

**基本用法:预演移动**
`git mv -n <源> <目标>`

```bash
# 显示将执行的移动但不实际执行
git mv -n old.js new.js
```

---

## 与原生 mv 的区别

**基本用法:原生移动后修复**
`mv <源> <目标> && git add -A`

```bash
# 用系统命令移动后,git 自动识别重命名
mv old.js new.js
git add -A
git status
```

---