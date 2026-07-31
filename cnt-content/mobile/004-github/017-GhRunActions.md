# gh run Actions 运行命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 查看运行记录

**基本用法:列出工作流运行**
`gh run list`

```bash
# 列出最近的运行记录
gh run list

# 按工作流过滤
gh run list --workflow=deploy.yml

# 按状态过滤
gh run list --status=failure

# 按分支过滤并限制条数
gh run list --branch=main --limit 10
```

---

**基本用法:查看运行详情**
`gh run view <运行ID>`

```bash
# 查看某次运行的详情
gh run view 12345

# 查看日志
gh run view 12345 --log

# 仅查看失败步骤日志
gh run view 12345 --log-failed

# 在浏览器打开
gh run view 12345 --web
```

---

## 监视运行

**基本用法:实时监视运行**
`gh run watch <运行ID>`

```bash
# 持续监视直到完成
gh run watch 12345

# 完成后退出并显示结果
gh run watch 12345 --exit-status
```

---

## 控制运行

**基本用法:重新运行**
`gh run rerun <运行ID>`

```bash
# 重新运行所有任务
gh run rerun 12345

# 仅重新运行失败的任务
gh run rerun 12345 --failed

# 调试模式重新运行
gh run rerun 12345 --debug
```

---

**基本用法:取消运行**
`gh run cancel <运行ID>`

```bash
# 取消正在运行的流水线
gh run cancel 12345
```

---

**基本用法:删除运行记录**
`gh run delete <运行ID>`

```bash
# 删除某次运行记录
gh run delete 12345
```

---

## 下载产物

**基本用法:下载构建产物**
`gh run download <运行ID>`

```bash
# 下载所有产物到当前目录
gh run download 12345

# 下载指定产物
gh run download 12345 -n build-artifacts

# 下载到指定目录
gh run download 12345 --dir ./out
```

---