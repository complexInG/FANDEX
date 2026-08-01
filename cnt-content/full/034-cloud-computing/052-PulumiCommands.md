---
order: 520
title: Pulumi IaC 命令
module: 034-cloud-computing
category: '034-cloud-computing'
difficulty: beginner
description: Pulumi IaC 命令 的完整教学讲解。
author: fanquanpp
updated: '2026-08-01'
related: []
prerequisites: []
---

# Pulumi IaC 命令

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 安装与配置

**基本写法：安装 Pulumi CLI**
`curl -fsSL https://get.pulumi.com | sh`
```bash
# Linux/macOS 一键安装
curl -fsSL https://get.pulumi.com | sh
```

---

**基本写法：Windows 安装**
`winget install pulumi.pulumi`
```bash
# Windows 通过 winget 安装
winget install pulumi.pulumi
```

---

**基本写法：查看版本**
`pulumi version`
```bash
# 查看当前 Pulumi 版本
pulumi version
```

---

**基本写法：登录 Pulumi 服务**
`pulumi login`
```bash
# 登录 Pulumi 云服务
pulumi login
```

---

**基本写法：本地后端登录**
`pulumi login file://<路径>`
```bash
# 使用本地文件系统作为状态后端
pulumi login file://~/.pulumi
```

---

**基本写法：自托管后端**
`pulumi login <URL>`
```bash
# 登录自托管的 Pulumi 服务
pulumi login https://pulumi.example.com
```

---

## 项目创建

**基本写法：创建新项目**
`pulumi new <模板> [--name <名称>]`
```bash
# 交互式创建 AWS Python 项目
pulumi new aws-python
```

---

**基本写法：创建 TypeScript AWS 项目**
`pulumi new aws-typescript`
```bash
# 创建 AWS TypeScript 模板项目
pulumi new aws-typescript --name my-app --description "My AWS App"
```

---

**基本写法：创建 GCP 项目**
`pulumi new gcp-typescript`
```bash
# 创建 GCP TypeScript 项目
pulumi new gcp-typescript
```

---

**基本写法：创建 Azure 项目**
`pulumi new azure-typescript`
```bash
# 创建 Azure TypeScript 项目
pulumi new azure-typescript
```

---

**基本写法：从模板创建**
`pulumi new https://github.com/<user>/<repo>`
```bash
# 从 GitHub 仓库创建项目
pulumi new https://github.com/pulumi/examples/tree/master/aws-py-eks
```

---

## 配置管理

**基本写法：设置配置值**
`pulumi config set <键> <值>`
```bash
# 设置普通配置
pulumi config set aws:region us-east-1
```

---

**基本写法：设置敏感配置**
`pulumi config set <键> <值> --secret`
```bash
# 加密保存数据库密码
pulumi config set dbPassword "MyPass123!" --secret
```

---

**基本写法：查看所有配置**
`pulumi config`
```bash
# 查看当前堆栈所有配置
pulumi config
```

---

**基本写法：查看配置明文**
`pulumi config --show-secrets`
```bash
# 查看包含密钥的配置(谨慎使用)
pulumi config --show-secrets
```

---

**基本写法：获取单个配置**
`pulumi config get <键>`
```bash
# 获取指定配置值
pulumi config get aws:region
```

---

**基本写法：移除配置**
`pulumi config rm <键>`
```bash
# 删除指定配置项
pulumi config rm dbPassword
```

---

## 堆栈管理

**基本写法：创建堆栈**
`pulumi stack init <堆栈名>`
```bash
# 创建生产堆栈
pulumi stack init production
```

---

**基本写法：列出堆栈**
`pulumi stack ls`
```bash
# 列出项目所有堆栈
pulumi stack ls
```

---

**基本写法：选择堆栈**
`pulumi stack select <堆栈名>`
```bash
# 切换到 dev 堆栈
pulumi stack select dev
```

---

