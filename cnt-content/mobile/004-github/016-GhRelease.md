# gh release 发布命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建发布

**基本用法:创建 release**
`gh release create <标签> [文件...]`

```bash
# 基于标签创建发布
gh release create v1.0.0 --title "v1.0.0" --notes "首次正式发布"

# 自动生成更新日志
gh release create v1.0.0 --generate-notes

# 上传构建产物
gh release create v1.0.0 ./dist/app.zip ./dist/app.tar.gz

# 标记为预发布
gh release create v1.0.0 --prerelease --notes "测试版本"

# 指定目标分支
gh release create v1.0.0 --target main --notes "发布"
```

---

## 查看发布

**基本用法:列出所有 release**
`gh release list`

```bash
# 列出当前仓库的发布
gh release list

# 限制条数
gh release list --limit 5
```

---

**基本用法:查看某个 release 详情**
`gh release view <标签>`

```bash
# 查看指定发布详情
gh release view v1.0.0

# 在浏览器中打开
gh release view v1.0.0 --web
```

---

## 下载与上传

**基本用法:下载 release 资源**
`gh release download <标签>`

```bash
# 下载所有资源到当前目录
gh release download v1.0.0

# 下载指定文件
gh release download v1.0.0 --pattern "*.zip"

# 下载到指定目录
gh release download v1.0.0 --dir ./downloads
```

---

**基本用法:补充上传资源**
`gh release upload <标签> <文件>`

```bash
# 给已有 release 追加文件
gh release upload v1.0.0 ./build/app.exe

# 删除已存在的同名文件后上传
gh release upload v1.0.0 ./app.zip --clobber
```

---

## 编辑与删除

**基本用法:编辑 release**
`gh release edit <标签>`

```bash
# 修改标题与说明
gh release edit v1.0.0 --title "v1.0.0 正式版" --notes "更新说明"

# 转为草稿
gh release edit v1.0.0 --draft
```

---

**基本用法:删除 release**
`gh release delete <标签>`

```bash
# 删除发布(不影响标签)
gh release delete v1.0.0 --yes

# 同时删除标签
gh release delete v1.0.0 --cleanup-tag
```

---