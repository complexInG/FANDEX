# git status 状态命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 基础查看

**基本用法:查看工作区状态**
`git status`

```bash
# 查看完整状态
git status

# 简洁模式
git status -s

# 显示被忽略文件
git status --ignored
```

---

## 紧凑输出

**基本用法:短格式**
`git status -s`

```bash
# 左列暂存区,右列工作区
git status -s

# 带分支信息
git status -sb
```

---

状态码含义:
- `M` 已修改(modified)
- `A` 已新增到暂存区(added)
- `D` 已删除(deleted)
- `R` 重命名(renamed)
- `??` 未跟踪(untracked)

---

## 瓷器格式

**基本用法:机器可读输出**
`git status --porcelain`

```bash
# 稳定的脚本可解析格式
git status --porcelain

# v2 版本含分支与重命名信息
git status --porcelain=v2

# 仅列出未跟踪文件
git status --porcelain | grep '^??'
```

---

## 分支信息

**基本用法:查看与上游分支关系**
`git status -sb`

```bash
# 显示领先/落后远程的提交数
git status -sb
# 输出示例:## main...origin/main [ahead 2, behind 1]
```

---

**基本用法:查看指定分支**
`git status <分支>`

```bash
# 与指定分支比较
git status main
```

---

## 长格式选项

**基本用法:长格式说明**
`git status --long`

```bash
# 强制长格式(默认)
git status --long
```

---