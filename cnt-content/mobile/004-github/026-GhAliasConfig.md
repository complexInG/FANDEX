# gh alias 与 config 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 别名管理

**基本用法:设置命令别名**
`gh alias set <别名> <展开>`

```bash
# 为 pr checkout 设置别名
gh alias set co "pr checkout"

# 设置 shell 别名(支持管道与变量)
gh alias set recent "run list --limit 5" --shell

# 列出全部别名
gh alias list

# 删除别名
gh alias delete co

# 从 YAML 文件导入别名
gh alias import aliases.yml --clobber
```

---

## 配置项

**基本用法:读取配置**
`gh config get <键>`

```bash
# 查看默认编辑器
gh config get editor

# 查看 git 协议
gh config get git_protocol

# 列出所有配置
gh config list
```

---

**基本用法:修改配置**
`gh config set <键> <值>`

```bash
# 设置编辑器
gh config set editor "code --wait"

# 设置 SSH 协议
gh config set git_protocol ssh

# 设置分页器关闭
gh config set pager ""

# 设置为指定主机
gh config set editor vim --host github.com
```

---

## 补全与状态

**基本用法:Shell 自动补全**
`gh completion -s <shell>`

```bash
# 生成 bash 补全脚本
gh completion -s bash > ~/.gh-completion.bash

# PowerShell 补全
gh completion -s powershell | Out-String | Invoke-Expression

# zsh 补全
gh completion -s zsh > "${fpath[1]}/_gh"
```

---

**基本用法:查看账户状态**
`gh status`

```bash
# 查看当前账户在所有仓库的工作概览
gh status
```

---