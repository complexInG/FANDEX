---
order: 360
title: 进程管理命令速查手册
module: getting-started

category: '001-getting-started'
difficulty: beginner
description: 进程管理命令速查手册 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---
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

---

## 参考文献

本模块各文档：环境搭建、编程基础、调试思维等。
MDN 学习区：https://developer.mozilla.org/zh-CN/docs/Learn_web_development
freeCodeCamp：https://www.freecodecamp.org/chinese/
黑马程序员官网：https://www.itheima.com/

## 延伸阅读

从入门到进阶路径：001 入门 -> 002 Markdown -> 003 Git -> 006 HTML -> 007 CSS -> 008 JS。
语言进阶：013 Java / 040 Python / 016 Go 按兴趣选择。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供基础课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 如何高效自学编程

目标驱动：每个阶段一个小项目（计算器、笔记、网站）。
费曼技巧：把学到的知识写出来或讲出来。
刻意练习：专注薄弱点，带反馈循环。
社区参与：提问、回答、代码评审加速成长。

### 13.2 学习路径规划

阶段一（2-4 周）：环境 + 基础语法 + 小练习。
阶段二（4-8 周）：数据结构 + 简单项目。
阶段三（2-3 月）：框架 + 实战项目 + 部署。
持续：算法刷题、源码阅读、开源贡献。
