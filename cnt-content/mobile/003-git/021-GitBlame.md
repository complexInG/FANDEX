# Git blame 与 annotate

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 基本用法

**基本写法：查看文件每行最后修改者**
`git blame <文件>`
```bash
# 显示 src/main.py 每行的作者与提交
git blame src/main.py
```

---

**基本写法：限定行范围**
`git blame -L <起始>,<结束> <文件>`
```bash
# 仅查看第 10 到 30 行的归属
git blame -L 10,30 src/main.py
```

---

**基本写法：限定起始行到文件末尾**
`git blame -L <起始> <文件>`
```bash
# 从第 50 行到文件末尾
git blame -L 50 src/main.py
```

---

## 提交范围控制

**基本写法：从指定提交开始追溯**
`git blame <提交> -- <文件>`
```bash
# 从 v1.0.0 标签开始追溯
git blame v1.0.0 -- src/main.py
```

---

**基本写法：限定追溯范围**
`git blame <起点>..<终点> -- <文件>`
```bash
# 仅在指定提交范围内追溯
git blame v1.0.0..HEAD -- src/main.py
```

---

**基本写法：查看更早版本**
`git blame <提交>^ -- <文件>`
```bash
# 查看上一次提交时的归属
git blame HEAD^ -- src/main.py
```

---

## 输出格式

**基本写法：显示完整哈希**
`git blame -l <文件>`
```bash
# 显示 40 位完整提交哈希
git blame -l src/main.py
```

---

**基本写法：显示作者邮箱**
`git blame -e <文件>`
```bash
# 用邮箱代替作者姓名
git blame -e src/main.py
```

---

**基本写法：显示提交时间**
`git blame -t <文件>`
```bash
# 显示原始时间戳而非日期
git blame -t src/main.py
```

---

**基本写法：空提交敏感模式**
`git blame -w <文件>`
```bash
# 忽略空白变更的提交
git blame -w src/main.py
```

---

## 行追踪

**基本写法：追踪行移动**
`git blame -M <文件>`
```bash
# 检测同一文件内的行移动
git blame -M src/main.py
```

---

**基本写法：检测跨文件复制移动**
`git blame -C <文件>`
```bash
# 检测从其他文件复制的行
git blame -C src/main.py
```

---

**基本写法：全仓库范围检测复制**
`git blame -CCC <文件>`
```bash
# 在所有提交中检测复制来源
git blame -CCC src/main.py
```

---

**基本写法：指定移动检测阈值**
`git blame -M<数量> <文件>`
```bash
# 设置移动检测的最小字符数
git blame -M20 src/main.py
```

---

## 增量查看

**基本写法：限制每次显示行数**
`git blame --incremental <文件>`
```bash
# 增量输出便于程序解析
git blame --incremental src/main.py
```

---

**基本写法：显示边界提交**
`git blame --root <文件>`
```bash
# 将根提交也标记为边界
git blame --root src/main.py
```

---

## annotate 命令

**基本写法：使用 annotate（blame 别名）**
`git annotate <文件>`
```bash
# annotate 等价于 blame
git annotate src/main.py
```

---

**基本写法：annotate 限定范围**
`git annotate -L <起始>,<结束> <文件>`
```bash
# annotate 限定行范围
git annotate -L 1,20 src/main.py
```

---

## 实用场景

**基本写法：定位 bug 引入提交**
`git blame -L <行>,<行> <文件>`
```bash
# 定位某行代码的最后修改提交
git blame -L 42,42 src/main.py
```

---

**基本写法：查看某行完整提交信息**
`git show <提交>`
```bash
# 查看 blame 找到的提交详情
git show abc1234
```

---

**基本写法：忽略某些提交**
`git blame --ignore-rev <提交> <文件>`
```bash
# 跳过指定提交（如格式化提交）
git blame --ignore-rev abc1234 src/main.py
```

---

**基本写法：通过文件配置忽略列表**
`git blame --ignore-revs-file <文件> <目标文件>`
```bash
# 从文件读取要忽略的提交列表
git blame --ignore-revs-file .git-blame-ignore revs.txt src/main.py
```

---

**基本写法：配置默认忽略文件**
`git config blame.ignoreRevsFile <文件>`
```bash
# 配置项目默认的 blame 忽略文件
git config blame.ignoreRevsFile .git-blame-ignore-revs
```

---

**基本写法：按颜色高亮输出**
`git blame --color-by-age <文件>`
```bash
# 按提交年龄着色显示
git blame --color-by-age src/main.py
```

---

**基本写法：按作者着色**
`git blame --color-lines <文件>`
```bash
# 同一作者的行用相同颜色
git blame --color-lines src/main.py
```

---

## 与其他命令配合

**基本写法：blame 找到提交后查看历史**
`git log -p <提交> -- <文件>`
```bash
# 查看指定提交对该文件的所有改动
git log -p abc1234 -- src/main.py
```

---

**基本写法：定位后用 bisect 深入**
`git bisect start && git bisect bad HEAD && git bisect good <提交>`
```bash
# 由 blame 结果启动二分查找
git bisect start && git bisect bad HEAD && git bisect good abc1234
```
