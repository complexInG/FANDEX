---
order: 10
title: shell 模块文档合集
module: 'shell'
category: 工具链
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：042-shell/001-ShellBasics.md ============ -->

## 1. 从"点菜"说起：Shell 是什么

### 1.1 一个餐厅的类比

想象你去一家餐厅（操作系统），你想让服务员（Shell）帮你做一件事：

- 你说："来一份红烧肉"（输入命令）
- 服务员去后厨让厨师做（调用系统程序）
- 服务员把菜端上来（返回结果）

**Shell 就是操作系统的"服务员"**：它读取你输入的命令，调用系统程序执行，并把结果返回给你。它既是**交互式工具**（你在终端里敲命令），也是**脚本语言**（把命令写进文件批量执行）。

Linux/macOS 默认是 bash（或 zsh），Windows 的 PowerShell 是另一套体系，但 Git Bash/WSL 可以运行 bash 脚本。

### 1.2 Shell 脚本的价值：做"胶水"

Shell 脚本的本质是**胶水**：把已有的小工具（ls、grep、awk、curl）串成自动化流程。

为什么需要 Shell 脚本？因为现实工作中有大量重复操作：

- 部署：拉代码 → 构建 → 重启服务
- 监控：检查日志 → 统计 → 告警
- 数据：下载 → 处理 → 汇总

这些操作一步步手敲会累死，写成脚本后一条命令搞定。**Shell 是运维与后端开发者的基本功**。

### 1.3 本章目标

本章是 Shell 的"第一课"，带你建立完整的基础框架。学完后你应该能：

1. 理解命令、变量、管道、控制流四大基础
2. 写出安全、健壮的简单脚本
3. 知道"生产脚本必须做什么"（严格模式）

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

每条命令执行后返回**退出码（exit code）**：0 表示成功，非 0 表示失败。`$?` 保存上一条命令的退出码。

```bash
ls /tmp
echo "退出码: $?"    # 0 = 成功
ls /不存在的目录
echo "退出码: $?"    # 2 = 失败
```

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

**规则**：

- 等号两侧**不能有空格**（`name = "alice"` 会被当成执行命令）
- 双引号内 `$var` 会展开，单引号内不会
- `$(...)` 是命令替换的现代写法（反引号已过时）

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

**管道是 Shell 最强大的能力**：无需中间文件，数据在进程间流动。`2>&1` 把标准错误合并到标准输出，便于统一记录日志。

### 2.4 第一个脚本

```bash
#!/bin/bash
# 输出 "Hello, World!"
echo "Hello, World!"

# 保存为 hello.sh 后：
chmod +x hello.sh   # 添加执行权限
./hello.sh          # 执行
```

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
```

**test 表达式速查**：

| 表达式 | 含义 |
| :--- | :--- |
| `-f 文件` | 文件存在且是普通文件 |
| `-d 目录` | 是目录 |
| `-z 字符串` | 字符串为空 |
| `-n 字符串` | 字符串非空 |
| `-eq / -lt / -gt` | 数字相等 / 小于 / 大于 |

**要点**：`[ ... ]` 是 `test` 命令的语法糖，`[[ ... ]]` 是 bash 扩展（支持正则与更安全比较）。变量必须加引号防止空值导致语法错误。

### 3.2 循环

```bash
#!/bin/bash
# for 循环：遍历文件
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

**要点**：`IFS=` 防止行首尾空白被吃掉，`-r` 防止反斜杠转义——这是读取文件行的标准姿势。

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

**要点**：`$1`、`$2` 是位置参数，`$*` 是所有参数；`local` 声明局部变量，避免污染全局。

## 4. 严格模式与错误处理

### 4.1 为什么需要严格模式

Shell 脚本默认"**宽容**"：命令失败不报错、未定义变量当空值、管道只看最后一段结果。这种宽容在生产环境是灾难——脚本会带着错误状态继续执行，产生半成品数据。

### 4.2 set -euo pipefail

**生产脚本必须在开头启用严格模式**：

```bash
#!/bin/bash
set -euo pipefail
```

| 选项 | 行为 |
| :--- | :--- |
| `set -e` | 任何命令失败立即退出脚本（避免"失败后继续执行"的连锁错误） |
| `set -u` | 使用未定义变量即报错（捕获拼写错误） |
| `set -o pipefail` | 管道中任意命令失败，整体视为失败（默认只看最后一个命令） |

### 4.3 trap 清理

```bash
#!/bin/bash
set -euo pipefail

cleanup() {
    echo "清理临时文件..."
    rm -f /tmp/tmp.$$
}
trap cleanup EXIT
```

`trap ... EXIT` 保证脚本无论正常结束还是出错退出都会执行清理函数——这是"无论成败都要清理"的标准姿势。

