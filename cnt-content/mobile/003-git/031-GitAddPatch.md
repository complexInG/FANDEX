# git add/restore/checkout 工作区命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 暂存文件

**基本用法:暂存改动**
`git add <路径>`

```bash
# 暂存单个文件
git add src/main.py

# 暂存整个目录
git add src/

# 暂存所有改动
git add .

# 暂存已跟踪文件(不含未跟踪)
git add -u
```

---

**基本用法:交互式暂存**
`git add -p`

```bash
# 逐块选择暂存(支持 y/n/s/e/q)
git add -p

# 交互模式主菜单
git add -i
```

---

**基本用法:按补丁暂存**
`git add --patch <文件>`

```bash
# 对指定文件逐块暂存
git add --patch src/utils.js
```

---

## 恢复工作区文件

**基本用法:丢弃工作区改动**
`git restore <文件>`

```bash
# 丢弃工作区改动(恢复到暂存区状态)
git restore src/main.py

# 恢复到指定提交的版本
git restore --source=HEAD~3 src/config.js

# 从暂存区取消暂存
git restore --staged src/main.py
```

---

**基本用法:用 checkout 恢复文件**
`git checkout -- <文件>`

```bash
# 旧写法:丢弃工作区改动
git checkout -- src/main.py

# 恢复指定提交的文件
git checkout a1b2c3d -- README.md
```

---

## 暂存区管理

**基本用法:取消暂存**
`git restore --staged <文件>`

```bash
# 把已暂存的文件移出暂存区
git restore --staged src/main.py

# 取消所有暂存
git restore --staged .
```

---

**基本用法:重置暂存区与工作区**
`git reset [选项] <提交>`

```bash
# 仅重置暂存区,保留工作区改动
git reset HEAD src/

# 软重置(保留改动到暂存区)
git reset --soft HEAD~1

# 混合重置(默认,保留改动到工作区)
git reset --mixed HEAD~1
```

---