**基本写法：查看当前堆栈**
`pulumi stack`
```bash
# 显示当前堆栈名称
pulumi stack
```

---

**基本写法：删除堆栈**
`pulumi stack rm <堆栈名>`
```bash
# 删除指定堆栈(需先清空资源)
pulumi stack rm staging
```

---

**基本写法：导出堆栈状态**
`pulumi stack export --file <文件>`
```bash
# 导出堆栈状态到本地文件
pulumi stack export --file state.json
```

---

## 部署与预览

**基本写法：预览变更**
`pulumi preview`
```bash
# 预览将要执行的变更
pulumi preview
```

---

**基本写法：部署基础设施**
`pulumi up`
```bash
# 部署到当前堆栈
pulumi up
```

---

**基本写法：跳过确认部署**
`pulumi up --yes`
```bash
# 自动确认部署(用于 CI/CD)
pulumi up --yes
```

---

**基本写法：部署指定堆栈**
`pulumi up --stack <堆栈名>`
```bash
# 部署到 production 堆栈
pulumi up --stack production --yes
```

---

**基本写法：显示详细差异**
`pulumi up --diff`
```bash
# 部署时显示详细 diff
pulumi up --diff
```

---

**基本写法：销毁资源**
`pulumi destroy`
```bash
# 销毁堆栈中所有资源
pulumi destroy
```

---

## 输出与查询

**基本写法：查看输出**
`pulumi stack output`
```bash
# 列出所有输出值
pulumi stack output
```

---

**基本写法：查看单个输出**
`pulumi stack output <输出名>`
```bash
# 获取指定输出值
pulumi stack output instanceId
```

---

**基本写法：输出 JSON 格式**
`pulumi stack output --json`
```bash
# JSON 格式输出便于脚本处理
pulumi stack output --json
```

---

**基本写法：显示输出值的密钥**
`pulumi stack output <名称> --show-secrets`
```bash
# 查看敏感输出值
pulumi stack output dbPassword --show-secrets
```

---

**基本写法：在程序中获取输出**
```typescript
// 在 Pulumi 程序中引用其他堆栈的输出
import * as pulumi from "@pulumi/pulumi";

const infraStack = new pulumi.StackReference("myorg/infra/prod");
const vpcId = infraStack.getOutput("vpcId");
```

---

## 状态管理

**基本写法：查看状态资源**
`pulumi stack --show-ids`
```bash
# 查看堆栈中所有资源 ID
pulumi stack --show-ids
```

---

**基本写法：导入资源**
`pulumi import <类型> <名称> <ID>`
```bash
# 导入现有 EC2 实例到 Pulumi 管理
pulumi import aws:ec2/instance:Instance my-instance i-1234567890abcdef0
```

---

**基本写法：导入并生成代码**
`pulumi import <类型> <名称> <ID> --out <目录>`
```bash
# 生成导入资源的代码
pulumi import aws:ec2/instance:Instance my-instance i-1234567890abcdef0 --out imported
```

---

**基本写法：删除状态中的资源**
`pulumi state delete <资源URN>`
```bash
# 从状态中移除资源(不删除实际资源)
pulumi state delete "urn:pulumi:dev::my-app::aws:ec2/instance:Instance::my-instance"
```

---

**基本写法：取消操作**
`pulumi cancel`
```bash
# 取消正在进行的更新
pulumi cancel
```

---

## 策略与合规

**基本写法：启用 Policy Pack**
`pulumi up --policy-pack <策略包路径>`
```bash
# 部署时应用 Policy Pack
pulumi up --policy-pack ./policies
```

---

**基本写法：强制执行策略**
`pulumi up --policy-pack <路径> --policy-pack-enforcement-level mandatory`
```bash
# 强制策略(违规时阻止部署)
pulumi up \
  --policy-pack ./policies \
  --policy-pack-enforcement-level mandatory
```

---

**基本写法：查看策略违规**
`pulumi preview --policy-pack <路径>`
```bash
# 预览时仅检查策略违规
pulumi preview --policy-pack ./policies
```