## 5. 常用文本处理（概览）

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
awk '{print $1, $3}' data.txt   # 打印第 1 列和第 3 列
awk 'END {print NR}' file.txt   # 统计行数
awk '{sum += $2} END {print sum}' data.txt  # 按第 2 列求和
```

**详细用法见本模块《文本处理三剑客》**。

## 6. 工程实践：部署脚本模板

把以上知识组合成第一个"生产级"脚本：

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

**要点**：

- `${1:?...}` 在缺少参数时直接报错退出
- `(cd ... && ...)` 在子 shell 中切换目录，不影响当前脚本
- 每步失败立即退出（set -e），不留半成品状态

## 7. 常见陷阱

**陷阱一：忘记引号。** `rm $file` 在文件名含空格时被拆成多个参数。所有变量加双引号。

**陷阱二：不用严格模式。** 命令失败继续执行，产生半成品状态。生产脚本必须 `set -euo pipefail`。

**陷阱三：`rm -rf` 误删。** 删除前先 `echo` 预览，使用 `set -u` 防止空变量导致 `rm -rf /`。

**陷阱四：脚本不可移植。** 避免 GNU 专属选项，或用 bash 明确 shebang。

**陷阱五：忽略退出码。** `command || { echo "失败"; exit 1; }` 显式处理。

<!-- ============ 文档分隔线：042-shell/002-CommandLineBasics.md ============ -->

## 1. 从"整理房间"说起

### 1.1 命令行的核心思维

想象你要整理一个房间（文件系统）：查看有哪些东西（ls）、建个新柜子（mkdir）、把文件挪进柜子（mv）、不要的扔掉（rm）。

**命令行（终端）就是和操作系统对话的界面**：你输入一条命令，Shell 解释并执行它。学会命令行不是为了背命令，而是掌握"**组合**"思维——用小命令拼出复杂操作。

### 1.2 命令的通用结构

```bash
命令名 [选项] [参数]
```

```bash
ls -l /home/user        # 命令 ls，选项 -l，参数 /home/user
mkdir -p backup/2026    # 选项 -p（自动创建父目录），参数 backup/2026
```

**规则**：

- 选项通常以 `-` 开头（短选项，可合并，如 `ls -la`）
- 长选项以 `--` 开头（如 `ls --all`）
- 每条命令执行后返回退出码：`0` 成功，非 `0` 失败，`echo $?` 查看

## 2. 目录导航

### 2.1 pwd 与 cd

```bash
pwd                     # 打印当前工作目录
cd /etc                 # 切换到 /etc（绝对路径）
cd ..                   # 返回上一级目录
cd ~                    # 回到当前用户家目录
cd -                    # 回到上一次所在目录
cd                      # 不带参数等价于 cd ~
```

绝对路径以 `/` 开头，相对路径以当前目录为起点。`cd -` 在频繁切换两个目录时非常实用。

### 2.2 路径速记符号

| 符号 | 含义 |
| --- | --- |
| `.` | 当前目录 |
| `..` | 上一级目录 |
| `~` | 当前用户家目录 |
| `~user` | 指定用户的家目录 |
| `-` | 上一次所在目录 |

## 3. 文件与目录操作

### 3.1 查看：ls

```bash
ls                      # 列出文件名
ls -l                   # 详细信息：权限、属主、大小、时间
ls -a                   # 包含隐藏文件（以 . 开头）
ls -lh                  # 大小以人类可读格式显示（K/M/G）
ls -lt                  # 按修改时间倒序排列
ls -R src               # 递归列出子目录
```

**读 `ls -l` 的第一列**：如 `-rw-r--r--`：

- 第 1 个字符：`-` 普通文件、`d` 目录、`l` 符号链接
- 后 9 位每 3 位一组：属主、属组、其他用户的 读(r)/写(w)/执行(x) 权限

### 3.2 创建：mkdir 与 touch

```bash
mkdir project           # 创建目录
mkdir -p a/b/c          # 递归创建多级目录，目录已存在也不报错
touch main.sh           # 文件不存在则创建，存在则更新时间戳
```

`-p` 是 mkdir 最常用的选项——脚本中创建目录结构时几乎必用，因为"已存在时不报错"的特性让脚本更健壮。

### 3.3 复制与移动：cp 与 mv

```bash
cp file.txt file.bak            # 复制文件
cp -r src/ dst/                 # 递归复制目录
cp -i file.txt file.bak         # 覆盖前询问（-i 交互确认）
mv old.txt new.txt              # 重命名
mv file.txt dir/                # 移动到目录
mv -i *.log logs/               # 批量移动，冲突时询问
```

- `cp` 复制目录必须加 `-r`（或 `-a` 保留属性）
- `mv` 兼具"重命名"和"移动"两种语义，比 cp 更快（同一文件系统内仅改指针）

### 3.4 删除：rm

```bash
rm file.txt             # 删除文件
rm -r dir/              # 递归删除目录
rm -f file.txt          # 强制删除，不询问
rm -rf dir/             # 递归强制删除（高危组合，慎用）
```

**安全习惯**：

- `rm` 删除不可恢复（无回收站）
- 先 `ls` 确认内容再删
- 变量必须加引号（`rm -rf "$dir"`），防止变量为空时执行 `rm -rf /`

## 4. 查找文件：find

find 按条件递归搜索，是文件查找的"主力军"：

```bash
find . -name "*.log"            # 按文件名匹配（支持通配符，需加引号）
find /var/log -type f           # 只找普通文件（-type d 找目录）
find . -size +10M               # 大于 10MB 的文件（-size -1k 小于 1KB）
find . -mtime -3                # 最近 3 天内修改的文件
find . -name "*.tmp" -delete    # 找到后直接删除
find . -name "*.py" -exec wc -l {} \;   # 对每个结果执行命令，{} 为占位符
```

**要点**：

- `-name` 模式必须加引号，否则通配符会被当前 Shell 先展开
- `-exec ... \;` 的 `\;` 是 find 命令的结束标记，必须转义；`{}` 代表当前匹配的文件路径
- 批量操作前建议先用 `-exec echo {} \;` 预览

## 5. 通配符

Shell 在把参数交给命令前，会先对通配符做"路径名展开"：

| 通配符 | 含义 | 示例 |
| --- | --- | --- |
| `*` | 匹配任意多个字符 | `*.txt` 匹配所有 txt 文件 |
| `?` | 匹配任意单个字符 | `file?.log` 匹配 file1.log |
| `[abc]` | 匹配括号内任一字符 | `file[12].log` 匹配 file1.log、file2.log |
| `[a-z]` | 匹配范围 | `[0-9]*` 匹配数字开头文件 |
| `{a,b}` | 花括号展开，逐个拼接 | `mv f.{txt,bak}` 等价两条命令 |

```bash
ls *.sh                  # 所有 .sh 脚本
rm log-2026-0?.txt       # log-2026-01.txt 到 log-2026-09.txt
touch report_{01..05}.md # 生成 report_01.md ... report_05.md
```

**通配符 ≠ 正则表达式**：通配符用于文件名匹配，`*` 表示"任意长度"；正则中 `*` 表示"前一项重复任意次"。若不需要展开，给模式加引号即可（`grep "*.c" file`）。

## 6. 帮助系统：man 与 --help

```bash
ls --help                # 快速查看选项摘要（所有 GNU 工具均支持）
man ls                   # 查看完整手册（q 退出，/ 搜索，n 跳到下一处）
man -k archive           # 关键字搜索手册页（等价于 apropos）
info coreutils           # info 格式文档，比 man 更详细
```

**要点**：`man` 手册分为若干节（如 1 命令、5 配置文件、8 系统管理命令），`man 5 crontab` 可查看特定节的文档。`--help` 适合快速回忆选项，`man` 适合系统学习。

## 7. 提高效率的小技巧

```bash
history                  # 查看命令历史
!!                       # 重复上一条命令
!100                     # 执行历史中第 100 条
Ctrl + R                 # 反向搜索历史命令
Tab                      # 命令与文件名自动补全（连按两次列出所有候选）
Ctrl + C                 # 终止当前命令
Ctrl + L                 # 清屏（等价于 clear）
```

**自动补全（Tab）是命令行效率的核心**：路径、命令、选项均可补全。习惯用 `Ctrl + R` 搜索历史，比重新输入快得多。

## 8. 常见陷阱

**陷阱一：目录名含空格。** `cd My Documents` 会被拆成两个参数，必须写成 `cd "My Documents"` 或 `cd My\ Documents`。

**陷阱二：`rm -rf` 加空变量。** `rm -rf $DIR` 中 `$DIR` 为空时等价于 `rm -rf`（危险）。始终写 `rm -rf "$DIR"`。

**陷阱三：通配符无匹配。** `ls *.log` 在没有 log 文件时会原样输出 `*.log` 并报错，可用 `nullglob` 选项或先检查。

**陷阱四：`find -exec` 忘记 `\;`。** 缺少结束符会立即报语法错误。

<!-- ============ 文档分隔线：042-shell/003-TextProcessingTools.md ============ -->

## 1. 从"三个工人"说起

### 1.1 三剑客分工

想象一条流水线，处理一叠文件（文本数据），三个工人各司其职：

| 工人 | 擅长 | 类比 |
| :--- | :--- | :--- |
| grep | 找出符合条件的行 | 质检员：筛出有问题的行 |
| sed | 按行替换、删除、插入 | 修理工：改写内容 |
| awk | 取列、统计、生成报表 | 会计：计算和汇总 |

三者都遵循"**读一行、处理一行、输出一行**"的流式模型，因此可以无缝接入管道：`cat file | grep ... | awk ... | sort ...`。

## 2. grep：行匹配（质检员）

### 2.1 基本用法

```bash
grep "error" app.log            # 输出包含 error 的行
grep -i "error" app.log         # 忽略大小写
grep -v "^#" nginx.conf         # 反选：排除以 # 开头的行
grep -c "error" app.log         # 只统计匹配行数
grep -n "error" app.log         # 显示行号
grep -o "[0-9.]*" app.log       # 只输出匹配的部分（而非整行）
grep -r "TODO" ./src            # 递归搜索目录
grep -l "error" /var/log/*.log  # 只列出包含匹配的文件名
```

**要点**：

- `-o` 在提取 IP、端口等片段时很常用
- `-l` 常用于定位"哪些文件有问题"
- grep 的退出码 0/1/2 分别表示"有匹配/无匹配/出错"，可在脚本中做条件判断

### 2.2 正则表达式

```bash
grep -E "err|warn" app.log      # -E 启用扩展正则，匹配 error 或 warn
grep -E "^[0-9]{4}-" app.log    # 以 4 位数字加 - 开头（如日期）
grep -E "(GET|POST) /api" log   # 分组匹配
grep "error\." app.log          # 基本正则：\. 匹配字面点号
```

**常用正则元字符**：

| 元字符 | 含义 |
| :--- | :--- |
| `^` / `$` | 行首 / 行尾 |
| `.` | 任意字符 |
| `*` | 前项重复 0 次以上 |
| `+` | 重复 1 次以上（需 -E） |
| `[]` | 字符集 |
| `\|` | 或 |

**建议**：统一加 `-E` 使用扩展正则，更易读。

## 3. sed：流编辑（修理工）

### 3.1 替换与删除

```bash
sed 's/old/new/' file           # 每行第一次出现的 old 替换为 new
sed 's/old/new/g' file          # 全局替换（g = global）
sed -i 's/old/new/g' file       # 直接写回原文件（-i = in-place）
sed -i.bak 's/old/new/g' file   # 写回前先备份为 file.bak
sed '/^#/d' file                # 删除注释行（d = delete）
sed '1,5d' file                 # 删除第 1 到第 5 行
```

**安全要点**：`sed -i` 修改原文件，务必先用不加 `-i` 的命令预览结果。

### 3.2 打印与插入

```bash
sed -n '10,20p' file            # 只打印第 10-20 行（-n 关闭默认输出）
sed -n '/ERROR/,/END/p' file    # 打印从 ERROR 到 END 之间的行
sed -i '3a\new_line' file       # 在第 3 行后插入一行（a = append）
sed -i '3i\new_line' file       # 在第 3 行前插入一行（i = insert）
```

sed 默认会把每一行都打印出来，`-n` 配合 `p` 才做到"只看想看的行"。

### 3.3 捕获分组

```bash
# 将 "name=alice" 改为 "name=ALICE"
echo "name=alice" | sed -E 's/(name=)(.*)/\1\U\2/'
# 提取日期：2026-08-01 -> 08/01
echo "2026-08-01" | sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2})/\2\/\3\/\1/'
```

`(...)` 捕获分组，`\1`、`\2` 引用分组内容，`\U` 将后续内容转大写。分组替换是 sed 进阶的核心能力。

## 4. awk：列处理与统计（会计）

awk 按"字段"工作：默认以空白（空格/制表符）分隔每一行，`$1`、`$2` 为第 1、2 列，`$0` 为整行。

### 4.1 取列与条件

```bash
awk '{print $1}' access.log          # 打印第一列（通常是 IP）
awk '{print $1, $9}' access.log      # 打印第 1 和第 9 列
awk -F: '{print $1}' /etc/passwd     # -F 指定分隔符为冒号
awk '$9 == 404 {print $1, $7}' log   # 只处理状态码为 404 的行
awk '$3 > 100 {print $0}' data.txt   # 第三列大于 100 的行
```

`-F` 可以指定任意分隔符，处理 `/etc/passwd`（冒号分隔）、CSV（逗号分隔）时必不可少。`$9 == 404` 是"条件 + 动作"的典型结构。

### 4.2 内置变量

| 内置变量 | 含义 |
| --- | --- |
| `NF` | 当前行的字段数（`$NF` 为最后一个字段） |
| `NR` | 已读入的行号（累计） |
| `FNR` | 当前文件中的行号 |
| `FS` | 输入字段分隔符（等价 -F） |
| `OFS` | 输出字段分隔符，默认空格 |

```bash
awk '{print NF, $NF}' data.txt    # 打印字段数和最后一个字段
awk 'NR==1 {print "表头:", $0}' f  # 处理第一行（表头）
awk -F, '{sum += $3} END {print "总和:", sum}' sales.csv
```

`$NF` 在日志分析中提取 URL、文件路径等"最后一列"时非常实用。`END { }` 块在所有行处理完后执行一次，用于输出统计结果。

### 4.3 统计与格式化

```bash
# 按第一列（IP）分组计数，输出前 10 名
awk '{cnt[$1]++} END {for (ip in cnt) print cnt[ip], ip}' access.log \
    | sort -rn | head -10

# 求平均值并格式化输出
awk '{sum += $2; n++} END {printf "平均: %.2f\n", sum/n}' data.txt
```

awk 的关联数组 `cnt[ip]` 天然适合分组统计，`for (ip in cnt)` 遍历所有键。`printf` 与 C 语言语法一致，`%.2f` 保留两位小数，适合生成报表。

## 5. 管道组合实战

三剑客单独使用威力有限，**串联起来才是生产级用法**。以下以 Nginx 访问日志 `access.log`（格式：IP 日期 请求 状态码 大小 来源）为例：

```bash
# 统计每个 IP 的访问次数，取 TOP 10
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -10

# 统计各状态码数量
awk '{print $9}' access.log | sort | uniq -c | sort -rn

# 找出 404 页面并去重
awk '$9 == 404 {print $7}' access.log | sort -u

# 最近 5 分钟的报错
grep "$(date -d '5 minutes ago' '+%d/%b/%Y:%H:%M')" error.log | wc -l
```

```text
输出示例（TOP IP 统计）：
    452 10.0.0.12
    301 10.0.0.33
    128 10.0.0.7
```

**核心套路**：`sort | uniq -c | sort -rn` 是"分组计数 + 排序"的标准三段式——先排序使相同行相邻，`uniq -c` 计数，再按数值倒序排。`$(...)` 命令替换让 grep 的匹配模式动态生成。

## 7. 常见误区

**误区一：grep、sed、awk 都要背下所有选项。** → 记住最常用的 10 个用法（本章已覆盖），其余用 `man` 查。

**误区二：正则表达式和通配符混淆。** → 文件名匹配用通配符，内容匹配用正则（grep -E）。

**误区三：`sed -i` 不预览直接改。** → 危险！先不加 `-i` 运行一次看输出，确认后再写回。

**误区四：awk 只用来"打印列"。** → awk 的真正威力是统计（关联数组 + END 块），打印列只是入门。

**误区五：什么都用三剑客硬写。** → 复杂逻辑（超过 20 行的 awk）应该用 Python/Perl，三剑客保持"短小精悍"。

<!-- ============ 文档分隔线：042-shell/004-ProcessJobControl.md ============ -->

## 1. 从"工厂车间"说起

### 1.1 进程是什么

想象一个工厂（操作系统），每台正在工作的机器就是一个**进程**：有机器编号（PID）、知道在干什么（命令行）、可以开也可以停。

**进程是操作系统中的运行实例**。每个进程有唯一 PID（进程号），并有父进程 PPID：

- **前台进程**：占据终端，命令执行期间终端不可用
- **后台进程**：命令末尾加 `&`，终端可继续输入
- **作业（job）**：Shell 对"一条命令及其子进程"的管理单元，前台作业、后台作业可切换

```bash
echo $$                 # 当前 Shell 的 PID
echo $PPID              # 当前 Shell 父进程的 PID
```

`$$` 常用于生成临时文件名（如 `/tmp/tmp.$$`），避免多进程冲突。

## 2. 查看进程：ps 与 top

### 2.1 ps：静态快照

```bash
ps                      # 只显示当前终端会话的进程
ps -ef                  # 全格式列出所有进程（BSD 风格：ps aux 亦可）
ps aux | grep nginx     # 查看 nginx 相关进程
ps -ef --sort=-%mem     # 按内存占用排序
pgrep -f "python app"   # 只输出匹配进程的 PID
pstree -p               # 树状显示进程父子关系
```

```text
ps aux 输出示例：
USER   PID %CPU %MEM  VSZ  RSS TTY STAT START TIME COMMAND
root     1  0.0  0.1 168M 13M ?    Ss   08:00 0:01 /sbin/init
```

**常用列含义**：

| 列 | 含义 |
| --- | --- |
| `PID` | 进程号 |
| `%CPU` / `%MEM` | 占用率 |
| `STAT` | 状态（S 睡眠、R 运行、Z 僵尸、T 停止） |
| `TIME` | 累计 CPU 时间 |

`pgrep` 按进程名取 PID，是脚本中"先查再杀"的标准前置命令。

### 2.2 top：动态监控

```bash
top                     # 每 3 秒刷新，按 CPU 排序（q 退出）
top -o %MEM             # 按内存排序
top -p 1234 -p 5678     # 只监控指定 PID
htop                    # 交互式增强版（需安装）
```

**top 交互快捷键**：`M` 按内存排序、`P` 按 CPU 排序、`k` 输入 PID 杀进程、`z` 高亮颜色。

## 3. 终止进程：kill

**kill 的本质是向进程发送"信号"**，进程可以自行决定如何响应：

| 信号 | 编号 | 行为 |
| --- | --- | --- |
| SIGHUP | 1 | 挂断；终端关闭时默认发给前台进程 |
| SIGINT | 2 | 键盘中断（Ctrl + C） |
| SIGTERM | 15 | 优雅终止（默认），进程可清理后退出 |
| SIGKILL | 9 | 强制杀死，进程无法拦截 |
| SIGSTOP | 19 | 暂停进程（Ctrl + Z 发送） |
| SIGCONT | 18 | 恢复暂停的进程 |

```bash
kill 1234                # 默认 SIGTERM，优雅终止
kill -9 1234             # SIGKILL 强制杀死（最后手段）
kill -TERM $(pgrep -f "myapp")   # 按名称动态取 PID 再杀
killall nginx            # 按进程名杀死所有匹配进程
pkill -f "python main"   # 按命令行全文匹配
```

**安全顺序**：

1. 优先用 `SIGTERM`（15）让程序自行清理（保存状态、释放端口）
2. 无效时才升级为 `SIGKILL`（9）
3. `kill -9` 会留下未清理的锁文件、socket 文件，是故障隐患

`pkill -f` 匹配完整命令行，比进程名更精准。

## 4. 后台任务与作业控制

### 4.1 & 与 jobs

```bash
sleep 100 &              # 放入后台运行，立即返回作业号 [1]
python server.py > log.txt 2>&1 &   # 后台运行并记录日志
jobs                     # 查看当前终端的所有作业
jobs -l                  # 显示作业的 PID
```

```text
[1]+  运行中               sleep 100 &
[2]-  运行中               python server.py > log.txt 2>&1 &
```

**要点**：

- 后台任务的输出仍会打印到终端，因此通常配合重定向把输出写入文件
- 作业号 `[1]`、`[2]` 与 PID 不同，作业控制命令（bg/fg/kill %n）使用作业号

### 4.2 bg、fg 与 Ctrl + Z

```bash
Ctrl + Z                 # 暂停当前前台任务，转为停止态
jobs                     # 此时显示 "已停止"
bg %1                    # 让作业 1 在后台继续运行
fg %1                    # 把作业 1 调回前台运行
fg                       # 不带参数恢复最近一个作业
kill %2                  # 终止作业 2（支持作业号）
```

**工作流程**：`Ctrl + Z 暂停 → bg 放后台 → 继续做别的事`。`fg`/`bg`/`kill` 均可使用 `%作业号` 定位作业。

**注意**：关闭终端后这些作业会收到 SIGHUP 被终止，需要 `nohup` 或 `disown` 保护。

## 5. 脱离终端运行

### 5.1 nohup 与 disown

```bash
nohup python app.py > app.log 2>&1 &
disown -h %1             # 让已启动的后台作业忽略 SIGHUP
disown -a                # 忽略所有后台作业
```

- `nohup`（no hangup）：让进程忽略挂断信号，即使关闭终端进程也不退出；输出默认写入 `nohup.out`，建议显式重定向到自己的日志文件
- `disown`：把作业从 Shell 作业表中移除，Shell 退出时不再给它发 SIGHUP

### 5.2 setsid 与终端复用器

```bash
setsid python app.py &   # 创建新会话，彻底脱离终端
tmux new -s web          # 开启 tmux 会话（重连不中断）
screen -S deploy         # 开启 screen 会话
```

- `setsid`：让进程成为新会话首领，连控制终端都没有
- `tmux`/`screen`：运维标配——在会话中跑长任务，断线重连后任务仍在，适合部署、编译等耗时操作

## 6. timeout：限时运行

```bash
timeout 10 ping 8.8.8.8          # 10 秒后自动终止
timeout -k 5 10 ./slow_job.sh    # 10 秒后先发 TERM，5 秒后仍不退则 KILL
timeout 30s curl -s https://api.example.com   # 请求限时
```

**要点**：

- `timeout` 防止命令"卡死"整个脚本，是脚本健壮性的关键工具
- 对可能无限等待的命令（网络请求、交互式程序）务必加超时
- 返回码 124 表示命令因超时被终止

## 7. 实战：一键重启服务

```bash
#!/bin/bash
set -euo pipefail
SERVICE="myapp"

# 1. 优雅停止：先 TERM，等待 10 秒，仍存活则 KILL
pkill -f "$SERVICE" || true
for i in $(seq 1 10); do
    pgrep -f "$SERVICE" > /dev/null || break
    sleep 1
done
pkill -9 -f "$SERVICE" 2>/dev/null || true

# 2. 启动并记录 PID
nohup python /opt/$SERVICE/main.py > /var/log/$SERVICE.log 2>&1 &
echo "新 PID: $!"

# 3. 健康检查
sleep 2
pgrep -f "$SERVICE" > /dev/null && echo "启动成功" || echo "启动失败"
```

**要点**：

- 生产环境的重启脚本必须"等进程真正退出再启动"，避免端口冲突
- `|| true` 容忍"没有匹配进程"的正常情况（否则 set -e 会让脚本退出）
- `$!` 保存刚启动后台进程的 PID

## 8. 常见误区

**误区一：kill 就是"杀死"进程。** → kill 是"发信号"，默认是优雅终止（SIGTERM），进程可以清理后退出；只有 `kill -9` 才是强制杀死。

**误区二：后台任务关了终端还能跑。** → 关闭终端会给后台任务发 SIGHUP，需要 `nohup` 或 `disown` 保护。

**误区三：`kill -9` 是最快最安全的。** → 恰恰相反，`kill -9` 跳过清理会留下脏状态。先 TERM，无效再 KILL。

**误区四：jobs 看不到就说明进程没了。** → jobs 只显示当前 Shell 的作业；别的终端/进程用 `ps` 查看。

<!-- ============ 文档分隔线：042-shell/005-EnvVariablesConfig.md ============ -->

## 1. 从"入职工牌"说起

### 1.1 环境变量是什么

想象一个新员工入职（进程启动），人事给他发一张**工牌（环境变量）**，上面写着：姓名、部门、工位号。员工到哪都能凭工牌被识别，不用每次重新解释"我是谁"。

**环境变量是"进程运行环境"中的一组键值对，被 Shell 与所有子进程继承**。它解决了"如何把配置传给程序"的问题：程序无需写死路径与配置，读取环境变量即可。

```bash
echo "你好, $USER，你当前在 $PWD"
```

### 1.2 环境变量 vs Shell 变量

| 类型 | 示例 | 能否被子进程继承 |
| --- | --- | --- |
| Shell 变量 | `name="alice"` | 否 |
| 环境变量 | `export NAME="alice"` | 是 |

**要点**：普通变量只在当前 Shell 有效；使用 `export` 后变为环境变量，会被子进程继承。

## 2. 查看与设置

```bash
env                     # 列出当前所有环境变量
printenv PATH           # 查看指定变量（比 echo $PATH 更准确）
echo "$HOME"            # 查看变量值
export EDITOR=vim       # 设置环境变量（当前会话有效）
export JAVA_HOME=/opt/jdk17   # 经典示例
unset JAVA_HOME         # 删除变量
env -i env              # 空环境运行命令（测试纯净环境）
```

**关键认知**：`export` 只影响当前 Shell 及其子进程，**不修改任何配置文件**，终端关闭即失效。想要"永久生效"必须写入配置文件（见第 6 节）。

## 3. PATH：命令查找路径

PATH 是**冒号分隔的目录列表**。执行 `ls` 时，Shell 按 PATH 顺序在各目录中查找可执行文件 `ls`：

```bash
echo "$PATH"
# 输出示例：/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
which ls                # 查看 ls 实际位于哪个目录
command -v node         # 推荐：查看命令路径（兼容性更好）
```

```bash
# 临时添加目录（当前会话）
export PATH="$HOME/bin:$PATH"

# 永久添加：写入 ~/.bashrc 再生效
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**要点**：

- 把自定义目录放在 `$PATH` **前面**优先级更高
- 永久修改必须**追加**到配置文件（不要覆盖原值）
- 修改后用 `source` 或重开终端生效
- PATH 中目录越靠前优先级越高，同名命令以先找到的为准

## 4. 常用特殊变量

| 变量 | 含义 |
| --- | --- |
| `HOME` | 当前用户家目录 |
| `USER` / `LOGNAME` | 当前用户名 |
| `SHELL` | 默认 Shell 路径 |
| `PWD` | 当前工作目录 |
| `OLDPWD` | 上一次所在目录 |
| `LANG` / `LC_ALL` | 系统语言与编码 |
| `TERM` | 终端类型 |
| `PS1` | 命令提示符格式 |
| `$?` | 上一条命令退出码 |
| `$$` | 当前 Shell 的 PID |

```bash
echo "你好, $USER，当前在 $PWD，语言 $LANG"
export LANG=zh_CN.UTF-8   # 设置中文环境
```

**要点**：`LANG` 影响乱码问题——中文显示乱码时优先检查 `LANG`/`LC_ALL` 是否为 UTF-8。`PS1` 定制提示符是"高手外观"的起点，但保持简单更实用。

## 5. 变量扩展语法

Bash 的 `${}` 扩展提供了默认值、必填校验等能力，**是脚本健壮性的基石**：

| 语法 | 含义 | 示例结果 |
| --- | --- | --- |
| `${var:-default}` | 未设置/为空时用 default | `echo ${PORT:-8080}` |
| `${var:=default}` | 未设置/为空时赋值并返回 | `${NAME:="world"}` |
| `${var:?msg}` | 未设置/为空时报错退出 | `${1:?缺少参数}` |
| `${var:+alt}` | 已设置且非空时用 alt | `${DEBUG:+开启}` |
| `${#var}` | 变量长度 | `${#name}` |
| `${var:2:4}` | 子串：从第 3 个字符取 4 个 | `${str:2:4}` |
| `${var//a/b}` | 全局替换 | `${path//\//-}` |
| `${var%%后缀}` | 去掉最长后缀 | `${file%%.tar.gz}` |

```bash
PORT="${PORT:-8080}"           # 未传环境变量时默认 8080
CONFIG="${CONFIG_FILE:?必须设置 CONFIG_FILE}"
name="FANDEX"
echo "${#name}"                # 5
echo "${name/DEX/dev}"         # FANdev（只替换第一处）
```

**要点**：`${var:-default}` 是脚本中最常用的扩展——让脚本"有默认值、可被环境变量覆盖"，这是可配置脚本的基本模式。`${var:?}` 让关键参数缺失时立即失败，避免带空值继续执行。

## 6. 配置文件加载顺序

bash 按"登录/非登录、交互/非交互"四种组合加载不同文件：

| 场景 | 加载顺序 |
| --- | --- |
| 登录 Shell（SSH 登录、`bash -l`） | `/etc/profile` → `~/.bash_profile`（或 `~/.bash_login`、`~/.profile`） |
| 非登录交互 Shell（打开终端） | `~/.bashrc` |
| 非交互 Shell（运行脚本） | 读取 `$BASH_ENV`，否则不读 |
| 退出登录 | `~/.bash_logout` |

```bash
cat ~/.bashrc          # 查看你的交互配置
cat ~/.profile         # 登录配置（macOS 默认）
```

**经典约定**：

- 环境变量放 `~/.profile`（登录时一次性加载）
- 别名与函数放 `~/.bashrc`（每次开终端加载）
- `~/.bash_profile` 通常写成先加载 `~/.bashrc`
- 脚本里设置的 export 不会影响父进程，只有 source 配置文件才能在当前 Shell 生效

## 7. 实践：正确管理环境变量

```bash
# 方案一：临时（当前会话）
export NODE_ENV=production

# 方案二：持久（推荐写入 ~/.bashrc 或 ~/.profile）
echo 'export NODE_ENV=production' >> ~/.bashrc && source ~/.bashrc

# 方案三：单条命令（不污染环境）
NODE_ENV=production node app.js

# 方案四：读取 .env 文件（不泄露到 shell 历史）
set -a; source .env; set +a
```

**四种方案的选择**：

- **方案三"命令前缀式"**只对单条命令生效，是运行一次性任务的首选
- **方案四**是脚本读取 `.env` 的常见手法：`set -a` 让 source 进来的变量自动 export，`set +a` 恢复
- `.env` 文件要加入 `.gitignore`，避免密钥入库（详见 039-engineering-practices《工程实践概述》）

## 8. 常见陷阱

**陷阱一：`export PATH=...` 忘记带上旧值。** `export PATH=/opt/bin` 会把 PATH 覆盖成只有 /opt/bin，连 ls 都找不到。务必写成 `$PATH` 拼接。

**陷阱二：变量赋值等号两侧加空格。** `name = "alice"` 会被解析成执行命令 `name`，应写 `name="alice"`。

**陷阱三：引号内不展开。** `echo '$HOME'` 输出字面量 `$HOME`，单引号内不做变量展开。

**陷阱四：修改配置文件不生效。** 改了 `~/.bashrc` 后未 `source` 也未重开终端。

<!-- ============ 文档分隔线：042-shell/006-ScriptDebugging.md ============ -->

## 1. 从"自动驾驶的刹车"说起

### 1.1 为什么需要调试体系

想象一辆车没有刹车（Shell 脚本默认行为）：踩错油门（命令失败）不会停下，反而继续加速（继续执行），最后撞墙（生产事故）。

**Shell 脚本默认"宽容"**：

- 命令失败不报错（继续执行）
- 未定义变量当空值（静默）
- 管道只看最后一段结果（前面的失败被忽略）

这种宽容在生产环境是灾难——脚本会带着错误状态继续执行，产生半成品数据。

### 1.2 调试体系的"三层防御"

| 层次 | 手段 | 作用 |
| :--- | :--- | :--- |
| 防患于未然 | `set -euo pipefail` | 让错误立刻暴露、当场停止 |
| 过程可视化 | `bash -x` / `set -x` | 跟踪每一步执行的细节 |
| 兜底清理 | `trap` | 无论成败都执行清理 |
| 静态检查 | shellcheck / shfmt | 在运行前发现错误 |

## 2. set -euo pipefail 详解

```bash
#!/bin/bash
set -euo pipefail
```

**逐个拆解**：

| 选项 | 完整写法 | 行为 |
| --- | --- | --- |
| `-e` | `set -o errexit` | 任何命令返回非零退出码立即退出脚本 |
| `-u` | `set -o nounset` | 引用未定义变量立即报错（不静默当空值） |
| `-o pipefail` | `set -o pipefail` | 管道中任一命令失败，整体退出码为失败 |

```bash
#!/bin/bash
set -euo pipefail

echo "第一步"
false                    # 返回非零，脚本在此退出
echo "这行永远不会执行"    # 不会执行
```

`false` 命令永远返回失败。在 `set -e` 下脚本第 3 行就终止，后续代码被跳过——这正是我们想要的"**快速失败**"。

### 2.1 例外与细节

```bash
# 1. 允许失败的场景：用 || 显式兜底
rm -f /tmp/x.tmp || true

# 2. 条件判断中失败是正常的（不触发退出）
if grep -q "error" log.txt; then
    echo "发现错误"
fi

# 3. 需要错误信息的场景：关闭 -e 后捕获
set +e
output=$(risky_command 2>&1)
status=$?
set -e
echo "退出码: $status"
```

**要点**：

- `set -e` 不是"所有失败都退出"：`if`/`while` 条件、`&&`/`||` 左侧、`!` 取反等上下文中的失败不会触发退出
- 真正"允许失败但想捕获结果"时，临时 `set +e` 再 `set -e` 是标准做法
- 注意 `set -u` 下 `$1` 若未传参会报错，需用 `${1:-}` 提供默认

## 3. bash -x：跟踪执行

```bash
bash -x script.sh       # 运行并打印每条命令的展开结果
bash -n script.sh       # 只做语法检查，不执行
bash -v script.sh       # 打印原始输入行（不展开变量）
```

```text
bash -x 输出示例：
+ set -euo pipefail
+ echo "开始"
开始
+ PORT=8080
+ grep -q "error" log.txt
+ echo "正常退出"
```

**要点**：`+` 开头的行是"展开后的命令"，能看出变量实际值、通配符实际匹配结果——绝大多数"为什么和我以为的不一样"问题在这里一目了然。

### 3.1 脚本内跟踪与 PS4

```bash
#!/bin/bash
export PS4='+ ${BASH_SOURCE}:${LINENO}: '   # 显示文件名与行号
set -x                    # 从这里开始跟踪
DEBUG=1
echo "值: $DEBUG"
set +x                    # 到这里结束跟踪
```

默认 `PS4` 只有一个 `+`，设置后输出变成 `+ script.sh:5: echo 值: 1`，定位问题行非常方便。**只在可疑片段前后开启/关闭 `set -x`**，比全程跟踪输出更清爽。

## 4. trap：注册信号处理

trap 在指定事件发生时执行自定义命令，是"无论成败都要清理"的实现手段：

```bash
#!/bin/bash
set -euo pipefail

tmpdir=$(mktemp -d)             # 创建临时目录
cleanup() {
    echo "[清理] 删除 $tmpdir"
    rm -rf "$tmpdir"
}
trap cleanup EXIT               # 脚本退出时执行 cleanup

# ... 业务逻辑，中途出错也会触发 cleanup ...
echo "处理中"
false                           # 触发 set -e 退出
```

**要点**：

- `trap ... EXIT` 是清理临时文件、锁文件的标准姿势——正常结束、出错退出、被信号终止都会执行
- `mktemp -d` 生成安全的临时目录，避免硬编码 `/tmp/xxx` 的冲突风险

### 4.1 常用事件

| 事件 | 触发时机 | 典型用途 |
| --- | --- | --- |
| `EXIT` | 脚本退出时（任何原因） | 清理临时文件 |
| `ERR` | 每条命令失败时 | 记录出错位置 |
| `INT` / `TERM` | 收到中断/终止信号 | 优雅停机 |
| `DEBUG` | 每条命令执行前 | 自实现跟踪 |

```bash
trap 'echo "出错于第 $LINENO 行"; exit 1' ERR
trap 'echo "收到 Ctrl+C，正在退出"; exit 130' INT
trap - EXIT              # 取消已注册的处理
trap -l                  # 列出所有信号
```

**要点**：`ERR` 陷阱配合 `$LINENO` 能在出错时打印行号，快速定位。信号陷阱要立即退出（`exit`），避免在信号处理中继续执行危险操作。

## 5. shellcheck：静态检查

shellcheck 是 Shell 脚本的"编译器警告"，能发现引号问题、未定义变量、常见陷阱：

```bash
shellcheck script.sh                 # 检查脚本
shellcheck -x deploy.sh              # 跟随 source 的文件一起检查
shellcheck -S warning script.sh      # 只显示 warning 及以上级别
```

```text
示例输出：
In script.sh line 7:
    rm -rf $tmpdir
           ^-----^ SC2086: Double quote to prevent globbing and word splitting.
```

**要点**：

- SC2086（变量未加引号）是最常见的警告，修复：`rm -rf "$tmpdir"`
- shellcheck 的警告码（SC 编号）可在官网按编号检索详细说明，是学习 Shell 陷阱的最佳教材
- 安装方式：`apt install shellcheck` / `brew install shellcheck`，也可在编辑器装插件实时检查

## 6. shfmt：统一格式

shfmt 自动格式化脚本，让团队风格一致：

```bash
shfmt -w script.sh      # 格式化并写回
shfmt -i 4 -w script.sh # 缩进 4 空格
shfmt -d script.sh      # 只显示差异（diff）
```

**要点**：shfmt 处理缩进、空格、换行等风格问题，与 shellcheck 功能互补：**shfmt 管"好不好看"，shellcheck 管"对不对"**。两者配合 CI 可以在提交前自动检查。

## 7. 调试清单：遇到问题按顺序走

1. 先 `bash -n script.sh` 排除语法错误；
2. 再 `shellcheck script.sh` 修复静态问题；
3. 运行时 `bash -x script.sh` 观察实际展开；
4. 用 `PS4='+ $LINENO: '` 定位出错行；
5. 对可疑片段 `set -x` / `set +x` 局部跟踪；
6. 关键处 `echo "DEBUG: var=$var"` 打印中间值（或写入日志文件）；
7. 生产脚本必须 `set -euo pipefail` + `trap cleanup EXIT`。

## 8. 常见误区

**误区一：`set -e` 会让所有失败都退出。** → 不是。`if` 条件、`&&`/`||` 左侧的失败不会触发退出——这正是设计如此（让脚本可以"尝试后判断"）。

**误区二：调试信息随便 print。** → 用 `set -x` 或条件化调试（`${DEBUG:+...}`），生产环境别留一堆 `echo` 垃圾。

**误区三：shellcheck 是"建议"，可看可不看。** → 多数 SC 警告对应真实陷阱（引号、未定义变量），是"生产脚本别踩坑"的免费教材。

**误区四：`trap` 只在出错时触发。** → `trap ... EXIT` 无论正常结束还是出错退出都会触发，是"无论成败都要清理"的标准姿势。

<!-- ============ 文档分隔线：042-shell/007-FunctionsArguments.md ============ -->

## 1. 从"菜谱里的步骤分组"说起

### 1.1 为什么需要函数

想象一本菜谱（脚本）：如果没有"分组步骤"的概念，每道菜的"洗菜、切菜、下锅"都要完整写一遍，菜谱会越来越长、越来越难改。

**函数把"一段可复用的逻辑"打包命名**，解决三件事：

| 问题 | 函数方案 |
| --- | --- |
| 同一段逻辑写多遍 | 定义一次，多处调用 |
| 脚本越来越长难维护 | 按职责拆分成命名块 |
| 无法测试局部逻辑 | 函数可独立调用验证 |

```bash
#!/bin/bash
greet() {
    echo "你好, $1"
}
greet "FANDEX"          # 输出：你好, FANDEX
```

**要点**：

- bash 函数两种写法：`name() { ... }` 或 `function name { ... }`，前者更通用
- 函数体最后一条命令的退出码即函数的退出码
- 定义必须在调用之前（bash 逐行解释执行）

## 2. 作用域：local 与全局

```bash
#!/bin/bash
count=0                 # 全局变量

increment() {
    local step="${1:-1}"    # local 声明局部变量
    count=$((count + step)) # 局部函数内可直接改全局
    local temp="临时值"      # 函数外访问不到
    echo "内部 temp=$temp"
}

increment 2
echo "count=$count"     # count=2，全局被修改
echo "temp=$temp"       # 空：函数外访问不到 temp
```

**要点**：

- 默认情况下函数内外变量互通（bash 没有"自动局部"）
- `local` 声明变量只在函数内可见，防止污染全局命名空间——**这是函数式脚本的纪律**
- `$(( ))` 是算术运算语法

## 3. 位置参数

### 3.1 基础

```bash
#!/bin/bash
echo "脚本名: $0"
echo "第 1 个参数: $1"
echo "第 2 个参数: $2"
echo "参数个数: $#"
```

```text
执行 ./demo.sh a b c 输出：
脚本名: ./demo.sh
第 1 个参数: a
第 2 个参数: b
参数个数: 3
```

**要点**：`$0` 是脚本名（函数内则是函数名），`$1`-`$9` 是前 9 个位置参数，第 10 个起必须写 `${10}`。`$#` 是参数个数，脚本入口处用它做参数数量校验。

### 3.2 $@ 与 $* 的区别

| 写法 | 行为 |
| --- | --- |
| `$@` | 每个参数独立，可含空格（推荐） |
| `"$@"` | 引号包裹：逐参数传递，最安全 |
| `$*` | 所有参数合并为一个字符串 |
| `"$*"` | 用 IFS 首字符连接成一个字符串 |

```bash
print_all() {
    echo "用 \"\$@\" 遍历:"
    for arg in "$@"; do
        echo "  [$arg]"
    done
}
print_all "a b" c
```

```text
输出：
用 "$@" 遍历:
  [a b]
  [c]
```

**要点**：`"$@"` 是唯一"不丢参数"的写法——参数 `a b` 保持为一个整体。`for x in $@` 或 `"$*"` 会把含空格的参数拆散，是经典 Bug 来源。**规则**：需要逐个处理用 `"$@"`，需要合并展示用 `"$*"`。

### 3.3 shift：消费参数

```bash
#!/bin/bash
while [ $# -gt 0 ]; do
    echo "处理参数: $1"
    shift               # 左移一位：$2 变成 $1
done
```

```text
./loop.sh a b c 输出：
处理参数: a
处理参数: b
处理参数: c
```

`shift [n]` 丢弃前 n 个参数（默认 1），配合 `while [ $# -gt 0 ]` 可逐个消费参数，是手写参数解析的基础。注意 `set -u` 下 `$1` 为空时会报错，循环前先判断 `$#`。

## 4. getopts：标准参数解析

getopts 是 bash 内置的参数解析器，支持单字母选项、可带参数选项、组合选项：

```bash
#!/bin/bash
usage() {
    echo "用法: $0 -f <文件> [-v] [-o <目录>]"
    echo "  -f  必填：输入文件"
    echo "  -o  输出目录（默认 ./out）"
    echo "  -v  显示版本"
    exit 1
}

out_dir="./out"
verbose=0
while getopts "f:o:vh" opt; do
    case "$opt" in
        f) file="$OPTARG" ;;        # OPTARG 保存选项参数
        o) out_dir="$OPTARG" ;;
        v) verbose=1 ;;
        h) usage ;;
        *) usage ;;                 # 未知选项
    esac
done
shift $((OPTIND - 1))               # 跳过已解析的选项

[ -n "${file:-}" ] || usage          # 必填参数校验

echo "文件: $file, 输出: $out_dir, 详细: $verbose"
echo "剩余位置参数: $*"
```

```text
./tool.sh -f data.txt -o ./tmp extra_arg 输出：
文件: data.txt, 输出: ./tmp, 详细: 0
剩余位置参数: extra_arg
```

**getopts 关键机制**：

- 选项字符串 `f:o:vh` 中，带 `:` 的选项（f、o）需要额外参数，值存入 `$OPTARG`；不带冒号的（v、h）是开关
- `OPTIND` 记录已消费到第几个参数，`shift $((OPTIND - 1))` 把剩余内容留给位置参数
- `*)` 分支处理非法选项
- getopts 支持 `-fv` 组合，比手写 shift 解析健壮得多

## 5. 返回值与输出捕获

函数通过两种方式"返回"结果：**退出码（数值状态）**与**标准输出（数据）**。

```bash
#!/bin/bash
is_running() {
    pgrep -f "$1" > /dev/null
}
is_running nginx && echo "nginx 在运行" || echo "nginx 未运行"

# 输出捕获：把函数 stdout 当数据用
get_date() { date "+%Y-%m-%d"; }
today=$(get_date)
echo "今天是 $today"
```

**要点**：

- `is_running` 直接复用 `pgrep` 的退出码，函数无需 `return` 语句
- 要"返回数据"时，让函数打印到标准输出，调用方用 `$(...)` 捕获——这是 bash 实现"函数返回值"的惯用法
- 显式 `return n` 只能返回 0-255 的整数状态码

## 6. 综合示例：带默认值的日志函数

```bash
#!/bin/bash
set -euo pipefail

# 日志函数：支持级别、时间戳、可选输出文件
log() {
    local level="${1:-INFO}"
    shift
    local ts
    ts=$(date "+%F %T")
    local msg="$*"
    local line="[$ts] [$level] $msg"
    echo "$line"
    if [ -n "${LOG_FILE:-}" ]; then
        echo "$line" >> "$LOG_FILE"
    fi
}

LOG_FILE=/var/log/app.log
log INFO "服务启动"
log WARN "配置缺失，使用默认值"
log ERROR "连接超时"
```

```text
输出：
[2026-08-01 14:30:22] [INFO] 服务启动
[2026-08-01 14:30:22] [WARN] 配置缺失，使用默认值
[2026-08-01 14:30:22] [ERROR] 连接超时
```

**要点**：

- 函数内部先 `local` 捕获参数再 `shift`，是"选项式"函数的标准写法
- 日志输出同时写终端与文件（`LOG_FILE` 用 `${VAR:-}` 提供空默认，避免 `set -u` 报错）
- 此函数可直接复制到任何脚本使用

## 7. 常见陷阱

**陷阱一：函数未定义就调用。** bash 顺序执行，定义必须在使用之前。

**陷阱二：`return` 想返回字符串。** `return` 只支持 0-255 整数状态码，返回数据请用 stdout + `$(...)`。

**陷阱三：`$@` 不加引号。** `for x in $@` 会拆散含空格参数，务必写 `"$@"`。

**陷阱四：循环内调用函数修改全局变量。** 意外改变循环变量（如 `i`），函数内尽量 `local`。

<!-- ============ 文档分隔线：042-shell/008-PracticalScripts.md ============ -->

## 1. 从"菜谱集"说起

前 7 篇文档讲解了命令、三剑客、进程、环境变量、调试、函数。本篇用 **4 个完整案例**串联全部知识点——就像一本菜谱集，把前面的"单个技巧"组合成"完整菜品"。

**生产级脚本的共同特征**：

1. 开头 `set -euo pipefail`，失败立即停止（006 篇）
2. 参数有默认值或必填校验，`getopts` 解析（007 篇）
3. 日志函数统一输出，带时间戳（007 篇）
4. 关键动作可预览（dry-run），删除前确认（002 篇）
5. 通过 `shellcheck` 静态检查（006 篇）

## 2. 案例一：部署脚本模板

```bash
#!/bin/bash
# deploy.sh - 通用部署脚本（前端/后端通用模板）
set -euo pipefail

APP_DIR="${APP_DIR:-/opt/myapp}"
BACKUP_DIR="${BACKUP_DIR:-/opt/backups}"
LOG_FILE="/var/log/deploy.log"

# 日志函数：输出到终端与日志文件
log() {
    local level="$1"; shift
    local line
    line="$(date '+%F %T') [$level] $*"
    echo "$line"
    echo "$line" >> "$LOG_FILE"
}

# 使用说明
usage() {
    echo "用法: $0 -v <版本号> [-d]"
    echo "  -v  必填：要部署的版本（git tag 或 commit）"
    echo "  -d  演练模式：只打印将要执行的命令"
    exit 1
}

dry_run=0
version=""
while getopts "v:dh" opt; do
    case "$opt" in
        v) version="$OPTARG" ;;
        d) dry_run=1 ;;
        *) usage ;;
    esac
done

[ -n "$version" ] || usage   # 版本号必填

run() {                       # 统一执行入口，支持演练模式
    if [ "$dry_run" = "1" ]; then
        echo "[演练] $*"
    else
        "$@"
    fi
}

log INFO "开始部署 v$version (dry_run=$dry_run)"

# 1. 拉取代码
run git -C "$APP_DIR" fetch --tags
run git -C "$APP_DIR" checkout "$version"

# 2. 备份当前版本（带时间戳）
ts="$(date '+%Y%m%d-%H%M%S')"
run tar -czf "$BACKUP_DIR/myapp-$ts.tar.gz" -C "$APP_DIR" --exclude=.git .
log INFO "已备份到 $BACKUP_DIR/myapp-$ts.tar.gz"

# 3. 构建
run bash -c "cd '$APP_DIR' && npm ci && npm run build"

# 4. 重启服务
if [ "$dry_run" = "0" ]; then
    systemctl restart myapp
    sleep 2
    systemctl is-active myapp || { log ERROR "服务启动失败"; exit 1; }
fi

log INFO "部署完成 v$version"
```

**设计亮点**：

- `run()` 封装所有危险命令，`-d` 演练模式只打印不执行——**部署前先演练是避免误操作的关键**
- 备份使用 `tar -czf` 带时间戳命名，`--exclude=.git` 排除仓库目录
- `systemctl is-active` 做服务健康校验，失败即退出
- 将脚本放入 crontab 或 CI 即可自动部署

## 3. 案例二：日志分析报表

```bash
#!/bin/bash
# log-report.sh - 生成访问日志分析日报
set -euo pipefail

LOG="${1:-/var/log/nginx/access.log}"     # 默认 nginx 日志路径
OUT="${2:-/tmp/report_$(date +%F).txt}"   # 默认输出文件

# 三个"为什么"：PV 多少、谁在访问、出过什么问题
{
    echo "============================================"
    echo " 访问日报 $(date '+%F %T')"
    echo "============================================"

    echo "1. 总请求数: $(wc -l < "$LOG")"

    echo "2. 独立 IP 数: $(awk '{print $1}' "$LOG" | sort -u | wc -l)"

    echo "3. 状态码分布:"
    awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn

    echo "4. 访问量 TOP 10 IP:"
    awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn | head -10

    echo "5. 访问量 TOP 10 页面:"
    awk '{print $7}' "$LOG" | sort | uniq -c | sort -rn | head -10

    echo "6. 404 错误页面（去重）:"
    awk '$9 == 404 {print $7}' "$LOG" | sort -u

    echo "7. 平均每秒请求数:"
    awk 'END {printf "  %.1f req/s\n", NR/3600}' "$LOG"
} | tee "$OUT"

echo "报表已生成: $OUT"
```

**设计亮点**：

- `{ ... }` 分组把多段输出合并成一次管道，`tee` 同时写文件与终端
- 所有统计复用 003 篇的三段式 `sort | uniq -c | sort -rn`
- 此脚本可放入 crontab 每天 0 点生成日报，运维同学每天查看即可掌握站点健康度

## 4. 案例三：定时备份脚本

```bash
#!/bin/bash
# backup.sh - 备份指定目录，保留最近 N 份
set -euo pipefail

SRC="${1:?用法: $0 <源目录> [保留份数]}"
KEEP="${2:-7}"
BACKUP_ROOT="/backups/$(basename "$SRC")"
LOG="/var/log/backup.log"

mkdir -p "$BACKUP_ROOT"
stamp="$(date '+%Y%m%d-%H%M%S')"
archive="$BACKUP_ROOT/$(basename "$SRC")-$stamp.tar.gz"

log() { echo "$(date '+%F %T') $*" >> "$LOG"; }

log "开始备份 $SRC -> $archive"

# 1. 打包（--exclude 排除缓存与临时文件）
tar -czf "$archive" \
    --exclude='*/node_modules' \
    --exclude='*/.git' \
    --exclude='*.log' \
    -C "$(dirname "$SRC")" "$(basename "$SRC")"

