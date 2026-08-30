---
order: 240
title: Java JDK 安装与配置
module: 'getting-started'
category: 工具链
difficulty: beginner
description: JDK 在主流系统下的安装与 JAVA_HOME、PATH 环境变量配置。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'getting-started/014-WindowsEnvConfigTutorial'
  - 'getting-started/015-MacOSEnvConfigTutorial'
  - 'getting-started/016-LinuxEnvConfigTutorial'
prerequisites:
  - 'getting-started/004-DevEnvSetup'
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
