---
order: 410
title: GitHub 冲突解决
module: github

category: '004-github'
difficulty: beginner
description: 以问题驱动方式讲解 Git 合并冲突的产生原理、冲突标记解读、完整解决流程与预防策略，覆盖 merge/rebase/cherry-pick 冲突场景，适合零基础学习者。
author: fanquanpp
updated: '2026-08-02'
related: []
prerequisites: []
---
## 开篇：冲突了怎么办——先别慌

想象这样一个场景：你和同事在同一张纸上写会议纪要。你在第 3 行写上"预算 5 万元"，同事也在第 3 行写上"预算 8 万元"。最后要把两份纪要合成一份，尴尬的时刻来了——**第 3 行到底听谁的？**

你把两份纪要交给主管，主管也拿不定主意，只能把两份内容都标出来，请你们两个当事人当面说清楚。

Git 遇到的情况一模一样：当两个分支**修改了同一文件的同一处内容，且修改不一致**时，Git 无法替你决定保留哪一份，于是它停下来，在文件里插入"争论标记"，把决定权交还给你。这就是**冲突（Conflict）**。

本篇采用**问题驱动**的叙事方式，从"遇到冲突的恐慌"切入，依次回答四个问题：**冲突从哪来？冲突长什么样？怎么解决？怎么预防？** 学完这一篇，你会把冲突从"灾难现场"变成"日常工作"。

---

## 一、原理讲解：冲突从哪来

### 1.1 冲突的唯一来源：三方合并

回顾 040 篇的三方合并机制：合并时 Git 比较三个版本——我方（ours）、对方（theirs）、共同祖先（base）。冲突的产生规则只有一条：

| 比较结果 | Git 的处理 |
| --- | --- |
| 只有一方改了某处 | 自动采用，无冲突 |
| 双方改了不同的地方 | 自动合并，无冲突 |
| 双方改了**同一处**且内容**不一致** | **冲突**，停下等人裁决 |

注意：**"同一处"** 是关键。你和同事一个改第 3 行、一个改第 30 行，Git 能自动合并；只有两人都改了第 3 行还改得不一样，才会冲突。

### 1.2 什么操作会触发冲突

```bash
# 最常见的触发场景
git merge feature        # 合并冲突
git pull                 # 拉取远程更新时的合并冲突（本质也是 merge）
git pull --rebase        # 变基冲突
git cherry-pick abc1234  # 移植提交冲突
git stash pop            # 恢复暂存冲突（见 045 篇）
```

### 1.3 冲突发生时的现象

执行合并命令后，终端会出现类似提示：

```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

同时 `git status` 会把冲突文件标记出来：

```
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   app.py
```

> 原理提示：冲突发生时，Git 进入"合并中"（MERGING）状态，此时**不要慌、不要乱敲命令**。你只有三个选择：解决并继续（continue）、放弃合并（abort）、或用工具辅助。Git 也贴心地生成了 `.git/MERGE_HEAD` 等临时状态文件，`git merge --abort` 就是靠它们还原现场的。

---

## 二、冲突长什么样：解读冲突标记

用编辑器打开冲突文件，你会看到 Git 插入的三段式标记：

```
<<<<<<< HEAD
当前分支（我方）的代码
=======
feature/login 分支（对方）的代码
>>>>>>> feature/login
```

标记含义逐行拆解：

| 标记 | 含义 |
| --- | --- |
| `<<<<<<< HEAD` | 冲突区域开始，下方是**当前分支**（我方）的内容 |
| `=======` | 分界线：上面是我方，下面是对方 |
| `>>>>>>> feature/login` | 冲突区域结束，标注对方分支名（或提交 ID） |

示例（一个真实的冲突文件）：

```python
def get_discount(price):
<<<<<<< HEAD
    return price * 0.9        # 我方：打九折
=======
    return price * 0.8        # 对方：打八折
>>>>>>> feature/login
```

### 2.1 快速查看冲突文件清单

```bash
# 仅列出有冲突的文件名
git diff --name-only --diff-filter=U

# 查看冲突的具体内容（带标记）
git diff

