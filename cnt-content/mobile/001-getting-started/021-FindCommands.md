# 查找命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## find 按条件查找

**基本用法:按名称查找**
`find <路径> -name "<模式>"`

```bash
# 按名称查找文件
find . -name "*.js"

# 不区分大小写
find /var/log -iname "*.LOG"

# 限制最大深度
find . -maxdepth 3 -name "*.md"
```

---

**基本用法:按类型查找**
`find <路径> -type <类型>`

```bash
# f 普通文件,d 目录,l 软链接
find . -type d -name "node_modules"

# 查找所有符号链接
find /usr -type l
```

---

**基本用法:按大小与时间**
`find <路径> -size <+/-大小>`

```bash
# 查找大于 100MB 的文件
find . -size +100M

# 查找 7 天内修改过的文件
find . -mtime -7

# 查找 30 分钟前访问过的文件
find . -amin +30
```

---

**基本用法:组合条件与动作**
`find <路径> <条件> -exec <命令> {} \;`

```bash
# 与条件:名为 .log 且大于 10MB
find . -name "*.log" -a -size +10M

# 或条件
find . -name "*.jpg" -o -name "*.png"

# 对结果执行命令
find . -name "*.tmp" -exec rm -f {} +

# 用户确认后执行
find . -name "*.bak" -ok rm {} \;
```

---

## locate 快速定位

**基本用法:从数据库查找**
`locate <模式>`

```bash
# 秒级定位文件路径
locate nginx.conf

# 正则匹配
locate -r "\.sh$"

# 更新文件数据库
sudo updatedb
```

---

## which/whereis 命令定位

**基本用法:查找可执行文件路径**
`which <命令>`

```bash
# 查看命令所在路径
which python3
```

---

**基本用法:查找二进制/源码/手册**
`whereis <命令>`

```bash
# 同时显示二进制、源码、man 路径
whereis nginx
```

---

**基本用法:查看命令类型**
`type <命令>`

```bash
# 区分内置命令、别名、外部命令
type cd
type ll
```

---

## grep -r 递归搜索内容

**基本用法:递归搜索目录内容**
`grep -r "<模式>" <路径>`

```bash
# 递归搜索目录下所有文件
grep -rn "TODO" src/

# 仅搜索指定扩展名
grep -rn --include="*.py" "def main" .

# 排除目录
grep -rn --exclude-dir=node_modules "console.log" .
```

---

## ack/rg 高级搜索

**基本用法:ripgrep 代码搜索**
`rg <模式> <路径>`

```bash
# 自动忽略 .gitignore 文件
rg "useState" src/

# 仅搜索特定类型文件
rg -t py "import" .

# 显示上下文 3 行
rg -C 3 "error" -i
```

---

## Windows 查找命令

**基本用法:PowerShell 递归查找**
`Get-ChildItem -Recurse -Filter <模式> <路径>`

```powershell
# 递归查找文件
Get-ChildItem -Path . -Filter *.js -Recurse

# 按内容搜索
Select-String -Path *.ps1 -Pattern "function" -Recurse
```

---