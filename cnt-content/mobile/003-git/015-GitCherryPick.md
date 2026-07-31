# Git cherry-pick

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：应用单个提交到当前分支**
`git cherry-pick <提交>`
```bash
# 将指定提交应用到当前分支
git cherry-pick abc1234
```

---

**基本写法：应用多个提交**
`git cherry-pick <提交1> <提交2>`
```bash
# 按顺序应用多个提交
git cherry-pick abc1234 def5678
```

---

**基本写法：应用提交范围**
`git cherry-pick <起点>..<终点>`
```bash
# 应用从起点之后到终点的提交（不含起点）
git cherry-pick v1.0.0..v1.1.0
```

---

**基本写法：应用包含起点的范围**
`git cherry-pick <起点>^..<终点>`
```bash
# 应用从起点到终点的所有提交
git cherry-pick v1.0.0^..v1.1.0
```

---

## 保留信息

**基本写法：保留原提交作者**
`git cherry-pick -x <提交>`
```bash
# 在提交信息中追加原提交哈希
git cherry-pick -x abc1234
```

---

**基本写法：保留原提交哈希引用**
`git cherry-pick --edit <提交>`
```bash
# 应用时打开编辑器修改提交信息
git cherry-pick --edit abc1234
```

---

**基本写法：使用原提交信息**
`git cherry-pick --no-commit <提交>`
```bash
# 应用变更但不立即提交
git cherry-pick --no-commit abc1234
```

---

**基本写法：自定义提交信息**
`git cherry-pick --signoff <提交>`
```bash
# 添加 Signed-off-by 签名
git cherry-pick --signoff abc1234
```

---

## 冲突处理

**基本写法：继续 cherry-pick**
`git cherry-pick --continue`
```bash
# 解决冲突后继续
git cherry-pick --continue
```

---

**基本写法：放弃当前 cherry-pick**
`git cherry-pick --abort`
```bash
# 取消并回到操作前状态
git cherry-pick --abort
```

---

**基本写法：跳过当前提交**
`git cherry-pick --skip`
```bash
# 跳过当前冲突提交继续下一个
git cherry-pick --skip
```

---

**基本写法：保留冲突标记的合并提交**
`git cherry-pick --keep-redundant-commits <提交>`
```bash
# 即使变更已被包含也保留提交
git cherry-pick --keep-redundant-commits abc1234
```

---

## 策略选项

**基本写法：指定合并策略**
`git cherry-pick -X <策略> <提交>`
```bash
# 使用 theirs 策略优先采用被应用提交
git cherry-pick -X theirs abc1234
```

---

**基本写法：使用 ours 策略**
`git cherry-pick -X ours <提交>`
```bash
# 冲突时优先保留当前分支内容
git cherry-pick -X ours abc1234
```

---

## 主分支回退场景

**基本写法：从 hotfix 分支拣选修复到 main**
`git cherry-pick <修复提交>`
```bash
# 切到 main 后应用 hotfix 提交
git cherry-pick hotfix-9a3b1c2
```

---

**基本写法：从 main 拣选到发布分支**
`git cherry-pick <提交>`
```bash
# 将 main 上的修复同步到 release 分支
git cherry-pick release-1.2.3
```

---

## 批量操作

**基本写法：批量拣选多分支提交**
`git cherry-pick <分支A>^..<分支B>`
```bash
# 拣选 A 到 B 范围内的所有提交
git cherry-pick feature^..release
```

---

**基本写法：从 git log 拣选**
`git cherry-pick $(git log --grep="<关键字>" --format=%H)`
```bash
# 拣选所有匹配关键字的提交
git cherry-pick $(git log --grep="fix:" --format=%H)
```

---

## 验证与查询

**基本写法：查看哪些提交尚未应用**
`git cherry -v <上游分支>`
```bash
# 显示尚未合并到上游的提交
git cherry -v main
```

---

**基本写法：显示带 + 或 - 的可拣选提交**
`git cherry <上游> <分支>`
```bash
# 列出指定分支相对上游的可拣选状态
git cherry main feature
```
