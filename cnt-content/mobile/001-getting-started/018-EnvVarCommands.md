# 环境变量命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看环境变量

**基本用法:查看所有环境变量**
`env`

```bash
# 列出当前所有环境变量
env
```

---

**基本用法:查看指定变量**
`printenv <变量名>`

```bash
# 查看 PATH 变量
printenv PATH

# 查看 HOME 变量
printenv HOME
```

---

**基本用法:查看单个变量值**
`echo $<变量名>`

```bash
# 输出变量值
echo $JAVA_HOME
```

---

## 设置环境变量

**基本用法:导出为环境变量**
`export <变量名>=<值>`

```bash
# 设置当前会话的环境变量
export NODE_ENV=production

# 追加到 PATH
export PATH=$PATH:/opt/bin

# 一次性导出多个
export DB_HOST=localhost DB_PORT=5432
```

---

**基本用法:设置只读变量**
`readonly <变量名>`

```bash
# 设置不可修改的变量
readonly VERSION=2.0
```

---

## Shell 变量管理

**基本用法:查看与设置 Shell 变量**
`set`

```bash
# 显示所有变量含 Shell 变量
set

# 开启 shell 选项
set -e
```

---

**基本用法:取消变量**
`unset <变量名>`

```bash
# 删除已定义变量
unset TEMP_VAR
```

---

## 持久化配置

**基本用法:写入配置文件**
`echo '<内容>' >> <文件>`

```bash
# 追加到当前用户配置
echo 'export GOPATH=$HOME/go' >> ~/.bashrc

# 追加到登录 shell 配置
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.profile
```

---

**基本用法:重新加载配置**
`source <文件>`

```bash
# 立即生效配置文件
source ~/.bashrc

# 简写形式
. ~/.bash_profile
```

---

## Windows 环境变量命令

**基本用法:PowerShell 设置环境变量**
`$env:<变量名>="<值>"`

```powershell
# 临时设置
$env:NODE_ENV="production"

# 查看变量
$env:PATH

# 永久设置用户级变量
[Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Java\jdk21", "User")
```

---

**基本用法:setx 命令(Windows)**
`setx <变量名> <值>`

```bash
# 永久写入用户环境变量(重启生效)
setx PYTHON_PATH "C:\Python312"
```

---

## 常用变量速查

**基本用法:常用内置变量**
`echo $<变量>`

```bash
# 当前用户
echo $USER

# 主目录
echo $HOME

# 当前 Shell
echo $SHELL

# 退出码
echo $?

# 当前进程号
echo $$
```

---