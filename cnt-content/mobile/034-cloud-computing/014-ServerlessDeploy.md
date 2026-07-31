# 云计算 Serverless 部署

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## Serverless Framework 安装

**基本写法：安装 Serverless CLI**
`npm install -g serverless`
```bash
# 全局安装 Serverless Framework
npm install -g serverless
```

---

**基本写法：查看版本**
`serverless --version`
```bash
# 查看当前 Serverless CLI 版本
serverless --version
```

---

**基本写法：查看帮助**
`serverless --help`
```bash
# 查看所有可用命令
serverless --help
```

---

## 凭证配置

**基本写法：配置 AWS 凭证**
`serverless config credentials --provider aws --key <访问密钥> --secret <私密密钥>`
```bash
# 为 Serverless 配置 AWS 部署凭证
serverless config credentials --provider aws --key AKIAIOSFODNN7EXAMPLE --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

---

**基本写法：指定 profile 部署**
`serverless deploy --aws-profile <配置名>`
```bash
# 使用特定 AWS profile 部署
serverless deploy --aws-profile production
```

---

## 项目创建

**基本写法：创建 AWS Python 项目**
`serverless create --template aws-python3 --path <路径>`
```bash
# 创建 Python 3 项目模板
serverless create --template aws-python3 --path my-service
```

---

**基本写法：创建 AWS Node.js 项目**
`serverless create --template aws-nodejs --path <路径>`
```bash
# 创建 Node.js 项目模板
serverless create --template aws-nodejs --path my-service
```

---

**基本写法：从已有模板创建**
`serverless create --template-url <GitHub URL> --path <路径>`
```bash
# 从 GitHub 模板创建项目
serverless create --template-url https://github.com/serverless/examples/tree/main/aws-node-rest-api --path my-api
```

---

## 部署操作

**基本写法：部署服务**
`serverless deploy [--stage <环境>] [--region <区域>]`
```bash
# 部署到 dev 环境的 us-east-1 区域
serverless deploy --stage dev --region us-east-1
```

---

**基本写法：部署单个函数**
`serverless deploy function --function <函数名>`
```bash
# 仅快速部署单个函数代码
serverless deploy function --function myHandler
```

---

**基本写法：部署详细输出**
`serverless deploy --verbose`
```bash
# 显示部署详细日志
serverless deploy --verbose
```

---

**基本写法：移除服务**
`serverless remove [--stage <环境>]`
```bash
# 删除服务及所有关联资源
serverless remove --stage dev
```

---

## 调用与日志

**基本写法：调用函数**
`serverless invoke --function <函数名> [--stage <环境>]`
```bash
# 在云端调用指定函数
serverless invoke --function myHandler --stage dev
```

---

**基本写法：本地调用函数**
`serverless invoke local --function <函数名>`
```bash
# 在本地环境调用函数便于调试
serverless invoke local --function myHandler
```

---

**基本写法：传递事件数据**
`serverless invoke --function <函数名> --path <事件文件>`
```bash
# 通过 JSON 文件传入事件
serverless invoke --function myHandler --path event.json
```

---

**基本写法：查看函数日志**
`serverless logs --function <函数名> [--tail]`
```bash
# 实时跟踪函数日志
serverless logs --function myHandler --tail
```

---

**基本写法：查看所有日志流**
`serverless logs --function <函数名> --startTime <时间>`
```bash
# 查看指定时间起的日志
serverless logs --function myHandler --startTime 1h
```

---

## 配置文件

**基本写法：serverless.yml 基本结构**
```yaml
# Serverless 服务配置文件
service: my-service
frameworkVersion: '3'
provider:
  name: aws
  runtime: python3.12
  region: us-east-1
functions:
  hello:
    handler: handler.hello
```

---

**基本写法：配置 HTTP 事件**
```yaml
# 为函数绑定 HTTP API 触发器
functions:
  api:
    handler: handler.api
    events:
      - httpApi:
          path: /users
          method: get
```

---

**基本写法：配置定时触发**
```yaml
# 配置 EventBridge 定时触发
functions:
  cron:
    handler: handler.cron
    events:
      - schedule:
          rate: cron(0 12 * * ? *)
          enabled: true
```

---

**基本写法：配置环境变量**
```yaml
# 为函数注入环境变量
functions:
  hello:
    handler: handler.hello
    environment:
      TABLE_NAME: my-table
      STAGE: ${sls:stage}
```

---

## 信息查看

**基本写法：查看已部署信息**
`serverless info [--stage <环境>]`
```bash
# 查看服务部署摘要与端点
serverless info --stage dev
```

---

**基本写法：打印编译后配置**
`serverless print [--stage <环境>]`
```bash
# 输出变量解析后的完整配置
serverless print --stage dev
```

---

**基本写法：滚动更新函数**
`serverless rollback --function <函数名> --version <版本>`
```bash
# 回滚函数到指定历史版本
serverless rollback --function myHandler --version 5
```

---

## 插件管理

**基本写法：安装插件**
`npm install --save-dev <插件名>`
```bash
# 安装 serverless-offline 插件用于本地模拟
npm install --save-dev serverless-offline
```

---

**基本写法：在配置中启用插件**
```yaml
# 在 serverless.yml 中注册插件
plugins:
  - serverless-offline
  - serverless-python-requirements
```
