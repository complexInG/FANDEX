---
order: 300
title: 编程入门 Java JDK 配置
module: 'getting-started'
category: 工具链
difficulty: beginner
description: 编程入门 Java JDK 配置 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

## Windows 安装

**基本写法：winget 安装 Microsoft OpenJDK**
`winget install Microsoft.OpenJDK.21`
```bash
# 安装 Microsoft Build of OpenJDK 21
winget install Microsoft.OpenJDK.21
```

---

**基本写法：winget 安装 Eclipse Temurin**
`winget install EclipseAdoptium.Temurin.21.JDK`
```bash
# 安装 Eclipse Temurin 21 版本
winget install EclipseAdoptium.Temurin.21.JDK
```

---

**基本写法：winget 安装指定 JDK 版本**
`winget install Microsoft.OpenJDK.17`
```bash
# 安装 JDK 17 LTS 版本
winget install Microsoft.OpenJDK.17
```

---

## macOS 安装

**基本写法：Homebrew 安装 Temurin**
`brew install --cask temurin@21`
```bash
# 通过 Homebrew 安装 Temurin 21
brew install --cask temurin@21
```

---

**基本写法：Homebrew 安装最新 JDK**
`brew install --cask temurin`
```bash
# 安装最新版本的 Temurin
brew install --cask temurin
```

---

## Linux 安装

**基本写法：apt 安装 OpenJDK（Ubuntu/Debian）**
`sudo apt-get install openjdk-21-jdk`
```bash
# 安装 OpenJDK 21
sudo apt-get install openjdk-21-jdk
```

---

**基本写法：yum 安装 OpenJDK（CentOS/RHEL）**
`sudo yum install java-21-openjdk-devel`
```bash
# 安装 OpenJDK 21 开发包
sudo yum install java-21-openjdk-devel
```

---

## 环境变量配置（Windows）

**基本写法：设置 JAVA_HOME（CMD）**
`setx JAVA_HOME "<JDK路径>"`
```bash
# 永久设置 JAVA_HOME 环境变量
setx JAVA_HOME "C:\Program Files\Microsoft\jdk-21"
```

---

**基本写法：设置 JAVA_HOME（PowerShell）**
`[Environment]::SetEnvironmentVariable("JAVA_HOME", "<JDK路径>", "User")`
```bash
# PowerShell 用户级环境变量设置
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Microsoft\jdk-21", "User")
```

---

**基本写法：将 JAVA_HOME\bin 加入 PATH**
`setx PATH "%PATH%;%JAVA_HOME%\bin"`
```bash
# 将 JDK 的 bin 目录追加到 PATH
setx PATH "%PATH%;%JAVA_HOME%\bin"
```

---

**基本写法：PowerShell 追加 PATH**
`[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";%JAVA_HOME%\bin", "User")`
```bash
# PowerShell 方式追加 PATH 环境变量
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";$env:JAVA_HOME\bin", "User")
```

---

## 环境变量配置（Linux/macOS）

**基本写法：bash 配置 JAVA_HOME**
`export JAVA_HOME=<JDK路径>`
```bash
# 写入 ~/.bashrc 或 ~/.bash_profile
export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
```

---

**基本写法：bash 追加 PATH**
`export PATH=$JAVA_HOME/bin:$PATH`
```bash
# 将 JDK bin 目录加入 PATH
export PATH=$JAVA_HOME/bin:$PATH
```

---

**基本写法：macOS 使用 java_home 工具**
`/usr/libexec/java_home -v <版本号>`
```bash
# 获取指定版本的 JDK 路径
/usr/libexec/java_home -v 21
```

---

## 安装验证

**基本写法：验证 Java 运行时**
`java -version`
```bash
# 应输出 openjdk version "21" 类似信息
java -version
```

---

**基本写法：验证 Java 编译器**
`javac -version`
```bash
# 验证 JDK 编译器是否可用
javac -version
```

---

**基本写法：验证 JAVA_HOME**
`echo %JAVA_HOME%`
```bash
# 查看已设置的 JAVA_HOME 路径
echo %JAVA_HOME%
```

---

**基本写法：运行测试程序**
`java -e "System.out.println(\"Java 运行正常\")"`
```bash
# 直接执行 Java 单行代码（JDK 22+）
java -e "System.out.println(\"Java 运行正常\")"
```

## 延伸阅读
从入门到进阶路径：001 入门 -> 002 Markdown -> 003 Git -> 006 HTML -> 007 CSS -> 008 JS。
语言进阶：013 Java / 040 Python / 016 Go 按兴趣选择。
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
