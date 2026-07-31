# 包管理命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## Debian/Ubuntu (apt)

**基本用法:更新与安装**
`apt [选项] <子命令> <包名>`

```bash
# 更新包索引
sudo apt update

# 安装软件包
sudo apt install -y curl git

# 升级所有已安装包
sudo apt upgrade

# 卸载包(保留配置)
sudo apt remove nginx

# 卸载并删除配置
sudo apt purge nginx

# 搜索包
apt search redis

# 查看包信息
apt show nginx
```

---

## CentOS/RHEL (yum/dnf)

**基本用法:安装管理**
`yum [选项] <子命令> <包名>`

```bash
# 安装软件包
sudo yum install -y vim

# 更新所有包
sudo yum update

# 卸载软件包
sudo yum remove vim

# 列出已安装
yum list installed

# dnf 为 yum 的新版本(Fedora/RHEL8+)
sudo dnf install -y htop
```

---

## macOS (Homebrew)

**基本用法:brew 安装**
`brew <子命令> <包名>`

```bash
# 安装软件
brew install node

# 更新 Homebrew 本身
brew update

# 升级所有包
brew upgrade

# 升级指定包
brew upgrade node

# 卸载软件
brew uninstall node

# 查看已安装
brew list

# 清理旧版本缓存
brew cleanup
```

---

## Windows (winget)

**基本用法:winget 安装**
`winget <子命令> <包标识>`

```powershell
# 安装软件
winget install Git.Git

# 搜索软件
winget search vscode

# 升级所有
winget upgrade --all

# 升级指定软件
winget upgrade Microsoft.VisualStudioCode

# 卸载软件
winget uninstall Microsoft.VisualStudioCode

# 列出已安装
winget list
```

---

## Windows (Chocolatey)

**基本用法:choco 安装**
`choco <子命令> <包名>`

```powershell
# 安装软件(管理员 PowerShell)
choco install python -y

# 升级所有
choco upgrade all -y

# 卸载软件
choco uninstall python -y

# 搜索包
choco search nodejs
```

---

## Arch Linux (pacman)

**基本用法:pacman 安装**
`pacman [选项] <包名>`

```bash
# 同步并安装
sudo pacman -S nginx

# 升级所有包
sudo pacman -Syu

# 卸载包
sudo pacman -R nginx

# 搜索包
pacman -Ss redis
```

---

## 通用服务管理

**基本用法:安装后启动服务**
`systemctl <子命令> <服务名>`

```bash
# 启动并设置开机自启
sudo systemctl enable --now nginx

# 查看状态
sudo systemctl status nginx

# 重启服务
sudo systemctl restart nginx
```

---