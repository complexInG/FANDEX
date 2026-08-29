---
order: 10
title: cloud-computing 模块文档合集
module: 'cloud-computing'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：034-cloud-computing/001-CloudComputingBasics.md ============ -->

## 1. 云计算概念与演进

### 1.1 什么是云计算

云计算是通过互联网按需提供**计算资源（服务器、存储、数据库、网络、软件）**的技术模式，核心特征是按需自助、广泛的网络接入、资源池化、快速弹性和可计量服务。

### 1.2 发展历程

| 阶段           | 时间      | 特点                     | 代表           |
| :------------- | :-------- | :----------------------- | :------------- |
| **大型机时代** | 1960s     | 集中计算、分时共享       | IBM System/360 |
| **PC 时代**    | 1980s-90s | 分布式计算、客户端服务器 | PC 局域网      |
| **网格计算**   | 2000s 初  | 跨组织资源共享           | SETI@home      |
| **云计算兴起** | 2006      | AWS 发布，按需付费       | AWS EC2        |
| **云原生时代** | 2015+     | 容器化、微服务、DevOps   | Kubernetes     |
| **智能云**     | 2023+     | AI + 云、Serverless      | AI 云服务      |

### 1.3 云计算核心特征

| 特征             | 说明                           |
| :--------------- | :----------------------------- |
| **按需自助服务** | 用户自行申请资源，无需人工干预 |
| **广泛网络接入** | 通过网络标准机制访问           |
| **资源池化**     | 多租户共享物理资源，动态分配   |
| **快速弹性**     | 资源可快速扩缩容，按需自动调整 |
| **可计量服务**   | 资源使用可监控、可计量、可计费 |

## 2. 服务模型

### 2.1 三种服务模型

```mermaid
flowchart TD
    SaaS[SaaS 软件即服务<br/>完整应用：Gmail、Salesforce、钉钉] --> PaaS[PaaS 平台即服务<br/>运行环境：Heroku、Cloud Run、函数计算]
    PaaS --> IaaS[IaaS 基础设施即服务<br/>虚拟机/网络：AWS EC2、阿里云 ECS]
    IaaS --> HW[物理硬件（数据中心）]
```

### 2.2 服务模型对比

| 维度         | IaaS               | PaaS           | SaaS       |
| :----------- | :----------------- | :------------- | :--------- |
| **你管理**   | 应用、数据、运行时 | 应用、数据     | 几乎不需要 |
| **云商管理** | OS、中间件、运行时 | OS、中间件     | 全部       |
| **灵活性**   | 最高               | 中等           | 最低       |
| **运维负担** | 最重               | 中等           | 最轻       |
| **典型产品** | EC2、ECS           | Cloud Run、SAE | 钉钉、飞书 |
| **适用场景** | 定制化基础设施     | 应用快速部署   | 即开即用   |

## 3. 部署模型

### 3.1 四种部署模型

| 模型       | 说明                       | 优势           | 劣势           |
| :--------- | :------------------------- | :------------- | :------------- |
| **公有云** | 第三方云商提供，多租户共享 | 低成本、弹性好 | 安全合规顾虑   |
| **私有云** | 企业自建或托管，独享资源   | 安全可控       | 成本高、弹性差 |
| **混合云** | 公有云 + 私有云组合        | 灵活平衡       | 架构复杂       |
| **多云**   | 使用多个云服务商           | 避免锁定       | 管理复杂       |

### 3.2 混合云架构

```mermaid
flowchart LR
    P[私有云<br/>核心业务<br/>敏感数据] <--> G[混合云网关<br/>专线/VPN<br/>数据同步] <--> U[公有云<br/>弹性业务<br/>大数据分析]
```

### 3.3 主流云服务商

| 云商       | 优势                | 代表产品                |
| :--------- | :------------------ | :---------------------- |
| **AWS**    | 生态最全、全球覆盖  | EC2、S3、Lambda         |
| **Azure**  | 企业集成、混合云    | VM、Blob、Functions     |
| **GCP**    | 大数据/AI、K8s 原生 | GCE、GCS、Cloud Run     |
| **阿里云** | 国内领先、生态完善  | ECS、OSS、函数计算      |
| **腾讯云** | 游戏社交、音视频    | CVM、COS、SCF           |
| **华为云** | 政企市场、AI        | ECS、OBS、FunctionGraph |

## 4. 高可用架构设计

### 4.1 高可用核心指标

| 指标        | 计算方式    | 年停机时间 |
| :---------- | :---------- | :--------- |
| **99%**     | 1 - 0.99    | 87.6 小时  |
| **99.9%**   | 1 - 0.999   | 8.76 小时  |
| **99.99%**  | 1 - 0.9999  | 52.6 分钟  |
| **99.999%** | 1 - 0.99999 | 5.26 分钟  |

### 4.2 多可用区架构

```mermaid
flowchart TD
    subgraph Region[Region 区域]
        subgraph AZa[AZ-a]
            A1[实例 x2]
            R1[RDS 主]
        end
        subgraph AZb[AZ-b]
            A2[实例 x2]
            R2[RDS 从]
        end
        subgraph AZc[AZ-c]
            A3[实例 x2]
            R3[RDS 从]
        end
    end
```

### 4.3 高可用设计原则

| 原则             | 实践                       |
| :--------------- | :------------------------- |
| **消除单点故障** | 多实例、多可用区部署       |
| **故障检测**     | 健康检查、心跳检测         |
| **自动恢复**     | 自动重启、自动替换故障实例 |
| **数据冗余**     | 多副本、跨区域备份         |
| **优雅降级**     | 核心功能优先，非核心可降级 |
| **限流熔断**     | 防止级联故障               |

## 5. 负载均衡配置

### 5.1 负载均衡类型

| 类型            | OSI 层 | 特点                      | 适用场景      |
| :-------------- | :----- | :------------------------ | :------------ |
| **L4 负载均衡** | 传输层 | 基于 IP+端口转发          | TCP/UDP 服务  |
| **L7 负载均衡** | 应用层 | 基于 HTTP 头/URL/内容转发 | Web 应用、API |

### 5.2 负载均衡算法

| 算法            | 说明                     | 适用场景       |
| :-------------- | :----------------------- | :------------- |
| **轮询**        | 依次分配请求             | 服务器性能一致 |
| **加权轮询**    | 按权重比例分配           | 服务器性能不同 |
| **最少连接**    | 分配给连接数最少的服务器 | 长连接服务     |
| **IP Hash**     | 同一 IP 分配到同一服务器 | 会话保持       |
| **一致性 Hash** | 减少节点变化时的请求迁移 | 缓存服务       |

### 5.3 Nginx 负载均衡配置

```nginx
# nginx.conf
upstream backend {
    # 加权轮询
    server 10.0.1.1:8080 weight=3;
    server 10.0.1.2:8080 weight=2;
    server 10.0.1.3:8080 weight=1;

    # 健康检查
    # server 10.0.1.4:8080 backup;  # 备用服务器

    keepalive 32;  # 长连接数
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 连接超时
        proxy_connect_timeout 5s;
        proxy_send_timeout 30s;
        proxy_read_timeout 30s;
    }

    # 健康检查端点
    location /health {
        access_log off;
        return 200 "OK";
    }
}
```

### 5.4 云负载均衡配置（阿里云 SLB）

```bash
# 使用阿里云 CLI 创建负载均衡
aliyun slb CreateLoadBalancer \
  --RegionId cn-hangzhou \
  --LoadBalancerName web-slb \
  --AddressType internet \
  --InternetChargeType paybytraffic

# 添加后端服务器
aliyun slb AddBackendServers \
  --LoadBalancerId lb-xxx \
  --BackendServers '[{"ServerId":"i-xxx1","Weight":"100"},{"ServerId":"i-xxx2","Weight":"100"}]'

# 创建监听
aliyun slb CreateLoadBalancerHTTPListener \
  --LoadBalancerId lb-xxx \
  --ListenerPort 80 \
  --BackendServerPort 8080 \
  --HealthCheckURI /health \
  --HealthCheckInterval 5
```

## 6. 弹性伸缩策略

### 6.1 伸缩模式

| 模式         | 触发方式       | 适用场景           |
| :----------- | :------------- | :----------------- |
| **定时伸缩** | 定时任务触发   | 可预测的周期性流量 |
| **动态伸缩** | 监控指标触发   | 不可预测的突发流量 |
| **固定数量** | 保持固定实例数 | 稳定业务           |
| **手动伸缩** | 人工调整       | 临时需求           |

### 6.2 动态伸缩策略

```yaml
# 伸缩策略配置示例
scaling_policies:
  # 扩容策略
  scale_out:
    trigger:
      metric: cpu_utilization
      threshold: 70%
      duration: 3m
    action:
      add_instances: 2
      cooldown: 300s

  # 缩容策略
  scale_in:
    trigger:
      metric: cpu_utilization
      threshold: 30%
      duration: 5m
    action:
      remove_instances: 1
      cooldown: 300s

  # 定时策略
  scheduled:
    - name: morning_peak
      recurrence: '0 7 * * 1-5' # 工作日7点
      min_size: 10
      max_size: 20
    - name: night_off_peak
      recurrence: '0 22 * * *' # 每晚22点
      min_size: 2
      max_size: 5
```

### 6.3 伸缩组配置要点

| 配置项         | 说明                           | 建议               |
| :------------- | :----------------------------- | :----------------- |
| **最小实例数** | 伸缩组最少保持的实例数         | 保证基础可用       |
| **最大实例数** | 伸缩组最多扩展的实例数         | 控制成本上限       |
| **冷却时间**   | 伸缩活动后的等待时间           | 300-600秒          |
| **健康检查**   | 实例健康状态检测               | 自动替换不健康实例 |
| **启动配置**   | 新实例的模板（镜像/规格/脚本） | 预装应用           |

## 7. 云成本优化

### 7.1 成本构成

| 成本类型     | 占比   | 优化空间           |
| :----------- | :----- | :----------------- |
| **计算资源** | 40-60% | 弹性伸缩、预留实例 |
| **存储资源** | 15-25% | 分层存储、生命周期 |
| **网络流量** | 10-20% | 内网通信、CDN      |
| **数据库**   | 10-15% | 规格优化、读写分离 |
| **其他服务** | 5-10%  | 按需使用           |

### 7.2 成本优化策略

| 策略                  | 说明                       | 预估节省 |
| :-------------------- | :------------------------- | :------- |
| **预留实例/包年包月** | 长期使用预付费             | 30-60%   |
| **弹性伸缩**          | 按负载自动调整资源         | 20-40%   |
| **Spot/抢占式实例**   | 使用闲置算力               | 60-90%   |
| **存储分层**          | 热数据标准存储、冷数据归档 | 40-70%   |
| **资源右置**          | 选择合适的实例规格         | 20-30%   |
| **闲置资源回收**      | 清理未使用的资源           | 10-20%   |

### 7.3 成本监控脚本

```python
import boto3
from datetime import datetime, timedelta

def get_daily_cost(days: int = 30) -> list:
    """获取 AWS 每日成本"""
    client = boto3.client('ce', region_name='us-east-1')

    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

    response = client.get_cost_and_usage(
        TimePeriod={'Start': start_date, 'End': end_date},
        Granularity='DAILY',
        Metrics=['BlendedCost'],
        GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
    )

    costs = []
    for result in response['ResultsByTime']:
        date = result['TimePeriod']['Start']
        total = sum(
            float(group['Metrics']['BlendedCost']['Amount'])
            for group in result['Groups']
        )
        costs.append({'date': date, 'total': round(total, 2)})

    return costs

def find_idle_resources():
    """发现闲置资源"""
    ec2 = boto3.resource('ec2')

    # 未附加的 EBS 卷
    volumes = list(ec2.volumes.filter(Filters=[
        {'Name': 'status', 'Values': ['available']}
    ]))
    print(f"未附加的 EBS 卷: {len(volumes)} 个")

    # 未使用的弹性 IP
    eips = [eip for eip in ec2.vpc_addresses.all()
            if eip.instance_id is None]
    print(f"未使用的弹性 IP: {len(eips)} 个")

    # 停止的实例
    stopped = list(ec2.instances.filter(Filters=[
        {'Name': 'instance-state-name', 'Values': ['stopped']}
    ]))
    print(f"停止的实例: {len(stopped)} 个")
```

### 7.4 FinOps 实践

```
成本可视化 → 成本归因 → 成本优化 → 持续治理
     ↓            ↓           ↓           ↓
  预算告警     标签分摊     采购策略     治理策略
```

| 阶段         | 关键活动                     | 工具                    |
| :----------- | :--------------------------- | :---------------------- |
| **Inform**   | 成本可视化、预算告警         | CloudHealth、云原生工具 |
| **Optimize** | 资源右置、预留实例、闲置回收 | Spot.io、Kubecost       |
| **Operate**  | 标签治理、成本分摊、持续优化 | FinOps 平台             |

<!-- ============ 文档分隔线：034-cloud-computing/002-CloudNetworkStorage.md ============ -->

## 1. VPC 虚拟私有云

### 1.1 VPC 概述

VPC（Virtual Private Cloud）是在公有云上创建的**逻辑隔离的虚拟网络**，用户可自定义网络拓扑、IP 地址范围、路由表和网关。

### 1.2 VPC 核心组件

```mermaid
flowchart TD
    subgraph VPC[VPC 10.0.0.0/16]
        subgraph Pub[公有子网 10.0.1.0/24]
            ALB[ALB]
            NAT[NAT GW]
        end
        subgraph Priv[私有子网 10.0.2.0/24]
            App[App]
            DB[DB]
        end
    end
    VPC --> IGW[Internet GW]
    IGW --> Net[Internet]
```

| 组件            | 说明                             |
| :-------------- | :------------------------------- |
| **VPC**         | 虚拟网络容器，定义 CIDR 地址范围 |
| **子网**        | VPC 内的网段，关联可用区         |
| **Internet GW** | 互联网网关，提供公网访问         |
| **NAT GW**      | NAT 网关，私有子网访问公网       |
| **路由表**      | 控制网络流量走向                 |
| **安全组**      | 实例级防火墙，控制入站出站规则   |
| **NACL**        | 子网级无状态防火墙               |

### 1.3 子网规划

```python
# 子网规划示例
subnet_planning = {
    "vpc_cidr": "10.0.0.0/16",       # 65536 个地址
    "subnets": {
        # 公有子网 - 面向互联网
        "public-web-a": {
            "cidr": "10.0.1.0/24",    # 256 个地址
            "az": "us-east-1a",
            "type": "public",
            "purpose": "负载均衡、NAT网关"
        },
        "public-web-b": {
            "cidr": "10.0.2.0/24",
            "az": "us-east-1b",
            "type": "public",
            "purpose": "负载均衡、NAT网关"
        },
        # 私有子网 - 应用层
        "private-app-a": {
            "cidr": "10.0.10.0/24",
            "az": "us-east-1a",
            "type": "private",
            "purpose": "应用服务器"
        },
        "private-app-b": {
            "cidr": "10.0.11.0/24",
            "az": "us-east-1b",
            "type": "private",
            "purpose": "应用服务器"
        },
        # 私有子网 - 数据层
        "private-db-a": {
            "cidr": "10.0.20.0/24",
            "az": "us-east-1a",
            "type": "private",
            "purpose": "数据库"
        },
        "private-db-b": {
            "cidr": "10.0.21.0/24",
            "az": "us-east-1b",
            "type": "private",
            "purpose": "数据库"
        }
    }
}
```

### 1.4 路由表配置

| 路由表         | 目标        | 下一跳  | 说明         |
| :------------- | :---------- | :------ | :----------- |
| **公有路由表** | 10.0.0.0/16 | local   | VPC 内部通信 |
|                | 0.0.0.0/0   | igw-xxx | 互联网网关   |
| **私有路由表** | 10.0.0.0/16 | local   | VPC 内部通信 |
|                | 0.0.0.0/0   | nat-xxx | NAT 网关     |

## 2. 安全组配置

### 2.1 安全组规则

```json5
// 安全组规则示例 - Web 服务器
{
  SecurityGroupId: 'sg-web',
  Rules: {
    Inbound: [
      {
        Protocol: 'TCP',
        Port: 443,
        Source: '0.0.0.0/0',
        Description: 'HTTPS 入站',
      },
      {
        Protocol: 'TCP',
        Port: 80,
        Source: '0.0.0.0/0',
        Description: 'HTTP 入站（重定向到 HTTPS）',
      },
      {
        Protocol: 'TCP',
        Port: 22,
        Source: '10.0.1.0/24',
        Description: 'SSH 仅限堡垒机子网',
      },
    ],
    Outbound: [
      {
        Protocol: 'TCP',
        Port: 443,
        Destination: '0.0.0.0/0',
        Description: 'HTTPS 出站（API 调用）',
      },
      {
        Protocol: 'TCP',
        Port: 3306,
        Destination: 'sg-db',
        Description: '访问数据库安全组',
      },
    ],
  },
}
```

### 2.2 安全组最佳实践

| 原则               | 说明                              |
| :----------------- | :-------------------------------- |
| **最小权限**       | 仅开放必要的端口和来源            |
| **安全组引用**     | 安全组之间引用而非 IP 段          |
| **分层设计**       | Web → App → DB 各层独立安全组     |
| **禁止 0.0.0.0/0** | 管理端口（SSH/RDP）不应对公网开放 |
| **默认拒绝**       | 出站规则也应限制                  |

### 2.3 安全组分层架构

```
Internet → [ALB 安全组: 80/443] → [Web 安全组: 仅 ALB] → [App 安全组: 仅 Web] → [DB 安全组: 仅 App]
```

## 3. NAT 网关

### 3.1 NAT 网关作用

私有子网中的实例需要访问公网（如下载补丁、调用外部 API），但不允许公网主动访问这些实例。NAT 网关提供**出站公网访问能力**。

### 3.2 NAT 网关配置

```bash
# AWS 创建 NAT 网关
aws ec2 create-nat-gateway \
  --subnet-id subnet-public-a \
  --allocation-id eipalloc-xxx \
  --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=nat-gw-a}]'

# 更新私有子网路由表
aws ec2 create-route \
  --route-table-id rtb-private-a \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id nat-xxx
```

## 4. 弹性计算服务

### 4.1 实例类型选型

| 类型         | 特点         | 适用场景               | AWS 类型 | 阿里云类型 |
| :----------- | :----------- | :--------------------- | :------- | :--------- |
| **通用型**   | CPU/内存均衡 | Web 服务器、中小数据库 | M6i      | g7         |
| **计算优化** | 高 CPU       | 批处理、科学计算       | C6i      | c7         |
| **内存优化** | 大内存       | 数据库、缓存           | R6i      | r7         |
| **存储优化** | 高 I/O       | 数据仓库、日志处理     | I4i      | i3         |
| **GPU 型**   | GPU 加速     | AI 训练、渲染          | P5       | gn7        |

### 4.2 实例生命周期

```
启动中 → 运行中 → 停止 → 停止中 → 运行中
  ↓                    ↓
  └──→ 终止（数据丢失）──┘
```

| 状态           | 计费   | 说明               |
| :------------- | :----- | :----------------- |
| **pending**    | 计费   | 正在启动           |
| **running**    | 计费   | 正在运行           |
| **stopping**   | 计费   | 正在停止           |
| **stopped**    | 不计费 | 已停止（EBS 保留） |
| **terminated** | 不计费 | 已终止（不可恢复） |

### 4.3 User Data 启动脚本

```bash
#!/bin/bash
# EC2 User Data - 实例启动时自动执行

# 更新系统
yum update -y

# 安装 Docker
amazon-linux-extras install docker -y
systemctl start docker
systemctl enable docker
usermod -aG docker ec2-user

# 拉取并运行应用
docker pull myapp:latest
docker run -d -p 8080:8080 \
  -e DB_HOST=${DB_HOST} \
  -e DB_PASSWORD=${DB_PASSWORD} \
  --restart=always \
  myapp:latest

# 注册到负载均衡
aws elbv2 register-targets \
  --target-group-arn arn:aws:elasticloadbalancing:... \
  --targets Id=$(ec2-metadata --instance-id | cut -d' ' -f2)
```

## 5. 镜像管理

### 5.1 镜像类型

| 类型           | 说明                     | 适用         |
| :------------- | :----------------------- | :----------- |
| **公共镜像**   | 云商提供的官方镜像       | 标准化部署   |
| **自定义镜像** | 基于实例创建的私有镜像   | 快速复制环境 |
| **共享镜像**   | 其他账号共享的镜像       | 跨账号协作   |
| **市场镜像**   | 第三方发布的预装软件镜像 | 快速搭建     |

### 5.2 镜像构建最佳实践

```dockerfile
# 构建应用镜像
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 多阶段构建 - 减小镜像体积
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app .

EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
```

### 5.3 镜像生命周期

```bash
# 创建自定义镜像
aws ec2 create-image \
  --instance-id i-xxx \
  --name "myapp-v2.3.1" \
  --description "Application image v2.3.1" \
  --no-reboot

# 跨区域复制镜像
aws ec2 copy-image \
  --source-region us-east-1 \
  --source-image-id ami-xxx \
  --region us-west-2 \
  --name "myapp-v2.3.1-west"

# 共享镜像给其他账号
aws ec2 modify-image-attribute \
  --image-id ami-xxx \
  --launch-permission "Add=[{UserId=123456789012}]"
```

## 6. 块存储服务

### 6.1 存储类型

| 类型           | IOPS   | 吞吐量    | 适用场景         | AWS 类型 |
| :------------- | :----- | :-------- | :--------------- | :------- |
| **标准 HDD**   | ~500   | ~90 MB/s  | 冷数据、日志     | st1      |
| **通用 SSD**   | 16,000 | 250 MB/s  | 系统盘、通用应用 | gp3      |
| **高性能 SSD** | 64,000 | 1000 MB/s | 数据库、高 I/O   | io2      |

### 6.2 EBS 卷操作

```bash
# 创建 EBS 卷
aws ec2 create-volume \
  --availability-zone us-east-1a \
  --size 100 \
  --volume-type gp3 \
  --iops 3000 \
  --throughput 125

# 附加到实例
aws ec2 attach-volume \
  --volume-id vol-xxx \
  --instance-id i-xxx \
  --device /dev/sdf

# 创建快照
aws ec2 create-snapshot \
  --volume-id vol-xxx \
  --description "Daily backup"

# 从快照恢复
aws ec2 create-volume \
  --snapshot-id snap-xxx \
  --availability-zone us-east-1a
```

### 6.3 快照策略

```bash
# 创建快照生命周期策略
aws dlm create-lifecycle-policy \
  --execution-role-arn arn:aws:iam::xxx:role/DLMRole \
  --description "Daily EBS backup" \
  --state ENABLED \
  --policy-details '{
    "PolicyType": "EBS_SNAPSHOT_MANAGEMENT",
    "ResourceTypes": ["VOLUME"],
    "TargetTags": [{"Key": "Backup", "Value": "daily"}],
    "Schedules": [{
      "Name": "DailyBackup",
      "CreateRule": {"Interval": 24, "IntervalUnit": "HOURS", "Times": ["03:00"]},
      "RetainRule": {"Count": 7},
      "CopyTags": true
    }]
  }'
```

## 7. 对象存储服务

### 7.1 对象存储概述

| 特性          | 说明                     |
| :------------ | :----------------------- |
| **无限容量**  | 存储空间无上限           |
| **高可用**    | 99.999999999% 数据持久性 |
| **HTTP 访问** | 通过 RESTful API 读写    |
| **分层存储**  | 标准/低频/归档/冷归档    |

### 7.2 存储类型对比

| 存储类型   | 访问频率 | 存储成本 | 访问成本 | 最短存储时间 |
| :--------- | :------- | :------- | :------- | :----------- |
| **标准**   | 频繁     | 高       | 低       | 无           |
| **低频**   | 不频繁   | 中       | 中       | 30 天        |
| **归档**   | 极少     | 低       | 高       | 60 天        |
| **冷归档** | 极少     | 最低     | 最高     | 90 天        |

### 7.3 S3 基本操作

```python
import boto3

s3 = boto3.client('s3')

# 创建存储桶
s3.create_bucket(
    Bucket='my-app-bucket',
    CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
)

# 上传文件
s3.upload_file(
    'local_file.pdf',
    'my-app-bucket',
    'documents/report.pdf',
    ExtraArgs={
        'ContentType': 'application/pdf',
        'Metadata': {'author': 'fanquanpp'}
    }
)

# 下载文件
s3.download_file('my-app-bucket', 'documents/report.pdf', '/tmp/report.pdf')

# 列出对象
response = s3.list_objects_v2(Bucket='my-app-bucket', Prefix='documents/')
for obj in response.get('Contents', []):
    print(f"{obj['Key']} - {obj['Size']} bytes - {obj['LastModified']}")

# 生成预签名 URL（临时访问）
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'my-app-bucket', 'Key': 'documents/report.pdf'},
    ExpiresIn=3600  # 1小时有效
)
```

### 7.4 生命周期管理

```json5
// S3 生命周期规则
{
  Rules: [
    {
      ID: 'ArchiveOldLogs',
      Status: 'Enabled',
      Filter: { Prefix: 'logs/' },
      Transitions: [
        {
          Days: 30,
          StorageClass: 'STANDARD_IA', // 30天后转低频
        },
        {
          Days: 90,
          StorageClass: 'GLACIER', // 90天后转归档
        },
      ],
      Expiration: {
        Days: 365, // 365天后删除
      },
    },
  ],
}
```

## 8. CDN 加速

### 8.1 CDN 工作原理

```
用户请求 → 边缘节点（命中缓存）→ 返回内容
              ↓（未命中）
           回源到源站 → 缓存到边缘 → 返回内容
```

### 8.2 CDN 配置

```bash
# 阿里云 CDN 配置
aliyun cdn AddCdnDomain \
  --DomainName cdn.example.com \
  --CdnType web \
  --Sources '[{"Content":"oss.example.com","Type":"oss","Priority":20}]'

# 缓存规则
# .html  → 缓存 10 分钟
# .jpg/.png → 缓存 30 天
# .css/.js  → 缓存 7 天
# /api/*    → 不缓存
```

### 8.3 CDN 缓存策略

| 资源类型      | 缓存时间 | 说明             |
| :------------ | :------- | :--------------- |
| **静态资源**  | 30 天    | 图片、CSS、JS    |
| **HTML 页面** | 10 分钟  | 页面更新频率较高 |
| **API 响应**  | 不缓存   | 动态数据         |
| **视频文件**  | 90 天    | 大文件长期缓存   |

### 8.4 CDN 性能优化

| 优化项         | 方法                           |
| :------------- | :----------------------------- |
| **缓存命中率** | 合理设置缓存规则和过期时间     |
| **回源优化**   | 回源跟随 301/302、回源超时配置 |
| **压缩**       | Gzip/Brotli 压缩传输           |
| **HTTPS**      | 全链路 HTTPS 加密              |
| **智能路由**   | 就近接入、智能 DNS 解析        |

<!-- ============ 文档分隔线：034-cloud-computing/003-ContainerOrchestration.md ============ -->

## 1. Docker 容器技术

### 1.1 Docker 核心概念

| 概念           | 说明                             |
| :------------- | :------------------------------- |
| **镜像**       | 只读模板，包含运行应用所需的一切 |
| **容器**       | 镜像的运行实例，隔离的进程       |
| **Dockerfile** | 构建镜像的指令文件               |
| **Registry**   | 镜像仓库，存储和分发镜像         |
| **Volume**     | 数据卷，持久化容器数据           |
| **Network**    | 容器网络，容器间通信             |

### 1.2 Dockerfile 编写

```dockerfile
# 多阶段构建 - Node.js 应用
# 阶段1: 构建
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# 阶段2: 运行
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# 非 root 用户
RUN addgroup -g 1001 appgroup && adduser -u 1001 -G appgroup -s /bin/sh -D appuser
USER appuser

EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

CMD ["node", "dist/main.js"]
```

### 1.3 Dockerfile 最佳实践

| 实践              | 说明               |
| :---------------- | :----------------- |
| **多阶段构建**    | 减小最终镜像体积   |
| **使用 Alpine**   | 基础镜像选择精简版 |
| **合并 RUN 指令** | 减少镜像层数       |
| **.dockerignore** | 排除不需要的文件   |
| **非 root 运行**  | 安全性考虑         |
| **固定版本标签**  | 避免使用 latest    |

```dockerfile
# 合并 RUN 指令减少层数
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*
```

### 1.4 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - '3000:3000'
    environment:
      - NODE_ENV=production
      - DB_HOST=postgres
      - REDIS_HOST=redis
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    restart: unless-stopped
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: app
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U app -d myapp']
      interval: 10s
      timeout: 5s
      retries: 5
    secrets:
      - db_password

  redis:
    image: redis:7-alpine
    command: redis-server --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes:
      - redisdata:/data

  nginx:
    image: nginx:alpine
    ports:
      - '80:80'
      - '443:443'
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app

volumes:
  pgdata:
  redisdata:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

### 1.5 常用 Docker 命令

```bash
# 镜像操作
docker build -t myapp:v1 .              # 构建镜像
docker images                            # 列出镜像
docker push registry/myapp:v1           # 推送镜像
docker rmi myapp:v1                     # 删除镜像

# 容器操作
docker run -d -p 3000:3000 --name app myapp:v1  # 运行容器
docker ps                                # 运行中的容器
docker logs -f app                       # 查看日志
docker exec -it app sh                   # 进入容器
docker stop app && docker rm app         # 停止并删除

# Compose 操作
docker compose up -d                     # 启动所有服务
docker compose down -v                   # 停止并删除（含数据卷）
docker compose logs -f app               # 跟踪日志
docker compose ps                        # 服务状态
```

## 2. Kubernetes 编排

### 2.1 K8s 核心概念

```mermaid
flowchart TD
    subgraph Cluster[Kubernetes Cluster]
        CP[Control Plane<br/>API Server / etcd / Scheduler / Controller Mgr]
        subgraph N1[Node 1]
            P1[Pod A] P2[Pod B]
            K1[kubelet kube-proxy]
        end
        subgraph N2[Node 2]
            P3[Pod C] P4[Pod D]
            K2[kubelet kube-proxy]
        end
        subgraph N3[Node 3]
            P5[Pod E] P6[Pod F]
            K3[kubelet kube-proxy]
        end
        CP --- N1
        CP --- N2
        CP --- N3
    end
```

### 2.2 Pod

```yaml
# pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    tier: frontend
spec:
  containers:
    - name: app
      image: registry/myapp:v1
      ports:
        - containerPort: 3000
      resources:
        requests:
          memory: '256Mi'
          cpu: '250m'
        limits:
          memory: '512Mi'
          cpu: '500m'
      env:
        - name: NODE_ENV
          value: 'production'
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
      livenessProbe:
        httpGet:
          path: /health
          port: 3000
        initialDelaySeconds: 15
        periodSeconds: 20
      readinessProbe:
        httpGet:
          path: /ready
          port: 3000
        initialDelaySeconds: 5
        periodSeconds: 10
    - name: log-sidecar
      image: fluent/fluentd:latest
      volumeMounts:
        - name: log-volume
          mountPath: /var/log/app
  volumes:
    - name: log-volume
      emptyDir: {}
```

### 2.3 Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1 # 滚动更新时最多多出1个Pod
      maxUnavailable: 0 # 滚动更新时不允许不可用
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: app
          image: registry/myapp:v2
          ports:
            - containerPort: 3000
          resources:
            requests:
              memory: '256Mi'
              cpu: '250m'
            limits:
              memory: '512Mi'
              cpu: '500m'
```

### 2.4 Service

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  selector:
    app: myapp
  ports:
    - protocol: TCP
      port: 80 # Service 端口
      targetPort: 3000 # Pod 端口
  type: ClusterIP # 集群内部访问
```

| Service 类型     | 说明                        | 适用场景     |
| :--------------- | :-------------------------- | :----------- |
| **ClusterIP**    | 集群内部 IP（默认）         | 内部服务通信 |
| **NodePort**     | 节点端口映射（30000-32767） | 开发测试     |
| **LoadBalancer** | 云商负载均衡器              | 生产对外服务 |
| **ExternalName** | CNAME 映射到外部域名        | 外部服务引用 |

### 2.5 Ingress

```yaml
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: 'true'
    nginx.ingress.kubernetes.io/rate-limit: '100'
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - api.example.com
      secretName: tls-secret
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /v1
            pathType: Prefix
            backend:
              service:
                name: myapp-v1-service
                port:
                  number: 80
          - path: /v2
            pathType: Prefix
            backend:
              service:
                name: myapp-v2-service
                port:
                  number: 80
```

### 2.6 ConfigMap 与 Secret

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  NODE_ENV: 'production'
  LOG_LEVEL: 'info'
  MAX_CONNECTIONS: '100'
  app.json: |
    {
      "theme": "dark",
      "language": "zh-CN"
    }

---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4= # base64("admin")
  password: cGFzc3dvcmQxMjM= # base64("password123")
stringData:
  connection-string: 'postgresql://admin:password123@db:5432/myapp'
```

### 2.7 HPA 自动伸缩

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Percent
          value: 100
          periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
```

### 2.8 常用 kubectl 命令

```bash
# 资源查看
kubectl get pods -A                          # 所有命名空间的 Pod
kubectl get deploy,svc,ing -n production     # 查看多种资源
kubectl describe pod myapp-pod               # Pod 详情
kubectl logs -f deployment/myapp -c app      # 跟踪日志

# 资源操作
kubectl apply -f deployment.yaml             # 应用配置
kubectl delete -f deployment.yaml            # 删除资源
kubectl scale deployment myapp --replicas=5  # 手动扩缩容

# 调试
kubectl exec -it myapp-pod -- sh             # 进入容器
kubectl port-forward svc/myapp 8080:80       # 端口转发
kubectl top pods                             # 资源使用

# 滚动更新
kubectl set image deployment/myapp app=registry/myapp:v3
kubectl rollout status deployment/myapp
kubectl rollout undo deployment/myapp        # 回滚
```

## 3. Helm 包管理

### 3.1 Helm Chart 结构

```mermaid
flowchart TD
    T0["myapp-chart/"]
    T1["Chart.yaml          # Chart 元数据"]
    T2["values.yaml         # 默认配置值"]
    T3["templates/"]
    T4["deployment.yaml"]
    T5["service.yaml"]
    T6["ingress.yaml"]
    T7["configmap.yaml"]
    T8["hpa.yaml"]
    T9["_helpers.tpl    # 模板辅助函数"]
    T10["NOTES.txt       # 安装后说明"]
    T11["charts/             # 依赖 Chart"]
    T12[".helmignore"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T10 --> T11
    T10 --> T12
```

### 3.2 Chart.yaml

```yaml
apiVersion: v2
name: myapp
description: My Application Helm Chart
type: application
version: 1.2.3 # Chart 版本
appVersion: '2.3.1' # 应用版本
dependencies:
  - name: postgresql
    version: '14.x.x'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: postgresql.enabled
  - name: redis
    version: '18.x.x'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: redis.enabled
```

### 3.3 values.yaml

```yaml
# 镜像配置
image:
  repository: registry/myapp
  tag: '2.3.1'
  pullPolicy: IfNotPresent

# 副本数
replicaCount: 3

# 资源限制
resources:
  requests:
    cpu: 250m
    memory: 256Mi
  limits:
    cpu: 500m
    memory: 512Mi

# Service 配置
service:
  type: ClusterIP
  port: 80

# Ingress 配置
ingress:
  enabled: true
  className: nginx
  hosts:
    - host: api.example.com
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: tls-secret
      hosts:
        - api.example.com

# 自动伸缩
autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70

# 依赖开关
postgresql:
  enabled: true
redis:
  enabled: true
```

### 3.4 Helm 常用命令

```bash
# 添加仓库
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

# 安装/升级
helm install myapp ./myapp-chart -n production
helm upgrade myapp ./myapp-chart -n production
helm upgrade --install myapp ./myapp-chart -n production -f values-prod.yaml

# 查看
helm list -n production
helm status myapp -n production
helm history myapp -n production

# 回滚
helm rollback myapp 1 -n production

# 卸载
helm uninstall myapp -n production
```

## 4. 容器镜像仓库

### 4.1 仓库类型

| 类型         | 产品             | 特点       |
| :----------- | :--------------- | :--------- |
| **公有仓库** | Docker Hub、GHCR | 免费、公开 |
| **云商仓库** | ECR、ACR、Harbor | 集成、安全 |
| **私有仓库** | Harbor、Nexus    | 完全自控   |

### 4.2 Harbor 私有仓库

```bash
# Docker 登录私有仓库
docker login harbor.example.com

# 镜像标签与推送
docker tag myapp:v1 harbor.example.com/project/myapp:v1
docker push harbor.example.com/project/myapp:v1

# 拉取镜像
docker pull harbor.example.com/project/myapp:v1

# K8s 使用私有仓库
kubectl create secret docker-registry harbor-secret \
  --docker-server=harbor.example.com \
  --docker-username=admin \
  --docker-password=Harbor12345 \
  -n production
```

### 4.3 镜像安全扫描

```bash
# Trivy 扫描
trivy image harbor.example.com/project/myapp:v1

# 扫描严重漏洞
trivy image --severity HIGH,CRITICAL harbor.example.com/project/myapp:v1

# CI 中集成扫描
trivy image --exit-code 1 --severity HIGH,CRITICAL myapp:v1
```

### 4.4 镜像标签策略

| 标签         | 说明                       | 示例            |
| :----------- | :------------------------- | :-------------- |
| **Git SHA**  | 精确对应代码版本           | `sha-abc1234`   |
| **语义版本** | 正式发布版本               | `v2.3.1`        |
| **分支名**   | 开发分支构建               | `main-20260614` |
| **latest**   | 最新构建（不推荐生产使用） | `latest`        |

<!-- ============ 文档分隔线：034-cloud-computing/004-IaC.md ============ -->

## 1. Terraform 基础设施即代码

### 1.1 Terraform 核心概念

| 概念         | 说明                               |
| :----------- | :--------------------------------- |
| **Provider** | 云服务商插件（AWS/Azure/阿里云等） |
| **Resource** | 基础设施资源定义（VM/VPC/DB等）    |
| **State**    | 资源状态文件，记录已创建的资源     |
| **Module**   | 可复用的 Terraform 配置包          |
| **Plan**     | 预览变更（干运行）                 |
| **Apply**    | 执行变更                           |

### 1.2 项目结构

```mermaid
flowchart TD
    T0["terraform/"]
    T1["main.tf             # 主配置"]
    T2["variables.tf        # 变量定义"]
    T3["outputs.tf          # 输出值"]
    T4["providers.tf        # Provider 配置"]
    T5["backend.tf          # State 后端配置"]
    T6["versions.tf         # 版本约束"]
    T7["terraform.tfvars    # 变量值"]
    T8["environments/"]
    T9["dev.tfvars"]
    T10["staging.tfvars"]
    T11["prod.tfvars"]
    T12["modules/"]
    T13["vpc/"]
    T14["main.tf"]
    T15["variables.tf"]
    T16["outputs.tf"]
    T17["ec2/"]
    T18["rds/"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T0 --> T6
    T0 --> T7
    T0 --> T8
    T11 --> T12
    T12 --> T13
    T12 --> T14
    T12 --> T15
    T12 --> T16
    T16 --> T17
    T16 --> T18
```

### 1.3 Provider 配置

```hcl
# providers.tf
terraform {
  required_version = ">= 1.6"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  # 远程 State 存储
  backend "s3" {
    bucket         = "terraform-state-prod"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "terraform"
      Project     = "myapp"
    }
  }
}
```

### 1.4 VPC 模块

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.name}-vpc"
  }
}

# 公有子网
resource "aws_subnet" "public" {
  count                   = length(var.public_subnet_cidrs)
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidrs[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.name}-public-${count.index + 1}"
    Tier = "public"
  }
}

# 私有子网
resource "aws_subnet" "private" {
  count             = length(var.private_subnet_cidrs)
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = {
    Name = "${var.name}-private-${count.index + 1}"
    Tier = "private"
  }
}

# 互联网网关
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.name}-igw"
  }
}

# NAT 网关（每个 AZ 一个）
resource "aws_nat_gateway" "main" {
  count         = length(var.public_subnet_cidrs)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = {
    Name = "${var.name}-nat-${count.index + 1}"
  }
}

resource "aws_eip" "nat" {
  count  = length(var.public_subnet_cidrs)
  domain = "vpc"
}

# 公有路由表
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "${var.name}-public-rt"
  }
}

# 私有路由表
resource "aws_route_table" "private" {
  count  = length(var.private_subnet_cidrs)
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }

  tags = {
    Name = "${var.name}-private-rt-${count.index + 1}"
  }
}
```

```hcl
# modules/vpc/variables.tf
variable "name" {
  description = "VPC 名称前缀"
  type        = string
}

variable "vpc_cidr" {
  description = "VPC CIDR 地址块"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "公有子网 CIDR 列表"
  type        = list(string)
}

variable "private_subnet_cidrs" {
  description = "私有子网 CIDR 列表"
  type        = list(string)
}

variable "availability_zones" {
  description = "可用区列表"
  type        = list(string)
}
```

### 1.5 主配置

```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"

  name                 = "${var.project}-${var.environment}"
  vpc_cidr             = var.vpc_cidr
  public_subnet_cidrs  = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones   = var.availability_zones
}

# EC2 实例
resource "aws_instance" "app" {
  count         = var.app_instance_count
  ami           = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  subnet_id     = module.vpc.private_subnet_ids[count.index % length(module.vpc.private_subnet_ids)]

  vpc_security_group_ids = [aws_security_group.app.id]

  user_data = templatefile("${path.module}/user_data.sh.tpl", {
    environment = var.environment
    db_host     = aws_db_instance.main.address
  })

  tags = {
    Name = "${var.project}-${var.environment}-app-${count.index + 1}"
  }
}

# RDS 数据库
resource "aws_db_instance" "main" {
  identifier     = "${var.project}-${var.environment}-db"
  engine         = "postgresql"
  engine_version = "16.1"
  instance_class = var.db_instance_class

  allocated_storage     = 100
  max_allocated_storage = 500
  storage_encrypted     = true

  db_name  = "myapp"
  username = "dbadmin"
  password = var.db_password

  vpc_security_group_ids = [aws_security_group.db.id]
  db_subnet_group_name   = aws_db_subnet_group.main.name

  backup_retention_period = 7
  backup_window           = "03:00-04:00"
  maintenance_window      = "Mon:04:00-Mon:05:00"

  skip_final_snapshot = false
  final_snapshot_identifier = "${var.project}-${var.environment}-final"
}

# 数据源 - 获取最新 Ubuntu AMI
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}
```

### 1.6 变量与输出

```hcl
# variables.tf
variable "project" {
  description = "项目名称"
  type        = string
  default     = "myapp"
}

variable "environment" {
  description = "环境名称"
  type        = string
}

variable "aws_region" {
  description = "AWS 区域"
  type        = string
  default     = "us-east-1"
}

variable "db_password" {
  description = "数据库密码"
  type        = string
  sensitive   = true
}

# outputs.tf
output "vpc_id" {
  description = "VPC ID"
  value       = module.vpc.vpc_id
}

output "app_instance_ids" {
  description = "应用实例 ID 列表"
  value       = aws_instance.app[*].id
}

output "db_endpoint" {
  description = "数据库连接端点"
  value       = aws_db_instance.main.endpoint
}
```

### 1.7 Terraform 工作流

```bash
# 初始化（下载 Provider 和模块）
terraform init

# 格式化代码
terraform fmt

# 验证语法
terraform validate

# 预览变更
terraform plan -var-file="environments/prod.tfvars" -out=tfplan

# 执行变更
terraform apply tfplan

# 查看状态
terraform state list
terraform state show aws_instance.app[0]

# 销毁所有资源
terraform destroy -var-file="environments/prod.tfvars"
```

## 2. Ansible 配置管理

### 2.1 Ansible 核心概念

| 概念          | 说明                             |
| :------------ | :------------------------------- |
| **Inventory** | 主机清单，定义管理的主机         |
| **Playbook**  | YAML 格式的任务编排文件          |
| **Role**      | 可复用的任务集合                 |
| **Module**    | 执行具体操作的模块               |
| **Handler**   | 被通知后执行的任务（如重启服务） |

### 2.2 Inventory 配置

```ini
# inventory/production.ini
[webservers]
web1 ansible_host=10.0.1.10
web2 ansible_host=10.0.1.11

[appservers]
app1 ansible_host=10.0.10.10
app2 ansible_host=10.0.10.11

[dbservers]
db1 ansible_host=10.0.20.10

[production:children]
webservers
appservers
dbservers

[production:vars]
ansible_user=ec2-user
ansible_ssh_private_key_file=~/.ssh/prod_key
ansible_python_interpreter=/usr/bin/python3
```

### 2.3 Playbook 编写

```yaml
# playbooks/deploy-app.yml
---
- name: 部署 Web 应用
  hosts: appservers
  become: true

  vars:
    app_version: '2.3.1'
    app_port: 3000
    app_dir: /opt/myapp

  tasks:
    - name: 安装依赖
      ansible.builtin.apt:
        name:
          - curl
          - python3-pip
        state: present
        update_cache: true

    - name: 创建应用目录
      ansible.builtin.file:
        path: '{{ app_dir }}'
        state: directory
        mode: '0755'

    - name: 下载应用包
      ansible.builtin.get_url:
        url: 'https://releases.example.com/myapp/{{ app_version }}/myapp-linux-amd64'
        dest: '{{ app_dir }}/myapp'
        mode: '0755'
      notify: restart myapp

    - name: 部署配置文件
      ansible.builtin.template:
        src: templates/app.conf.j2
        dest: '{{ app_dir }}/app.conf'
        mode: '0644'
      notify: restart myapp

    - name: 部署 systemd 服务
      ansible.builtin.template:
        src: templates/myapp.service.j2
        dest: /etc/systemd/system/myapp.service
        mode: '0644'
      notify: restart myapp

    - name: 确保 myapp 服务运行
      ansible.builtin.systemd:
        name: myapp
        state: started
        enabled: true
        daemon_reload: true

    - name: 等待应用就绪
      ansible.builtin.wait_for:
        port: '{{ app_port }}'
        delay: 5
        timeout: 60

  handlers:
    - name: restart myapp
      ansible.builtin.systemd:
        name: myapp
        state: restarted
```

### 2.4 Role 结构

```mermaid
flowchart TD
    T0["roles/"]
    T1["nginx/"]
    T2["tasks/"]
    T3["main.yml          # 主任务"]
    T4["handlers/"]
    T5["main.yml          # 处理器"]
    T6["templates/"]
    T7["nginx.conf.j2     # 模板文件"]
    T8["files/"]
    T9["nginx.repo        # 静态文件"]
    T10["vars/"]
    T11["main.yml          # 角色变量"]
    T12["defaults/"]
    T13["main.yml          # 默认变量"]
    T14["meta/"]
    T15["main.yml          # 角色依赖"]
    T0 --> T1
    T1 --> T2
    T1 --> T3
    T3 --> T4
    T1 --> T5
    T5 --> T6
    T1 --> T7
    T7 --> T8
    T1 --> T9
    T9 --> T10
    T1 --> T11
    T11 --> T12
    T1 --> T13
    T13 --> T14
    T14 --> T15
```

### 2.5 模板文件

```jinja2
# roles/nginx/templates/nginx.conf.j2
worker_processes {{ ansible_processor_vcpus }};
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections {{ nginx_worker_connections | default(1024) }};
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    upstream app_backend {
        {% for host in groups['appservers'] %}
        server {{ hostvars[host]['ansible_host'] }}:{{ app_port }};
        {% endfor %}
    }

    server {
        listen 80;
        server_name {{ nginx_server_name }};

        location / {
            proxy_pass http://app_backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
```

## 3. Pulumi

### 3.1 Pulumi 概述

Pulumi 是使用**通用编程语言**（Python/TypeScript/Go）编写基础设施即代码的工具：

| 特性         | Terraform       | Pulumi          |
| :----------- | :-------------- | :-------------- |
| **语言**     | HCL（专用语言） | Python/TS/Go/C# |
| **状态管理** | 自管理/SaaS     | Pulumi Cloud    |
| **测试**     | 有限            | 原生单元测试    |
| **逻辑**     | 声明式          | 命令式+声明式   |
| **生态**     | 最丰富          | 增长中          |

### 3.2 Pulumi 示例（Python）

```python
# __main__.py
import pulumi
import pulumi_aws as aws

# 配置
config = pulumi.Config()
environment = config.get("environment") or "dev"

# 创建 VPC
vpc = aws.ec2.Vpc("main-vpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    tags={"Name": f"myapp-{environment}-vpc"},
)

# 创建子网
public_subnet = aws.ec2.Subnet("public-subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    availability_zone="us-east-1a",
    map_public_ip_on_launch=True,
    tags={"Name": f"myapp-{environment}-public"},
)

# 创建安全组
sg = aws.ec2.SecurityGroup("app-sg",
    vpc_id=vpc.id,
    description="Application security group",
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=443,
            to_port=443,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            protocol="-1",
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
)

# 输出
pulumi.export("vpc_id", vpc.id)
pulumi.export("subnet_id", public_subnet.id)
pulumi.export("security_group_id", sg.id)
```

## 4. GitOps

### 4.1 GitOps 原则

| 原则               | 说明                         |
| :----------------- | :--------------------------- |
| **声明式描述**     | 系统状态用声明式方式描述     |
| **Git 为唯一信源** | 所有变更通过 Git 提交        |
| **自动拉取**       | Agent 自动拉取并应用期望状态 |
| **持续协调**       | 持续比对实际状态与期望状态   |

### 4.2 ArgoCD 配置

```yaml
# argocd-app.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/k8s-manifests.git
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - ServerSideApply=true
    retry:
      limit: 3
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### 4.3 Flux 配置

```yaml
# gotk-sync.yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/org/k8s-manifests.git
  ref:
    branch: main
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: myapp
  namespace: flux-system
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: myapp
  path: './overlays/production'
  prune: true
  healthChecks:
    - apiVersion: apps/v1
      kind: Deployment
      name: myapp
      namespace: production
```

## 5. Python 自动化运维脚本

### 5.1 批量实例管理

```python
import boto3
import concurrent.futures

ec2 = boto3.resource('ec2')

def get_instances_by_tag(tag_key: str, tag_value: str):
    """根据标签获取实例列表"""
    return list(ec2.instances.filter(Filters=[
        {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]))

def execute_ssm_command(instance_ids: list, command: str):
    """通过 SSM 执行命令"""
    ssm = boto3.client('ssm')
    response = ssm.send_command(
        InstanceIds=instance_ids,
        DocumentName='AWS-RunShellScript',
        Parameters={'commands': [command]},
        TimeoutSeconds=300,
    )
    return response['Command']['CommandId']

def rolling_restart(tag_key: str, tag_value: str, batch_size: int = 1):
    """滚动重启实例"""
    instances = get_instances_by_tag(tag_key, tag_value)
    print(f"找到 {len(instances)} 个实例")

    for i in range(0, len(instances), batch_size):
        batch = instances[i:i + batch_size]
        ids = [inst.id for inst in batch]

        # 停止实例
        print(f"停止实例: {ids}")
        for inst in batch:
            inst.stop()
        for inst in batch:
            inst.wait_until_stopped()

        # 启动实例
        print(f"启动实例: {ids}")
        for inst in batch:
            inst.start()
        for inst in batch:
            inst.wait_until_running()

        # 健康检查
        print(f"等待实例就绪: {ids}")
        execute_ssm_command(ids, 'curl -sf http://localhost:3000/health || exit 1')
        print(f"批次 {i // batch_size + 1} 完成")
```

### 5.2 资源清理脚本

```python
import boto3
from datetime import datetime, timedelta

def cleanup_unused_resources(dry_run: bool = True):
    """清理未使用的云资源"""
    ec2 = boto3.resource('ec2')
    findings = []

    # 未附加的 EBS 卷
    for vol in ec2.volumes.filter(Filters=[
        {'Name': 'status', 'Values': ['available']}
    ]):
        findings.append({
            'type': 'EBS Volume',
            'id': vol.id,
            'size': f"{vol.size}GB",
            'age': str(datetime.now() - vol.create_time.replace(tzinfo=None)),
        })
        if not dry_run:
            vol.delete()

    # 未使用的弹性 IP
    for eip in ec2.vpc_addresses.all():
        if eip.instance_id is None:
            findings.append({
                'type': 'Elastic IP',
                'id': eip.allocation_id,
                'ip': eip.public_ip,
            })
            if not dry_run:
                eip.release()

    # 过期的快照（>30天）
    cutoff = datetime.now() - timedelta(days=30)
    for snap in ec2.snapshots.filter(OwnerIds=['self']):
        if snap.start_time.replace(tzinfo=None) < cutoff:
            # 检查是否被 AMI 引用
            is_used = any(
                snap.id in [b['Ebs']['SnapshotId'] for b in img.block_device_mappings]
                for img in ec2.images.filter(OwnerIds=['self'])
            )
            if not is_used:
                findings.append({
                    'type': 'Snapshot',
                    'id': snap.id,
                    'age': str(datetime.now() - snap.start_time.replace(tzinfo=None)),
                })
                if not dry_run:
                    snap.delete()

    return findings
```

## 6. 云监控告警

### 6.1 Prometheus 监控

```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

rule_files:
  - 'alerts/*.yml'

scrape_configs:
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

### 6.2 告警规则

```yaml
# alerts/app-alerts.yml
groups:
  - name: app-alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: '高错误率: {{ $labels.instance }}'
          description: '5xx 错误率超过 5%，当前值: {{ $value | humanizePercentage }}'

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: '高延迟: {{ $labels.instance }}'
          description: 'P95 延迟超过 1s，当前值: {{ $value }}s'

      - alert: PodCrashLooping
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: 'Pod 崩溃重启: {{ $labels.namespace }}/{{ $labels.pod }}'
```

### 6.3 Grafana 仪表盘

```json5
// 关键监控面板
{
  dashboard: {
    title: 'Application Overview',
    panels: [
      {
        title: '请求速率 (QPS)',
        type: 'timeseries',
        targets: [{ expr: 'sum(rate(http_requests_total[5m]))' }],
      },
      {
        title: '错误率',
        type: 'gauge',
        targets: [
          {
            expr: 'sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m]))',
          },
        ],
      },
      {
        title: 'P95 延迟',
        type: 'timeseries',
        targets: [
          {
            expr: 'histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket[5m])) by (le))',
          },
        ],
      },
      {
        title: 'CPU 使用率',
        type: 'timeseries',
        targets: [
          {
            expr: 'sum(rate(container_cpu_usage_seconds_total{namespace="production"}[5m])) by (pod)',
          },
        ],
      },
      {
        title: '内存使用',
        type: 'timeseries',
        targets: [
          { expr: 'sum(container_memory_working_set_bytes{namespace="production"}) by (pod)' },
        ],
      },
    ],
  },
}
```

### 6.4 CloudWatch 告警

```bash
# 创建 CPU 告警
aws cloudwatch put-metric-alarm \
  --alarm-name "high-cpu-alert" \
  --alarm-description "CPU 使用率超过 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --dimensions Name=AutoScalingGroupName,Value=myapp-asg \
  --alarm-actions arn:aws:sns:us-east-1:xxx:ops-alerts

# 创建自定义指标告警
aws cloudwatch put-metric-alarm \
  --alarm-name "high-error-rate" \
  --metric-name ErrorRate \
  --namespace MyApp \
  --statistic Average \
  --period 60 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 3 \
  --datapoints-to-alarm 2 \
  --treat-missing-data breaching \
  --alarm-actions arn:aws:sns:us-east-1:xxx:ops-alerts
```

### 6.5 监控体系总览

```
指标采集 → 数据存储 → 可视化 → 告警 → 通知
   │          │          │        │       │
Prometheus   TSDB     Grafana  Alert   Slack/钉钉
CloudWatch   CloudWatch AWS     SNS     Email/SMS
Datadog      Datadog   Datadog  Monitor PagerDuty
```

| 层级         | 工具                      | 关注点             |
| :----------- | :------------------------ | :----------------- |
| **基础设施** | CloudWatch、Node Exporter | CPU/内存/磁盘/网络 |
| **应用层**   | APM、自定义指标           | 延迟/错误率/吞吐量 |
| **业务层**   | 自定义指标、日志分析      | 订单量/转化率      |
| **安全层**   | GuardDuty、WAF 日志       | 异常访问/攻击检测  |

<!-- ============ 文档分隔线：034-cloud-computing/005-IaaSPaaSSaaS.md ============ -->

## 1. 云计算服务模式概述

### 1.1 服务模式层级

```mermaid
flowchart TD
    SaaS[SaaS 应用层] --> PaaS[PaaS 平台层] --> IaaS[IaaS 基础设施层] --> HW[物理硬件/数据中心]
```

### 1.2 责任划分

| 层级     | IaaS   | PaaS   | SaaS   |
| -------- | ------ | ------ | ------ |
| 应用     | 客户   | 客户   | 供应商 |
| 数据     | 客户   | 客户   | 供应商 |
| 运行时   | 客户   | 供应商 | 供应商 |
| 中间件   | 客户   | 供应商 | 供应商 |
| 操作系统 | 客户   | 供应商 | 供应商 |
| 虚拟化   | 供应商 | 供应商 | 供应商 |
| 服务器   | 供应商 | 供应商 | 供应商 |
| 存储     | 供应商 | 供应商 | 供应商 |
| 网络     | 供应商 | 供应商 | 供应商 |

## 2. IaaS（基础设施即服务）

### 2.1 定义

提供虚拟化的计算资源（服务器、存储、网络），用户自行管理操作系统及以上层级。

### 2.2 核心服务

| 服务   | 描述             | 示例             |
| ------ | ---------------- | ---------------- |
| 计算   | 虚拟机/裸金属    | EC2, ECS, VM     |
| 存储   | 块/对象/文件存储 | S3, EBS, OSS     |
| 网络   | VPC/负载均衡     | VPC, ELB, SLB    |
| 数据库 | 自建数据库       | RDS（IaaS 模式） |

### 2.3 适用场景

- 需要完全控制操作系统
- 自定义运行时环境
- 迁移传统应用
- 高性能计算

### 2.4 代表产品

| 供应商 | 产品                           |
| ------ | ------------------------------ |
| AWS    | EC2, S3, VPC                   |
| Azure  | Virtual Machines, Blob Storage |
| GCP    | Compute Engine, Cloud Storage  |
| 阿里云 | ECS, OSS, VPC                  |
| 华为云 | ECS, OBS, VPC                  |

## 3. PaaS（平台即服务）

### 3.1 定义

提供应用运行平台，用户只需关注应用代码和数据，无需管理底层基础设施。

### 3.2 核心服务

| 服务     | 描述         | 示例                  |
| -------- | ------------ | --------------------- |
| 运行时   | 语言运行环境 | Node.js, Python, Java |
| 中间件   | 应用服务器   | Tomcat, Nginx         |
| 数据库   | 托管数据库   | RDS, Cloud SQL        |
| 消息队列 | 托管消息     | SQS, MQ               |
| CI/CD    | 构建部署     | CodePipeline          |

### 3.3 适用场景

- 快速应用开发
- 微服务架构
- API 后端
- DevOps 团队

### 3.4 代表产品

| 供应商 | 产品                           |
| ------ | ------------------------------ |
| AWS    | Elastic Beanstalk, Lambda, RDS |
| Azure  | App Service, Functions         |
| GCP    | App Engine, Cloud Functions    |
| 阿里云 | SAE, FC, RDS                   |
| Heroku | Heroku Platform                |

## 4. SaaS（软件即服务）

### 4.1 定义

直接提供可用的软件应用，用户通过浏览器或 API 使用，无需安装和维护。

### 4.2 核心特征

- 多租户架构
- 按需付费
- 自动更新
- 随时随地访问

### 4.3 适用场景

- 企业协作
- 客户管理
- 办公自动化
- 数据分析

### 4.4 代表产品

| 类别 | 产品                         |
| ---- | ---------------------------- |
| 协作 | Slack, Teams, 飞书           |
| CRM  | Salesforce, HubSpot          |
| 办公 | Google Workspace, Office 365 |
| 设计 | Figma, Canva                 |
| 开发 | GitHub, GitLab               |

## 5. 选型指南

### 5.1 决策矩阵

| 需求     | IaaS | PaaS | SaaS |
| -------- | ---- | ---- | ---- |
| 完全控制 |      |      |      |
| 快速上线 |      |      |      |
| 定制化   |      |      |      |
| 运维成本 | 高   | 中   | 低   |
| 技术门槛 | 高   | 中   | 低   |
| 长期成本 | 中   | 中   | 高   |

### 5.2 混合策略

```
核心业务 → IaaS（完全控制）
应用服务 → PaaS（快速迭代）
通用工具 → SaaS（降低成本）
```

<!-- ============ 文档分隔线：034-cloud-computing/006-VirtualizationTech.md ============ -->

## 1. 虚拟化概述

### 1.1 虚拟化的定义与意义

虚拟化（Virtualization）是一种资源管理技术，通过在物理硬件与操作系统之间引入**虚拟化层（VMM/Hypervisor）**，将一台物理机的计算资源抽象为多个独立的虚拟执行环境。其核心目标是**资源隔离**与**资源复用**。

虚拟化带来的关键价值：

- **资源利用率提升**：从平均 15%-20% 提升至 60%-80%
- **隔离性**：故障域隔离，安全域隔离
- **封装性**：虚拟机以文件形式存在，便于备份、迁移、克隆
- **硬件无关性**：虚拟机可在不同物理主机间迁移

### 1.2 虚拟化分类

| 类型             | 描述                               | 典型场景        |
| ---------------- | ---------------------------------- | --------------- |
| 全虚拟化         | Guest OS 无需修改即可运行          | 通用服务器整合  |
| 半虚拟化         | Guest OS 需要修改以配合 Hypervisor | 高性能 I/O 场景 |
| 硬件辅助虚拟化   | 利用 CPU 硬件特性实现高效虚拟化    | 现代云平台主流  |
| 操作系统级虚拟化 | 共享内核，隔离进程与资源           | 容器技术        |
| 桌面虚拟化       | 远程交付虚拟桌面                   | VDI 场景        |
| 网络虚拟化       | 虚拟交换机、SDN、Overlay           | 云网络          |

## 2. Hypervisor 架构

### 2.1 Type 1 Hypervisor（裸金属）

直接运行在物理硬件之上，不依赖宿主操作系统：

```mermaid
flowchart TD
    subgraph VMs[VM 1 / VM 2 / VM 3<br/>Guest OS]
    end
    H[Type 1 Hypervisor<br/>VMware ESXi / Hyper-V / KVM]
    HW[Physical Hardware]
    VMs --> H --> HW
```

**代表产品**：

- **VMware ESXi**：企业级，功能完善，vSphere 生态
- **Microsoft Hyper-V**：Windows Server 内置，Azure 底层
- **KVM（Kernel-based Virtual Machine）**：Linux 内核模块，开源，OpenStack 默认
- **Xen**：早期开源 Hypervisor，AWS 早期使用

### 2.2 Type 2 Hypervisor（托管型）

运行在宿主操作系统之上：

```mermaid
flowchart TD
    VMs[VM 1 / VM 2<br/>Guest OS] --> H[Type 2 Hypervisor<br/>VMware Workstation / VirtualBox]
    H --> OS[Host Operating System] --> HW[Physical Hardware]
```

**代表产品**：VMware Workstation、Oracle VirtualBox、Parallels Desktop

### 2.3 KVM 架构详解

KVM 是当前云基础设施的事实标准：

```mermaid
flowchart TD
    subgraph User[User Space]
        Q1[QEMU vCPU0]
        Q2[QEMU vCPU1]
        KIO[/dev/kvm ioctl]
    end
    subgraph Kernel[Kernel Space]
        KM[KVM Kernel Module<br/>vCPU Thread / MMU EPT]
    end
    HW[Physical Hardware<br/>Intel VT-x / AMD-V + EPT/RVI]
    Q1 --> KIO
    Q2 --> KIO
    KIO --> KM
    KM --> HW
```

KVM 关键组件：

- **kvm.ko**：内核模块，负责 CPU 虚拟化和内存虚拟化
- **QEMU**：用户态进程，负责 I/O 设备模拟
- **virtio**：半虚拟化 I/O 框架，大幅提升 I/O 性能

## 3. CPU 虚拟化

### 3.1 特权级与陷阱

x86 架构定义了 4 个特权级（Ring 0-3），传统 OS 内核运行在 Ring 0，用户态运行在 Ring 3。虚拟化面临的根本问题是：Guest OS 期望运行在 Ring 0，但实际由 Hypervisor 掌控最高特权。

### 3.2 硬件辅助虚拟化

**Intel VT-x** 引入了两种操作模式：

- **VMX Root Mode**：Hypervisor 运行的模式，拥有完全硬件控制权
- **VMX Non-Root Mode**：Guest 运行的模式，受限操作触发 VM-Exit

关键数据结构：

```mermaid
flowchart TD
    V[VMCS Virtual Machine Control Structure]
    V --> G[Guest-state Area<br/>Guest 寄存器状态]
    V --> H[Host-state Area<br/>Host 寄存器状态]
    V --> E[VM-execution control fields 执行控制]
    V --> X[VM-exit control fields 退出控制]
    V --> N[VM-entry control fields 进入控制]
    V --> I[VM-exit information fields 退出原因信息]
```

**VM-Exit 触发场景**：

| 触发类型 | 示例                      |
| -------- | ------------------------- |
| 指令触发 | `CPUID`、`INVD`、`VMXON`  |
| 异常触发 | 缺页异常（EPT violation） |
| 中断触发 | 外部中断、NMI             |
| I/O 触发 | 访问映射为 I/O 的 GPA     |

### 3.3 vCPU 调度

Hypervisor 将 vCPU 作为宿主系统的线程进行调度：

```
物理 CPU 0:  [vCPU0(VM1)][vCPU2(VM2)][vCPU0(VM1)][vCPU3(VM3)]
物理 CPU 1:  [vCPU1(VM1)][vCPU1(VM1)][vCPU2(VM2)][vCPU0(VM1)]
```

调度策略需考虑：

- **公平性**：各 vCPU 获得合理的 CPU 时间
- **缓存亲和性**：vCPU 尽量调度到同一 pCPU 以利用缓存
- **NUMA 感知**：vCPU 与内存分配在同一 NUMA 节点
- **实时性**：满足 SLA 对延迟的要求

## 4. 内存虚拟化

### 4.1 影子页表（Shadow Page Table）

早期软件方案，Hypervisor 维护 Guest 虚拟地址到宿主物理地址的映射：

```
GVA ──(Guest Page Table)──> GPA ──(Shadow Page Table)──> HPA
```

缺点：页表维护开销大，每次 Guest 修改页表都需 VM-Exit。

### 4.2 扩展页表（EPT / NPT）

硬件辅助方案，两级页表由硬件自动遍历：

```
GVA ──(Guest Page Table)──> GPA ──(EPT)──> HPA
```

EPT 带来的优势：

- Guest 修改自身页表**无需 VM-Exit**
- 硬件自动完成地址翻译，性能接近原生
- 支持**大页（Huge Pages）**映射，减少 TLB Miss

EPT 地址翻译开销：

$$
\text{EPT Walk 次数} = \lceil \log_2(\text{GPA 空间} / \text{页大小}) \rceil \times \text{EPT 层级}
$$

对于 4 级 EPT 和 4KB 页面，一次完整翻译需要 24 次内存访问（4 级 Guest PT + 4 级 EPT），TLB 命中至关重要。

### 4.3 内存超额分配

Hypervisor 通常分配超过物理内存的总量给 VM：

- **气球驱动（Balloon Driver）**：Guest 内核模块，Hypervisor 通过 inflate 回收 Guest 内存
- **透明大页（THP）**：自动合并 4KB 页为 2MB/1GB 大页
- **KSM（Kernel Samepage Merging）**：合并相同内容的内存页
- **交换（Swap）**：将 Guest 内存换出到宿主交换分区

## 5. I/O 虚拟化

### 5.1 设备模拟

QEMU 纯软件模拟硬件设备，Guest 使用标准驱动即可工作：

```
Guest App → Guest Driver → MMIO/PIO → VM-Exit → QEMU Device Model → Host I/O
```

优点：兼容性好；缺点：每次 I/O 都需 VM-Exit，性能差。

### 5.2 半虚拟化（Virtio）

Guest 使用专用 virtio 驱动，通过共享内存环形缓冲区通信：

```mermaid
flowchart LR
    G[virtio-net driver] -->|virtqueue shared mem| H[vhost-net backend]
    H -->|notification| G
```

Virtio 核心数据结构——**vring**：

```mermaid
flowchart TD
    V[vring]
    V --> D[Descriptor Table 描述符表<br/>描述 buffer 地址与长度]
    V --> A[Available Ring 可用环<br/>Guest → Host 方向]
    V --> U[Used Ring 已用环<br/>Host → Guest 方向]
```

Virtio 性能优化演进：

| 版本          | 特性              | 性能提升 |
| ------------- | ----------------- | -------- |
| Virtio Legacy | 基于端口 I/O 通知 | 基线     |
| Virtio 1.0    | 基于 MMIO + PCI   | 约 10%   |
| Vhost-net     | 内核态处理网络包  | 约 50%   |
| Vhost-user    | 用户态 DPDK 后端  | 约 100%  |
| VDPA          | 硬件卸载          | 接近原生 |

### 5.3 SR-IOV 直通

**Single Root I/O Virtualization** 允许一个物理网卡创建多个虚拟功能（VF），每个 VF 可直接分配给 VM：

```mermaid
flowchart TD
    V1[VM 1 VF0] --> PF[PF Physical Function 物理网卡]
    V2[VM 2 VF1] --> PF
    V3[VM 3 VF2] --> PF
```

SR-IOV 绕过 Hypervisor，I/O 路径为：

$$
\text{VM} \xrightarrow{\text{DMA}} \text{VF} \xrightarrow{\text{硬件交换}} \text{PF} \xrightarrow{\text{物理链路}} \text{网络}
$$

延迟接近物理机，但牺牲了 VM 迁移灵活性。

## 6. 容器虚拟化

### 6.1 容器 vs 虚拟机

```mermaid
flowchart TD
    subgraph VM[虚拟机]
        VA[App A<br/>Bins/Libs<br/>Guest OS]
        VB[App B<br/>Bins/Libs<br/>Guest OS]
        VH[Hypervisor]
        VOS[Host OS]
        VHW[Physical Hardware]
    end
    subgraph Container[容器]
        CA[App A<br/>Bins/Libs<br/>Container]
        CB[App B<br/>Bins/Libs<br/>Container]
        CR[Container Runtime]
        COS[Host OS]
        CHW[Physical Hardware]
    end
```

### 6.2 Linux 容器技术基础

容器依赖 Linux 内核三大隔离机制：

**Namespace（命名空间）**：

| Namespace | 隔离内容       | 系统调用          |
| --------- | -------------- | ----------------- |
| PID       | 进程 ID        | `CLONE_NEWPID`    |
| Network   | 网络栈         | `CLONE_NEWNET`    |
| Mount     | 文件系统挂载点 | `CLONE_NEWNS`     |
| UTS       | 主机名与域名   | `CLONE_NEWUTS`    |
| IPC       | System V IPC   | `CLONE_NEWIPC`    |
| User      | 用户与组 ID    | `CLONE_NEWUSER`   |
| Cgroup    | Cgroup 根目录  | `CLONE_NEWCGROUP` |

**Cgroup（控制组）**：资源限制与统计

```
cpu.max        → CPU 时间配额
memory.max     → 内存使用上限
io.max         → I/O 带宽限制
pids.max       → 进程数上限
```

**UnionFS（联合文件系统）**：镜像分层

```mermaid
flowchart TD
    W[可写层 Container Layer<br/>容器运行时修改] --> L3[Layer 3 App Code<br/>应用代码]
    L3 --> L2[Layer 2 Dependencies<br/>依赖库]
    L2 --> L1[Layer 1 Base OS<br/>基础镜像]
```

### 6.3 安全容器

传统容器共享内核，存在逃逸风险。安全容器方案：

- **Kata Containers**：轻量级 VM，每个容器运行在独立 VM 中
- **gVisor**：用户态内核（Sentry），拦截系统调用
- **Firecracker**：AWS 开源，极简 VMM，启动时间 < 125ms

## 7. 虚拟机迁移

### 7.1 冷迁移（Cold Migration）

VM 关机后迁移磁盘镜像和配置到目标主机，再启动。简单可靠但需要停机。

### 7.2 热迁移（Live Migration）

VM 运行中迁移到目标主机，对用户透明。核心流程：

```mermaid
flowchart TD
    T0["1. 预拷贝阶段（Pre-copy）"]
    T1["迭代1：传输全部内存页"]
    T2["迭代2：传输脏页（迭代1期间修改的页）"]
    T3["迭代3：传输脏页（迭代2期间修改的页）"]
    T4["...直到脏页率低于阈值"]
    T5["2. 停机拷贝阶段（Stop-and-copy）"]
    T6["暂停 VM"]
    T7["传输最终脏页"]
    T8["恢复 VM 在目标主机"]
    T9["3. 切换阶段"]
    T10["将网络流量重定向到新位置"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T4 --> T5
    T5 --> T6
    T5 --> T7
    T5 --> T8
    T8 --> T9
    T9 --> T10
```

热迁移关键指标：

$$
\text{总停机时间} = \frac{\text{最终脏页数据量}}{\text{网络带宽}} + \text{VM 状态切换时间}
$$

$$
\text{总迁移时间} = \sum_{i=1}^{n} \frac{\text{第 } i \text{ 轮脏页量}}{\text{网络带宽}} + \text{停机时间}
$$

### 7.3 后拷贝迁移（Post-copy）

先切换 VM 到目标主机，再按需拉取内存页：

```
1. 暂停源 VM
2. 在目标主机启动 VM
3. 按需拉取（On-demand）：VM 访问缺失页时触发缺页中断，从源拉取
4. 主动推送（Active Push）：源后台推送剩余页
```

优点：总迁移时间短；缺点：停机后性能下降，源主机故障会导致 VM 不可用。

## 8. 虚拟化性能调优

### 8.1 CPU 调优

- **vCPU 绑定（CPU Pinning）**：将 vCPU 固定到 pCPU，减少缓存失效
- **NUMA 对齐**：vCPU 与内存分配在同一 NUMA 节点
- **大页配置**：使用 2MB/1GB 大页减少 TLB Miss

### 8.2 内存调优

- **KSM**：适用于同质 VM 集群，异质负载关闭
- **气球驱动**：动态调整 Guest 内存
- **透明大页**：默认开启，数据库等应用建议显式配置

### 8.3 I/O 调优

- **Virtio + Vhost**：网络和块设备使用半虚拟化驱动
- **SR-IOV**：高吞吐低延迟场景使用直通
- **IOThread**：QEMU 将 I/O 处理移至独立线程
- **AIO/IO_uring**：Linux 异步 I/O 后端，io_uring 性能更优

<!-- ============ 文档分隔线：034-cloud-computing/007-CloudArchitectureDesign.md ============ -->

## 1. 云架构设计原则

### 1.1 Well-Architected Framework

AWS Well-Architected Framework 定义了六大支柱：

| 支柱     | 核心关注             | 关键实践                        |
| -------- | -------------------- | ------------------------------- |
| 卓越运营 | 运维自动化、事件响应 | IaC、可观测性、Runbook          |
| 安全性   | 数据保护、身份认证   | 最小权限、加密、审计            |
| 可靠性   | 故障恢复、弹性伸缩   | 多 AZ、自动恢复、混沌工程       |
| 性能效率 | 资源选型、高效利用   | 按需选型、缓存、压缩            |
| 成本优化 | 消除浪费、合理定价   | Reserved Instance、Right-sizing |
| 可持续性 | 资源效率、碳足迹     | Graviton、Spot、弹性调度        |

### 1.2 云原生设计原则

- **不可变基础设施**：服务器不手动修改，通过替换实现变更
- **声明式 API**：描述期望状态，系统自动收敛
- **自服务**：开发团队自助获取资源，无需审批瓶颈
- **松耦合**：服务间通过 API 通信，独立部署与扩展
- **可观测**：指标、日志、链路追踪三位一体

### 1.3 设计权衡

架构设计本质是权衡，常见决策点：

$$
\text{CAP} \Rightarrow \text{一致性 vs 可用性 vs 分区容错}
$$

$$
\text{延迟 vs 一致性} \Rightarrow \text{强一致（同步复制） vs 最终一致（异步复制）}
$$

$$
\text{成本 vs 可靠性} \Rightarrow \text{单区域 vs 多区域}
$$

## 2. 微服务架构

### 2.1 微服务拆分策略

**领域驱动设计（DDD）** 是微服务拆分的核心方法论：

```mermaid
flowchart LR
    subgraph BC[限界上下文 Bounded Context]
        O[订单上下文<br/>Aggregate Order]
        P[支付上下文<br/>Aggregate Payment]
        S[库存上下文<br/>Aggregate Stock]
    end
```

拆分原则：

- **单一职责**：每个服务聚焦一个业务能力
- **独立部署**：服务可独立发布，不影响其他服务
- **数据自治**：每个服务拥有自己的数据存储
- **接口契约**：服务间通过明确定义的 API 交互

### 2.2 服务通信模式

**同步通信**：

| 协议      | 适用场景       | 特点                   |
| --------- | -------------- | ---------------------- |
| REST/HTTP | CRUD 操作      | 简单通用，但开销大     |
| gRPC      | 服务间高频调用 | 高性能，强类型，流式   |
| GraphQL   | 前端聚合查询   | 按需获取，减少过度获取 |

**异步通信**：

| 模式      | 适用场景 | 代表技术      |
| --------- | -------- | ------------- |
| 点对点    | 任务分发 | RabbitMQ、SQS |
| 发布/订阅 | 事件通知 | Kafka、SNS    |
| 事件溯源  | 审计追踪 | EventStoreDB  |

### 2.3 服务网格（Service Mesh）

服务网格将通信逻辑从应用代码中抽离到基础设施层：

```mermaid
flowchart LR
    subgraph Mesh[Service Mesh]
        A[Service A<br/>Sidecar] <--> B[Service B<br/>Sidecar]
        CP[Control Plane<br/>Pilot / Citadel / Galley]
    end
```

核心能力：流量管理、安全通信（mTLS）、可观测性、故障注入。

## 3. 事件驱动架构

### 3.1 事件驱动核心概念

```mermaid
flowchart LR
    Prod[事件生产者] -->|事件| Router[事件路由器] -->|事件| Cons[事件消费者]
    Router --> Store[事件存储<br/>可选，用于事件回放]
```

**事件 vs 命令 vs 查询**：

| 类型 | 意图           | 响应期望      | 示例             |
| ---- | -------------- | ------------- | ---------------- |
| 命令 | 请求执行操作   | 期望成功/失败 | `CreateOrder`    |
| 事件 | 通知已发生事实 | 无期望        | `OrderCreated`   |
| 查询 | 请求信息       | 期望返回数据  | `GetOrderStatus` |

### 3.2 事件溯源（Event Sourcing）

不存储当前状态，而是存储所有状态变更事件：

```
传统方式：  Order { id: 1, status: "shipped", total: 99.9 }

事件溯源：  OrderCreated   { id: 1, items: [...], total: 99.9 }
           OrderPaid      { id: 1, paymentId: "pay_123" }
           OrderShipped   { id: 1, trackingNo: "SF123456" }
```

当前状态通过重放事件获得：

$$
\text{State}_{current} = \text{Apply}(\text{Event}_1, \text{Event}_2, \ldots, \text{Event}_n)
$$

为避免每次全量重放，使用**快照（Snapshot）**：

$$
\text{State}_{current} = \text{Apply}(\text{Snapshot}_k, \text{Event}_{k+1}, \ldots, \text{Event}_n)
$$

### 3.3 CQRS 模式

命令查询职责分离（Command Query Responsibility Segregation）：

```mermaid
flowchart LR
    W[Write Side API] -->|Command| CM[Command Model OLTP] -->|Event| QM[Query Model OLAP]
    R[Read Side API] <-->|Query| QM
```

优势：读写模型独立优化，读侧可水平扩展；代价：最终一致性、复杂度增加。

## 4. 无服务器架构

### 4.1 Serverless 核心理念

Serverless 不是没有服务器，而是**无需管理服务器**：

- **FaaS（Function as a Service）**：按请求执行代码
- **BaaS（Backend as a Service）**：托管后端服务（数据库、认证、存储）

### 4.2 FaaS 执行模型

```mermaid
flowchart LR
    A[请求到达] --> B[冷启动] --> C[初始化运行时] --> D[执行函数] --> E[返回结果] --> F[实例保活] --> G[超时回收]
    G -.->|下次请求，若实例已回收| B
```

冷启动时间参考：

| 运行时  | 冷启动时间 | 备注           |
| ------- | ---------- | -------------- |
| Node.js | 100-300ms  | 较快           |
| Python  | 200-500ms  | 中等           |
| Java    | 1-3s       | JVM 启动开销   |
| Go      | 50-200ms   | 编译型，启动快 |
| Rust    | 50-150ms   | 编译型，启动快 |
| .NET    | 500ms-2s   | CLR 初始化     |

### 4.3 Serverless 适用场景

**适合**：

- 事件驱动型工作负载（Webhook、定时任务）
- 流量波动大的 API
- 数据处理管道（ETL）
- 实时文件处理（图片/视频转码）

**不适合**：

- 长时间运行任务（>15min）
- 低延迟要求（冷启动不可控）
- 需要持久连接（WebSocket、gRPC 流）
- 高频小请求（调用费用累积）

### 4.4 Serverless 成本模型

$$
\text{月成本} = \text{请求数} \times \text{单价/百万请求} + \sum_{i} (\text{执行时间}_i \times \text{内存}_i \times \text{单价/GB·s})
$$

与传统方案的成本交叉点：

$$
\text{当 } \frac{\text{请求量} \times \text{平均执行时间}}{\text{时间窗口}} < \text{服务器利用率阈值} \text{ 时，Serverless 更优}
$$

## 5. 多区域高可用架构

### 5.1 高可用层级

```mermaid
flowchart TD
    GLB[全球负载均衡 DNS/CDN]
    subgraph RA[区域 A]
        ALB1[ALB 多 AZ]
        AZ1[AZ1] AZ2[AZ2] AZ3[AZ3]
        DB1[数据库主]
    end
    subgraph RB[区域 B]
        ALB2[ALB 多 AZ]
        BZ1[AZ1] BZ2[AZ2] BZ3[AZ3]
        DB2[数据库从]
    end
    GLB --> ALB1
    GLB --> ALB2
```

### 5.2 RPO 与 RTO

| 指标                | 含义                     | 典型值                |
| ------------------- | ------------------------ | --------------------- |
| RPO（恢复点目标）   | 可容忍的最大数据丢失量   | 0（同步复制）- 数小时 |
| RTO（恢复时间目标） | 可容忍的最大服务中断时间 | 秒级 - 数小时         |

$$
\text{可用性} = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} = 1 - \frac{\text{MTTR}}{\text{MTBF} + \text{MTTR}}
$$

其中 MTBF 为平均故障间隔时间，MTTR 为平均恢复时间。

### 5.3 灾备策略

| 策略       | RPO    | RTO    | 成本 | 实现方式                 |
| ---------- | ------ | ------ | ---- | ------------------------ |
| 备份与恢复 | 小时级 | 小时级 | 低   | 定期备份到对象存储       |
| 预置备用   | 分钟级 | 分钟级 | 中   | 备用区域保持最小容量     |
| 温备用     | 秒级   | 分钟级 | 中高 | 备用区域持续运行但流量低 |
| 多活       | 接近零 | 接近零 | 高   | 多区域同时服务           |

## 6. 架构评审

### 6.1 架构决策记录（ADR）

每个重要架构决策应记录：

```
ADR-001: 选择事件驱动架构处理订单流程

状态: 已接受

背景:
  订单系统需要与支付、库存、物流等多个系统交互，
  同步调用导致级联故障风险和响应延迟增加。

决策:
  采用事件驱动架构，订单服务发布领域事件，
  下游服务异步订阅处理。

后果:
  正面: 松耦合、弹性提升、可独立扩展
  负面: 最终一致性、调试复杂度增加、需要事件排序机制
```

### 6.2 架构评审检查清单

**可靠性**：

- [ ] 单点故障是否消除
- [ ] 是否有自动故障转移机制
- [ ] 是否有重试与熔断策略
- [ ] 是否有混沌工程验证

**安全性**：

- [ ] 数据是否加密（传输中 + 静态）
- [ ] 身份认证与授权是否完备
- [ ] 是否有网络分段与隔离
- [ ] 是否有安全扫描与审计

**可扩展性**：

- [ ] 是否支持水平扩展
- [ ] 是否有自动伸缩策略
- [ ] 是否有缓存策略
- [ ] 数据库是否有分片方案

**可观测性**：

- [ ] 是否有指标监控
- [ ] 是否有分布式追踪
- [ ] 是否有结构化日志
- [ ] 是否有告警与 Runbook

<!-- ============ 文档分隔线：034-cloud-computing/008-PublicCloudPrivateCloudHybridCloud.md ============ -->

## 1. 部署模型概述

### 1.1 四种部署模型

| 模型   | 基础设施归属 | 访问范围 |
| ------ | ------------ | -------- |
| 公有云 | 云供应商     | 公开     |
| 私有云 | 组织自建     | 组织内部 |
| 混合云 | 混合         | 按需     |
| 多云   | 多供应商     | 按需     |

## 2. 公有云

### 2.1 特点

| 优势         | 劣势           |
| ------------ | -------------- |
| 无需前期投资 | 数据不在本地   |
| 弹性伸缩     | 依赖供应商     |
| 全球部署     | 长期成本可能高 |
| 丰富的服务   | 合规限制       |
| 快速上线     | 供应商锁定     |

### 2.2 主要供应商

| 供应商 | 市场份额 | 优势               |
| ------ | -------- | ------------------ |
| AWS    | ~32%     | 最全面、生态最丰富 |
| Azure  | ~23%     | 企业集成、混合云   |
| GCP    | ~11%     | 数据分析、AI/ML    |
| 阿里云 | ~6%      | 中国市场、电商     |
| 华为云 | ~4%      | 政企、5G           |

### 2.3 适用场景

- 初创公司
- 互联网应用
- 全球化业务
- AI/ML 工作负载
- 开发测试环境

## 3. 私有云

### 3.1 特点

| 优势         | 劣势         |
| ------------ | ------------ |
| 数据完全控制 | 前期投资大   |
| 安全合规     | 运维成本高   |
| 定制化       | 扩展性受限   |
| 低延迟       | 技术门槛高   |
| 无供应商锁定 | 资源利用率低 |

### 3.2 实现方式

| 方式       | 描述               | 代表                      |
| ---------- | ------------------ | ------------------------- |
| 自建       | 购买硬件+部署软件  | OpenStack, VMware         |
| 托管       | 供应商提供专属硬件 | AWS Outposts, Azure Stack |
| 虚拟私有云 | 公有云中的隔离网络 | VPC                       |

### 3.3 适用场景

- 金融/政府
- 数据敏感行业
- 合规要求严格
- 大规模稳定负载
- 核心业务系统

## 4. 混合云

### 4.1 架构

```mermaid
flowchart LR
    P[私有云<br/>核心业务] <-->|专线/VPN| U[公有云<br/>弹性负载]
```

### 4.2 典型模式

| 模式     | 描述                           |
| -------- | ------------------------------ |
| 云爆发   | 私有云为主，公有云应对峰值     |
| 数据驻留 | 敏感数据在私有云，计算在公有云 |
| 灾备     | 公有云作为灾备站点             |
| 边缘计算 | 边缘节点+云端协同              |

### 4.3 关键技术

| 技术     | 作用               |
| -------- | ------------------ |
| 专线连接 | 低延迟、高带宽互联 |
| 统一管理 | 混合云管理平台     |
| 容器化   | 跨云一致性         |
| Istio    | 服务网格跨云通信   |

## 5. 多云

### 5.1 驱动因素

- 避免供应商锁定
- 选择最优服务
- 合规要求
- 灾备冗余
- 成本优化

### 5.2 挑战

| 挑战       | 解决方案          |
| ---------- | ----------------- |
| 管理复杂   | 统一管理平台      |
| 网络互联   | 云间专线          |
| 数据一致性 | 分布式存储        |
| 技能要求   | Terraform/Ansible |
| 成本控制   | FinOps            |

## 6. 选型指南

| 场景        | 推荐模型      |
| ----------- | ------------- |
| 初创/互联网 | 公有云        |
| 金融/政府   | 私有云+混合云 |
| 弹性业务    | 混合云        |
| 全球化      | 多云          |
| 合规+弹性   | 混合云        |

<!-- ============ 文档分隔线：034-cloud-computing/009-DockerDeepAnalysis.md ============ -->

## 1. Docker 镜像优化

### 1.1 多阶段构建

```dockerfile
# 构建阶段
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# 运行阶段
FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

### 1.2 镜像瘦身策略

| 策略                 | 效果           |
| -------------------- | -------------- |
| 使用 Alpine 基础镜像 | 减少 80%+ 体积 |
| 多阶段构建           | 去除构建依赖   |
| 合并 RUN 指令        | 减少镜像层数   |
| .dockerignore        | 排除不必要文件 |
| distroless 镜像      | 最小运行时     |

### 1.3 缓存优化

```dockerfile
#  先复制依赖文件，利用缓存
COPY package*.json ./
RUN npm ci
COPY . .

#  先复制全部，每次代码变更都重新安装依赖
COPY . .
RUN npm ci
```

## 2. Docker 网络

### 2.1 网络模式

| 模式    | 描述           | 用途         |
| ------- | -------------- | ------------ |
| bridge  | 默认桥接网络   | 单机容器通信 |
| host    | 共享宿主机网络 | 高性能场景   |
| none    | 无网络         | 安全隔离     |
| overlay | 跨主机网络     | Swarm/集群   |
| macvlan | 容器独立 MAC   | 网络设备集成 |

### 2.2 自定义网络

```bash
# 创建自定义网络
docker network create --driver bridge --subnet 172.20.0.0/16 mynet

# 容器加入网络
docker run --network mynet --name app nginx

# 容器间通过名称通信
docker run --network mynet --name api my-api
# app 容器可通过 http://api:8080 访问
```

### 2.3 DNS 解析

- 自定义网络：内置 DNS，支持容器名解析
- 默认 bridge：无 DNS，需 `--link`（已废弃）

## 3. Docker 存储

### 3.1 存储类型

| 类型       | 描述           | 生命周期       |
| ---------- | -------------- | -------------- |
| Volume     | Docker 管理    | 独立于容器     |
| Bind Mount | 宿主机目录挂载 | 独立于容器     |
| tmpfs      | 内存存储       | 容器停止即消失 |

### 3.2 Volume 操作

```bash
# 创建
docker volume create mydata

# 使用
docker run -v mydata:/data nginx

# 指定驱动
docker volume create --driver local --opt type=nfs mydata

# 备份
docker run --rm -v mydata:/data -v $(pwd):/backup alpine tar czf /backup/data.tar.gz /data
```

### 3.3 存储驱动

| 驱动         | 文件系统     | 适用场景    |
| ------------ | ------------ | ----------- |
| overlay2     | overlayfs    | 默认推荐    |
| devicemapper | devicemapper | CentOS 旧版 |
| btrfs        | btrfs        | 大量写入    |
| zfs          | zfs          | 数据完整性  |

## 4. Docker Compose

### 4.1 完整示例

```yaml
version: '3.8'
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - '3000:3000'
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    healthcheck:
      test: ['CMD-SHELL', 'pg_isready -U postgres']
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
```

## 5. Docker 安全

### 5.1 镜像安全

| 措施         | 描述                              |
| ------------ | --------------------------------- |
| 非 root 运行 | `USER app`                        |
| 最小基础镜像 | Alpine/distroless                 |
| 镜像扫描     | Trivy/Snyk                        |
| 签名验证     | Docker Content Trust              |
| 固定版本     | `node:18.17.0` 而非 `node:latest` |

### 5.2 运行时安全

```dockerfile
# 安全 Dockerfile
FROM node:18-alpine
RUN addgroup -g 1001 app && adduser -u 1001 -G app -s /bin/sh -D app
WORKDIR /app
COPY --chown=app:app . .
USER app
EXPOSE 3000
CMD ["node", "server.js"]
```

### 5.3 资源限制

```bash
# CPU 和内存限制
docker run --cpus=0.5 --memory=512m nginx

# 只读文件系统
docker run --read-only --tmpfs /tmp nginx
```

## 6. Docker 最佳实践

| 实践             | 描述             |
| ---------------- | ---------------- |
| 一个容器一个进程 | 单一职责         |
| 无状态设计       | 数据存 Volume    |
| 健康检查         | HEALTHCHECK 指令 |
| 优雅关闭         | 处理 SIGTERM     |
| 日志管理         | stdout/stderr    |
| 环境变量配置     | 不硬编码         |

<!-- ============ 文档分隔线：034-cloud-computing/010-CloudNativeApp.md ============ -->

## 1. 云原生定义与演进

### 1.1 CNCF 定义

云原生技术**赋能组织在公有云、私有云和混合云等动态环境中构建和运行可弹性扩展的应用**。云原生的代表技术包括容器、服务网格、不可变基础设施和声明式 API。

云原生技术栈全景：

```mermaid
flowchart TD
    App[应用层<br/>Serverless / Batch / Streaming / ML Pipeline] --> Plat[平台层<br/>Kubernetes / Service Mesh / CI-CD / Observability]
    Plat --> Infra[基础设施层<br/>Container Runtime / IaC / Cloud Provider APIs]
```

### 1.2 云原生成熟度模型

| 阶段    | 描述     | 关键特征              |
| ------- | -------- | --------------------- |
| Level 0 | 传统部署 | 手动部署，无容器化    |
| Level 1 | 容器化   | 应用容器化，手动编排  |
| Level 2 | 编排化   | K8s 部署，自动伸缩    |
| Level 3 | 声明式   | GitOps，IaC，自动配置 |
| Level 4 | 自服务   | 平台工程，开发者门户  |
| Level 5 | 智能化   | AIOps，自适应优化     |

## 2. 12-Factor 方法论

### 2.1 十二因素详解

| #   | 因素           | 核心原则               | 云原生实践                       |
| --- | -------------- | ---------------------- | -------------------------------- |
| 1   | 代码库         | 一份代码库，多次部署   | 单仓库 / 多仓库 + 共享库         |
| 2   | 依赖           | 显式声明并隔离依赖     | Dockerfile、go.mod、package.json |
| 3   | 配置           | 在环境中存储配置       | ConfigMap、Secret、环境变量      |
| 4   | 后端服务       | 将后端服务当作附加资源 | Service Binding、CSI             |
| 5   | 构建/发布/运行 | 严格分离构建和运行     | CI → 镜像仓库 → CD               |
| 6   | 进程           | 无状态进程             | 无状态 Pod + 外部状态存储        |
| 7   | 端口绑定       | 通过端口绑定提供服务   | Service + Ingress                |
| 8   | 并发           | 通过进程模型扩展       | HPA + Pod 水平扩展               |
| 9   | 易处理         | 快速启动和优雅终止     | 健康检查 + 优雅关闭              |
| 10  | 开发/生产一致  | 尽可能保持一致         | 容器镜像统一环境                 |
| 11  | 日志           | 将日志视为事件流       | stdout → Fluentd → ES            |
| 12  | 管理进程       | 一次性管理进程         | Job / CronJob                    |

### 2.2 扩展因素（15-Factor）

在 12-Factor 基础上的扩展：

- **13. API First**：API 优先设计，契约驱动开发
- **14. Telemetry**：可观测性内置，指标/日志/追踪三合一
- **15. Security**：安全左移，SBOM、漏洞扫描、签名验证

## 3. 容器化最佳实践

### 3.1 镜像优化

**多阶段构建**：

```dockerfile
# 构建阶段
FROM golang:1.22 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o server .

# 运行阶段
FROM gcr.io/distroless/static:nonroot
COPY --from=builder /app/server /server
USER nonroot:nonroot
ENTRYPOINT ["/server"]
```

**镜像大小优化策略**：

| 策略             | 效果             | 示例                              |
| ---------------- | ---------------- | --------------------------------- |
| 使用精简基础镜像 | 减少 80-90%      | `alpine`、`distroless`、`scratch` |
| 多阶段构建       | 仅保留运行时产物 | 编译型语言必用                    |
| 合并层           | 减少层数         | `&&` 合并 RUN 指令                |
| .dockerignore    | 排除无关文件     | 排除 `.git`、`node_modules`       |
| 镜像压缩         | 减小传输大小     | `docker-slim`、`crane`            |

### 3.2 安全最佳实践

- **非 root 运行**：`USER nonroot:nonroot`
- **只读文件系统**：`readOnlyRootFilesystem: true`
- **最小权限**：仅安装必要包，删除包管理器缓存
- **镜像签名**：Cosign / Notary 签名验证
- **漏洞扫描**：Trivy / Grype 集成 CI
- **SBOM**：生成软件物料清单

### 3.3 健康检查

```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 10
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5

startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

三种探针的区别：

| 探针           | 用途               | 失败后果             |
| -------------- | ------------------ | -------------------- |
| livenessProbe  | 检测死锁/无响应    | 重启容器             |
| readinessProbe | 检测是否可接收流量 | 从 Service 移除      |
| startupProbe   | 检测启动是否完成   | 在成功前阻止其他探针 |

## 4. Kubernetes 编排进阶

### 4.1 工作负载管理

| 资源        | 用途         | 特点                   |
| ----------- | ------------ | ---------------------- |
| Deployment  | 无状态应用   | 滚动更新、回滚         |
| StatefulSet | 有状态应用   | 稳定网络标识、有序部署 |
| DaemonSet   | 节点守护进程 | 每节点一个 Pod         |
| Job         | 一次性任务   | 完成即退出             |
| CronJob     | 定时任务     | Cron 表达式调度        |

### 4.2 调度策略

**节点选择器与亲和性**：

```yaml
# 节点选择器（简单）
nodeSelector:
  disktype: ssd

# 节点亲和性（高级）
affinity:
  nodeAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      nodeSelectorTerms:
        - matchExpressions:
            - key: topology.kubernetes.io/zone
              operator: In
              values: [us-east-1a, us-east-1b]
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 80
        preference:
          matchExpressions:
            - key: node.kubernetes.io/instance-type
              operator: In
              values: [m6i.large, m6i.xlarge]

# Pod 反亲和性（分散部署）
podAntiAffinity:
  preferredDuringSchedulingIgnoredDuringExecution:
    - weight: 100
      podAffinityTerm:
        labelSelector:
          matchLabels:
            app: my-service
        topologyKey: kubernetes.io/hostname
```

### 4.3 资源管理

**请求与限制**：

```yaml
resources:
  requests: # 调度依据，保证最低资源
    cpu: '250m' # 0.25 核
    memory: '256Mi'
  limits: # 硬上限，超限 OOMKill 或 Throttle
    cpu: '500m' # 0.5 核
    memory: '512Mi'
```

CPU Throttle 原理：容器在 100ms 周期内使用完 CPU 配额后会被限流：

$$
\text{CPU 周期} = 100\text{ms}, \quad \text{配额} = \text{limit} \times 100\text{ms}
$$

$$
\text{limit}=500\text{m} \Rightarrow \text{配额}=50\text{ms}, \text{即每 100ms 可用 50ms}
$$

**QoS 等级**：

| QoS        | 条件                           | 驱逐优先级 |
| ---------- | ------------------------------ | ---------- |
| Guaranteed | requests == limits（CPU+内存） | 最后被驱逐 |
| Burstable  | requests < limits              | 中等       |
| BestEffort | 无 requests/limits             | 最先被驱逐 |

### 4.4 自动伸缩

**HPA（水平 Pod 伸缩）**：

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: '1000'
```

伸缩算法：

$$
\text{期望副本数} = \left\lceil \frac{\text{当前指标值}}{\text{目标指标值}} \times \text{当前副本数} \right\rceil
$$

**VPA（垂直 Pod 伸缩）**：自动调整 Pod 的 CPU/内存请求和限制。

**Cluster Autoscaler**：根据 Pod 调度失败自动增减节点。

## 5. GitOps 工作流

### 5.1 GitOps 核心原则

1. **声明式**：系统所有配置声明式描述
2. **版本控制**：所有声明存储在 Git 中
3. **自动拉取**：系统自动从 Git 拉取期望状态
4. **持续协调**：软件代理持续对比实际状态与期望状态

### 5.2 GitOps 工具对比

| 工具          | 推模型 | 拉模型 | 多集群 | 生态           |
| ------------- | ------ | ------ | ------ | -------------- |
| ArgoCD        |        |        |        | CNCF Graduated |
| Flux          |        |        |        | CNCF Graduated |
| Rancher Fleet |        |        |        | SUSE 生态      |

### 5.3 ArgoCD 工作流

```mermaid
flowchart TD
    T0["开发者推送代码 → CI 构建镜像 → 更新 Git 仓库中的镜像标签"]
    T1["ArgoCD 检测到 Git 变更 → 生成 Diff → 自动/手动同步 → K8s 应用更新"]
    T2["ArgoCD 持续对比 Git 状态与集群状态 → 检测漂移 → 自动修正"]
    T0 --> T1
    T1 --> T2
```

**Application 清单**：

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
spec:
  project: default
  source:
    repoURL: https://github.com/org/k8s-manifests
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## 6. 云原生可观测性

### 6.1 三大支柱

```mermaid
flowchart LR
    O[可观测性]
    O --> M[指标 Metrics<br/>Prometheus / Grafana / Datadog]
    O --> L[日志 Logs<br/>Fluentd / Loki / Elasticsearch]
    O --> T[追踪 Traces<br/>OpenTelemetry / Jaeger / Tempo]
```

### 6.2 OpenTelemetry 统一标准

OpenTelemetry 统一了指标、日志和追踪的采集与传输：

```mermaid
flowchart TD
    T0["应用代码 → OTel SDK → OTel Collector → 后端（Prometheus/Jaeger/Loki）"]
    T1["Trace（W3C Trace Context）"]
    T2["Metrics（OTLP）"]
    T3["Logs（OTLP）"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
```

**W3C Trace Context 传播**：

```
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
             │  │                │                │           │
             版本 trace-id       span-id          采样标志
```

### 6.3 SLO/SLI/SLA

| 概念 | 含义                     | 示例                   |
| ---- | ------------------------ | ---------------------- |
| SLA  | 服务等级协议（商业合同） | 99.9% 可用性，违约退款 |
| SLO  | 服务等级目标（内部目标） | 99.95% 可用性          |
| SLI  | 服务等级指标（度量值）   | 成功请求 / 总请求      |

**错误预算**：

$$
\text{错误预算} = 1 - \text{SLO}
$$

$$
\text{月度错误预算（分钟）} = 30 \times 24 \times 60 \times (1 - \text{SLO})
$$

| SLO     | 月度允许宕机 | 年度允许宕机 |
| ------- | ------------ | ------------ |
| 99.9%   | 43.8 分钟    | 8.76 小时    |
| 99.95%  | 21.9 分钟    | 4.38 小时    |
| 99.99%  | 4.38 分钟    | 52.6 分钟    |
| 99.999% | 26 秒        | 5.26 分钟    |

<!-- ============ 文档分隔线：034-cloud-computing/011-KubernetesArchitecture.md ============ -->

## 1. Kubernetes 整体架构

### 1.1 架构图

```mermaid
flowchart TD
    subgraph CP[控制平面]
        API[API Server]
        SCH[Scheduler]
        CM[Controller Manager]
        ETCD[etcd]
    end
    subgraph N1[Node 1]
        K1[kubelet] P1[kube-proxy] PD1[Pods]
    end
    subgraph N2[Node 2]
        K2[kubelet] P2[kube-proxy] PD2[Pods]
    end
    CP --> N1
    CP --> N2
```

### 1.2 设计理念

| 理念       | 描述                       |
| ---------- | -------------------------- |
| 声明式 API | 描述期望状态，系统自动趋近 |
| 控制循环   | 持续观测并调和状态         |
| 松耦合     | 组件间通过 API 通信        |
| 可扩展     | CRD、Operator、插件        |

## 2. 控制平面组件

### 2.1 API Server

集群的统一入口，所有操作都通过 API Server 进行。

**核心功能**：

- RESTful API 网关
- 认证、授权、准入控制
- 数据验证与持久化
- Watch 机制（变更通知）

**请求流程**：

```
请求 → 认证 → 授权 → 准入控制 → 验证 → etcd 持久化 → 响应
```

### 2.2 etcd

分布式键值存储，Kubernetes 的唯一状态存储。

| 特性   | 描述            |
| ------ | --------------- |
| 一致性 | Raft 共识协议   |
| Watch  | 监听键值变化    |
| 事务   | Compare-and-Set |
| TTL    | 键值过期        |

**运维要点**：

- 奇数节点（3/5/7）
- SSD 存储
- 独立部署
- 定期备份

### 2.3 Scheduler

负责将 Pod 调度到合适的节点。

**调度流程**：

```
1. 过滤（Filter）：排除不满足条件的节点
2. 评分（Score）：对可行节点打分
3. 绑定（Bind）：将 Pod 绑定到最高分节点
```

**调度策略**：

| 策略            | 描述                          |
| --------------- | ----------------------------- |
| 节点选择器      | `nodeSelector`                |
| 节点亲和性      | `nodeAffinity`                |
| Pod 亲和/反亲和 | `podAffinity/podAntiAffinity` |
| 污点与容忍      | `taints/tolerations`          |
| 资源限制        | CPU/内存请求与限制            |

### 2.4 Controller Manager

运行各种控制器，每个控制器是一个控制循环。

| 控制器                     | 功能            |
| -------------------------- | --------------- |
| Deployment Controller      | 管理 ReplicaSet |
| ReplicaSet Controller      | 维护 Pod 副本数 |
| Node Controller            | 节点健康监测    |
| Job Controller             | 一次性任务      |
| Endpoints Controller       | Service 端点    |
| Service Account Controller | 服务账户        |

## 3. 节点组件

### 3.1 kubelet

节点上的代理，负责 Pod 的生命周期管理。

**核心职责**：

- Pod 创建与销毁
- 容器健康检查
- 资源使用上报
- Volume 挂载

### 3.2 kube-proxy

维护网络规则，实现 Service 的负载均衡。

**代理模式**：

| 模式      | 描述          | 性能         |
| --------- | ------------- | ------------ |
| iptables  | iptables 规则 | 中           |
| IPVS      | IPVS 负载均衡 | 高           |
| userspace | 用户空间代理  | 低（已弃用） |

### 3.3 容器运行时

| 运行时     | 特点            |
| ---------- | --------------- |
| containerd | 默认推荐        |
| CRI-O      | 轻量级          |
| Docker     | 已弃用（1.24+） |

## 4. API 对象与资源

### 4.1 核心资源

| 资源        | API 组     | 描述               |
| ----------- | ---------- | ------------------ |
| Pod         | core       | 最小调度单元       |
| Service     | core       | 服务发现与负载均衡 |
| ConfigMap   | core       | 配置管理           |
| Secret      | core       | 敏感数据           |
| Namespace   | core       | 资源隔离           |
| Deployment  | apps       | 无状态应用         |
| StatefulSet | apps       | 有状态应用         |
| DaemonSet   | apps       | 每节点一个 Pod     |
| Job         | batch      | 一次性任务         |
| CronJob     | batch      | 定时任务           |
| Ingress     | networking | HTTP 路由          |
| PV/PVC      | storage    | 持久化存储         |

### 4.2 声明式管理

```yaml
# 期望状态
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.25
```

## 5. 高可用架构

### 5.1 控制平面 HA

```mermaid
flowchart TD
    LB[负载均衡器 LB]
    M1[Master 1 leader]
    M2[Master 2 follower]
    M3[Master 3 follower]
    LB --> M1
    LB --> M2
    LB --> M3
```

### 5.2 etcd HA

- 3 节点容忍 1 节点故障
- 5 节点容忍 2 节点故障
- 使用 Raft 协议选举 Leader
## 上下文与配置

**基本写法：查看 kubeconfig**
`kubectl config view`
```bash
# 查看当前 kubeconfig 配置
kubectl config view
```

---

**基本写法：合并多个 kubeconfig**
`KUBECONFIG=<文件1>:<文件2> kubectl config view --flatten > merged.conf`
```bash
# 合并多个集群配置
KUBECONFIG=~/.kube/config:cluster2.conf kubectl config view --flatten > merged.conf
```

---

**基本写法：切换上下文**
`kubectl config use-context <上下文名>`
```bash
# 切换到指定上下文
kubectl config use-context my-cluster
```

---

**基本写法：设置默认命名空间**
`kubectl config set-context --current --namespace=<命名空间>`
```bash
# 为当前上下文设置默认命名空间
kubectl config set-context --current --namespace=production
```

---

**基本写法：创建用户凭证**
`kubectl config set-credentials <用户名> --token=<token>`
```bash
# 为 kubeconfig 添加 token 认证
kubectl config set-credentials my-user --token=eyJhbGciOiJSUzI1...
```

---

## 资源管理进阶

**基本写法：使用标签过滤**
`kubectl get pods -l <标签选择器>`
```bash
# 通过标签筛选 Pod
kubectl get pods -l app=web,tier=frontend
```

---

**基本写法：使用字段选择器**
`kubectl get pods --field-selector status.phase=Running`
```bash
# 仅查询运行中的 Pod
kubectl get pods --field-selector status.phase=Running
```

---

**基本写法：跨命名空间查询**
`kubectl get pods --all-namespaces`
```bash
# 查询所有命名空间的 Pod
kubectl get pods --all-namespaces
```

---

**基本写法：自定义列输出**
`kubectl get pods -o custom-columns=<列定义>`
```bash
# 自定义输出列展示资源使用
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName
```

---

**基本写法：JSONPath 输出**
`kubectl get pods -o jsonpath='<表达式>'`
```bash
# 提取所有 Pod 名和 IP
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

---

## Pod 调试

**基本写法：进入容器执行命令**
`kubectl exec -it <pod> [-c <容器>] -- <命令>`
```bash
# 进入 nginx 容器交互式 shell
kubectl exec -it my-pod -c nginx -- /bin/sh
```

---

**基本写法：临时调试容器**
`kubectl debug -it <pod> --image=<镜像> --target=<容器>`
```bash
# 注入临时调试容器排查问题
kubectl debug -it my-pod --image=busybox:1.36 --target=my-app
```

---

**基本写法：节点调试**
`kubectl debug node/<节点> -it --image=<镜像>`
```bash
# 在节点上创建调试 Pod
kubectl debug node/my-node -it --image=ubuntu:22.04
```

---

**基本写法：复制文件到容器**
`kubectl cp <本地文件> <命名空间>/<pod>:<路径>`
```bash
# 将本地文件复制到 Pod
kubectl cp ./app.conf my-pod:/etc/app/app.conf
```

---

**基本写法：端口转发**
`kubectl port-forward <pod> <本地端口>:<容器端口>`
```bash
# 转发 Pod 端口到本地
kubectl port-forward my-pod 8080:80
```

---

## 日志与事件

**基本写法：查看多容器 Pod 日志**
`kubectl logs <pod> [-c <容器>] [--tail <行数>]`
```bash
# 查看指定容器最近 100 行日志
kubectl logs my-pod -c sidecar --tail=100
```

---

**基本写法：实时流式日志**
`kubectl logs -f <pod>`
```bash
# 实时跟踪 Pod 日志输出
kubectl logs -f my-pod
```

---

**基本写法：基于标签聚合日志**
`kubectl logs -l <标签选择器>`
```bash
# 查看某应用所有 Pod 日志
kubectl logs -l app=web --tail=50
```

---

**基本写法：查看之前容器日志**
`kubectl logs <pod> --previous`
```bash
# 查看容器崩溃前的日志
kubectl logs my-pod --previous
```

---

**基本写法：查看事件**
`kubectl get events [--sort-by='.lastTimestamp']`
```bash
# 按时间排序查看事件
kubectl get events --sort-by='.lastTimestamp' -n default
```

---

## 资源伸缩

**基本写法：扩缩 Deployment**
`kubectl scale deployment <名称> --replicas=<数量>`
```bash
# 将副本数扩到 5
kubectl scale deployment web --replicas=5
```

---

**基本写法：基于文件扩缩**
`kubectl scale -f <文件> --replicas=<数量>`
```bash
# 通过资源清单文件扩缩
kubectl scale -f deployment.yaml --replicas=3
```

---

**基本写法：自动伸缩**
`kubectl autoscale deployment <名称> --min=<最小> --max=<最大> --cpu-percent=<百分比>`
```bash
# 创建 HPA 基于 CPU 自动伸缩
kubectl autoscale deployment web --min=2 --max=10 --cpu-percent=70
```

---

**基本写法：查看 HPA 状态**
`kubectl get hpa`
```bash
# 查看水平自动伸缩器
kubectl get hpa -w
```

---

**基本写法：滚动更新**
`kubectl set image deployment/<名称> <容器>=<新镜像>`
```bash
# 更新镜像触发滚动更新
kubectl set image deployment/web nginx=nginx:1.25
```

---

## 滚动更新管理

**基本写法：查看更新状态**
`kubectl rollout status deployment/<名称>`
```bash
# 实时查看滚动更新进度
kubectl rollout status deployment/web
```

---

**基本写法：查看历史版本**
`kubectl rollout history deployment/<名称>`
```bash
# 查看 Deployment 修订历史
kubectl rollout history deployment/web
```

---

**基本写法：回滚到指定版本**
`kubectl rollout undo deployment/<名称> --to-revision=<版本>`
```bash
# 回滚到修订版本 3
kubectl rollout undo deployment/web --to-revision=3
```

---

**基本写法：暂停滚动更新**
`kubectl rollout pause deployment/<名称>`
```bash
# 暂停更新便于多次修改
kubectl rollout pause deployment/web
```

---

**基本写法：恢复滚动更新**
`kubectl rollout resume deployment/<名称>`
```bash
# 恢复暂停的滚动更新
kubectl rollout resume deployment/web
```

---

## 网络与策略

**基本写法：创建网络策略**
```yaml
# network-policy.yaml 限制 Pod 间通信
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: web-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: web
  policyTypes:
    - Ingress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: api
      ports:
        - protocol: TCP
          port: 80
```

---

**基本写法：应用网络策略**
`kubectl apply -f <策略文件>`
```bash
# 创建网络策略限制访问
kubectl apply -f network-policy.yaml
```

---

**基本写法：DNS 测试**
`kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup <服务名>`
```bash
# 测试集群内 DNS 解析
kubectl run dns-test --image=busybox:1.36 --rm -it -- nslookup kubernetes.default
```

---

**基本写法：连通性测试**
`kubectl run curl-test --image=curlimages/curl:8.5.0 --rm -it -- curl <URL>`
```bash
# 在集群内测试服务连通性
kubectl run curl-test --image=curlimages/curl:8.5.0 --rm -it -- curl http://web.default.svc.cluster.local
```

---

**基本写法：查看 Endpoints**
`kubectl get endpoints <服务名>`
```bash
# 查看服务对应的后端 Pod
kubectl get endpoints web
```

---

## 存储管理

**基本写法：列出存储类**
`kubectl get storageclass`
```bash
# 查看集群所有存储类
kubectl get sc
```

---

**基本写法：创建持久卷声明**
```yaml
# pvc.yaml 持久卷声明
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 10Gi
```

---

**基本写法：动态供给卷**
`kubectl apply -f pvc.yaml`
```bash
# 创建 PVC 触发动态供给
kubectl apply -f pvc.yaml
```

---

**基本写法：查看 PV 状态**
`kubectl get pv`
```bash
# 查看所有持久卷
kubectl get pv -o wide
```

---

**基本写法：扩容 PVC**
`kubectl patch pvc <名称> -p '{"spec":{"resources":{"requests":{"storage":"20Gi"}}}}'`
```bash
# 在线扩容 PVC
kubectl patch pvc my-pvc -p '{"spec":{"resources":{"requests":{"storage":"20Gi"}}}}'
```

---

## 安全与 RBAC

**基本写法：创建 Service Account**
`kubectl create serviceaccount <名称> [-n <命名空间>]`
```bash
# 创建服务账户
kubectl create serviceaccount my-sa -n default
```

---

**基本写法：创建角色**
```yaml
# role.yaml 命名空间内角色
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
  - apiGroups: [""]
    resources: ["pods", "pods/log"]
    verbs: ["get", "list", "watch"]
```

---

**基本写法：绑定角色**
`kubectl create rolebinding <绑定名> --role=<角色> --serviceaccount=<命名空间>:<SA>`
```bash
# 为 SA 绑定 Role
kubectl create rolebinding my-binding \
  --role=pod-reader \
  --serviceaccount=default:my-sa \
  -n default
```

---

**基本写法：集群角色绑定**
`kubectl create clusterrolebinding <绑定名> --clusterrole=<角色> --user=<用户>`
```bash
# 为用户绑定集群角色
kubectl create clusterrolebinding admin-binding \
  --clusterrole=cluster-admin \
  --user=alice@example.com
```

---

**基本写法：查看权限**
`kubectl auth can-i <动作> <资源> [--as=<用户>]`
```bash
# 检查用户是否有权限创建 Pod
kubectl auth can-i create pods --as=alice@example.com
```

---

## 集群节点管理

**基本写法：查看节点详情**
`kubectl describe node <节点名>`
```bash
# 查看节点详细信息
kubectl describe node my-node
```

---

**基本写法：节点打标签**
`kubectl label nodes <节点> <键>=<值>`
```bash
# 为节点添加标签
kubectl label nodes my-node disktype=ssd
```

---

**基本写法：节点污点**
`kubectl taint nodes <节点> <键>=<值>:<效果>`
```bash
# 为节点添加 NoSchedule 污点
kubectl taint nodes my-node dedicated=gpu:NoSchedule
```

---

**基本写法：移除污点**
`kubectl taint nodes <节点> <键>:<效果>-`
```bash
# 移除节点污点(末尾减号)
kubectl taint nodes my-node dedicated=gpu:NoSchedule-
```

---

**基本写法：节点驱逐**
`kubectl drain <节点> --ignore-daemonsets --delete-emptydir-data`
```bash
# 安全驱逐节点上所有 Pod
kubectl drain my-node --ignore-daemonsets --delete-emptydir-data
```

---

## 自定义资源与 Operator

**基本写法：查看 CRD**
`kubectl get crd`
```bash
# 列出所有自定义资源定义
kubectl get crd
```

---

**基本写法：查看 CR 实例**
`kubectl get <资源类型>`
```bash
# 查看某 CRD 的所有实例
kubectl get certificates
```

---

**基本写法：查看 Operator Pod**
`kubectl get pods -n <命名空间> | grep <operator>`
```bash
# 查看 Cert-Manager Operator
kubectl get pods -n cert-manager
```

---

**基本写法：查看 CR 详情**
`kubectl describe <资源类型> <名称>`
```bash
# 查看 Certificate 自定义资源详情
kubectl describe certificate my-cert -n default
```

---

**基本写法：编辑 CR**
`kubectl edit <资源类型> <名称>`
```bash
# 在线编辑自定义资源
kubectl edit certificate my-cert -n default
```

---

## 性能与资源

**基本写法：查看资源使用**
`kubectl top pods`
```bash
# 查看 Pod CPU/内存使用
kubectl top pods -n default
```

---

**基本写法：查看节点资源**
`kubectl top nodes`
```bash
# 查看节点资源使用情况
kubectl top nodes
```

---

**基本写法：查看资源配额**
`kubectl describe resourcequota`
```bash
# 查看命名空间资源配额
kubectl describe resourcequota -n default
```

---

**基本写法：创建 LimitRange**
```yaml
# limit-range.yaml 默认资源限制
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
spec:
  limits:
    - type: Container
      default:
        cpu: 500m
        memory: 512Mi
      defaultRequest:
        cpu: 100m
        memory: 128Mi
```

---

**基本写法：创建 ResourceQuota**
```yaml
# resource-quota.yaml 命名空间配额
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    persistentvolumeclaims: "10"
```

---

## 高级调度

**基本写法：节点亲和性**
```yaml
# 通过节点亲和性调度 Pod
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: disktype
                operator: In
                values:
                  - ssd
  containers:
    - name: app
      image: nginx:1.25
```

---

**基本写法：Pod 反亲和性**
```yaml
# Pod 反亲和性使副本分散到不同节点
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        - labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values:
                  - web
          topologyKey: kubernetes.io/hostname
```

---

**基本写法：拓扑分布约束**
```yaml
# 跨可用区均匀分布
spec:
  topologySpreadConstraints:
    - maxSkew: 1
      topologyKey: topology.kubernetes.io/zone
      whenUnsatisfiable: DoNotSchedule
      labelSelector:
        matchLabels:
          app: web
```

---

**基本写法：优先级与抢占**
```yaml
# 高优先级 Pod 抢占低优先级
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000
globalDefault: false
description: "高优先级 Pod"
```

<!-- ============ 文档分隔线：034-cloud-computing/012-CloudDatabaseService.md ============ -->

## 1. 云数据库服务概述

### 1.1 托管数据库 vs 自建数据库

| 维度     | 托管数据库               | 自建数据库               |
| -------- | ------------------------ | ------------------------ |
| 运维负担 | 低（自动备份/升级/监控） | 高（全链路自行负责）     |
| 可用性   | 内置多 AZ 高可用         | 需自行搭建主从/集群      |
| 弹性     | 按需伸缩，存储自动扩展   | 容量规划，扩容复杂       |
| 成本     | 按使用付费，有溢价       | 前期投入大，长期可能更低 |
| 灵活性   | 受限于云厂商功能         | 完全控制配置与插件       |
| 迁移风险 | 厂商锁定                 | 无锁定                   |

### 1.2 云数据库服务分类

```mermaid
flowchart LR
    S[云数据库服务]
    S --> R[关系型<br/>RDS/Cloud SQL/MySQL/PostgreSQL/SQL Server/Oracle]
    S --> N[NoSQL<br/>DynamoDB/MongoDB Atlas/ElastiCache/Firestore]
    S --> C[云原生/新架构<br/>Aurora/PolarDB/TiDB Cloud/CockroachDB/PlanetScale]
```

## 2. 托管关系型数据库

### 2.1 AWS RDS

RDS 支持多种数据库引擎，提供统一的托管能力：

| 引擎       | 版本  | 最大存储 | 最大实例        |
| ---------- | ----- | -------- | --------------- |
| MySQL      | 8.0   | 64 TB    | db.r6g.16xlarge |
| PostgreSQL | 16    | 64 TB    | db.r6g.16xlarge |
| MariaDB    | 10.11 | 64 TB    | db.r6g.16xlarge |
| Oracle     | 19c   | 64 TB    | db.r6g.16xlarge |
| SQL Server | 2022  | 16 TB    | db.r6g.16xlarge |

**多 AZ 部署架构**：

```mermaid
flowchart TD
    subgraph Region[AWS Region]
        subgraph AZA[AZ-A]
            P[Primary R/W]
        end
        subgraph AZB[AZ-B]
            S1[Standby R]
        end
        RR[Read Replica<br/>异步复制，跨区域可选]
    end
    P <-->|同步复制| S1
    P --> RR
```

### 2.2 阿里云 RDS

与 AWS RDS 类似，但针对国内场景优化：

- **X-Engine**：阿里自研存储引擎，压缩率高达 10:1
- **SQL 审计**：内置 SQL 审计与性能洞察
- **CloudDBA**：智能诊断与优化建议
- **多租户隔离**：资源组级别的 CPU/内存隔离

### 2.3 高可用与故障切换

RDS 多 AZ 故障切换流程：

```
1. 主实例故障检测（30-60秒）
2. DNS 切换到备用实例
3. 备用实例提升为主实例
4. 自动创建新的备用实例
5. 应用通过新 DNS 端点重连
```

总故障切换时间通常在 **1-5 分钟**。

## 3. 云原生数据库

### 3.1 Amazon Aurora

Aurora 是 AWS 自研的云原生关系数据库，核心创新在于**存储计算分离**：

```mermaid
flowchart TD
    subgraph Aurora[Aurora 架构]
        subgraph Compute[计算层]
            W[Writer Instance]
            R1[Reader 1 Instance]
            R2[Reader 2 Instance]
        end
        subgraph Storage[Aurora Storage 6 副本/3 AZ]
            P1[P1 AZ-A] P2[P2 AZ-A] P3[P3 AZ-B] P4[P4 AZ-B] P5[P5 AZ-C] P6[P6 AZ-C]
        end
        W --> Storage
        R1 --> Storage
        R2 --> Storage
    end
```

**Aurora 关键特性**：

- **日志即数据库**：计算节点只写 Redo Log 到存储层，存储节点自行构建数据页
- **6 副本写入**：4/6 确认即写入成功，兼顾性能与可靠性
- **读副本延迟**：亚毫秒级（共享存储，无需复制数据）
- **快速克隆**：Copy-on-Write 克隆，秒级创建

Aurora 写入流程：

$$
\text{写入延迟} = \max(\text{4 个最快副本确认时间})
$$

$$
\text{数据可靠性} = 1 - P(\text{6 副本中 ≥3 副本同时故障}) \approx 1 - 10^{-7}
$$

### 3.2 阿里云 PolarDB

PolarDB 采用类似的存储计算分离架构：

- **PolarFS**：分布式文件系统，RDMA 网络低延迟
- **共享存储**：一写多读，读节点直接共享存储
- **物理复制**：基于 Redo Log 的物理复制，延迟 < 1ms
- **Serverless**：自动弹性，按 ACU 计费

### 3.3 TiDB Cloud

TiDB 是开源的 HTAP（混合事务/分析处理）数据库：

```mermaid
flowchart TD
    subgraph TiDBCloud[TiDB Cloud 架构]
        TDB[TiDB SQL 层<br/>解析 → 优化 → 执行 → 返回]
        TKV[TiKV 行存/OLTP<br/>Raft 复制]
        TF[TiFlash 列存/OLAP<br/>异步复制]
        PD[PD 调度器]
    end
    TDB --> TKV
    TDB --> TF
    TKV --> PD
    TF --> PD
```

HTAP 查询路由：

$$
\text{查询类型} = \begin{cases} \text{OLTP} \Rightarrow \text{TiKV（行存）} \\ \text{OLAP} \Rightarrow \text{TiFlash（列存）} \end{cases}
$$

## 4. NoSQL 托管服务

### 4.1 DynamoDB

AWS DynamoDB 是全托管的键值/文档数据库：

**核心概念**：

| 概念          | 描述                   |
| ------------- | ---------------------- |
| Table         | 数据集合               |
| Item          | 一条记录（最大 400KB） |
| Attribute     | 字段                   |
| Partition Key | 分区键（必需）         |
| Sort Key      | 排序键（可选）         |
| GSI           | 全局二级索引           |
| LSI           | 本地二级索引           |

**容量模式**：

- **预置容量**：指定 RCU/WCU，适合可预测负载
- **按需容量**：自动伸缩，适合不可预测负载

$$
\text{RCU} = \begin{cases} 1 & \text{强一致读 } \leq 4\text{KB} \\ 2 & \text{最终一致读 } \leq 4\text{KB} \end{cases}
$$

$$
\text{WCU} = 1 \text{ per } 1\text{KB write}
$$

**DAX（DynamoDB Accelerator）**：内存缓存，微秒级延迟，写穿透策略。

### 4.2 MongoDB Atlas

全托管 MongoDB 服务，多云支持：

- **集群类型**：副本集、分片集群、Serverless
- **Atlas Search**：内置全文搜索（基于 Lucene）
- **Atlas Data Lake**：查询 S3 数据
- **Atlas App Services**：无服务器后端
- **自动分片**：基于分片键自动数据分布

### 4.3 ElastiCache / Redis 云服务

托管 Redis/Memcached 服务：

| 特性     | Redis                             | Memcached  |
| -------- | --------------------------------- | ---------- |
| 数据结构 | 丰富（String/List/Set/Hash/ZSet） | 简单 KV    |
| 持久化   | RDB + AOF                         | 无         |
| 集群     | Redis Cluster                     | 客户端分片 |
| 复制     | 主从复制                          | 无         |
| 适用场景 | 缓存 + 数据存储                   | 纯缓存     |

## 5. 数据库迁移策略

### 5.1 迁移方法论

```
评估 → 规划 → 迁移 → 验证 → 切换 → 优化
 │       │       │       │       │       │
 ▼       ▼       ▼       ▼       ▼       ▼
源端分析  迁移方案  全量+增量  数据校验  灰度切换  性能调优
兼容性    回滚计划  CDC同步   功能测试  流量切换  成本优化
```

### 5.2 同构迁移 vs 异构迁移

**同构迁移**（MySQL → RDS MySQL）：

- 使用原生工具（mysqldump、DTS）
- 兼容性高，风险低
- 主要关注版本差异和字符集

**异构迁移**（Oracle → PostgreSQL）：

- Schema 转换（数据类型、存储过程、SQL 方言）
- 使用 AWS SCT / 阿里云 ADAM 评估兼容性
- 应用代码适配工作量可能很大

### 5.3 最小停机迁移（CDC）

基于变更数据捕获（CDC）的迁移流程：

```
1. 全量导出源库数据 → 导入目标库
2. 启动 CDC 捕获增量变更
3. 持续同步增量数据到目标库
4. 验证数据一致性
5. 短暂停机（秒级），同步最后增量
6. 切换应用到目标库
```

CDC 工具：

| 工具        | 源端            | 目标端       | 特点           |
| ----------- | --------------- | ------------ | -------------- |
| AWS DMS     | 多种            | 多种         | 全托管         |
| Debezium    | MySQL/PG/Oracle | Kafka        | 开源，基于日志 |
| Canal       | MySQL           | Kafka/自定义 | 阿里开源       |
| Cloud Canal | 多种            | 多种         | 商业化 CDC     |

### 5.4 数据校验

迁移后必须进行数据校验：

$$
\text{校验方法} = \begin{cases} \text{行数对比} & \text{快速验证} \\ \text{Checksum 对比} & \text{精确验证} \\ \text{业务抽样验证} & \text{语义验证} \end{cases}
$$

## 6. 多区域复制与容灾

### 6.1 跨区域复制策略

| 策略     | 复制方式      | RPO         | 成本 | 适用场景 |
| -------- | ------------- | ----------- | ---- | -------- |
| 同步复制 | 写入时同步    | 0           | 高   | 金融交易 |
| 异步复制 | 后台同步      | 秒级-分钟级 | 中   | 一般业务 |
| 半同步   | 至少1个从确认 | 接近0       | 中高 | 关键业务 |

### 6.2 Aurora Global Database

Aurora 全球数据库支持跨区域只读和灾难恢复：

```mermaid
flowchart LR
    subgraph P[主区域 us-1]
        PW[Writer]
        PS[Storage 6副本]
        PW --> PS
    end
    subgraph B[备区域 eu-1]
        BR[Reader]
        BS[Storage 6副本]
        BR --> BS
    end
    PS -->|复制| BS
```

- 跨区域复制延迟通常 < 1 秒
- 备区域可挂载最多 16 个读实例
- 灾难恢复 RTO < 1 分钟（托管的集群切换）

### 6.3 DynamoDB Global Tables

DynamoDB 全球表支持多区域多活写入：

- 所有区域均可读写
- 基于最后写入者胜出（LWW）解决冲突
- 复制延迟通常 < 1 秒
- 适合全球分布的应用

### 6.4 容灾演练

容灾方案必须定期验证：

- **桌面演练**：团队讨论故障场景与应对步骤
- **组件演练**：模拟单个组件故障（数据库主从切换）
- **全量演练**：模拟区域级故障，验证完整恢复流程
- **混沌工程**：生产环境注入故障（Chaos Monkey、Litmus）

<!-- ============ 文档分隔线：034-cloud-computing/013-KubernetesCore.md ============ -->

## 1. Pod

### 1.1 Pod 概念

Pod 是 Kubernetes 最小调度单元，包含一个或多个容器，共享网络和存储。

### 1.2 Pod 生命周期

| 阶段      | 描述               |
| --------- | ------------------ |
| Pending   | 已创建，等待调度   |
| Running   | 已调度，容器运行中 |
| Succeeded | 容器正常退出       |
| Failed    | 容器异常退出       |
| Unknown   | 状态未知           |

### 1.3 Pod 配置

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-app
spec:
  containers:
    - name: app
      image: nginx:1.25
      ports:
        - containerPort: 80
      resources:
        requests:
          cpu: 100m
          memory: 128Mi
        limits:
          cpu: 500m
          memory: 512Mi
      livenessProbe:
        httpGet:
          path: /healthz
          port: 80
        initialDelaySeconds: 15
        periodSeconds: 10
      readinessProbe:
        httpGet:
          path: /ready
          port: 80
        initialDelaySeconds: 5
        periodSeconds: 5
      env:
        - name: DB_HOST
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: database_host
      volumeMounts:
        - name: data
          mountPath: /data
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: app-data
```

### 1.4 探针类型

| 探针           | 用途     | 失败动作     |
| -------------- | -------- | ------------ |
| livenessProbe  | 存活检查 | 重启容器     |
| readinessProbe | 就绪检查 | 移出 Service |
| startupProbe   | 启动检查 | 杀死容器     |

## 2. Deployment

### 2.1 概念

管理无状态应用，维护 Pod 副本数和滚动更新。

### 2.2 配置示例

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: web
          image: nginx:1.25
          ports:
            - containerPort: 80
```

### 2.3 更新策略

| 策略          | 描述             |
| ------------- | ---------------- |
| RollingUpdate | 滚动更新（默认） |
| Recreate      | 先删后建         |

### 2.4 常用操作

```bash
# 查看滚动更新状态
kubectl rollout status deployment/web

# 查看历史版本
kubectl rollout history deployment/web

# 回滚
kubectl rollout undo deployment/web

# 回滚到指定版本
kubectl rollout undo deployment/web --to-revision=2

# 暂停/恢复更新
kubectl rollout pause deployment/web
kubectl rollout resume deployment/web
```

## 3. Service

### 3.1 概念

Service 为一组 Pod 提供稳定的访问入口和负载均衡。

### 3.2 Service 类型

| 类型         | 描述                | 访问范围 |
| ------------ | ------------------- | -------- |
| ClusterIP    | 集群内部 IP（默认） | 集群内   |
| NodePort     | 节点端口映射        | 集群外   |
| LoadBalancer | 云负载均衡器        | 互联网   |
| ExternalName | CNAME 映射          | DNS      |

### 3.3 配置示例

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-service
spec:
  type: ClusterIP
  selector:
    app: web
  ports:
    - port: 80
      targetPort: 8080
```

### 3.4 服务发现

```
# 集群内访问
web-service.default.svc.cluster.local

# 简写（同命名空间）
web-service
```

## 4. StatefulSet

### 4.1 概念

管理有状态应用，提供稳定的网络标识和持久化存储。

### 4.2 与 Deployment 区别

| 特性     | Deployment | StatefulSet |
| -------- | ---------- | ----------- |
| Pod 名称 | 随机后缀   | 有序编号    |
| 网络标识 | 不稳定     | 稳定 DNS    |
| 存储     | 共享       | 独立 PVC    |
| 扩缩容   | 随机顺序   | 有序        |
| 更新     | 随机顺序   | 逆序        |

### 4.3 配置示例

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: mysql
  replicas: 3
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - name: mysql
          image: mysql:8.0
          volumeMounts:
            - name: data
              mountPath: /var/lib/mysql
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ['ReadWriteOnce']
        resources:
          requests:
            storage: 10Gi
```

## 5. ConfigMap 与 Secret

### 5.1 ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database_host: 'mysql.default.svc.cluster.local'
  database_port: '3306'
  app.properties: |
    key1=value1
    key2=value2
```

### 5.2 Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4= # base64(admin)
  password: cGFzc3dvcmQ= # base64(password)
```

> 注意：Secret 默认仅 Base64 编码，建议启用加密存储或使用外部密钥管理（Vault）。

## 6. DaemonSet 与 Job

### 6.1 DaemonSet

每个节点运行一个 Pod 副本，适用于日志采集、监控代理等。

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  selector:
    matchLabels:
      app: fluentd
  template:
    metadata:
      labels:
        app: fluentd
    spec:
      containers:
        - name: fluentd
          image: fluentd:latest
```

### 6.2 Job 与 CronJob

```yaml
# 一次性任务
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  completions: 1
  backoffLimit: 3
  template:
    spec:
      containers:
        - name: migrate
          image: myapp:migrate
      restartPolicy: Never
```

```yaml
# 定时任务
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: '0 2 * * *'
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: backup
              image: myapp:backup
          restartPolicy: OnFailure
```

<!-- ============ 文档分隔线：034-cloud-computing/014-CloudStorageService.md ============ -->

## 1. 云存储服务分类

### 1.1 存储类型对比

| 类型     | 访问方式   | 延迟      | 吞吐 | 适用场景              |
| -------- | ---------- | --------- | ---- | --------------------- |
| 对象存储 | REST API   | 10-100ms  | 高   | 图片/视频/备份/数据湖 |
| 块存储   | 块设备接口 | <1ms      | 中高 | 数据库/虚拟机磁盘     |
| 文件存储 | NFS/SMB    | 1-10ms    | 中   | 共享文件/内容管理     |
| 归档存储 | 异步恢复   | 分钟-小时 | 低   | 合规归档/冷数据       |

### 1.2 存储层级

```mermaid
flowchart TD
    H[标准/热存储<br/>频繁访问，低延迟] --> W[低频/温存储<br/>月访问1-2次，检索费]
    W --> C[归档/冷存储<br/>年访问1-2次，恢复需小时]
    C --> D[深度归档<br/>极少访问，合规保留]
```

成本递减，存取成本递增

## 2. 对象存储

### 2.1 核心概念

```mermaid
flowchart TD
    B[Bucket 桶]
    B --> O1[Object 对象]
    O1 --> D1[Data 数据]
    O1 --> K1[Key 键名]
    O1 --> M1[Metadata 元数据]
    O1 --> V1[Version ID 版本ID]
    B --> O2[Object ...]
```

各云厂商对象存储对照：

| AWS | 阿里云 | GCP           | Azure        |
| --- | ------ | ------------- | ------------ |
| S3  | OSS    | Cloud Storage | Blob Storage |

### 2.2 S3 存储类

| 存储类                  | 最小存储期 | 检索费 | 可用性 | 典型用途               |
| ----------------------- | ---------- | ------ | ------ | ---------------------- |
| S3 Standard             | 无         | 无     | 99.99% | 热数据                 |
| S3 Intelligent          | 无         | 无     | 99.9%  | 访问模式不明           |
| S3 Standard-IA          | 30天       | 有     | 99.9%  | 低频访问               |
| S3 One Zone-IA          | 30天       | 有     | 99.5%  | 可重建的低频数据       |
| S3 Glacier Instant      | 90天       | 有     | 99.9%  | 需即时检索的归档       |
| S3 Glacier Flexible     | 90天       | 有     | 99.99% | 归档（分钟-小时恢复）  |
| S3 Glacier Deep Archive | 180天      | 有     | 99.99% | 长期归档（12小时恢复） |

### 2.3 S3 数据一致性

S3 提供**强一致性**读写：

- 写后读一致性：新对象写入后立即可读
- 覆盖写后读一致性：覆盖已有对象后立即可读
- 删除一致性：删除后立即不可读

### 2.4 S3 性能优化

**多部分上传**：

```mermaid
flowchart LR
    P1[Part 1 5MB] --> S3[S3]
    P2[Part 2 5MB] --> S3
    P3[Part 3 5MB] --> S3
    PN[Part N 5MB] --> S3
    CM[Complete Multipart Upload] --> S3
```

- 最小分片大小：5MB（最后一个分片除外）
- 最大分片数量：10,000
- 最大对象大小：5TB

**S3 Transfer Acceleration**：利用 CloudFront 边缘节点加速跨区域上传。

**S3 请求速率**：

$$
\text{单前缀请求限制} = 3{,}500 \text{ PUT/COPY/POST/DELETE/s} + 5{,}500 \text{ GET/s}
$$

通过前缀分散可线性提升吞吐：

$$
\text{总吞吐} = \text{前缀数} \times \text{单前缀限制}
$$

### 2.5 S3 安全

- **服务端加密**：SSE-S3（AES-256）、SSE-KMS（客户管理密钥）、SSE-C（客户提供密钥）
- **客户端加密**：上传前在客户端加密
- **预签名 URL**：临时授权访问
- **Bucket Policy**：细粒度访问控制
- **VPC Endpoint**：私有网络访问，不经公网
- **Object Lock**：WORM（一次写多次读）合规保留

## 3. 块存储

### 3.1 EBS（Elastic Block Store）

EBS 是 AWS 的块存储服务，作为 EC2 实例的持久化磁盘：

| 卷类型            | 最大 IOPS | 最大吞吐   | 最大容量 | 适用场景     |
| ----------------- | --------- | ---------- | -------- | ------------ |
| gp3               | 16,000    | 1,000 MB/s | 16 TB    | 通用 SSD     |
| io2 Block Express | 256,000   | 4,000 MB/s | 64 TB    | 高性能数据库 |
| st1               | 500       | 500 MB/s   | 16 TB    | 吞吐优化 HDD |
| sc1               | 250       | 250 MB/s   | 16 TB    | 冷 HDD       |

**gp3 独立配置 IOPS 和吞吐**：

$$
\text{IOPS} = \min(16{,}000, \text{配置值})
$$

$$
\text{吞吐} = \min(1{,}000 \text{ MB/s}, \text{配置值})
$$

$$
\text{吞吐上限} = \frac{\text{IOPS} \times \text{块大小}}{1024} \text{ MB/s}
$$

### 3.2 EBS 快照

EBS 快照是增量备份，存储在 S3 中：

```
全量快照1:  [A][B][C][D]        ← 包含所有数据块
增量快照2:  [B'][E]             ← 仅包含变更块
增量快照3:  [C'][F]             ← 仅包含变更块

恢复快照3:  [A][B'][C'][D][E][F] ← 合并所有快照的块
```

快照成本：

$$
\text{快照存储费} = \text{增量数据量} \times \text{单价/GB}
$$

### 3.3 多挂载卷

io2 卷支持多实例同时挂载（Multi-Attach）：

- 最多 16 个实例同时读写
- 需要集群文件系统（如 OCFS2、GFS2）
- 适用于 Oracle RAC、SAP HANA 等共享存储场景

## 4. 文件存储

### 4.1 EFS（Elastic File System）

AWS EFS 是托管 NFS 文件系统：

```mermaid
flowchart TD
    subgraph EFS[EFS]
        FS[文件系统 自动伸缩<br/>/data/<br/>app1 / app2 / shared]
    end
    E1[EC2-1 mount] --> FS
    E2[EC2-2 mount] --> FS
    E3[ECS mount] --> FS
```

**EFS 存储类**：

| 存储类                 | 价格 | 访问模式        |
| ---------------------- | ---- | --------------- |
| Standard               | 标准 | 频繁访问        |
| Infrequent Access (IA) | 低   | 月访问 < 1 次   |
| Archive                | 极低 | 年访问 < 1-2 次 |

**EFS 性能模式**：

- **通用用途**：默认，低延迟，适合 Web 服务、CMS
- **最大 I/O**：高并发，延迟略高，适合大数据分析、媒体处理

**EFS 吞吐模式**：

- **突发吞吐**：基于文件系统大小分配基准和突发额度
- **预置吞吐**：独立于存储量指定吞吐量

$$
\text{基准吞吐} = \text{存储量(GB)} \times 0.05 \text{ MB/s/GB}
$$

### 4.2 FSx

AWS FSx 提供专用文件系统：

| 类型                 | 协议          | 适用场景     |
| -------------------- | ------------- | ------------ |
| FSx for Windows      | SMB           | Windows 应用 |
| FSx for Lustre       | POSIX         | HPC/机器学习 |
| FSx for NetApp ONTAP | NFS/SMB/iSCSI | 企业级多协议 |
| FSx for OpenZFS      | NFS           | 高性能 Linux |

### 4.3 阿里云 NAS

阿里云文件存储 NAS：

- **通用型 NAS**：NFS/SMB 协议，容量型/性能型/高级型
- **极速型 NAS**：基于 NVMe，亚毫秒延迟
- **CPFS**：并行文件系统，HPC 场景

## 5. 数据生命周期管理

### 5.1 生命周期策略

S3 生命周期规则自动转换对象存储类：

```json
{
  "Rules": [
    {
      "ID": "TransitionToIA",
      "Status": "Enabled",
      "Transitions": [
        { "Days": 30, "StorageClass": "STANDARD_IA" },
        { "Days": 90, "StorageClass": "GLACIER" },
        { "Days": 365, "StorageClass": "DEEP_ARCHIVE" }
      ],
      "Expiration": { "Days": 2555 }
    }
  ]
}
```

生命周期转换路径：

```
Standard → Standard-IA (30天) → Glacier (90天) → Deep Archive (365天) → 过期删除 (2555天)
```

### 5.2 成本优化分析

不同存储类的月度成本（以 1TB 数据为例）：

$$
C_{\text{Standard}} = 1000 \text{ GB} \times \$0.023/\text{GB} = \$23.00
$$

$$
C_{\text{IA}} = 1000 \text{ GB} \times \$0.0125/\text{GB} = \$12.50
$$

$$
C_{\text{Glacier}} = 1000 \text{ GB} \times \$0.004/\text{GB} = \$4.00
$$

$$
C_{\text{Deep Archive}} = 1000 \text{ GB} \times \$0.00099/\text{GB} = \$0.99
$$

### 5.3 智能分层

S3 Intelligent-Tiering 自动监控访问模式并移动数据：

```mermaid
flowchart TD
    H[频繁访问层] -->|30天未访问| W[低频访问层] -->|访问时自动回热| H
    W -->|30天| A[归档即时访问层] -->|90天| D[归档灵活访问层] -->|180天| DD[深度归档访问层]
```

每月监控和自动化费用：每 1,000 个对象 $0.0025。

## 6. 跨区域复制与一致性

### 6.1 S3 跨区域复制（CRR）

```mermaid
flowchart LR
    A[源区域 Bucket A<br/>us-east-1] -->|复制 异步| B[目标区域 Bucket B<br/>eu-west-1]
```

CRR 配置要求：

- 源和目标 Bucket 均需开启版本控制
- IAM 角色需授予复制权限
- 可指定存储类转换规则
- 复制时间控制（RTC）：15 分钟内完成 99.99% 的对象

### 6.2 双向复制与冲突解决

双向复制场景下，同一对象可能同时被修改：

$$
\text{冲突解决策略} = \begin{cases} \text{最新版本优先} & \text{基于时间戳} \\ \text{源区域优先} & \text{配置优先级} \end{cases}
$$

### 6.3 数据一致性验证

跨区域复制后的数据一致性验证方法：

| 方法                   | 精度   | 开销 | 适用场景 |
| ---------------------- | ------ | ---- | -------- |
| S3 Replication Metrics | 统计级 | 低   | 日常监控 |
| S3 Batch Operations    | 对象级 | 中   | 定期校验 |
| 自定义校验脚本         | 字节级 | 高   | 合规审计 |

S3 Replication Metrics 关键指标：

- **ReplicationLatency**：源对象复制到目标的时间
- **BytesPendingReplication**：待复制的字节数
- **OperationsPendingReplication**：待复制的操作数

<!-- ============ 文档分隔线：034-cloud-computing/015-KubernetesNetwork.md ============ -->

## 1. Kubernetes 网络模型

### 1.1 基本要求

| 要求             | 描述               |
| ---------------- | ------------------ |
| Pod 间直接通信   | 无需 NAT           |
| Node 与 Pod 通信 | 无需 NAT           |
| Pod 自身 IP      | 每个 Pod 有独立 IP |

### 1.2 三层网络

```mermaid
flowchart TD
    I[Ingress 网络<br/>外部流量入口] --> S[Service 网络<br/>虚拟 IP ClusterIP]
    S --> P[Pod 网络<br/>容器 IP]
    P --> N[Node 网络<br/>物理网络]
```

## 2. CNI 插件

### 2.1 常见 CNI

| 插件    | 模式          | 特点           |
| ------- | ------------- | -------------- |
| Calico  | BGP/VXLAN     | 网络策略强     |
| Flannel | VXLAN/host-gw | 简单易用       |
| Cilium  | eBPF          | 高性能、可观测 |
| Weave   | VXLAN         | 自动拓扑       |
| Antrea  | OVS           | VMware 生态    |

### 2.2 Calico 网络模式

| 模式  | 描述          | 性能 |
| ----- | ------------- | ---- |
| BGP   | 直接路由      | 高   |
| VXLAN | Overlay 封装  | 中   |
| IPIP  | IP-in-IP 封装 | 中   |

### 2.3 Cilium 优势

- 基于 eBPF，内核级数据路径
- 无需 iptables
- 支持 L3-L7 网络策略
- 内置可观测性（Hubble）

## 3. Pod 网络

### 3.1 同节点 Pod 通信

```
Pod A → veth pair → cni0 (bridge) → veth pair → Pod B
```

### 3.2 跨节点 Pod 通信

```
Pod A → veth → cni0 → 路由 → 物理网络 → 路由 → cni0 → veth → Pod B
```

### 3.3 Pause 容器

每个 Pod 有一个 Pause 容器，负责：

- 创建网络命名空间
- 维持 Pod 网络
- 共享网络栈

## 4. Service 网络

### 4.1 kube-proxy 工作原理

```
Client → ClusterIP → iptables/IPVS → Pod IP
```

### 4.2 iptables 模式

```bash
# 随机选择后端 Pod
-A KUBE-SERVICES -d 10.96.0.1/32 -j KUBE-SVC-XXX
-A KUBE-SVC-XXX -m statistic --probability 0.33 -j KUBE-SEP-POD1
-A KUBE-SVC-XXX -m statistic --probability 0.5 -j KUBE-SEP-POD2
-A KUBE-SVC-XXX -j KUBE-SEP-POD3
```

### 4.3 IPVS 模式

| 调度算法 | 描述       |
| -------- | ---------- |
| rr       | 轮询       |
| lc       | 最少连接   |
| wrr      | 加权轮询   |
| sh       | 源地址哈希 |

## 5. Ingress

### 5.1 Ingress 架构

```
Internet → Ingress Controller → Service → Pod
```

### 5.2 Ingress 配置

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: 'true'
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - example.com
      secretName: tls-secret
  rules:
    - host: example.com
      http:
        paths:
          - path: /api
            pathType: Prefix
            backend:
              service:
                name: api-service
                port:
                  number: 8080
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-service
                port:
                  number: 80
```

### 5.3 Ingress Controller 对比

| Controller    | 特点               |
| ------------- | ------------------ |
| NGINX Ingress | 最广泛使用         |
| Traefik       | 自动发现、配置简单 |
| Envoy/Istio   | 服务网格集成       |
| Kong          | API 网关功能       |

## 6. NetworkPolicy

### 6.1 概念

NetworkPolicy 控制 Pod 间的网络访问，类似防火墙规则。

### 6.2 配置示例

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              env: production
        - podSelector:
            matchLabels:
              app: web
      ports:
        - port: 8080
          protocol: TCP
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: database
      ports:
        - port: 5432
          protocol: TCP
```

### 6.3 默认策略

```yaml
# 默认拒绝所有入站
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
spec:
  podSelector: {}
  policyTypes:
    - Ingress
```

> 注意：NetworkPolicy 需要支持它的 CNI 插件（Calico、Cilium 等），Flannel 不支持。

<!-- ============ 文档分隔线：034-cloud-computing/016-CloudNetworkService.md ============ -->

## 1. 虚拟私有云（VPC）

### 1.1 VPC 核心概念

VPC（Virtual Private Cloud）是云上的隔离虚拟网络，用户可自定义 IP 地址范围、子网、路由表和网关：

```mermaid
flowchart TD
    subgraph VPC[VPC 10.0.0.0/16]
        subgraph Pub[公有子网 10.0.1.0/24]
            ALB[ALB]
            BS[Bastion]
        end
        subgraph Priv[私有子网 10.0.2.0/24]
            APP[App]
            DB[DB]
        end
        IGW[Internet Gateway]
    end
```

### 1.2 子网设计

**三层架构子网规划**：

| 层级    | 子网     | CIDR        | 可公网访问 | 用途              |
| ------- | -------- | ----------- | ---------- | ----------------- |
| Web 层  | 公有子网 | 10.0.1.0/24 | 是         | ALB、NAT、Bastion |
| App 层  | 私有子网 | 10.0.2.0/24 | 否         | 应用服务器        |
| Data 层 | 私有子网 | 10.0.3.0/24 | 否         | 数据库、缓存      |

**CIDR 容量计算**：

$$
\text{可用 IP 数} = 2^{(32 - \text{前缀长度})} - 5
$$

其中减去 5 个保留地址：网络地址、广播地址、网关地址、DNS 地址、广播地址。

### 1.3 安全组与网络 ACL

| 特性 | 安全组                     | 网络 ACL                 |
| ---- | -------------------------- | ------------------------ |
| 层级 | 实例级                     | 子网级                   |
| 状态 | 有状态（自动放行返回流量） | 无状态（需显式放行双向） |
| 规则 | 仅允许规则                 | 允许 + 拒绝规则          |
| 评估 | 全部规则评估               | 按规则编号顺序评估       |
| 默认 | 拒绝所有入站，允许所有出站 | 允许所有入站和出站       |

**最小权限安全组设计**：

```
ALB 安全组:
  入站: 80, 443 from 0.0.0.0/0
  出站: 8080 to App 安全组

App 安全组:
  入站: 8080 from ALB 安全组
  出站: 3306 to DB 安全组, 6379 to Redis 安全组

DB 安全组:
  入站: 3306 from App 安全组
  出站: 无
```

## 2. 负载均衡

### 2.1 负载均衡类型

```mermaid
flowchart LR
    L4[L4 传输层<br/>NLB<br/>TCP/UDP/TLS<br/>超低延迟 百万RPS 保留源IP]
    L7[L7 应用层<br/>ALB<br/>HTTP/HTTPS/gRPC<br/>路径/主机路由 SSL 终止 认证/速率限制]
```

### 2.2 ALB 路由规则

ALB 基于请求内容进行路由：

```mermaid
flowchart TD
    R1[IF Host = api.example.com AND Path = /users/* → Forward to user-service]
    R2[IF Host = api.example.com AND Path = /orders/* → Forward to order-service]
    R3[IF Path = /static/* → Redirect to CDN]
    R4[IF Header[X-Canary] = true → Forward to canary-service 10%]
```

### 2.3 负载均衡算法

| 算法       | 描述               | 适用场景 |
| ---------- | ------------------ | -------- |
| 轮询       | 依次分配           | 均匀负载 |
| 最少连接   | 分配给连接数最少的 | 长连接   |
| IP 哈希    | 基于客户端 IP 哈希 | 会话保持 |
| 加权轮询   | 按权重分配         | 异构实例 |
| 随机       | 随机选择           | 简单场景 |
| 一致性哈希 | 最小化哈希变更     | 缓存亲和 |

一致性哈希虚拟节点数选择：

$$
\text{虚拟节点数} = \frac{\text{物理节点数} \times 150}{\text{允许的负载偏差百分比}}
$$

## 3. CDN 与边缘计算

### 3.1 CDN 工作原理

```mermaid
flowchart TD
    R[请求] --> H{命中缓存?}
    H -- 是 --> RET[直接返回]
    H -- 未命中 --> O[回源获取] --> C[缓存] --> RET
```

**CDN 关键指标**：

$$
\text{缓存命中率} = \frac{\text{缓存命中请求数}}{\text{总请求数}} \times 100\%
$$

$$
\text{目标缓存命中率} > 95\%
$$

### 3.2 CloudFront 功能

| 功能                   | 描述                        |
| ---------------------- | --------------------------- |
| Lambda@Edge            | 在边缘节点运行 Lambda 函数  |
| CloudFront Functions   | 轻量级 JS 函数（<1ms 启动） |
| Field Level Encryption | 敏感字段端到端加密          |
| Origin Access Control  | 限制 S3 仅允许 CDN 访问     |
| Real-time Logs         | 实时访问日志流              |
| Signed URL/Cookie      | 付费内容保护                |

### 3.3 边缘计算

边缘计算将计算推到离用户更近的位置：

```mermaid
flowchart LR
    IoT[IoT<br/>&lt;1ms] --> PoP[CDN PoP<br/>&lt;10ms] --> Reg[Regional<br/>&lt;50ms] --> Cen[Central<br/>&lt;100ms]
```

边缘计算应用场景：

- **IoT 网关**：本地数据预处理与过滤
- **实时视频分析**：边缘推理，减少回传带宽
- **AR/VR 渲染**：低延迟渲染
- **游戏加速**：就近匹配与计算

## 4. DNS 服务

### 4.1 Route 53

AWS Route 53 是高可用的 DNS 服务：

**路由策略**：

| 策略        | 描述         | 适用场景           |
| ----------- | ------------ | ------------------ |
| Simple      | 单一记录     | 单服务器           |
| Weighted    | 按权重分配   | A/B 测试、灰度发布 |
| Latency     | 延迟最优路由 | 多区域部署         |
| Failover    | 主备切换     | 灾难恢复           |
| Geolocation | 地理位置路由 | 本地化内容         |
| Multi-value | 返回多个值   | 简单负载均衡       |

### 4.2 全局流量管理

多区域部署的 DNS 策略：

```mermaid
flowchart TD
    T0["用户请求 → Route 53"]
    T1["健康检查: 区域 A 健康? → 延迟路由"]
    T2["us-east-1: 20ms"]
    T3["eu-west-1: 80ms"]
    T4["选择最低延迟区域 → 返回 us-east-1 IP"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T3 --> T4
```

### 4.3 DNS 安全

- **DNSSEC**：DNS 响应签名验证，防止 DNS 欺骗
- **DNS over HTTPS (DoH)**：加密 DNS 查询
- **DNS over TLS (DoT)**：TLS 加密 DNS 查询
- **域名锁定**：防止未授权的域名转移

## 5. 专线与 VPN

### 5.1 VPN 连接

**Site-to-Site VPN**：IPsec 隧道连接本地网络与 VPC

```mermaid
flowchart LR
    DC[本地数据中心] <-->|IPsec 隧道| VPN[VPN Gateway VPC]
```

- 两条隧道自动冗余
- 带宽：1.25 Gbps/隧道
- 加密：AES-256
- 延迟：受公网影响，不稳定

**Client VPN**：OpenVPN 客户端连接 VPC

### 5.2 专线连接（Direct Connect）

专线提供专用物理连接：

```mermaid
flowchart LR
    DC[本地数据中心] <-->|专用光纤| DX[DX 位置 Colocation] <-->|专用连接| VPC[VPC]
```

| 带宽          | 延迟     | 稳定性 | 成本 |
| ------------- | -------- | ------ | ---- |
| 1/10/100 Gbps | 低且稳定 | 高     | 高   |

**专线 + VPN 双路径架构**：

```mermaid
flowchart TD
    DC[本地数据中心] -->|专线 主路径 低延迟| V1[VPC]
    DC -->|VPN 备份路径 高可用| V1
```

### 5.3 VPC 对等连接与中转网关

**VPC Peering**：点对点连接两个 VPC

```mermaid
flowchart LR
    A[VPC A] <-->|Peering| B[VPC B]
    B <-->|Peering| C[VPC C]
    A -.->|不支持传递路由| C
```

**Transit Gateway**：中心化网络枢纽

```mermaid
flowchart TD
    TG[Transit Gateway] --> A[VPC A 支持传递路由]
    TG --> B[VPC B]
    TG --> C[VPC C]
```

Transit Gateway 支持路由表、多区域对等、IPsec VPN 附件。

## 6. 网络架构设计

### 6.1 多账户网络架构

企业级多账户网络拓扑：

```mermaid
flowchart TD
    TG[Transit Gateway<br/>中心化网络枢纽] --> VPC_A[VPC A<br/>支持传递路由]
    TG --> VPC_B[VPC B]
    TG --> VPC_C[VPC C]
```

### 6.2 网络分段与零信任

零信任网络架构原则：

- **永不信任，始终验证**：每次访问都需认证授权
- **最小权限**：仅授予完成任务所需的最小权限
- **微分段**：细粒度网络隔离
- **持续监控**：实时检测异常行为

### 6.3 网络性能优化

**TCP 优化**：

$$
\text{BDP} = \text{带宽} \times \text{RTT}
$$

$$
\text{最优窗口大小} = \frac{\text{BDP}}{\text{MSS}}
$$

例如：10 Gbps 链路，RTT = 10ms，MSS = 1460 字节：

$$
\text{BDP} = 10 \times 10^9 \times 0.01 = 100 \text{ MB}
$$

$$
\text{窗口大小} = \frac{100 \times 10^6}{1460} \approx 68{,}493
$$

**网络优化清单**：

- [ ] 启用 TCP 窗口缩放（Window Scaling）
- [ ] 调整 TCP 缓冲区大小
- [ ] 启用 ECN（Explicit Congestion Notification）
- [ ] 使用 jumbo frame（MTU 9001）
- [ ] 启用 TCP Fast Open
- [ ] 选择合适的 TCP 拥塞控制算法（BBR / Cubic）

<!-- ============ 文档分隔线：034-cloud-computing/017-KubernetesStorage.md ============ -->

## 1. 存储概述

### 1.1 存储分层

```mermaid
flowchart TD
    App[应用 Pod] --> PVC[PVC 声明]
    PVC --> PV[PV 卷]
    PV --> SC[StorageClass 类]
    SC --> CSI[CSI 驱动]
    CSI --> Backend[后端存储]
```

### 1.2 存储类型

| 类型      | 描述     | 生命周期 |
| --------- | -------- | -------- |
| emptyDir  | 临时目录 | 随 Pod   |
| hostPath  | 节点路径 | 独立     |
| PV/PVC    | 持久卷   | 独立     |
| ConfigMap | 配置     | 独立     |
| Secret    | 敏感数据 | 独立     |

## 2. PV 与 PVC

### 2.1 PersistentVolume (PV)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-nfs
spec:
  capacity:
    storage: 50Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: nfs
  nfs:
    server: 10.0.0.100
    path: /data/share
```

### 2.2 PersistentVolumeClaim (PVC)

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: fast-ssd
```

### 2.3 访问模式

| 模式             | 缩写 | 描述                 |
| ---------------- | ---- | -------------------- |
| ReadWriteOnce    | RWO  | 单节点读写           |
| ReadOnlyMany     | ROX  | 多节点只读           |
| ReadWriteMany    | RWX  | 多节点读写           |
| ReadWriteOncePod | RWOP | 单 Pod 读写（1.27+） |

### 2.4 回收策略

| 策略    | 描述                 |
| ------- | -------------------- |
| Retain  | 保留数据，需手动清理 |
| Delete  | 删除 PV 和后端存储   |
| Recycle | 已废弃               |

### 2.5 绑定流程

```
PVC 创建 → 控制器匹配 PV → 绑定 → Pod 使用 PVC
```

## 3. StorageClass

### 3.1 概念

StorageClass 定义存储"类"，支持动态供给。

### 3.2 配置示例

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  iopsPerGB: '50'
  throughput: '250'
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
```

### 3.3 动态供给流程

```
PVC 创建（指定 StorageClass）→
  Provisioner 检测 →
    自动创建 PV →
      PVC 绑定 PV →
        Pod 使用
```

### 3.4 卷绑定模式

| 模式                 | 描述              |
| -------------------- | ----------------- |
| Immediate            | 立即绑定          |
| WaitForFirstConsumer | 等 Pod 调度后绑定 |

## 4. CSI（容器存储接口）

### 4.1 概念

CSI 是 Kubernetes 存储插件的标准接口，使存储供应商无需修改 Kubernetes 代码。

### 4.2 CSI 架构

```
Kubernetes → CSI Sidecar → CSI Driver → 存储后端
```

### 4.3 常见 CSI 驱动

| 驱动                      | 后端存储            |
| ------------------------- | ------------------- |
| ebs.csi.aws.com           | AWS EBS             |
| disk.csi.azure.com        | Azure Disk          |
| pd.csi.storage.gke.io     | GCP Persistent Disk |
| disk.csi.alibabacloud.com | 阿里云云盘          |
| csi-hostpath              | 本地存储（测试）    |
| ceph-csi                  | Ceph RBD/CephFS     |
| nfs.csi.k8s.io            | NFS                 |

## 5. 临时存储

### 5.1 emptyDir

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cache-pod
spec:
  containers:
    - name: app
      image: nginx
      volumeMounts:
        - name: cache
          mountPath: /cache
  volumes:
    - name: cache
      emptyDir:
        medium: Memory # 可选：使用内存
        sizeLimit: 256Mi
```

### 5.2 hostPath

```yaml
volumes:
  - name: data
    hostPath:
      path: /data/app
      type: DirectoryOrCreate
```

> 注意：hostPath 不推荐生产使用，存在安全和调度问题。

## 6. 存储最佳实践

| 实践                 | 描述             |
| -------------------- | ---------------- |
| 使用 PVC 而非直接 PV | 解耦应用与存储   |
| 使用 StorageClass    | 动态供给         |
| WaitForFirstConsumer | 避免跨区绑定     |
| 数据备份             | 定期快照         |
| 加密存储             | 启用加密         |
| 监控                 | 监控存储使用率   |
| 清理策略             | 合理设置回收策略 |

<!-- ============ 文档分隔线：034-cloud-computing/018-CloudSecurityService.md ============ -->

## 1. 共享责任模型

### 1.1 模型概述

云安全遵循**共享责任模型**，云厂商和客户各负责不同层面的安全：

```mermaid
flowchart TD
    subgraph Shared[责任共担]
        I[IaaS<br/>云厂商：物理安全、基础设施、网络<br/>客户：OS、应用、数据]
        P[PaaS<br/>云厂商：物理、基础设施、OS、运行时<br/>客户：应用代码、数据]
        S[SaaS<br/>云厂商：几乎全部<br/>客户：数据、访问控制]
    end
```

### 1.2 各云厂商模型差异

| 责任领域     | AWS    | Azure  | 阿里云 |
| ------------ | ------ | ------ | ------ |
| 物理数据中心 | 云厂商 | 云厂商 | 云厂商 |
| 网络基础设施 | 云厂商 | 云厂商 | 云厂商 |
| 虚拟化层     | 云厂商 | 云厂商 | 云厂商 |
| 操作系统     | 客户   | 客户   | 客户   |
| 应用与数据   | 客户   | 客户   | 客户   |
| 身份与访问   | 客户   | 客户   | 客户   |

## 2. 身份与访问管理（IAM）

### 2.1 IAM 核心概念

```mermaid
flowchart LR
    P[Principal 谁] --> R[Role 角色] --> PL[Policy 权限] --> Res[Resource 什么资源]
```

认证（AuthN）：你是谁？授权（AuthZ）：你能做什么？审计（Audit）：你做了什么？

### 2.2 IAM 策略

**基于身份的策略**（附加到用户/角色）：

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["10.0.0.0/8"]
        },
        "StringEquals": {
          "s3:x-amz-server-side-encryption": "aws:kms"
        }
      }
    }
  ]
}
```

**基于资源的策略**（附加到资源，如 S3 Bucket Policy）。

### 2.3 最小权限原则

最小权限实施策略：

1. **从拒绝所有开始**：默认拒绝，逐步放行
2. **使用 AWS Access Analyzer**：识别过度权限
3. **权限边界（Permissions Boundary）**：设置角色权限上限
4. **服务控制策略（SCP）**：组织级权限限制
5. **会话策略**：临时会话的权限缩小

### 2.4 联合身份

```mermaid
flowchart LR
    IdP[企业 IdP AD/LDAP] -->|SAML/OIDC 联合认证| IAM[IAM Role 临时凭证] --> AWS[AWS 资源]
```

联合身份优势：

- 无需管理 IAM 用户
- 使用现有企业身份体系
- 临时凭证自动轮换
- 集中审计

### 2.5 临时安全凭证

STS（Security Token Service）提供临时凭证：

$$
\text{临时凭证有效期} = \min(\text{请求时长}, \text{角色最大会话时长})
$$

| 凭证类型           | 有效期    | 用途       |
| ------------------ | --------- | ---------- |
| AssumeRole         | 15min-12h | 跨账户访问 |
| GetFederationToken | 15min-36h | 联合身份   |
| GetSessionToken    | 15min-36h | MFA 场景   |

## 3. 数据加密与密钥管理

### 3.1 加密层次

```mermaid
flowchart TD
    A[应用层加密<br/>应用代码实现，最灵活] --> S[存储层加密<br/>数据库/文件系统透明加密]
    S --> D[磁盘层加密<br/>EBS 加密，操作系统不可见]
    D --> N[网络层加密<br/>TLS/IPsec，传输中保护]
```

### 3.2 KMS（Key Management Service）

KMS 提供密钥的创建、管理和审计：

```mermaid
flowchart TD
    AWS[AWS 托管密钥 aws/*] --> HSM[HSM 硬件安全模块<br/>密钥在 HSM 中生成和存储]
    CUST[客户托管密钥 alias/*] --> HSM
    BYOK[客户自带密钥 ext/*] --> HSM
```

**信封加密**：

KMS 使用信封加密保护数据，避免每次请求都访问 KMS：

```
1. 请求数据密钥 → KMS 返回明文 DK + 密文 DK
2. 使用明文 DK 加密数据
3. 存储密文 DK + 密文数据
4. 丢弃明文 DK

解密:
1. 发送密文 DK → KMS 解密 → 返回明文 DK
2. 使用明文 DK 解密数据
```

信封加密性能优势：

$$
\text{KMS 调用次数} = \frac{\text{数据量}}{\text{4KB}} \text{ (直接加密)}
$$

$$
\text{KMS 调用次数} = 1 \text{ (信封加密)}
$$

### 3.3 密钥轮换

- **自动轮换**：每年自动轮换（AWS 托管密钥）
- **按需轮换**：手动创建新密钥版本
- **别名轮换**：更新别名指向的密钥

密钥轮换不影响已加密数据（旧密钥版本仍可解密）。

## 4. 网络安全

### 4.1 深度防御

```mermaid
flowchart TD
    B[边界防护<br/>WAF / Shield / CloudFront] --> N[网络防护<br/>VPC / 安全组 / NACL / VPC Endpoint]
    N --> H[主机防护<br/>OS 加固 / 漏洞修补 / 运行时保护]
    H --> A[应用防护<br/>输入验证 / 认证授权 / 会话管理]
    A --> D[数据防护<br/>加密 / 脱敏 / 访问控制]
```

### 4.2 WAF（Web Application Firewall）

WAF 保护 Web 应用免受常见攻击：

| 规则类型 | 防护内容         |
| -------- | ---------------- |
| SQL 注入 | 恶意 SQL 语句    |
| XSS      | 跨站脚本攻击     |
| RFC 违规 | 不合规 HTTP 请求 |
| 机器人   | 自动化攻击       |
| IP 信誉  | 已知恶意 IP      |
| 速率限制 | DDoS 防护        |

**WAF 规则优先级**：

```
规则1 (Allow: 已知好IP) → 规则2 (Block: 已知坏IP) → 规则3 (Rate Limit) → 规则4 (SQLi检测) → 默认动作
```

### 4.3 DDoS 防护

| 服务                | 防护层级 | 特点                          |
| ------------------- | -------- | ----------------------------- |
| AWS Shield Standard | L3/L4    | 自动免费防护                  |
| AWS Shield Advanced | L3/L4/L7 | 付费，$3000/月，DDoS 响应团队 |
| CloudFront          | L7       | 分布式吸收流量                |
| Route 53            | DNS      | DNS 层防护                    |
| WAF                 | L7       | 应用层规则                    |

DDoS 攻击类型与防御：

$$
\text{攻击流量} = \text{攻击包速率} \times \text{包大小}
$$

| 攻击类型   | 层级 | 防御策略              |
| ---------- | ---- | --------------------- |
| SYN Flood  | L4   | SYN Cookie、限速      |
| UDP Flood  | L4   | 限速、Geo 屏蔽        |
| DNS 放大   | L3   | DNSSEC、限速          |
| HTTP Flood | L7   | WAF 速率限制、CAPTCHA |
| Slowloris  | L7   | 连接超时、并发限制    |

### 4.4 VPC Endpoint

VPC Endpoint 允许私有网络访问云服务，不经公网：

**Interface Endpoint**（PrivateLink）：

```
VPC ── ENI ── PrivateLink ── 云服务
       (私有IP)
```

**Gateway Endpoint**（S3/DynamoDB 专用）：

```
VPC ── 路由表 ── Gateway Endpoint ── S3/DynamoDB
       (免费)
```

## 5. 合规与审计

### 5.1 合规框架

| 框架      | 行业 | 核心要求               |
| --------- | ---- | ---------------------- |
| SOC 2     | 通用 | 安全性、可用性、机密性 |
| PCI DSS   | 支付 | 卡数据保护             |
| HIPAA     | 医疗 | 健康信息保护           |
| GDPR      | 隐私 | 个人数据保护           |
| ISO 27001 | 通用 | 信息安全管理体系       |
| 等保 2.0  | 中国 | 网络安全等级保护       |

### 5.2 AWS Config

Config 持续记录资源配置变更，评估合规性：

```mermaid
flowchart TD
    RC[资源变更] --> CR[Config Recorder] --> CI[配置项]
    CR --> RULE[合规规则]
    RULE --> COMP[COMPLIANT]
    RULE --> NON[NON_COMPLIANT] --> FIX[自动修正]
```

常用合规规则：

- 加密 EBS 卷
- S3 Bucket 禁止公开访问
- 安全组不允许 22/3389 端口入站
- IAM 用户必须启用 MFA
- RDS 实例必须开启加密

### 5.3 CloudTrail

CloudTrail 记录所有 API 调用，用于安全审计：

```
API 调用 → CloudTrail → S3 (长期存储)
                      → CloudWatch Logs (实时监控)
                      → EventBridge (事件驱动)
```

关键审计场景：

- 谁创建了/删除了资源？
- 何时修改了 IAM 策略？
- 哪些 API 调用失败？
- 是否有异常的登录行为？

## 6. 安全运营与事件响应

### 6.1 安全运营中心

```mermaid
flowchart LR
    D[检测<br/>GuardDuty/SecurityHub/Config] --> A[分析<br/>上下文/取证] --> C[遏制<br/>隔离/撤销权限]
    C --> E[根除<br/>修补/清除恶意] --> R[恢复<br/>验证/恢复服务] --> X[复盘<br/>改进/文档/策略]
```

### 6.2 GuardDuty

GuardDuty 是托管的威胁检测服务：

| 检测类型      | 示例                    |
| ------------- | ----------------------- |
| 异常 API 调用 | 来自异常地域的 API 调用 |
| 凭证泄露      | GitHub 上发现 AWS 凭证  |
| 恶意 IP 交互  | 与已知 C2 服务器通信    |
| 挖矿行为      | 异常高的 CPU 使用 EC2   |
| 暴力破解      | 多次登录失败            |
| 权限提升      | 异常的 IAM 操作         |

### 6.3 自动化响应

安全事件自动化响应架构：

```mermaid
flowchart LR
    GD[GuardDuty 发现] --> EB[EventBridge] --> L[Lambda 自动动作]
    L --> A1[撤销 IAM 凭证]
    L --> A2[隔离 EC2 实例]
    L --> A3[阻止恶意 IP]
    L --> A4[通知安全团队]
    L --> A5[创建 JIRA 工单]
```

### 6.4 安全基线检查

云账户安全基线检查清单：

**身份与访问**：

- [ ] Root 账户无 AK/SK
- [ ] Root 账户启用 MFA
- [ ] 所有 IAM 用户启用 MFA
- [ ] 无 IAM 访问密钥超过 90 天
- [ ] 最小权限策略

**网络**：

- [ ] 安全组不允许 0.0.0.0/0 入站
- [ ] VPC 流日志已开启
- [ ] S3 Bucket 禁止公开访问

**数据保护**：

- [ ] EBS 卷加密
- [ ] RDS 实例加密
- [ ] S3 对象加密
- [ ] CloudTrail 日志加密

**监控**：

- [ ] CloudTrail 全区域启用
- [ ] Config 合规规则配置
- [ ] GuardDuty 启用
- [ ] 安全告警通知配置

<!-- ============ 文档分隔线：034-cloud-computing/019-HelmPackageManagement.md ============ -->

## 1. Helm 概述

### 1.1 什么是 Helm

Helm 是 Kubernetes 的包管理器，将应用定义为 Chart，实现一键部署和版本管理。

### 1.2 核心概念

| 概念       | 描述                  |
| ---------- | --------------------- |
| Chart      | 应用包（模板+默认值） |
| Release    | Chart 的部署实例      |
| Repository | Chart 仓库            |
| Values     | 配置值                |

### 1.3 Helm 3 vs Helm 2

| 对比项       | Helm 2           | Helm 3          |
| ------------ | ---------------- | --------------- |
| Tiller       | 需要             | 不需要          |
| 安全模型     | Tiller 权限      | kubeconfig 权限 |
| Release 存储 | ConfigMap/Secret | Secret          |
| 命名空间     | Tiller 全局      | 按命名空间      |

## 2. Chart 结构

### 2.1 目录结构

```mermaid
flowchart TD
    T0["my-chart/"]
    T1["Chart.yaml          # Chart 元数据"]
    T2["values.yaml         # 默认值"]
    T3["charts/             # 依赖 Chart"]
    T4["templates/          # 模板文件"]
    T5["deployment.yaml"]
    T6["service.yaml"]
    T7["ingress.yaml"]
    T8["configmap.yaml"]
    T9["_helpers.tpl    # 模板辅助"]
    T10["NOTES.txt       # 安装说明"]
    T11["templates/tests/    # 测试模板"]
    T12[".helmignore         # 忽略文件"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T10 --> T11
    T10 --> T12
```

### 2.2 Chart.yaml

```yaml
apiVersion: v2
name: my-app
description: My application Helm chart
type: application
version: 1.0.0 # Chart 版本
appVersion: '2.1.0' # 应用版本
dependencies:
  - name: redis
    version: '17.0.0'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: redis.enabled
```

### 2.3 values.yaml

```yaml
replicaCount: 3

image:
  repository: my-app
  pullPolicy: IfNotPresent
  tag: '2.1.0'

service:
  type: ClusterIP
  port: 80

ingress:
  enabled: true
  className: nginx
  hosts:
    - host: example.com
      paths:
        - path: /
          pathType: Prefix

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 512Mi

redis:
  enabled: true
  auth:
    password: ''
```

## 3. 模板语法

### 3.1 基本语法

```yaml
# 引用值
{{ .Values.replicaCount }}

# 条件判断
{{- if .Values.ingress.enabled }}
# ingress 内容
{{- end }}

# 循环
{{- range .Values.ingress.hosts }}
- host: {{ .host }}
{{- end }}

# 默认值
image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
```

### 3.2 辅助模板

```yaml
# templates/_helpers.tpl
{{- define "my-app.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{- define "my-app.labels" -}}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
app.kubernetes.io/name: {{ include "my-app.fullname" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
```

### 3.3 使用辅助模板

```yaml
metadata:
  name: { { include "my-app.fullname" . } }
  labels: { { - include "my-app.labels" . | nindent 4 } }
```

## 4. 常用命令

### 4.1 仓库管理

```bash
# 添加仓库
helm repo add bitnami https://charts.bitnami.com/bitnami

# 更新索引
helm repo update

# 搜索 Chart
helm search repo nginx
```

### 4.2 安装与升级

```bash
# 安装
helm install my-release bitnami/nginx

# 自定义值
helm install my-release bitnami/nginx -f values.yaml

# 设置单个值
helm install my-release bitnami/nginx --set service.type=NodePort

# 升级
helm upgrade my-release bitnami/nginx -f values.yaml

# 安装或升级
helm upgrade --install my-release bitnami/nginx -f values.yaml
```

### 4.3 管理与调试

```bash
# 查看已安装
helm list

# 查看状态
helm status my-release

# 查看历史
helm history my-release

# 回滚
helm rollback my-release 1

# 卸载
helm uninstall my-release

# 调试模板
helm template my-release . --debug
helm install --dry-run my-release . --debug
```

## 5. Chart 依赖

### 5.1 声明依赖

```yaml
# Chart.yaml
dependencies:
  - name: redis
    version: '17.0.0'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: redis.enabled
  - name: postgresql
    version: '12.0.0'
    repository: 'https://charts.bitnami.com/bitnami'
    condition: postgresql.enabled
    alias: db
```

### 5.2 更新依赖

```bash
helm dependency update
helm dependency build
```

## 6. 最佳实践

| 实践     | 描述                         |
| -------- | ---------------------------- |
| 版本控制 | Chart 和 values 文件纳入 Git |
| 环境分离 | 每个环境独立 values 文件     |
| 条件依赖 | 使用 condition 控制可选组件  |
| 模板复用 | 使用 \_helpers.tpl           |
| 资源限制 | 始终设置 resources           |
| 健康检查 | 配置 liveness/readiness      |
| 镜像标签 | 不使用 latest                |
| 测试     | 编写 helm test               |

<!-- ============ 文档分隔线：034-cloud-computing/020-CloudCostOptimization.md ============ -->

## 1. 云成本管理框架

### 1.1 FinOps 定义

FinOps（Financial Operations）是将财务、技术和业务团队结合在一起，通过**数据驱动的决策**来优化云成本的实践。

FinOps 成熟度模型：

```mermaid
flowchart LR
    Crawl[Crawl 爬行<br/>基础可见性、成本分配、标签策略、预算告警] --> Walk[Walk 行走<br/>优化与治理、预留采购、异常检测、团队问责]
    Walk --> Run[Run 奔跑<br/>持续优化与自动化、智能伸缩、自动 Right-sizing、单位经济学驱动]
```

### 1.2 成本可见性

**成本分配标签**：

| 标签键      | 描述     | 示例                         |
| ----------- | -------- | ---------------------------- |
| Environment | 环境     | production / staging / dev   |
| Team        | 团队     | backend / frontend / data    |
| Service     | 服务     | user-service / order-service |
| CostCenter  | 成本中心 | CC-001 / CC-002              |
| Project     | 项目     | project-alpha                |

**成本分析维度**：

```mermaid
flowchart TD
    T0["总成本"]
    T1["按服务: EC2 / S3 / RDS / CloudFront ..."]
    T2["按团队: 后端 / 前端 / 数据 / 运维"]
    T3["按环境: 生产 / 测试 / 开发"]
    T4["按区域: us-east-1 / eu-west-1 / ap-northeast-1"]
    T5["按账户: 账户A / 账户B / 账户C"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
```

### 1.3 单位经济学

将云成本与业务指标关联：

$$
\text{单位成本} = \frac{\text{云总成本}}{\text{业务指标}}
$$

常见单位经济学指标：

| 业务类型 | 业务指标   | 单位成本   |
| -------- | ---------- | ---------- |
| SaaS     | 活跃用户数 | $/MAU      |
| 电商     | 订单数     | $/订单     |
| 流媒体   | 观看时长   | $/小时     |
| API 服务 | API 调用数 | $/百万调用 |

## 2. 计算资源优化

### 2.1 Right-sizing（规格调整）

Right-sizing 是将实例规格匹配实际工作负载需求：

```
当前: m5.2xlarge (8 vCPU, 32GB)
实际使用: CPU 15%, 内存 40%
推荐: m5.large (2 vCPU, 8GB)
节省: ~75%
```

**Right-sizing 分析流程**：

```mermaid
flowchart TD
    T0["1. 收集 CloudWatch 指标（14-30天）"]
    T1["CPU 利用率"]
    T2["内存利用率（需 CloudWatch Agent）"]
    T3["网络吞吐"]
    T4["磁盘 I/O"]
    T5["2. 识别低利用率实例"]
    T6["CPU < 40% 持续 14 天"]
    T7["内存 < 40% 持续 14 天"]
    T8["3. 推荐合适规格"]
    T9["基于峰值利用率 + 安全余量"]
    T10["考虑突发需求"]
    T11["4. 执行调整"]
    T12["停机调整（简单）"]
    T13["蓝绿替换（零停机）"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T4 --> T5
    T5 --> T6
    T5 --> T7
    T7 --> T8
    T8 --> T9
    T8 --> T10
    T10 --> T11
    T11 --> T12
    T11 --> T13
```

### 2.2 预留实例（Reserved Instances）

| 类型       | 折扣     | 灵活性         | 适用场景     |
| ---------- | -------- | -------------- | ------------ |
| 标准预留   | 最高 72% | 不可更改实例族 | 稳定工作负载 |
| 可转换预留 | 最高 54% | 可更改实例族   | 需灵活调整   |
| 节省计划   | 最高 72% | 按计算家族承诺 | 灵活承诺     |

**预留实例购买决策**：

$$
\text{盈亏平衡点} = \frac{\text{预付费用}}{\text{按需小时价} - \text{预留小时价}}
$$

例如：m5.large 按需 $0.096/h，1年全预付预留 $511（$0.058/h）：

$$
\text{盈亏平衡} = \frac{511}{0.096 - 0.058} = 13{,}447 \text{ 小时} \approx 560 \text{ 天}
$$

1年全预付不适用，3年全预付 $1{,}022（$0.039/h）：

$$
\text{盈亏平衡} = \frac{1022}{0.096 - 0.039} = 17{,}930 \text{ 小时} \approx 747 \text{ 天}
$$

3年承诺约 2 年回本。

### 2.3 Spot 实例

Spot 实例利用云厂商闲置容量，折扣高达 90%：

**Spot 实例定价模型**：

$$
\text{Spot 价格} = \text{市场供需决定}
$$

$$
\text{中断概率} \propto \frac{\text{Spot 价格}}{\text{按需价格}}
$$

| Spot 价格/按需价格 | 中断概率 | 风险等级 |
| ------------------ | -------- | -------- |
| < 30%              | < 5%/周  | 低       |
| 30%-50%            | 5-10%/周 | 中       |
| > 50%              | > 10%/周 | 高       |

**Spot 实例最佳实践**：

- **Spot Fleet**：多实例类型 + 多 AZ 分散风险
- **Spot 中断通知**：2 分钟预警，优雅处理
- **检查点机制**：定期保存计算状态
- **混合策略**：按需 + Spot 组合

```mermaid
flowchart TD
    OD[按需实例 N 个<br/>核心容量，保证基线] + SP[Spot 实例 M 个<br/>弹性容量，可被中断]
    OD --> T[总容量 = N + M<br/>保证容量 ≥ N]
    SP --> T
```

### 2.4 自动伸缩优化

**伸缩策略成本优化**：

```
保守策略: min=5, max=20, target=70% CPU
  → 响应快，但可能过度配置

激进策略: min=2, max=20, target=85% CPU
  → 成本低，但可能影响性能

推荐: min=3, max=20, target=75% CPU + 预测性伸缩
  → 平衡成本与性能
```

**预测性伸缩**：基于历史数据预测负载，提前扩容：

$$
\text{预测负载}(t) = \alpha \times \text{历史负载}(t - 7d) + (1-\alpha) \times \text{趋势}(t)
$$

## 3. 存储成本优化

### 3.1 存储分层策略

根据访问频率自动分层：

```mermaid
flowchart TD
    Q{数据访问频率?}
    Q -->|频繁 >1次/天| S1[Standard]
    Q -->|偶尔 >1次/月| S2[Standard-IA]
    Q -->|稀少 >1次/年| S3[Glacier Instant]
    Q -->|极少 <1次/年| S4[Glacier Deep Archive]
    Q -->|未知| S5[Intelligent-Tiering]
```

**生命周期规则成本节省计算**：

$$
\text{月节省} = \text{数据量} \times (\text{当前单价} - \text{目标单价}) - \text{检索费}
$$

### 3.2 EBS 优化

| 优化措施     | 节省幅度 | 实施方式             |
| ------------ | -------- | -------------------- |
| 删除未挂载卷 | 100%     | 定期扫描未挂载 EBS   |
| 缩减过大卷   | 30-60%   | 监控磁盘利用率       |
| 快照清理     | 变化大   | 删除过期快照         |
| gp2 → gp3    | ~20%     | gp3 更便宜且性能独立 |
| 降级冷数据卷 | 50%+     | 冷数据用 st1/sc1     |

**gp2 vs gp3 成本对比**：

$$
C_{\text{gp2}} = \text{容量(GB)} \times \$0.10/\text{GB}
$$

$$
C_{\text{gp3}} = \text{容量(GB)} \times \$0.08/\text{GB} + \max(0, \text{IOPS} - 3000) \times \$0.005 + \max(0, \text{吞吐} - 125) \times \$0.04
$$

300GB 卷，gp2 = $30/月，gp3 = $24/月，节省 20%。

### 3.3 快照优化

```
快照管理策略:
1. 保留策略: 日快照保留7天，周快照保留4周，月快照保留12月
2. 删除孤立快照: 无关联 AMI 的快照
3. 压缩快照: 使用第三方工具压缩
4. 跨区域复制: 仅复制必要快照
```

## 4. 网络成本优化

### 4.1 数据传输费用

数据传输是云成本中容易被忽视的部分：

| 传输方向        | 费用              |
| --------------- | ----------------- |
| 入站到 AWS      | 免费              |
| 同区域 EC2 之间 | 免费              |
| 跨区域 EC2 之间 | $0.02/GB          |
| 出站到互联网    | $0.09/GB (前10TB) |
| S3 跨区域复制   | $0.02/GB          |

### 4.2 网络优化策略

**CDN 卸载**：

$$
\text{CDN 节省} = \text{可缓存流量} \times (\text{EC2 出站费} - \text{CloudFront 费})
$$

$$
= \text{可缓存流量} \times (\$0.09 - \$0.085) = \$0.005/\text{GB}
$$

虽然单价差异小，但 CDN 还减少了 EC2 负载。

**VPC Endpoint 节省**：

```
无 Endpoint: EC2 → NAT Gateway → 互联网 → S3
  费用: NAT 数据处理费 $0.045/GB + NAT 小时费

有 Endpoint: EC2 → VPC Gateway Endpoint → S3
  费用: 免费 (Gateway Endpoint 对 S3/DynamoDB 免费)
```

**S3 传输加速**：

```
远距离上传: 用户(亚洲) → S3(美国)
  直接上传: 高延迟，可能超时
  Transfer Acceleration: 用户 → 边缘节点 → 优化路径 → S3
  额外费用: $0.04/GB (但减少失败重传)
```

### 4.3 区域选择

不同区域价格差异：

$$
\text{区域价格系数} = \frac{\text{目标区域价格}}{\text{us-east-1 价格}}
$$

| 区域           | EC2 系数 | S3 系数 | 数据传出系数 |
| -------------- | -------- | ------- | ------------ |
| us-east-1      | 1.00     | 1.00    | 1.00         |
| eu-west-1      | 1.05     | 1.00    | 1.00         |
| ap-northeast-1 | 1.10     | 1.00    | 1.00         |
| ap-southeast-1 | 1.15     | 1.02    | 1.00         |
| sa-east-1      | 1.25     | 1.05    | 1.00         |

## 5. FinOps 实践

### 5.1 FinOps 团队结构

```mermaid
flowchart TD
    F[财务<br/>预算/预测/报告] --> FP[FinOps 平台/流程]
    E[工程<br/>优化/架构/自动化] --> FP
    B[业务<br/>价值/优先级/ROI] --> FP
```

### 5.2 成本告警与预算

**多级预算告警**：

```mermaid
flowchart TD
    T0["月度预算: $100,000"]
    T1["50% ($50,000)  → 信息通知: '已使用50%预算'"]
    T2["80% ($80,000)  → 警告通知: '已使用80%预算，请检查'"]
    T3["100% ($100,000) → 严重告警: '预算已用完'"]
    T4["120% ($120,000) → 紧急告警: '超预算20%，需审批'"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
```

**异常检测**：

$$
\text{异常分数} = \frac{|\text{实际成本} - \text{预测成本}|}{\text{标准差}}
$$

$$
\text{若异常分数} > 3 \Rightarrow \text{触发告警}
$$

### 5.3 成本优化看板

关键指标：

| 指标         | 计算                            | 目标       |
| ------------ | ------------------------------- | ---------- |
| 浪费率       | 未使用资源成本 / 总成本         | < 10%      |
| 预留覆盖率   | 预留实例覆盖的支出 / 可预留支出 | > 70%      |
| 单位成本趋势 | 当月单位成本 vs 上月            | 下降或持平 |
| Spot 利用率  | Spot 支出 / 总计算支出          | > 20%      |
| 标签覆盖率   | 有标签资源 / 总资源             | > 95%      |

### 5.4 持续优化循环

```mermaid
flowchart LR
    I[Inform 告知<br/>成本分配与可视化/预算与告警/异常检测] --> O[Optimize 优化<br/>Right-sizing/预留采购/存储分层/架构优化]
    O --> P[Operate 运营<br/>自动化策略/治理与合规/持续监控]
    P --> I
```

### 5.5 成本优化自动化

**自动 Right-sizing**：

```
CloudWatch 指标 → Lambda 分析 → 生成建议 →
  自动执行（开发环境）或
  人工审批（生产环境）
```

**自动 Spot 中断处理**：

```
Spot 中断通知 → EventBridge → Lambda →
  1. 标记实例为 draining
  2. 从负载均衡器移除
  3. 在新 Spot 实例启动替代
  4. 等待优雅关闭
```

**自动快照清理**：

```
每日定时 → Lambda →
  1. 列出所有快照
  2. 检查关联 AMI
  3. 删除超过保留期的孤立快照
  4. 发送清理报告
```

<!-- ============ 文档分隔线：034-cloud-computing/021-TwelveFactorApp.md ============ -->

## 1. 12-Factor 概述

### 1.1 起源

12-Factor App 由 Heroku 联合创始人 Adam Wiggins 于 2011 年提出，是构建 SaaS 应用的方法论。

### 1.2 核心目标

- 可移植性
- 云原生部署
- 持续部署
- 弹性伸缩

## 2. 十二个要素

### 2.1 Codebase — 代码库

一份代码库，多次部署。

```
一个应用 → 一个 Git 仓库
同一代码库 → 多个部署（dev/staging/prod）
不同应用 → 不同代码库
```

| 规则       | 描述                 |
| ---------- | -------------------- |
| 单一代码库 | 一个应用一个仓库     |
| 多次部署   | 共享代码，不同配置   |
| 不共享代码 | 不同应用不共享代码库 |

### 2.2 Dependencies — 依赖

显式声明并隔离依赖。

```json
// package.json
{
  "dependencies": {
    "express": "^4.18.0",
    "lodash": "^4.17.21"
  }
}
```

| 规则     | 描述             |
| -------- | ---------------- |
| 显式声明 | 通过清单文件声明 |
| 隔离     | 不依赖系统级包   |
| 锁定     | 使用 lock 文件   |

### 2.3 Config — 配置

在环境中存储配置。

```bash
# 环境变量
export DATABASE_URL=postgres://user:pass@host:5432/db
export API_KEY=sk-xxx
export LOG_LEVEL=info
```

| 规则     | 描述             |
| -------- | ---------------- |
| 不硬编码 | 配置不写在代码中 |
| 环境变量 | 通过 env 传入    |
| 严格分离 | 代码与配置独立   |

**配置判断标准**：在不同部署间是否变化？变化 → 配置，不变 → 代码。

### 2.4 Backing Services — 后端服务

将后端服务当作附加资源。

```
应用 ←→ 数据库（可替换）
应用 ←→ 消息队列（可替换）
应用 ←→ 缓存（可替换）
```

| 规则     | 描述                 |
| -------- | -------------------- |
| 统一接口 | 本地和远程服务无差别 |
| 可替换   | 通过配置切换服务     |
| 松耦合   | 不绑定特定实现       |

### 2.5 Build, Release, Run — 构建/发布/运行

严格分离构建和运行阶段。

```
构建：代码 → 可执行包
发布：可执行包 + 配置 → 发布版本
运行：启动发布版本
```

| 阶段    | 输入        | 输出     |
| ------- | ----------- | -------- |
| Build   | 代码 + 依赖 | 构建产物 |
| Release | 构建 + 配置 | 发布版本 |
| Run     | 发布版本    | 运行进程 |

### 2.6 Processes — 进程

以无状态进程运行应用。

| 规则     | 描述               |
| -------- | ------------------ |
| 无状态   | 进程不存储状态     |
| 持久数据 | 存入后端服务       |
| 可替换   | 任何进程可随时停止 |

### 2.7 Port Binding — 端口绑定

通过端口绑定提供服务。

```javascript
// 应用自包含 Web 服务器
const server = app.listen(process.env.PORT || 3000);
```

| 规则     | 描述                  |
| -------- | --------------------- |
| 自包含   | 不依赖外部 Web 服务器 |
| 端口监听 | 通过端口暴露服务      |
| 可寻址   | URL 即服务            |

### 2.8 Concurrency — 并发

通过进程模型进行扩展。

```
扩展方式：
- 横向扩展（增加进程数）
- 纵向扩展（增加资源）
```

| 进程类型 | 描述           |
| -------- | -------------- |
| Web      | 处理 HTTP 请求 |
| Worker   | 处理后台任务   |
| Clock    | 定时任务       |

### 2.9 Disposability — 易处理

快速启动和优雅终止。

| 规则     | 描述                 |
| -------- | -------------------- |
| 快速启动 | 秒级启动             |
| 优雅关闭 | 处理完当前请求后退出 |
| 健壮性   | 进程可随时被替换     |

```javascript
// 优雅关闭
process.on('SIGTERM', () => {
  server.close(() => {
    process.exit(0);
  });
});
```

### 2.10 Dev/Prod Parity — 开发/生产一致

尽可能保持开发、预发布和生产环境一致。

| 差异 | 传统 | 12-Factor |
| ---- | ---- | --------- |
| 时间 | 数周 | 数小时    |
| 人员 | 不同 | 相同      |
| 工具 | 不同 | 相同      |

### 2.11 Logs — 日志

将日志视为事件流。

```bash
# 输出到 stdout/stderr
console.log("Request processed");
console.error("Database connection failed");
```

| 规则       | 描述               |
| ---------- | ------------------ |
| 不管理日志 | 应用不关心日志存储 |
| 事件流     | 日志是连续的事件流 |
| 集中处理   | 由外部系统收集     |

### 2.12 Admin Processes — 管理进程

将管理任务作为一次性进程运行。

```bash
# 一次性管理任务
rails db:migrate
python manage.py migrate
npx prisma migrate deploy
```

| 规则     | 描述               |
| -------- | ------------------ |
| 一次性   | 运行后退出         |
| 同代码库 | 使用相同代码和配置 |
| 同环境   | 在相同环境中运行   |

## 3. 现代扩展

### 3.1 超越 12-Factor

| 新要素    | 描述           |
| --------- | -------------- |
| API First | API 优先设计   |
| Telemetry | 遥测与可观测性 |
| Security  | 安全左移       |
| Container | 容器化         |
| CI/CD     | 持续集成部署   |

### 3.2 与云原生的关系

12-Factor 是云原生的理论基础，CNCF 的很多项目（Kubernetes、Istio）都是 12-Factor 的工程实现。

<!-- ============ 文档分隔线：034-cloud-computing/022-MicroserviceArchitecture.md ============ -->

## 1. 微服务概述

### 1.1 什么是微服务

微服务是一种将应用拆分为一组小型、独立部署的服务的架构风格。

### 1.2 与单体架构对比

| 对比项 | 单体架构 | 微服务架构 |
| ------ | -------- | ---------- |
| 部署   | 整体部署 | 独立部署   |
| 技术栈 | 统一     | 异构       |
| 扩展   | 整体扩展 | 按需扩展   |
| 故障   | 全局影响 | 局部影响   |
| 团队   | 集中     | 分散       |
| 复杂度 | 代码复杂 | 运维复杂   |

### 1.3 何时使用微服务

| 场景          | 推荐   |
| ------------- | ------ |
| 小团队/初创   | 单体   |
| 大型复杂系统  | 微服务 |
| 快速验证      | 单体   |
| 高并发/多团队 | 微服务 |

## 2. 服务拆分策略

### 2.1 拆分原则

| 原则     | 描述                   |
| -------- | ---------------------- |
| 单一职责 | 每个服务一个业务能力   |
| 高内聚   | 相关功能放在一起       |
| 松耦合   | 服务间依赖最小化       |
| 独立部署 | 可独立发布             |
| 数据自治 | 每个服务有自己的数据库 |

### 2.2 拆分方法

| 方法       | 描述             |
| ---------- | ---------------- |
| 按业务能力 | 围绕业务功能拆分 |
| 按子域     | DDD 限界上下文   |
| 按用例     | 围绕用户场景     |
| 按数据     | 围绕数据所有权   |

### 2.3 DDD 限界上下文

```mermaid
flowchart TD
    subgraph O[订单上下文]
        OS[OrderService] OD[OrderDB]
    end
    subgraph I[库存上下文]
        IS[InventorySvc] ID[InventoryDB]
    end
    subgraph P[支付上下文]
        PS[PaymentService] PD[PaymentDB]
    end
```

## 3. 服务通信

### 3.1 同步通信

| 方式    | 协议           | 特点           |
| ------- | -------------- | -------------- |
| REST    | HTTP/JSON      | 简单、通用     |
| gRPC    | HTTP2/Protobuf | 高性能、强类型 |
| GraphQL | HTTP/JSON      | 灵活查询       |

### 3.2 异步通信

| 方式     | 协议          | 特点           |
| -------- | ------------- | -------------- |
| 消息队列 | AMQP          | 解耦、削峰     |
| 事件驱动 | Kafka         | 高吞吐、持久化 |
| 事件总线 | Redis Streams | 轻量级         |

### 3.3 通信模式

| 模式      | 描述         | 适用场景   |
| --------- | ------------ | ---------- |
| 请求-响应 | 同步调用     | 查询类     |
| 事件通知  | 异步通知     | 状态变更   |
| 事件溯源  | 存储所有事件 | 审计、回放 |
| CQRS      | 读写分离     | 复杂查询   |

### 3.4 Saga 模式

分布式事务管理：

**编排式**：

```
OrderService → CreateOrder → ReserveInventory → ProcessPayment → ConfirmOrder
                                      ↓ 失败
                              CancelOrder ← RefundPayment
```

**协调式**：

```
Saga Coordinator → 调用各服务 → 失败时发送补偿命令
```

## 4. 数据管理

### 4.1 数据库每服务一个

```
 每个服务有独立数据库
 服务间直接访问其他服务的数据库
 通过 API 或事件共享数据
```

### 4.2 数据一致性

| 策略       | 描述          |
| ---------- | ------------- |
| 强一致性   | 2PC（不推荐） |
| 最终一致性 | Saga + 事件   |
| 补偿事务   | 失败时回滚    |

### 4.3 API 组合

```
API Gateway → 聚合多个服务的数据 → 返回给客户端

GET /order-details/123
  → OrderService: 订单信息
  → InventoryService: 库存状态
  → PaymentService: 支付状态
  → 组合返回
```

## 5. 服务治理

### 5.1 服务发现

| 方式       | 描述                   |
| ---------- | ---------------------- |
| 客户端发现 | 客户端查询注册中心     |
| 服务端发现 | 负载均衡器查询注册中心 |

### 5.2 负载均衡

| 策略     | 描述             |
| -------- | ---------------- |
| 轮询     | 依次分配         |
| 随机     | 随机分配         |
| 加权     | 按权重分配       |
| 最少连接 | 分配给连接最少的 |

### 5.3 熔断器

```javascript
// 熔断器状态机
CLOSED → (错误率超阈值) → OPEN
OPEN → (超时后) → HALF_OPEN
HALF_OPEN → (探测成功) → CLOSED
HALF_OPEN → (探测失败) → OPEN
```

### 5.4 限流

| 算法     | 描述             |
| -------- | ---------------- |
| 固定窗口 | 固定时间窗口计数 |
| 滑动窗口 | 平滑计数         |
| 令牌桶   | 匀速生成令牌     |
| 漏桶     | 匀速消费请求     |

## 6. 微服务最佳实践

| 实践       | 描述                 |
| ---------- | -------------------- |
| API 版本化 | `/api/v1/resource`   |
| 幂等设计   | 重复请求结果一致     |
| 健康检查   | `/health` 端点       |
| 优雅降级   | 依赖失败时的备选方案 |
| 配置外部化 | 环境变量/配置中心    |
| 可观测性   | 日志+指标+追踪       |
| 契约测试   | 消费者驱动契约       |
| CI/CD      | 每个服务独立流水线   |

<!-- ============ 文档分隔线：034-cloud-computing/023-ServiceMesh.md ============ -->

## 1. 服务网格概述

### 1.1 什么是服务网格

服务网格（Service Mesh）是专门处理服务间通信的基础设施层，通过 Sidecar 代理实现流量管理、安全通信和可观测性。

### 1.2 架构模式

```mermaid
flowchart TD
    CP[控制平面<br/>配置分发、证书管理、策略]
    S1[Sidecar Proxy<br/>Service A]
    S2[Sidecar Proxy<br/>Service B]
    CP --> S1
    CP --> S2
    S1 <--> S2
```

### 1.3 核心功能

| 功能     | 描述                   |
| -------- | ---------------------- |
| 流量管理 | 路由、分流、重试、超时 |
| 安全     | mTLS、认证、授权       |
| 可观测性 | 指标、日志、追踪       |
| 弹性     | 熔断、限流、故障注入   |

## 2. Istio

### 2.1 架构

| 组件   | 功能                                  |
| ------ | ------------------------------------- |
| istiod | 控制平面（Pilot+Citadel+Galley 合并） |
| Envoy  | 数据平面 Sidecar 代理                 |

### 2.2 流量管理

**VirtualService**：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    - reviews
  http:
    - match:
        - headers:
            x-user-type:
              exact: premium
      route:
        - destination:
            host: reviews
            subset: v2
    - route:
        - destination:
            host: reviews
            subset: v1
          weight: 90
        - destination:
            host: reviews
            subset: v2
          weight: 10
```

**DestinationRule**：

```yaml
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: reviews
spec:
  host: reviews
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
  subsets:
    - name: v1
      labels:
        version: v1
    - name: v2
      labels:
        version: v2
```

### 2.3 安全策略

**PeerAuthentication（mTLS）**：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT
```

**AuthorizationPolicy**：

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: api-access
spec:
  selector:
    matchLabels:
      app: api
  rules:
    - from:
        - source:
            principals: ['cluster.local/ns/default/sa/web']
      to:
        - operation:
            methods: ['GET', 'POST']
            paths: ['/api/*']
```

### 2.4 可观测性

| 组件       | 功能       |
| ---------- | ---------- |
| Prometheus | 指标收集   |
| Grafana    | 指标可视化 |
| Jaeger     | 分布式追踪 |
| Kiali      | 服务拓扑图 |

## 3. Linkerd

### 3.1 特点

| 特点      | 描述                    |
| --------- | ----------------------- |
| 轻量级    | Rust 实现的 micro-proxy |
| 简单      | 最小化配置              |
| 自动 mTLS | 默认启用                |
| 快速      | 低延迟开销              |

### 3.2 与 Istio 对比

| 对比项   | Istio       | Linkerd            |
| -------- | ----------- | ------------------ |
| 代理     | Envoy (C++) | micro-proxy (Rust) |
| 复杂度   | 高          | 低                 |
| 功能     | 全面        | 核心功能           |
| 资源消耗 | 高          | 低                 |
| 社区     | 大          | 中                 |
| 学习曲线 | 陡          | 平缓               |

## 4. 流量管理场景

### 4.1 金丝雀发布

```yaml
# 90% v1, 10% v2 → 逐步调整
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
spec:
  http:
    - route:
        - destination:
            host: myapp
            subset: v1
          weight: 90
        - destination:
            host: myapp
            subset: v2
          weight: 10
```

### 4.2 故障注入

```yaml
# 注入 500ms 延迟，10% 概率
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
spec:
  http:
    - fault:
        delay:
          percentage:
            value: 10
          fixedDelay: 500ms
      route:
        - destination:
            host: myapp
```

### 4.3 重试与超时

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
spec:
  http:
    - route:
        - destination:
            host: myapp
      retries:
        attempts: 3
        perTryTimeout: 2s
        retryOn: 5xx,reset,connect-failure
      timeout: 10s
```

## 5. 服务网格选型

| 场景              | 推荐                |
| ----------------- | ------------------- |
| 大规模/复杂需求   | Istio               |
| 中小规模/简单优先 | Linkerd             |
| eBPF 方案         | Cilium Service Mesh |
| 多集群            | Istio               |
| 资源受限          | Linkerd             |

<!-- ============ 文档分隔线：034-cloud-computing/024-Observability.md ============ -->

## 1. 可观测性概述

### 1.1 三大支柱

| 支柱           | 描述         | 核心问题         |
| -------------- | ------------ | ---------------- |
| 日志 (Logs)    | 离散事件记录 | 发生了什么？     |
| 指标 (Metrics) | 聚合数值数据 | 现在什么状态？   |
| 追踪 (Traces)  | 请求链路追踪 | 请求经过了哪里？ |

### 1.2 监控 vs 可观测性

| 对比项 | 监控         | 可观测性       |
| ------ | ------------ | -------------- |
| 方式   | 预定义仪表盘 | 探索式查询     |
| 问题   | 已知问题     | 未知问题       |
| 数据   | 指标为主     | 日志+指标+追踪 |
| 思维   | 被动告警     | 主动探索       |

## 2. 日志

### 2.1 日志级别

| 级别  | 用途               |
| ----- | ------------------ |
| ERROR | 错误，需要立即处理 |
| WARN  | 警告，可能的问题   |
| INFO  | 重要业务事件       |
| DEBUG | 调试信息           |
| TRACE | 详细追踪           |

### 2.2 结构化日志

```json
{
  "timestamp": "2026-06-14T10:30:00Z",
  "level": "INFO",
  "service": "order-service",
  "trace_id": "abc123",
  "span_id": "def456",
  "message": "Order created",
  "user_id": "user-789",
  "order_id": "order-101",
  "duration_ms": 45
}
```

### 2.3 日志架构

```
应用 → Fluentd/Filebeat → Kafka → Logstash → Elasticsearch → Kibana
                                    或
应用 → Fluent Bit → Loki → Grafana
```

### 2.4 ELK vs EFK vs PLG

| 栈  | 组件                              | 特点                  |
| --- | --------------------------------- | --------------------- |
| ELK | Elasticsearch + Logstash + Kibana | 功能全面、资源消耗大  |
| EFK | Elasticsearch + Fluentd + Kibana  | Fluentd 替代 Logstash |
| PLG | Prometheus + Loki + Grafana       | 轻量、与指标统一      |

## 3. 指标

### 3.1 指标类型

| 类型      | 描述           | 示例                 |
| --------- | -------------- | -------------------- |
| Counter   | 单调递增计数器 | 请求总数、错误总数   |
| Gauge     | 可增可减的值   | 当前连接数、内存使用 |
| Histogram | 分布统计       | 请求延迟分布         |
| Summary   | 分位数统计     | P50/P95/P99 延迟     |

### 3.2 Prometheus

**数据模型**：

```
metric_name{label1="value1", label2="value2"} value timestamp

http_requests_total{method="GET", path="/api/users", status="200"} 1234
```

**PromQL 查询**：

```promql
# 请求速率（每秒）
rate(http_requests_total[5m])

# P99 延迟
histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))

# 错误率
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# 按 service 分组
sum(rate(http_requests_total[5m])) by (service)
```

### 3.3 四大黄金信号

| 信号   | 描述         | 指标            |
| ------ | ------------ | --------------- |
| 延迟   | 请求处理时间 | P50/P95/P99     |
| 流量   | 请求量       | QPS             |
| 错误   | 失败率       | Error Rate      |
| 饱和度 | 资源使用率   | CPU/Memory/Disk |

### 3.4 RED 方法

| 指标     | 描述     |
| -------- | -------- |
| Rate     | 请求速率 |
| Errors   | 错误率   |
| Duration | 请求延迟 |

### 3.5 USE 方法

| 指标        | 描述   |
| ----------- | ------ |
| Utilization | 使用率 |
| Saturation  | 饱和度 |
| Errors      | 错误数 |

## 4. 分布式追踪

### 4.1 核心概念

| 概念        | 描述                 |
| ----------- | -------------------- |
| Trace       | 一次请求的完整链路   |
| Span        | 链路中的一个操作     |
| SpanContext | 跨进程传递的上下文   |
| Baggage     | 跨 Span 传播的键值对 |

### 4.2 OpenTelemetry

统一可观测性标准，合并了 OpenTracing 和 OpenCensus。

**架构**：

```
应用 → OTel SDK → OTel Collector → 后端（Jaeger/Tempo/...）
```

**代码示例**：

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# 配置
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="otel-collector:4317"))
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# 使用
tracer = trace.get_tracer("my-service")
with tracer.start_as_current_span("process-order") as span:
    span.set_attribute("order.id", "12345")
    # 业务逻辑
```

### 4.3 追踪后端

| 工具       | 特点                   |
| ---------- | ---------------------- |
| Jaeger     | CNCF 项目，功能全面    |
| Zipkin     | 老牌追踪系统           |
| Tempo      | Grafana 生态，对象存储 |
| SkyWalking | APM+追踪               |

## 5. 告警

### 5.1 告警原则

| 原则     | 描述                   |
| -------- | ---------------------- |
| 可操作性 | 每个告警都应有明确动作 |
| 避免噪音 | 减少无效告警           |
| 分级     | P0-P3 分级             |
| 升级     | 超时自动升级           |

### 5.2 AlertManager 配置

```yaml
route:
  receiver: 'slack'
  group_by: ['alertname', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty'
      repeat_interval: 1h

receivers:
  - name: 'slack'
    slack_configs:
      - channel: '#alerts'
  - name: 'pagerduty'
    pagerduty_configs:
      - service_key: 'xxx'
```

## 6. 可观测性最佳实践

| 实践         | 描述                          |
| ------------ | ----------------------------- |
| 关联三大支柱 | trace_id 贯穿日志、指标、追踪 |
| 语义约定     | 使用 OpenTelemetry 语义约定   |
| 采样策略     | 尾部采样保留异常请求          |
| SLO/SLI      | 定义服务等级目标和指标        |
| 仪表盘分层   | 概览→服务→实例                |

<!-- ============ 文档分隔线：034-cloud-computing/025-AWSCore.md ============ -->

## 1. 计算

### 1.1 EC2 实例类型

EC2 实例类型是AWS核心服务的重要组成部分。本节详细介绍EC2 实例类型的核心概念、工作原理和实际应用。

**关键要点**：

- EC2 实例类型的定义与核心原理
- EC2 实例类型的实现方式与技术细节
- EC2 实例类型在实际场景中的应用与最佳实践
- EC2 实例类型的常见问题与解决方案

EC2 实例类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Lambda 无服务器

Lambda 无服务器是AWS核心服务的重要组成部分。本节详细介绍Lambda 无服务器的核心概念、工作原理和实际应用。

**关键要点**：

- Lambda 无服务器的定义与核心原理
- Lambda 无服务器的实现方式与技术细节
- Lambda 无服务器在实际场景中的应用与最佳实践
- Lambda 无服务器的常见问题与解决方案

Lambda 无服务器在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 存储

### 2.1 S3 存储类别

S3 存储类别是AWS核心服务的重要组成部分。本节详细介绍S3 存储类别的核心概念、工作原理和实际应用。

**关键要点**：

- S3 存储类别的定义与核心原理
- S3 存储类别的实现方式与技术细节
- S3 存储类别在实际场景中的应用与最佳实践
- S3 存储类别的常见问题与解决方案

S3 存储类别在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 EBS 卷类型

EBS 卷类型是AWS核心服务的重要组成部分。本节详细介绍EBS 卷类型的核心概念、工作原理和实际应用。

**关键要点**：

- EBS 卷类型的定义与核心原理
- EBS 卷类型的实现方式与技术细节
- EBS 卷类型在实际场景中的应用与最佳实践
- EBS 卷类型的常见问题与解决方案

EBS 卷类型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 网络

### 3.1 VPC 与子网

VPC 与子网是AWS核心服务的重要组成部分。本节详细介绍VPC 与子网的核心概念、工作原理和实际应用。

**关键要点**：

- VPC 与子网的定义与核心原理
- VPC 与子网的实现方式与技术细节
- VPC 与子网在实际场景中的应用与最佳实践
- VPC 与子网的常见问题与解决方案

VPC 与子网在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 安全组与 NACL

安全组与 NACL是AWS核心服务的重要组成部分。本节详细介绍安全组与 NACL的核心概念、工作原理和实际应用。

**关键要点**：

- 安全组与 NACL的定义与核心原理
- 安全组与 NACL的实现方式与技术细节
- 安全组与 NACL在实际场景中的应用与最佳实践
- 安全组与 NACL的常见问题与解决方案

安全组与 NACL在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 数据库与安全

### 4.1 RDS 多可用区

RDS 多可用区是AWS核心服务的重要组成部分。本节详细介绍RDS 多可用区的核心概念、工作原理和实际应用。

**关键要点**：

- RDS 多可用区的定义与核心原理
- RDS 多可用区的实现方式与技术细节
- RDS 多可用区在实际场景中的应用与最佳实践
- RDS 多可用区的常见问题与解决方案

RDS 多可用区在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 IAM 策略与角色

IAM 策略与角色是AWS核心服务的重要组成部分。本节详细介绍IAM 策略与角色的核心概念、工作原理和实际应用。

**关键要点**：

- IAM 策略与角色的定义与核心原理
- IAM 策略与角色的实现方式与技术细节
- IAM 策略与角色在实际场景中的应用与最佳实践
- IAM 策略与角色的常见问题与解决方案

IAM 策略与角色在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：034-cloud-computing/026-MultiCloudHybridArchitecture.md ============ -->

## 1. 多云策略

### 1.1 多云动机

多云动机是多云与混合云架构的重要组成部分。本节详细介绍多云动机的核心概念、工作原理和实际应用。

**关键要点**：

- 多云动机的定义与核心原理
- 多云动机的实现方式与技术细节
- 多云动机在实际场景中的应用与最佳实践
- 多云动机的常见问题与解决方案

多云动机在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 云厂商选择

云厂商选择是多云与混合云架构的重要组成部分。本节详细介绍云厂商选择的核心概念、工作原理和实际应用。

**关键要点**：

- 云厂商选择的定义与核心原理
- 云厂商选择的实现方式与技术细节
- 云厂商选择在实际场景中的应用与最佳实践
- 云厂商选择的常见问题与解决方案

云厂商选择在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 网络互联

### 2.1 VPC Peering

VPC Peering是多云与混合云架构的重要组成部分。本节详细介绍VPC Peering的核心概念、工作原理和实际应用。

**关键要点**：

- VPC Peering的定义与核心原理
- VPC Peering的实现方式与技术细节
- VPC Peering在实际场景中的应用与最佳实践
- VPC Peering的常见问题与解决方案

VPC Peering在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 VPN 网关

VPN 网关是多云与混合云架构的重要组成部分。本节详细介绍VPN 网关的核心概念、工作原理和实际应用。

**关键要点**：

- VPN 网关的定义与核心原理
- VPN 网关的实现方式与技术细节
- VPN 网关在实际场景中的应用与最佳实践
- VPN 网关的常见问题与解决方案

VPN 网关在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 专线接入

专线接入是多云与混合云架构的重要组成部分。本节详细介绍专线接入的核心概念、工作原理和实际应用。

**关键要点**：

- 专线接入的定义与核心原理
- 专线接入的实现方式与技术细节
- 专线接入在实际场景中的应用与最佳实践
- 专线接入的常见问题与解决方案

专线接入在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 多云管理

### 3.1 Terraform 多 Provider

Terraform 多 Provider是多云与混合云架构的重要组成部分。本节详细介绍Terraform 多 Provider的核心概念、工作原理和实际应用。

**关键要点**：

- Terraform 多 Provider的定义与核心原理
- Terraform 多 Provider的实现方式与技术细节
- Terraform 多 Provider在实际场景中的应用与最佳实践
- Terraform 多 Provider的常见问题与解决方案

Terraform 多 Provider在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 统一监控

统一监控是多云与混合云架构的重要组成部分。本节详细介绍统一监控的核心概念、工作原理和实际应用。

**关键要点**：

- 统一监控的定义与核心原理
- 统一监控的实现方式与技术细节
- 统一监控在实际场景中的应用与最佳实践
- 统一监控的常见问题与解决方案

统一监控在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 数据与身份

### 4.1 数据同步

数据同步是多云与混合云架构的重要组成部分。本节详细介绍数据同步的核心概念、工作原理和实际应用。

**关键要点**：

- 数据同步的定义与核心原理
- 数据同步的实现方式与技术细节
- 数据同步在实际场景中的应用与最佳实践
- 数据同步的常见问题与解决方案

数据同步在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 统一身份认证

统一身份认证是多云与混合云架构的重要组成部分。本节详细介绍统一身份认证的核心概念、工作原理和实际应用。

**关键要点**：

- 统一身份认证的定义与核心原理
- 统一身份认证的实现方式与技术细节
- 统一身份认证在实际场景中的应用与最佳实践
- 统一身份认证的常见问题与解决方案

统一身份认证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
## 多云工具安装

**基本写法：安装 rclone**
`curl https://rclone.org/install.sh | sudo bash`
```bash
# 安装 rclone 跨云同步工具
curl https://rclone.org/install.sh | sudo bash
```

---

**基本写法：Windows 安装 rclone**
`winget install Rclone.Rclone`
```bash
# Windows 通过 winget 安装
winget install Rclone.Rclone
```

---

**基本写法：查看版本**
`rclone version`
```bash
# 查看 rclone 版本
rclone version
```

---

**基本写法：交互式配置**
`rclone config`
```bash
# 进入交互式配置新增远程存储
rclone config
```

---

**基本写法：查看已配置远程**
`rclone listremotes`
```bash
# 列出所有已配置的远程存储
rclone listremotes
```

---

## 远程存储配置

**基本写法：配置 AWS S3**
```ini
# ~/.config/rclone/rclone.conf 配置 S3
[mys3]
type = s3
provider = AWS
env_auth = false
access_key_id = AKIAIOSFODNN7EXAMPLE
secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
region = us-east-1
endpoint =
location_constraint = us-east-1
```

---

**基本写法：配置 Azure Blob**
```ini
# 配置 Azure Blob Storage
[myazure]
type = azureblob
account = mystorageaccount
key = MyStorageKey1234567890ABCDEF==
endpoint =
```

---

**基本写法：配置 GCS**
```ini
# 配置 Google Cloud Storage
[mygcs]
type = google cloud storage
client_id = your-client-id
client_secret = your-client-secret
project_number = 123456789012
service_account_file = /path/to/key.json
object_acl = private
bucket_acl = private
```

---

**基本写法：配置阿里云 OSS**
```ini
# 配置阿里云 OSS
[myoss]
type = s3
provider = Alibaba
env_auth = false
access_key_id = LTAI4your-access-key
secret_access_key = your-secret-key
endpoint = oss-cn-hangzhou.aliyuncs.com
acl = private
```

---

**基本写法：配置腾讯云 COS**
```ini
# 配置腾讯云 COS
[mycos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = AKIDyour-access-key
secret_access_key = your-secret-key
endpoint = cos.ap-guangzhou.myqcloud.com
```

---

## 数据同步

**基本写法：同步目录**
`rclone sync <源> <目标> [--progress]`
```bash
# 从 S3 同步到 Azure Blob
rclone sync mys3:my-bucket myazure:my-container --progress
```

---

**基本写法：复制文件**
`rclone copy <源> <目标>`
```bash
# 复制 S3 文件到 GCS(保留原文件)
rclone copy mys3:my-bucket/data mygcs:my-bucket/data --progress
```

---

**基本写法：移动文件**
`rclone move <源> <目标>`
```bash
# 移动文件并删除源(用于迁移)
rclone move mys3:old-bucket myazure:new-container --progress
```

---

**基本写法：增量同步**
`rclone sync <源> <目标> --update --verbose`
```bash
# 仅同步修改过的文件
rclone sync mys3:my-bucket mygcs:my-bucket --update --verbose
```

---

**基本写法：带过滤同步**
`rclone sync <源> <目标> --include <模式> --exclude <模式>`
```bash
# 仅同步 images 目录下的 jpg 文件
rclone sync mys3:my-bucket myazure:my-container \
  --include "images/*.jpg" \
  --exclude "*"
```

---

## 数据查看与校验

**基本写法：列出文件**
`rclone ls <远程>:<路径>`
```bash
# 列出 S3 桶内所有文件
rclone ls mys3:my-bucket
```

---

**基本写法：列出大小**
`rclone lsl <远程>:<路径>`
```bash
# 列出文件含大小和修改时间
rclone lsl mygcs:my-bucket/data
```

---

**基本写法：树形显示**
`rclone tree <远程>:<路径>`
```bash
# 树形结构展示目录
rclone tree mys3:my-bucket
```

---

**基本写法：计算大小**
`rclone size <远程>:<路径>`
```bash
# 计算目录总大小与文件数
rclone size mys3:my-bucket
```

---

**基本写法：校验数据完整性**
`rclone check <源> <目标>`
```bash
# 校验源和目标文件是否一致
rclone check mys3:my-bucket myazure:my-container --download
```

---

**基本写法：对比差异**
`rclone check <源> <目标> --one-way`
```bash
# 仅检查源比目标多的文件
rclone check mys3:my-bucket myazure:my-container --one-way
```

---

## 跨云迁移实战

**基本写法：AWS 到 GCP 迁移**
`rclone sync mys3:source-bucket mygcs:target-bucket --transfers <并发> --checkers <并发>`
```bash
# 高并发迁移大量文件
rclone sync mys3:source-bucket mygcs:target-bucket \
  --transfers 32 \
  --checkers 16 \
  --progress \
  --stats 30s
```

---

**基本写法：Azure 到 AWS 迁移**
`rclone sync myazure:container mys3:bucket --retries <次数>`
```bash
# 带重试机制的迁移
rclone sync myazure:my-container mys3:my-bucket \
  --retries 5 \
  --low-level-retries 10 \
  --progress
```

---

**基本写法：迁移带带宽限制**
`rclone sync <源> <目标> --bwlimit <带宽>`
```bash
# 限制带宽 10MB/s 避免影响业务
rclone sync mys3:my-bucket myazure:my-container \
  --bwlimit 10M \
  --progress
```

---

**基本写法：迁移大型数据集**
`rclone sync <源> <目标> --s3-chunk-size <大小> --s3-upload-concurrency <并发>`
```bash
# 优化大文件迁移
rclone sync mys3:source mygcs:target \
  --s3-chunk-size 256M \
  --s3-upload-concurrency 8 \
  --transfers 16 \
  --progress
```

---

**基本写法：迁移并保留元数据**
`rclone sync <源> <目标> --metadata`
```bash
# 保留所有元数据(ACL、时间戳)
rclone sync mys3:my-bucket myazure:my-container \
  --metadata \
  --progress
```

---

## 数据备份策略

**基本写法：定时备份脚本**
```bash
#!/bin/bash
# daily-backup.sh 每日备份脚本
set -e

DATE=$(date +%Y%m%d)
SOURCE="mys3:production-data"
DEST="myazure:backup/$DATE"

# 执行同步备份
rclone sync $SOURCE $DEST \
  --progress \
  --log-file /var/log/rclone-backup.log \
  --transfers 16

# 删除 30 天前的备份
rclone delete myazure:backup/ --min-age 30d
echo "Backup completed: $DATE"
```

---

**基本写法：使用 systemd timer 调度**
```ini
# /etc/systemd/system/rclone-backup.timer
[Unit]
Description=Daily rclone backup

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

---

**基本写法：服务定义**
```ini
# /etc/systemd/system/rclone-backup.service
[Unit]
Description=Run rclone backup
After=network-online.target

[Service]
Type=oneshot
ExecStart=/opt/scripts/daily-backup.sh
User=backup
```

---

**基本写法：加密备份**
`rclone sync <源> <加密目标> --crypt-remote <远程> --crypt-directory-name <目录>`
```ini
# rclone.conf 配置加密远程
[backup-encrypted]
type = crypt
remote = myazure:encrypted-backup
filename_encryption = standard
directory_name_encryption = true
password = MyEncryptedPassword123
password2 = MySaltForEncryption123
```

---

**基本写法：解密恢复**
`rclone copy <加密远程>:<路径> <本地路径>`
```bash
# 从加密备份恢复数据
rclone copy backup-encrypted:2026-07-31 /tmp/restored --progress
```

---

## Velero 跨云 K8s 迁移

**基本写法：安装 Velero**
`velero install --provider <提供者> --bucket <桶> --secret-file <凭证文件>`
```bash
# 安装 Velero 备份工具
velero install \
  --provider aws \
  --bucket velero-backups \
  --backup-location-config region=us-east-1 \
  --snapshot-location-config region=us-east-1 \
  --secret-file credentials-velero
```

---

**基本写法：创建备份**
`velero backup create <备份名> [--include-namespaces <命名空间>]`
```bash
# 备份指定命名空间
velero backup create my-backup --include-namespaces production
```

---

**基本写法：查看备份状态**
`velero backup describe <备份名>`
```bash
# 查看备份详情
velero backup describe my-backup --details
```

---

**基本写法：从备份恢复**
`velero restore create --from-backup <备份名>`
```bash
# 在目标集群恢复备份
velero restore create --from-backup my-backup
```

---

**基本写法：跨集群迁移**
```bash
# 源集群:创建备份到对象存储
velero backup create cluster-migration --include-cluster-resources=true

# 目标集群:配置相同的备份位置后恢复
velero restore create --from-backup cluster-migration
```

---

## 跨云镜像迁移

**基本写法：拉取镜像**
`docker pull <源镜像>`
```bash
# 拉取 Docker Hub 镜像
docker pull nginx:1.25
```

---

**基本写法：打标签到目标仓库**
`docker tag <源镜像> <目标仓库>/<镜像>:<标签>`
```bash
# 为推送到 ECR 准备标签
docker tag nginx:1.25 123456789012.dkr.ecr.us-east-1.amazonaws.com/nginx:1.25
```

---

**基本写法：推送镜像**
`docker push <目标仓库>/<镜像>:<标签>`
```bash
# 推送到 AWS ECR
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/nginx:1.25
```

---

**基本写法：使用 skopeo 跨仓库复制**
`skopeo copy docker://<源> docker://<目标>`
```bash
# 直接在仓库间复制镜像(无需本地拉取)
skopeo copy \
  docker://docker.io/nginx:1.25 \
  docker://123456789012.dkr.ecr.us-east-1.amazonaws.com/nginx:1.25
```

---

**基本写法：跨云批量迁移镜像**
```bash
#!/bin/bash
# migrate-images.sh 批量迁移镜像
IMAGES=(
  "nginx:1.25"
  "redis:7.2"
  "postgres:16"
)
SOURCE="docker.io"
TARGET="123456789012.dkr.ecr.us-east-1.amazonaws.com"

for img in "${IMAGES[@]}"; do
  echo "Migrating $img..."
  skopeo copy \
    docker://$SOURCE/$img \
    docker://$TARGET/$img \
    --dest-creds AWS:$(aws ecr get-login-password)
done
```

---

## 跨云数据库迁移

**基本写法：AWS DMS 创建复制实例**
`aws dms create-replication-instance --replication-instance-identifier <ID> --replication-instance-class <类>`
```bash
# 创建 DMS 复制实例
aws dms create-replication-instance \
  --replication-instance-identifier my-dms \
  --replication-instance-class dms.r5.large \
  --allocated-storage 100
```

---

**基本写法：创建端点**
`aws dms create-endpoint --endpoint-identifier <ID> --endpoint-type <类型> --engine-name <引擎> --server-name <服务器> --port <端口>`
```bash
# 创建源端 PostgreSQL 端点
aws dms create-endpoint \
  --endpoint-identifier source-pg \
  --endpoint-type source \
  --engine-name postgres \
  --server-name pg.source.com \
  --port 5432 \
  --database-name mydb \
  --username admin \
  --password 'Pass123!'
```

---

**基本写法：创建迁移任务**
`aws dms create-replication-task --replication-task-identifier <ID> --source-endpoint-arn <源> --target-endpoint-arn <目标> --replication-instance-arn <实例> --migration-type <类型>`
```bash
# 创建全量+CDC 迁移任务
aws dms create-replication-task \
  --replication-task-identifier my-migration \
  --source-endpoint-arn arn:aws:dms:us-east-1:123456789012:endpoint:ABC \
  --target-endpoint-arn arn:aws:dms:us-east-1:123456789012:endpoint:DEF \
  --replication-instance-arn arn:aws:dms:us-east-1:123456789012:rep:GHI \
  --migration-type full-load-and-cdc \
  --table-mappings file://mappings.json
```

---

**基本写法：启动迁移任务**
`aws dms start-replication-task --replication-task-arn <ARN> --start-replication-task-type start-replication`
```bash
# 启动数据库迁移任务
aws dms start-replication-task \
  --replication-task-arn arn:aws:dms:us-east-1:123456789012:task:XYZ \
  --start-replication-task-type start-replication
```

---

**基本写法：查看任务状态**
`aws dms describe-replication-tasks`
```bash
# 查看所有迁移任务
aws dms describe-replication-tasks
```

---

## 跨云 IaC 工具

**基本写法：Terraform 多云 provider 配置**
```hcl
# 多云部署的 Terraform 配置
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "azurerm" {
  features {}
}

provider "google" {
  project = "my-project-123"
  region  = "us-central1"
}
```

---

**基本写法：跨云相同资源定义**
```hcl
# 在三云创建相同规格的虚拟机
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"
  tags = { Name = "web-server" }
}

resource "azurerm_linux_virtual_machine" "web" {
  name                = "web-server"
  resource_group_name = azurerm_resource_group.main.name
  location            = "East US"
  size                = "Standard_B1s"
  admin_username      = "adminuser"
}

resource "google_compute_instance" "web" {
  name         = "web-server"
  machine_type = "e2-medium"
  zone         = "us-central1-a"
}
```

---

**基本写法：使用 Terragrunt 多环境管理**
```hcl
# env/prod/terragrunt.hcl
terraform {
  source = "../../modules/web-server"
}

inputs = {
  instance_count = 5
  instance_type  = "t3.large"
  environment    = "production"
}
```

---

**基本写法：跨云状态后端**
```hcl
# 使用 HCP Terraform Cloud 作为统一后端
terraform {
  cloud {
    organization = "my-org"
    workspaces {
      name = "multi-cloud-prod"
    }
  }
}
```

---

## 监控与告警

**基本写法：rclone 同步状态检查脚本**
```bash
#!/bin/bash
# check-sync.sh 检查同步状态
LOG_FILE="/var/log/rclone-backup.log"
ERROR_COUNT=$(grep -c "ERROR" $LOG_FILE)
SUCCESS_COUNT=$(grep -c "Sync successful" $LOG_FILE)

if [ $ERROR_COUNT -gt 0 ]; then
  echo "WARNING: $ERROR_COUNT errors found in last sync"
  exit 1
fi
echo "OK: Last sync completed successfully"
```

---

**基本写法：跨云成本对比**
```bash
# 使用 Infracost 估算多云成本
infracost breakdown --path . --format json > costs.json
# 查看各云资源成本
jq '.projects[].breakdown.resources[] | {address, monthlyCost}' costs.json
```

---

**基本写法：Cloud Custodian 多云策略**
```yaml
# custodian.yml 多云资源策略
policies:
  - name: aws-unused-eips
    resource: aws.elastic-ip
    filters:
      - AssociationId: absent
    actions:
      - delete
  - name: azure-unattached-disks
    resource: azure.disk
    filters:
      - type: value
        key: managedBy
        value: null
    actions:
      - type: delete
```

---

**基本写法：运行 Custodian**
`custodian run -s <输出> <策略文件>`
```bash
# 执行多云合规策略
custodian run -s output custodian.yml
```

<!-- ============ 文档分隔线：034-cloud-computing/027-LoadBalanceAutoScaling.md ============ -->

## 1. 负载均衡

### 1.1 ALB 应用层

ALB 应用层是负载均衡与自动伸缩的重要组成部分。本节详细介绍ALB 应用层的核心概念、工作原理和实际应用。

**关键要点**：

- ALB 应用层的定义与核心原理
- ALB 应用层的实现方式与技术细节
- ALB 应用层在实际场景中的应用与最佳实践
- ALB 应用层的常见问题与解决方案

ALB 应用层在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 NLB 网络层

NLB 网络层是负载均衡与自动伸缩的重要组成部分。本节详细介绍NLB 网络层的核心概念、工作原理和实际应用。

**关键要点**：

- NLB 网络层的定义与核心原理
- NLB 网络层的实现方式与技术细节
- NLB 网络层在实际场景中的应用与最佳实践
- NLB 网络层的常见问题与解决方案

NLB 网络层在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 CLB 经典

CLB 经典是负载均衡与自动伸缩的重要组成部分。本节详细介绍CLB 经典的核心概念、工作原理和实际应用。

**关键要点**：

- CLB 经典的定义与核心原理
- CLB 经典的实现方式与技术细节
- CLB 经典在实际场景中的应用与最佳实践
- CLB 经典的常见问题与解决方案

CLB 经典在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Auto Scaling

### 2.1 启动模板

启动模板是负载均衡与自动伸缩的重要组成部分。本节详细介绍启动模板的核心概念、工作原理和实际应用。

**关键要点**：

- 启动模板的定义与核心原理
- 启动模板的实现方式与技术细节
- 启动模板在实际场景中的应用与最佳实践
- 启动模板的常见问题与解决方案

启动模板在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 伸缩策略

伸缩策略是负载均衡与自动伸缩的重要组成部分。本节详细介绍伸缩策略的核心概念、工作原理和实际应用。

**关键要点**：

- 伸缩策略的定义与核心原理
- 伸缩策略的实现方式与技术细节
- 伸缩策略在实际场景中的应用与最佳实践
- 伸缩策略的常见问题与解决方案

伸缩策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 目标追踪

目标追踪是负载均衡与自动伸缩的重要组成部分。本节详细介绍目标追踪的核心概念、工作原理和实际应用。

**关键要点**：

- 目标追踪的定义与核心原理
- 目标追踪的实现方式与技术细节
- 目标追踪在实际场景中的应用与最佳实践
- 目标追踪的常见问题与解决方案

目标追踪在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 健康检查

### 3.1 EC2 健康检查

EC2 健康检查是负载均衡与自动伸缩的重要组成部分。本节详细介绍EC2 健康检查的核心概念、工作原理和实际应用。

**关键要点**：

- EC2 健康检查的定义与核心原理
- EC2 健康检查的实现方式与技术细节
- EC2 健康检查在实际场景中的应用与最佳实践
- EC2 健康检查的常见问题与解决方案

EC2 健康检查在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 ELB 健康检查

ELB 健康检查是负载均衡与自动伸缩的重要组成部分。本节详细介绍ELB 健康检查的核心概念、工作原理和实际应用。

**关键要点**：

- ELB 健康检查的定义与核心原理
- ELB 健康检查的实现方式与技术细节
- ELB 健康检查在实际场景中的应用与最佳实践
- ELB 健康检查的常见问题与解决方案

ELB 健康检查在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 最佳实践

### 4.1 预热策略

预热策略是负载均衡与自动伸缩的重要组成部分。本节详细介绍预热策略的核心概念、工作原理和实际应用。

**关键要点**：

- 预热策略的定义与核心原理
- 预热策略的实现方式与技术细节
- 预热策略在实际场景中的应用与最佳实践
- 预热策略的常见问题与解决方案

预热策略在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 容量预留

容量预留是负载均衡与自动伸缩的重要组成部分。本节详细介绍容量预留的核心概念、工作原理和实际应用。

**关键要点**：

- 容量预留的定义与核心原理
- 容量预留的实现方式与技术细节
- 容量预留在实际场景中的应用与最佳实践
- 容量预留的常见问题与解决方案

容量预留在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：034-cloud-computing/028-ServerlessArchitecture.md ============ -->

## 1. Serverless 原理

### 1.1 FaaS 与 BaaS

FaaS 与 BaaS是无服务器架构的重要组成部分。本节详细介绍FaaS 与 BaaS的核心概念、工作原理和实际应用。

**关键要点**：

- FaaS 与 BaaS的定义与核心原理
- FaaS 与 BaaS的实现方式与技术细节
- FaaS 与 BaaS在实际场景中的应用与最佳实践
- FaaS 与 BaaS的常见问题与解决方案

FaaS 与 BaaS在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 事件驱动模型

事件驱动模型是无服务器架构的重要组成部分。本节详细介绍事件驱动模型的核心概念、工作原理和实际应用。

**关键要点**：

- 事件驱动模型的定义与核心原理
- 事件驱动模型的实现方式与技术细节
- 事件驱动模型在实际场景中的应用与最佳实践
- 事件驱动模型的常见问题与解决方案

事件驱动模型在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. Lambda 优化

### 2.1 冷启动原因

冷启动原因是无服务器架构的重要组成部分。本节详细介绍冷启动原因的核心概念、工作原理和实际应用。

**关键要点**：

- 冷启动原因的定义与核心原理
- 冷启动原因的实现方式与技术细节
- 冷启动原因在实际场景中的应用与最佳实践
- 冷启动原因的常见问题与解决方案

冷启动原因在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 预留并发

预留并发是无服务器架构的重要组成部分。本节详细介绍预留并发的核心概念、工作原理和实际应用。

**关键要点**：

- 预留并发的定义与核心原理
- 预留并发的实现方式与技术细节
- 预留并发在实际场景中的应用与最佳实践
- 预留并发的常见问题与解决方案

预留并发在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Provisioned Concurrency

Provisioned Concurrency是无服务器架构的重要组成部分。本节详细介绍Provisioned Concurrency的核心概念、工作原理和实际应用。

**关键要点**：

- Provisioned Concurrency的定义与核心原理
- Provisioned Concurrency的实现方式与技术细节
- Provisioned Concurrency在实际场景中的应用与最佳实践
- Provisioned Concurrency的常见问题与解决方案

Provisioned Concurrency在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. Serverless Framework

### 3.1 项目结构

项目结构是无服务器架构的重要组成部分。本节详细介绍项目结构的核心概念、工作原理和实际应用。

**关键要点**：

- 项目结构的定义与核心原理
- 项目结构的实现方式与技术细节
- 项目结构在实际场景中的应用与最佳实践
- 项目结构的常见问题与解决方案

项目结构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 部署与回滚

部署与回滚是无服务器架构的重要组成部分。本节详细介绍部署与回滚的核心概念、工作原理和实际应用。

**关键要点**：

- 部署与回滚的定义与核心原理
- 部署与回滚的实现方式与技术细节
- 部署与回滚在实际场景中的应用与最佳实践
- 部署与回滚的常见问题与解决方案

部署与回滚在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 架构模式

### 4.1 API Gateway + Lambda

API Gateway + Lambda是无服务器架构的重要组成部分。本节详细介绍API Gateway + Lambda的核心概念、工作原理和实际应用。

**关键要点**：

- API Gateway + Lambda的定义与核心原理
- API Gateway + Lambda的实现方式与技术细节
- API Gateway + Lambda在实际场景中的应用与最佳实践
- API Gateway + Lambda的常见问题与解决方案

API Gateway + Lambda在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 事件管道

事件管道是无服务器架构的重要组成部分。本节详细介绍事件管道的核心概念、工作原理和实际应用。

**关键要点**：

- 事件管道的定义与核心原理
- 事件管道的实现方式与技术细节
- 事件管道在实际场景中的应用与最佳实践
- 事件管道的常见问题与解决方案

事件管道在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 限制与对策

限制与对策是无服务器架构的重要组成部分。本节详细介绍限制与对策的核心概念、工作原理和实际应用。

**关键要点**：

- 限制与对策的定义与核心原理
- 限制与对策的实现方式与技术细节
- 限制与对策在实际场景中的应用与最佳实践
- 限制与对策的常见问题与解决方案

限制与对策在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。
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

<!-- ============ 文档分隔线：034-cloud-computing/029-CloudMigration6RStrategy.md ============ -->

## 1. 6R 策略概述

### 1.1 Rehost 重新托管

Rehost 重新托管是云迁移6R策略的重要组成部分。本节详细介绍Rehost 重新托管的核心概念、工作原理和实际应用。

**关键要点**：

- Rehost 重新托管的定义与核心原理
- Rehost 重新托管的实现方式与技术细节
- Rehost 重新托管在实际场景中的应用与最佳实践
- Rehost 重新托管的常见问题与解决方案

Rehost 重新托管在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.2 Replatform 平台替换

Replatform 平台替换是云迁移6R策略的重要组成部分。本节详细介绍Replatform 平台替换的核心概念、工作原理和实际应用。

**关键要点**：

- Replatform 平台替换的定义与核心原理
- Replatform 平台替换的实现方式与技术细节
- Replatform 平台替换在实际场景中的应用与最佳实践
- Replatform 平台替换的常见问题与解决方案

Replatform 平台替换在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 1.3 Repurchase 重新购买

Repurchase 重新购买是云迁移6R策略的重要组成部分。本节详细介绍Repurchase 重新购买的核心概念、工作原理和实际应用。

**关键要点**：

- Repurchase 重新购买的定义与核心原理
- Repurchase 重新购买的实现方式与技术细节
- Repurchase 重新购买在实际场景中的应用与最佳实践
- Repurchase 重新购买的常见问题与解决方案

Repurchase 重新购买在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 2. 深度改造

### 2.1 Refactor 重构

Refactor 重构是云迁移6R策略的重要组成部分。本节详细介绍Refactor 重构的核心概念、工作原理和实际应用。

**关键要点**：

- Refactor 重构的定义与核心原理
- Refactor 重构的实现方式与技术细节
- Refactor 重构在实际场景中的应用与最佳实践
- Refactor 重构的常见问题与解决方案

Refactor 重构在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.2 Retire 退役

Retire 退役是云迁移6R策略的重要组成部分。本节详细介绍Retire 退役的核心概念、工作原理和实际应用。

**关键要点**：

- Retire 退役的定义与核心原理
- Retire 退役的实现方式与技术细节
- Retire 退役在实际场景中的应用与最佳实践
- Retire 退役的常见问题与解决方案

Retire 退役在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 2.3 Retain 保留

Retain 保留是云迁移6R策略的重要组成部分。本节详细介绍Retain 保留的核心概念、工作原理和实际应用。

**关键要点**：

- Retain 保留的定义与核心原理
- Retain 保留的实现方式与技术细节
- Retain 保留在实际场景中的应用与最佳实践
- Retain 保留的常见问题与解决方案

Retain 保留在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 3. 迁移评估

### 3.1 应用画像

应用画像是云迁移6R策略的重要组成部分。本节详细介绍应用画像的核心概念、工作原理和实际应用。

**关键要点**：

- 应用画像的定义与核心原理
- 应用画像的实现方式与技术细节
- 应用画像在实际场景中的应用与最佳实践
- 应用画像的常见问题与解决方案

应用画像在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.2 TCO 分析

TCO 分析是云迁移6R策略的重要组成部分。本节详细介绍TCO 分析的核心概念、工作原理和实际应用。

**关键要点**：

- TCO 分析的定义与核心原理
- TCO 分析的实现方式与技术细节
- TCO 分析在实际场景中的应用与最佳实践
- TCO 分析的常见问题与解决方案

TCO 分析在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 3.3 风险评估

风险评估是云迁移6R策略的重要组成部分。本节详细介绍风险评估的核心概念、工作原理和实际应用。

**关键要点**：

- 风险评估的定义与核心原理
- 风险评估的实现方式与技术细节
- 风险评估在实际场景中的应用与最佳实践
- 风险评估的常见问题与解决方案

风险评估在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

## 4. 迁移执行

### 4.1 分批迁移

分批迁移是云迁移6R策略的重要组成部分。本节详细介绍分批迁移的核心概念、工作原理和实际应用。

**关键要点**：

- 分批迁移的定义与核心原理
- 分批迁移的实现方式与技术细节
- 分批迁移在实际场景中的应用与最佳实践
- 分批迁移的常见问题与解决方案

分批迁移在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.2 数据迁移

数据迁移是云迁移6R策略的重要组成部分。本节详细介绍数据迁移的核心概念、工作原理和实际应用。

**关键要点**：

- 数据迁移的定义与核心原理
- 数据迁移的实现方式与技术细节
- 数据迁移在实际场景中的应用与最佳实践
- 数据迁移的常见问题与解决方案

数据迁移在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

### 4.3 切换验证

切换验证是云迁移6R策略的重要组成部分。本节详细介绍切换验证的核心概念、工作原理和实际应用。

**关键要点**：

- 切换验证的定义与核心原理
- 切换验证的实现方式与技术细节
- 切换验证在实际场景中的应用与最佳实践
- 切换验证的常见问题与解决方案

切换验证在工程实践中需要根据具体场景选择合适的策略，平衡性能、可靠性和复杂度。

<!-- ============ 文档分隔线：034-cloud-computing/030-AWSCliConfigure.md ============ -->

## 安装与版本

**基本写法：安装 AWS CLI**
`pip install awscli` 或 `brew install awscli`
```bash
# 通过 pip 安装 AWS CLI v2
pip install awscliv2
```

---

**基本写法：查看版本**
`aws --version`
```bash
# 输出 CLI 版本与依赖库版本
aws --version
```

---

**基本写法：升级 CLI**
`pip install --upgrade awscli`
```bash
# 升级到最新版本
pip install --upgrade awscli
```

---

## 凭证配置

**基本写法：交互式配置**
`aws configure [--profile <配置名>]`
```bash
# 配置默认账户的密钥与区域
aws configure
```

---

**基本写法：配置命名 Profile**
`aws configure --profile <配置名>`
```bash
# 为生产环境创建独立配置
aws configure --profile production
```

---

**基本写法：设置单项配置值**
`aws configure set <键> <值> [--profile <配置名>]`
```bash
# 设置默认区域为 us-west-2
aws configure set region us-west-2
```

---

**基本写法：查看当前配置**
`aws configure list [--profile <配置名>]`
```bash
# 列出当前所有配置项
aws configure list
```

---

**基本写法：通过环境变量配置**
`export AWS_<KEY>=<值>`
```bash
# 设置访问密钥与默认区域
export AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
```

---

## 身份验证

**基本写法：获取当前调用者身份**
`aws sts get-caller-identity [--profile <配置名>]`
```bash
# 验证当前凭证对应的账号与用户
aws sts get-caller-identity
```

---

**基本写法：切换默认 Profile**
`export AWS_PROFILE=<配置名>`
```bash
# 切换默认使用 production profile
export AWS_PROFILE=production
```

---

## 输出格式

**基本写法：指定输出格式**
`aws <命令> --output <json|table|text>`
```bash
# 以表格形式输出 EC2 实例
aws ec2 describe-instances --output table
```

---

**基本写法：使用 JMESPath 查询过滤**
`aws <命令> --query '<JMESPath 表达式>'`
```bash
# 仅提取实例 ID
aws ec2 describe-instances --query 'Reservations[0].Instances[0].InstanceId' --output text
```

---

**基本写法：查看配置文件位置**
`cat ~/.aws/credentials`
```bash
# 查看本地凭证文件内容
cat ~/.aws/credentials
```

---

**基本写法：列出所有 Profile**
`cat ~/.aws/config`
```bash
# 查看所有命名 profile 配置
cat ~/.aws/config
```

<!-- ============ 文档分隔线：034-cloud-computing/031-AWSS3Command.md ============ -->

## 桶操作

**基本写法：列出所有桶**
`aws s3 ls [--profile <配置名>]`
```bash
# 列出当前账号下所有 S3 桶
aws s3 ls
```

---

**基本写法：创建桶**
`aws s3 mb s3://<桶名> [--region <区域>]`
```bash
# 在默认区域创建新桶
aws s3 mb s3://my-unique-bucket
```

---

**基本写法：指定区域创建桶**
`aws s3 mb s3://<桶名> --region <区域>`
```bash
# 在 eu-west-1 区域创建桶
aws s3 mb s3://my-bucket --region eu-west-1
```

---

**基本写法：删除空桶**
`aws s3 rb s3://<桶名>`
```bash
# 仅删除空桶
aws s3 rb s3://my-bucket
```

---

**基本写法：强制删除非空桶**
`aws s3 rb s3://<桶名> --force`
```bash
# 删除桶及其所有对象
aws s3 rb s3://my-bucket --force
```

---

## 对象操作

**基本写法：列出桶内对象**
`aws s3 ls s3://<桶名>[/<前缀>] [--recursive]`
```bash
# 递归列出桶内所有对象
aws s3 ls s3://my-bucket --recursive
```

---

**基本写法：上传文件**
`aws s3 cp <本地文件> s3://<桶名>/[<路径>]`
```bash
# 上传单个文件到 S3
aws s3 cp file.txt s3://my-bucket/
```

---

**基本写法：下载文件**
`aws s3 cp s3://<桶名>/<键> <本地路径>`
```bash
# 从 S3 下载文件到本地
aws s3 cp s3://my-bucket/file.txt ./
```

---

**基本写法：递归上传目录**
`aws s3 cp <本地目录> s3://<桶名>/<前缀> --recursive`
```bash
# 递归上传整个目录
aws s3 cp ./folder s3://my-bucket/folder --recursive
```

---

**基本写法：同步本地到 S3**
`aws s3 sync <本地目录> s3://<桶名>/<前缀> [--delete] [--exclude <模式>]`
```bash
# 同步并删除目标中多余的文件
aws s3 sync ./src s3://my-bucket/src --delete --exclude "*.tmp"
```

---

**基本写法：删除单个对象**
`aws s3 rm s3://<桶名>/<键>`
```bash
# 删除指定对象
aws s3 rm s3://my-bucket/file.txt
```

---

**基本写法：递归删除目录**
`aws s3 rm s3://<桶名>/<前缀> --recursive`
```bash
# 递归删除目录下所有对象
aws s3 rm s3://my-bucket/folder --recursive
```

---

## 高级 API

**基本写法：使用 s3api 创建桶**
`aws s3api create-bucket --bucket <桶名> [--region <区域>]`
```bash
# 通过 s3api 精细控制创建桶
aws s3api create-bucket --bucket my-bucket --region us-east-1
```

---

**基本写法：获取桶大小统计**
`aws s3 ls s3://<桶名> --recursive --summarize`
```bash
# 统计桶内对象总数与总大小
aws s3 ls s3://my-bucket --recursive --summarize
```

---

**基本写法：预览操作不实际执行**
`<命令> --dryrun`
```bash
# 预览同步将执行的更改
aws s3 sync ./src s3://my-bucket/src --dryrun
```

<!-- ============ 文档分隔线：034-cloud-computing/032-AWSEC2Command.md ============ -->

## 实例查询

**基本写法：列出所有实例**
`aws ec2 describe-instances [--filters <过滤器>]`
```bash
# 列出当前账号所有 EC2 实例
aws ec2 describe-instances
```

---

**基本写法：过滤运行中实例**
`aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"`
```bash
# 仅列出 running 状态的实例
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"
```

---

**基本写法：查询指定字段**
`aws ec2 describe-instances --query '<JMESPath>' --output table`
```bash
# 提取实例 ID 类型状态公网 IP
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,InstanceType,State.Name,PublicIpAddress]' --output table
```

---

## 实例生命周期

**基本写法：启动新实例**
`aws ec2 run-instances --image-id <AMI> --instance-type <类型> [--key-name <密钥名>] [--security-group-ids <安全组ID>]`
```bash
# 启动一台 t2.micro 实例
aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --key-name my-key-pair
```

---

**基本写法：在 VPC 子网中启动**
`aws ec2 run-instances --image-id <AMI> --instance-type <类型> --subnet-id <子网ID> --security-group-ids <安全组ID>`
```bash
# 指定子网与安全组启动实例
aws ec2 run-instances --image-id ami-12345 --instance-type t3.small --subnet-id subnet-abc123 --security-group-ids sg-12345
```

---

**基本写法：启动已停止的实例**
`aws ec2 start-instances --instance-ids <实例ID>`
```bash
# 启动停止状态的实例
aws ec2 start-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：停止实例**
`aws ec2 stop-instances --instance-ids <实例ID>`
```bash
# 停止实例保留 EBS 卷
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：终止实例**
`aws ec2 terminate-instances --instance-ids <实例ID>`
```bash
# 永久终止实例并删除 EBS
aws ec2 terminate-instances --instance-ids i-1234567890abcdef0
```

---

**基本写法：重启实例**
`aws ec2 reboot-instances --instance-ids <实例ID>`
```bash
# 重启指定实例
aws ec2 reboot-instances --instance-ids i-1234567890abcdef0
```

---

## 密钥对

**基本写法：创建密钥对**
`aws ec2 create-key-pair --key-name <密钥名> --query 'KeyMaterial' --output text > <文件>`
```bash
# 创建密钥对并保存私钥到本地
aws ec2 create-key-pair --key-name my-new-key --query 'KeyMaterial' --output text > my-new-key.pem
```

---

**基本写法：列出密钥对**
`aws ec2 describe-key-pairs`
```bash
# 查看所有密钥对
aws ec2 describe-key-pairs
```

---

**基本写法：删除密钥对**
`aws ec2 delete-key-pair --key-name <密钥名>`
```bash
# 删除指定密钥对
aws ec2 delete-key-pair --key-name my-old-key
```

---

## 安全组

**基本写法：创建安全组**
`aws ec2 create-security-group --group-name <名称> --description <描述> [--vpc-id <VPC ID>]`
```bash
# 在指定 VPC 中创建安全组
aws ec2 create-security-group --group-name my-sg --description "My security group" --vpc-id vpc-12345
```

---

**基本写法：开放 SSH 端口**
`aws ec2 authorize-security-group-ingress --group-id <安全组ID> --protocol tcp --port 22 --cidr 0.0.0.0/0`
```bash
# 允许任意 IP 访问 22 端口
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 22 --cidr 0.0.0.0/0
```

---

**基本写法：开放 HTTP 端口**
`aws ec2 authorize-security-group-ingress --group-id <安全组ID> --protocol tcp --port 80 --cidr 0.0.0.0/0`
```bash
# 允许任意 IP 访问 80 端口
aws ec2 authorize-security-group-ingress --group-id sg-12345 --protocol tcp --port 80 --cidr 0.0.0.0/0
```

---

**基本写法：撤销入站规则**
`aws ec2 revoke-security-group-ingress --group-id <安全组ID> --protocol tcp --port 22 --cidr 0.0.0.0/0`
```bash
# 撤销 SSH 入站规则
aws ec2 revoke-security-group-ingress --group-id sg-12345 --protocol tcp --port 22 --cidr 0.0.0.0/0
```

---

## EBS 卷

**基本写法：列出卷**
`aws ec2 describe-volumes [--filters <过滤器>]`
```bash
# 列出所有 EBS 卷
aws ec2 describe-volumes
```

---

**基本写法：创建卷**
`aws ec2 create-volume --availability-zone <可用区> --size <GB>`
```bash
# 在 us-east-1a 创建 100GB 卷
aws ec2 create-volume --availability-zone us-east-1a --size 100
```

---

**基本写法：附加卷到实例**
`aws ec2 attach-volume --volume-id <卷ID> --instance-id <实例ID> --device <设备名>`
```bash
# 将卷附加为 /dev/sdf
aws ec2 attach-volume --volume-id vol-12345 --instance-id i-1234567890abcdef0 --device /dev/sdf
```

---

**基本写法：创建快照**
`aws ec2 create-snapshot --volume-id <卷ID> [--description <描述>]`
```bash
# 为卷创建快照备份
aws ec2 create-snapshot --volume-id vol-12345 --description "Volume backup"
```

---

## 弹性 IP

**基本写法：分配弹性 IP**
`aws ec2 allocate-address --domain vpc`
```bash
# 在 VPC 中分配弹性 IP
aws ec2 allocate-address --domain vpc
```

---

**基本写法：关联弹性 IP 到实例**
`aws ec2 associate-address --instance-id <实例ID> --allocation-id <分配ID>`
```bash
# 将弹性 IP 绑定到实例
aws ec2 associate-address --instance-id i-1234567890abcdef0 --allocation-id eipalloc-12345
```

---

**基本写法：释放弹性 IP**
`aws ec2 release-address --allocation-id <分配ID>`
```bash
# 释放未使用的弹性 IP
aws ec2 release-address --allocation-id eipalloc-12345
```

<!-- ============ 文档分隔线：034-cloud-computing/033-AWSLambdaCommand.md ============ -->

## 函数管理

**基本写法：列出函数**
`aws lambda list-functions [--region <区域>]`
```bash
# 列出当前区域所有 Lambda 函数
aws lambda list-functions
```

---

**基本写法：查看函数详情**
`aws lambda get-function --function-name <函数名>`
```bash
# 查看指定函数配置与代码位置
aws lambda get-function --function-name my-function
```

---

**基本写法：创建函数**
`aws lambda create-function --function-name <函数名> --runtime <运行时> --role <角色ARN> --handler <处理函数> --zip-file fileb://<zip 路径>`
```bash
# 创建 Python 函数
aws lambda create-function --function-name my-function --runtime python3.12 --role arn:aws:iam::123456789012:role/lambda-role --handler index.handler --zip-file fileb://function.zip
```

---

**基本写法：更新函数代码**
`aws lambda update-function-code --function-name <函数名> --zip-file fileb://<zip 路径>`
```bash
# 上传新的代码包
aws lambda update-function-code --function-name my-function --zip-file fileb://function.zip
```

---

**基本写法：更新函数配置**
`aws lambda update-function-configuration --function-name <函数名> [--timeout <秒>] [--memory-size <MB>]`
```bash
# 修改超时与内存配置
aws lambda update-function-configuration --function-name my-function --timeout 30 --memory-size 512
```

---

**基本写法：删除函数**
`aws lambda delete-function --function-name <函数名>`
```bash
# 删除指定 Lambda 函数
aws lambda delete-function --function-name my-function
```

---

## 函数调用

**基本写法：同步调用**
`aws lambda invoke --function-name <函数名> <输出文件>`
```bash
# 同步调用并保存响应到文件
aws lambda invoke --function-name my-function response.json
```

---

**基本写法：异步调用**
`aws lambda invoke --function-name <函数名> --invocation-type Event <输出文件>`
```bash
# 异步调用不等待返回
aws lambda invoke --function-name my-function --invocation-type Event response.json
```

---

**基本写法：传递 payload**
`aws lambda invoke --function-name <函数名> --payload fileb://<文件> <输出文件>`
```bash
# 通过文件传递 JSON 载荷
aws lambda invoke --function-name my-function --payload fileb://payload.json response.json
```

---

**基本写法：指定别名或版本**
`aws lambda invoke --function-name <函数名>:<限定符> <输出文件>`
```bash
# 调用 prod 别名的版本
aws lambda invoke --function-name my-function:prod response.json
```

---

## 版本与别名

**基本写法：发布版本**
`aws lambda publish-version --function-name <函数名>`
```bash
# 发布当前代码为新版本
aws lambda publish-version --function-name my-function
```

---

**基本写法：列出版本**
`aws lambda list-versions-by-function --function-name <函数名>`
```bash
# 查看所有已发布版本
aws lambda list-versions-by-function --function-name my-function
```

---

**基本写法：创建别名**
`aws lambda create-alias --function-name <函数名> --name <别名> --function-version <版本号>`
```bash
# 为版本 1 创建 prod 别名
aws lambda create-alias --function-name my-function --name prod --function-version 1
```

---

**基本写法：更新别名指向**
`aws lambda update-alias --function-name <函数名> --name <别名> --function-version <版本号>`
```bash
# 将 prod 别名切换到版本 2
aws lambda update-alias --function-name my-function --name prod --function-version 2
```

---

## 层管理

**基本写法：发布层**
`aws lambda publish-layer-version --layer-name <层名> --zip-file fileb://<zip 路径> --compatible-runtimes <运行时>`
```bash
# 发布 Python 依赖层
aws lambda publish-layer-version --layer-name my-deps --zip-file fileb://layer.zip --compatible-runtimes python3.12
```

---

**基本写法：列出层**
`aws lambda list-layers`
```bash
# 列出账号下所有层
aws lambda list-layers
```

---

**基本写法：为函数附加层**
`aws lambda update-function-configuration --function-name <函数名> --layers <层ARN>`
```bash
# 将层附加到函数
aws lambda update-function-configuration --function-name my-function --layers arn:aws:lambda:us-east-1:123456789012:layer:my-deps:1
```

---

## 日志查看

**基本写法：查看日志组**
`aws logs describe-log-groups --log-group-name-prefix /aws/lambda/<函数名>`
```bash
# 查看 Lambda 函数对应日志组
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/my-function
```

---

**基本写法：查看最近日志流**
`aws logs tail /aws/lambda/<函数名> [--since <时间>]`
```bash
# 查看最近 10 分钟的日志
aws logs tail /aws/lambda/my-function --since 10m
```

<!-- ============ 文档分隔线：034-cloud-computing/034-AWSIAMCommand.md ============ -->

## 用户管理

**基本写法：列出用户**
`aws iam list-users`
```bash
# 列出账号下所有 IAM 用户
aws iam list-users
```

---

**基本写法：创建用户**
`aws iam create-user --user-name <用户名>`
```bash
# 创建新的 IAM 用户
aws iam create-user --user-name john
```

---

**基本写法：删除用户**
`aws iam delete-user --user-name <用户名>`
```bash
# 删除指定 IAM 用户
aws iam delete-user --user-name john
```

---

**基本写法：查看用户详情**
`aws iam get-user --user-name <用户名>`
```bash
# 查看指定用户信息
aws iam get-user --user-name john
```

---

## 访问密钥

**基本写法：创建访问密钥**
`aws iam create-access-key --user-name <用户名>`
```bash
# 为用户生成新的访问密钥
aws iam create-access-key --user-name john
```

---

**基本写法：列出访问密钥**
`aws iam list-access-keys --user-name <用户名>`
```bash
# 查看用户的所有访问密钥 ID
aws iam list-access-keys --user-name john
```

---

**基本写法：停用访问密钥**
`aws iam update-access-key --access-key-id <密钥ID> --status Inactive --user-name <用户名>`
```bash
# 临时停用访问密钥
aws iam update-access-key --access-key-id AKIAIOSFODNN7EXAMPLE --status Inactive --user-name john
```

---

**基本写法：删除访问密钥**
`aws iam delete-access-key --access-key-id <密钥ID> --user-name <用户名>`
```bash
# 永久删除访问密钥
aws iam delete-access-key --access-key-id AKIAIOSFODNN7EXAMPLE --user-name john
```

---

## 策略管理

**基本写法：列出策略**
`aws iam list-policies [--scope Local]`
```bash
# 列出自定义策略
aws iam list-policies --scope Local
```

---

**基本写法：查看策略详情**
`aws iam get-policy --policy-arn <策略ARN>`
```bash
# 查看策略元数据
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：创建策略**
`aws iam create-policy --policy-name <策略名> --policy-document file://<文件>`
```bash
# 从 JSON 文件创建策略
aws iam create-policy --policy-name my-policy --policy-document file://policy.json
```

---

**基本写法：附加策略到用户**
`aws iam attach-user-policy --user-name <用户名> --policy-arn <策略ARN>`
```bash
# 为用户附加 S3 只读策略
aws iam attach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：分离策略**
`aws iam detach-user-policy --user-name <用户名> --policy-arn <策略ARN>`
```bash
# 从用户移除策略
aws iam detach-user-policy --user-name john --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

---

**基本写法：列出用户策略**
`aws iam list-attached-user-policies --user-name <用户名>`
```bash
# 查看用户附加的所有策略
aws iam list-attached-user-policies --user-name john
```

---

## 角色管理

**基本写法：创建角色**
`aws iam create-role --role-name <角色名> --assume-role-policy-document file://<文件>`
```bash
# 创建可被 Lambda 服务扮演的角色
aws iam create-role --role-name lambda-role --assume-role-policy-document file://trust-policy.json
```

---

**基本写法：列出角色**
`aws iam list-roles`
```bash
# 列出账号下所有角色
aws iam list-roles
```

---

**基本写法：附加策略到角色**
`aws iam attach-role-policy --role-name <角色名> --policy-arn <策略ARN>`
```bash
# 为角色附加执行策略
aws iam attach-role-policy --role-name lambda-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

---

## 用户组管理

**基本写法：创建用户组**
`aws iam create-group --group-name <组名>`
```bash
# 创建新的用户组
aws iam create-group --group-name developers
```

---

**基本写法：添加用户到组**
`aws iam add-user-to-group --group-name <组名> --user-name <用户名>`
```bash
# 将用户加入 developers 组
aws iam add-user-to-group --group-name developers --user-name john
```

---

**基本写法：列出组内用户**
`aws iam get-group --group-name <组名>`
```bash
# 查看 developers 组成员
aws iam get-group --group-name developers
```

<!-- ============ 文档分隔线：034-cloud-computing/035-AWSCloudFormation.md ============ -->

## 模板基础

**基本写法：YAML 模板结构**
```yaml
# CloudFormation 模板基本结构
AWSTemplateFormatVersion: '2010-09-09'
Description: My stack template
Resources:
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t2.micro
      ImageId: ami-0c55b159cbfafe1f0
```

---

**基本写法：定义参数**
```yaml
# 通过参数实现模板复用
Parameters:
  InstanceType:
    Type: String
    Default: t2.micro
    AllowedValues: [t2.micro, t2.small, t3.micro]
```

---

**基本写法：定义输出**
```yaml
# 输出资源属性便于跨栈引用
Outputs:
  InstanceId:
    Value: !Ref MyInstance
    Export:
      Name: my-stack-instance-id
```

---

## 栈管理

**基本写法：创建栈**
`aws cloudformation create-stack --stack-name <栈名> --template-body file://<文件>`
```bash
# 从本地 YAML 文件创建栈
aws cloudformation create-stack --stack-name myStack --template-body file://template.yaml
```

---

**基本写法：从 S3 模板创建栈**
`aws cloudformation create-stack --stack-name <栈名> --template-url https://s3.amazonaws.com/<桶>/<键>`
```bash
# 从 S3 上的模板创建栈
aws cloudformation create-stack --stack-name myStack --template-url https://s3.amazonaws.com/my-bucket/template.yaml
```

---

**基本写法：更新栈**
`aws cloudformation update-stack --stack-name <栈名> --template-body file://<文件>`
```bash
# 应用模板变更更新栈
aws cloudformation update-stack --stack-name myStack --template-body file://template.yaml
```

---

**基本写法：删除栈**
`aws cloudformation delete-stack --stack-name <栈名>`
```bash
# 删除栈及所有资源
aws cloudformation delete-stack --stack-name myStack
```

---

**基本写法：列出所有栈**
`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE`
```bash
# 列出已成功创建与更新的栈
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
```

---

**基本写法：查看栈详情**
`aws cloudformation describe-stacks --stack-name <栈名>`
```bash
# 查看栈状态与输出
aws cloudformation describe-stacks --stack-name myStack
```

---

## 变更集

**基本写法：创建变更集**
`aws cloudformation create-change-set --stack-name <栈名> --change-set-name <变更集名> --template-body file://<文件>`
```bash
# 预览变更生成变更集
aws cloudformation create-change-set --stack-name myStack --change-set-name my-change --template-body file://template.yaml
```

---

**基本写法：查看变更集**
`aws cloudformation describe-change-set --stack-name <栈名> --change-set-name <变更集名>`
```bash
# 查看变更集将要执行的操作
aws cloudformation describe-change-set --stack-name myStack --change-set-name my-change
```

---

**基本写法：执行变更集**
`aws cloudformation execute-change-set --stack-name <栈名> --change-set-name <变更集名>`
```bash
# 执行变更集中的操作
aws cloudformation execute-change-set --stack-name myStack --change-set-name my-change
```

---

## 事件与资源

**基本写法：查看栈事件**
`aws cloudformation describe-stack-events --stack-name <栈名>`
```bash
# 查看栈操作事件日志
aws cloudformation describe-stack-events --stack-name myStack
```

---

**基本写法：列出栈资源**
`aws cloudformation list-stack-resources --stack-name <栈名>`
```bash
# 查看栈内所有资源物理 ID
aws cloudformation list-stack-resources --stack-name myStack
```

---

## 验证与检查

**基本写法：验证模板**
`aws cloudformation validate-template --template-body file://<文件>`
```bash
# 检查模板语法是否正确
aws cloudformation validate-template --template-body file://template.yaml
```

---

**基本写法：估算栈费用**
`aws cloudformation estimate-template-cost --template-body file://<文件>`
```bash
# 估算模板部署后费用
aws cloudformation estimate-template-cost --template-body file://template.yaml
```

---

## 嵌套栈

**基本写法：嵌套栈资源**
```yaml
# 在主栈中嵌套子栈
Resources:
  NestedStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://s3.amazonaws.com/my-bucket/nested.yaml
      Parameters:
        Env: production
```

---

## Drift 检测

**基本写法：检测栈漂移**
`aws cloudformation detect-stack-drift --stack-name <栈名>`
```bash
# 检测栈是否被外部修改
aws cloudformation detect-stack-drift --stack-name myStack
```

---

**基本写法：查看漂移结果**
`aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id <检测ID>`
```bash
# 查看漂移检测进度与结果
aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id abc-123
```

<!-- ============ 文档分隔线：034-cloud-computing/036-AzureCliConfigure.md ============ -->

## 安装与版本

**基本写法：安装 Azure CLI**
`az` 或通过包管理器安装
```bash
# Windows 通过 winget 安装
winget install -e --id Microsoft.AzureCLI
```

---

**基本写法：查看版本**
`az version`
```bash
# 输出 CLI 版本与依赖库版本
az version
```

---

**基本写法：升级 CLI**
`az upgrade`
```bash
# 升级到最新版本
az upgrade
```

---

**基本写法：查看帮助**
`az [<命令组>] --help`
```bash
# 查看 vm 子命令帮助
az vm --help
```

---

**基本写法：模糊查找命令**
`az find "<关键词>"`
```bash
# 查找 role 相关命令
az find "az role"
```

---

## 登录认证

**基本写法：浏览器交互登录**
`az login`
```bash
# 通过浏览器进行交互式登录
az login
```

---

**基本写法：使用设备码登录**
`az login --use-device-code`
```bash
# 通过设备码进行双因素认证登录
az login --use-device-code
```

---

**基本写法：服务主体登录**
`az login --service-principal -u <应用ID> -p <密码或证书> --tenant <租户ID>`
```bash
# 通过服务主体登录便于脚本化
az login --service-principal -u 00000000-0000-0000-0000-000000000000 -p myPassword --tenant 00000000-0000-0000-0000-000000000000
```

---

**基本写法：登出**
`az logout [--username <用户名>]`
```bash
# 登出当前账号
az logout
```

---

## 订阅管理

**基本写法：列出订阅**
`az account list`
```bash
# 列出当前账号下所有订阅
az account list
```

---

**基本写法：列出订阅（简洁版）**
`az account subscription list`
```bash
# 列出租户下所有可用订阅
az account subscription list
```

---

**基本写法：设置当前订阅**
`az account set --subscription <订阅ID或名称>`
```bash
# 切换到指定订阅
az account set --subscription 0ad021f2-9dde-4cb1-8aa4-d71018aaeec8
```

---

**基本写法：查看当前订阅**
`az account show`
```bash
# 查看当前激活的订阅
az account show
```

---

## 配置管理

**基本写法：查看当前配置**
`az config get`
```bash
# 列出本地配置项
az config get
```

---

**基本写法：设置默认资源组**
`az config set defaults.group=<资源组名>`
```bash
# 设置默认资源组避免每次指定
az config set defaults.group=MyResourceGroup
```

---

**基本写法：关闭区域建议提示**
`az config set core.display_region_identified=no`
```bash
# 关闭区域推荐消息
az config set core.display_region_identified=no
```

---

## 输出格式

**基本写法：指定输出格式**
`az <命令> --output <json|table|tsv|yaml>`
```bash
# 以表格形式输出资源组
az group list --output table
```

---

**基本写法：使用 JMESPath 查询**
`az <命令> --query '<JMESPath 表达式>'`
```bash
# 仅提取资源组名称
az group list --query "[].name" --output tsv
```

---

**基本写法：列出可用区域**
`az account list-locations`
```bash
# 列出当前订阅支持的所有区域
az account list-locations
```

---

## 扩展管理

**基本写法：列出已安装扩展**
`az extension list`
```bash
# 查看已安装的 CLI 扩展
az extension list
```

---

**基本写法：安装扩展**
`az extension add --name <扩展名>`
```bash
# 安装特定扩展
az extension add --name azure-devops
```

---

**基本写法：移除扩展**
`az extension remove --name <扩展名>`
```bash
# 移除不再需要的扩展
az extension remove --name azure-devops
```

<!-- ============ 文档分隔线：034-cloud-computing/037-AzureGroupVMCommand.md ============ -->

## 资源组管理

**基本写法：创建资源组**
`az group create --name <资源组名> --location <区域>`
```bash
# 在 eastus 区域创建资源组
az group create --name MyResourceGroup --location eastus
```

---

**基本写法：列出所有资源组**
`az group list [--output table]`
```bash
# 以表格形式列出资源组
az group list --output table
```

---

**基本写法：查看资源组详情**
`az group show --name <资源组名>`
```bash
# 查看指定资源组信息
az group show --name MyResourceGroup
```

---

**基本写法：删除资源组**
`az group delete --name <资源组名> [--yes] [--no-wait]`
```bash
# 删除资源组及所有资源不等待
az group delete --name MyResourceGroup --yes --no-wait
```

---

**基本写法：按名称过滤资源组**
`az group list --query "[?starts_with(name, 'msdocs') == \`true\`].name" -o table`
```bash
# 列出以 msdocs 开头的资源组
az group list --query "[?starts_with(name, 'msdocs') == \`true\`].name" -o table
```

---

## 虚拟机创建

**基本写法：创建 Ubuntu VM**
`az vm create --resource-group <资源组名> --name <VM名> --image Ubuntu2204 [--admin-username <用户名>] [--generate-ssh-keys]`
```bash
# 创建 Ubuntu 22.04 VM 并自动生成 SSH 密钥
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --admin-username azureuser --generate-ssh-keys
```

---

**基本写法：指定镜像与大小创建**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --size <VM大小>`
```bash
# 创建 Standard_B2s 大小的 VM
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --size Standard_B2s
```

---

**基本写法：在 VNet 子网中创建**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --vnet-name <VNet名> --subnet <子网名>`
```bash
# 指定虚拟网络与子网创建 VM
az vm create --resource-group test-rg --name vm-public --image Ubuntu2204 --vnet-name vnet-1 --subnet subnet-public
```

---

**基本写法：使用已有 SSH 公钥**
`az vm create --resource-group <资源组名> --name <VM名> --image <镜像> --ssh-key-values <公钥路径>`
```bash
# 使用本地公钥创建 VM
az vm create --resource-group MyResourceGroup --name my-vm --image Ubuntu2204 --ssh-key-values ~/.ssh/id_rsa.pub
```

---

## VM 查询

**基本写法：列出所有 VM**
`az vm list [--resource-group <资源组名>] [-d]`
```bash
# 列出所有 VM 并显示电源状态
az vm list -d
```

---

**基本写法：查看 VM 详情**
`az vm show --resource-group <资源组名> --name <VM名>`
```bash
# 查看 VM 完整配置
az vm show --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：按创建时间过滤 VM**
`az vm list -d --query "[?timeCreated >= '2024-01-01'].[name, powerState]"`
```bash
# 查询 2024 年后创建的 VM
az vm list -d --query "[?timeCreated >= '2024-01-01'].[name, powerState]"
```

---

## VM 生命周期

**基本写法：启动 VM**
`az vm start --resource-group <资源组名> --name <VM名>`
```bash
# 启动已停止的 VM
az vm start --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：停止 VM**
`az vm stop --resource-group <资源组名> --name <VM名>`
```bash
# 停止运行中的 VM
az vm stop --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：分配（释放计算资源）**
`az vm deallocate --resource-group <资源组名> --name <VM名>`
```bash
# 释放 VM 不再产生计算费用
az vm deallocate --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：重启 VM**
`az vm restart --resource-group <资源组名> --name <VM名>`
```bash
# 重启指定 VM
az vm restart --resource-group MyResourceGroup --name my-vm
```

---

**基本写法：删除 VM**
`az vm delete --resource-group <资源组名> --name <VM名> [--yes]`
```bash
# 删除 VM 不询问确认
az vm delete --resource-group MyResourceGroup --name my-vm --yes
```

---

## VM 连接

**基本写法：获取 SSH 连接信息**
`az vm show --resource-group <资源组名> --name <VM名> -d --query publicIps -o tsv`
```bash
# 获取 VM 公网 IP 用于 SSH 连接
az vm show --resource-group MyResourceGroup --name my-vm -d --query publicIps -o tsv
```

---

**基本写法：打开端口**
`az vm open-port --resource-group <资源组名> --name <VM名> --port <端口>`
```bash
# 打开 80 端口入站
az vm open-port --resource-group MyResourceGroup --name my-vm --port 80
```

---

**基本写法：执行远程命令**
`az vm run-command invoke --resource-group <资源组名> --name <VM名> --command-id RunShellScript --scripts "<命令>"`
```bash
# 远程执行 shell 命令
az vm run-command invoke --resource-group MyResourceGroup --name my-vm --command-id RunShellScript --scripts "uptime"
```

---

## 磁盘管理

**基本写法：列出磁盘**
`az disk list --resource-group <资源组名>`
```bash
# 列出资源组下所有托管磁盘
az disk list --resource-group MyResourceGroup
```

---

**基本写法：创建磁盘**
`az disk create --resource-group <资源组名> --name <磁盘名> --size-gb <GB>`
```bash
# 创建 20GB 数据磁盘
az disk create --resource-group MyResourceGroup --name my-disk --size-gb 20
```

---

**基本写法：附加磁盘到 VM**
`az vm disk attach --resource-group <资源组名> --vm-name <VM名> --name <磁盘名>`
```bash
# 将现有磁盘附加到 VM
az vm disk attach --resource-group MyResourceGroup --vm-name my-vm --name my-disk
```

<!-- ============ 文档分隔线：034-cloud-computing/038-AzureStorageCommand.md ============ -->

## 存储账户

**基本写法：创建存储账户**
`az storage account create --resource-group <资源组名> --name <账户名> --location <区域> --sku <SKU>`
```bash
# 创建本地冗余存储账户
az storage account create --resource-group MyResourceGroup --name storage134 --location eastus --sku Standard_LRS
```

---

**基本写法：列出存储账户**
`az storage account list [--resource-group <资源组名>]`
```bash
# 列出当前订阅所有存储账户
az storage account list
```

---

**基本写法：查看账户详情**
`az storage account show --resource-group <资源组名> --name <账户名>`
```bash
# 查看存储账户属性
az storage account show --resource-group MyResourceGroup --name storage134
```

---

**基本写法：更新访问层**
`az storage account update --resource-group <资源组名> --name <账户名> --access-tier <Hot|Cool>`
```bash
# 设置访问层为 Hot
az storage account update --resource-group MyResourceGroup --name storage134 --access-tier Hot
```

---

**基本写法：获取账户密钥**
`az storage account keys list --resource-group <资源组名> --account-name <账户名>`
```bash
# 获取存储账户访问密钥
az storage account keys list --resource-group MyResourceGroup --account-name storage134
```

---

**基本写法：删除存储账户**
`az storage account delete --resource-group <资源组名> --name <账户名>`
```bash
# 删除存储账户
az storage account delete --resource-group MyResourceGroup --name storage134
```

---

## Blob 容器

**基本写法：创建容器**
`az storage container create --name <容器名> --account-name <账户名>`
```bash
# 在存储账户中创建 Blob 容器
az storage container create --name my-container --account-name storage134
```

---

**基本写法：列出容器**
`az storage container list --account-name <账户名>`
```bash
# 列出所有 Blob 容器
az storage container list --account-name storage134
```

---

**基本写法：列出容器内 Blob**
`az storage blob list --container-name <容器名> --account-name <账户名>`
```bash
# 列出容器内所有 Blob
az storage blob list --container-name my-container --account-name storage134
```

---

## Blob 操作

**基本写法：上传文件到 Blob**
`az storage blob upload --account-name <账户名> --container-name <容器名> --name <Blob名> --file <本地文件>`
```bash
# 上传本地文件到 Blob 容器
az storage blob upload --account-name storage134 --container-name my-container --name data.txt --file ./data.txt
```

---

**基本写法：上传时指定访问层**
`az storage blob upload --account-name <账户名> --container-name <容器名> --file <文件> --tier <层>`
```bash
# 上传并设置为 Hot 访问层
az storage blob upload --account-name storage134 --container-name my-container --file ./data.txt --tier Hot
```

---

**基本写法：下载 Blob**
`az storage blob download --account-name <账户名> --container-name <容器名> --name <Blob名> --file <本地文件>`
```bash
# 下载 Blob 到本地
az storage blob download --account-name storage134 --container-name my-container --name data.txt --file ./downloaded.txt
```

---

**基本写法：删除 Blob**
`az storage blob delete --account-name <账户名> --container-name <容器名> --name <Blob名>`
```bash
# 删除指定 Blob
az storage blob delete --account-name storage134 --container-name my-container --name data.txt
```

---

**基本写法：更改 Blob 访问层**
`az storage blob set-tier --account-name <账户名> --container-name <容器名> --name <Blob名> --tier <层>`
```bash
# 将 Blob 设置为 P10 高级层
az storage blob set-tier --account-name storage134 --container-name my-container --name data.txt --tier P10
```

---

## 连接字符串

**基本写法：获取连接字符串**
`az storage account show-connection-string --resource-group <资源组名> --name <账户名>`
```bash
# 获取用于应用配置的连接字符串
az storage account show-connection-string --resource-group MyResourceGroup --name storage134
```

---

**基本写法：使用连接字符串操作**
`az storage blob list --container-name <容器名> --connection-string "<连接字符串>"`
```bash
# 通过连接字符串列出 Blob
az storage blob list --container-name my-container --connection-string "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"
```

---

## 文件共享

**基本写法：创建文件共享**
`az storage share create --name <共享名> --account-name <账户名>`
```bash
# 创建 Azure 文件共享
az storage share create --name my-share --account-name storage134
```

---

**基本写法：上传文件到共享**
`az storage file upload --share-name <共享名> --source <本地文件> --account-name <账户名>`
```bash
# 上传文件到文件共享
az storage file upload --share-name my-share --source ./file.txt --account-name storage134
```

---

## 队列与表

**基本写法：创建队列**
`az storage queue create --name <队列名> --account-name <账户名>`
```bash
# 创建存储队列用于消息传递
az storage queue create --name my-queue --account-name storage134
```

---

**基本写法：向队列添加消息**
`az storage message put --queue-name <队列名> --content "<消息>" --account-name <账户名>`
```bash
# 向队列添加一条文本消息
az storage message put --queue-name my-queue --content "Hello" --account-name storage134
```

---

**基本写法：从队列取消息**
`az storage message get --queue-name <队列名> --account-name <账户名>`
```bash
# 取出队列中下一条消息
az storage message get --queue-name my-queue --account-name storage134
```

<!-- ============ 文档分隔线：034-cloud-computing/039-GCPCliConfigure.md ============ -->

## 安装与初始化

**基本写法：安装 gcloud CLI**
`sudo apt-get install -y google-cloud-cli`
```bash
# 在 Ubuntu 上通过官方源安装
sudo apt-get install -y google-cloud-cli
```

---

**基本写法：交互式初始化**
`gcloud init`
```bash
# 启动配置向导进行账号项目区域设置
gcloud init
```

---

**基本写法：查看安装信息**
`gcloud info`
```bash
# 显示 gcloud 安装路径与版本
gcloud info
```

---

**基本写法：查看版本**
`gcloud version`
```bash
# 输出 gcloud 及组件版本
gcloud version
```

---

**基本写法：升级组件**
`gcloud components update`
```bash
# 升级所有已安装组件
gcloud components update
```

---

## 认证登录

**基本写法：用户账号登录**
`gcloud auth login`
```bash
# 通过浏览器进行账号认证
gcloud auth login
```

---

**基本写法：应用默认凭证**
`gcloud auth application-default login`
```bash
# 为本地应用配置默认凭证
gcloud auth application-default login
```

---

**基本写法：列出已认证账号**
`gcloud auth list`
```bash
# 查看当前已登录账号列表
gcloud auth list
```

---

**基本写法：撤销认证**
`gcloud auth revoke [<账号>]`
```bash
# 撤销当前账号认证
gcloud auth revoke
```

---

## 项目管理

**基本写法：列出所有项目**
`gcloud projects list`
```bash
# 查看账号下所有项目
gcloud projects list
```

---

**基本写法：创建项目**
`gcloud projects create <项目ID>`
```bash
# 创建新项目
gcloud projects create my-new-project-123
```

---

**基本写法：查看项目详情**
`gcloud projects describe <项目ID>`
```bash
# 查看项目元数据
gcloud projects describe my-new-project-123
```

---

**基本写法：删除项目**
`gcloud projects delete <项目ID>`
```bash
# 删除指定项目
gcloud projects delete my-new-project-123
```

---

## 配置管理

**基本写法：列出当前配置**
`gcloud config list`
```bash
# 查看当前激活配置的属性
gcloud config list
```

---

**基本写法：设置默认项目**
`gcloud config set project <项目ID>`
```bash
# 设置默认项目避免每次指定
gcloud config set project my-project-id
```

---

**基本写法：设置默认区域**
`gcloud config set compute/region <区域>`
```bash
# 设置默认计算区域
gcloud config set compute/region us-central1
```

---

**基本写法：设置默认可用区**
`gcloud config set compute/zone <可用区>`
```bash
# 设置默认计算可用区
gcloud config set compute/zone us-central1-a
```

---

**基本写法：获取当前项目**
`gcloud config get-value project`
```bash
# 查看当前默认项目 ID
gcloud config get-value project
```

---

## 多配置管理

**基本写法：创建命名配置**
`gcloud config configurations create <配置名>`
```bash
# 创建独立配置用于多项目管理
gcloud config configurations create my-config
```

---

**基本写法：列出所有配置**
`gcloud config configurations list`
```bash
# 查看所有命名配置
gcloud config configurations list
```

---

**基本写法：切换激活配置**
`gcloud config configurations activate <配置名>`
```bash
# 切换到指定配置
gcloud config configurations activate my-config
```

---

**基本写法：查看当前配置名**
`gcloud config configurations describe <配置名>`
```bash
# 查看指定配置详情
gcloud config configurations describe my-config
```

---

## 组件管理

**基本写法：列出已安装组件**
`gcloud components list`
```bash
# 查看所有可用与已安装组件
gcloud components list
```

---

**基本写法：安装组件**
`gcloud components install <组件名>`
```bash
# 安装 kubectl 等额外组件
gcloud components install kubectl
```

---

**基本写法：移除组件**
`gcloud components remove <组件名>`
```bash
# 移除不再使用的组件
gcloud components remove kubectl
```

<!-- ============ 文档分隔线：034-cloud-computing/040-GCPComputeStorage.md ============ -->

## Compute Engine 实例

**基本写法：列出所有实例**
`gcloud compute instances list`
```bash
# 列出当前项目所有 VM 实例
gcloud compute instances list
```

---

**基本写法：创建实例**
`gcloud compute instances create <实例名> [--machine-type=<类型>] [--image-family=<镜像族>] [--image-project=<项目>]`
```bash
# 创建 e2-medium Ubuntu 22.04 实例
gcloud compute instances create my-instance --machine-type=e2-medium --image-family=ubuntu-2204-lts --image-project=ubuntu-os-cloud
```

---

**基本写法：查看实例详情**
`gcloud compute instances describe <实例名> [--zone <可用区>]`
```bash
# 查看实例完整配置
gcloud compute instances describe my-instance --zone us-central1-a
```

---

**基本写法：启动实例**
`gcloud compute instances start <实例名> [--zone <可用区>]`
```bash
# 启动已停止的实例
gcloud compute instances start my-instance
```

---

**基本写法：停止实例**
`gcloud compute instances stop <实例名> [--zone <可用区>]`
```bash
# 停止运行中的实例
gcloud compute instances stop my-instance
```

---

**基本写法：重启实例**
`gcloud compute instances reset <实例名> [--zone <可用区>]`
```bash
# 强制重置实例
gcloud compute instances reset my-instance
```

---

**基本写法：删除实例**
`gcloud compute instances delete <实例名> [--zone <可用区>]`
```bash
# 删除实例及关联磁盘
gcloud compute instances delete my-instance
```

---

## SSH 连接

**基本写法：SSH 登录实例**
`gcloud compute ssh <实例名> [--zone <可用区>]`
```bash
# 自动管理密钥并 SSH 登录
gcloud compute ssh my-instance
```

---

**基本写法：使用 scp 传输文件**
`gcloud compute scp <本地文件> <实例名>:<远程路径> [--zone <可用区>]`
```bash
# 上传本地文件到实例
gcloud compute scp ./file.txt my-instance:~/file.txt
```

---

**基本写法：从实例下载文件**
`gcloud compute scp <实例名>:<远程路径> <本地路径>`
```bash
# 下载实例文件到本地
gcloud compute scp my-instance:~/log.txt ./
```

---

## 防火墙规则

**基本写法：列出防火墙规则**
`gcloud compute firewall-rules list`
```bash
# 查看所有防火墙规则
gcloud compute firewall-rules list
```

---

**基本写法：创建允许 HTTP 规则**
`gcloud compute firewall-rules create <规则名> --allow tcp:80 --source-ranges 0.0.0.0/0`
```bash
# 创建允许任意 IP 访问 80 端口的规则
gcloud compute firewall-rules create allow-http --allow tcp:80 --source-ranges 0.0.0.0/0
```

---

**基本写法：创建允许 SSH 规则**
`gcloud compute firewall-rules create <规则名> --allow tcp:22 --source-ranges <CIDR>`
```bash
# 允许特定 CIDR 通过 SSH 访问
gcloud compute firewall-rules create allow-ssh --allow tcp:22 --source-ranges 192.168.1.0/24
```

---

**基本写法：删除防火墙规则**
`gcloud compute firewall-rules delete <规则名>`
```bash
# 删除指定防火墙规则
gcloud compute firewall-rules delete allow-http
```

---

## Cloud Storage 桶

**基本写法：列出所有桶**
`gcloud storage buckets list`
```bash
# 列出项目下所有存储桶
gcloud storage buckets list
```

---

**基本写法：创建桶**
`gcloud storage buckets create gs://<桶名> [--location=<区域>]`
```bash
# 在指定区域创建桶
gcloud storage buckets create gs://my-unique-bucket --location=us-central1
```

---

**基本写法：列出桶内对象**
`gcloud storage ls gs://<桶名>/[<前缀>]`
```bash
# 列出桶内所有对象
gcloud storage ls gs://my-bucket
```

---

**基本写法：上传文件**
`gcloud storage cp <本地文件> gs://<桶名>/[<前缀>]`
```bash
# 上传本地文件到桶
gcloud storage cp ./file.txt gs://my-bucket/
```

---

**基本写法：下载文件**
`gcloud storage cp gs://<桶名>/<键> <本地路径>`
```bash
# 从桶下载文件到本地
gcloud storage cp gs://my-bucket/file.txt ./
```

---

**基本写法：同步目录**
`gcloud storage rsync <本地目录> gs://<桶名>/<前缀> [--delete]`
```bash
# 增量同步本地目录到桶
gcloud storage rsync ./src gs://my-bucket/src --delete
```

---

**基本写法：删除对象**
`gcloud storage rm gs://<桶名>/<键> [-r]`
```bash
# 递归删除桶内目录
gcloud storage rm gs://my-bucket/folder -r
```

---

**基本写法：删除桶**
`gcloud storage buckets delete gs://<桶名>`
```bash
# 删除空桶
gcloud storage buckets delete gs://my-bucket
```

---

## Cloud Run 部署

**基本写法：部署 Cloud Run 服务**
`gcloud run deploy --source . [--region <区域>] [--allow-unauthenticated]`
```bash
# 从源码部署并允许匿名访问
gcloud run deploy --source . --region us-central1 --allow-unauthenticated
```

---

**基本写法：列出 Cloud Run 服务**
`gcloud run services list`
```bash
# 列出所有 Cloud Run 服务
gcloud run services list
```

---

**基本写法：查看服务日志**
`gcloud run services logs tail <服务名> [--region <区域>]`
```bash
# 实时跟踪服务日志
gcloud run services logs tail my-service --region us-central1
```

---

**基本写法：删除 Cloud Run 服务**
`gcloud run services delete <服务名> [--region <区域>]`
```bash
# 删除指定服务
gcloud run services delete my-service --region us-central1
```

<!-- ============ 文档分隔线：034-cloud-computing/041-TerraformBasic.md ============ -->

## 模板语法

**基本写法：provider 声明**
```hcl
# 声明使用的云提供商与区域
provider "aws" {
  region = "us-east-1"
}
```

---

**基本写法：resource 资源块**
```hcl
# 定义 EC2 实例资源
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

---

**基本写法：variable 输入变量**
```hcl
# 定义可由外部传入的变量
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
```

---

**基本写法：output 输出值**
```hcl
# 输出资源属性供其他模块引用
output "instance_id" {
  value = aws_instance.example.id
}
```

---

**基本写法：引用变量与资源**
```hcl
# 在资源中引用变量
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_type
}
```

---

## 核心工作流

**基本写法：初始化工作目录**
`terraform init`
```bash
# 下载 provider 插件并初始化后端
terraform init
```

---

**基本写法：升级初始化**
`terraform init -upgrade`
```bash
# 升级 provider 与模块到允许的最新版本
terraform init -upgrade
```

---

**基本写法：预览变更**
`terraform plan`
```bash
# 预览将要创建修改销毁的资源
terraform plan
```

---

**基本写法：保存计划到文件**
`terraform plan -out=<文件名>`
```bash
# 将计划保存到文件供 apply 使用
terraform plan -out=tf.tfplan
```

---

**基本写法：应用变更**
`terraform apply`
```bash
# 应用配置变更需手动确认
terraform apply
```

---

**基本写法：自动确认应用**
`terraform apply -auto-approve`
```bash
# 应用变更无需确认适合 CI/CD
terraform apply -auto-approve
```

---

**基本写法：应用指定计划**
`terraform apply <计划文件>`
```bash
# 应用预先保存的计划文件
terraform apply tf.tfplan
```

---

**基本写法：销毁所有资源**
`terraform destroy`
```bash
# 销毁当前配置管理的所有资源
terraform destroy
```

---

**基本写法：销毁单个资源**
`terraform destroy -target=<资源类型>.<资源名>`
```bash
# 仅销毁指定资源
terraform destroy -target=aws_instance.example
```

---

## 验证与格式化

**基本写法：语法校验**
`terraform validate`
```bash
# 检查配置语法与一致性
terraform validate
```

---

**基本写法：格式化代码**
`terraform fmt`
```bash
# 将配置文件格式化为规范风格
terraform fmt
```

---

**基本写法：递归格式化**
`terraform fmt -recursive`
```bash
# 递归格式化所有子目录文件
terraform fmt -recursive
```

---

**基本写法：检查格式但不修改**
`terraform fmt -check`
```bash
# 检查格式不规范则退出码 1
terraform fmt -check
```

---

## 变量传递

**基本写法：命令行传变量**
`terraform plan -var "<键>=<值>"`
```bash
# 通过命令行传入变量值
terraform plan -var "instance_type=t3.small"
```

---

**基本写法：使用变量定义文件**
`terraform plan -var-file=<文件>`
```bash
# 通过 tfvars 文件传入多个变量
terraform plan -var-file=prod.tfvars
```

---

**基本写法：查看所有输出**
`terraform output`
```bash
# 查看应用后的输出值
terraform output
```

---

**基本写法：查看 JSON 格式输出**
`terraform output -json`
```bash
# 以 JSON 格式输出便于脚本解析
terraform output -json
```

---

## 模块管理

**基本写法：使用本地模块**
```hcl
# 引用本地子模块
module "vpc" {
  source = "./modules/vpc"
  cidr   = "10.0.0.0/16"
}
```

---

**基本写法：使用 Registry 模块**
```hcl
# 引用 Terraform Registry 上的官方模块
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"
  cidr    = "10.0.0.0/16"
}
```

---

**基本写法：下载与更新模块**
`terraform get [-update]`
```bash
# 下载引用的模块
terraform get -update
```

<!-- ============ 文档分隔线：034-cloud-computing/042-TerraformStateModule.md ============ -->

## 状态查看

**基本写法：列出状态中所有资源**
`terraform state list`
```bash
# 列出当前状态文件中所有资源
terraform state list
```

---

**基本写法：查看资源详情**
`terraform state show <资源类型>.<资源名>`
```bash
# 查看指定资源的状态属性
terraform state show aws_instance.example
```

---

**基本写法：以人类可读格式查看**
`terraform show`
```bash
# 显示整个状态文件
terraform show
```

---

**基本写法：以 JSON 输出状态**
`terraform show -json`
```bash
# 输出 JSON 格式状态便于程序解析
terraform show -json
```

---

**基本写法：查看所有输出值**
`terraform output`
```bash
# 显示所有 output 块的值
terraform output
```

---

**基本写法：查看单个输出**
`terraform output <输出名>`
```bash
# 查看指定输出值
terraform output instance_id
```

---

## 状态管理

**基本写法：拉取远程状态**
`terraform state pull`
```bash
# 从后端拉取状态到标准输出
terraform state pull
```

---

**基本写法：推送本地状态**
`terraform state push <状态文件>`
```bash
# 推送本地状态文件到远程后端
terraform state push terraform.tfstate
```

---

**基本写法：从状态中移除资源**
`terraform state rm <资源类型>.<资源名>`
```bash
# 移除资源但不销毁实际基础设施
terraform state rm aws_instance.example
```

---

**基本写法：重命名状态中的资源**
`terraform state mv <旧地址> <新地址>`
```bash
# 重命名状态中的资源地址
terraform state mv aws_instance.old aws_instance.new
```

---

**基本写法：替换资源**
`terraform apply -replace=<资源类型>.<资源名>`
```bash
# 强制销毁并重建指定资源
terraform apply -replace=aws_instance.example
```

---

**基本写法：检测漂移**
`terraform plan -refresh-only`
```bash
# 仅刷新状态检测实际漂移
terraform plan -refresh-only
```

---

## 资源导入

**基本写法：导入现有资源**
`terraform import <资源类型>.<资源名> <远程ID>`
```bash
# 将现有 EC2 实例导入到 Terraform 管理
terraform import aws_instance.example i-1234567890abcdef0
```

---

**基本写法：声明式导入块**
```hcl
# Terraform 1.5+ 支持的声明式导入
import {
  to = aws_instance.example
  id = "i-1234567890abcdef0"
}
```

---

**基本写法：生成导入配置**
`terraform plan -generate-config-out=<文件>`
```bash
# 为导入的资源生成配置代码
terraform plan -generate-config-out=generated.tf
```

---

## 工作空间

**基本写法：列出工作空间**
`terraform workspace list`
```bash
# 列出所有工作空间
terraform workspace list
```

---

**基本写法：创建工作空间**
`terraform workspace new <工作空间名>`
```bash
# 创建新的工作空间用于多环境管理
terraform workspace new production
```

---

**基本写法：切换工作空间**
`terraform workspace select <工作空间名>`
```bash
# 切换到指定工作空间
terraform workspace select production
```

---

**基本写法：查看当前工作空间**
`terraform workspace show`
```bash
# 输出当前激活的工作空间名
terraform workspace show
```

---

**基本写法：删除工作空间**
`terraform workspace delete <工作空间名>`
```bash
# 删除非当前激活的工作空间
terraform workspace delete staging
```

---

**基本写法：在配置中引用工作空间**
```hcl
# 根据工作空间区分环境配置
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = terraform.workspace == "production" ? "t3.medium" : "t3.micro"
}
```

---

## 后端配置

**基本写法：本地后端**
```hcl
# 默认本地后端
terraform {
  backend "local" {
    path = "terraform.tfstate"
  }
}
```

---

**基本写法：S3 远程后端**
```hcl
# 使用 S3 与 DynamoDB 实现远程状态与锁
terraform {
  backend "s3" {
    bucket         = "my-tfstate-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "tf-locks"
    encrypt        = true
  }
}
```

---

**基本写法：后端初始化迁移**
`terraform init -migrate-state`
```bash
# 切换后端时迁移现有状态
terraform init -migrate-state
```

---

**基本写法：强制重新配置后端**
`terraform init -reconfigure`
```bash
# 忽略已有配置重新初始化后端
terraform init -reconfigure
```

---

## 模块引用

**基本写法：引用模块输出**
```hcl
# 引用子模块的输出值
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id     = module.vpc.public_subnet_id
}
```

---

**基本写法：从 Git 仓库引用模块**
```hcl
# 引用 Git 仓库中的模块
module "vpc" {
  source = "git::https://github.com/example/terraform-modules.git//vpc?ref=v1.2.0"
  cidr   = "10.0.0.0/16"
}
```

<!-- ============ 文档分隔线：034-cloud-computing/043-AWSCloudWatch.md ============ -->

## 命名空间与指标查看

**基本写法：列出所有命名空间**
`aws cloudwatch list-namespaces`
```bash
# 查看账户下所有 CloudWatch 命名空间
aws cloudwatch list-namespaces
```

---

**基本写法：列出指定命名空间下的指标**
`aws cloudwatch list-metrics --namespace <命名空间>`
```bash
# 列出 AWS/EC2 命名空间下所有指标
aws cloudwatch list-metrics --namespace AWS/EC2
```

---

**基本写法：按指标名与维度过滤**
`aws cloudwatch list-metrics --namespace <命名空间> --metric-name <指标名> --dimensions <维度>`
```bash
# 查看 EC2 CPUUtilization 指标
aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name CPUUtilization
```

---

**基本写法：分页查询指标**
`aws cloudwatch list-metrics --namespace <命名空间> --next-token <令牌>`
```bash
# 使用上一次返回的 token 继续分页查询
aws cloudwatch list-metrics --namespace AWS/EC2 --next-token EXAMPLE_TOKEN
```

---

## 指标数据获取

**基本写法：获取指标统计数据**
`aws cloudwatch get-metric-statistics --namespace <命名空间> --metric-name <指标名> --start-time <开始> --end-time <结束> --period <秒> --statistics <统计>`
```bash
# 获取过去 1 小时 EC2 平均 CPU 利用率
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Average
```

---

**基本写法：多统计方式查询**
`aws cloudwatch get-metric-statistics --statistics Average Maximum Minimum Sum`
```bash
# 同时查询平均值、最大值、最小值、求和
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Average Maximum Minimum Sum
```

---

**基本写法：使用扩展统计百分位**
`aws cloudwatch get-metric-statistics --extended-statistics <百分位>`
```bash
# 查询 P95 P99 百分位数据
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --extended-statistics p95 p99
```

---

## 日志组与日志流

**基本写法：列出日志组**
`aws logs describe-log-groups [--log-group-name-prefix <前缀>]`
```bash
# 列出以 /aws/lambda 开头的日志组
aws logs describe-log-groups --log-group-name-prefix /aws/lambda
```

---

**基本写法：创建日志组**
`aws logs create-log-group --log-group-name <日志组名>`
```bash
# 创建自定义日志组并设置保留
aws logs create-log-group --log-group-name /myapp/prod
```

---

**基本写法：设置日志保留**
`aws logs put-retention-policy --log-group-name <日志组名> --retention-in-days <天数>`
```bash
# 设置日志保留 30 天
aws logs put-retention-policy --log-group-name /myapp/prod --retention-in-days 30
```

---

**基本写法：列出日志流**
`aws logs describe-log-streams --log-group-name <日志组名>`
```bash
# 查看指定日志组下日志流
aws logs describe-log-streams --log-group-name /aws/lambda/myFunction
```

---

**基本写法：删除日志组**
`aws logs delete-log-group --log-group-name <日志组名>`
```bash
# 删除日志组及其所有日志流
aws logs delete-log-group --log-group-name /myapp/dev
```

---

## 日志查询

**基本写法：获取日志事件**
`aws logs get-log-events --log-group-name <日志组名> --log-stream-name <日志流名>`
```bash
# 获取最新 50 条日志事件
aws logs get-log-events \
  --log-group-name /aws/lambda/myFunction \
  --log-stream-name '2026/07/31/[$LATEST]abc123' \
  --limit 50
```

---

**基本写法：过滤日志事件**
`aws logs filter-log-events --log-group-name <日志组名> --filter-pattern <过滤模式>`
```bash
# 查询包含 ERROR 的日志
aws logs filter-log-events \
  --log-group-name /myapp/prod \
  --filter-pattern ERROR \
  --start-time 1785489000000
```

---

**基本写法：使用 JSON 过滤语法**
`aws logs filter-log-events --filter-pattern <JSON模式>`
```bash
# 过滤 level 为 ERROR 且 message 包含 timeout 的日志
aws logs filter-log-events \
  --log-group-name /myapp/prod \
  --filter-pattern '{ $.level = "ERROR" && $.message = "timeout" }'
```

---

**基本写法：跨多日志组查询**
`aws logs filter-log-events --log-group-names <日志组1> <日志组2>`
```bash
# 同时在多个日志组中查询
aws logs filter-log-events \
  --log-group-names /myapp/api /myapp/worker \
  --filter-pattern ERROR
```

---

## Logs Insights 查询

**基本写法：启动 Logs Insights 查询**
`aws logs start-query --log-group-names <日志组> --start-time <开始> --end-time <结束> --query-string <查询>`
```bash
# 启动查询统计错误日志
aws logs start-query \
  --log-group-names /myapp/prod \
  --start-time 1785489000 \
  --end-time 1785492600 \
  --query-string 'fields @timestamp, @message | filter level = "ERROR" | sort @timestamp desc | limit 100'
```

---

**基本写法：获取查询结果**
`aws logs get-query-results --query-id <查询ID>`
```bash
# 通过查询 ID 获取结果
aws logs get-query-results --query-id EXAMPLE-QUERY-ID
```

---

**基本写法：停止查询**
`aws logs stop-query --query-id <查询ID>`
```bash
# 终止运行中的查询
aws logs stop-query --query-id EXAMPLE-QUERY-ID
```

---

**基本写法：聚合统计查询**
`aws logs start-query --query-string <统计查询>`
```bash
# 按错误类型聚合统计
aws logs start-query \
  --log-group-names /myapp/prod \
  --start-time 1785489000 \
  --end-time 1785492600 \
  --query-string 'filter level = "ERROR" | stats count(*) by errorType | sort count(*) desc'
```

---

## 告警管理

**基本写法：创建基于指标的告警**
`aws cloudwatch put-metric-alarm --alarm-name <告警名> --metric-name <指标> --namespace <命名空间> --threshold <阈值> --comparison-operator <操作符> --evaluation-periods <周期数> --period <秒>`
```bash
# 创建 CPU 利用率超 80% 触发的告警
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0
```

---

**基本写法：告警附加 SNS 通知**
`aws cloudwatch put-metric-alarm --alarm-actions <SNS ARN>`
```bash
# 告警触发时发送 SNS 通知
aws cloudwatch put-metric-alarm \
  --alarm-name HighCPU \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:my-topic
```

---

**基本写法：列出所有告警**
`aws cloudwatch describe-alarms [--state-value <状态>]`
```bash
# 仅列出处于告警状态的告警
aws cloudwatch describe-alarms --state-value ALARM
```

---

**基本写法：删除告警**
`aws cloudwatch delete-alarms --alarm-names <告警名>`
```bash
# 删除指定告警
aws cloudwatch delete-alarms --alarm-names HighCPU
```

---

## 仪表盘与注解

**基本写法：获取仪表盘**
`aws cloudwatch get-dashboard --dashboard-name <仪表盘名>`
```bash
# 获取仪表盘定义 JSON
aws cloudwatch get-dashboard --dashboard-name my-dashboard
```

---

**基本写法：创建或更新仪表盘**
`aws cloudwatch put-dashboard --dashboard-name <仪表盘名> --dashboard-body <JSON>`
```bash
# 通过 JSON 创建仪表盘
aws cloudwatch put-dashboard \
  --dashboard-name my-dashboard \
  --dashboard-body '{"widgets":[{"type":"metric","x":0,"y":0,"width":12,"height":6,"properties":{"metrics":[["AWS/EC2","CPUUtilization"]],"region":"us-east-1","title":"CPU 使用率"}}]}'
```

---

**基本写法：列出所有仪表盘**
`aws cloudwatch list-dashboards`
```bash
# 列出账户所有仪表盘
aws cloudwatch list-dashboards
```

---

**基本写法：删除仪表盘**
`aws cloudwatch delete-dashboards --dashboard-names <仪表盘名>`
```bash
# 删除指定仪表盘
aws cloudwatch delete-dashboards --dashboard-names my-dashboard
```

---

## 指标流与异常检测

**基本写法：创建指标流**
`aws cloudwatch put-metric-stream --name <流名> --firehose-arn <Firehose ARN> --output-format <格式>`
```bash
# 创建指标流到 Kinesis Firehose
aws cloudwatch put-metric-stream \
  --name my-stream \
  --firehose-arn arn:aws:firehose:us-east-1:123456789012:deliverystream/my-stream \
  --output-format opentelemetry0.7 \
  --role-arn arn:aws:iam::123456789012:role/my-stream-role
```

---

**基本写法：创建异常检测模型**
`aws cloudwatch put-anomaly-detector --namespace <命名空间> --metric-name <指标名>`
```bash
# 为 EC2 CPU 指标创建异常检测
aws cloudwatch put-anomaly-detector \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --stat Average
```

---

**基本写法：列出异常检测器**
`aws cloudwatch describe-anomaly-detectors`
```bash
# 查看所有异常检测模型
aws cloudwatch describe-anomaly-detectors
```

---

**基本写法：删除异常检测器**
`aws cloudwatch delete-anomaly-detectors --namespace <命名空间> --metric-name <指标名>`
```bash
# 删除指定异常检测模型
aws cloudwatch delete-anomaly-detectors \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization
```

---

## Contributor Insights 与 RUM

**基本写法：创建 Contributor Insights 规则**
`aws logs put-insight-rule --insight-rule <JSON>`
```bash
# 创建按 IP 统计访问的规则
aws logs put-insight-rule \
  --insight-rule '{
    "name": "TopIPs",
    "logFormat": "JSON",
    "logGroupNames": ["/myapp/prod"],
    "fields": ["clientIp"],
    "contribution": {"keys": ["clientIp"], "value": "1"}
  }'
```

---

**基本写法：查询 Contributor Insights 结果**
`aws logs get-insight-query-results --insight-rule-name <规则名>`
```bash
# 获取 TopIPs 规则的查询结果
aws logs get-insight-query-results \
  --insight-rule-name TopIPs \
  --start-time 1785489000000 \
  --end-time 1785492600000
```

---

**基本写法：启用 RUM 应用监控**
`aws rum create-app-monitor --name <应用名> --domain <域名> --app-configuration <JSON>`
```bash
# 创建 RUM 应用监控
aws rum create-app-monitor \
  --name my-app \
  --domain example.com \
  --app-configuration '{"AllowCookies":true,"EnableXRay":true}'
```

---

**基本写法：查看 RUM 应用监控列表**
`aws rum list-app-monitors`
```bash
# 列出所有 RUM 应用监控
aws rum list-app-monitors
```

---

## 合成监控与自定义指标

**基本写法：创建 Canary 合成监控**
`aws synthetics create-canary --name <名称> --code <代码配置> --schedule <调度> --artifact-s3-location <S3>`
```bash
# 创建每 5 分钟运行的 Canary
aws synthetics create-canary \
  --name my-canary \
  --code Handler= CanaryHandler.handler,ZipFile= canary.zip \
  --schedule 'Expression="rate(5 minutes)"' \
  --artifact-s3-location s3://my-bucket/canary \
  --execution-role-arn arn:aws:iam::123456789012:role/CanaryRole \
  --runtime-version syn-1.0
```

---

**基本写法：启动 Canary**
`aws synthetics start-canary --name <名称>`
```bash
# 启动指定 Canary
aws synthetics start-canary --name my-canary
```

---

**基本写法：发布自定义指标**
`aws cloudwatch put-metric-data --namespace <命名空间> --metric-data <指标数据>`
```bash
# 推送自定义业务指标
aws cloudwatch put-metric-data \
  --namespace MyApplication \
  --metric-data '[{"MetricName":"OrderCount","Dimensions":[{"Name":"Service","Value":"Checkout"}],"Value":42,"Unit":"Count"}]'
```

---

**基本写法：发布带时间戳的指标**
`aws cloudwatch put-metric-data --metric-data <带时间戳>`
```bash
# 推送带时间戳的历史数据
aws cloudwatch put-metric-data \
  --namespace MyApplication \
  --metric-data '[{"MetricName":"Latency","Timestamp":"2026-07-31T00:00:00Z","Value":250,"Unit":"Milliseconds"}]'
```

<!-- ============ 文档分隔线：034-cloud-computing/044-AWSRDSCommands.md ============ -->

## 实例创建与查看

**基本写法：查看可用数据库引擎**
`aws rds describe-db-engine-versions`
```bash
# 列出所有数据库引擎及版本
aws rds describe-db-engine-versions
```

---

**基本写法：查看 MySQL 引擎版本**
`aws rds describe-db-engine-versions --engine mysql`
```bash
# 查看 MySQL 引擎的所有可用版本
aws rds describe-db-engine-versions --engine mysql
```

---

**基本写法：创建 RDS 实例**
`aws rds create-db-instance --db-instance-identifier <实例ID> --db-instance-class <实例类> --engine <引擎> --master-username <用户> --master-user-password <密码> --allocated-storage <GB>`
```bash
# 创建 MySQL 8.0 实例
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.micro \
  --engine mysql \
  --engine-version 8.0.35 \
  --master-username admin \
  --master-user-password 'MyStrongPass123!' \
  --allocated-storage 20
```

---

**基本写法：列出所有 RDS 实例**
`aws rds describe-db-instances [--db-instance-identifier <实例ID>]`
```bash
# 查看账户下所有 RDS 实例
aws rds describe-db-instances
```

---

**基本写法：查看实例详情**
`aws rds describe-db-instances --db-instance-identifier <实例ID>`
```bash
# 查看指定实例详情
aws rds describe-db-instances --db-instance-identifier mydb
```

---

**基本写法：删除实例**
`aws rds delete-db-instance --db-instance-identifier <实例ID> [--skip-final-snapshot]`
```bash
# 删除实例但不保留最终快照
aws rds delete-db-instance --db-instance-identifier mydb --skip-final-snapshot
```

---

## 实例配置管理

**基本写法：修改实例规格**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --db-instance-class <实例类> --apply-immediately`
```bash
# 立即将实例规格升级到 t3.medium
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.medium \
  --apply-immediately
```

---

**基本写法：扩容存储**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --allocated-storage <GB> --apply-immediately`
```bash
# 扩容存储至 100GB
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --allocated-storage 100 \
  --apply-immediately
```

---

**基本写法：修改参数组**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --db-parameter-group-name <参数组>`
```bash
# 应用新的参数组
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --db-parameter-group-name myparamgroup \
  --apply-immediately
```

---

**基本写法：重启实例**
`aws rds reboot-db-instance --db-instance-identifier <实例ID>`
```bash
# 重启 RDS 实例
aws rds reboot-db-instance --db-instance-identifier mydb
```

---

**基本写法：查看实例状态**
`aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus]'`
```bash
# 列出实例名与状态
aws rds describe-db-instances \
  --query 'DBInstances[*].[DBInstanceIdentifier,DBInstanceStatus]' \
  --output table
```

---

## 快照管理

**基本写法：创建手动快照**
`aws rds create-db-snapshot --db-instance-identifier <实例ID> --db-snapshot-identifier <快照名>`
```bash
# 为 mydb 实例创建手动快照
aws rds create-db-snapshot \
  --db-instance-identifier mydb \
  --db-snapshot-identifier mydb-snapshot-20260731
```

---

**基本写法：列出快照**
`aws rds describe-db-snapshots [--db-instance-identifier <实例ID>]`
```bash
# 列出所有手动快照
aws rds describe-db-snapshots --snapshot-type manual
```

---

**基本写法：从快照还原实例**
`aws rds restore-db-instance-from-db-snapshot --db-instance-identifier <新实例ID> --db-snapshot-identifier <快照名>`
```bash
# 从快照还原为新实例
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier mydb-restored \
  --db-snapshot-identifier mydb-snapshot-20260731
```

---

**基本写法：删除快照**
`aws rds delete-db-snapshot --db-snapshot-identifier <快照名>`
```bash
# 删除指定快照
aws rds delete-db-snapshot --db-snapshot-identifier mydb-snapshot-20260731
```

---

**基本写法：将快照复制到另一区域**
`aws rds copy-db-snapshot --source-db-snapshot-identifier <源ARN> --target-db-snapshot-identifier <目标快照名>`
```bash
# 跨区域复制快照用于灾备
aws rds copy-db-snapshot \
  --source-db-snapshot-identifier arn:aws:rds:us-east-1:123456789012:snapshot:mydb-snapshot \
  --target-db-snapshot-identifier mydb-snapshot-copy \
  --region us-west-2
```

---

## 安全组与子网

**基本写法：修改安全组**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --vpc-security-group-ids <安全组ID>`
```bash
# 修改实例所属 VPC 安全组
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --vpc-security-group-ids sg-12345678 \
  --apply-immediately
```

---

**基本写法：查看子网组**
`aws rds describe-db-subnet-groups`
```bash
# 列出所有 DB 子网组
aws rds describe-db-subnet-groups
```

---

**基本写法：创建子网组**
`aws rds create-db-subnet-group --db-subnet-group-name <组名> --db-subnet-group-description <描述> --subnet-ids <子网ID列表>`
```bash
# 创建 DB 子网组关联多个子网
aws rds create-db-subnet-group \
  --db-subnet-group-name my-subnet-group \
  --db-subnet-group-description "my subnet group" \
  --subnet-ids subnet-abc subnet-def subnet-ghi
```

---

**基本写法：查看安全组**
`aws ec2 describe-security-groups --group-ids <安全组ID>`
```bash
# 查看安全组规则
aws ec2 describe-security-groups --group-ids sg-12345678
```

---

## 参数组管理

**基本写法：创建参数组**
`aws rds create-db-parameter-group --db-parameter-group-name <组名> --db-parameter-group-family <家族> --description <描述>`
```bash
# 创建 MySQL 8.0 参数组
aws rds create-db-parameter-group \
  --db-parameter-group-name my-param-group \
  --db-parameter-group-family mysql8.0 \
  --description "My custom MySQL params"
```

---

**基本写法：修改参数**
`aws rds modify-db-parameter-group --db-parameter-group-name <组名> --parameters <参数列表>`
```bash
# 修改 max_connections 与 time_zone
aws rds modify-db-parameter-group \
  --db-parameter-group-name my-param-group \
  --parameters "ParameterName=max_connections,ParameterValue=500,ApplyMethod=immediate" \
               "ParameterName=time_zone,ParameterValue=Asia/Shanghai,ApplyMethod=pending-reboot"
```

---

**基本写法：查看参数组详情**
`aws rds describe-db-parameters --db-parameter-group-name <组名>`
```bash
# 查看参数组中所有参数
aws rds describe-db-parameters --db-parameter-group-name my-param-group
```

---

**基本写法：删除参数组**
`aws rds delete-db-parameter-group --db-parameter-group-name <组名>`
```bash
# 删除未被使用的参数组
aws rds delete-db-parameter-group --db-parameter-group-name my-param-group
```

---

## Aurora 集群

**基本写法：创建 Aurora 集群**
`aws rds create-db-cluster --db-cluster-identifier <集群ID> --engine aurora-mysql --master-username <用户> --master-user-password <密码>`
```bash
# 创建 Aurora MySQL 集群
aws rds create-db-cluster \
  --db-cluster-identifier my-cluster \
  --engine aurora-mysql \
  --engine-version 8.0.mysql_aurora.3.04.0 \
  --master-username admin \
  --master-user-password 'MyStrongPass123!' \
  --database-name mydb \
  --backup-retention-period 7
```

---

**基本写法：创建集群实例**
`aws rds create-db-instance --db-instance-identifier <实例ID> --db-instance-class <类> --engine aurora-mysql --db-cluster-identifier <集群ID>`
```bash
# 为 Aurora 集群添加实例
aws rds create-db-instance \
  --db-instance-identifier my-cluster-instance-1 \
  --db-instance-class db.r6g.large \
  --engine aurora-mysql \
  --db-cluster-identifier my-cluster
```

---

**基本写法：故障转移集群**
`aws rds failover-db-cluster --db-cluster-identifier <集群ID> --target-db-instance-identifier <目标实例>`
```bash
# 手动故障转移到指定实例
aws rds failover-db-cluster \
  --db-cluster-identifier my-cluster \
  --target-db-instance-identifier my-cluster-instance-2
```

---

**基本写法：删除集群**
`aws rds delete-db-cluster --db-cluster-identifier <集群ID> --skip-final-snapshot`
```bash
# 删除 Aurora 集群及其实例
aws rds delete-db-cluster \
  --db-cluster-identifier my-cluster \
  --skip-final-snapshot
```

---

## 事件与日志

**基本写法：查看事件**
`aws rds describe-events [--source-identifier <资源ID>] [--source-type <类型>]`
```bash
# 查看指定实例最近 1 小时事件
aws rds describe-events \
  --source-identifier mydb \
  --source-type db-instance \
  --duration 60
```

---

**基本写法：查看事件订阅**
`aws rds describe-event-subscriptions`
```bash
# 列出所有事件订阅
aws rds describe-event-subscriptions
```

---

**基本写法：创建事件订阅**
`aws rds create-event-subscription --subscription-name <订阅名> --source-type <类型> --event-categories <分类> --sns-topic-arn <SNS ARN>`
```bash
# 订阅实例故障事件
aws rds create-event-subscription \
  --subscription-name my-failure-sub \
  --source-type db-instance \
  --event-categories failure \
  --sns-topic-arn arn:aws:sns:us-east-1:123456789012:rds-events
```

---

**基本写法：下载日志文件**
`aws rds download-db-log-file-portion --db-instance-identifier <实例ID> --log-file-name <文件名> --output text`
```bash
# 下载 error.log 日志到本地
aws rds download-db-log-file-portion \
  --db-instance-identifier mydb \
  --log-file-name error/mysql-error-running.log \
  --output text > error.log
```

---

## 多可用区与只读副本

**基本写法：开启多可用区**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --multi-az --apply-immediately`
```bash
# 为实例开启多 AZ 高可用
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --multi-az \
  --apply-immediately
```

---

**基本写法：创建只读副本**
`aws rds create-db-instance-read-replica --db-instance-identifier <副本ID> --source-db-instance-identifier <源实例>`
```bash
# 从主实例创建只读副本
aws rds create-db-instance-read-replica \
  --db-instance-identifier mydb-read-replica \
  --source-db-instance-identifier mydb \
  --db-instance-class db.t3.micro
```

---

**基本写法：将只读副本提升为主实例**
`aws rds promote-read-replica --db-instance-identifier <副本ID>`
```bash
# 提升只读副本为独立主实例
aws rds promote-read-replica --db-instance-identifier mydb-read-replica
```

---

**基本写法：跨区域只读副本**
`aws rds create-db-instance-read-replica --db-instance-identifier <副本ID> --source-db-instance-identifier <源ARN> --region <区域>`
```bash
# 创建跨区域只读副本用于灾备
aws rds create-db-instance-read-replica \
  --db-instance-identifier mydb-dr \
  --source-db-instance-identifier arn:aws:rds:us-east-1:123456789012:db:mydb \
  --region us-west-2
```

---

## 备份与维护

**基本写法：修改备份保留期**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --backup-retention-period <天>`
```bash
# 设置自动备份保留 14 天
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --backup-retention-period 14 \
  --apply-immediately
```

---

**基本写法：设置维护窗口**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --preferred-maintenance-window <窗口>`
```bash
# 设置每周日凌晨维护窗口
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --preferred-maintenance-window sun:03:00-sun:05:00
```

---

**基本写法：立即应用待处理修改**
`aws rds apply-pending-maintenance-action --resource-id <资源ID> --apply-action <动作> --opt-in-type immediate`
```bash
# 立即应用待处理的 OS 更新
aws rds apply-pending-maintenance-action \
  --resource-id db:mydb \
  --apply-action system-update \
  --opt-in-type immediate
```

---

**基本写法：查看待处理维护动作**
`aws rds describe-pending-maintenance-actions`
```bash
# 列出所有待处理的维护动作
aws rds describe-pending-maintenance-actions
```

---

## Performance Insights

**基本写法：开启 Performance Insights**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --enable-performance-insights --performance-insights-retention-period <天>`
```bash
# 开启 PI 并保留 7 天数据
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --enable-performance-insights \
  --performance-insights-retention-period 7 \
  --apply-immediately
```

---

**基本写法：获取性能指标**
`aws pi get-resource-metrics --service-type RDS --identifier <实例ID> --metric-queries <指标> --start-time <开始> --end-time <结束>`
```bash
# 查询数据库负载指标
aws pi get-resource-metrics \
  --service-type RDS \
  --identifier db-mydb \
  --metric-queries '[{"Metric":"db.load.avg","GroupBy":{"Group":"db.sql"}}]' \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period-in-seconds 300
```

---

**基本写法：关闭 Performance Insights**
`aws rds modify-db-instance --db-instance-identifier <实例ID> --no-enable-performance-insights --apply-immediately`
```bash
# 关闭 PI 节省成本
aws rds modify-db-instance \
  --db-instance-identifier mydb \
  --no-enable-performance-insights \
  --apply-immediately
```

<!-- ============ 文档分隔线：034-cloud-computing/045-AWSVPCCommands.md ============ -->

## VPC 创建与管理

**基本写法：创建 VPC**
`aws ec2 create-vpc --cidr-block <CIDR> [--instance-tenancy <租期>]`
```bash
# 创建 10.0.0.0/16 网段的 VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --instance-tenancy default
```

---

**基本写法：列出所有 VPC**
`aws ec2 describe-vpcs`
```bash
# 查看账户所有 VPC
aws ec2 describe-vpcs
```

---

**基本写法：查看指定 VPC**
`aws ec2 describe-vpcs --vpc-ids <VPC ID>`
```bash
# 查看指定 VPC 详情
aws ec2 describe-vpcs --vpc-ids vpc-12345678
```

---

**基本写法：删除 VPC**
`aws ec2 delete-vpc --vpc-id <VPC ID>`
```bash
# 删除指定 VPC(必须先删除其下所有资源)
aws ec2 delete-vpc --vpc-id vpc-12345678
```

---

**基本写法：为 VPC 添加名称标签**
`aws ec2 create-tags --resources <资源ID> --tags Key=Name,Value=<名称>`
```bash
# 给 VPC 添加名称
aws ec2 create-tags \
  --resources vpc-12345678 \
  --tags Key=Name,Value=my-vpc
```

---

## 子网管理

**基本写法：创建子网**
`aws ec2 create-subnet --vpc-id <VPC ID> --cidr-block <CIDR> [--availability-zone <AZ>]`
```bash
# 在 VPC 中创建子网
aws ec2 create-subnet \
  --vpc-id vpc-12345678 \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-east-1a
```

---

**基本写法：列出子网**
`aws ec2 describe-subnets [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 查看指定 VPC 下所有子网
aws ec2 describe-subnets \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

**基本写法：删除子网**
`aws ec2 delete-subnet --subnet-id <子网ID>`
```bash
# 删除指定子网
aws ec2 delete-subnet --subnet-id subnet-12345678
```

---

**基本写法：为子网开启公网映射**
`aws ec2 modify-subnet-attribute --subnet-id <子网ID> --map-public-ip-on-launch`
```bash
# 让子网中的实例自动获取公网 IP
aws ec2 modify-subnet-attribute \
  --subnet-id subnet-12345678 \
  --map-public-ip-on-launch
```

---

**基本写法：分配 IPv6 CIDR**
`aws ec2 associate-subnet-cidr-block --subnet-id <子网ID> --ipv6-cidr-block <IPv6 CIDR>`
```bash
# 为子网分配 IPv6 网段
aws ec2 associate-subnet-cidr-block \
  --subnet-id subnet-12345678 \
  --ipv6-cidr-block 2600:1f18:4113:b200::/64
```

---

## 路由表

**基本写法：创建路由表**
`aws ec2 create-route-table --vpc-id <VPC ID>`
```bash
# 在指定 VPC 创建路由表
aws ec2 create-route-table --vpc-id vpc-12345678
```

---

**基本写法：添加路由**
`aws ec2 create-route --route-table-id <路由表ID> --destination-cidr-block <CIDR> --gateway-id <网关ID>`
```bash
# 添加 0.0.0.0/0 默认路由到 Internet 网关
aws ec2 create-route \
  --route-table-id rtb-12345678 \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id igw-12345678
```

---

**基本写法：添加 NAT 网关路由**
`aws ec2 create-route --route-table-id <路由表ID> --destination-cidr-block <CIDR> --nat-gateway-id <NAT ID>`
```bash
# 私有子网通过 NAT 网关访问外网
aws ec2 create-route \
  --route-table-id rtb-12345678 \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id nat-12345678
```

---

**基本写法：关联子网**
`aws ec2 associate-route-table --route-table-id <路由表ID> --subnet-id <子网ID>`
```bash
# 将路由表关联到子网
aws ec2 associate-route-table \
  --route-table-id rtb-12345678 \
  --subnet-id subnet-12345678
```

---

**基本写法：列出路由表**
`aws ec2 describe-route-tables [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 查看指定 VPC 的路由表
aws ec2 describe-route-tables \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

## 网关

**基本写法：创建 Internet 网关**
`aws ec2 create-internet-gateway`
```bash
# 创建 Internet Gateway
aws ec2 create-internet-gateway
```

---

**基本写法：附加到 VPC**
`aws ec2 attach-internet-gateway --internet-gateway-id <网关ID> --vpc-id <VPC ID>`
```bash
# 将 IGW 附加到 VPC
aws ec2 attach-internet-gateway \
  --internet-gateway-id igw-12345678 \
  --vpc-id vpc-12345678
```

---

**基本写法：创建 NAT 网关**
`aws ec2 create-nat-gateway --subnet-id <子网ID> --allocation-id <EIP ID>`
```bash
# 在公有子网创建 NAT 网关
aws ec2 create-nat-gateway \
  --subnet-id subnet-12345678 \
  --allocation-id eipalloc-12345678
```

---

**基本写法：创建 VPC 端点**
`aws ec2 create-vpc-endpoint --vpc-id <VPC ID> --service-name <服务名> --route-table-ids <路由表ID>`
```bash
# 创建 S3 Gateway 端点
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --service-name com.amazonaws.us-east-1.s3 \
  --route-table-ids rtb-12345678
```

---

**基本写法：创建接口端点**
`aws ec2 create-vpc-endpoint --vpc-id <VPC ID> --vpc-endpoint-type Interface --service-name <服务名> --subnet-ids <子网ID>`
```bash
# 创建 PrivateLink 接口端点
aws ec2 create-vpc-endpoint \
  --vpc-id vpc-12345678 \
  --vpc-endpoint-type Interface \
  --service-name com.amazonaws.us-east-1.ec2 \
  --subnet-ids subnet-12345678
```

---

## 安全组

**基本写法：创建安全组**
`aws ec2 create-security-group --group-name <组名> --description <描述> --vpc-id <VPC ID>`
```bash
# 在 VPC 中创建安全组
aws ec2 create-security-group \
  --group-name my-sg \
  --description "My security group" \
  --vpc-id vpc-12345678
```

---

**基本写法：添加入站规则**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol <协议> --port <端口> --cidr <CIDR>`
```bash
# 允许 0.0.0.0/0 访问 80 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

---

**基本写法：添加 SSH 入站规则**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol tcp --port 22 --cidr <CIDR>`
```bash
# 仅允许指定 IP 访问 22 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 22 \
  --cidr 203.0.113.0/24
```

---

**基本写法：移除入站规则**
`aws ec2 revoke-security-group-ingress --group-id <组ID> --protocol <协议> --port <端口> --cidr <CIDR>`
```bash
# 移除 80 端口的入站规则
aws ec2 revoke-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
```

---

**基本写法：引用其他安全组**
`aws ec2 authorize-security-group-ingress --group-id <组ID> --protocol tcp --port <端口> --source-group <源组ID>`
```bash
# 允许其他安全组中的实例访问本组 3306 端口
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 3306 \
  --source-group sg-87654321
```

---

## 网络访问控制列表

**基本写法：创建网络 ACL**
`aws ec2 create-network-acl --vpc-id <VPC ID>`
```bash
# 在 VPC 中创建网络 ACL
aws ec2 create-network-acl --vpc-id vpc-12345678
```

---

**基本写法：添加 ACL 规则**
`aws ec2 create-network-acl-entry --network-acl-id <ACL ID> --rule-number <序号> --protocol <协议> --rule-action <动作> --cidr-block <CIDR> --port-range From=<起>,To=<止>`
```bash
# 添加允许 HTTP 入站的 ACL 规则
aws ec2 create-network-acl-entry \
  --network-acl-id acl-12345678 \
  --rule-number 100 \
  --protocol 6 \
  --rule-action allow \
  --cidr-block 0.0.0.0/0 \
  --port-range From=80,To=80 \
  --egress false
```

---

**基本写法：关联子网**
`aws ec2 replace-network-acl-association --association-id <关联ID> --network-acl-id <ACL ID>`
```bash
# 将 ACL 关联到子网
aws ec2 replace-network-acl-association \
  --association-id aclassoc-12345678 \
  --network-acl-id acl-12345678
```

---

**基本写法：查看网络 ACL**
`aws ec2 describe-network-acls [--filters Name=vpc-id,Values=<VPC ID>]`
```bash
# 列出指定 VPC 的所有 ACL
aws ec2 describe-network-acls \
  --filters Name=vpc-id,Values=vpc-12345678
```

---

## 弹性 IP

**基本写法：分配弹性 IP**
`aws ec2 allocate-address --domain <域>`
```bash
# 为 VPC 分配弹性 IP
aws ec2 allocate-address --domain vpc
```

---

**基本写法：关联到实例**
`aws ec2 associate-address --instance-id <实例ID> --allocation-id <EIP ID>`
```bash
# 将弹性 IP 关联到 EC2 实例
aws ec2 associate-address \
  --instance-id i-1234567890abcdef0 \
  --allocation-id eipalloc-12345678
```

---

**基本写法：释放弹性 IP**
`aws ec2 release-address --allocation-id <EIP ID>`
```bash
# 释放未使用的弹性 IP
aws ec2 release-address --allocation-id eipalloc-12345678
```

---

**基本写法：查看所有弹性 IP**
`aws ec2 describe-addresses`
```bash
# 列出账户所有弹性 IP
aws ec2 describe-addresses
```

---

## Peering 与 VPN

**基本写法：创建 VPC Peering**
`aws ec2 create-vpc-peering-connection --vpc-id <本端VPC> --peer-vpc-id <对端VPC>`
```bash
# 创建 VPC 对等连接
aws ec2 create-vpc-peering-connection \
  --vpc-id vpc-12345678 \
  --peer-vpc-id vpc-87654321
```

---

**基本写法：接受 Peering 请求**
`aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id <连接ID>`
```bash
# 接收 VPC 对等连接请求
aws ec2 accept-vpc-peering-connection \
  --vpc-peering-connection-id pcx-12345678
```

---

**基本写法：创建客户网关**
`aws ec2 create-customer-gateway --type ipsec.1 --public-ip <公网IP> --bgp-asn <ASN>`
```bash
# 创建 VPN 客户网关
aws ec2 create-customer-gateway \
  --type ipsec.1 \
  --public-ip 203.0.113.10 \
  --bgp-asn 65000
```

---

**基本写法：创建 VPN 连接**
`aws ec2 create-vpn-connection --customer-gateway-id <CGW ID> --vpn-gateway-id <VGW ID> --type ipsec.1`
```bash
# 建立 Site-to-Site VPN 连接
aws ec2 create-vpn-connection \
  --customer-gateway-id cgw-12345678 \
  --vpn-gateway-id vgw-12345678 \
  --type ipsec.1
```

---

## 流日志与网络监控

**基本写法：启用 VPC 流日志**
`aws ec2 create-flow-logs --resource-ids <资源ID> --resource-type <类型> --traffic-type <流量> --log-group-name <日志组>`
```bash
# 为 VPC 启用流日志记录所有流量
aws ec2 create-flow-logs \
  --resource-ids vpc-12345678 \
  --resource-type VPC \
  --traffic-type ALL \
  --log-group-name /aws/vpc/flowlogs \
  --deliver-logs-permission-arn arn:aws:iam::123456789012:role/FlowLogsRole
```

---

**基本写法：查看流日志**
`aws ec2 describe-flow-logs`
```bash
# 列出所有流日志配置
aws ec2 describe-flow-logs
```

---

**基本写法：删除流日志**
`aws ec2 delete-flow-logs --flow-log-ids <流日志ID>`
```bash
# 删除指定流日志
aws ec2 delete-flow-logs --flow-log-ids fl-12345678
```

---

**基本写法：启用 Reachability Analyzer**
`aws ec2 create-network-insights-path --source <资源ID> --destination <资源ID> --protocol <协议>`
```bash
# 创建路径分析(检查网络可达性)
aws ec2 create-network-insights-path \
  --source i-1234567890abcdef0 \
  --destination i-abcdef1234567890 \
  --protocol tcp
```

---

## Transit Gateway

**基本写法：创建 Transit Gateway**
`aws ec2 create-transit-gateway [--description <描述>]`
```bash
# 创建中转网关用于多 VPC 互联
aws ec2 create-transit-gateway --description "my-tgw"
```

---

**基本写法：附加 VPC 到 TGW**
`aws ec2 create-transit-gateway-vpc-attachment --transit-gateway-id <TGW ID> --vpc-id <VPC ID> --subnet-ids <子网ID列表>`
```bash
# 将 VPC 附加到中转网关
aws ec2 create-transit-gateway-vpc-attachment \
  --transit-gateway-id tgw-12345678 \
  --vpc-id vpc-12345678 \
  --subnet-ids subnet-12345678 subnet-87654321
```

---

**基本写法：查看 TGW 附件**
`aws ec2 describe-transit-gateway-attachments`
```bash
# 列出所有 TGW 附件
aws ec2 describe-transit-gateway-attachments
```

---

**基本写法：创建 TGW 路由**
`aws ec2 create-transit-gateway-route --destination-cidr-block <CIDR> --transit-gateway-route-table-id <表ID> --transit-gateway-attachment-id <附件ID>`
```bash
# 在 TGW 路由表中添加路由
aws ec2 create-transit-gateway-route \
  --destination-cidr-block 10.0.0.0/16 \
  --transit-gateway-route-table-id tgw-rtb-12345678 \
  --transit-gateway-attachment-id tgw-attach-12345678
```

<!-- ============ 文档分隔线：034-cloud-computing/046-AWSSQSCommands.md ============ -->

## SQS 队列管理

**基本写法：创建标准队列**
`aws sqs create-queue --queue-name <队列名>`
```bash
# 创建标准队列
aws sqs create-queue --queue-name my-queue
```

---

**基本写法：创建 FIFO 队列**
`aws sqs create-queue --queue-name <队列名.fifo> --attributes FIFOQueueEnabled=true`
```bash
# 创建 FIFO 队列(.fifo 后缀必填)
aws sqs create-queue \
  --queue-name my-queue.fifo \
  --attributes FIFOQueueEnabled=true,ContentBasedDeduplication=true
```

---

**基本写法：列出所有队列**
`aws sqs list-queues [--queue-name-prefix <前缀>]`
```bash
# 列出以 my 开头的队列
aws sqs list-queues --queue-name-prefix my
```

---

**基本写法：查看队列 URL**
`aws sqs get-queue-url --queue-name <队列名>`
```bash
# 获取指定队列的 URL
aws sqs get-queue-url --queue-name my-queue
```

---

**基本写法：删除队列**
`aws sqs delete-queue --queue-url <队列URL>`
```bash
# 删除指定队列
aws sqs delete-queue --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue
```

---

**基本写法：设置队列属性**
`aws sqs set-queue-attributes --queue-url <URL> --attributes <属性>`
```bash
# 设置消息保留 4 天、可见性超时 300 秒
aws sqs set-queue-attributes \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --attributes MessageRetentionPeriod=345600,VisibilityTimeout=300
```

---

## SQS 消息收发

**基本写法：发送消息**
`aws sqs send-message --queue-url <URL> --message-body <内容>`
```bash
# 发送一条文本消息到队列
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --message-body '{"order_id":"12345","status":"paid"}'
```

---

**基本写法：FIFO 队列发送消息**
`aws sqs send-message --queue-url <URL> --message-body <内容> --message-group-id <组ID>`
```bash
# FIFO 队列必须指定 MessageGroupId
aws sqs send-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue.fifo \
  --message-body '{"order_id":"12345"}' \
  --message-group-id order-group-1 \
  --message-deduplication-id dedup-001
```

---

**基本写法：批量发送消息**
`aws sqs send-message-batch --queue-url <URL> --entries <条目>`
```bash
# 一次发送最多 10 条消息
aws sqs send-message-batch \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --entries '[{"Id":"msg1","MessageBody":"first"},{"Id":"msg2","MessageBody":"second"}]'
```

---

**基本写法：接收消息**
`aws sqs receive-message --queue-url <URL> [--max-number-of-messages <数量>] [--wait-time-seconds <秒>]`
```bash
# 长轮询接收 10 条消息
aws sqs receive-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --max-number-of-messages 10 \
  --wait-time-seconds 20
```

---

**基本写法：删除消息**
`aws sqs delete-message --queue-url <URL> --receipt-handle <回执>`
```bash
# 处理完成后删除消息
aws sqs delete-message \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --receipt-handle AQEBwJm...EXAMPLE
```

---

**基本写法：改变可见性超时**
`aws sqs change-message-visibility --queue-url <URL> --receipt-handle <回执> --visibility-timeout <秒>`
```bash
# 延长消息处理时间
aws sqs change-message-visibility \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --receipt-handle AQEBwJm...EXAMPLE \
  --visibility-timeout 600
```

---

## SQS 死信队列

**基本写法：配置死信队列**
`aws sqs set-queue-attributes --queue-url <URL> --attributes RedrivePolicy=<JSON>`
```bash
# 设置接收 5 次后转入死信队列
aws sqs set-queue-attributes \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --attributes '{"RedrivePolicy":"{\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:123456789012:my-dlq\",\"maxReceiveCount\":\"5\"}"}'
```

---

**基本写法：查看死信队列属性**
`aws sqs get-queue-attributes --queue-url <URL> --attribute-names RedrivePolicy`
```bash
# 查看队列的死信策略
aws sqs get-queue-attributes \
  --queue-url https://sqs.us-east-1.amazonaws.com/123456789012/my-queue \
  --attribute-names RedrivePolicy
```

---

**基本写法：从死信队列重新驱动消息**
`aws sqs start-message-move-task --source-arn <DLQ ARN> --destination-arn <目标 ARN>`
```bash
# 将死信队列消息重新投递回主队列
aws sqs start-message-move-task \
  --source-arn arn:aws:sqs:us-east-1:123456789012:my-dlq \
  --destination-arn arn:aws:sqs:us-east-1:123456789012:my-queue
```

---

**基本写法：查看队列指标**
`aws cloudwatch get-metric-statistics --namespace AWS/SQS --metric-name ApproximateNumberOfMessagesVisible`
```bash
# 查看队列中可见消息数量
aws cloudwatch get-metric-statistics \
  --namespace AWS/SQS \
  --metric-name ApproximateNumberOfMessagesVisible \
  --dimensions Name=QueueName,Value=my-queue \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Average
```

---

## SNS 主题管理

**基本写法：创建 SNS 主题**
`aws sns create-topic --name <主题名>`
```bash
# 创建 SNS 主题
aws sns create-topic --name my-topic
```

---

**基本写法：列出所有主题**
`aws sns list-topics`
```bash
# 列出账户下所有 SNS 主题
aws sns list-topics
```

---

**基本写法：查看主题属性**
`aws sns get-topic-attributes --topic-arn <主题ARN>`
```bash
# 查看主题配置
aws sns get-topic-attributes --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```

---

**基本写法：删除主题**
`aws sns delete-topic --topic-arn <主题ARN>`
```bash
# 删除指定 SNS 主题
aws sns delete-topic --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```

---

**基本写法：设置主题属性**
`aws sns set-topic-attributes --topic-arn <主题ARN> --attribute-name <属性> --attribute-value <值>`
```bash
# 设置主题显示名称
aws sns set-topic-attributes \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --attribute-name DisplayName \
  --attribute-value "My Topic"
```

---

## SNS 订阅管理

**基本写法：订阅 SQS 队列**
`aws sns subscribe --topic-arn <主题ARN> --protocol sqs --notification-endpoint <队列ARN>`
```bash
# 让 SQS 队列订阅 SNS 主题
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --protocol sqs \
  --notification-endpoint arn:aws:sqs:us-east-1:123456789012:my-queue
```

---

**基本写法：邮件订阅**
`aws sns subscribe --topic-arn <主题ARN> --protocol email --notification-endpoint <邮箱>`
```bash
# 通过邮件订阅主题(需邮件确认)
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --protocol email \
  --notification-endpoint user@example.com
```

---

**基本写法：HTTP 端点订阅**
`aws sns subscribe --topic-arn <主题ARN> --protocol https --notification-endpoint <URL>`
```bash
# 通过 HTTPS 端点订阅主题
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --protocol https \
  --notification-endpoint https://example.com/webhook
```

---

**基本写法：列出订阅**
`aws sns list-subscriptions-by-topic --topic-arn <主题ARN>`
```bash
# 查看指定主题所有订阅
aws sns list-subscriptions-by-topic \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic
```

---

**基本写法：取消订阅**
`aws sns unsubscribe --subscription-arn <订阅ARN>`
```bash
# 删除指定订阅
aws sns unsubscribe --subscription-arn arn:aws:sns:us-east-1:123456789012:my-topic:12345678-1234-1234-1234-123456789012
```

---

## SNS 发布消息

**基本写法：发布消息**
`aws sns publish --topic-arn <主题ARN> --message <内容>`
```bash
# 向主题发布消息
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --message "Deployment completed"
```

---

**基本写法：带主题发布**
`aws sns publish --topic-arn <主题ARN> --message <内容> --subject <主题>`
```bash
# 发送带主题的邮件通知
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --message "Build failed: see logs" \
  --subject "ALERT: Build Failure"
```

---

**基本写法：消息属性**
`aws sns publish --topic-arn <主题ARN> --message <内容> --message-attributes <属性>`
```bash
# 携带属性便于订阅端过滤
aws sns publish \
  --topic-arn arn:aws:sns:us-east-1:123456789012:my-topic \
  --message "Order 12345" \
  --message-attributes '{"event":{"DataType":"String","StringValue":"order_created"}}'
```

---

**基本写法：直接发送到手机号**
`aws sns publish --phone-number <号码> --message <内容>`
```bash
# 直接发 SMS 短信
aws sns publish \
  --phone-number +8613800138000 \
  --message "Your verification code is 123456"
```

---

## SNS 过滤策略

**基本写法：设置订阅过滤策略**
`aws sns set-subscription-attributes --subscription-arn <订阅ARN> --attribute-name FilterPolicy --attribute-value <JSON>`
```bash
# 仅接收 event=order_created 的消息
aws sns set-subscription-attributes \
  --subscription-arn arn:aws:sns:us-east-1:123456789012:my-topic:abc-123 \
  --attribute-name FilterPolicy \
  --attribute-value '{"event":["order_created"]}'
```

---

**基本写法：范围过滤策略**
`aws sns set-subscription-attributes --subscription-arn <订阅ARN> --attribute-name FilterPolicy --attribute-value <范围JSON>`
```bash
# 仅接收 price 在 100-1000 之间的消息
aws sns set-subscription-attributes \
  --subscription-arn arn:aws:sns:us-east-1:123456789012:my-topic:abc-123 \
  --attribute-name FilterPolicy \
  --attribute-value '{"price":[{"numeric":[">=",100,"<=",1000]}]}'
```

---

**基本写法：移除过滤策略**
`aws sns set-subscription-attributes --subscription-arn <订阅ARN> --attribute-name FilterPolicy --attribute-value "{}"`
```bash
# 清除过滤策略接收全部消息
aws sns set-subscription-attributes \
  --subscription-arn arn:aws:sns:us-east-1:123456789012:my-topic:abc-123 \
  --attribute-name FilterPolicy \
  --attribute-value '{}'
```

---

## Kinesis 数据流

**基本写法：创建数据流**
`aws kinesis create-stream --stream-name <流名> --shard-count <分片数>`
```bash
# 创建 3 分片的 Kinesis 流
aws kinesis create-stream --stream-name my-stream --shard-count 3
```

---

**基本写法：写入记录**
`aws kinesis put-record --stream-name <流名> --data <数据> --partition-key <分区键>`
```bash
# 写入一条记录到流中
aws kinesis put-record \
  --stream-name my-stream \
  --data '{"event":"login","user":"alice"}' \
  --partition-key alice
```

---

**基本写法：批量写入**
`aws kinesis put-records --stream-name <流名> --records <记录列表>`
```bash
# 批量写入多条记录
aws kinesis put-records \
  --stream-name my-stream \
  --records '[{"Data":"event1","PartitionKey":"k1"},{"Data":"event2","PartitionKey":"k2"}]'
```

---

**基本写法：读取记录**
`aws kinesis get-shard-iterator --stream-name <流名> --shard-id <分片ID> --shard-iterator-type TRIM_HORIZON`
```bash
# 获取分片迭代器
aws kinesis get-shard-iterator \
  --stream-name my-stream \
  --shard-id shardId-000000000000 \
  --shard-iterator-type TRIM_HORIZON
```

---

**基本写法：列出所有流**
`aws kinesis list-streams`
```bash
# 列出账户所有 Kinesis 流
aws kinesis list-streams
```

---

## EventBridge 事件

**基本写法：创建事件总线**
`aws events create-event-bus --name <总线名>`
```bash
# 创建自定义事件总线
aws events create-event-bus --name my-bus
```

---

**基本写法：发布事件**
`aws events put-events --entries <事件>`
```bash
# 向默认总线发布事件
aws events put-events \
  --entries '[{"Source":"my.app","DetailType":"Order","Detail":"{\"id\":12345}","EventBusName":"default"}]'
```

---

**基本写法：创建规则**
`aws events put-rule --name <规则名> --event-pattern <模式> --event-bus-name <总线>`
```bash
# 创建匹配指定源的规则
aws events put-rule \
  --name my-rule \
  --event-pattern '{"source":["my.app"]}' \
  --event-bus-name default
```

---

**基本写法：为目标添加权限**
`aws events put-targets --rule <规则名> --targets <目标>`
```bash
# 将 Lambda 函数设为规则目标
aws events put-targets \
  --rule my-rule \
  --targets '[{"Id":"1","Arn":"arn:aws:lambda:us-east-1:123456789012:function:my-func"}]'
```

---

**基本写法：定时触发**
`aws events put-rule --name <规则名> --schedule-expression <表达式>`
```bash
# 每 5 分钟触发一次
aws events put-rule \
  --name cron-rule \
  --schedule-expression 'rate(5 minutes)'
```

<!-- ============ 文档分隔线：034-cloud-computing/047-AWSDynamoDB.md ============ -->

## 表创建与管理

**基本写法：创建表**
`aws dynamodb create-table --table-name <表名> --attribute-definitions <属性> --key-schema <键> --billing-mode <计费>`
```bash
# 创建按用户 ID 分区的表
aws dynamodb create-table \
  --table-name Users \
  --attribute-definitions AttributeName=UserId,AttributeType=S \
  --key-schema AttributeName=UserId,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST
```

---

**基本写法：创建带排序键的表**
`aws dynamodb create-table --table-name <表名> --attribute-definitions <属性> --key-schema <键>`
```bash
# 创建复合主键表(分区键 + 排序键)
aws dynamodb create-table \
  --table-name Orders \
  --attribute-definitions AttributeName=UserId,AttributeType=S AttributeName=OrderId,AttributeType=S \
  --key-schema AttributeName=UserId,KeyType=HASH AttributeName=OrderId,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

---

**基本写法：列出所有表**
`aws dynamodb list-tables`
```bash
# 查看当前账户所有表
aws dynamodb list-tables
```

---

**基本写法：查看表描述**
`aws dynamodb describe-table --table-name <表名>`
```bash
# 查看表结构详情
aws dynamodb describe-table --table-name Users
```

---

**基本写法：删除表**
`aws dynamodb delete-table --table-name <表名>`
```bash
# 删除指定表及其所有数据
aws dynamodb delete-table --table-name Users
```

---

**基本写法：更新表配置**
`aws dynamodb update-table --table-name <表名> --billing-mode PROVISIONED --provisioned-throughput <吞吐量>`
```bash
# 切换为预置计费模式
aws dynamodb update-table \
  --table-name Users \
  --billing-mode PROVISIONED \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

---

## 数据写入

**基本写法：写入单条数据**
`aws dynamodb put-item --table-name <表名> --item <项>`
```bash
# 写入一条用户记录
aws dynamodb put-item \
  --table-name Users \
  --item '{"UserId":{"S":"u001"},"Name":{"S":"Alice"},"Age":{"N":"30"}}'
```

---

**基本写法：条件写入**
`aws dynamodb put-item --table-name <表名> --item <项> --condition-expression <条件>`
```bash
# 仅在用户不存在时写入
aws dynamodb put-item \
  --table-name Users \
  --item '{"UserId":{"S":"u001"},"Name":{"S":"Alice"}}' \
  --condition-expression 'attribute_not_exists(UserId)'
```

---

**基本写法：批量写入**
`aws dynamodb batch-write-item --request-items <请求>`
```bash
# 一次写入多条记录到多张表
aws dynamodb batch-write-item \
  --request-items '{
    "Users": [{"PutRequest":{"Item":{"UserId":{"S":"u002"},"Name":{"S":"Bob"}}}}],
    "Orders": [{"PutRequest":{"Item":{"UserId":{"S":"u002"},"OrderId":{"S":"o001"}}}}]
  }'
```

---

**基本写法：更新条目**
`aws dynamodb update-item --table-name <表名> --key <键> --update-expression <表达式> --expression-attribute-values <值>`
```bash
# 更新用户姓名和年龄
aws dynamodb update-item \
  --table-name Users \
  --key '{"UserId":{"S":"u001"}}' \
  --update-expression 'SET #n = :name, Age = :age' \
  --expression-attribute-names '{"#n":"Name"}' \
  --expression-attribute-values '{":name":{"S":"Alice Smith"},":age":{"N":"31"}}'
```

---

**基本写法：原子计数器更新**
`aws dynamodb update-item --table-name <表名> --key <键> --update-expression <表达式>`
```bash
# 原子自增计数
aws dynamodb update-item \
  --table-name Counters \
  --key '{"CounterId":{"S":"views"}}' \
  --update-expression 'SET Value = Value + :inc' \
  --expression-attribute-values '{":inc":{"N":"1"}}'
```

---

## 数据查询

**基本写法：按主键读取**
`aws dynamodb get-item --table-name <表名> --key <键>`
```bash
# 根据用户 ID 获取单条记录
aws dynamodb get-item \
  --table-name Users \
  --key '{"UserId":{"S":"u001"}}'
```

---

**基本写法：投影指定字段**
`aws dynamodb get-item --table-name <表名> --key <键> --projection-expression <字段>`
```bash
# 仅返回 Name 字段
aws dynamodb get-item \
  --table-name Users \
  --key '{"UserId":{"S":"u001"}}' \
  --projection-expression '#n' \
  --expression-attribute-names '{"#n":"Name"}'
```

---

**基本写法：查询分区键**
`aws dynamodb query --table-name <表名> --key-condition-expression <条件>`
```bash
# 查询指定用户所有订单
aws dynamodb query \
  --table-name Orders \
  --key-condition-expression 'UserId = :uid' \
  --expression-attribute-values '{":uid":{"S":"u001"}}'
```

---

**基本写法：范围查询排序键**
`aws dynamodb query --table-name <表名> --key-condition-expression <范围条件>`
```bash
# 查询用户订单 ID 在 o001-o099 之间
aws dynamodb query \
  --table-name Orders \
  --key-condition-expression 'UserId = :uid AND OrderId BETWEEN :start AND :end' \
  --expression-attribute-values '{":uid":{"S":"u001"},":start":{"S":"o001"},":end":{"S":"o099"}}'
```

---

**基本写法：索引分页**
`aws dynamodb query --table-name <表名> --key-condition-expression <条件> --limit <数量> --exclusive-start-key <键>`
```bash
# 翻页查询下 10 条
aws dynamodb query \
  --table-name Orders \
  --key-condition-expression 'UserId = :uid' \
  --expression-attribute-values '{":uid":{"S":"u001"}}' \
  --limit 10 \
  --exclusive-start-key '{"UserId":{"S":"u001"},"OrderId":{"S":"o010"}}'
```

---

## 扫描与过滤

**基本写法：全表扫描**
`aws dynamodb scan --table-name <表名>`
```bash
# 扫描表所有记录
aws dynamodb scan --table-name Users
```

---

**基本写法：扫描过滤**
`aws dynamodb scan --table-name <表名> --filter-expression <过滤> --expression-attribute-values <值>`
```bash
# 过滤年龄大于 25 的用户
aws dynamodb scan \
  --table-name Users \
  --filter-expression 'Age > :minAge' \
  --expression-attribute-values '{":minAge":{"N":"25"}}'
```

---

**基本写法：扫描分页**
`aws dynamodb scan --table-name <表名> --limit <数量> --exclusive-start-key <键>`
```bash
# 每次扫描 100 条
aws dynamodb scan --table-name Users --limit 100
```

---

**基本写法：并行扫描**
`aws dynamodb scan --table-name <表名> --total-segments <段数> --segment <段号>`
```bash
# 并行扫描第 0 段(总共 4 段)
aws dynamodb scan \
  --table-name Users \
  --total-segments 4 \
  --segment 0
```

---

**基本写法：删除条目**
`aws dynamodb delete-item --table-name <表名> --key <键>`
```bash
# 删除指定用户记录
aws dynamodb delete-item \
  --table-name Users \
  --key '{"UserId":{"S":"u001"}}'
```

---

## 索引管理

**基本写法：创建全局二级索引**
`aws dynamodb update-table --table-name <表名> --attribute-definitions <属性> --global-secondary-index-updates <索引>`
```bash
# 为 Users 表创建按 Email 查询的 GSI
aws dynamodb update-table \
  --table-name Users \
  --attribute-definitions AttributeName=Email,AttributeType=S \
  --global-secondary-index-updates '[{"Create":{"IndexName":"EmailIndex","KeySchema":[{"AttributeName":"Email","KeyType":"HASH"}],"Projection":{"ProjectionType":"ALL"},"ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":5}}}]'
```

---

**基本写法：查询全局二级索引**
`aws dynamodb query --table-name <表名> --index-name <索引名> --key-condition-expression <条件>`
```bash
# 通过 Email 索引查询
aws dynamodb query \
  --table-name Users \
  --index-name EmailIndex \
  --key-condition-expression 'Email = :email' \
  --expression-attribute-values '{":email":{"S":"alice@example.com"}}'
```

---

**基本写法：创建本地二级索引**
`aws dynamodb update-table --table-name <表名> --attribute-definitions <属性> --local-secondary-index-updates <索引>`
```bash
# 创建按 CreatedAt 排序的 LSI
aws dynamodb update-table \
  --table-name Orders \
  --attribute-definitions AttributeName=CreatedAt,AttributeType=S \
  --local-secondary-index-updates '[{"Create":{"IndexName":"CreatedIndex","KeySchema":[{"AttributeName":"UserId","KeyType":"HASH"},{"AttributeName":"CreatedAt","KeyType":"RANGE"}],"Projection":{"ProjectionType":"ALL"}}}]'
```

---

**基本写法：删除索引**
`aws dynamodb update-table --table-name <表名> --global-secondary-index-updates <删除>`
```bash
# 删除 EmailIndex 索引
aws dynamodb update-table \
  --table-name Users \
  --global-secondary-index-updates '[{"Delete":{"IndexName":"EmailIndex"}}]'
```

---

## 事务操作

**基本写法：事务写入**
`aws dynamodb transact-write-items --transact-items <项>`
```bash
# 原子写入用户和订单(要么都成功,要么都失败)
aws dynamodb transact-write-items \
  --transact-items '[
    {"Put":{"TableName":"Users","Item":{"UserId":{"S":"u003"},"Name":{"S":"Charlie"}}}},
    {"Put":{"TableName":"Orders","Item":{"UserId":{"S":"u003"},"OrderId":{"S":"o003"}}}}
  ]'
```

---

**基本写法：事务读取**
`aws dynamodb transact-get-items --transact-items <项>`
```bash
# 一次性原子读取多个条目
aws dynamodb transact-get-items \
  --transact-items '[
    {"Get":{"TableName":"Users","Key":{"UserId":{"S":"u001"}}}},
    {"Get":{"TableName":"Users","Key":{"UserId":{"S":"u002"}}}}
  ]'
```

---

**基本写法：条件检查事务**
`aws dynamodb transact-write-items --transact-items <带条件>`
```bash
# 带条件的事务写入
aws dynamodb transact-write-items \
  --transact-items '[
    {"Put":{"TableName":"Users","Item":{"UserId":{"S":"u004"}},"ConditionExpression":"attribute_not_exists(UserId)"}},
    {"Update":{"TableName":"Counters","Key":{"CounterId":{"S":"users"}},"UpdateExpression":"SET Value = Value + :inc","ExpressionAttributeValues":{":inc":{"N":"1"}}}}
  ]'
```

---

## 流与 TTL

**基本写法：启用 DynamoDB Streams**
`aws dynamodb update-table --table-name <表名> --stream-specification <规格>`
```bash
# 启用 NEW_AND_OLD_IMAGES 流
aws dynamodb update-table \
  --table-name Users \
  --stream-specification StreamEnabled=true,StreamViewType=NEW_AND_OLD_IMAGES
```

---

**基本写法：查看流描述**
`aws dynamodb describe-table --table-name <表名> --query 'Table.StreamSpecification'`
```bash
# 查看表的流配置
aws dynamodb describe-table \
  --table-name Users \
  --query 'Table.StreamSpecification'
```

---

**基本写法：启用 TTL**
`aws dynamodb update-time-to-live --table-name <表名> --time-to-live-specification <规格>`
```bash
# 启用 TTL 自动删除 30 天前的记录
aws dynamodb update-time-to-live \
  --table-name Sessions \
  --time-to-live-specification Enabled=true,AttributeName=expireAt
```

---

**基本写法：查看 TTL 配置**
`aws dynamodb describe-time-to-live --table-name <表名>`
```bash
# 查看表 TTL 状态
aws dynamodb describe-time-to-live --table-name Sessions
```

---

## 备份与恢复

**基本写法：创建备份**
`aws dynamodb create-backup --table-name <表名> --backup-name <备份名>`
```bash
# 创建表备份
aws dynamodb create-backup \
  --table-name Users \
  --backup-name Users-backup-20260731
```

---

**基本写法：列出备份**
`aws dynamodb list-backups`
```bash
# 列出所有备份
aws dynamodb list-backups
```

---

**基本写法：从备份还原表**
`aws dynamodb restore-table-from-backup --target-table-name <新表> --backup-arn <备份ARN>`
```bash
# 从备份还原到新表
aws dynamodb restore-table-from-backup \
  --target-table-name Users-restored \
  --backup-arn arn:aws:dynamodb:us-east-1:123456789012:table/Users/backup/01234567890123-Users-backup
```

---

**基本写法：跨表还原**
`aws dynamodb restore-table-to-point-in-time --source-table-name <源表> --target-table-name <目标表>`
```bash
# 时间点恢复(PITR)到新表
aws dynamodb restore-table-to-point-in-time \
  --source-table-name Users \
  --target-table-name Users-recovered \
  --use-latest-restorable-time
```

---

**基本写法：导出到 S3**
`aws dynamodb export-table-to-point-in-time --table-arn <表ARN> --s3-bucket <桶> --s3-prefix <前缀> --export-format <格式>`
```bash
# 导出表数据到 S3
aws dynamodb export-table-to-point-in-time \
  --table-arn arn:aws:dynamodb:us-east-1:123456789012:table/Users \
  --s3-bucket my-bucket \
  --s3-prefix dynamodb-exports/Users/ \
  --export-format DYNAMODB_JSON
```

---

## 容量与计费

**基本写法：自动扩容**
`aws application-autoscaling register-scalable-target --service-namespace dynamodb --resource-id <资源> --scalable-dimension <维度>`
```bash
# 注册表的写入容量为可伸缩目标
aws application-autoscaling register-scalable-target \
  --service-namespace dynamodb \
  --resource-id table/Users \
  --scalable-dimension dynamodb:table:WriteCapacityUnits \
  --min-capacity 5 \
  --max-capacity 100
```

---

**基本写法：配置扩容策略**
`aws application-autoscaling put-scaling-policy --policy-name <策略> --service-namespace dynamodb --resource-id <资源> --policy-type TargetTrackingScaling`
```bash
# 目标追踪策略保持利用率 70%
aws application-autoscaling put-scaling-policy \
  --policy-name UsersWriteScaling \
  --service-namespace dynamodb \
  --resource-id table/Users \
  --scalable-dimension dynamodb:table:WriteCapacityUnits \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration '{"TargetValue":70.0,"PredefinedMetricSpecification":{"PredefinedMetricType":"DynamoDBWriteCapacityUtilization"}}'
```

---

**基本写法：查看表消费容量**
`aws cloudwatch get-metric-statistics --namespace AWS/DynamoDB --metric-name ConsumedReadCapacityUnits`
```bash
# 查询表已消费读容量
aws cloudwatch get-metric-statistics \
  --namespace AWS/DynamoDB \
  --metric-name ConsumedReadCapacityUnits \
  --dimensions Name=TableName,Value=Users \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Sum
```

<!-- ============ 文档分隔线：034-cloud-computing/048-AzureFunctions.md ============ -->

## 核心工具安装

**基本写法：安装 Azure Functions Core Tools**
`npm install -g azure-functions-core-tools@<版本>`
```bash
# 安装 Azure Functions Core Tools v4
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

---

**基本写法：查看版本**
`func --version`
```bash
# 查看 Core Tools 版本
func --version
```

---

**基本写法：查看帮助**
`func --help`
```bash
# 查看所有可用命令
func --help
```

---

**基本写法：登录 Azure**
`az login`
```bash
# 通过浏览器交互登录 Azure
az login
```

---

**基本写法：设置默认订阅**
`az account set --subscription <订阅ID>`
```bash
# 切换到指定订阅
az account set --subscription 00000000-0000-0000-0000-000000000000
```

---

## 项目创建

**基本写法：创建项目**
`func init <项目名> [--worker-runtime <运行时>]`
```bash
# 创建 Node.js v18 项目
func init my-functions --worker-runtime node --language javascript
```

---

**基本写法：创建 Python 项目**
`func init <项目名> --worker-runtime python --model V2`
```bash
# 创建 Python V2 编程模型项目
func init my-py-funcs --worker-runtime python --model V2
```

---

**基本写法：创建 .NET 项目**
`func init <项目名> --worker-runtime dotnet`
```bash
# 创建 .NET 隔离工作进程项目
func init my-dotnet-funcs --worker-runtime dotnet-isolated
```

---

**基本写法：创建 Docker 项目**
`func init <项目名> --docker`
```bash
# 创建带 Dockerfile 的项目
func init my-docker-funcs --worker-runtime node --docker
```

---

## 函数创建

**基本写法：创建函数**
`func new --name <函数名> --template <模板>`
```bash
# 创建 HTTP 触发函数
func new --name HttpExample --template "HTTP trigger"
```

---

**基本写法：创建定时函数**
`func new --name <函数名> --template "Timer trigger"`
```bash
# 创建定时触发函数
func new --name DailyJob --template "Timer trigger"
```

---

**基本写法：创建队列触发函数**
`func new --name <函数名> --template "Azure Queue Storage trigger"`
```bash
# 创建队列触发函数
func new --name QueueHandler --template "Azure Queue Storage trigger"
```

---

**基本写法：创建 Cosmos DB 触发函数**
`func new --name <函数名> --template "Azure Cosmos DB trigger"`
```bash
# 创建 Cosmos DB 变更触发函数
func new --name CosmosTrigger --template "Azure Cosmos DB trigger"
```

---

**基本写法：查看可用模板**
`func templates list`
```bash
# 列出所有可用函数模板
func templates list
```

---

## 本地运行

**基本写法：本地运行项目**
`func start [--port <端口>]`
```bash
# 在 7071 端口启动本地运行时
func start --port 7071
```

---

**基本写法：指定运行时**
`func start --runtime <运行时>`
```bash
# 强制使用 node 运行时启动
func start --runtime node
```

---

**基本写法：使用本地设置文件**
`func start --functions <函数名>`
```bash
# 仅启动指定函数
func start --functions HttpExample
```

---

**基本写法：连接本地存储模拟器**
`func start`
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "node"
  }
}
```

---

## 部署到 Azure

**基本写法：部署函数应用**
`func azure functionapp publish <应用名>`
```bash
# 部署到已有函数应用
func azure functionapp publish my-func-app
```

---

**基本写法：发布并显示部署脚本**
`func azure functionapp publish <应用名> --publish-local-settings`
```bash
# 同时部署本地设置
func azure functionapp publish my-func-app --publish-local-settings
```

---

**基本写法：使用 zip 部署**
`az functionapp deployment source config-zip --name <应用名> --resource-group <组> --src <zip>`
```bash
# 通过 zip 包部署
az functionapp deployment source config-zip \
  --name my-func-app \
  --resource-group my-rg \
  --src deploy.zip
```

---

**基本写法：从 Git 部署**
`az functionapp deployment source config --name <应用名> --resource-group <组> --repo-url <URL> --branch <分支>`
```bash
# 从 GitHub 持续部署
az functionapp deployment source config \
  --name my-func-app \
  --resource-group my-rg \
  --repo-url https://github.com/myorg/myrepo \
  --branch main \
  --manual-integration
```

---

**基本写法：启用部署槽**
`az functionapp deployment slot create --name <应用名> --resource-group <组> --slot <槽名>`
```bash
# 创建 staging 部署槽
az functionapp deployment slot create \
  --name my-func-app \
  --resource-group my-rg \
  --slot staging
```

---

## 应用服务计划

**基本写法：创建消费计划**
`az functionapp plan create --name <计划名> --resource-group <组> --location <区域> --sku <SKU>`
```bash
# 创建消费计划(按需计费)
az functionapp plan create \
  --name my-plan \
  --resource-group my-rg \
  --location eastus \
  --sku Y1 \
  --is-linux
```

---

**基本写法：创建高级计划**
`az functionapp plan create --name <计划名> --sku EP1`
```bash
# 创建 EP1 高级计划(预置实例)
az functionapp plan create \
  --name my-premium-plan \
  --resource-group my-rg \
  --location eastus \
  --sku EP1 \
  --is-linux
```

---

**基本写法：创建函数应用**
`az functionapp create --name <应用名> --storage-account <存储> --plan <计划> --resource-group <组> --runtime <运行时>`
```bash
# 创建 Node.js 函数应用
az functionapp create \
  --name my-func-app \
  --storage-account mystorage123 \
  --plan my-plan \
  --resource-group my-rg \
  --runtime node \
  --runtime-version 20 \
  --functions-version 4
```

---

**基本写法：查看函数应用**
`az functionapp list --resource-group <组>`
```bash
# 列出资源组下所有函数应用
az functionapp list --resource-group my-rg --output table
```

---

**基本写法：删除函数应用**
`az functionapp delete --name <应用名> --resource-group <组>`
```bash
# 删除函数应用
az functionapp delete --name my-func-app --resource-group my-rg
```

---

## 配置与连接

**基本写法：设置应用设置**
`az functionapp config appsettings set --name <应用名> --resource-group <组> --settings <键=值>`
```bash
# 设置数据库连接字符串
az functionapp config appsettings set \
  --name my-func-app \
  --resource-group my-rg \
  --settings DB_CONNECTION="Server=...;Database=..."
```

---

**基本写法：查看应用设置**
`az functionapp config appsettings list --name <应用名> --resource-group <组>`
```bash
# 列出所有应用设置
az functionapp config appsettings list \
  --name my-func-app \
  --resource-group my-rg
```

---

**基本写法：删除应用设置**
`az functionapp config appsettings delete --name <应用名> --resource-group <组> --setting-names <键>`
```bash
# 删除指定配置项
az functionapp config appsettings delete \
  --name my-func-app \
  --resource-group my-rg \
  --setting-names OLD_KEY
```

---

**基本写法：绑定存储账户**
`az functionapp config appsettings set --name <应用名> --settings AzureWebJobsStorage=<连接串>`
```bash
# 设置运行时所需的存储连接
az functionapp config appsettings set \
  --name my-func-app \
  --resource-group my-rg \
  --settings AzureWebJobsStorage="DefaultEndpointsProtocol=https;AccountName=..."
```

---

## 触发器与绑定配置

**基本写法：HTTP 触发器配置**
```json
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["get", "post"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ]
}
```

---

**基本写法：定时触发器配置**
```json
{
  "bindings": [
    {
      "type": "timerTrigger",
      "direction": "in",
      "name": "myTimer",
      "schedule": "0 0 * * * *"
    }
  ]
}
```

---

**基本写法：队列输出绑定**
```json
{
  "bindings": [
    {
      "type": "queue",
      "direction": "out",
      "name": "outputQueueItem",
      "queueName": "myqueue",
      "connection": "AzureWebJobsStorage"
    }
  ]
}
```

---

**基本写法：Python V2 模型触发器**
```python
# Python V2 编程模型的装饰器触发器
import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="hello")
def hello(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Hello, World!")
```

---

## 监控与诊断

**基本写法：查看函数日志**
`az functionapp log tail --name <应用名> --resource-group <组>`
```bash
# 实时查看应用日志流
az functionapp log tail \
  --name my-func-app \
  --resource-group my-rg
```

---

**基本写法：启用 Application Insights**
`az monitor app-insights component create --app <名称> --location <区域> --resource-group <组>`
```bash
# 创建 Application Insights 资源
az monitor app-insights component create \
  --app my-ai \
  --location eastus \
  --resource-group my-rg
```

---

**基本写法：关联 Application Insights**
`az functionapp config appsettings set --name <应用名> --settings APPINSIGHTS_INSTRUMENTATIONKEY=<键>`
```bash
# 将 Application Insights 连接到函数应用
az functionapp config appsettings set \
  --name my-func-app \
  --resource-group my-rg \
  --settings APPINSIGHTS_INSTRUMENTATIONKEY=00000000-0000-0000-0000-000000000000
```

---

**基本写法：执行函数**
`az functionapp function invoke --name <应用名> --resource-group <组> --function-name <函数>`
```bash
# 通过 Azure CLI 远程调用函数
az functionapp function invoke \
  --name my-func-app \
  --resource-group my-rg \
  --function-name HttpExample
```

---

## 持久化函数

**基本写法：安装 Durable Functions 扩展**
`func extensions install --package Microsoft.Azure.WebJobs.Extensions.DurableTask --version <版本>`
```bash
# 安装 Durable Functions 扩展
func extensions install \
  --package Microsoft.Azure.WebJobs.Extensions.DurableTask \
  --version 2.13.0
```

---

**基本写法：存储提供者配置**
```json
{
  "extensions": {
    "durableTask": {
      "storageProvider": {
        "type": "AzureStorage",
        "connectionStringName": "AzureWebJobsStorage"
      },
      "hubName": "MyTaskHub"
    }
  }
}
```

---

**基本写法：Netherite 存储提供者**
```json
{
  "extensions": {
    "durableTask": {
      "storageProvider": {
        "type": "Netherite",
        "storageConnectionName": "AzureWebJobsStorage",
        "eventHubName": "durable-event-hub"
      }
    }
  }
}
```

---

## 部署槽与 CI/CD

**基本写法：交换部署槽**
`az functionapp deployment slot swap --name <应用名> --resource-group <组> --slot <槽名> --target-slot production`
```bash
# 将 staging 槽交换到生产
az functionapp deployment slot swap \
  --name my-func-app \
  --resource-group my-rg \
  --slot staging \
  --target-slot production
```

---

**基本写法：列出部署槽**
`az functionapp deployment slot list --name <应用名> --resource-group <组>`
```bash
# 查看应用所有部署槽
az functionapp deployment slot list \
  --name my-func-app \
  --resource-group my-rg
```

---

**基本写法：删除部署槽**
`az functionapp deployment slot delete --name <应用名> --resource-group <组> --slot <槽名>`
```bash
# 删除指定部署槽
az functionapp deployment slot delete \
  --name my-func-app \
  --resource-group my-rg \
  --slot staging
```

---

**基本写法：配置 GitHub Actions 部署**
`az functionapp deployment github-actions add --repo <仓库> --resource-group <组> --name <应用名> --branch <分支>`
```bash
# 为函数应用配置 GitHub Actions CI
az functionapp deployment github-actions add \
  --repo myorg/myrepo \
  --resource-group my-rg \
  --name my-func-app \
  --branch main
```

---

## 密钥管理

**基本写法：列出函数密钥**
`az functionapp function keys list --name <应用名> --resource-group <组> --function-name <函数>`
```bash
# 查看 HttpExample 函数的密钥
az functionapp function keys list \
  --name my-func-app \
  --resource-group my-rg \
  --function-name HttpExample
```

---

**基本写法：设置函数密钥**
`az functionapp function keys set --name <应用名> --resource-group <组> --function-name <函数> --key-name <键名> --key-value <值>`
```bash
# 设置自定义函数密钥
az functionapp function keys set \
  --name my-func-app \
  --resource-group my-rg \
  --function-name HttpExample \
  --key-name MyKey \
  --key-value MySecretValue123
```

---

**基本写法：设置主机密钥**
`az functionapp keys set --name <应用名> --resource-group <组> --key-name <键名> --key-value <值> --key-type masterKey`
```bash
# 设置主机密钥(所有函数共用)
az functionapp keys set \
  --name my-func-app \
  --resource-group my-rg \
  --key-name MyHostKey \
  --key-value MyHostKeyValue123 \
  --key-type masterKey
```

---

**基本写法：使用函数密钥调用**
```bash
# 通过 URL 查询参数传递密钥调用 HTTP 函数
curl "https://my-func-app.azurewebsites.net/api/HttpExample?code=MySecretValue123"
```

<!-- ============ 文档分隔线：034-cloud-computing/049-AzureAKSCommands.md ============ -->

## 集群创建

**基本写法：创建 AKS 集群**
`az aks create --name <集群名> --resource-group <组> --node-count <节点数> --generate-ssh-keys`
```bash
# 创建 3 节点 AKS 集群
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --node-count 3 \
  --node-vm-size Standard_DS2_v2 \
  --generate-ssh-keys
```

---

**基本写法：创建带系统池的集群**
`az aks create --name <集群名> --resource-group <组> --nodepool-name <池名> --node-count <数量>`
```bash
# 创建系统节点池
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --nodepool-name systempool \
  --node-count 3 \
  --mode System
```

---

**基本写法：使用托管 AAD 集成**
`az aks create --name <集群名> --resource-group <组> --enable-aad --aad-admin-group-object-ids <组ID>`
```bash
# 启用 Azure AD 集成与 RBAC
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --enable-aad \
  --aad-admin-group-object-ids 00000000-0000-0000-0000-000000000000 \
  --enable-azure-rbac
```

---

**基本写法：创建带网络插件集群**
`az aks create --name <集群名> --network-plugin <插件> --network-plugin-mode <模式>`
```bash
# 创建 Azure CNI Overlay 网络的集群
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --network-plugin azure \
  --network-plugin-mode overlay \
  --pod-cidr 10.244.0.0/16
```

---

**基本写法：使用可用区**
`az aks create --name <集群名> --resource-group <组> --zones 1 2 3`
```bash
# 跨三个可用区部署节点
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --zones 1 2 3 \
  --node-count 3
```

---

## 凭证与访问

**基本写法：获取集群凭证**
`az aks get-credentials --name <集群名> --resource-group <组>`
```bash
# 将 AKS 凭证合并到 kubeconfig
az aks get-credentials \
  --name my-aks \
  --resource-group my-rg
```

---

**基本写法：覆盖现有凭证**
`az aks get-credentials --name <集群名> --resource-group <组> --overwrite-existing`
```bash
# 覆盖已有的同名上下文
az aks get-credentials \
  --name my-aks \
  --resource-group my-rg \
  --overwrite-existing
```

---

**基本写法：使用管理员凭证**
`az aks get-credentials --name <集群名> --resource-group <组> --admin`
```bash
# 获取 cluster-admin 凭证(应急使用)
az aks get-credentials \
  --name my-aks \
  --resource-group my-rg \
  --admin
```

---

**基本写法：查看集群信息**
`az aks show --name <集群名> --resource-group <组>`
```bash
# 查看集群详细配置
az aks show --name my-aks --resource-group my-rg
```

---

**基本写法：列出所有集群**
`az aks list --resource-group <组>`
```bash
# 列出资源组下所有 AKS 集群
az aks list --resource-group my-rg --output table
```

---

## 节点池管理

**基本写法：添加节点池**
`az aks nodepool add --cluster-name <集群> --name <池名> --resource-group <组> --node-count <数量>`
```bash
# 添加用户节点池
az aks nodepool add \
  --cluster-name my-aks \
  --name userpool \
  --resource-group my-rg \
  --node-count 5 \
  --node-vm-size Standard_DS3_v2 \
  --mode User
```

---

**基本写法：列出节点池**
`az aks nodepool list --cluster-name <集群> --resource-group <组>`
```bash
# 查看集群所有节点池
az aks nodepool list \
  --cluster-name my-aks \
  --resource-group my-rg \
  --output table
```

---

**基本写法：缩放节点池**
`az aks nodepool scale --cluster-name <集群> --name <池名> --resource-group <组> --node-count <数量>`
```bash
# 将节点池缩放到 8 个节点
az aks nodepool scale \
  --cluster-name my-aks \
  --name userpool \
  --resource-group my-rg \
  --node-count 8
```

---

**基本写法：删除节点池**
`az aks nodepool delete --cluster-name <集群> --name <池名> --resource-group <组>`
```bash
# 删除指定节点池
az aks nodepool delete \
  --cluster-name my-aks \
  --name userpool \
  --resource-group my-rg
```

---

**基本写法：升级节点池**
`az aks nodepool upgrade --cluster-name <集群> --name <池名> --resource-group <组> --kubernetes-version <版本>`
```bash
# 升级节点池到指定 K8s 版本
az aks nodepool upgrade \
  --cluster-name my-aks \
  --name userpool \
  --resource-group my-rg \
  --kubernetes-version 1.30.0
```

---

## 集群升级与维护

**基本写法：查看可用升级版本**
`az aks get-upgrades --name <集群名> --resource-group <组>`
```bash
# 列出集群可升级的版本
az aks get-upgrades \
  --name my-aks \
  --resource-group my-rg
```

---

**基本写法：升级集群**
`az aks upgrade --name <集群名> --resource-group <组> --kubernetes-version <版本>`
```bash
# 升级集群控制面到 1.30.0
az aks upgrade \
  --name my-aks \
  --resource-group my-rg \
  --kubernetes-version 1.30.0
```

---

**基本写法：仅升级控制面**
`az aks upgrade --name <集群名> --resource-group <组> --kubernetes-version <版本> --control-plane-only`
```bash
# 仅升级控制面不升级节点
az aks upgrade \
  --name my-aks \
  --resource-group my-rg \
  --kubernetes-version 1.30.0 \
  --control-plane-only
```

---

**基本写法：配置维护窗口**
`az aks maintenanceconfiguration add --cluster-name <集群> --resource-group <组> --name <配置名> --config-file <文件>`
```bash
# 配置每周六维护窗口
az aks maintenanceconfiguration add \
  --cluster-name my-aks \
  --resource-group my-rg \
  --name default \
  --config-file maintenance.json
```

---

**基本写法：自动升级配置**
`az aks update --name <集群名> --resource-group <组> --auto-upgrade-channel <通道>`
```bash
# 启用 stable 自动升级通道
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --auto-upgrade-channel stable
```

---

## 缩放与自动伸缩

**基本写法：手动缩放集群**
`az aks scale --name <集群名> --resource-group <组> --node-count <数量>`
```bash
# 调整节点数为 5
az aks scale \
  --name my-aks \
  --resource-group my-rg \
  --node-count 5
```

---

**基本写法：启用集群自动伸缩**
`az aks update --name <集群名> --resource-group <组> --enable-cluster-autoscaler --min-count <最小> --max-count <最大>`
```bash
# 启用集群自动伸缩 3-10
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-cluster-autoscaler \
  --min-count 3 \
  --max-count 10
```

---

**基本写法：节点池自动伸缩**
`az aks nodepool update --cluster-name <集群> --name <池名> --enable-cluster-autoscaler --min-count <最小> --max-count <最大>`
```bash
# 为用户节点池启用自动伸缩
az aks nodepool update \
  --cluster-name my-aks \
  --name userpool \
  --resource-group my-rg \
  --enable-cluster-autoscaler \
  --min-count 2 \
  --max-count 20
```

---

**基本写法：禁用集群自动伸缩**
`az aks update --name <集群名> --resource-group <组> --disable-cluster-autoscaler`
```bash
# 关闭集群自动伸缩
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --disable-cluster-autoscaler
```

---

**基本写法：启用 KEDA 事件驱动伸缩**
`az aks update --name <集群名> --resource-group <组> --enable-keda`
```bash
# 启用 KEDA 工作负载伸缩
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-keda
```

---

## 网络配置

**基本写法：启用 HTTP 应用路由**
`az aks update --name <集群名> --resource-group <组> --enable-http-application-routing`
```bash
# 启用 HTTP 应用路由附加功能
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-http-application-routing
```

---

**基本写法：启用 Azure 服务网格**
`az aks update --name <集群名> --resource-group <组> --enable-azure-service-mesh`
```bash
# 启用 Azure Service Mesh
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-azure-service-mesh
```

---

**基本写法：配置出口负载均衡器**
`az aks create --name <集群名> --resource-group <组> --load-balancer-outbound-ips <IP ID>`
```bash
# 使用指定公网 IP 作为出口
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --load-balancer-outbound-ips /subscriptions/.../providers/Microsoft.Network/publicIPAddresses/my-ip
```

---

**基本写法：私有集群**
`az aks create --name <集群名> --resource-group <组> --enable-private-cluster`
```bash
# 创建私有集群(API 服务器不可公网访问)
az aks create \
  --name my-aks \
  --resource-group my-rg \
  --enable-private-cluster \
  --enable-private-cluster-public-fqdn
```

---

## 安全与身份

**基本写法：启用工作负载身份**
`az aks update --name <集群名> --resource-group <组> --enable-workload-identity --enable-oidc-issuer`
```bash
# 启用 Workload Identity(替代 AAD Pod Identity)
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-workload-identity \
  --enable-oidc-issuer
```

---

**基本写法：查看 OIDC 颁发者 URL**
`az aks show --name <集群名> --resource-group <组> --query oidcIssuerProfile.issuerURL`
```bash
# 获取 OIDC 颁发者 URL
az aks show \
  --name my-aks \
  --resource-group my-rg \
  --query oidcIssuerProfile.issuerURL \
  --output tsv
```

---

**基本写法：启用 Azure Key Vault 密钥库**
`az aks update --name <集群名> --resource-group <组> --enable-keyvault-secrets-provider`
```bash
# 启用 Key Vault Secrets Provider
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-keyvault-secrets-provider \
  --rotate-secret-after 30d
```

---

**基本写法：分配 Azure 角色**
`az role assignment create --role <角色> --assignee <对象ID> --scope <范围>`
```bash
# 为用户授予 AKS 集群用户角色
az role assignment create \
  --role "Azure Kubernetes Service Cluster User Role" \
  --assignee 00000000-0000-0000-0000-000000000000 \
  --scope /subscriptions/.../resourceGroups/my-rg/providers/Microsoft.ContainerService/managedClusters/my-aks
```

---

## 监控与诊断

**基本写法：启用 Container Insights**
`az aks update --name <集群名> --resource-group <组> --enable-azure-monitor`
```bash
# 启用 Container Insights 监控
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-azure-monitor \
  --workspace-resource-id /subscriptions/.../providers/Microsoft.OperationalInsights/workspaces/my-law
```

---

**基本写法：查看集群健康状态**
`az aks show --name <集群名> --resource-group <组> --query 'powerState'`
```bash
# 查看集群电源状态
az aks show \
  --name my-aks \
  --resource-group my-rg \
  --query 'powerState'
```

---

**基本写法：列出集群活动日志**
`az monitor activity-log list --resource-id <集群ID>`
```bash
# 查看 AKS 集群活动日志
az monitor activity-log list \
  --resource-id /subscriptions/.../resourceGroups/my-rg/providers/Microsoft.ContainerService/managedClusters/my-aks \
  --max-events 50
```

---

**基本写法：运行命令**
`az aks command invoke --name <集群名> --resource-group <组> --command <命令>`
```bash
# 远程在集群中执行 kubectl 命令
az aks command invoke \
  --name my-aks \
  --resource-group my-rg \
  --command "kubectl get pods -A"
```

---

## 附加组件与功能

**基本写法：启用 ACI 虚拟节点**
`az aks update --name <集群名> --resource-group <组> --enable-virtual-node`
```bash
# 启用虚拟节点(Serverless 容器)
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-virtual-node \
  --subnet aci-subnet
```

---

**基本写法：启用 GitOps**
`az aks update --name <集群名> --resource-group <组> --enable-azure-policy`
```bash
# 启用 Azure Policy 用于合规管理
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-azure-policy
```

---

**基本写法：启用 Image Cleaner**
`az aks update --name <集群名> --resource-group <组> --enable-image-cleaner`
```bash
# 启用 Eraser 清理未使用镜像
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-image-cleaner \
  --image-cleaner-interval-hours 24
```

---

**基本写法：启用节点快照**
`az aks update --name <集群名> --resource-group <组> --enable-node-snapshot`
```bash
# 启用节点配置快照
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --enable-node-snapshot
```

---

## 集群停止与删除

**基本写法：停止集群**
`az aks stop --name <集群名> --resource-group <组>`
```bash
# 停止集群节省成本(保留状态)
az aks stop \
  --name my-aks \
  --resource-group my-rg
```

---

**基本写法：启动集群**
`az aks start --name <集群名> --resource-group <组>`
```bash
# 启动已停止的集群
az aks start \
  --name my-aks \
  --resource-group my-rg
```

---

**基本写法：删除集群**
`az aks delete --name <集群名> --resource-group <组> --yes --no-wait`
```bash
# 删除 AKS 集群
az aks delete \
  --name my-aks \
  --resource-group my-rg \
  --yes \
  --no-wait
```

---

**基本写法：仅删除集群但不删除资源组**
`az aks delete --name <集群名> --resource-group <组>`
```bash
# 交互式确认删除集群
az aks delete \
  --name my-aks \
  --resource-group my-rg
```

---

## ACR 容器注册表集成

**基本写法：创建 ACR**
`az acr create --name <注册表名> --resource-group <组> --sku <SKU>`
```bash
# 创建 Premium ACR
az acr create \
  --name myacr123 \
  --resource-group my-rg \
  --sku Premium
```

---

**基本写法：附加 ACR 到 AKS**
`az aks update --name <集群名> --resource-group <组> --attach-acr <ACR 名>`
```bash
# 让 AKS 集群有权限拉取 ACR 镜像
az aks update \
  --name my-aks \
  --resource-group my-rg \
  --attach-acr myacr123
```

---

**基本写法：登录 ACR**
`az acr login --name <注册表名>`
```bash
# 登录 ACR
az acr login --name myacr123
```

---

**基本写法：列出仓库**
`az acr repository list --name <注册表名>`
```bash
# 列出 ACR 中所有镜像仓库
az acr repository list --name myacr123 --output table
```

<!-- ============ 文档分隔线：034-cloud-computing/050-GCPGKECommands.md ============ -->

## 凭证与项目

**基本写法：登录 GCP**
`gcloud auth login`
```bash
# 通过浏览器交互登录 Google Cloud
gcloud auth login
```

---

**基本写法：设置项目**
`gcloud config set project <项目ID>`
```bash
# 切换到指定项目
gcloud config set project my-project-123
```

---

**基本写法：查看当前配置**
`gcloud config list`
```bash
# 查看当前账户、项目等配置
gcloud config list
```

---

**基本写法：应用凭证**
`gcloud auth application-default login`
```bash
# 为本地应用设置默认凭证
gcloud auth application-default login
```

---

**基本写法：列出账户**
`gcloud auth list`
```bash
# 查看所有已登录账户
gcloud auth list
```

---

## 集群创建

**基本写法：创建 Autopilot 集群**
`gcloud container clusters create-auto <集群名> --region <区域>`
```bash
# 创建 Autopilot 集群(Google 托管节点)
gcloud container clusters create-auto my-gke \
  --region us-central1
```

---

**基本写法：创建标准集群**
`gcloud container clusters create <集群名> --region <区域> --num-nodes <节点数>`
```bash
# 创建标准模式 GKE 集群
gcloud container clusters create my-gke \
  --region us-central1 \
  --num-nodes 3 \
  --machine-type e2-medium
```

---

**基本写法：创建带可用区集群**
`gcloud container clusters create <集群名> --zone <可用区> --num-nodes <数量>`
```bash
# 创建单可用区集群
gcloud container clusters create my-gke \
  --zone us-central1-a \
  --num-nodes 3
```

---

**基本写法：启用 Workload Identity**
`gcloud container clusters create <集群名> --region <区域> --workload-pool <项目ID>.svc.id.goog`
```bash
# 启用 Workload Identity
gcloud container clusters create my-gke \
  --region us-central1 \
  --workload-pool my-project-123.svc.id.goog
```

---

**基本写法：使用发布通道**
`gcloud container clusters create <集群名> --region <区域> --release-channel <通道>`
```bash
# 使用 Regular 发布通道
gcloud container clusters create my-gke \
  --region us-central1 \
  --release-channel regular \
  --enable-ip-alias
```

---

## 凭证与连接

**基本写法：获取集群凭证**
`gcloud container clusters get-credentials <集群名> --region <区域>`
```bash
# 配置 kubectl 连接到 GKE 集群
gcloud container clusters get-credentials my-gke \
  --region us-central1
```

---

**基本写法：跨项目获取凭证**
`gcloud container clusters get-credentials <集群名> --region <区域> --project <项目ID>`
```bash
# 访问其他项目的集群
gcloud container clusters get-credentials my-gke \
  --region us-central1 \
  --project other-project-456
```

---

**基本写法：使用内部 IP**
`gcloud container clusters get-credentials <集群名> --region <区域> --internal-ip`
```bash
# 通过内部 IP 连接私有集群
gcloud container clusters get-credentials my-gke \
  --region us-central1 \
  --internal-ip
```

---

**基本写法：查看集群列表**
`gcloud container clusters list`
```bash
# 列出当前项目所有集群
gcloud container clusters list
```

---

**基本写法：查看集群详情**
`gcloud container clusters describe <集群名> --region <区域>`
```bash
# 查看 my-gke 集群配置
gcloud container clusters describe my-gke \
  --region us-central1
```

---

## 节点池管理

**基本写法：创建节点池**
`gcloud container node-pools create <池名> --cluster <集群> --region <区域> --num-nodes <数量>`
```bash
# 为集群添加新节点池
gcloud container node-pools create user-pool \
  --cluster my-gke \
  --region us-central1 \
  --num-nodes 5 \
  --machine-type e2-standard-4
```

---

**基本写法：列出节点池**
`gcloud container node-pools list --cluster <集群> --region <区域>`
```bash
# 查看集群所有节点池
gcloud container node-pools list \
  --cluster my-gke \
  --region us-central1
```

---

**基本写法：缩放节点池**
`gcloud container clusters resize <集群> --region <区域> --node-pool <池名> --num-nodes <数量>`
```bash
# 缩放节点池到 10 个节点
gcloud container clusters resize my-gke \
  --region us-central1 \
  --node-pool user-pool \
  --num-nodes 10
```

---

**基本写法：删除节点池**
`gcloud container node-pools delete <池名> --cluster <集群> --region <区域>`
```bash
# 删除指定节点池
gcloud container node-pools delete user-pool \
  --cluster my-gke \
  --region us-central1
```

---

**基本写法：GPU 节点池**
`gcloud container node-pools create <池名> --accelerator type=<GPU 类型>,count=<数量>`
```bash
# 创建带 T4 GPU 的节点池
gcloud container node-pools create gpu-pool \
  --cluster my-gke \
  --region us-central1 \
  --num-nodes 2 \
  --machine-type n1-standard-4 \
  --accelerator type=nvidia-tesla-t4,count=1
```

---

## 集群升级

**基本写法：查看可用升级版本**
`gcloud container get-server-config --region <区域>`
```bash
# 查看区域支持的所有版本
gcloud container get-server-config \
  --region us-central1
```

---

**基本写法：升级集群控制面**
`gcloud container clusters upgrade <集群> --region <区域> --master --cluster-version <版本>`
```bash
# 升级控制面到 1.30
gcloud container clusters upgrade my-gke \
  --region us-central1 \
  --master \
  --cluster-version 1.30.1-gke.1000
```

---

**基本写法：升级节点池**
`gcloud container clusters upgrade <集群> --region <区域> --node-pool <池名> --cluster-version <版本>`
```bash
# 升级指定节点池
gcloud container clusters upgrade my-gke \
  --region us-central1 \
  --node-pool default-pool \
  --cluster-version 1.30.1-gke.1000
```

---

**基本写法：仅升级一部分节点**
`gcloud container clusters upgrade <集群> --region <区域> --node-pool <池名> --batch-soak-duration <时间>`
```bash
# 分批升级节点池并设置间隔
gcloud container clusters upgrade my-gke \
  --region us-central1 \
  --node-pool default-pool \
  --batch-size 3 \
  --batch-soak-duration 120s
```

---

**基本写法：取消升级**
`gcloud container clusters upgrade <集群> --region <区域> --node-pool <池名> --cancel`
```bash
# 取消正在进行的节点池升级
gcloud container clusters upgrade my-gke \
  --region us-central1 \
  --node-pool default-pool \
  --cancel
```

---

## 自动伸缩与维护

**基本写法：启用节点自动伸缩**
`gcloud container clusters update <集群> --region <区域> --enable-autoscaling --min-nodes <最小> --max-nodes <最大>`
```bash
# 启用集群自动伸缩 1-10
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-autoscaling \
  --min-nodes 1 \
  --max-nodes 10 \
  --node-pool default-pool
```

---

**基本写法：禁用自动伸缩**
`gcloud container clusters update <集群> --region <区域> --no-enable-autoscaling`
```bash
# 关闭节点自动伸缩
gcloud container clusters update my-gke \
  --region us-central1 \
  --no-enable-autoscaling \
  --node-pool default-pool
```

---

**基本写法：配置维护窗口**
`gcloud container clusters update <集群> --region <区域> --maintenance-window-start <时间>`
```bash
# 设置每日凌晨维护窗口
gcloud container clusters update my-gke \
  --region us-central1 \
  --maintenance-window-start 03:00 \
  --maintenance-window-end 07:00 \
  --maintenance-window-recurrence FREQ=DAILY
```

---

**基本写法：维护排除项**
`gcloud container clusters update <集群> --region <区域> --add-maintenance-exclusion-name <名称> --add-maintenance-exclusion-start <开始> --add-maintenance-exclusion-end <结束>`
```bash
# 添加维护排除窗口(该期间不进行维护)
gcloud container clusters update my-gke \
  --region us-central1 \
  --add-maintenance-exclusion-name holiday \
  --add-maintenance-exclusion-start 2026-12-24T00:00:00Z \
  --add-maintenance-exclusion-end 2026-12-26T00:00:00Z
```

---

## 网络配置

**基本写法：创建私有集群**
`gcloud container clusters create <集群> --region <区域> --enable-private-nodes --master-ipv4-cidr <CIDR>`
```bash
# 创建私有节点集群
gcloud container clusters create my-gke \
  --region us-central1 \
  --enable-private-nodes \
  --master-ipv4-cidr 172.16.0.0/28 \
  --enable-ip-alias
```

---

**基本写法：启用主授权网络**
`gcloud container clusters update <集群> --region <区域> --enable-master-authorized-networks --master-authorized-networks <CIDR>`
```bash
# 仅允许指定 IP 段访问控制面
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-master-authorized-networks \
  --master-authorized-networks 203.0.113.0/24
```

---

**基本写法：启用 Ingress**
`gcloud container clusters update <集群> --region <区域> --enable-addons HttpLoadBalancing`
```bash
# 启用 HTTP(S) 负载均衡器
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-addons HttpLoadBalancing
```

---

**基本写法：启用 Network Policy**
`gcloud container clusters update <集群> --region <区域> --enable-network-policy`
```bash
# 启用网络策略(限制 Pod 间通信)
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-network-policy
```

---

## 安全与身份

**基本写法：启用 Workload Identity**
`gcloud container clusters update <集群> --region <区域> --workload-pool <项目ID>.svc.id.goog`
```bash
# 在已有集群启用 Workload Identity
gcloud container clusters update my-gke \
  --region us-central1 \
  --workload-pool my-project-123.svc.id.goog
```

---

**基本写法：创建 IAM 绑定**
`gcloud iam service-accounts add-iam-policy-binding <SA> --role roles/iam.workloadIdentityUser --member <成员>`
```bash
# 允许 K8s SA 使用 GCP SA
gcloud iam service-accounts add-iam-policy-binding \
  my-gsa@my-project-123.iam.gserviceaccount.com \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:my-project-123.svc.id.goog[default/my-ksa]"
```

---

**基本写法：为 K8s SA 添加注解**
`kubectl annotate serviceaccount <SA> iam.gke.io/gcp-service-account=<GCP SA>`
```bash
# 注解 K8s SA 关联 GCP SA
kubectl annotate serviceaccount my-ksa \
  iam.gke.io/gcp-service-account=my-gsa@my-project-123.iam.gserviceaccount.com
```

---

**基本写法：启用 Binary Authorization**
`gcloud container clusters update <集群> --region <区域> --enable-binauthz`
```bash
# 启用 Binary Authorization 强制镜像签名验证
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-binauthz
```

---

## 监控与日志

**基本写法：启用 Cloud Monitoring**
`gcloud container clusters update <集群> --region <区域> --enable-dataplane-v2 --logging=<日志类型>`
```bash
# 启用系统与工作负载监控
gcloud container clusters update my-gke \
  --region us-central1 \
  --logging=SYSTEM,WORKLOAD \
  --monitoring=SYSTEM
```

---

**基本写法：查询日志**
`gcloud logging read "resource.type=\"k8s_container\"" --limit <数量>`
```bash
# 查询 GKE 容器日志
gcloud logging read \
  'resource.type="k8s_container" AND resource.labels.cluster_name="my-gke"' \
  --limit 50 \
  --format=json
```

---

**基本写法：流式日志**
`gcloud logging tail "resource.type=\"k8s_container\""`
```bash
# 实时跟踪容器日志
gcloud logging tail \
  'resource.type="k8s_container" AND resource.labels.cluster_name="my-gke"'
```

---

**基本写法：查询指标**
`gcloud monitoring metrics list --filter <过滤>`
```bash
# 查询容器 CPU 利用率
gcloud monitoring time-series list \
  --filter 'metric.type="kubernetes.io/container/cpu/core_usage_time"' \
  --interval-start-time 2026-07-31T00:00:00Z \
  --interval-end-time 2026-07-31T01:00:00Z
```

---

## 附加组件与功能

**基本写法：启用 Cloud Run on GKE**
`gcloud container clusters update <集群> --region <区域> --enable-addons CloudRun`
```bash
# 启用 Cloud Run 附加组件
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-addons CloudRun
```

---

**基本写法：启用 Config Sync**
`gcloud container clusters update <集群> --region <区域> --enable-config-sync`
```bash
# 启用 Config Sync 用于 GitOps 配置
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-config-sync
```

---

**基本写法：启用 HPA**
`gcloud container clusters update <集群> --region <区域> --enable-horizontal-pod-autoscaling`
```bash
# 启用水平 Pod 自动伸缩
gcloud container clusters update my-gke \
  --region us-central1 \
  --enable-horizontal-pod-autoscaling
```

---

**基本写法：启用 GKE Hub**
`gcloud container hub memberships register <集群> --gke-cluster <区域>/<集群>`
```bash
# 将集群注册到 GKE Hub 用于多集群管理
gcloud container hub memberships register my-gke \
  --gke-cluster us-central1/my-gke \
  --enable-workload-identity
```

---

## 集群操作

**基本写法：停止集群**
`gcloud container clusters update <集群> --region <区域> --no-enable-autoscaling`
```bash
# 缩容到 0(等效停止)
gcloud container clusters resize my-gke \
  --region us-central1 \
  --node-pool default-pool \
  --num-nodes 0
```

---

**基本写法：删除集群**
`gcloud container clusters delete <集群> --region <区域>`
```bash
# 删除指定集群
gcloud container clusters delete my-gke \
  --region us-central1
```

---

**基本写法：配置默认区域**
`gcloud config set compute/region <区域>`
```bash
# 设置默认计算区域避免每次指定
gcloud config set compute/region us-central1
```

---

**基本写法：查看操作列表**
`gcloud container operations list --region <区域>`
```bash
# 查看集群操作历史
gcloud container operations list \
  --region us-central1 \
  --filter="status=RUNNING"
```

---

## Artifact Registry 镜像

**基本写法：创建 Artifact Registry**
`gcloud artifacts repositories create <仓库名> --repository-format docker --location <位置>`
```bash
# 创建 Docker 仓库
gcloud artifacts repositories create my-repo \
  --repository-format docker \
  --location us-central1
```

---

**基本写法：配置 Docker 认证**
`gcloud auth configure-docker <位置>-docker.pkg.dev`
```bash
# 为 Artifact Registry 配置 Docker 凭证
gcloud auth configure-docker us-central1-docker.pkg.dev
```

---

**基本写法：列出仓库镜像**
`gcloud artifacts docker images list <位置>-docker.pkg.dev/<项目>/<仓库>`
```bash
# 列出仓库中所有镜像
gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/my-project-123/my-repo
```

---

**基本写法：清理无标签镜像**
`gcloud artifacts docker images delete <镜像> --delete-tags`
```bash
# 删除无标签的镜像
gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/my-project-123/my-repo \
  --filter="-tags:*" \
  --format="get(package)" \
  | xargs -I{} gcloud artifacts docker images delete {}
```

<!-- ============ 文档分隔线：034-cloud-computing/051-GCPBigQuery.md ============ -->

## bq 工具基础

**基本写法：查看帮助**
`bq --help`
```bash
# 查看 bq 命令行工具帮助
bq --help
```

---

**基本写法：查看版本**
`bq version`
```bash
# 查看 bq 工具版本
bq version
```

---

**基本写法：设置默认项目**
`gcloud config set project <项目ID>`
```bash
# 设置 bq 操作的默认项目
gcloud config set project my-project-123
```

---

**基本写法：指定项目运行**
`bq --project_id <项目ID> query <查询>`
```bash
# 在指定项目下运行查询
bq --project_id my-project-123 query 'SELECT 1'
```

---

**基本写法：设置查询位置**
`bq --location <位置> query <查询>`
```bash
# 指定查询在 EU 区域执行
bq --location EU query 'SELECT 1'
```

---

## 数据集管理

**基本写法：创建数据集**
`bq mk --dataset --location <位置> <项目>:<数据集>`
```bash
# 创建 US 多区域数据集
bq mk --dataset --location US my-project-123:my_dataset
```

---

**基本写法：列出数据集**
`bq ls [--project_id <项目ID>]`
```bash
# 列出当前项目所有数据集
bq ls
```

---

**基本写法：查看数据集信息**
`bq show <项目>:<数据集>`
```bash
# 查看数据集详细信息
bq show my-project-123:my_dataset
```

---

**基本写法：删除数据集**
`bq rm -r -d <数据集>`
```bash
# 删除数据集及其所有表
bq rm -r -d my_dataset
```

---

**基本写法：更新数据集**
`bq update --description <描述> <数据集>`
```bash
# 更新数据集描述
bq update --description "用户分析数据集" my_dataset
```

---

## 表操作

**基本写法：创建表**
`bq mk --table <项目>:<数据集>.<表> <字段:类型>`
```bash
# 创建带 schema 的表
bq mk --table my_dataset.users \
  user_id:STRING,name:STRING,age:INTEGER,created_at:TIMESTAMP
```

---

**基本写法：列出表**
`bq ls <项目>:<数据集>`
```bash
# 列出数据集中所有表
bq ls my_dataset
```

---

**基本写法：查看表结构**
`bq show --schema <项目>:<数据集>.<表>`
```bash
# 查看表 schema
bq show --schema --format=prettyjson my_dataset.users
```

---

**基本写法：查看表详情**
`bq show <项目>:<数据集>.<表>`
```bash
# 查看表详细信息
bq show my_dataset.users
```

---

**基本写法：删除表**
`bq rm -t <项目>:<数据集>.<表>`
```bash
# 删除指定表
bq rm -t my_dataset.users
```

---

**基本写法：复制表**
`bq cp <源表> <目标表>`
```bash
# 复制表到另一数据集
bq cp my_dataset.users my_dataset.users_backup
```

---

## 数据查询

**基本写法：运行查询**
`bq query <SQL>`
```bash
# 运行标准 SQL 查询
bq query 'SELECT * FROM my_dataset.users LIMIT 10'
```

---

**基本写法：格式化输出**
`bq query --format <格式> <SQL>`
```bash
# 以 JSON 格式输出
bq query --format=prettyjson 'SELECT * FROM my_dataset.users LIMIT 10'
```

---

**基本写法：保存查询结果到表**
`bq query --destination_table <表> --use_legacy_sql=false <SQL>`
```bash
# 查询结果保存到新表
bq query \
  --destination_table my_dataset.results \
  --use_legacy_sql=false \
  'SELECT * FROM my_dataset.users WHERE age > 18'
```

---

**基本写法：追加结果到表**
`bq query --destination_table <表> --append_table <SQL>`
```bash
# 将结果追加到已有表
bq query \
  --destination_table my_dataset.results \
  --append_table \
  'SELECT * FROM my_dataset.users WHERE age > 30'
```

---

**基本写法：运行参数化查询**
`bq query --parameter=<参数> <SQL>`
```bash
# 使用命名参数查询
bq query \
  --parameter='min_age:INT64:21' \
  'SELECT * FROM my_dataset.users WHERE age >= @min_age'
```

---

## 数据加载

**基本写法：从本地 CSV 加载**
`bq load --source_format=CSV <数据集>.<表> <文件> <schema>`
```bash
# 加载本地 CSV 文件到表
bq load --source_format=CSV \
  my_dataset.users \
  users.csv \
  user_id:STRING,name:STRING,age:INTEGER
```

---

**基本写法：从 GCS 加载**
`bq load --source_format=<格式> <表> <gs://路径>`
```bash
# 从 Cloud Storage 加载 JSON 数据
bq load --source_format=NEWLINE_DELIMITED_JSON \
  my_dataset.events \
  gs://my-bucket/events/*.json \
  event_id:STRING,event_type:STRING,timestamp:TIMESTAMP
```

---

**基本写法：自动检测 schema**
`bq load --autodetect <表> <源>`
```bash
# 自动检测 CSV 文件 schema
bq load --autodetect \
  my_dataset.users \
  gs://my-bucket/users.csv
```

---

**基本写法：指定跳过行数**
`bq load --skip_leading_rows=<行数> <表> <源> <schema>`
```bash
# 跳过 CSV 首行表头
bq load --skip_leading_rows=1 \
  my_dataset.users \
  gs://my-bucket/users.csv \
  user_id:STRING,name:STRING,age:INTEGER
```

---

**基本写法：从 Datastore 备份加载**
`bq load --source_format=DATASTORE_BACKUP <表> <gs://路径>`
```bash
# 从 Datastore 备份导出加载
bq load --source_format=DATASTORE_BACKUP \
  my_dataset.entities \
  gs://my-bucket/backup/2026/07/31/entities.export
```

---

## 数据导出

**基本写法：导出为 CSV**
`bq extract <表> <gs://路径>`
```bash
# 导出表数据到 GCS 为 CSV
bq extract my_dataset.users \
  gs://my-bucket/exports/users-*.csv
```

---

**基本写法：导出为 JSON**
`bq extract --destination_format=NEWLINE_DELIMITED_JSON <表> <gs://路径>`
```bash
# 导出为 NDJSON 格式
bq extract \
  --destination_format=NEWLINE_DELIMITED_JSON \
  my_dataset.users \
  gs://my-bucket/exports/users.json
```

---

**基本写法：导出为 Avro**
`bq extract --destination_format=AVRO <表> <gs://路径>`
```bash
# 导出为 Avro 格式
bq extract \
  --destination_format=AVRO \
  --compression=SNAPPY \
  my_dataset.users \
  gs://my-bucket/exports/users-*.avro
```

---

**基本写法：压缩导出**
`bq extract --compression=GZIP <表> <gs://路径>`
```bash
# 导出 CSV 并使用 GZIP 压缩
bq extract \
  --compression=GZIP \
  my_dataset.users \
  gs://my-bucket/exports/users-*.csv.gz
```

---

## 流式插入

**基本写法：使用 insert 命令**
`bq insert <表> <JSON 数据>`
```bash
# 流式插入单条数据
bq insert my_dataset.users \
  '{"user_id":"u001","name":"Alice","age":30}'
```

---

**基本写法：批量插入**
`bq insert <表> <文件>`
```bash
# 从文件读取多行 JSON 插入
bq insert my_dataset.events events.ndjson
```

---

**基本写法：忽略未知字段**
`bq insert --ignore_unknown_values <表> <JSON>`
```bash
# 插入时忽略 schema 中没有的字段
bq insert --ignore_unknown_values \
  my_dataset.users \
  '{"user_id":"u002","name":"Bob","extra":"field"}'
```

---

**基本写法：模板插入**
`bq insert --template_suffix=<后缀> <模板表> <JSON>`
```bash
# 通过模板表自动创建分片表
bq insert --template_suffix=_20260731 \
  my_dataset.events_template \
  '{"event_id":"e001","type":"click"}'
```

---

## 视图与物化视图

**基本写法：创建视图**
`bq mk --view <SQL> --use_legacy_sql=false <数据集>.<视图>`
```bash
# 创建标准 SQL 视图
bq mk --view \
  --use_legacy_sql=false \
  my_dataset.active_users \
  'SELECT * FROM my_dataset.users WHERE status = "active"'
```

---

**基本写法：创建物化视图**
`bq mk --materialized_view <SQL> <数据集>.<视图>`
```bash
# 创建物化视图聚合统计
bq mk --materialized_view \
  my_dataset.user_stats \
  'SELECT user_id, COUNT(*) AS cnt FROM my_dataset.events GROUP BY user_id'
```

---

**基本写法：更新物化视图**
`bq query --use_legacy_sql=false 'ALTER MATERIALIZED VIEW <视图> SET OPTIONS(enable_refresh=true)'`
```bash
# 启用物化视图自动刷新
bq query --use_legacy_sql=false \
  'ALTER MATERIALIZED VIEW my_dataset.user_stats SET OPTIONS(enable_refresh=true, refresh_interval_minutes=30)'
```

---

**基本写法：删除视图**
`bq rm -v <视图>`
```bash
# 删除视图
bq rm -v my_dataset.active_users
```

---

## 分区表与聚簇表

**基本写法：创建分区表**
`bq mk --table --time_partitioning_type=DAY <表> <schema>`
```bash
# 按天创建分区表
bq mk --table \
  --time_partitioning_type=DAY \
  --time_partitioning_field=created_at \
  my_dataset.events \
  event_id:STRING,created_at:TIMESTAMP
```

---

**基本写法：创建聚簇表**
`bq mk --table --clustering_fields=<字段> <表> <schema>`
```bash
# 创建带聚簇列的表
bq mk --table \
  --clustering_fields=user_id,event_type \
  my_dataset.events \
  event_id:STRING,user_id:STRING,event_type:STRING,timestamp:TIMESTAMP
```

---

**基本写法：分区与聚簇组合**
`bq mk --table --time_partitioning_type=DAY --clustering_fields=<字段> <表> <schema>`
```bash
# 创建按天分区且按 user_id 聚簇的表
bq mk --table \
  --time_partitioning_type=DAY \
  --time_partitioning_field=timestamp \
  --clustering_fields=user_id \
  my_dataset.events \
  event_id:STRING,user_id:STRING,timestamp:TIMESTAMP
```

---

**基本写法：查询指定分区**
`bq query 'SELECT * FROM <表> WHERE <分区过滤>'`
```bash
# 仅查询 2026 年 7 月 31 日数据
bq query --use_legacy_sql=false \
  'SELECT * FROM my_dataset.events WHERE DATE(timestamp) = "2026-07-31"'
```

---

## 数据处理与转换

**基本写法：使用 BigQuery ML 训练模型**
`bq query 'CREATE MODEL <模型> OPTIONS(...) AS SELECT ...'`
```bash
# 训练逻辑回归模型
bq query --use_legacy_sql=false '
  CREATE OR REPLACE MODEL my_dataset.user_churn_model
  OPTIONS(model_type="logistic_reg", input_label_cols=["churned"]) AS
  SELECT * FROM my_dataset.user_features
'
```

---

**基本写法：使用模型预测**
`bq query 'SELECT * FROM ML.PREDICT(MODEL <模型>, ...)'`
```bash
# 使用模型预测
bq query --use_legacy_sql=false '
  SELECT * FROM ML.PREDICT(MODEL my_dataset.user_churn_model,
    (SELECT * FROM my_dataset.new_users))
'
```

---

**基本写法：执行 DML 更新**
`bq query 'UPDATE <表> SET ... WHERE ...'`
```bash
# 批量更新数据
bq query --use_legacy_sql=false '
  UPDATE my_dataset.users
  SET status = "inactive"
  WHERE last_login < TIMESTAMP("2025-01-01")
'
```

---

**基本写法：删除数据**
`bq query 'DELETE FROM <表> WHERE ...'`
```bash
# 删除满足条件的数据
bq query --use_legacy_sql=false '
  DELETE FROM my_dataset.users
  WHERE status = "deleted"
'
```

---

## 调度与作业

**基本写法：列出作业**
`bq ls -j`
```bash
# 列出最近的作业
bq ls -j -n 20
```

---

**基本写法：查看作业详情**
`bq show -j <作业ID>`
```bash
# 查看指定作业状态
bq show -j job_1234567890
```

---

**基本写法：取消作业**
`bq cancel <作业ID>`
```bash
# 取消运行中的查询作业
bq cancel job_1234567890
```

---

**基本写法：创建定时查询**
`bq query --schedule='every 24 hours' --destination_table=<表> <SQL>`
```bash
# 每天定时执行汇总查询
bq query \
  --schedule='every 24 hours' \
  --destination_table=my_dataset.daily_stats \
  --use_legacy_sql=false \
  'SELECT DATE(timestamp) AS day, COUNT(*) AS cnt FROM my_dataset.events GROUP BY day'
```

---

**基本写法：列出定时查询**
`bq ls --transfer_config`
```bash
# 列出所有定时查询配置
bq ls --transfer_config --transfer_location=us
```

---

## 权限与共享

**基本写法：添加表权限**
`bq add-iam-policy-binding <表> --role=<角色> --member=<成员>`
```bash
# 授予用户表查询权限
bq add-iam-policy-binding \
  my_dataset.users \
  --role=roles/bigquery.dataViewer \
  --member=user:alice@example.com
```

---

**基本写法：移除表权限**
`bq remove-iam-policy-binding <表> --role=<角色> --member=<成员>`
```bash
# 移除用户表权限
bq remove-iam-policy-binding \
  my_dataset.users \
  --role=roles/bigquery.dataViewer \
  --member=user:alice@example.com
```

---

**基本写法：授权数据集访问**
`bq update --source <文件> <数据集>`
```json
{
  "access": [
    {"role": "READER", "userByEmail": "alice@example.com"},
    {"role": "WRITER", "groupBy": "data-team@example.com"}
  ]
}
```

---

**基本写法：授权视图共享**
`bq update --view <SQL> <数据集>.<视图>`
```bash
# 更新视图并配置授权
bq update \
  --view 'SELECT user_id, name FROM my_dataset.users' \
  --use_legacy_sql=false \
  my_dataset.public_users
```

---

## 计费与优化

**基本写法：查询字节数预估**
`bq query --dry_run <SQL>`
```bash
# 干运行估算查询字节数
bq query --dry_run --use_legacy_sql=false \
  'SELECT * FROM my_dataset.events WHERE DATE(timestamp) = "2026-07-31"'
```

---

**基本写法：设置最大字节**
`bq query --maximum_bytes_billed=<字节> <SQL>`
```bash
# 限制查询最大字节数
bq query \
  --maximum_bytes_billed=1000000000 \
  --use_legacy_sql=false \
  'SELECT * FROM my_dataset.events'
```

---

**基本写法：查看表存储统计**
`bq show --format=prettyjson <表>`
```bash
# 查看表存储大小与统计
bq show --format=prettyjson my_dataset.events
```

---

**基本写法：设置表过期**
`bq update --expiration <秒> <表>`
```bash
# 设置表 30 天后过期
bq update --expiration 2592000 my_dataset.temp_data
```

---

## 跨云与外部数据

**基本写法：创建外部表**
`bq mk --external_table_definition=<定义> <表>`
```bash
# 创建映射到 GCS 的外部表
bq mk --external_table_definition='gs://my-bucket/data/*.csv@CSV=user_id:STRING,name:STRING' \
  my_dataset.external_users
```

---

**基本写法：查询 Cloud SQL**
`bq query 'SELECT * FROM EXTERNAL_QUERY("<连接>")'`
```bash
# 通过联邦查询 Cloud SQL
bq query --use_legacy_sql=false '
  SELECT * FROM EXTERNAL_QUERY("my-project.us.cloudsql-connection")
'
```

---

**基本写法：BigLake 表**
`bq mk --table --table_type=EXTERNAL --format=PARQUET <表> <gs://路径>`
```bash
# 创建 BigLake 表查询 GCS Parquet
bq mk --table \
  --table_type=EXTERNAL \
  --format=PARQUET \
  --source_uris=gs://my-bucket/data/*.parquet \
  my_dataset.biglake_table
```

---

**基本写法：导出到 BigQuery Studio**
`bq query --destination_table=<表> --overwrite_table <SQL>`
```bash
# 覆盖写结果到新表供 Studio 分析
bq query \
  --destination_table=my_dataset.analysis \
  --overwrite_table \
  --use_legacy_sql=false \
  'SELECT * FROM my_dataset.users WHERE age > 18'
```

<!-- ============ 文档分隔线：034-cloud-computing/052-PulumiCommands.md ============ -->

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

<!-- ============ 文档分隔线：034-cloud-computing/053-HarborRegistry.md ============ -->

## 安装与部署

**基本写法：下载 Harbor 安装包**
`curl -fsSL https://github.com/goharbor/harbor/releases/download/v<版本>/harbor-offline-installer-v<版本>.tgz -o harbor.tgz`
```bash
# 下载 Harbor 2.11 离线安装包
curl -fsSL https://github.com/goharbor/harbor/releases/download/v2.11.0/harbor-offline-installer-v2.11.0.tgz -o harbor.tgz
```

---

**基本写法：解压安装包**
`tar xzf harbor.tgz`
```bash
# 解压到当前目录
tar xzf harbor.tgz
```

---

**基本写法：复制配置模板**
`cp harbor.yml.tmpl harbor.yml`
```bash
# 复制默认配置模板
cd harbor
cp harbor.yml.tmpl harbor.yml
```

---

**基本写法：执行安装**
`sudo install.sh`
```bash
# 运行安装脚本
sudo ./install.sh
```

---

**基本写法：启用 Notary 验证**
`sudo install.sh --with-notary`
```bash
# 安装并启用镜像签名功能
sudo ./install.sh --with-notary
```

---

## 配置文件

**基本写法：HTTP 配置**
```yaml
# harbor.yml HTTP 配置
hostname: harbor.example.com
http:
  port: 80
harbor_admin_password: Harbor12345
database:
  password: root123
  max_idle_conns: 50
data_volume: /data/harbor
```

---

**基本写法：HTTPS 配置**
```yaml
# harbor.yml HTTPS 配置
hostname: harbor.example.com
http:
  port: 80
https:
  port: 443
  certificate: /data/cert/harbor.crt
  private_key: /data/cert/harbor.key
harbor_admin_password: Harbor12345
```

---

**基本写法：外部数据库配置**
```yaml
# 使用外部 PostgreSQL
external_database:
  harbor:
    host: pg.example.com
    port: 5432
    username: harbor
    password: HarborDb123
    db_name: harbor_db
    max_idle_conns: 50
```

---

**基本写法：外部 Redis 配置**
```yaml
# 使用外部 Redis
external_redis:
  host: redis.example.com
  port: 6379
  password: RedisPass123
  registry_db_index: 1
  jobservice_db_index: 2
```

---

**基本写法：邮件配置**
```yaml
# 邮件服务器配置
email_server:
  host: smtp.example.com
  port: 587
  username: sender@example.com
  password: MailPass123
  from: sender@example.com
  ssl: false
  insecure: false
```

---

## Docker 客户端登录

**基本写法：登录 Harbor**
`docker login <Harbor 地址>`
```bash
# 登录 Harbor 仓库
docker login harbor.example.com
```

---

**基本写法：使用用户名密码登录**
`docker login -u <用户名> -p <密码> <Harbor 地址>`
```bash
# 非交互式登录(避免在 CI 暴露密码用 stdin)
echo "MyPassword123" | docker login harbor.example.com -u admin --password-stdin
```

---

**基本写法：配置非安全仓库**
```json
// /etc/docker/daemon.json
{
  "insecure-registries": ["harbor.example.com:80"]
}
```

---

**基本写法：重启 Docker**
`sudo systemctl restart docker`
```bash
# 修改 daemon.json 后重启 Docker
sudo systemctl restart docker
```

---

**基本写法：退出登录**
`docker logout <Harbor 地址>`
```bash
# 移除本地凭证
docker logout harbor.example.com
```

---

## 镜像推送

**基本写法：构建镜像**
`docker build -t <镜像名>:<标签> .`
```bash
# 构建带 Harbor 地址标签的镜像
docker build -t harbor.example.com/myproject/app:v1.0 .
```

---

**基本写法：为镜像打标签**
`docker tag <源镜像> <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 为本地镜像打 Harbor 仓库标签
docker tag myapp:latest harbor.example.com/myproject/app:v1.0
```

---

**基本写法：推送镜像**
`docker push <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 推送镜像到 Harbor
docker push harbor.example.com/myproject/app:v1.0
```

---

**基本写法：推送多架构镜像**
```bash
# 创建并推送多架构 manifest
docker buildx build --platform linux/amd64,linux/arm64 \
  -t harbor.example.com/myproject/app:v1.0 \
  --push .
```

---

**基本写法：拉取镜像**
`docker pull <Harbor 地址>/<项目>/<镜像>:<标签>`
```bash
# 从 Harbor 拉取镜像
docker pull harbor.example.com/myproject/app:v1.0
```

---

## 项目与用户管理

**基本写法：创建项目**
```bash
# 通过 API 创建项目
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects \
  -d '{
    "project_name": "myproject",
    "public": false,
    "storage_limit": 53687091200
  }'
```

---

**基本写法：列出项目**
```bash
# 列出所有项目
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/projects
```

---

**基本写法：创建用户**
```bash
# 通过 API 创建用户
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/users \
  -d '{
    "username": "alice",
    "email": "alice@example.com",
    "realname": "Alice",
    "password": "AlicePass123!",
    "comment": "developer"
  }'
```

---

**基本写法：分配项目角色**
```bash
# 为用户分配项目开发者角色
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1/members \
  -d '{
    "role_id": 2,
    "member_user": {"username": "alice"}
  }'
```

---

**基本写法：删除项目**
```bash
# 删除指定项目(需先清空镜像)
curl -X DELETE -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/projects/1
```

---

## 镜像管理 API

**基本写法：列出仓库**
```bash
# 列出项目下所有镜像仓库
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories"
```

---

**基本写法：列出镜像标签**
```bash
# 列出指定镜像的所有标签
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts"
```

---

**基本写法：删除镜像**
```bash
# 删除指定标签的镜像
curl -X DELETE -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0"
```

---

**基本写法：扫描镜像**
```bash
# 触发镜像漏洞扫描
curl -X POST -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan"
```

---

**基本写法：查看扫描结果**
```bash
# 获取镜像扫描报告
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan/report"
```

---

## 漏洞扫描

**基本写法：查看扫描器**
```bash
# 查看已配置的扫描器
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/scanners
```

---

**基本写法：设置默认扫描器**
```bash
# 将 Trivy 设为默认扫描器
curl -X PUT -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/scanners/Trivy \
  -d '{"is_default": true}'
```

---

**基本写法：配置扫描策略**
```yaml
# harbor.yml 启用漏洞扫描
scan:
  enabled: true
  trivy:
    ignore_unfixed: false
    skip_update: false
    offline_scan: false
```

---

**基本写法：查看 CVE 详情**
```bash
# 获取扫描出的漏洞详情
curl -u admin:Harbor12345 \
  "https://harbor.example.com/api/v2.0/projects/myproject/repositories/app/artifacts/v1.0/scan/report" \
  | jq '.vulnerabilities[] | {id: .id, severity: .severity, package: .package}'
```

---

## 复制策略

**基本写法：创建远程仓库**
```bash
# 创建到远程 Harbor 的复制目标
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/registries \
  -d '{
    "name": "remote-harbor",
    "type": "harbor",
    "url": "https://harbor.remote.com",
    "credential": {
      "type": "basic",
      "access_key": "admin",
      "access_secret": "RemotePass123"
    }
  }'
```

---

**基本写法：创建复制策略**
```bash
# 创建推送模式复制策略
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/replication/policies \
  -d '{
    "name": "sync-to-remote",
    "src_registry": {"id": 1},
    "dest_registry": null,
    "trigger": {"type": "scheduled", "trigger_settings": {"cron": "0 0 * * * *"}},
    "filters": [{"type": "name", "value": "myproject/*"}]
  }'
```

---

**基本写法：手动触发复制**
```bash
# 手动启动一次复制
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/replication/executions \
  -d '{"policy_id": 1}'
```

---

**基本写法：查看复制状态**
```bash
# 查看复制执行历史
curl -u admin:Harbor12345 \
  https://harbor.example.com/api/v2.0/replication/executions
```

---

## 垃圾回收

**基本写法：查看 GC 配置**
`docker-compose -f /harbor/docker-compose.yml stop`
```bash
# 停止 Harbor 服务准备 GC
cd /harbor
docker-compose -f docker-compose.yml stop
```

---

**基本写法：执行 GC**
`docker run -it --name gc --rm --volumes-from registry-core vmware/harbor-registryctl:2.11.0 garbage-collect --dry-run /etc/registry/config.yml`
```bash
# 干运行查看 GC 影响
docker run -it --name gc --rm \
  --volumes-from registry-core \
  goharbor/registry-photon:v2.11.0 \
  garbage-collect --dry-run /etc/registry/config.yml
```

---

**基本写法：实际执行 GC**
`docker run -it --name gc --rm --volumes-from registry-core goharbor/registry-photon:v2.11.0 garbage-collect /etc/registry/config.yml`
```bash
# 实际执行垃圾回收(需停止 Harbor)
docker run -it --name gc --rm \
  --volumes-from registry-core \
  goharbor/registry-photon:v2.11.0 \
  garbage-collect /etc/registry/config.yml
```

---

**基本写法：定时 GC 任务**
```bash
# 通过 API 创建定时 GC 任务
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/system/gc/schedule \
  -d '{
    "schedule": {"type": "Weekly", "cron": "0 0 0 * * 0", "weekday": 0},
    "parameters": {"delete_untagged": true}
  }'
```

---

## 备份与升级

**基本写法：备份数据库**
`docker exec -it harbor-db pg_dump -U postgres registry > backup.sql`
```bash
# 备份 Harbor 数据库
docker exec -it harbor-db pg_dump -U postgres registry > harbor-$(date +%Y%m%d).sql
```

---

**基本写法：备份存储卷**
`tar czf harbor-data-<日期>.tgz /data/harbor`
```bash
# 备份整个 Harbor 数据卷
tar czf harbor-data-20260731.tgz /data/harbor
```

---

**基本写法：恢复数据库**
`docker exec -i harbor-db psql -U postgres registry < backup.sql`
```bash
# 从备份恢复数据库
docker exec -i harbor-db psql -U postgres registry < harbor-20260731.sql
```

---

**基本写法：升级 Harbor**
`sudo ./install.sh`
```bash
# 下载新版本后执行安装脚本升级
cd harbor
sudo ./install.sh
```

---

**基本写法：迁移配置文件**
`sudo ./migrate --input <旧配置> --output <新配置>`
```bash
# 升级时迁移 harbor.cfg 到 harbor.yml
sudo ./migrate --input harbor.cfg --output harbor.yml
```

---

## Helm 部署方式

**基本写法：添加 Harbor Helm 仓库**
`helm repo add harbor https://helm.goharbor.io`
```bash
# 添加 Harbor 官方 Helm 仓库
helm repo add harbor https://helm.goharbor.io
helm repo update
```

---

**基本写法：配置 values.yaml**
```yaml
# values.yaml 关键配置
expose:
  type: ingress
  tls:
    enabled: true
    certSource: secret
    secret:
      secretName: harbor-tls
      notarySecretName: notary-tls
externalURL: https://harbor.example.com
harborAdminPassword: "Harbor12345"
persistence:
  persistentVolumeClaim:
    registry:
      size: 100Gi
    database:
      size: 10Gi
```

---

**基本写法：通过 Helm 安装 Harbor**
`helm install harbor harbor/harbor -f values.yaml -n harbor --create-namespace`
```bash
# 在 harbor 命名空间安装 Harbor
helm install harbor harbor/harbor \
  -f values.yaml \
  -n harbor \
  --create-namespace
```

---

**基本写法：升级 Harbor**
`helm upgrade harbor harbor/harbor -f values.yaml -n harbor`
```bash
# 升级 Harbor 到新版本
helm repo update
helm upgrade harbor harbor/harbor \
  -f values.yaml \
  -n harbor
```

---

**基本写法：卸载 Harbor**
`helm uninstall harbor -n harbor`
```bash
# 卸载 Harbor(不删除 PVC)
helm uninstall harbor -n harbor
```

---

## 高级配置

**基本写法：配置 OIDC 登录**
```yaml
# harbor.yml 配置 OIDC
oidc:
  name: "Google"
  endpoint: "https://accounts.google.com"
  client_id: "your-client-id"
  client_secret: "your-client-secret"
  scope: "openid,profile,email"
  verify_cert: true
```

---

**基本写法：配置 LDAP**
```yaml
# harbor.yml 配置 LDAP 认证
ldap:
  url: ldaps://ldap.example.com
  base_dn: dc=example,dc=com
  filter: "(objectClass=person)"
  uid: uid
  scope: 2
  timeout: 5
```

---

**基本写法：配置 Webhook**
```bash
# 通过 API 创建 Webhook
curl -X POST -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1/webhook/policies \
  -d '{
    "name": "image-push-notify",
    "enabled": true,
    "targets": [{"type": "http", "address": "https://app.example.com/webhook"}],
    "event_types": ["PUSH_ARTIFACT"],
    "creator": "admin"
  }'
```

---

**基本写法：配置配额**
```bash
# 设置项目存储配额
curl -X PUT -u admin:Harbor12345 \
  -H "Content-Type: application/json" \
  https://harbor.example.com/api/v2.0/projects/1 \
  -d '{"metadata": {"storage_limit": "53687091200"}}'
```

<!-- ============ 文档分隔线：034-cloud-computing/054-CloudInitCommands.md ============ -->

## cloud-init 基础

**基本写法：查看版本**
`cloud-init --version`
```bash
# 查看 cloud-init 版本
cloud-init --version
```

---

**基本写法：查看 cloud-init 状态**
`cloud-init status`
```bash
# 查看实例初始化状态
cloud-init status
```

---

**基本写法：等待完成**
`cloud-init status --wait`
```bash
# 阻塞等待 cloud-init 完成
cloud-init status --wait
```

---

**基本写法：查看详细状态**
`cloud-init status --long`
```bash
# 显示详细 cloud-init 状态与错误信息
cloud-init status --long
```

---

**基本写法：查看 cloud-init 文档**
`cloud-init --help`
```bash
# 查看所有可用子命令
cloud-init --help
```

---

## 用户数据配置

**基本写法：使用 cloud-config 格式**
```yaml
# user-data.yaml 用户数据脚本
#cloud-config
hostname: web-server
manage_etc_hosts: true
```

---

**基本写法：使用 shell 脚本**
```bash
#!/bin/bash
# user-data.sh 通过 shell 脚本初始化
set -e
apt-get update
apt-get install -y nginx
systemctl enable nginx
systemctl start nginx
```

---

**基本写法：包含文件**
```yaml
# 写入文件到实例
#cloud-config
write_files:
  - path: /etc/myapp/config.yaml
    content: |
      server:
        port: 8080
        host: 0.0.0.0
    owner: root:root
    permissions: '0644'
```

---

**基本写法：从 URL 下载文件**
```yaml
# 从远程 URL 下载配置文件
#cloud-config
write_files:
  - path: /etc/nginx/conf.d/default.conf
    encoding: b64
    content: <Base64 编码内容>
    defer: true
```

---

**基本写法：追加到文件**
```yaml
# 追加内容到已有文件
#cloud-config
write_files:
  - path: /etc/hosts
    content: |
      10.0.0.5  db.internal
      10.0.0.6  cache.internal
    append: true
```

---

## 软件包管理

**基本写法：更新软件包**
```yaml
#cloud-config
package_update: true
package_upgrade: true
package_reboot_if_required: true
```

---

**基本写法：安装软件包**
```yaml
#cloud-config
packages:
  - nginx
  - git
  - htop
  - curl
package_update: true
```

---

**基本写法：指定软件源**
```yaml
#cloud-config
apt:
  sources:
    docker.list:
      source: "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
      keyid: 9DC858229FC7DD38854AE2D88D81803C0EBFCD88
```

---

**基本写法：安装指定版本**
```yaml
#cloud-config
packages:
  - [nginx, 1.18.0-0ubuntu1]
package_update: true
```

---

**基本写法：安装 Snap 包**
```yaml
#cloud-config
snap:
  commands:
    - snap install --classic code
    - snap install go --channel 1.22/stable --classic
```

---

## 用户与组管理

**基本写法：创建用户**
```yaml
#cloud-config
users:
  - name: deploy
    sudo: ALL=(ALL) NOPASSWD:ALL
    groups: sudo, docker
    shell: /bin/bash
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2E... user@example.com
```

---

**基本写法：默认用户配置 SSH key**
```yaml
#cloud-config
ssh_authorized_keys:
  - ssh-rsa AAAAB3NzaC1yc2E... admin@example.com
  - ssh-ed25519 AAAAC3NzaC1lZDI1... deploy@example.com
```

---

**基本写法：禁用密码登录**
```yaml
#cloud-config
ssh_pwauth: false
disable_root: true
```

---

**基本写法：设置用户密码**
```yaml
#cloud-config
chpasswd:
  list: |
    deploy:MyStrongPass123!
  expire: false
```

---

**基本写法：移除默认用户**
```yaml
#cloud-config
users:
  - default
  - name: myuser
    groups: sudo
    shell: /bin/bash
    sudo: ALL=(ALL) NOPASSWD:ALL
    lock_passwd: false
```

---

## 命令执行

**基本写法：运行命令**
```yaml
#cloud-config
runcmd:
  - mkdir -p /data/app
  - chown -R deploy:deploy /data
  - systemctl restart nginx
```

---

**基本写法：执行多行脚本**
```yaml
#cloud-config
runcmd:
  - |
    #!/bin/bash
    set -e
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    systemctl enable docker
    systemctl start docker
```

---

**基本写法：bootcmd 启动命令**
```yaml
#cloud-config
bootcmd:
  - echo "Boot at $(date)" >> /var/log/boot.log
  - mkdir -p /mnt/data
```

---

**基本写法：使用模块顺序**
```yaml
#cloud-config
cloud_final_modules:
  - package-update-upgrade-install
  - puppet
  - chef
  - mcollective
  - salt-minion
  - reset_rmc
  - refresh_rmc_and_interface
  - rightscale_userdata
  - scripts-vendor
  - scripts-per-once
  - scripts-per-boot
  - scripts-per-instance
  - scripts-user
  - ssh-authkey-fingerprints
  - keys-to-console
  - install-hotplug
  - phone-home
  - final-message
  - power-state-change
```

---

## 磁盘与挂载

**基本写法：挂载磁盘**
```yaml
#cloud-config
mounts:
  - [ /dev/vdb, /data, ext4, "defaults,noatime", "0", "2" ]
  - [ /dev/vdc, /backup, xfs, "defaults", "0", "0" ]
```

---

**基本写法：格式化磁盘**
```yaml
#cloud-config
disk_setup:
  /dev/vdb:
    table_type: gpt
    layout: true
    overwrite: false
fs_setup:
  - device: /dev/vdb
    filesystem: ext4
    label: data
```

---

**基本写法：创建 RAID**
```yaml
#cloud-config
disk_setup:
  md0:
    table_type: mbr
    layout: [ /dev/vdb, /dev/vdc ]
    overwrite: true
raidd:
  md0:
    devices:
      - /dev/vdb
      - /dev/vdc
    level: 1
    metadata: 1.2
    name: md0
```

---

**基本写法：调整 LVM**
```yaml
#cloud-config
lvm:
  lvmdisk:
    type: lvm
    devices:
      - /dev/vdb
  lvms:
    - name: data
      vg: lvmdisk
      size: 100G
```

---

**基本写法：fstab 配置**
```yaml
#cloud-config
mounts:
  - [ /dev/vdb, /data, ext4, "defaults,noatime,nofail", "0", "2" ]
  - [ /dev/vdc, /logs, xfs, "defaults,nofail", "0", "0" ]
  - [ tmpfs, /tmp, tmpfs, "defaults,size=2G", "0", "0" ]
```

---

## 网络配置

**基本写法：配置静态 IP**
```yaml
#cloud-config
version: 2
ethernets:
  eth0:
    addresses:
      - 10.0.1.100/24
    gateway4: 10.0.1.1
    nameservers:
      addresses: [8.8.8.8, 1.1.1.1]
    routes:
      - to: 10.0.0.0/16
        via: 10.0.1.1
```

---

**基本写法：配置 DHCP**
```yaml
#cloud-config
version: 2
ethernets:
  eth0:
    dhcp4: true
    dhcp6: true
```

---

**基本写法：多网卡配置**
```yaml
#cloud-config
version: 2
ethernets:
  eth0:
    addresses: [10.0.1.100/24]
    gateway4: 10.0.1.1
  eth1:
    addresses: [192.168.1.50/24]
    routes:
      - to: 192.168.0.0/16
        via: 192.168.1.1
```

---

**基本写法：配置 Bonding**
```yaml
#cloud-config
version: 2
bonds:
  bond0:
    interfaces: [eth0, eth1]
    parameters:
      mode: 802.3ad
      lacp-rate: fast
      transmit-hash-policy: layer3+4
    addresses: [10.0.1.100/24]
    gateway4: 10.0.1.1
```

---

**基本写法：配置 VLAN**
```yaml
#cloud-config
version: 2
vlans:
  vlan100:
    id: 100
    link: eth0
    addresses: [10.100.0.10/24]
  vlan200:
    id: 200
    link: eth0
    addresses: [10.200.0.10/24]
```

---

## 服务管理

**基本写法：启用服务**
```yaml
#cloud-config
runcmd:
  - systemctl enable nginx
  - systemctl enable docker
  - systemctl enable redis
```

---

**基本写法：自定义服务**
```yaml
#cloud-config
write_files:
  - path: /etc/systemd/system/myapp.service
    content: |
      [Unit]
      Description=My Application
      After=network.target
      [Service]
      Type=simple
      User=deploy
      ExecStart=/opt/myapp/app
      Restart=always
      [Install]
      WantedBy=multi-user.target
runcmd:
  - systemctl daemon-reload
  - systemctl enable myapp
  - systemctl start myapp
```

---

**基本写法：启动时延迟启动**
```yaml
#cloud-config
bootcmd:
  - sleep 30 && systemctl restart myapp &
```

---

## 模块与日志

**基本写法：查看日志**
`sudo cat /var/log/cloud-init.log`
```bash
# 查看 cloud-init 详细日志
sudo cat /var/log/cloud-init.log | less
```

---

**基本写法：查看输出日志**
`sudo cat /var/log/cloud-init-output.log`
```bash
# 查看 cloud-init 执行输出
sudo tail -n 100 /var/log/cloud-init-output.log
```

---

**基本写法：清理 cloud-init 状态**
`sudo cloud-init clean`
```bash
# 清理 cloud-init 状态便于重新运行
sudo cloud-init clean
```

---

**基本写法：清理并重启**
`sudo cloud-init clean --logs --reboot`
```bash
# 清理日志并重启重新初始化
sudo cloud-init clean --logs --reboot
```

---

**基本写法：单模块运行**
`sudo cloud-init modules --mode=<模式> [--name=<模块>]`
```bash
# 单独运行指定模块
sudo cloud-init modules --mode=final --name=final-message
```

---

## 调试与分析

**基本写法：查询实例元数据**
`curl http://169.254.169.254/latest/meta-data/`
```bash
# 查询 AWS EC2 元数据
curl -s http://169.254.169.254/latest/meta-data/instance-id
```

---

**基本写法：查询用户数据**
`curl http://169.254.169.254/latest/user-data`
```bash
# 查看实例启动时传入的用户数据
curl -s http://169.254.169.254/latest/user-data
```

---

**基本写法：分析 cloud-init 阶段**
`cloud-init analyze show`
```bash
# 显示各阶段耗时
cloud-init analyze show -i /var/log/cloud-init.log
```

---

**基本写法：生成时间报告**
`cloud-init analyze dump`
```bash
# 输出时间分析 JSON
cloud-init analyze dump -i /var/log/cloud-init.log > timing.json
```

---

**基本写法：验证 user-data**
`cloud-init schema --config-file <文件>`
```bash
# 验证 user-data 配置正确性
cloud-init schema --config-file user-data.yaml
```

---

## 云平台集成

**基本写法：AWS EC2 启动模板**
```bash
# 通过 AWS CLI 创建带 user-data 的启动模板
aws ec2 create-launch-template \
  --launch-template-name my-template \
  --launch-template-data '{
    "ImageId": "ami-0c55b159cbfafe1f0",
    "InstanceType": "t3.micro",
    "UserData": "'"$(base64 -w 0 user-data.sh)"'"
  }'
```

---

**基本写法：Azure VM 自定义数据**
```bash
# 通过 Azure CLI 创建 VM 时传入 cloud-init
az vm create \
  --name my-vm \
  --resource-group my-rg \
  --image Ubuntu2204 \
  --custom-data @cloud-init.yaml \
  --admin-username azureuser
```

---

**基本写法：GCP GCE 启动脚本**
```bash
# 通过 gcloud 创建 GCE 实例并传入 cloud-init
gcloud compute instances create my-instance \
  --zone=us-central1-a \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --metadata-from-file user-data=cloud-init.yaml
```

---

**基本写法：OpenStack 创建实例**
```bash
# OpenStack 使用 cloud-init
openstack server create \
  --flavor m1.medium \
  --image ubuntu-22.04 \
  --user-data cloud-init.yaml \
  my-instance
```

---

**基本写法：Vagrant 集成**
```ruby
# Vagrantfile 使用 cloud-init
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
  end
  config.vm.provision "file", source: "./cloud-init.yaml", destination: "/tmp/cloud-init.yaml"
  config.vm.provision "shell", inline: "cloud-init --file /tmp/cloud-init.yaml init"
end
```

---

## 高级应用

**基本写法：Power State 控制**
```yaml
#cloud-config
power_state:
  mode: reboot
  message: "Rebooting after cloud-init"
  timeout: 30
  condition: True
```

---

**基本写法：Phone Home 通知**
```yaml
#cloud-config
phone_home:
  url: http://config.example.com/register
  post: [ instance_id, hostname, fqdn ]
  tries: 10
```

---

**基本写法：设置时区**
```yaml
#cloud-config
timezone: Asia/Shanghai
locale: zh_CN.UTF-8
```

---

**基本写法：NTP 配置**
```yaml
#cloud-config
ntp:
  enabled: true
  ntp_client: chrony
  servers:
    - ntp.aliyun.com
    - cn.pool.ntp.org
  pools:
    - 0.cn.pool.ntp.org
```

---

**基本写法：指定数据源**
```yaml
#cloud-config
datasource_list:
  - Ec2
  - Azure
  - GCE
  - OpenStack
  - NoCloud
  - ConfigDrive
datasource:
  Ec2:
    timeout: 30
    max_wait: 120
```

<!-- ============ 文档分隔线：034-cloud-computing/055-AWSCloudFront.md ============ -->

## 分配创建

**基本写法：创建分配最小配置**
`aws cloudfront create-distribution --distribution-config <JSON>`
```bash
# 创建最小可用的 CloudFront 分配
aws cloudfront create-distribution --distribution-config '{
  "CallerReference": "my-distribution-001",
  "Comment": "My CDN distribution",
  "Enabled": true,
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "my-origin",
      "DomainName": "my-bucket.s3.amazonaws.com",
      "S3OriginConfig": {"OriginAccessIdentity": ""}
    }]
  },
  "DefaultCacheBehavior": {
    "TargetOriginId": "my-origin",
    "ViewerProtocolPolicy": "redirect-to-https",
    "TrustedSigners": {"Enabled": false, "Quantity": 0},
    "ForwardedValues": {"QueryString": false, "Cookies": {"Forward": "none"}, "Headers": {"Quantity": 0}, "QueryStringCacheKeys": {"Quantity": 0}},
    "MinTTL": 0,
    "DefaultTTL": 3600,
    "MaxTTL": 86400
  }
}'
```

---

**基本写法：使用文件配置创建**
`aws cloudfront create-distribution --distribution-config file://<文件>`
```bash
# 通过 JSON 文件创建分配
aws cloudfront create-distribution --distribution-config file://distribution.json
```

---

**基本写法：列出分配**
`aws cloudfront list-distributions`
```bash
# 列出账户下所有分配
aws cloudfront list-distributions
```

---

**基本写法：查看分配详情**
`aws cloudfront get-distribution --id <分配ID>`
```bash
# 查看指定分配详情
aws cloudfront get-distribution --id E1A2B3C4D5E6F7
```

---

**基本写法：删除分配**
`aws cloudfront delete-distribution --id <分配ID> --if-match <ETag>`
```bash
# 删除指定分配(必须先禁用)
aws cloudfront delete-distribution --id E1A2B3C4D5E6F7 --if-match E2QWERTYUIOP
```

---

## 分配配置

**基本写法：禁用分配**
`aws cloudfront update-distribution --distribution-config <JSON> --id <分配ID> --if-match <ETag>`
```bash
# 设置 Enabled 为 false 禁用分配
aws cloudfront update-distribution \
  --distribution-config file://disabled-config.json \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：启用分配**
`aws cloudfront update-distribution --id <分配ID> --if-match <ETag>`
```bash
# 修改配置启用已禁用的分配
aws cloudfront update-distribution \
  --distribution-config file://enabled-config.json \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：更新缓存行为**
```json
{
  "DefaultCacheBehavior": {
    "TargetOriginId": "my-origin",
    "ViewerProtocolPolicy": "https-only",
    "TrustedSigners": {"Enabled": false, "Quantity": 0},
    "ForwardedValues": {
      "QueryString": true,
      "Cookies": {"Forward": "all"},
      "Headers": {"Quantity": 2, "Items": ["Origin", "Access-Control-Request-Method"]},
      "QueryStringCacheKeys": {"Quantity": 0}
    },
    "MinTTL": 0,
    "DefaultTTL": 300,
    "MaxTTL": 3600,
    "AllowedMethods": {"Quantity": 7, "Items": ["GET", "HEAD", "OPTIONS", "PUT", "POST", "PATCH", "DELETE"]}
  }
}
```

---

**基本写法：配置自定义错误页面**
```json
{
  "CustomErrorResponses": {
    "Quantity": 1,
    "Items": [{
      "ErrorCode": 404,
      "ResponsePagePath": "/404.html",
      "ResponseCode": "404",
      "ErrorCachingMinTTL": 300
    }]
  }
}
```

---

**基本写法：配置地理限制**
`aws cloudfront update-distribution --distribution-config <JSON> --id <分配ID>`
```json
{
  "Restrictions": {
    "GeoRestriction": {
      "RestrictionType": "whitelist",
      "Quantity": 2,
      "Items": ["CN", "US"]
    }
  }
}
```

---

## 源站配置

**基本写法：S3 源配置**
```json
{
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "s3-origin",
      "DomainName": "my-bucket.s3.amazonaws.com",
      "S3OriginConfig": {
        "OriginAccessIdentity": "origin-access-identity/cloudfront/E1A2B3C4D5E6F7"
      }
    }]
  }
}
```

---

**基本写法：自定义源配置**
```json
{
  "Origins": {
    "Quantity": 1,
    "Items": [{
      "Id": "custom-origin",
      "DomainName": "www.example.com",
      "CustomOriginConfig": {
        "HTTPPort": 80,
        "HTTPSPort": 443,
        "OriginProtocolPolicy": "https-only",
        "OriginSslProtocols": {"Quantity": 2, "Items": ["TLSv1.2", "TLSv1.3"]}
      }
    }]
  }
}
```

---

**基本写法：创建源访问身份**
`aws cloudfront create-cloud-front-origin-access-identity --cloud-front-origin-access-identity-config <JSON>`
```bash
# 创建 OAI 用于 S3 源访问控制
aws cloudfront create-cloud-front-origin-access-identity \
  --cloud-front-origin-access-identity-config \
  '{"CallerReference":"my-oai","Comment":"OAI for my-bucket"}'
```

---

**基本写法：配置源组故障转移**
```json
{
  "OriginGroups": {
    "Quantity": 1,
    "Items": [{
      "Id": "my-origin-group",
      "Members": {
        "Quantity": 2,
        "Items": [
          {"OriginId": "primary-origin"},
          {"OriginId": "secondary-origin"}
        ]
      },
      "FailoverCriteria": {
        "StatusCodes": {"Quantity": 3, "Items": [500, 502, 503]}
      }
    }]
  }
}
```

---

**基本写法：源路径模式路由**
```json
{
  "CacheBehaviors": {
    "Quantity": 1,
    "Items": [{
      "PathPattern": "/images/*",
      "TargetOriginId": "images-origin",
      "ViewerProtocolPolicy": "redirect-to-https",
      "TrustedSigners": {"Enabled": false, "Quantity": 0},
      "ForwardedValues": {"QueryString": false, "Cookies": {"Forward": "none"}, "Headers": {"Quantity": 0}, "QueryStringCacheKeys": {"Quantity": 0}},
      "MinTTL": 0
    }]
  }
}
```

---

## 失效与缓存

**基本写法：创建失效**
`aws cloudfront create-invalidation --distribution-id <分配ID> --paths <路径>`
```bash
# 失效指定路径的缓存
aws cloudfront create-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --paths "/index.html" "/images/*"
```

---

**基本写法：失效所有文件**
`aws cloudfront create-invalidation --distribution-id <分配ID> --paths "/*"`
```bash
# 失效整个分配的缓存
aws cloudfront create-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --paths "/*"
```

---

**基本写法：查看失效状态**
`aws cloudfront get-invalidation --distribution-id <分配ID> --id <失效ID>`
```bash
# 查询失效操作进度
aws cloudfront get-invalidation \
  --distribution-id E1A2B3C4D5E6F7 \
  --id I1A2B3C4D5E6F7
```

---

**基本写法：列出失效**
`aws cloudfront list-invalidations --distribution-id <分配ID>`
```bash
# 列出最近的失效记录
aws cloudfront list-invalidations \
  --distribution-id E1A2B3C4D5E6F7
```

---

**基本写法：配置缓存策略**
`aws cloudfront create-cache-policy --cache-policy-config <JSON>`
```bash
# 创建自定义缓存策略
aws cloudfront create-cache-policy --cache-policy-config '{
  "Name": "my-cache-policy",
  "Comment": "My custom cache policy",
  "DefaultTTL": 3600,
  "MaxTTL": 86400,
  "MinTTL": 0,
  "ParametersInCacheKeyAndForwardedToOrigin": {
    "EnableAcceptEncodingGzip": true,
    "EnableAcceptEncodingBrotli": true,
    "HeadersConfig": {"HeaderBehavior": "none"},
    "CookiesConfig": {"CookieBehavior": "none"},
    "QueryStringsConfig": {"QueryStringBehavior": "none"}
  }
}'
```

---

## 源访问控制

**基本写法：创建源访问控制**
`aws cloudfront create-origin-access-control --origin-access-control-config <JSON>`
```bash
# 创建 OAC(推荐替代 OAI)
aws cloudfront create-origin-access-control --origin-access-control-config '{
  "Name": "my-oac",
  "Description": "OAC for S3 origin",
  "SigningProtocol": "sigv4",
  "SigningBehavior": "always",
  "OriginAccessControlOriginType": "s3"
}'
```

---

**基本写法：列出源访问控制**
`aws cloudfront list-origin-access-controls`
```bash
# 列出所有 OAC
aws cloudfront list-origin-access-controls
```

---

**基本写法：删除源访问控制**
`aws cloudfront delete-origin-access-control --id <ID> --if-match <ETag>`
```bash
# 删除指定 OAC
aws cloudfront delete-origin-access-control \
  --id E1A2B3C4D5E6F7 \
  --if-match E2QWERTYUIOP
```

---

**基本写法：S3 桶策略授权 CloudFront**
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {
      "Service": "cloudfront.amazonaws.com"
    },
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::my-bucket/*",
    "Condition": {
      "StringEquals": {
        "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7"
      }
    }
  }]
}
```

---

## TLS/SSL 证书

**基本写法：配置 SSL 证书**
```json
{
  "ViewerCertificate": {
    "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi",
    "SSLSupportMethod": "sni-only",
    "MinimumProtocolVersion": "TLSv1.2_2021",
    "Certificate": "arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi",
    "CertificateSource": "acm"
  }
}
```

---

**基本写法：ACM 申请证书**
`aws acm request-certificate --domain-name <域名> --validation-method DNS`
```bash
# 在 us-east-1 区域申请证书(CloudFront 必需)
aws acm request-certificate \
  --domain-name "*.example.com" \
  --validation-method DNS \
  --region us-east-1
```

---

**基本写法：查看证书**
`aws acm describe-certificate --certificate-arn <ARN>`
```bash
# 查看证书状态与验证信息
aws acm describe-certificate \
  --certificate-arn arn:aws:acm:us-east-1:123456789012:certificate/abc-def-ghi \
  --region us-east-1
```

---

**基本写法：配置备用域名**
```json
{
  "Aliases": {
    "Quantity": 2,
    "Items": ["www.example.com", "cdn.example.com"]
  }
}
```

---

**基本写法：配置安全策略**
```json
{
  "ViewerCertificate": {
    "MinimumProtocolVersion": "TLSv1.2_2021",
    "SSLSupportMethod": "sni-only"
  }
}
```

---

## 函数与 Lambda@Edge

**基本写法：创建 CloudFront 函数**
`aws cloudfront create-function --name <函数名> --function-code <代码> --function-config <配置>`
```bash
# 创建 CloudFront 函数
aws cloudfront create-function \
  --name my-function \
  --function-code fileb://function.js \
  --function-config '{"Comment":"My function","Runtime":"cloudfront-js-2.0"}'
```

---

**基本写法：发布函数**
`aws cloudfront publish-function --name <函数名> --if-match <ETag>`
```bash
# 发布函数使其可关联到分配
aws cloudfront publish-function \
  --name my-function \
  --if-match ETVERTYUIOPASDF
```

---

**基本写法：测试函数**
`aws cloudfront test-function --name <函数名> --if-match <ETag> --event-object <事件>`
```bash
# 测试函数处理指定事件
aws cloudfront test-function \
  --name my-function \
  --if-match ETVERTYUIOPASDF \
  --event-object fileb://event.json
```

---

**基本写法：关联函数到分配**
```json
{
  "DefaultCacheBehavior": {
    "FunctionAssociations": {
      "Quantity": 1,
      "Items": [{
        "FunctionARN": "arn:aws:cloudfront::123456789012:function/my-function",
        "EventType": "viewer-request"
      }]
    }
  }
}
```

---

**基本写法：列出函数**
`aws cloudfront list-functions`
```bash
# 列出所有 CloudFront 函数
aws cloudfront list-functions
```

---

## 实时日志与监控

**基本写法：创建实时日志配置**
`aws cloudfront create-realtime-log-config --end-points <端点> --fields <字段> --name <名称> --sampling-rate <比率>`
```bash
# 创建实时日志推送到 Kinesis
aws cloudfront create-realtime-log-config \
  --end-points '[{"StreamType":"Kinesis","Endpoint":{"Stream":{"Arn":"arn:aws:kinesis:us-east-1:123456789012:stream/my-stream","RoleArn":"arn:aws:iam::123456789012:role/cf-realtime"}}}]' \
  --fields '["timestamp","c-ip","time-to-first-byte","sc-status"]' \
  --name my-realtime-log \
  --sampling-rate 100
```

---

**基本写法：查看实时日志配置**
`aws cloudfront get-realtime-log-config --name <名称>`
```bash
# 查看指定实时日志配置
aws cloudfront get-realtime-log-config --name my-realtime-log
```

---

**基本写法：列出实时日志配置**
`aws cloudfront list-realtime-log-configs`
```bash
# 列出所有实时日志配置
aws cloudfront list-realtime-log-configs
```

---

**基本写法：删除实时日志配置**
`aws cloudfront delete-realtime-log-config --name <名称>`
```bash
# 删除指定实时日志配置
aws cloudfront delete-realtime-log-config --name my-realtime-log
```

---

**基本写法：监控分配指标**
`aws cloudwatch get-metric-statistics --namespace AWS/CloudFront --metric-name Requests`
```bash
# 查看 CloudFront 请求量指标
aws cloudwatch get-metric-statistics \
  --namespace AWS/CloudFront \
  --metric-name Requests \
  --dimensions Name=DistributionId,Value=E1A2B3C4D5E6F7 \
  --start-time 2026-07-31T00:00:00Z \
  --end-time 2026-07-31T01:00:00Z \
  --period 300 \
  --statistics Sum
```

---

## 标签管理

**基本写法：添加标签**
`aws cloudfront tag-resource --resource <ARN> --tags <标签>`
```bash
# 为分配添加标签
aws cloudfront tag-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7 \
  --tags 'Items=[{Key=Environment,Value=Production},{Key=Team,Value=DevOps}]'
```

---

**基本写法：查看标签**
`aws cloudfront list-tags-for-resource --resource <ARN>`
```bash
# 查看分配的所有标签
aws cloudfront list-tags-for-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7
```

---

**基本写法：移除标签**
`aws cloudfront untag-resource --resource <ARN> --tag-keys <键列表>`
```bash
# 移除指定标签
aws cloudfront untag-resource \
  --resource arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7 \
  --tag-keys 'Items=[Environment]'
```

---

## 复制与迁移

**基本写法：复制分配配置**
```bash
# 通过脚本复制分配到新分配
ETAG=$(aws cloudfront get-distribution --id E1A2B3C4D5E6F7 --query 'ETag' --output text)
aws cloudfront get-distribution-config --id E1A2B3C4D5E6F7 --query 'DistributionConfig' > copy-config.json
# 修改 CallerReference 后使用 create-distribution 创建
```

---

**基本写法：跨账户迁移**
```bash
# 导出当前分配配置
aws cloudfront get-distribution-config --id E1A2B3C4D5E6F7 > export.json
# 在目标账户创建新分配
aws cloudfront create-distribution --distribution-config file://export.json --profile target-account
```

---

**基本写法：列出标签为某值的分配**
```bash
# 查询特定环境的所有分配
aws resourcegroupstaggingapi get-resources \
  --tag-filters Key=Environment,Values=Production \
  --resource-type-filters cloudfront:distribution
```

---

**基本写法：查看分配标签**
```bash
# 列出分配的所有标签
for dist in $(aws cloudfront list-distributions --query 'DistributionList.Items[].Id' --output text); do
  echo "Distribution: $dist"
  aws cloudfront list-tags-for-resource \
    --resource arn:aws:cloudfront::123456789012:distribution/$dist
done
```
