# GitHub Actions 缓存与产物速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## actions/cache 缓存

**基本用法:缓存依赖**
`uses: actions/cache@v4`

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.npm
      node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    # 部分匹配回退
    restore-keys: |
      ${{ runner.os }}-node-
```

---

**基本用法:缓存不同包管理器**
`uses: actions/cache@v4`

```yaml
# pip 缓存
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}

# Gradle 缓存
- uses: actions/cache@v4
  with:
    path: |
      ~/.gradle/caches
      ~/.gradle/wrapper
    key: ${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*') }}
```

---

## 缓存管理命令

**基本用法:通过 gh 管理缓存**
`gh cache <子命令>`

```bash
# 列出仓库缓存
gh cache list

# 按键删除缓存
gh cache delete <key>

# 删除所有缓存
gh cache delete --all
```

---

## 上传产物

**基本用法:上传构建产物**
`uses: actions/upload-artifact@v4`

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: dist-files
    path: |
      dist/
      build/
    # 保留天数
    retention-days: 14
    # 覆盖同名
    overwrite: true
    # 压缩级别
    compression-level: 6
```

---

## 下载产物

**基本用法:在工作流中下载**
`uses: actions/download-artifact@v4`

```yaml
- uses: actions/download-artifact@v4
  with:
    name: dist-files
    path: ./artifact

# 下载上一个工作流产物
- uses: actions/download-artifact@v4
  with:
    name: dist-files
    run-id: ${{ github.event.workflow_run.id }}
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

**基本用法:通过 gh 命令下载**
`gh run download`

```bash
# 下载某次运行的产物
gh run download 12345 -n dist-files
```

---