---

**基本写法：创建 Policy Pack**
```typescript
// policies/index.ts
import { PolicyPack } from "@pulumi/policy";

new PolicyPack("my-policy-pack", {
  policies: [
    {
      name: "no-public-ec2",
      description: "禁止 EC2 实例直接关联公网 IP",
      enforcementLevel: "mandatory",
      validateResource: (args, reportViolation) => {
        if (args.type === "aws:ec2/instance:Instance") {
          if (args.props.associatePublicIpAddress) {
            reportViolation("EC2 不应直接关联公网 IP");
          }
        }
      },
    },
  ],
});
```

---

## 提供者配置

**基本写法：配置 AWS 提供者**
```typescript
// 配置 AWS 提供者指定区域
import * as aws from "@pulumi/aws";

const provider = new aws.Provider("my-provider", {
  region: "us-west-2",
});
```

---

**基本写法：使用指定 profile**
`pulumi config set aws:profile <profile名>`
```bash
# 使用特定 AWS profile
pulumi config set aws:profile production
```

---

**基本写法：多区域部署**
```typescript
// 为不同区域创建不同提供者
import * as aws from "@pulumi/aws";

const usEastProvider = new aws.Provider("us-east", { region: "us-east-1" });
const usWestProvider = new aws.Provider("us-west", { region: "us-west-2" });
```

---

**基本写法：自定义提供者端点**
```typescript
// 使用 LocalStack 端点本地测试
import * as aws from "@pulumi/aws";

const localstackProvider = new aws.Provider("localstack", {
  endpoints: [{ hostname: "localhost", port: 4566, protocol: "http" }],
  skipCredentialsValidation: true,
  skipMetadataApiCheck: true,
});
```

---

## CI/CD 集成

**基本写法：设置 GitHub Actions**
```yaml
# .github/workflows/pulumi.yml
name: Pulumi
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm install
      - uses: pulumi/actions@v5
        with:
          command: up
          stack-name: production
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

---

**基本写法：使用 access token**
`pulumi login --token <token>`
```bash
# 通过 token 非交互登录(用于 CI)
pulumi login --token pul-xxxxxxxxxx
```

---

**基本写法：CI 模式**
`pulumi up --yes --non-interactive`
```bash
# 非交互模式部署
pulumi up --yes --non-interactive
```

---

**基本写法：使用 GitHub OIDC**
```yaml
# 通过 GitHub OIDC 部署到 AWS
permissions:
  id-token: write
  contents: read
jobs:
  deploy:
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/github-actions
          aws-region: us-east-1
      - uses: pulumi/actions@v5
        with:
          command: up
          stack-name: production
```

---

## 组件与抽象

**基本写法：创建组件资源**
```typescript
// 创建可复用的组件资源
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

export class WebServer extends pulumi.ComponentResource {
  public readonly instanceId: pulumi.Output<string>;

  constructor(name: string, opts?: pulumi.ComponentResourceOptions) {
    super("my:module:WebServer", name, {}, opts);

    const sg = new aws.ec2.SecurityGroup(`${name}-sg`, {
      ingress: [{ protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] }],
    }, { parent: this });

    const instance = new aws.ec2.Instance(`${name}-instance`, {
      instanceType: "t3.micro",
      ami: "ami-0c55b159cbfafe1f0",
      vpcSecurityGroupIds: [sg.id],
    }, { parent: this });

    this.instanceId = instance.id;
    this.registerOutputs({ instanceId: this.instanceId });
  }
}
```

---

**基本写法：使用组件**
```typescript
// 在主程序中使用自定义组件
import { WebServer } from "./webserver";

const web1 = new WebServer("web1");
const web2 = new WebServer("web2");
export const web1Id = web1.instanceId;
```

---

**基本写法：导出多资源**
```typescript
// 同时导出多个相关资源
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("my-bucket");
const table = new aws.dynamodb.Table("my-table", {
  attributes: [{ name: "id", type: "S" }],
  hashKey: "id",
  billingMode: "PAY_PER_REQUEST",
});

