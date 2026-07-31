# Git describe 版本描述

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：描述当前提交**
`git describe`
```bash
# 显示当前 HEAD 距离最近标签的描述
git describe
```

---

**基本写法：描述指定提交**
`git describe <提交>`
```bash
# 描述指定分支最新提交
git describe main
```

---

**基本写法：描述指定标签**
`git describe <标签>`
```bash
# 描述 v1.0.0 标签
git describe v1.0.0
```

---

## 标签选择

**基本写法：仅使用带注释的标签**
`git describe --tags`
```bash
# 包含轻量标签与带注释标签
git describe --tags
```

---

**基本写法：包含所有引用**
`git describe --all`
```bash
# 使用所有引用（含分支）描述
git describe --all
```

---

**基本写法：仅匹配特定模式标签**
`git describe --match "<模式>"`
```bash
# 仅匹配 v 开头的版本标签
git describe --match "v*"
```

---

**基本写法：排除特定模式标签**
`git describe --exclude "<模式>"`
```bash
# 排除 alpha 与 beta 标签
git describe --exclude "*alpha*" --exclude "*beta*"
```

---

## 输出格式

**基本写法：仅显示最近标签**
`git describe --abbrev=0`
```bash
# 仅输出最近标签名，不显示提交距离
git describe --abbrev=0
```

---

**基本写法：指定哈希缩写长度**
`git describe --abbrev=<长度>`
```bash
# 输出 7 位提交哈希缩写
git describe --abbrev=7
```

---

**基本写法：始终输出长格式**
`git describe --long`
```bash
# 始终输出 标签-距离-哈希 完整格式
git describe --long
```

---

**基本写法：自定义输出格式**
`git describe --format="<格式>"`
```bash
# 自定义描述输出格式
git describe --format="%d-%h"
```

---

## 提交距离控制

**基本写法：限制标签查找深度**
`git describe --max-count=<数量>`
```bash
# 最多向前查找 100 个标签
git describe --max-count=100
```

---

**基本写法：按提交数量限制**
`git describe --candidates=<数量>`
```bash
# 仅在最近 5 个候选中查找标签
git describe --candidates=5
```

---

**基本写法：找不到标签时回退到哈希**
`git describe --always`
```bash
# 无标签时输出短哈希而非报错
git describe --always
```

---

## 与 dirty 状态结合

**基本写法：附加工作区状态**
`git describe --dirty`
```bash
# 工作区有改动时附加 -dirty
git describe --dirty
```

---

**基本写法：附加详细 dirty 标记**
`git describe --dirty --broken`
```bash
# 包含工作区改动与损坏对象标记
git describe --dirty --broken
```

---

**基本写法：自定义 dirty 标记**
`git describe --dirty-mark=<标记>`
```bash
# 自定义脏标记字符串
git describe --dirty-mark="-modified"
```

---

## 实用场景

**基本写法：生成版本号字符串**
`git describe --tags --always --dirty`
```bash
# 用于构建系统的版本号
git describe --tags --always --dirty
```

---

**基本写法：写入版本文件**
`git describe --tags > VERSION`
```bash
# 将版本描述写入文件供程序读取
git describe --tags > VERSION
```

---

**基本写法：组合提交信息**
`git describe --long --dirty --tags`
```bash
# 完整版本描述用于发布报告
git describe --long --dirty --tags
```

---

**基本写法：在 CI 中获取版本**
`git describe --tags --abbrev=0`
```bash
# 获取最近版本标签用于构建产物命名
git describe --tags --abbrev=0
```

---

## 多标签场景

**基本写法：优先匹配主版本**
`git describe --match "v[0-9]*" --match "release-*"`
```bash
# 同时匹配多种版本模式
git describe --match "v[0-9]*" --match "release-*"
```

---

**基本写法：忽略特定前缀标签**
`git describe --exclude "nightly-*"`
```bash
# 排除每日构建标签
git describe --exclude "nightly-*"
```
