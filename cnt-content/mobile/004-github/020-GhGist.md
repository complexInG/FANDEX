# gh gist 代码片段命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建 Gist

**基本用法:创建公开 gist**
`gh gist create <文件>`

```bash
# 从文件创建公开 gist
gh gist create snippet.js

# 创建私密 gist(不可搜索但仍可访问)
gh gist create snippet.js --secret

# 从标准输入创建
echo "console.log(1)" | gh gist create -f script.js

# 添加描述
gh gist create note.md --desc "配置笔记"
```

---

## 查看 Gist

**基本用法:列出 gist**
`gh gist list`

```bash
# 列出自己的 gist
gh gist list

# 限制条数
gh gist list --limit 20
```

---

**基本用法:查看 gist 内容**
`gh gist view <ID>`

```bash
# 查看 gist 内容
gh gist view abc123

# 查看原始内容
gh gist view abc123 --raw

# 在浏览器打开
gh gist view abc123 --web
```

---

## 编辑与克隆

**基本用法:编辑 gist**
`gh gist edit <ID>`

```bash
# 编辑 gist 内容
gh gist edit abc123

# 用指定文件替换
gh gist edit abc123 new_content.js
```

---

**基本用法:克隆 gist**
`gh gist clone <ID>`

```bash
# 把 gist 克隆为本地仓库
gh gist clone abc123 my-snippet
```

---

## 删除与重命名

**基本用法:删除 gist**
`gh gist delete <ID>`

```bash
# 删除 gist
gh gist delete abc123 --yes
```

---

**基本用法:重命名文件**
`gh gist rename <ID> <旧名> <新名>`

```bash
# 重命名 gist 中的文件
gh gist rename abc123 old.js new.js
```

---