export const bucketName = bucket.id;
export const tableName = table.id;
```

---

## 模板与示例

**基本写法：列出所有模板**
`pulumi new --list-templates`
```bash
# 查看所有可用项目模板
pulumi new --list-templates
```

---

**基本写法：使用 Kubernetes 模板**
`pulumi new kubernetes-typescript`
```bash
# 创建 K8s TypeScript 项目
pulumi new kubernetes-typescript
```

---

**基本写法：使用容器模板**
`pulumi new dockerfile`
```bash
# 从 Dockerfile 创建项目
pulumi new dockerfile
```

---

**基本写法：查看示例**
`pulumi new --list-templates | grep example`
```bash
# 列出示例模板
pulumi new --list-templates
```

---

## 别名与重构

**基本写法：重命名资源**
```typescript
// 通过 alias 重命名资源而不重建
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("new-name", {
  // 其他属性
}, {
  aliases: [{ name: "old-name" }],
});
```

---

**基本写法：跨类型别名**
```typescript
// 跨类型迁移资源
const instance = new aws.ec2.Instance("my-instance", {
  // ...
}, {
  aliases: [{ type: "aws:ec2/instance:InstanceV1" }],
});
```

---

**基本写法：父资源别名**
```typescript
// 修改父资源时保持子资源
const child = new SomeResource("child", { /* ... */ }, {
  parent: newParent,
  aliases: [{ parent: oldParent }],
});
```

---

**基本写法：批量别名**
```typescript
// 多个别名同时使用
const resource = new SomeResource("name", { /* ... */ }, {
  aliases: [
    { name: "old-name-1" },
    { name: "old-name-2" },
    { type: "old:type:Resource" },
  ],
});
```

## 参考文献



AWS 文档：https://docs.aws.amazon.com/
Microsoft Azure 文档：https://learn.microsoft.com/zh-cn/azure/
Google Cloud 文档：https://cloud.google.com/docs?hl=zh-cn
阿里云文档：https://help.aliyun.com/
CNCF 云原生全景：https://landscape.cncf.io/

## 延伸阅读



虚拟化与容器，见 034-cloud-computing 模块相关文档。
Kubernetes 架构，见 034-cloud-computing 模块 K8s 文档。
DevOps 与 IaC，见 031-devops 模块。
尚硅谷 Bilibili 空间（https://space.bilibili.com/302417610 ）提供云计算课程。

## 模块文档速查表

| 文档 | 主题 | 与本文的关联 |
| --- | --- | --- |
| 云计算基础 | 001-CloudComputingBasics | 本文的前置基础 |
| 云网络与存储 | 002-CloudNetworkStorage | 本文的并列主题 |
| 容器与编排 | 003-ContainerOrchestration | 本文的并列主题 |
| 基础设施即代码 | 004-IaC | 本文的前置基础 |
| IaaS与PaaS与SaaS | 005-IaaSPaaSSaaS | 本文的并列主题 |
| 虚拟化技术 | 006-VirtualizationTech | 本文的并列主题 |
| 云架构设计 | 007-CloudArchitectureDesign | 本文的原理深化 |
| 公有云与私有云与混合云 | 008-PublicCloudPrivateCloudHybridCloud | 本文的并列主题 |
| Docker深度解析 | 009-DockerDeepAnalysis | 本文的并列主题 |
| 云原生应用 | 010-CloudNativeApp | 本文的并列主题 |
| Kubernetes架构 | 011-KubernetesArchitecture | 本文的原理深化 |
| 云数据库服务 | 012-CloudDatabaseService | 本文的并列主题 |
| Kubernetes核心资源 | 013-KubernetesCore | 本文的并列主题 |
| 云存储服务 | 014-CloudStorageService | 本文的并列主题 |
| Kubernetes网络 | 015-KubernetesNetwork | 本文的并列主题 |
| 云网络服务 | 016-CloudNetworkService | 本文的并列主题 |
| Kubernetes存储 | 017-KubernetesStorage | 本文的并列主题 |
| 云安全服务 | 018-CloudSecurityService | 本文的安全延伸 |
| Helm包管理 | 019-HelmPackageManagement | 本文的并列主题 |
| 云成本优化 | 020-CloudCostOptimization | 本文的性能延伸 |
| 12要素应用 | 021-TwelveFactorApp | 本文的并列主题 |
| 微服务架构 | 022-MicroserviceArchitecture | 本文的原理深化 |
| 服务网格 | 023-ServiceMesh | 本文的并列主题 |
| 可观测性 | 024-Observability | 本文的并列主题 |
| AWS核心服务 | 025-AWSCore | 本文的并列主题 |
| 多云与混合云架构 | 026-MultiCloudHybridArchitecture | 本文的原理深化 |
| 负载均衡与自动伸缩 | 027-LoadBalanceAutoScaling | 本文的并列主题 |
| 无服务器架构 | 028-ServerlessArchitecture | 本文的原理深化 |
| 云迁移6R策略 | 029-CloudMigration6RStrategy | 本文的并列主题 |
| 云计算 AWS CLI 配置 | 030-AWSCliConfigure | 本文的并列主题 |
| 云计算 AWS S3 命令 | 031-AWSS3Command | 本文的并列主题 |
| 云计算 AWS EC2 命令 | 032-AWSEC2Command | 本文的并列主题 |
| 云计算 AWS Lambda 命令 | 033-AWSLambdaCommand | 本文的并列主题 |
| 云计算 AWS IAM 命令 | 034-AWSIAMCommand | 本文的并列主题 |
| 云计算 AWS CloudFormation | 035-AWSCloudFormation | 本文的并列主题 |
| 云计算 Azure CLI 配置 | 036-AzureCliConfigure | 本文的并列主题 |
| 云计算 Azure 资源组与 VM | 037-AzureGroupVMCommand | 本文的并列主题 |
| 云计算 Azure 存储命令 | 038-AzureStorageCommand | 本文的并列主题 |
| 云计算 GCP gcloud 配置 | 039-GCPCliConfigure | 本文的并列主题 |
| 云计算 GCP Compute 与 Storage | 040-GCPComputeStorage | 本文的并列主题 |
| 云计算 Terraform 基础 | 041-TerraformBasic | 本文的前置基础 |
| 云计算 Terraform 状态与模块 | 042-TerraformStateModule | 本文的并列主题 |
| AWS CloudWatch 监控日志命令 | 043-AWSCloudWatch | 本文的并列主题 |
| AWS RDS 数据库命令 | 044-AWSRDSCommands | 本文的并列主题 |
| AWS VPC 网络命令 | 045-AWSVPCCommands | 本文的并列主题 |
| AWS SQS/SNS 消息队列命令 | 046-AWSSQSCommands | 本文的并列主题 |
| AWS DynamoDB 命令 | 047-AWSDynamoDB | 本文的并列主题 |
| Azure Functions 命令 | 048-AzureFunctions | 本文的并列主题 |
| Azure AKS Kubernetes 命令 | 049-AzureAKSCommands | 本文的并列主题 |
| GCP GKE Kubernetes 命令 | 050-GCPGKECommands | 本文的并列主题 |
| GCP BigQuery 命令 | 051-GCPBigQuery | 本文的并列主题 |
| Pulumi IaC 命令 | 052-PulumiCommands | 本文自身 |
| Harbor 私有镜像仓库命令 | 053-HarborRegistry | 本文的并列主题 |
| cloud-init 云实例初始化 | 054-CloudInitCommands | 本文的并列主题 |
| AWS CloudFront CDN 命令 | 055-AWSCloudFront | 本文的并列主题 |
