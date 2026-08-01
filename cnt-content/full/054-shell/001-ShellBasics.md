---
order: 1
title: Shell 脚本编程基础
module: shell
category: Shell
difficulty: beginner
description: 'Shell 脚本编程基础：命令、变量、管道、控制流、函数与工程实践'
author: fanquanpp
updated: '2026-08-01'
related:
  - getting-started/命令行基础
  - git/Git基础操作
  - devops/CI/CD流水线
prerequisites:
  - getting-started/命令行基础
---
## 1. Shell 是什么

Shell 是操作系统提供的命令解释器：读取用户输入的命令，调用系统程序，并把结果返回给用户。它既是交互式工具，也是脚本语言。Linux/macOS 默认是 bash（或 zsh），Windows 的 PowerShell 是另一套体系，但 Git Bash/WSL 可以运行 bash 脚本。

Shell 脚本的价值在于“胶水”：把已有的小工具（ls、grep、awk、curl）串成自动化流程，用于构建、部署、监控、数据处理。

## 2. 基本命令与语法

### 2.1 命令结构

```bash
命令名 [选项] [参数]
```

示例：

```bash
ls -la /home/user        # 列出目录详细信息
grep -rn "TODO" ./src    # 递归搜索文本
curl -s https://example.com  # 请求网页
```

每条命令执行后返回退出码（exit code）：0 表示成功，非 0 表示失败。`$?` 保存上一条命令的退出码。

### 2.2 变量

```bash
#!/bin/bash
# 变量赋值：等号两侧不能有空格
name="FANDEX"
count=42

# 使用变量：$name 或 ${name}
echo "项目名称: $name"
echo "计数: ${count}"

# 命令替换：把命令输出存入变量
files=$(ls | wc -l)
echo "文件数: $files"
```

讲解：双引号内 `$var` 会展开，单引号内不会；`$(...)` 是命令替换的现代写法（反引号已过时）。

### 2.3 管道与重定向

```bash
# 管道：把前一个命令的输出作为后一个命令的输入
cat access.log | grep "ERROR" | sort | uniq -c | sort -rn

# 重定向：写入文件 / 追加 / 从文件读
echo "hello" > out.txt
echo "world" >> out.txt
wc -l < out.txt

# 错误流合并
command > all.log 2>&1
```

讲解：管道是 Shell 最强大的能力：无需中间文件，数据在进程间流动。`2>&1` 把标准错误合并到标准输出，便于统一记录日志。

## 3. 控制流

### 3.1 条件判断

```bash
#!/bin/bash
file="config.yaml"

if [ -f "$file" ]; then
    echo "文件存在"
elif [ -d "$file" ]; then
    echo "是目录"
else
    echo "不存在"
fi

# test 命令的常用表达式
# -f 文件存在且是普通文件；-d 目录；-z 字符串为空；-n 非空
# -eq 数字相等；-lt 小于；-gt 大于
# && 与；|| 或
```

讲解：`[ ... ]` 是 `test` 命令的语法糖，`[[ ... ]]` 是 bash 扩展（支持正则与更安全比较）。变量必须加引号防止空值导致语法错误。

### 3.2 循环

```bash
#!/bin/bash
# for 循环
for file in *.log; do
    echo "处理 $file"
done

# 数字循环
for i in $(seq 1 5); do
    echo "第 $i 次"
done

# while 循环：读取文件每一行
while IFS= read -r line; do
    echo "$line"
done < data.txt
```

讲解：`IFS=` 防止行首尾空白被吃掉，`-r` 防止反斜杠转义——这是读取文件行的标准姿势。

### 3.3 函数

```bash
#!/bin/bash

# 函数定义
log() {
    local level="$1"
    shift
    echo "[$level] $*"
}

# 调用
log INFO "构建开始"
log ERROR "构建失败"
```

讲解：`$1`、`$2` 是位置参数，`$*` 是所有参数；`local` 声明局部变量，避免污染全局。

## 4. 严格模式与错误处理

生产脚本必须在开头启用严格模式：

```bash
#!/bin/bash
set -euo pipefail
```

三者的含义：

`set -e`：任何命令失败立即退出脚本，避免“失败后继续执行”的连锁错误；

`set -u`：使用未定义变量即报错，捕获拼写错误；

`set -o pipefail`：管道中任意命令失败，整体视为失败（默认只看最后一个命令）。

配合 `trap` 实现清理：

```bash
#!/bin/bash
set -euo pipefail

cleanup() {
    echo "清理临时文件..."
    rm -f /tmp/tmp.$$
}
trap cleanup EXIT
```

