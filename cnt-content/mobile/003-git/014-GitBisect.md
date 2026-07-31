# Git bisect 二分查找

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 启动与基本流程

**基本写法：启动二分查找**
`git bisect start`
```bash
# 进入 bisect 模式
git bisect start
```

---

**基本写法：标记当前提交为坏**
`git bisect bad [<提交>]`
```bash
# 标记 HEAD 为有问题的提交
git bisect bad
```

---

**基本写法：标记已知的好提交**
`git bisect good <提交>`
```bash
# 指定一个正常的旧提交
git bisect good v1.0.0
```

---

**基本写法：一行启动并指定好坏**
`git bisect start <坏提交> <好提交>`
```bash
# 同时指定坏起点与好起点
git bisect start HEAD v1.0.0
```

---

## 标记测试结果

**基本写法：当前提交标记为好**
`git bisect good`
```bash
# 当前测试通过，继续二分
git bisect good
```

---

**基本写法：当前提交标记为坏**
`git bisect bad`
```bash
# 当前测试失败，继续二分
git bisect bad
```

---

**基本写法：跳过当前提交**
`git bisect skip`
```bash
# 跳过无法测试的提交
git bisect skip
```

---

## 查看状态

**基本写法：查看二分状态**
`git bisect status`
```bash
# 显示当前 bisect 进度
git bisect status
```

---

**基本写法：查看剩余待测提交**
`git bisect visualize`
```bash
# 用 git log 查看剩余范围
git bisect visualize
```

---

**基本写法：查看已测试提交日志**
`git bisect log`
```bash
# 输出 bisect 操作过程
git bisect log
```

---

## 自动化二分

**基本写法：自动二分测试**
`git bisect run <命令> [<参数>]`
```bash
# 用测试脚本自动定位首坏提交
git bisect run npm test
```

---

**基本写法：通过脚本退出码判定**
`git bisect run <脚本>`
```bash
# 125 表示跳过，0 好，1-124 坏
git bisect run ./scripts/check-bug.sh
```

---

**基本写法：编译并测试**
`git bisect run <命令1> && <命令2>`
```bash
# 先编译再测试
git bisect run sh -c 'make && make test'
```

---

## 范围控制

**基本写法：限定路径范围**
`git bisect start -- <路径>`
```bash
# 只二分指定路径下的变更
git bisect start -- src/auth
```

---

**基本写法：排除某些提交**
`git bisect skip <提交1> <提交2>`
```bash
# 跳过多条已知不可测提交
git bisect skip abc1234 def5678
```

---

## 结束与回退

**基本写法：结束二分查找**
`git bisect reset`
```bash
# 退出 bisect 模式回到原分支
git bisect reset
```

---

**基本写法：结束后切回指定分支**
`git bisect reset <分支>`
```bash
# 退出并切回 main 分支
git bisect reset main
```

---

## 恢复中断的二分

**基本写法：记录二分过程到文件**
`git bisect log > <文件>`
```bash
# 保存当前 bisect 状态
git bisect log > bisect.log
```

---

**基本写法：从文件恢复二分状态**
`git bisect replay <文件>`
```bash
# 重新执行记录的 bisect 步骤
git bisect replay bisect.log
```

---

## 查看引入问题的提交

**基本写法：定位首坏提交后查看**
`git show <提交>`
```bash
# 查看被 bisect 锁定的提交内容
git show HEAD
```

---

**基本写法：查看引入问题的差异**
`git diff <好提交> <坏提交>`
```bash
# 查看好坏提交之间的差异
git diff v1.0.0 HEAD
```
