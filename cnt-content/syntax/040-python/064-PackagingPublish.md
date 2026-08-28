# Python 打包与发布

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## setuptools 项目配置

**基本写法：pyproject.toml 元数据**
`[project]`
```toml
# 项目基本元数据
[project]
name = "mypackage"
version = "0.1.0"
description = "示例包"
readme = "README.md"
requires-python = ">=3.12"
license = {text = "MIT"}
authors = [{name = "Alice", email = "alice@example.com"}]
```

**基本写法：依赖声明**
`dependencies = [...]`
```toml
# 运行时依赖
dependencies = [
    "requests>=2.31",
    "pydantic>=2.0",
]
```

**基本写法：可选依赖**
`[project.optional-dependencies]`
```toml
# 可选依赖分组
[project.optional-dependencies]
dev = ["pytest>=8.0", "ruff>=0.4"]
docs = ["sphinx>=7.0"]
```

**基本写法：构建系统**
`[build-system]`
```toml
# 声明构建后端
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

**基本写法：包发现配置**
`[tool.setuptools.packages.find]`
```toml
# 自动发现包
[tool.setuptools.packages.find]
where = ["src"]
```

---

## 版本号管理

**基本写法：静态版本**
`version = "<版本>"`
```toml
# 直接写版本号
version = "1.2.3"
```

**基本写法：动态版本**
`dynamic = ["version"]`
```toml
# 动态读取版本
[project]
dynamic = ["version"]
[tool.setuptools.dynamic]
version = {attr = "mypackage.__version__"}
```

---

## 构建包

**基本写法：安装 build**
`pip install build`
```python
# 安装构建工具
pip install build
```

**基本写法：构建 sdist 与 wheel**
`python -m build`
```python
# 构建源码分发包与 wheel
python -m build
```

**基本写法：仅构建 wheel**
`python -m build --wheel`
```python
# 仅构建 wheel 包
python -m build --wheel
```

**基本写法：仅构建 sdist**
`python -m build --sdist`
```python
# 仅构建源码分发
python -m build --sdist
```

---

## wheel 包结构

**基本写法：查看 wheel 内容**
`python -m zipfile -l <wheel>`
```python
# 查看 wheel 内文件
python -m zipfile -l mypackage-0.1.0-py3-none-any.whl
```

**基本写法：纯 Python wheel**
`py3-none-any.whl`
```python
# 命名约定：{包名}-{版本}-{python}-{abi}-{平台}.whl
# py3-none-any：纯 Python，所有平台
```

**基本写法：平台 wheel**
`cp312-cp312-win_amd64.whl`
```python
# CPython 3.12，Windows x64 平台特定 wheel
```

---

## 发布到 PyPI

**基本写法：安装 twine**
`pip install twine`
```python
# 安装发布工具
pip install twine
```

**基本写法：检查包**
`twine check dist/*`
```python
# 检查包元数据
twine check dist/*
```

**基本写法：上传到 TestPyPI**
`twine upload --repository testpypi dist/*`
```python
# 上传到测试仓库
twine upload --repository testpypi dist/*
```

**基本写法：上传到 PyPI**
`twine upload dist/*`
```python
# 上传到正式 PyPI
twine upload dist/*
```

**基本写法：配置 API Token**
`~/.pypirc`
```ini
# 配置 PyPI 凭据
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxx
```

---

## entry_points 入口点

**基本写法：命令行脚本**
`[project.scripts]`
```toml
# 注册命令行入口
[project.scripts]
mycli = "mypackage.cli:main"
```

**基本写法：GUI 入口**
`[project.gui-scripts]`
```toml
# GUI 应用入口
[project.gui-scripts]
mygui = "mypackage.gui:main"
```

---

## 包内资源

**基本写法：include-package-data**
`[tool.setuptools]`
```toml
# 包含所有版本控制文件
[tool.setuptools]
include-package-data = true
```

**基本写法：MANIFEST.in**
`include <文件模式>`
```
# 显式声明包含文件
include README.md LICENSE
recursive-include mypackage/data *.json *.txt
```

**基本写法：package-data**
`[tool.setuptools.package-data]`
```toml
# 指定包数据
[tool.setuptools.package-data]
mypackage = ["data/*.json"]
```

---

## 可编辑安装

**基本写法：开发模式安装**
`pip install -e <项目>`
```python
# 可编辑安装，源码修改即时生效
pip install -e .
```

**基本写法：PEP 660 可编辑安装**
`pip install -e . --config-settings editable_mode=compat`
```python
# 标准化可编辑安装
pip install -e .
```

---

## 依赖锁定

**基本写法：pip-tools 锁定**
`pip-compile <文件>`
```python
# 锁定依赖到 requirements.txt
pip install pip-tools
pip-compile pyproject.toml
```

**基本写法：pip-sync 同步**
`pip-sync <文件>`
```python
# 精确同步环境依赖
pip-sync requirements.txt
```

---

## uv 打包

**基本写法：uv build**
`uv build`
```python
# uv 构建包
uv build
```

**基本写法：uv publish**
`uv publish`
```python
# uv 发布到 PyPI
uv publish
```

---

## Poetry 打包

**基本写法：poetry build**
`poetry build`
```python
# poetry 构建包
poetry build
```

**基本写法：poetry publish**
`poetry publish`
```python
# poetry 发布到 PyPI
poetry publish
```

---

## ruff 配置

**基本写法：ruff 配置**
`[tool.ruff]`
```toml
# ruff 代码检查配置
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]
```
