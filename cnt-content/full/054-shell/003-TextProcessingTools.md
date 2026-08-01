---
order: 3
title: 文本处理三剑客：grep、sed、awk
module: shell
category: Shell
difficulty: intermediate
description: '文本处理三剑客：grep 行匹配、sed 流编辑、awk 列处理与统计、管道组合实战'
author: fanquanpp
updated: '2026-08-01'
related:
  - shell/008-PracticalScripts
  - shell/004-ProcessJobControl
prerequisites:
  - shell/002-CommandLineBasics
---
## 1. 三剑客分工

grep、sed、awk 是 Linux 文本处理的"三剑客"，处理模型各不相同：

| 工具 | 处理模型 | 擅长场景 |
| --- | --- | --- |
| grep | 行筛选 | 找出匹配的行（过滤） |
| sed | 流编辑器 | 按行做替换、删除、插入（改写） |
| awk | 行 + 列 | 取列、条件统计、生成报表（计算） |

三者都遵循"读一行、处理一行、输出一行"的流式模型，因此可以无缝接入管道：`cat file | grep ... | awk ... | sort ...`。

## 2. grep：行匹配

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

讲解：`-o` 在提取 IP、端口等片段时很常用；`-l` 常用于定位"哪些文件有问题"。grep 的退出码 0/1/2 分别表示"有匹配/无匹配/出错"，可在脚本中做条件判断。

### 2.2 正则表达式

```bash
grep -E "err|warn" app.log      # -E 启用扩展正则，匹配 error 或 warn
grep -E "^[0-9]{4}-" app.log    # 以 4 位数字加 - 开头（如日期）
grep -E "(GET|POST) /api" log   # 分组匹配
grep "error\." app.log          # 基本正则：\. 匹配字面点号
```

讲解：常用正则元字符：`^` 行首、`$` 行尾、`.` 任意字符、`*` 前项重复 0 次以上、`+` 重复 1 次以上（需 -E）、`[]` 字符集、`|` 或。默认的基本正则与 `-E` 扩展正则在元字符转义规则上不同，习惯上统一加 `-E` 更易读。

## 3. sed：流编辑

### 3.1 替换与删除

```bash
sed 's/old/new/' file           # 每行第一次出现的 old 替换为 new
sed 's/old/new/g' file          # 全局替换（g = global）
sed -i 's/old/new/g' file       # 直接写回原文件（-i = in-place）
sed -i.bak 's/old/new/g' file   # 写回前先备份为 file.bak
sed '/^#/d' file                # 删除注释行（d = delete）
sed '1,5d' file                 # 删除第 1 到第 5 行
```

讲解：`sed -i` 修改原文件，务必先用不加 `-i` 的命令预览结果。`/pattern/d` 按匹配删除是清理配置文件注释的常用姿势。

### 3.2 打印与插入

```bash
sed -n '10,20p' file            # 只打印第 10-20 行（-n 关闭默认输出）
sed -n '/ERROR/,/END/p' file    # 打印从 ERROR 到 END 之间的行
sed -i '3a\new_line' file       # 在第 3 行后插入一行（a = append）
sed -i '3i\new_line' file       # 在第 3 行前插入一行（i = insert）
```

讲解：sed 默认会把每一行都打印出来，`-n` 配合 `p` 才做到"只看想看的行"。

### 3.3 捕获分组

```bash
# 将 "name=alice" 改为 "name=ALICE"
echo "name=alice" | sed -E 's/(name=)(.*)/\1\U\2/'
# 提取日期：2026-08-01 -> 08/01
echo "2026-08-01" | sed -E 's/([0-9]{4})-([0-9]{2})-([0-9]{2})/\2\/\3\/\1/'
```

讲解：`(...)` 捕获分组，`\1`、`\2` 引用分组内容，`\U` 将后续内容转大写。分组替换是 sed 进阶的核心能力。

## 4. awk：列处理与统计

awk 按"字段"工作：默认以空白（空格/制表符）分隔每一行，`$1`、`$2` 为第 1、2 列，`$0` 为整行。

### 4.1 取列与条件

```bash
awk '{print $1}' access.log          # 打印第一列（通常是 IP）
awk '{print $1, $9}' access.log      # 打印第 1 和第 9 列
awk -F: '{print $1}' /etc/passwd     # -F 指定分隔符为冒号
awk '$9 == 404 {print $1, $7}' log   # 只处理状态码为 404 的行
awk '$3 > 100 {print $0}' data.txt   # 第三列大于 100 的行
```

讲解：`-F` 可以指定任意分隔符，处理 `/etc/passwd`（冒号分隔）、CSV（逗号分隔）时必不可少。`$9 == 404` 是"条件 + 动作"的典型结构。

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

讲解：`$NF` 在日志分析中提取 URL、文件路径等"最后一列"时非常实用。`END { }` 块在所有行处理完后执行一次，用于输出统计结果。

### 4.3 统计与格式化

```bash
# 按第一列（IP）分组计数，输出前 10 名
awk '{cnt[$1]++} END {for (ip in cnt) print cnt[ip], ip}' access.log \
    | sort -rn | head -10

# 求平均值并格式化输出
awk '{sum += $2; n++} END {printf "平均: %.2f\n", sum/n}' data.txt
```

讲解：awk 的关联数组 `cnt[ip]` 天然适合分组统计，`for (ip in cnt)` 遍历所有键。`printf` 与 C 语言语法一致，`%.2f` 保留两位小数，适合生成报表。

## 5. 管道组合实战

三剑客单独使用威力有限，串联起来才是生产级用法。以下以 Nginx 访问日志 `access.log`（格式：IP 日期 请求 状态码 大小 来源）为例：

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

讲解：`sort | uniq -c | sort -rn` 是"分组计数 + 排序"的标准三段式：先排序使相同行相邻，`uniq -c` 计数，再按数值倒序排。`$(...)` 命令替换让 grep 的匹配模式动态生成。

## 6. 综合练习：生成简洁日报

```bash
#!/bin/bash
LOG="access.log"
echo "===== 访问统计日报 ====="
echo "总请求数: $(wc -l < "$LOG")"
echo "独立 IP 数: $(awk '{print $1}' "$LOG" | sort -u | wc -l)"
echo "404 次数: $(grep -c ' 404 ' "$LOG")"
echo "流量 TOP 5 资源:"
awk '{size[$7] += $10} END {for (u in size) print size[u], u}' "$LOG" \
    | sort -rn | head -5
```

讲解：脚本把前面所有技巧整合成一个小报表工具，`size[$7] += $10` 按 URL 累加传输字节数，输出流量最大的 5 个资源。该模式可直接套用到任何"按维度聚合统计"的场景。

## 7. 参考资源

GNU grep 手册：https://www.gnu.org/software/grep/manual/

GNU sed 手册：https://www.gnu.org/software/sed/manual/

GNU awk 手册：https://www.gnu.org/software/gawk/manual/

正则表达式在线测试：https://regex101.com/
