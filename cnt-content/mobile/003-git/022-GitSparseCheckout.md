# Git sparse-checkout 与 partial clone

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## sparse-checkout 启用

**基本写法：初始化稀疏检出**
`git sparse-checkout init`
```bash
# 启用稀疏检出（默认仅根目录文件）
git sparse-checkout init
```

---

**基本写法：启用锥形模式**
`git sparse-checkout init --cone`
```bash
# 启用推荐的锥形模式（目录级匹配）
git sparse-checkout init --cone
```

---

**基本写法：启用模式模式**
`git sparse-checkout init --no-cone`
```bash
# 启用完整模式匹配（支持通配符）
git sparse-checkout init --no-cone
```

---

## 设置检出路径

**基本写法：设置需要检出的目录**
`git sparse-checkout set <路径1> <路径2>`
```bash
# 仅检出 src 与 docs 目录
git sparse-checkout set src docs
```

---

**基本写法：从标准输入读取路径**
`git sparse-checkout set --stdin < <文件>`
```bash
# 从文件读取路径列表
git sparse-checkout set --stdin < paths.txt
```

---

**基本写法：追加检出目录**
`git sparse-checkout add <路径>`
```bash
# 在已有基础上添加 tests 目录
git sparse-checkout add tests
```

---

**基本写法：重新应用稀疏规则**
`git sparse-checkout reapply`
```bash
# 修改规则后重新应用
git sparse-checkout reapply
```

---

## 查看与管理

**基本写法：查看当前检出规则**
`git sparse-checkout list`
```bash
# 列出当前所有稀疏检出路径
git sparse-checkout list
```

---

**基本写法：检查路径是否匹配**
`git sparse-checkout check-rules <路径>`
```bash
# 检查某路径是否会被检出
git sparse-checkout check-rules src/api/users.ts
```

---

**基本写法：禁用稀疏检出**
`git sparse-checkout disable`
```bash
# 关闭稀疏检出恢复完整工作区
git sparse-checkout disable
```

---

## cone 模式规则

**基本写法：添加根目录文件**
`git sparse-checkout set "/*"`
```bash
# 锥形模式下检出所有根目录文件
git sparse-checkout set "/*"
```

---

**基本写法：递归检出子目录**
`git sparse-checkout set src/`
```bash
# 检出 src 目录及其全部子目录
git sparse-checkout set src/
```

---

**基本写法：多层目录匹配**
`git sparse-checkout set src/api src/shared`
```bash
# 同时检出多个顶层子目录
git sparse-checkout set src/api src/shared
```

---

## 非 cone 模式规则

**基本写法：使用通配符匹配**
`git sparse-checkout set "/*.md"`
```bash
# 仅检出根目录 markdown 文件
git sparse-checkout set "/*.md"
```

---

**基本写法：排除某些路径**
`git sparse-checkout set "src/*" "!src/legacy/*"`
```bash
# 检出 src 但排除 legacy 子目录
git sparse-checkout set "src/*" "!src/legacy/*"
```

---

**基本写法：母目录与子目录同时配置**
`git sparse-checkout set "src/" "src/legacy/file.ts"`
```bash
# 检出 src 目录但只保留 legacy 中一个文件
git sparse-checkout set "src/" "src/legacy/file.ts"
```

---

## partial clone 部分克隆

**基本写法：克隆时跳过所有 blob**
`git clone --filter=blob:none <仓库URL>`
```bash
# 仅克隆提交历史，blob 按需获取
git clone --filter=blob:none https://github.com/org/repo.git
```

---

**基本写法：按大小过滤 blob**
`git clone --filter=blob:limit=<大小> <仓库URL>`
```bash
# 跳过大于 1MB 的 blob
git clone --filter=blob:limit=1m https://github.com/org/repo.git
```

---

**基本写法：仅克隆目录树**
`git clone --filter=tree:0 <仓库URL>`
```bash
# 仅克隆提交与目录结构
git clone --filter=tree:0 https://github.com/org/repo.git
```

---

**基本写法：仅克隆指定分支**
`git clone --branch <分支> --single-branch <仓库URL>`
```bash
# 仅克隆 main 分支历史
git clone --branch main --single-branch https://github.com/org/repo.git
```

---

## 组合使用

**基本写法：稀疏检出加部分克隆**
`git clone --filter=blob:none --sparse <仓库URL>`
```bash
# 同时启用部分克隆与稀疏检出
git clone --filter=blob:none --sparse https://github.com/org/repo.git
```

---

**基本写法：克隆后配置稀疏检出**
`git sparse-checkout set <路径>`
```bash
# 进入仓库后设置检出路径
git sparse-checkout set src/api
```

---

**基本写法：将现有仓库转为部分克隆**
`git remote set-origin --filter=blob:none origin`
```bash
# 修改远程配置启用过滤（需新克隆才生效）
git config remote.origin.partialclonefilter blob:none
```

---

## 浅克隆对比

**基本写法：浅克隆指定深度**
`git clone --depth=<深度> <仓库URL>`
```bash
# 仅克隆最近 10 次提交
git clone --depth=10 https://github.com/org/repo.git
```

---

**基本写法：浅克隆指定时间**
`git clone --shallow-since=<日期> <仓库URL>`
```bash
# 仅克隆 2024 年以来的提交
git clone --shallow-since=2024-01-01 https://github.com/org/repo.git
```

---

**基本写法：解除浅克隆**
`git fetch --unshallow`
```bash
# 拉取全部历史转为完整仓库
git fetch --unshallow
```

---

## 按需获取对象

**基本写法：手动获取缺失 blob**
`git fetch origin <路径>`
```bash
# 按需拉取指定路径的 blob
git fetch origin src/api/users.ts
```

---

**基本写法：批量获取某目录**
`git sparse-checkout add <路径>`
```bash
# 添加目录触发对象获取
git sparse-checkout add src/shared
```

---

**基本写法：检查缺失对象**
`git fsck --connectivity-only`
```bash
# 检查仓库对象连通性
git fsck --connectivity-only
```

---

## 配置与优化

**基本写法：配置部分克隆过滤**
`git config remote.origin.partialclonefilter <过滤>`
```bash
# 设置远程仓库部分克隆过滤规则
git config remote.origin.partialclonefilter blob:none
```

---

**基本写法：启用按需获取**
`git config remote.origin.promisor true`
```bash
# 标记远程为 promisor 允许按需获取
git config remote.origin.promisor true
```

---

**基本写法：查看 sparse 配置**
`git config --get-all core.sparseCheckout`
```bash
# 查看稀疏检出是否启用
git config --get-all core.sparseCheckout
```

---

**基本写法：查看 sparseCheckoutCone**
`git config core.sparseCheckoutCone`
```bash
# 查看是否启用锥形模式
git config core.sparseCheckoutCone
```
