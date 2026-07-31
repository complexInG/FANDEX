# GitHub Actions 上下文与表达式速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 常用上下文

**基本用法:引用上下文值**
`${{ <上下文>.<属性> }}`

```yaml
# github 上下文
steps:
  - run: echo ${{ github.repository }}
  - run: echo ${{ github.event_name }}
  - run: echo ${{ github.ref }}
  - run: echo ${{ github.sha }}

# 环境变量上下文
steps:
  - run: echo ${{ env.NODE_ENV }}

# 作业上下文
steps:
  - if: ${{ failure() }}
    run: echo "前置步骤失败"
```

---

## 上下文一览

**基本用法:job 上下文**
`${{ job.<属性> }}`

```yaml
# 任务状态
${{ job.status }}
${{ job.container.id }}
```

---

**基本用法:steps 上下文**
`${{ steps.<id>.<属性> }}`

```yaml
steps:
  - id: setvar
    run: echo "result=hello" >> $GITHUB_OUTPUT
  - run: echo ${{ steps.setvar.outputs.result }}
```

---

**基本用法:secrets 与 vars 上下文**
`${{ secrets.<名称> }}`

```yaml
steps:
  - run: deploy.sh ${{ secrets.DEPLOY_TOKEN }}
  - run: echo ${{ vars.ENV_NAME }}
```

---

**基本用法:matrix 上下文**
`${{ matrix.<键> }}`

```yaml
strategy:
  matrix:
    node: [18, 20]
steps:
  - run: echo "Node ${{ matrix.node }}"
```

---

## 表达式函数

**基本用法:逻辑运算**
`${{ <表达式> }}`

```yaml
if: ${{ github.ref == 'refs/heads/main' && success() }}
if: ${{ failure() || cancelled() }}
```

---

**基本用法:常用函数**
`${{ <函数>(<参数>) }}`

```yaml
# 包含判断
if: ${{ contains(github.event.head_commit.message, '[skip ci]') }}
# 字符串开头匹配
if: ${{ startsWith(github.ref, 'refs/tags/') }}
# 字符串格式化
run: echo "${{ format('Hello {0} {1}', 'GitHub', 'Actions') }}"
# JSON 转字符串
run: echo "${{ toJSON(github.event) }}"
# 从 JSON 解析
run: echo "${{ fromJSON(env.CONFIG).key }}"
```

---

**基本用法:状态检查函数**
`${{ <状态函数>() }}`

```yaml
# 所有前置步骤成功
if: ${{ success() }}
# 任一前置步骤失败
if: ${{ failure() }}
# 任务被取消
if: ${{ cancelled() }}
# 总是执行(无论成功失败)
if: ${{ always() }}
```

---