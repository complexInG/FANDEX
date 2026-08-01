# gh extension 扩展命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 安装扩展

**基本用法:安装扩展**
`gh extension install <仓库>`

```bash
# 安装社区扩展
gh extension install dlvhdr/gh-dash

# 安装特定版本
gh extension install dlvhdr/gh-dash --pin v2.0.0
```

---

**基本用法:搜索扩展**
`gh extension search <关键词>`

```bash
# 搜索相关扩展
gh extension search notify
```

---

## 管理扩展

**基本用法:列出扩展**
`gh extension list`

```bash
# 查看已安装扩展
gh extension list
```

---

**基本用法:升级扩展**
`gh extension upgrade`

```bash
# 升级所有扩展
gh extension upgrade --all

# 升级指定扩展
gh extension upgrade gh-dash
```

---

**基本用法:移除扩展**
`gh extension remove <名称>`

```bash
# 卸载扩展
gh extension remove gh-dash
```

---

## 创建扩展

**基本用法:创建扩展脚手架**
`gh extension create <名称>`

```bash
# 创建新扩展(含脚手架)
gh extension create my-ext

# 创建预编译扩展(Go)
gh extension create my-ext --precompiled=go
```

---

**基本用法:本地开发扩展**
`gh extension install <路径>`

```bash
# 以本地目录方式安装用于开发
gh extension install .
```

---

## 浏览扩展

**基本用法:在浏览器打开**
`gh extension browse <名称>`

```bash
# 打开扩展仓库主页
gh extension browse gh-dash
```

---