# 查看冲突文件在各自版本中的内容
git show HEAD:app.py         # 我方版本
git show feature/login:app.py  # 对方版本
```

---

## 三、怎么解决：完整流程四步走

冲突解决的标准流程是：**找文件 → 改内容 → 标记解决 → 收尾提交**。

### 3.1 第一步：定位冲突文件

```bash
git status
# 找到 both modified 的文件，就是需要处理的
```

### 3.2 第二步：手动编辑，做出裁决

打开冲突文件，做三件事：

1. 删除冲突标记行（`<<<<<<<`、`=======`、`>>>>>>>`）；
2. 决定保留哪份内容——我方、对方、或融合两者（三者均可）；
3. 确保文件语法正确、逻辑完整。

保留技巧：

```bash
# 想直接保留当前分支（我方）的版本
git checkout --ours app.py

# 想直接保留对方分支的版本
git checkout --theirs app.py

# 注意：checkout --ours/--theirs 只对冲突文件生效，且会覆盖整个文件
```

### 3.3 第三步：告诉 Git"这个冲突解决了"

```bash
# 编辑完成后，git add 即表示该文件冲突已解决
git add app.py
```

### 3.4 第四步：按操作类型收尾

```bash
# 如果是在 merge / pull 中：完成合并提交
git commit -m "merge: 合并 feature/login 分支"

# 或用默认合并信息（Git 自动生成）
git commit --no-edit

# 如果是在 rebase 中：继续变基
git rebase --continue

# 如果是在 cherry-pick 中：继续
git cherry-pick --continue
```

### 3.5 图形化工具辅助

```bash
# 用 VS Code 打开冲突文件（界面会提供 Accept Current/Incoming 按钮）
code app.py

# 启动配置好的图形化合并工具
git mergetool

# 指定具体工具
git mergetool --tool=vimdiff
```

---

## 四、想反悔：中止操作

解决到一半觉得太乱？Git 允许一键回到操作前状态：

```bash
# 中止合并（回到 merge 之前）
git merge --abort

# 中止变基
git rebase --abort

# 中止 cherry-pick
git cherry-pick --abort
```

> 注意：`--abort` 会丢弃本次合并带来的所有改动（包括你已做的冲突编辑）。要谨慎使用；不过它至少不会动你已经提交过的历史。

---

## 五、怎么预防：让冲突少发生

冲突无法 100% 避免，但可以大幅减少：

```bash
# 1. 拉取前先把本地改动收好（避免"工作区脏"导致的额外麻烦）
git stash && git pull && git stash pop

# 2. 用 rebase 方式拉取，减少多余的合并提交
git pull --rebase

# 3. 定期同步主分支：先看远程变化，再变基自己的分支
git fetch origin
git rebase origin/main

# 4. 合并前先看两分支差异，评估冲突风险
git diff main...feature

