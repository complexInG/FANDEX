# 编程入门 开发环境概览

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 工具链组成

**基本写法：查看 Node.js 版本**
`node --version`
```bash
# 验证 Node.js 是否安装成功
node --version
```

---

**基本写法：查看 Python 版本**
`python --version`
```bash
# 验证 Python 是否安装成功
python --version
```

---

**基本写法：查看 Java 版本**
`java -version`
```bash
# 验证 JDK 是否安装成功
java -version
```

---

**基本写法：查看 Git 版本**
`git --version`
```bash
# 验证 Git 是否安装成功
git --version
```

---

**基本写法：查看 Docker 版本**
`docker --version`
```bash
# 验证 Docker 是否安装成功
docker --version
```

---

**基本写法：查看 VS Code 版本**
`code --version`
```bash
# 验证 VS Code 命令行工具是否可用
code --version
```

---

## 包管理器识别

**基本写法：查看 npm 版本**
`npm --version`
```bash
# Node.js 默认包管理器
npm --version
```

---

**基本写法：查看 pnpm 版本**
`pnpm --version`
```bash
# 高性能 Node.js 包管理器
pnpm --version
```

---

**基本写法：查看 pip 版本**
`pip --version`
```bash
# Python 默认包管理器
pip --version
```

---

**基本写法：查看 uv 版本**
`uv --version`
```bash
# 新一代 Rust 实现的 Python 包管理器
uv --version
```

---

## 系统信息查询

**基本写法：查看操作系统信息（Windows）**
`systeminfo | findstr /B /C:"OS"`
```bash
# 查看 Windows 系统版本
systeminfo | findstr /B /C:"OS"
```

---

**基本写法：查看系统架构（Windows）**
`echo %PROCESSOR_ARCHITECTURE%`
```bash
# 查看处理器架构（x64 或 ARM64）
echo %PROCESSOR_ARCHITECTURE%
```

---

**基本写法：查看系统架构（跨平台）**
`uname -m`
```bash
# Linux/macOS 查看处理器架构
uname -m
```

---

## 环境变量检查

**基本写法：查看 PATH 环境变量（Windows）**
`echo %PATH%`
```bash
# 查看当前 PATH 环境变量
echo %PATH%
```

---

**基本写法：查看 PATH 环境变量（PowerShell）**
`$env:PATH`
```bash
# PowerShell 方式查看 PATH
$env:PATH
```

---

**基本写法：查看 JAVA_HOME**
`echo %JAVA_HOME%`
```bash
# 查看 Java 主目录环境变量
echo %JAVA_HOME%
```

---

**基本写法：查看所有环境变量（Windows）**
`set`
```bash
# 列出所有环境变量
set
```

---

**基本写法：查看所有环境变量（PowerShell）**
`Get-ChildItem Env:`
```bash
# PowerShell 列出所有环境变量
Get-ChildItem Env:
```
