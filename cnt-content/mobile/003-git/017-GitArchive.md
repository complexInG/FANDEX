# Git archive 归档导出

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：导出 tar 归档**
`git archive --format=tar <提交> -o <文件>`
```bash
# 将 HEAD 导出为 tar 文件
git archive --format=tar HEAD -o project.tar
```

---

**基本写法：导出 zip 归档**
`git archive --format=zip <提交> -o <文件>`
```bash
# 将 HEAD 导出为 zip 文件
git archive --format=zip HEAD -o project.zip
```

---

**基本写法：根据扩展名自动识别格式**
`git archive <提交> -o <文件>`
```bash
# 通过 .tar.gz 扩展名自动选格式与压缩
git archive HEAD -o project.tar.gz
```

---

## 指定内容范围

**基本写法：导出指定路径**
`git archive <提交> <路径>`
```bash
# 仅导出 src 目录内容
git archive HEAD src/ -o src.tar
```

---

**基本写法：导出多个路径**
`git archive <提交> <路径1> <路径2>`
```bash
# 导出 src 与 docs 目录
git archive HEAD src/ docs/ -o bundle.tar
```

---

**基本写法：排除指定路径**
`git archive <提交> ':(exclude)<路径>'`
```bash
# 排除 tests 目录
git archive HEAD ':(exclude)tests/' -o release.tar
```

---

**基本写法：排除多个路径**
`git archive <提交> ':(exclude)<路径1>' ':(exclude)<路径2>'`
```bash
# 同时排除 tests 与 node_modules
git archive HEAD ':(exclude)tests/' ':(exclude)node_modules/' -o release.tar
```

---

## 添加前缀目录

**基本写法：导出时添加统一前缀**
`git archive --prefix=<前缀>/ <提交>`
```bash
# 所有文件前添加 project-v1.0/ 目录
git archive --prefix=project-v1.0/ HEAD -o release.tar.gz
```

---

**基本写法：路径级别前缀**
`git archive --prefix=<前缀> <提交> <路径>`
```bash
# 将 src 内容放到 release/src/ 下
git archive --prefix=release/ HEAD src/ -o bundle.tar
```

---

## 指定分支标签

**基本写法：导出指定标签版本**
`git archive <标签> -o <文件>`
```bash
# 导出 v1.2.0 标签版本
git archive v1.2.0 -o release-1.2.0.tar.gz
```

---

**基本写法：导出指定分支**
`git archive <分支> -o <文件>`
```bash
# 导出 release 分支内容
git archive release -o release.tar
```

---

**基本写法：导出某次提交**
`git archive <提交哈希> -o <文件>`
```bash
# 导出指定提交的快照
git archive abc1234 -o snapshot.tar
```

---

## 提交信息

**基本写法：将提交信息加入归档**
`git archive --format=tar <提交> | tar -O -xf - <文件>`
```bash
# 从归档中提取特定文件内容
git archive --format=tar HEAD | tar -O -xf - README.md
```

---

**基本写法：附加版本说明**
`git archive --add-file <文件> <提交>`
```bash
# 归档时追加本地文件
git archive --add-file VERSION.txt HEAD -o release.tar
```

---

## 压缩选项

**基本写法：指定压缩级别**
`git archive --format=tar.gz -<级别> <提交>`
```bash
# 使用最大压缩级别
git archive --format=tar.gz -9 HEAD -o release.tar.gz
```

---

**基本写法：输出到标准输出**
`git archive <提交>`
```bash
# 直接输出到 stdout 供管道使用
git archive HEAD | tar -x -C /tmp/release
```

---

## 远程仓库归档

**基本写法：从远程仓库归档**
`git archive --remote=<仓库URL> <分支>`
```bash
# 直接从远程仓库归档（需服务器支持）
git archive --remote=https://git.example.com/repo.git HEAD -o remote.tar
```

---

**基本写法：远程归档带前缀**
`git archive --remote=<URL> --prefix=<前缀>/ <分支>`
```bash
# 远程归档并添加前缀
git archive --remote=https://git.example.com/repo.git --prefix=repo/ main -o repo.tar
```

---

## 实用场景

**基本写法：导出干净的发布包**
`git archive --format=tar.gz --prefix=<项目>-<版本>/ <标签> -o <文件>`
```bash
# 制作标准源码发布包
git archive --format=tar.gz --prefix=myapp-1.0.0/ v1.0.0 -o myapp-1.0.0.tar.gz
```

---

**基本写法：导出并校验**
`git archive <提交> -o <文件> && sha256sum <文件>`
```bash
# 归档并生成校验和
git archive v1.0.0 -o release.tar.gz && sha256sum release.tar.gz
```

---

**基本写法：归档排除 git 元数据**
`git archive <提交> | tar -t`
```bash
# 列出归档内容验证
git archive HEAD | tar -t
```