# 5. 查看两分支的共同祖先（分叉点）
git merge-base main feature
```

日常预防习惯（比命令更重要）：

- **小步提交、勤同步**：改动越小越少，冲突面就越小；
- **分工明确**：尽量避免多人同时改同一文件同一区域；
- **配置文件谨慎改**：如 `package.json`、`.env.example` 这类高频文件最容易冲突；
- **提交前先 pull**：这是团队协作的第一铁律。

---

## 六、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 冲突后直接乱提交 | 提交信息里残留 `<<<<<<<` 标记 | 忘记删除冲突标记就 commit | 搜索并删除所有 `<<<<<<<`、`=======`、`>>>>>>>` 行再 add+commit |
| add 了文件但仍提示冲突未解决 | `you have unmerged paths` | 还有别的冲突文件没处理 | `git status` 检查所有 `both modified` 文件，逐一处理 |
| 不知道怎么退出冲突状态 | 执行任何命令都提示合并中 | 停在 MERGING/Rebasing 状态 | 走完收尾流程（commit / rebase --continue），或 `--abort` 放弃 |
| 误用 --abort 丢失编辑 | 冲突解决到一半，abort 后改动全没了 | 理解偏差——abort 是放弃不是保存 | 想保留处理结果就继续走 add+commit；abort 前确认放弃 |
| checkout --ours 不生效 | 文件内容没变成我方的 | 该文件不是冲突文件，或拼写错误 | 先 `git status` 确认文件确实处于 unmerged 状态 |
| 冲突后 push 被拒 | `non-fast-forward` | 只解决完没 commit，或没重新 add | 走完 3.4 节收尾：add → commit（或 continue）→ push |
| 解决冲突时误删对方代码 | 功能上线后缺失对方的功能 | 裁决时只留了自己那份 | 融合双方内容，而不是简单二选一；重大合并建议先讨论 |

---

## 七、实战练习

### 练习 1：制造并解决第一个冲突（入门）

**题目**：在同一文件的同一行，从 main 和 feature 分别写入不同内容，merge 触发冲突，手动编辑解决后提交。

**提示**：参考 040 篇的三方合并场景构造分叉。

**参考答案要点**：

```bash
git init -b main
echo "version: 1.0" > config.txt
git add . && git commit -m "init"
git switch -c feature
echo "version: 2.0" > config.txt
git commit -am "feature: 改版本号"
git switch main
echo "version: 3.0" > config.txt
git commit -am "main: 改版本号"
git merge feature            # 冲突！
# 编辑 config.txt：删除标记，保留想要的版本
git add config.txt
git commit -m "merge: 解决版本号冲突"
```

### 练习 2：用 --ours/--theirs 快速裁决（入门）

**题目**：同样的冲突场景，改用 `git checkout --ours` / `--theirs` 快速选择一方，观察效果。

**提示**：该命令在冲突状态下对冲突文件生效。

**参考答案要点**：

```bash
git merge feature            # 冲突
git checkout --theirs config.txt   # 直接采用 feature 的版本
git add config.txt
git commit -m "merge: 采用 feature 版本"
```

### 练习 3：变基冲突的处理（进阶）

**题目**：用 `git pull --rebase`（或 `git rebase`）触发冲突，练习 `git rebase --continue` 与 `git rebase --abort` 两条路径。

**提示**：rebase 冲突可能一个提交一个提交地出现，耐心逐个解决。

**参考答案要点**：

```bash
git switch feature
git rebase main              # 冲突
# 解决第一个文件 -> git add
git rebase --continue        # 若还有后续冲突继续处理
# 全部完成后：历史呈直线
```

### 练习 4：cherry-pick 冲突（进阶）

**题目**：把一个在旧版本基础上写的提交 cherry-pick 到已大幅变化的分支上，体验冲突并完成收尾。

**提示**：cherry-pick 冲突用 `git cherry-pick --continue` 或 `--abort`。

**参考答案要点**：

```bash
git cherry-pick abc1234      # 冲突
git status                   # 找到冲突文件
# 编辑解决 -> git add
git cherry-pick --continue
```

### 练习 5：冲突预防演练（综合）

**题目**：在一个"脏工作区"（有未提交改动）上执行 pull，观察报错；再用 `git stash` 方案成功完成"先收后拉再恢复"。

**提示**：`git stash` + `git pull` + `git stash pop` 三连。

**参考答案要点**：

```bash
echo "未提交的改动" >> app.py
git pull                     # 报错：local changes would be overwritten
git stash                    # 1. 收好改动
git pull                     # 2. 拉取成功
git stash pop                # 3. 恢复改动（若与远程冲突，按本文流程解决）
```

---

## 八、一句话记忆

**冲突 = 双方改了同一处且不一致，Git 交回裁决权——看标记（<<<<<<< 我方 / ======= 对方 / >>>>>>>），编辑裁决，add 标记已解决，merge --continue 或 commit 收尾；不想玩了就 --abort，想少冲突就小步提交勤同步。**

---

## 参考链接

- Git 官方文档（git merge）：https://git-scm.com/docs/git-merge
- Git 官方文档（git rebase，中文）：https://git-scm.com/docs/git-rebase/zh_HANS-CN.html
- Pro Git 中文版 3.2 分支的新建与合并（冲突解决）：https://git-scm.com/book/zh/v2/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6
- GitHub 文档（解决合并冲突）：https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts

## 延伸阅读

- 冲突的底层机制（三方合并、快进合并），见上一篇 040-GitMergeRebase。
- 拉取更新时的冲突处理，见 039-GitPullFetch。
- 暂存与回退（stash 临时收好改动、reset 回退），见 045-GitStashReset。
- 关联文档：分支模型与分支规则，见 007-BranchModelBranchRule；GitHub PR 合并流程，见 027-PullRequestCompleteCollaborationFlow。
