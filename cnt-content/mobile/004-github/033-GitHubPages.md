# GitHub Pages 部署配置速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Actions 部署 Pages

**基本用法:部署静态站点**
`uses: actions/deploy-pages@v4`

```yaml
name: Deploy Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## gh-pages 分支方式

**基本用法:推送构建产物到 gh-pages**
`git push origin <子树>:gh-pages`

```bash
# 把 dist 子目录作为 gh-pages 分支根推送
git subtree push --prefix dist origin gh-pages

# 强制更新 gh-pages
git push origin `git subtree split --prefix dist`:gh-pages --force
```

---

## 配置 Pages 源

**基本用法:通过 gh 配置 Pages**
`gh api repos/<owner>/<repo>/pages`

```bash
# 设置 Pages 源为 GitHub Actions
gh api repos/owner/repo/pages -X POST -f source[branch]=main -f source[path]=/

# 修改 Pages 源
gh api repos/owner/repo/pages -X PUT -f source[branch]=gh-pages

# 查看 Pages 配置
gh api repos/owner/repo/pages
```

---

## 自定义域名

**基本用法:配置自定义域名**
`echo "<域名>" > CNAME`

```bash
# 在站点根目录创建 CNAME 文件
echo "docs.example.com" > dist/CNAME

# 配置 DNS:把 www 指向 <user>.github.io
```

---

## 通过 gh-pages 工具发布

**基本用法:用 gh-pages 工具**
`npx gh-pages -d <目录>`

```bash
# 把 dist 发布到 gh-pages 分支
npx gh-pages -d dist

# 指定分支与消息
npx gh-pages -d dist -b gh-pages -m "deploy [skip ci]"
```

---