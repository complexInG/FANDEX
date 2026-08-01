# Git shortlog 提交摘要

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：查看提交者统计**
`git shortlog`
```bash
# 按作者分组显示提交数量
git shortlog
```

---

**基本写法：限定提交范围**
`git shortlog <提交范围>`
```bash
# 仅统计最近 30 天的提交
git shortlog --since="30 days"
```

---

**基本写法：统计指定分支**
`git shortlog <分支>`
```bash
# 统计 main 分支提交
git shortlog main
```

---

**基本写法：从某版本起统计**
`git shortlog <标签>..HEAD`
```bash
# 统计 v1.0.0 之后的所有提交
git shortlog v1.0.0..HEAD
```

---

## 输出格式

**基本写法：按数量排序**
`git shortlog -n`
```bash
# 提交数量多的作者排在前面
git shortlog -n
```

---

**基本写法：按作者排序**
`git shortlog -s`
```bash
# 仅显示提交数量与作者名
git shortlog -s
```

---

**基本写法：组合数量与姓名排序**
`git shortlog -s -n`
```bash
# 按提交数量降序显示摘要
git shortlog -s -n
```

---

**基本写法：显示完整提交信息**
`git shortlog -e`
```bash
# 同时显示作者邮箱
git shortlog -e
```

---

## 分组方式

**基本写法：按作者分组**
`git shortlog --group=author`
```bash
# 默认按作者名分组
git shortlog --group=author
```

---

**基本写法：按邮箱分组**
`git shortlog --group=email`
```bash
# 按邮箱分组避免同名不同人
git shortlog --group=email
```

---

**基本写法：按提交者分组**
`git shortlog --group=committer`
```bash
# 按提交者而非作者分组
git shortlog --group=committer
```

---

**基本写法：多分组聚合**
`git shortlog --group=author --group=email`
```bash
# 同时按作者与邮箱分组
git shortlog --group=author --group=email
```

---

## 格式化输出

**基本写法：自定义行格式**
`git shortlog --format="<格式>"`
```bash
# 自定义每条提交的显示格式
git shortlog --format="%h %s"
```

---

**基本写法：只显示提交主题**
`git shortlog -w`
```bash
# 包装长行输出更整齐
git shortlog -w
```

---

**基本写法：指定换行宽度**
`git shortlog -w<宽度>`
```bash
# 设置 80 列换行
git shortlog -w80
```

---

## 过滤范围

**基本写法：按时间过滤**
`git shortlog --since="<时间>" --until="<时间>"`
```bash
# 统计 2024 年的提交
git shortlog --since="2024-01-01" --until="2024-12-31"
```

---

**基本写法：按作者过滤**
`git shortlog --author="<关键字>"`
```bash
# 仅统计 Alice 的提交
git shortlog --author="Alice"
```

---

**基本写法：按提交信息过滤**
`git shortlog --grep="<关键字>"`
```bash
# 仅统计 fix 类提交
git shortlog --grep="^fix:"
```

---

**基本写法：按路径过滤**
`git shortlog -- <路径>`
```bash
# 仅统计 src 目录的提交
git shortlog -- src/
```

---

## 报告生成

**基本写法：生成发布说明**
`git shortlog -s -n <标签>..HEAD > CHANGELOG.txt`
```bash
# 生成自上版本以来的贡献者列表
git shortlog -s -n v1.0.0..HEAD > CHANGELOG.txt
```

---

**基本写法：Markdown 格式输出**
`git shortlog -s -n --format="* %s"`
```bash
# 输出 Markdown 列表格式的变更摘要
git shortlog --format="* %s" v1.0.0..HEAD
```

---

**基本写法：按作者生成详细日志**
`git shortlog -e -n v1.0.0..HEAD`
```bash
# 按作者分组生成发布日志
git shortlog -e -n v1.0.0..HEAD
```

---

## 统计行数（结合其他命令）

**基本写法：统计每个作者提交数**
`git shortlog -s -n --all`
```bash
# 全分支统计作者提交数
git shortlog -s -n --all
```

---

**基本写法：组合 numstat 统计行数**
`git log --author="<作者>" --numstat --pretty=tformat: | awk '{add+=$1; del+=$2} END {print add, del}'`
```bash
# 统计某作者新增与删除的行数
git log --author="Alice" --numstat --pretty=tformat: | awk '{add+=$1; del+=$2} END {print add, del}'
```

---

## 多仓库合并统计

**基本写法：跨仓库汇总贡献**
`git log --all --pretty=format:"%an" | sort | uniq -c | sort -nr`
```bash
# 用基础命令统计所有引用的作者
git log --all --pretty=format:"%an" | sort | uniq -c | sort -nr
```

---

**基本写法：导出报告供汇总**
`git shortlog -sne --all > contributors.txt`
```bash
# 导出全分支贡献者列表
git shortlog -sne --all > contributors.txt
```
