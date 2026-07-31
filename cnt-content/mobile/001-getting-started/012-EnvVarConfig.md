# 编程入门 环境变量配置

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Windows 系统变量查看

**基本写法：查看所有环境变量（CMD）**
`set`
```bash
# 列出所有环境变量
set
```

---

**基本写法：查看特定变量（CMD）**
`echo %<变量名>%`
```bash
# 查看指定环境变量的值
echo %PATH%
```

---

**基本写法：查看所有变量（PowerShell）**
`Get-ChildItem Env:`
```bash
# PowerShell 列出所有环境变量
Get-ChildItem Env:
```

---

**基本写法：查看特定变量（PowerShell）**
`$env:<变量名>`
```bash
# PowerShell 查看指定变量
$env:PATH
```

---

## Windows 环境变量设置

**基本写法：临时设置变量（CMD）**
`set <变量名>=<值>`
```bash
# 仅当前会话有效的变量
set MY_VAR=hello
```

---

**基本写法：永久设置用户变量（CMD）**
`setx <变量名> "<值>"`
```bash
# 永久写入用户环境变量
setx JAVA_HOME "C:\Program Files\Java\jdk-21"
```

---

**基本写法：永久设置系统变量（CMD）**
`setx <变量名> "<值>" /M`
```bash
# 写入系统级环境变量（需管理员权限）
setx PATH "%PATH%;C:\new\path" /M
```

---

**基本写法：PowerShell 设置用户变量**
`[Environment]::SetEnvironmentVariable("<变量名>", "<值>", "User")`
```bash
# PowerShell 永久设置用户变量
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Java\jdk-21", "User")
```

---

**基本写法：PowerShell 设置系统变量**
`[Environment]::SetEnvironmentVariable("<变量名>", "<值>", "Machine")`
```bash
# PowerShell 设置系统级变量（需管理员权限）
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\new", "Machine")
```

---

## Windows PATH 管理

**基本写法：追加路径到 PATH**
`setx PATH "%PATH%;<新路径>"`
```bash
# 将新路径追加到 PATH 环境变量
setx PATH "%PATH%;C:\my\tools"
```

---

**基本写法：PowerShell 追加 PATH**
`$env:PATH = $env:PATH + ";<新路径>"`
```bash
# 临时追加路径到当前会话 PATH
$env:PATH = $env:PATH + ";C:\my\tools"
```

---

**基本写法：PowerShell 永久追加用户 PATH**
`$old = [Environment]::GetEnvironmentVariable("PATH", "User"); [Environment]::SetEnvironmentVariable("PATH", $old + ";<新路径>", "User")`
```bash
# 永久追加路径到用户 PATH
$old = [Environment]::GetEnvironmentVariable("PATH", "User")
[Environment]::SetEnvironmentVariable("PATH", $old + ";C:\my\tools", "User")
```

---

## Linux/macOS 环境变量

**基本写法：临时设置变量**
`export <变量名>=<值>`
```bash
# 仅当前 shell 会话有效
export MY_VAR=hello
```

---

**基本写法：写入 bash 配置文件**
`echo 'export <变量名>=<值>' >> ~/.bashrc`
```bash
# 追加到 bashrc 实现永久生效
echo 'export JAVA_HOME=/usr/lib/jvm/java-21' >> ~/.bashrc
```

---

**基本写法：写入 zsh 配置文件**
`echo 'export <变量名>=<值>' >> ~/.zshrc`
```bash
# 追加到 zshrc（macOS 默认 shell）
echo 'export JAVA_HOME=/usr/lib/jvm/java-21' >> ~/.zshrc
```

---

**基本写法：追加路径到 PATH**
`export PATH=$PATH:<新路径>`
```bash
# 将新路径追加到 PATH 变量
export PATH=$PATH:/usr/local/bin
```

---

**基本写法：前置路径到 PATH**
`export PATH=<新路径>:$PATH`
```bash
# 将新路径前置到 PATH（优先级更高）
export PATH=/usr/local/bin:$PATH
```

---

## 配置文件重新加载

**基本写法：重新加载 bashrc**
`source ~/.bashrc`
```bash
# 重新加载 bash 配置文件
source ~/.bashrc
```

---

**基本写法：重新加载 zshrc**
`source ~/.zshrc`
```bash
# 重新加载 zsh 配置文件
source ~/.zshrc
```

---

**基本写法：重新加载 profile**
`source ~/.profile`
```bash
# 重新加载 profile 文件
source ~/.profile
```

---

## 变量删除

**基本写法：删除用户变量（PowerShell）**
`[Environment]::SetEnvironmentVariable("<变量名>", $null, "User")`
```bash
# 删除用户级环境变量
[Environment]::SetEnvironmentVariable("MY_VAR", $null, "User")
```

---

**基本写法：删除 setx 设置的变量**
`reg delete "HKCU\Environment" /F /V <变量名>`
```bash
# 通过注册表删除用户环境变量
reg delete "HKCU\Environment" /F /V MY_VAR
```

---

**基本写法：删除 bash 中的变量**
`unset <变量名>`
```bash
# 删除当前 shell 中的环境变量
unset MY_VAR
```
