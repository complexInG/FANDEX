# Python 虚拟环境与包管理

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## venv 标准库

**基本写法：创建虚拟环境**
`python -m venv <目录>`
```python
# 在当前目录创建 .venv 虚拟环境
# python -m venv .venv
```

---

**基本写法：激活虚拟环境（Windows）**
`.venv\Scripts\Activate.ps1`
```python
# PowerShell 激活脚本，激活后提示符前缀显示 (.venv)
# .venv\Scripts\Activate.ps1
```

---

**基本写法：激活虚拟环境（Linux/macOS）**
`source <目录>/bin/activate`
```python
# bash/zsh 下激活
# source .venv/bin/activate
```

---

**基本写法：退出虚拟环境**
`deactivate`
```python
# 在已激活环境中退出
# deactivate
```

---

**基本写法：指定不安装 pip**
`python -m venv <目录> --without-pip`
```python
# 创建不含 pip 的轻量环境
# python -m venv myenv --without-pip
```

---

**基本写法：升级环境内部组件**
`python -m venv <目录> --upgrade`
```python
# 升级已有环境的 Python 内部组件，保留已装包
# python -m venv myenv --upgrade
```

---

## pip 包管理

**基本写法：安装包**
`pip install <包名>`
```python
# 安装最新版本的 requests
# pip install requests
```

---

**基本写法：安装指定版本**
`pip install <包名>==<版本>`
```python
# 安装指定版本
# pip install requests==2.32.3
```

---

**基本写法：从需求文件安装**
`pip install -r <需求文件>`
```python
# 按 requirements.txt 批量安装
# pip install -r requirements.txt
```

---

**基本写法：卸载包**
`pip uninstall <包名>`
```python
# 卸载指定包
# pip uninstall requests
```

---

**基本写法：导出依赖列表**
`pip freeze > <文件>`
```python
# 将当前已安装包导出为 requirements
# pip freeze > requirements.txt
```

---

**基本写法：查看已安装包**
`pip list`
```python
# 列出所有已安装包及版本
# pip list
```

---

**基本写法：升级包**
`pip install --upgrade <包名>`
```python
# 升级到最新版本
# pip install --upgrade requests
```

---

**基本写法：查看包详情**
`pip show <包名>`
```python
# 显示包元信息与依赖
# pip show requests
```

---

## poetry 项目管理

**基本写法：初始化项目**
`poetry init`
```python
# 交互式生成 pyproject.toml
# poetry init
```

---

**基本写法：新建项目**
`poetry new <项目名>`
```python
# 创建标准目录结构
# poetry new mypkg
```

---

**基本写法：添加依赖**
`poetry add <包名>`
```python
# 安装并写入 pyproject.toml
# poetry add fastapi
```

---

**基本写法：添加开发依赖**
`poetry add <包名> --group dev`
```python
# 添加到 dev 依赖组
# poetry add pytest --group dev
```

---

**基本写法：安装全部依赖**
`poetry install`
```python
# 按 pyproject.toml 安装并锁定
# poetry install
```

---

**基本写法：指定解释器创建环境**
`poetry env use <python版本>`
```python
# 使用指定解释器创建虚拟环境
# poetry env use python3.12
```

---

**基本写法：运行命令**
`poetry run <命令>`
```python
# 在项目环境中执行
# poetry run python main.py
```

---

**基本写法：打包构建**
`poetry build`
```python
# 生成 sdist 与 wheel 包
# poetry build
```

---

**基本写法：发布到 PyPI**
`poetry publish`
```python
# 发布构建产物到 PyPI
# poetry publish
```

---

## uv 极速管理

**基本写法：创建虚拟环境**
`uv venv [目录]`
```python
# 默认在 .venv 创建环境
# uv venv
```

---

**基本写法：指定 Python 版本**
`uv venv --python <版本>`
```python
# 自动下载并使用指定版本
# uv venv --python 3.13
```

---

**基本写法：pip 兼容安装**
`uv pip install <包名>`
```python
# 兼容 pip 语法但更快
# uv pip install requests
```

---

**基本写法：按需求文件安装**
`uv pip install -r <需求文件>`
```python
# 批量安装依赖
# uv pip install -r requirements.txt
```

---

**基本写法：导出依赖**
`uv pip freeze > <文件>`
```python
# 导出当前环境依赖
# uv pip freeze > requirements.txt
```

---

**基本写法：添加项目依赖**
`uv add <包名>`
```python
# 写入 pyproject.toml 并安装
# uv add fastapi
```

---

**基本写法：移除依赖**
`uv remove <包名>`
```python
# 从项目中移除
# uv remove fastapi
```

---

**基本写法：同步依赖**
`uv sync`
```python
# 按锁文件精确重建环境
# uv sync
```

---

**基本写法：运行脚本**
`uv run <脚本>`
```python
# 自动加载环境运行
# uv run python main.py
```

---

**基本写法：临时依赖运行**
`uv run --with <包名> <命令>`
```python
# 隔离环境临时安装并执行
# uv run --with httpx python -c "import httpx"
```

---

**基本写法：初始化项目**
`uv init <项目名>`
```python
# 生成标准项目结构
# uv init myproject
```

---

**基本写法：安装指定 Python**
`uv python install <版本>`
```python
# 下载安装指定解释器
# uv python install 3.13
```

---

**基本写法：列出可用 Python**
`uv python list`
```python
# 查看本地及可下载版本
# uv python list
```

---