## pip 包安装

**基本写法：安装包**
`pip install <包名>`
```bash
# 安装指定的 Python 包
pip install requests
```

---

**基本写法：安装指定版本**
`pip install <包名>==<版本号>`
```bash
# 安装指定版本的包
pip install django==5.0.6
```

---

**基本写法：批量安装依赖**
`pip install -r <需求文件>`
```bash
# 从 requirements.txt 安装所有依赖
pip install -r requirements.txt
```

---

**基本写法：从 git 仓库安装**
`pip install git+<仓库地址>`
```bash
# 直接从 GitHub 仓库安装包
pip install git+https://github.com/user/repo.git
```

---

## pip 包管理

**基本写法：卸载包**
`pip uninstall <包名>`
```bash
# 移除已安装的包
pip uninstall requests
```

---

**基本写法：查看已安装包**
`pip list`
```bash
# 列出所有已安装的包
pip list
```

---

**基本写法：查看包详情**
`pip show <包名>`
```bash
# 查看指定包的详细信息
pip show django
```

---

**基本写法：导出依赖列表**
`pip freeze > requirements.txt`
```bash
# 导出当前环境所有依赖到文件
pip freeze > requirements.txt
```

---

**基本写法：升级包**
`pip install --upgrade <包名>`
```bash
# 升级包到最新版本
pip install --upgrade requests
```

---

## 镜像源配置

**基本写法：使用清华镜像源安装**
`pip install <包名> -i <镜像地址>`
```bash
# 使用清华大学镜像源加速下载
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

**基本写法：永久设置镜像源**
`pip config set global.index-url <镜像地址>`
```bash
# 永久切换为清华镜像源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

---

**基本写法：查看当前配置**
`pip config list`
```bash
# 查看 pip 的所有配置项
pip config list
```

---

## venv 虚拟环境

**基本写法：创建虚拟环境**
`python -m venv <环境名>`
```bash
# 在当前目录创建虚拟环境
python -m venv .venv
```

---

**基本写法：激活虚拟环境（Windows）**
`<环境名>\Scripts\activate`
```bash
# Windows 下激活虚拟环境
.venv\Scripts\activate
```

---

**基本写法：激活虚拟环境（Linux/macOS）**
`source <环境名>/bin/activate`
```bash
# Linux/macOS 下激活虚拟环境
source .venv/bin/activate
```

---

**基本写法：退出虚拟环境**
`deactivate`
```bash
# 退出当前虚拟环境
deactivate
```

---

**基本写法：指定 Python 版本创建环境**
`py -<版本号> -m venv <环境名>`
```bash
# 使用 Python 3.11 创建虚拟环境
py -3.11 -m venv .venv311
```

---

## pipx 全局工具安装

**基本写法：安装 pipx**
`pip install pipx`
```bash
# 安装 pipx 用于管理全局命令行工具
pip install pipx
```

---

**基本写法：安装命令行工具**
`pipx install <包名>`
```bash
# 在隔离环境中安装 CLI 工具
pipx install black
```

---

**基本写法：运行临时工具**
`pipx run <包名> <参数>`
```bash
# 临时运行而不安装
pipx run cowsay "hello"
```
