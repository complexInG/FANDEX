# gitattributes 与 gitignore 速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## gitattributes 文件属性

**基本用法:指定换行符处理**
`<模式> <属性>`

```bash
# 创建 .gitattributes 文件
# 统一为 LF 换行符
* text=auto eol=lf

# Windows 文件保留 CRLF
*.bat text eol=crlf

# 二进制文件不做换行处理
*.png binary
```

---

**基本用法:指定合并策略**
`<模式> merge=<策略>`

```bash
# 锁定文件保留己方版本
package-lock.json merge=ours

# 指定 diff 算法
*.c diff=cpp
```

---

**基本用法:导出时忽略**
`<模式> export-ignore`

```bash
# 归档时排除测试文件
tests/ export-ignore
*.spec.js export-ignore
```

---

**基本用法:LFS 跟踪大文件**
`<模式> filter=lfs`

```bash
# 用 git-lfs 跟踪大文件
*.psd filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs
```

---

**基本用法:语言统计**
`<模式> linguist-language=<语言>`

```bash
# 指定 GitHub 语言识别
*.h linguist-language=cpp
docs/* linguist-documentation
vendor/* linguist-vendored
```

---

## gitignore 忽略规则

**基本用法:忽略文件**
`<模式>`

```bash
# 创建 .gitignore
# 忽略所有 .log 文件
*.log

# 忽略整个目录
node_modules/
dist/

# 但不忽略特定文件
!important.log

# 忽略某目录下除某文件外
temp/*
!temp/keep.md
```

---

**基本用法:全局忽略**
`git config --global core.excludesfile <文件>`

```bash
# 设置全局忽略文件
git config --global core.excludesfile ~/.gitignore_global
```

---

**基本用法:已跟踪文件停止跟踪**
`git rm --cached <文件>`

```bash
# 从仓库移除但保留本地文件
git rm --cached .env
git commit -m "stop tracking .env"
```

---

## 检查忽略原因

**基本用法:查看为何被忽略**
`git check-ignore -v <文件>`

```bash
# 显示是哪条规则忽略了该文件
git check-ignore -v secrets.key
```

---