讲解：`trap ... EXIT` 保证脚本无论正常结束还是出错退出都会执行清理函数。

## 5. 常用文本处理

### 5.1 grep：行匹配

```bash
grep -i "error" log.txt        # 忽略大小写
grep -v "^#" config.conf       # 排除注释行
grep -E "err|warn" log.txt     # 扩展正则，匹配多个词
```

### 5.2 sed：流编辑

```bash
sed -i 's/old/new/g' file.txt   # 全局替换并写回
sed -n '10,20p' file.txt        # 打印第 10-20 行
```

### 5.3 awk：列处理与统计

```bash
# 打印第 1 列和第 3 列
awk '{print $1, $3}' data.txt

# 统计行数
awk 'END {print NR}' file.txt

# 按第 2 列求和
awk '{sum += $2} END {print sum}' data.txt
```

## 6. 工程实践

### 6.1 部署脚本模板

```bash
#!/bin/bash
set -euo pipefail

APP_DIR="/opt/myapp"
VERSION="${1:?请提供版本号}"

echo "开始部署 v${VERSION}"

# 1. 拉取代码
git -C "$APP_DIR" fetch --tags
git -C "$APP_DIR" checkout "v${VERSION}"

# 2. 构建
(cd "$APP_DIR" && pnpm install --frozen-lockfile && pnpm build)

# 3. 重启服务（systemd 示例）
systemctl restart myapp
systemctl --no-pager status myapp

echo "部署完成"
```

讲解：`${1:?...}` 在缺少参数时直接报错退出；`(cd ... && ...)` 在子 shell 中切换目录，不影响当前脚本。

### 6.2 日志分析

```bash
#!/bin/bash
set -euo pipefail

LOG="access.log"

echo "== 访问量 TOP10 IP =="
awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn | head -10

echo "== 状态码统计 =="
awk '{print $9}' "$LOG" | sort | uniq -c

echo "== 404 页面 =="
grep " 404 " "$LOG" | awk '{print $7}' | sort -u
```

## 7. 常见陷阱

陷阱一：忘记引号。`rm $file` 在文件名含空格时被拆成多个参数。所有变量加双引号。

陷阱二：不用严格模式。命令失败继续执行，产生半成品状态。

陷阱三：`rm -rf` 误删。删除前先 `echo` 预览，使用 `set -u` 防止空变量导致 `rm -rf /`。

陷阱四：脚本不可移植。避免 GNU 专属选项，或用 bash 明确 shebang。

陷阱五：忽略退出码。`command || { echo "失败"; exit 1; }` 显式处理。

## 8. 参考资源

Bash 参考手册：https://www.gnu.org/software/bash/manual/

ShellCheck（静态检查）：https://www.shellcheck.net/

Explain Shell：https://explainshell.com/

Bash 陷阱汇总：https://mywiki.wooledge.org/BashPitfalls

尚硅谷 Bilibili 空间：https://space.bilibili.com/302417610

## 9. 小结

Shell 是运维与后端开发者的基本功：命令、管道、控制流、严格模式四件套覆盖日常 90% 场景。脚本保持薄层，复杂逻辑交给 Python 等语言；用 shellcheck 保证质量，用 set -euo pipefail 保证安全。

## 参考文献

Bash 参考手册：https://www.gnu.org/software/bash/manual/
ShellCheck：https://www.shellcheck.net/
Explain Shell：https://explainshell.com/
Bash 陷阱：https://mywiki.wooledge.org/BashPitfalls

## 延伸阅读

Shell 与 Linux 命令，见 001-getting-started/012-CommandLineBasics 文档。
CI/CD 中的 Shell，见 031-devops 模块。
文本处理工具，见 051-data-analysis 模块相关文档。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供 Linux 课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 bash 严格模式详解

set -e：命令非零退出即终止；注意管道与 if 条件的例外。
set -u：未定义变量报错；配合 ${var:-default} 提供默认。
set -o pipefail：管道任一段失败整体失败。
陷阱：set -e 在函数内与 && 链的行为差异；用 set -x 调试。

### 13.2 文本处理三剑客

grep：行匹配与正则；-E 扩展正则、-r 递归、-v 反选。
sed：流编辑；s/查找/替换/、-n p 打印、地址范围。
awk：列处理与统计；$NF 最后一列、BEGIN/END 块。
组合：管道串联三剑客完成日志统计报表。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| Shell 脚本编程基础 | 001-ShellBasics | 本文自身 |
