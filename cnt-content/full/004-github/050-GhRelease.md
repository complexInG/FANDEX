---
order: 500
title: gh release 发布命令速查手册
module: github

category: '004-github'
difficulty: beginner
description: gh release 发布命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
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

## 参考文献

GitHub 文档：https://docs.github.com/zh
GitHub Actions 文档：https://docs.github.com/zh/actions
GitHub REST API：https://docs.github.com/zh/rest
GitHub GraphQL API：https://docs.github.com/zh/graphql

## 延伸阅读

GitHub Actions CI/CD，见 004-github 模块 Actions 文档。
Git 协作基础，见 003-git 模块。
DevOps 自动化，见 031-devops 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供 GitHub 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 GitHub Actions 深入

事件驱动：push、pull_request、schedule、workflow_dispatch；on 支持过滤路径与分支。
上下文：github（事件数据）、env、secrets、needs（任务依赖）；表达式与函数。
安全：第三方 action 固定 SHA；权限默认最小；OIDC 换取云凭证。
缓存与性能：actions/cache、并发控制、矩阵并行。

### 13.2 开源协作治理

CONTRIBUTING 定义贡献路径；Issue 标签（good first issue）引导新手。
维护者时间管理：合并队列、自动化 triage、定期发布。
社区健康：行为准则执行、讨论区沉淀、感谢贡献。
安全披露：SECURITY.md + 私密漏洞报告流程。
