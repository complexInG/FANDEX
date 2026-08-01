# Git 配置管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 配置级别

**基本写法：设置仓库级配置（仅当前仓库）**
`git config <键> <值>`
```bash
# 设置当前仓库的用户名
git config user.name "Alice"
```

---

**基本写法：设置全局级配置（当前用户所有仓库）**
`git config --global <键> <值>`
```bash
# 设置全局用户邮箱
git config --global user.email "alice@example.com"
```

---

**基本写法：设置系统级配置（本机所有用户）**
`git config --system <键> <值>`
```bash
# 设置系统级默认分支名（需管理员权限）
git config --system init.defaultBranch main
```

---

**基本写法：查看某级别配置来源**
`git config --show-origin <键>`
```bash
# 显示配置项来自哪个文件
git config --show-origin user.name
```

---

## 查看配置

**基本写法：查看所有配置（合并后最终值）**
`git config --list`
```bash
# 列出所有生效配置
git config --list
```

---

**基本写法：查看指定级别配置**
`git config --list --<级别>`
```bash
# 仅查看全局级配置
git config --list --global
```

---

**基本写法：查看单个配置项**
`git config <键>`
```bash
# 查看当前用户名
git config user.name
```

---

**基本写法：查看配置类型**
`git config --type <类型> <键>`
```bash
# 以布尔类型读取配置
git config --type bool core.autocrlf
```

---

## 编辑配置文件

**基本写法：直接打开配置文件编辑**
`git config --<级别> --edit`
```bash
# 用默认编辑器打开全局配置
git config --global --edit
```

---

## 用户身份

**基本写法：配置提交身份**
`git config --global user.name "<姓名>"`
```bash
# 设置全局提交姓名
git config --global user.name "Alice Lee"
```

---

**基本写法：配置提交邮箱**
`git config --global user.email "<邮箱>"`
```bash
# 设置全局提交邮箱
git config --global user.email "alice@example.com"
```

---

**基本写法：按仓库单独配置身份**
`git config user.name "<姓名>"`
```bash
# 仅当前仓库使用工作账号
git config user.name "Alice Corp"
```

---

## 默认分支与初始化

**基本写法：设置 init 默认分支**
`git config --global init.defaultBranch <分支名>`
```bash
# 新仓库默认使用 main 分支
git config --global init.defaultBranch main
```

---

## 行尾处理

**基本写法：Windows 自动转 CRLF**
`git config --global core.autocrlf true`
```bash
# 检出转 CRLF，提交转 LF
git config --global core.autocrlf true
```

---

**基本写法：Linux/Mac 保留 LF**
`git config --global core.autocrlf input`
```bash
# 检出保留 LF，提交转 LF
git config --global core.autocrlf input
```

---

## 编辑器与工具

**基本写法：设置默认编辑器**
`git config --global core.editor "<命令>"`
```bash
# 使用 VS Code 作为默认编辑器
git config --global core.editor "code --wait"
```

---

**基本写法：设置默认合并工具**
`git config --global merge.tool <工具>`
```bash
# 配置 VS Code 为合并工具
git config --global merge.tool vscode
```

---

**基本写法：配置合并工具路径**
`git config --global mergetool.<工具>.cmd "<命令>"`
```bash
# 配置 vscode 合并工具调用命令
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

---

## 别名（alias）

**基本写法：设置命令别名**
`git config --global alias.<别名> "<命令>"`
```bash
# 用 co 代替 checkout
git config --global alias.co checkout
```

---

**基本写法：设置带参数别名**
`git config --global alias.<别名> "!<脚本>"`
```bash
# 用 ! 前缀执行外部命令
git config --global alias.lg "log --oneline --graph --all"
```

---

**基本写法：删除别名**
`git config --global --unset alias.<别名>`
```bash
# 移除 co 别名
git config --global --unset alias.co
```

---

## 拉取与推送行为

**基本写法：拉取时默认使用 rebase**
`git config --global pull.rebase true`
```bash
# pull 默认变基而非合并
git config --global pull.rebase true
```

---

**基本写法：拉取仅快进**
`git config --global pull.ff only`
```bash
# 仅允许快进拉取，否则失败
git config --global pull.ff only
```

---

**基本写法：推送默认模式**
`git config --global push.default <模式>`
```bash
# 只推送当前分支到同名上游
git config --global push.default simple
```

---

## 颜色与输出

**基本写法：开启颜色输出**
`git config --global color.ui auto`
```bash
# 终端自动启用颜色
git config --global color.ui auto
```

---

## 凭据缓存

**基本写法：开启凭据助手**
`git config --global credential.helper <助手>`
```bash
# 使用系统凭据管理器
git config --global credential.helper manager
```

---

**基本写法：临时内存缓存**
`git config --global credential.helper 'cache --timeout=<秒>'`
```bash
# 凭据缓存 1 小时
git config --global credential.helper 'cache --timeout=3600'
```

---

## 增删改配置项

**基本写法：新增或修改配置项**
`git config --<级别> <键> <值>`
```bash
# 修改全局 init 默认分支
git config --global init.defaultBranch main
```

---

**基本写法：删除配置项**
`git config --<级别> --unset <键>`
```bash
# 删除全局用户名配置
git config --global --unset user.name
```

---

**基本写法：删除多处同键配置**
`git config --<级别> --unset-all <键>`
```bash
# 删除所有同名配置项
git config --local --unset-all remote.origin.fetch
```

---

**基本写法：追加多值配置**
`git config --<级别> --add <键> <值>`
```bash
# 追加一条 fetch 规则
git config --local --add remote.origin.fetch '+refs/tags/*:refs/tags/*'
```

---

## 引用存储格式（Reftable）

**基本写法：查看引用存储格式**
`git config core.refStorage`
```bash
# 查看当前引用存储后端
git config core.refStorage
```

---

**基本写法：迁移到 reftable 后端**
`git refs migrate --ref-storage=reftable`
```bash
# 切换到 reftable 引用存储（适用于多分支大仓）
git refs migrate --ref-storage=reftable
```

---

## 文件路径与位置

**基本写法：查看各级别配置文件路径**
`git config --list --show-origin`
```bash
# 显示每条配置来源文件
git config --list --show-origin
```

---

**基本写法：仓库级配置文件位置**
`.git/config`
```bash
# 编辑当前仓库配置文件
git config --local --edit
```

---

**基本写法：全局配置文件位置**
`~/.gitconfig`
```bash
# 编辑用户级配置文件
git config --global --edit
```

---

**基本写法：系统级配置文件位置**
`/etc/gitconfig`
```bash
# 编辑系统级配置文件（需管理员权限）
git config --system --edit
```