# 2. 校验压缩包完整性
tar -tzf "$archive" > /dev/null && log "压缩包校验通过"

# 3. 清理过期备份（按时间排序，保留最近 KEEP 份）
ls -1t "$BACKUP_ROOT"/*.tar.gz 2>/dev/null | tail -n +$((KEEP + 1)) | while read -r old; do
    echo "删除过期备份: $old"
    rm -f "$old"
done

log "备份完成，共 $(du -h "$archive" | cut -f1)"
```

```bash
# 配合 crontab 每天凌晨 2 点执行（crontab -e 编辑）
0 2 * * * /usr/local/bin/backup.sh /var/www/myapp 7 >> /var/log/backup_cron.log 2>&1
```

**设计亮点**：

- `tar -tzf` 列出包内容校验可读性，**防止备份损坏而不知情**
- 过期清理用 `ls -1t`（按时间倒序）+ `tail -n +K` 挑出"第 K 份之后的旧包"逐一删除，实现滚动保留
- crontab 五个字段分别表示分、时、日、月、星期，`0 2 * * *` 即每天 2 点
- **备份脚本务必先本地验证一轮再上定时任务**

## 5. 案例四：文件批量处理

```bash
#!/bin/bash
# batch-process.sh - 批量重命名与归类（演练模式安全预览）
set -euo pipefail

# 场景 1：批量重命名，把 IMG_*.JPG 改为 2026-photo-NNNN.jpg
counter=1
for file in IMG_*.JPG; do
    [ -e "$file" ] || continue          # 无匹配文件时跳过
    new_name=$(printf "2026-photo-%04d.jpg" "$counter")
    echo "重命名: $file -> $new_name"
    mv "$file" "$new_name"
    counter=$((counter + 1))
done

# 场景 2：按扩展名归类到子目录
for file in *; do
    [ -f "$file" ] || continue
    ext="${file##*.}"                   # 取扩展名
    case "$ext" in
        jpg|png|gif) target="images" ;;
        md|txt)      target="docs" ;;
        sh|py)       target="scripts" ;;
        *)           target="misc" ;;
    esac
    mkdir -p "$target"
    mv "$file" "$target/"
done
echo "批量处理完成"
```

**设计亮点**：

- `[ -e "$file" ] || continue` 是"通配符可能无匹配"的防御（结合 002 篇陷阱三）
- `printf "%04d"` 生成四位补零序号
- `${file##*.}` 用参数扩展取扩展名，比 `sed`/`awk` 更轻快
- **批量脚本一律先打印再执行（演练模式），确认无误后再去掉 echo 落盘**

## 6. 脚本上线检查清单

写完一个脚本、准备投入使用前，按清单检查：

1. `bash -n script.sh` 语法检查；
2. `shellcheck script.sh` 静态检查，0 warning；
3. 用 `-d` 或注释掉危险命令先演练一遍；
4. 在临时目录用测试数据跑通；
5. 检查 `set -euo pipefail`、日志函数、参数校验是否齐全；
6. 正式使用后保留日志，便于事后追溯。

## 7. 常见误区

**误区一：生产脚本不设演练模式。** → 删除、重启、覆盖等危险操作，没有 dry-run 就是在"赌运气"。

**误区二：备份不做校验。** → `tar -tzf` 校验只花一秒钟，却能避免"备份了但损坏了"的灾难。

**误区三：脚本写完就上 crontab。** → 定时任务没有交互确认，必须先在命令行手工验证。

**误区四：删过期文件不留余地。** → 保留份数（KEEP）设大一点，宁多勿少——删除容易恢复难。

<!-- ============ 文档分隔线：042-shell/009-TextProcessing.md ============ -->

## cat 拼接查看

**基本用法:查看文件内容**
`cat [选项] <文件>`

```bash
# 显示文件内容并带行号
cat -n main.py

# 合并多个文件
cat header.md body.md footer.md > full.md
```

---

## head/tail 头尾查看

**基本用法:查看文件头部**
`head [选项] <文件>`

```bash
# 查看前 20 行
head -n 20 README.md

# 查看前 50 字节
head -c 50 data.bin
```

---

**基本用法:查看文件尾部**
`tail [选项] <文件>`

```bash
# 查看末尾 30 行
tail -n 30 error.log

# 实时追踪日志新增内容
tail -f application.log
```

---

## less 分页浏览

**基本用法:分页查看大文件**
`less <文件>`

```bash
# 分页查看(快捷键:q 退出,/ 搜索,n 下一个)
less large.log
```

---

## grep 文本搜索

**基本用法:搜索匹配行**
`grep [选项] <模式> <文件>`

```bash
# 显示行号并忽略大小写
grep -in "error" app.log

# 显示匹配行前后各 2 行
grep -C 2 "exception" trace.log

# 仅输出匹配部分
grep -oE "[0-9]{1,3}(\.[0-9]{1,3}){3}" access.log

# 反向匹配(显示不包含的行)
grep -v "DEBUG" app.log
```

---

## sed 流编辑

**基本用法:替换文本**
`sed [选项] <脚本> <文件>`

```bash
# 将第一个 old 替换为 new(原地预览)
sed 's/old/new/' file.txt

# 全局替换并打印
sed 's/foo/bar/g' file.txt

# 原地修改文件并备份
sed -i.bak 's/8080/3000/g' config.ini

# 删除空行
sed '/^$/d' messy.txt

# 删除第 3 到 5 行
sed '3,5d' data.txt
```

---

## awk 列处理

**基本用法:按列提取**
`awk [选项] <脚本> <文件>`

```bash
# 打印第一列
awk '{print $1}' access.log

# 指定分隔符打印第二列
awk -F: '{print $2}' users.txt

# 条件过滤:第二列大于 100
awk '$2 > 100 {print $1, $2}' scores.txt

# 统计行数
awk 'END {print NR}' file.txt

# 求第三列总和
awk '{sum += $3} END {print sum}' sales.csv
```

---

## cut 切分

**基本用法:按分隔符切分**
`cut [选项] <文件>`

```bash
# 按冒号切分取第一字段
cut -d: -f1 /etc/passwd

# 取第 1 到 3 字符
cut -c1-3 names.txt
```

---

## sort/uniq 排序去重

**基本用法:排序**
`sort [选项] <文件>`

```bash
# 数值倒序排序
sort -nr scores.txt

# 按第三列排序
sort -k3 -n data.txt
```

---

**基本用法:去重**
`uniq [选项] <文件>`

```bash
# 配合 sort 去重并计数
sort items.txt | uniq -c | sort -nr
```

---

## wc 统计

**基本用法:统计行数字数**
`wc [选项] <文件>`

```bash
# 统计行数
wc -l README.md

# 统计单词数
wc -w article.md
```

<!-- ============ 文档分隔线：042-shell/010-PipeRedirect.md ============ -->

## 标准输出重定向

**基本用法:覆盖写入文件**
`<命令> > <文件>`

```bash
# 把命令输出写入文件(覆盖)
ls -la > files.txt

# 把错误信息也写入同一文件
ls /nope > result.txt 2>&1
```

---

**基本用法:追加写入文件**
`<命令> >> <文件>`

```bash
# 追加日志到末尾
echo "done" >> build.log
```

---

## 标准输入重定向

**基本用法:从文件读取输入**
`<命令> < <文件>`

```bash
# 从文件读取内容统计行数
wc -l < data.txt
```

---

## 标准错误重定向

**基本用法:重定向错误输出**
`<命令> 2> <文件>`

```bash
# 仅丢弃错误信息
find / -name "*.conf" 2> /dev/null

# 错误追加到日志
make build 2>> error.log
```

---

**基本用法:合并标准输出与错误**
`<命令> &> <文件>`

```bash
# 同时收集输出和错误到同一文件
npm install &> install.log
```

---

## 管道

**基本用法:连接命令**
`<命令1> | <命令2>`

```bash
# 翻页查看长输出
ls -la | less

# 过滤后再统计
grep "ERROR" app.log | wc -l

# 多级管道处理
cat access.log | grep "404" | awk '{print $7}' | sort | uniq -c | sort -nr | head
```

---

## tee 双向输出

**基本用法:同时输出到屏幕和文件**
`<命令> | tee <文件>`

```bash
# 屏幕显示并写入日志
make test | tee test.log

# 追加模式
echo "step2" | tee -a progress.log
```

---

## xargs 参数传递

**基本用法:把输入转为参数**
`<命令> | xargs <命令>`

```bash
# 批量删除查找到的文件
find . -name "*.tmp" | xargs rm -f

# 每行一个参数执行
cat urls.txt | xargs -n1 curl -I

# 指定替换位置
ls *.bak | xargs -I{} mv {} archive/

# 并行执行 4 个
find . -name "*.png" | xargs -P4 -n1 optipng
```

---

## 进程替换

**基本用法:对比两个命令输出**
`diff <(<命令1>) <(<命令2>)`

```bash
# 对比两个目录文件列表
diff <(ls dir1) <(ls dir2)
```

---

## here document

**基本用法:多行输入**
`<命令> << <结束标记>`

```bash
# 多行写入文件
cat > note.txt <<EOF
第一行内容
第二行内容
EOF
```

<!-- ============ 文档分隔线：042-shell/011-ProcessManage.md ============ -->

## 查看进程

**基本用法:查看进程快照**
`ps [选项]`

```bash
# 查看所有进程详细信息
ps -ef

# BSD 风格全格式列表
ps aux

# 查找指定进程
ps -ef | grep nginx
```

---

**基本用法:实时进程监控**
`top [选项]`

```bash
# 启动交互式监控
top

# 按内存使用排序
top -o %MEM

# 仅监控指定用户
top -u deploy
```

---

**基本用法:更友好的监控**
`htop`

```bash
# 彩色交互式监控(需安装)
htop

# 树状查看进程
htop -t
```

---

## 后台运行

**基本用法:命令放后台执行**
`<命令> &`

```bash
# 后台运行脚本
python train.py &

# 查看后台任务列表
jobs

# 把最近后台任务调到前台
fg %1
```

---

**基本用法:免挂断运行**
`nohup <命令> &`

```bash
# 关闭终端后仍运行
nohup node server.js > app.log 2>&1 &
```

---

## 终止进程

**基本用法:发送信号**
`kill [选项] <PID>`

```bash
# 优雅终止
kill 1234

# 强制杀死
kill -9 1234

# 发送指定信号
kill -SIGTERM 1234
```

---

**基本用法:按名称杀进程**
`killall <进程名>`

```bash
# 杀死所有同名进程
killall nginx

# pkill 按模式匹配
pkill -f "python train"
```

---

## 资源监控

**基本用法:查看内存使用**
`free [选项]`

```bash
# 以 MB 显示
free -m

# 每秒刷新
free -s 1
```

---

**基本用法:查看磁盘使用**
`df [选项]`

```bash
# 人类可读格式
df -h
```

---

**基本用法:查看目录大小**
`du [选项] <路径>`

```bash
# 显示各目录大小并汇总
du -sh *

# 按大小排序找出最大目录
du -sh * | sort -rh | head
```

---

## 系统信息

**基本用法:查看系统负载**
`uptime`

```bash
# 显示运行时间与平均负载
uptime
```

---

**基本用法:Windows 进程管理**
`Get-Process`

```powershell
# 列出所有进程
Get-Process

# 按名称查找
Get-Process node

# 停止进程
Stop-Process -Name node -Force
```

<!-- ============ 文档分隔线：042-shell/012-CompressArchive.md ============ -->

## tar 归档

**基本用法:创建归档**
`tar [选项] <归档名> <文件>`

```bash
# 打包为 .tar
tar -cvf archive.tar src/

# 打包并 gzip 压缩(.tar.gz)
tar -czvf project.tar.gz dist/

# 打包并 bzip2 压缩(压缩率更高)
tar -cjvf project.tar.bz2 dist/

# 打包并 xz 压缩
tar -cJvf project.tar.xz dist/
```

---

**基本用法:查看归档内容**
`tar -tvf <归档名>`

```bash
# 列出 tar.gz 内容不解压
tar -tzvf project.tar.gz
```

---

**基本用法:解压归档**
`tar -xvf <归档名>`

```bash
# 解压到当前目录
tar -xzvf project.tar.gz

# 解压到指定目录
tar -xzvf project.tar.gz -C /opt/

# 仅解压指定文件
tar -xzvf project.tar.gz path/to/file
```

---

## gzip/bzip2 单文件压缩

**基本用法:gzip 压缩**
`gzip [选项] <文件>`

```bash
# 压缩(原文件被替换为 .gz)
gzip large.log

# 保留原文件压缩
gzip -k large.log

# 解压
gzip -d large.log.gz
```

---

**基本用法:bzip2 压缩**
`bzip2 <文件>`

```bash
# 压缩为 .bz2
bzip2 bigfile.dat

# 解压
bzip2 -d bigfile.dat.bz2
```

---

## zip/unzip

**基本用法:zip 压缩目录**
`zip [选项] <归档名> <路径>`

```bash
# 递归压缩目录
zip -r archive.zip src/

# 添加密码保护
zip -r -e secret.zip docs/

# 排除文件
zip -r app.zip . -x "*/node_modules/*"
```

---

**基本用法:unzip 解压**
`unzip [选项] <归档名>`

```bash
# 解压到当前目录
unzip archive.zip

# 解压到指定目录
unzip archive.zip -d /tmp/out

# 查看内容不解压
unzip -l archive.zip
```

---

## 7z 七格式

**基本用法:7z 压缩解压**
`7z <子命令> <归档名> <文件>`

```bash
# 压缩为 7z 格式
7z a archive.7z src/

# 解压
7z x archive.7z

# 列出内容
7z l archive.7z

# 自解压包
7z a -sfx archive.exe src/
```

---

## Windows 内置命令

**基本用法:PowerShell 压缩解压**
`Compress-Archive`

```powershell
# 压缩目录
Compress-Archive -Path src\* -DestinationPath app.zip

# 解压
Expand-Archive -Path app.zip -DestinationPath .\out
```

---

## 校验与分割

**基本用法:生成与校验哈希**
`sha256sum <文件>`

```bash
# 生成校验值
sha256sum image.iso > image.sha256

# 校验完整性
sha256sum -c image.sha256
```

---

**基本用法:大文件分割**
`split [选项] <文件>`

```bash
# 每 100MB 分割一个文件
split -b 100M big.tar.gz part_

# 合并
cat part_* > big.tar.gz
```

<!-- ============ 文档分隔线：042-shell/013-CronScheduling.md ============ -->

# 定时任务与调度

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- crontab 五字段与常用写法
- 环境差异与日志重定向
- at 一次性任务
- systemd timer 对比 cron
- 防重叠运行（flock）

<!-- ============ 文档分隔线：042-shell/014-SshRemoteOperations.md ============ -->

# SSH 与远程操作

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 密钥对与免密登录
- ssh config 多主机管理
- scp 与 rsync 同步
- 本地/远程/动态端口转发
- 远程批量执行
