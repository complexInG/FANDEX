# git gc/prune/fsck 仓库维护命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## gc 垃圾回收

**基本用法:手动整理仓库**
`git gc [选项]`

```bash
# 执行垃圾回收与压缩
git gc

# 更彻底的整理(更耗时)
git gc --aggressive

# 自动判断是否需要整理
git gc --auto

# 仅整理不压缩
git gc --no-prune
```

---

**基本用法:压包**
`git repack [选项]`

```bash
# 重新打包松散对象
git repack -d

# 增量打包
git repack -a -d
```

---

## prune 清理松散对象

**基本用法:删除不可达对象**
`git prune [选项]`

```bash
# 删除超过 2 周的不可达松散对象
git prune --expire=2.weeks.ago

# 预演查看将删除什么
git prune -n

# 立即清理所有不可达对象
git prune --expire=now
```

---

## fsck 完整性检查

**基本用法:检查仓库完整性**
`git fsck [选项]`

```bash
# 检查所有对象的连通性与完整性
git fsck --full

# 显示悬挂的提交对象
git fsck --lost-found

# 检查不可达对象
git fsck --unreachable
```

---

## count-objects 统计

**基本用法:查看对象统计**
`git count-objects -v`

```bash
# 显示对象数量与占用空间
git count-objects -v
```

---

## maintenance 维护任务

**基本用法:启动后台维护**
`git maintenance run [选项]`

```bash
# 运行所有维护任务
git maintenance run --all

# 启用自动维护
git maintenance start

# 注册仓库到自动维护
git maintenance register
```

---