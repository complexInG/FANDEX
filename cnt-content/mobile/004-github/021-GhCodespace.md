# gh codespace 命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 创建与列出

**基本用法:创建 codespace**
`gh codespace create`

```bash
# 交互式创建
gh codespace create

# 指定仓库与分支
gh codespace create --repo owner/repo --branch dev

# 指定机器规格
gh codespace create --machine basicLinux32gb
```

---

**基本用法:列出 codespace**
`gh codespace list`

```bash
# 列出所有 codespace
gh codespace list
```

---

## 连接与操作

**基本用法:SSH 连接**
`gh codespace ssh`

```bash
# 通过 SSH 连接到 codespace
gh codespace ssh -c <codespace名>

# 在 VS Code 中打开
gh codespace code
```

---

**基本用法:查看日志**
`gh codespace logs`

```bash
# 实时查看创建日志
gh codespace logs -c <codespace名>
```

---

**基本用法:查看详情**
`gh codespace view`

```bash
# 查看 codespace 详情
gh codespace view -c <codespace名>
```

---

## 管理生命周期

**基本用法:停止 codespace**
`gh codespace stop`

```bash
# 停止运行中的 codespace
gh codespace stop -c <codespace名>
```

---

**基本用法:重建 codespace**
`gh codespace rebuild`

```bash
# 重建(应用 devcontainer 改动)
gh codespace rebuild -c <codespace名>
```

---

**基本用法:删除 codespace**
`gh codespace delete`

```bash
# 删除指定 codespace
gh codespace delete -c <codespace名> --force

# 删除所有已停止的 codespace
gh codespace delete --days 7
```

---

## 端口管理

**基本用法:查看端口转发**
`gh codespace ports`

```bash
# 列出转发端口
gh codespace ports -c <codespace名>

# 设置端口可见性
gh codespace ports visibility 3000:public -c <codespace名>
```

---