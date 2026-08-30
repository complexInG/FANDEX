---
order: 10
title: message-queue 模块文档合集
module: 'message-queue'
category: 云与基础设施
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-29'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：054-message-queue/001-MessageQueueOverview.md ============ -->

## 0. 一句话理解

> 消息队列（MQ）就是"生产者把消息放进信箱，消费者有空再取"：它让系统之间解耦、削峰、异步，是分布式系统的标配中间件。

## 1. 消息队列解决什么问题

### 1.1 解耦

下单后要通知库存、积分、短信三个系统。直接调用接口，每加一个系统就要改代码；改成"下单消息发到队列"，新系统自己订阅即可。

### 1.2 削峰

秒杀瞬间 10 万请求打到数据库会挂。先把请求写进队列，消费端按数据库能承受的速度慢慢处理——"排队打饭"而不是"一起挤窗口"。

### 1.3 异步

发邮件、生成报表等耗时操作从请求链路里挪到后台异步执行，接口响应从 3 秒降到 100 毫秒。

## 2. 核心概念

| 概念 | 说明 | 生活类比 |
| --- | --- | --- |
| Producer 生产者 | 发消息的一方 | 寄信人 |
| Consumer 消费者 | 收消息处理的一方 | 收信人 |
| Broker 代理 | 消息暂存与转发的服务器 | 邮局 |
| Topic / Queue | 消息的分类容器 | 信箱 |
| 消费组 | 一组消费者分担消息 | 多个邮递员分工 |

## 3. 三种投递语义

| 语义 | 含义 | 代价 |
| --- | --- | --- |
| At-most-once 至多一次 | 消息可能丢，但绝不重复 | 最低 |
| At-least-once 至少一次 | 不丢，但可能重复 | 需消费端幂等 |
| Exactly-once 精确一次 | 不丢不重 | 最高，通常配合事务/幂等实现 |

企业默认选择 **At-least-once + 消费端幂等**：既不丢消息，又用"去重表/唯一键"把重复消费变成无害操作。

## 4. 主流中间件对比

| 维度 | Kafka | RabbitMQ | Pulsar |
| --- | --- | --- | --- |
| 定位 | 分布式事件流平台 | 传统消息代理 | 云原生流平台 |
| 模型 | Topic + 分区 | Exchange + Queue | Topic + 分区 |
| 顺序保证 | 分区内有序 | 单队列有序 | 分区内有序 |
| 吞吐 | 极高 | 中 | 高 |
| 延迟 | 毫秒级 | 微秒级 | 毫秒级 |
| 重放 | 消息可保留重读 | 消费后删除 | 可保留重读 |
| 典型场景 | 日志、指标、事件流 | 任务分发、RPC 解耦 | 混合场景、多租户 |

## 5. 什么时候不要用消息队列

- 调用方必须立刻知道结果（改用同步 API）；
- 系统只有一个模块、没有峰值压力（引入 MQ 徒增复杂度）；
- 需要强事务跨系统一致性（MQ 只能最终一致，账务场景要慎重）。

## 6. 动手试试

1. 列出你熟悉的三个系统交互场景，判断哪个适合引入 MQ、为什么。
2. 用 Docker 分别启动 Kafka 与 RabbitMQ（见后续两章），跑通"发一条、收一条"。
3. 思考：如果消费者处理失败，消息应该怎么办？（答案见 004 可靠消息模式）

## 7. 一句话记住

> MQ 的三大价值是解耦、削峰、异步；选型看场景：海量事件流选 Kafka，灵活任务分发选 RabbitMQ，云原生多租户选 Pulsar。

<!-- ============ 文档分隔线：054-message-queue/002-KafkaQuickStart.md ============ -->

## 0. 一句话理解

> Kafka 把消息写进"主题"里，主题拆成多个"分区"并行存储；同一条 key 的消息永远进同一分区，所以分区内有序。

## 1. 用 Docker Compose 启动

```yaml
# docker-compose.yml
services:
  kafka:
    image: apache/kafka:4.0
    ports:
      - "9092:9092"
```

```bash
docker compose up -d
docker exec -it kafka-kafka-1 /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 --create --topic orders --partitions 3
```

**讲解：**

1. `apache/kafka:4.0` 是官方镜像（Kafka 4.x 为 2025 起的当前主线）。
2. `--partitions 3` 为主题建 3 个分区：分区是并行度单位，分区越多吞吐越高。
3. `--bootstrap-server` 指定集群入口地址，命令行工具都靠它连接。

## 2. 命令行收发消息

```bash
# 启动生产者（输入一行，回车发送一条）
docker exec -it kafka-kafka-1 /opt/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server localhost:9092 --topic orders

# 另开终端启动消费者
docker exec -it kafka-kafka-1 /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 --topic orders --from-beginning
```

**讲解：**

1. 生产者输入 `{"orderId":1,"amount":99}` 回车即发送，消费者终端实时打印。
2. `--from-beginning` 表示从头消费所有历史消息——Kafka 的消息默认保留 7 天，可重放。
3. 生产代码使用官方客户端（Java/Go/Python 等），命令行为学习调试用。

## 3. 分区键与顺序

```text
消息 A（key=user-1） -> 分区 0
消息 B（key=user-1） -> 分区 0
消息 C（key=user-2） -> 分区 1
```

**讲解：**

1. 发送时带 key，Kafka 对 key 做哈希决定分区：**同一个 key 永远进同一分区**。
2. 分区内消息按写入顺序存储、消费组内同一分区的消息也按顺序投递给同一个消费者实例。
3. 因此"同一用户的订单事件必须有序"就用 `key=userId`；全局有序则需要单分区（牺牲吞吐）。

## 4. 消费组

```bash
docker exec -it kafka-kafka-1 /opt/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 --topic orders --group order-handler
```

**讲解：**

1. `--group order-handler` 声明消费组：组内多个消费者实例自动平分分区（3 分区最多 3 个实例并行）。
2. 消费组记录了"消费到哪个偏移量"：重启后从上次位置继续，不会从头再来（除非 `--from-beginning`）。
3. 组内一个实例挂了，其分区自动分配给组内其他实例——这是 Kafka 高可用的基础。

## 5. 动手试试

1. 创建 `user-events` 主题（3 分区），用同一个 key 发 5 条消息，观察它们是否总进同一分区。
2. 起两个同组消费者，发 6 条消息，观察消息如何被两个消费者平分。
3. 停止消费者再启动（不删 group），发新消息，确认不会重复消费旧消息。

## 6. 一句话记住

> Kafka 的消息存在分区里：key 决定分区、分区决定顺序、消费组决定并行；消息保留可重放，是它与传统队列最大的不同。

<!-- ============ 文档分隔线：054-message-queue/003-RabbitMQQuickStart.md ============ -->

## 0. 一句话理解

> RabbitMQ 的核心是"交换机决定消息进哪个队列"：生产者只发给交换机，交换机按路由键把消息送进绑定的队列，消费者从队列取。

## 1. 启动与后台

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
```

**讲解：**

1. `5672` 是 AMQP 协议端口（应用连接），`15672` 是管理后台（浏览器访问，默认账号 `guest/guest`）。
2. `rabbitmq:4-management` 镜像自带管理插件；RabbitMQ 4.x 为当前主线。
3. 管理后台可以直观看到交换机、队列、消息积压情况，入门阶段多看看。

## 2. 交换机类型

| 类型 | 路由规则 | 场景 |
| --- | --- | --- |
| direct 直连 | 路由键完全相等 | 按级别路由（info/error） |
| fanout 广播 | 发给所有绑定队列 | 广播通知 |
| topic 主题 | 通配符匹配（`*` 一段、`#` 多段） | 灵活分类路由 |
| headers 头匹配 | 按消息头匹配 | 少见 |

## 3. Python 收发示例

```bash
pip install pika
```

```python
# send.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")
channel.queue_declare(queue="log-queue")
channel.queue_bind(exchange="logs", queue="log-queue")

channel.basic_publish(
    exchange="logs",
    routing_key="",
    body="Hello RabbitMQ".encode()
)

print("已发送")
connection.close()
```

```python
# receive.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")
channel.queue_declare(queue="log-queue")
channel.queue_bind(exchange="logs", queue="log-queue")


def callback(ch, method, properties, body):
    print("收到：", body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue="log-queue", on_message_callback=callback)
print("等待消息……")
channel.start_consuming()
```

**讲解：**

1. `exchange_declare` 声明交换机（fanout 广播），`queue_declare` 声明队列，`queue_bind` 把两者绑定。
2. 生产者 `basic_publish` 只指定交换机与消息体，不关心队列。
3. 消费者 `basic_consume` 注册回调；`basic_ack` 手动确认"这条我处理完了"。
4. **手动确认是关键**：处理成功才 ack，消费者崩溃时消息会重新投递，避免消息丢失。

## 4. 工作队列与公平分发

```python
channel.basic_qos(prefetch_count=1)
```

**讲解：**

1. 多个消费者订阅同一队列时，RabbitMQ 默认轮询分发；`prefetch_count=1` 表示"一次最多拿 1 条，处理完再拿"。
2. 这样慢消费者不会被塞满任务，快消费者不会空闲——实现"能者多劳"。
3. 不设置 QoS 时，如果某条消息处理很久，其他消息仍会继续派发给该消费者，造成堆积不均。

## 5. 动手试试

1. 起两个 `receive.py`，连发 10 条消息，观察带/不带 `prefetch_count=1` 的分发差异。
2. 把回调里的 `basic_ack` 注释掉再重启消费者，观察消息是否被重新投递。
3. 改用 `topic` 交换机：`logs.info`、`logs.error` 两条路由键分别路由到不同队列。

## 6. 一句话记住

> RabbitMQ 的模型是"交换机 → 队列 → 消费者"三段式；手动 ack + prefetch=1 是可靠任务队列的标准姿势。

<!-- ============ 文档分隔线：054-message-queue/004-ReliableMessagingPatterns.md ============ -->

## 0. 一句话理解

> 消息系统的可靠性 = 不丢（确认机制）+ 不重（消费幂等）+ 失败有去处（死信队列）+ 快慢有协调（背压）。

## 1. 不丢消息：三段确认

| 阶段 | 风险 | 对策 |
| --- | --- | --- |
| 生产者 → Broker | 网络闪断，消息没发出 | 发送确认（Kafka acks=all，RabbitMQ publisher confirms） |
| Broker 存储 | 服务器宕机丢数据 | 副本机制（Kafka 多副本、RabbitMQ 镜像/仲裁队列） |
| Broker → 消费者 | 消费者处理失败 | 手动确认：成功才 ack，失败重投 |

```python
# RabbitMQ 生产者确认（pika 示例片段）
channel.confirm_delivery()
if channel.basic_publish(...):
    print("Broker 已确认收到")
```

**讲解：**

1. `confirm_delivery()` 开启发布确认：`basic_publish` 返回成功代表 Broker 已持久化，而不是"发出去了"。
2. 消费者侧"先处理业务、后 ack"；如果先 ack 再处理，处理崩溃就会丢消息。
3. Kafka 生产端 `acks=all` 表示副本全部写入成功才确认，配合 `min.insync.replicas=2` 使用。

## 2. 消费幂等：重复无害

```python
# 幂等示例：用唯一键去重（Redis SETNX 或数据库唯一索引）
import redis

r = redis.Redis()
message_id = "order-1001-paid"

ok = r.set(message_id, "1", nx=True, ex=86400)
if ok:
    # 第一次处理
    process_payment(message_id)
else:
    # 重复消息，直接跳过
    print("重复消息，忽略")
```

**讲解：**

1. At-least-once 语义下消息可能重复投递，消费端必须"重复执行也安全"。
2. 用消息唯一 ID + 去重存储（Redis `SET NX` 或数据库唯一索引）是最常用的幂等方案。
3. 也可以设计业务天然幂等：如"把余额设置为 100"重复执行结果相同；而"余额 +10"就不幂等。

## 3. 死信队列：失败消息有去处

```text
业务队列 -> 重试 3 次仍失败 -> 死信队列（DLQ）
                                -> 人工/定时任务分析补偿
```

**讲解：**

1. 消息处理失败通常先重试（指数退避），超过次数后放入死信队列，而不是无限重试阻塞主队列。
2. 死信队列里的消息由监控告警 + 人工排查，修复后重新放回业务队列。
3. RabbitMQ 用 `x-dead-letter-exchange` 声明死信；Kafka 通常用独立的 `xxx-dlq` 主题。

## 4. 顺序保证

```text
必须有序：同一订单的事件（创建 -> 支付 -> 发货）
做法：Kafka 用 key=orderId 保证进同一分区；RabbitMQ 用单队列 + 单消费者
```

**讲解：**

1. 全局有序成本极高，99% 的场景只需要"业务键内有序"。
2. Kafka 一个分区一个消费者实例处理，顺序自然保证；分区数就是并行上限。
3. 顺序与吞吐是矛盾：要顺序就别把同一 key 的消息拆到多个分区。

## 5. 背压与消费能力

```text
生产速率 10 万/秒 > 消费速率 1 万/秒
=> 队列积压 -> 监控告警 -> 扩容消费者 / 优化消费逻辑 / 降级
```

**讲解：**

1. 消息积压（Lag）是首要监控指标：Kafka 看消费组 Lag，RabbitMQ 看队列 Ready 数量。
2. 扩容消费者前先确认瓶颈：数据库慢则加消费者也没用，先优化查询与批量处理。
3. 长期积压要考虑降级策略：丢弃非关键消息或合并批量处理，避免"雪崩式追债"。

## 6. 生产检查清单

- 生产者开启发送确认，失败有重试与告警；
- Broker 开启副本与持久化（Kafka `acks=all` + 副本数 3）；
- 消费者手动确认 + 重试 + 死信队列；
- 消费逻辑幂等，重复消息无害；
- 监控队列积压、消费 Lag、重试次数，配告警；
- 消息体带唯一 ID、时间戳与 schema 版本，便于追踪与演进。

## 7. 动手试试

1. 在 RabbitMQ 里搭"业务队列 + 死信队列"：让一条消息处理失败 3 次后进入 DLQ。
2. 用 Redis `SET NX` 实现一个消费去重器，连续投递同一 ID 两次，确认第二次被忽略。
3. 给 Kafka 消费组配一个积压告警：Lag 超过阈值时输出日志（可用命令行 `kafka-consumer-groups.sh --describe` 查看 Lag）。

## 8. 一句话记住

> 可靠 = 确认不丢 + 幂等不重 + DLQ 兜底 + Lag 监控；顺序只在业务键内保证，别拿全局有序换吞吐。

<!-- ============ 文档分隔线：054-message-queue/005-AdvancedRoadmap.md ============ -->

## 0. 你现在在哪里

学习目标：对照进阶路线，明确接下来三站要学什么、为什么按这个顺序学。

前四篇文档带你完成了消息队列的入门闭环：理解队列解决什么问题（001）、
跑通 Kafka（002）、跑通 RabbitMQ（003）、掌握可靠投递的通用模式（004）。
到这里，你已经能给业务选型并搭起"能收能发"的消息链路。

本篇是通往精通阶段的路线图：把剩余的核心能力拆成三站，说明每一站要解决的问题、
涉及的核心机制与学习产出，后续版本会把每一站展开为独立文档。

## 1. 进阶路线总览

| 站点 | 主题 | 解决的问题 | 核心机制 |
| --- | --- | --- | --- |
| 第五站 | Kafka 消费者组与位移管理 | 消费侧怎么扩、怎么保证不丢不重 | 分区分配、再均衡、位移提交、幂等与事务 |
| 第六站 | RocketMQ 快速上手 | 第三大主流选型：交易链路的特色能力 | 顺序/延时/事务消息、重试与死信 |
| 第七站 | 监控、容量与运维 | 线上怎么养：让消息系统长期健康 | lag 观测、容量估算、故障手册 |

三站的关系：第五站把 Kafka 的消费侧吃透（生产环境一半的事故在这里），
第六站补齐 Kafka 不擅长的交易场景能力，第七站站到运维视角俯瞰整个系统。
按顺序学：第五站的位移与再均衡概念在第六、七站都会用到。

## 2. 第五站：Kafka 消费者组与位移管理

生产环境 Kafka 问题的重灾区在消费侧，这一站要吃透四件事：

- 消费者组模型：分区独占消费，组内扩缩容触发再均衡。
- 分区分配策略演进：Range/RoundRobin/Sticky 到 CooperativeSticky（协作式再均衡，
  只挪动必要的分区，避免"停止世界"）。
- 位移提交语义：自动提交与手动提交的组合决定"至少一次/至多一次/精确一次"，
  配合幂等生产者（enable.idempotence）与事务实现跨分区原子写。
- lag 观测：`kafka-consumer-groups.sh --describe` 与 `__consumer_offsets` 主题。

## 3. 第六站：RocketMQ 快速上手

RocketMQ（当前 5.5 版本线）在电商与金融交易链路中广泛使用，
它把 Kafka/RabbitMQ 需要绕路实现的能力做成了原生特性：

- 架构与启动：NameServer + Broker（5.x 新增 Proxy 层）。
- 四种特色消息：顺序消息（MessageQueueSelector 保证单队列有序）、
  延时消息（5.x 支持任意时间）、事务消息（半消息 + 回查）、批量消息。
- 重试与死信：%RETRY% 与 %DLQ% 主题的流转规则。
- 三大队列选型对比表：模型（流/队列）、顺序、延迟、事务、运维复杂度。

## 4. 第七站：监控、容量与运维

消息系统的健康靠数据说话：

- 核心指标：消费 lag、端到端延迟、Broker 吞吐、磁盘水位。
- 监控落地：Kafka 用 Prometheus + kafka exporter + Grafana；
  RocketMQ 用官方 Dashboard。
- 容量规划方法：峰值 QPS × 消息大小 × 保留期估算磁盘；
  分区数 = 目标吞吐 ÷ 单分区吞吐（附算例）。
- 常见故障手册：消费堆积处理、再均衡风暴、磁盘打满、Broker 宕机演练。

## 5. 学习建议

1. 顺序学，不跳站：第五站的概念是后两站的通用语言。
2. 每站一个产出：手写一个可控提交位移的消费者、用事务消息实现"扣款 + 发券"、
   为自己的集群画一张 lag 看板并算一次容量。
3. 版本跟进：Kafka 4.x 已完全 KRaft 化（无 ZooKeeper），新集群不要再规划 ZK；
   RocketMQ 认准 5.x。

## 小结与延伸

- 进阶三站：消费侧可靠性 → 特色消息 → 监控运维，对应从"能通"到"能扛"的跨越。
- 每一站的展开文档将陆续补充在本模块中，编号紧接本篇（006 起）。
- 官方资源：kafka.apache.org/documentation、rocketmq.apache.org/docs。

<!-- ============ 文档分隔线：054-message-queue/006-KafkaConsumerGroupDeepDive.md ============ -->

# Kafka 消费者组与位移管理

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 消费者组模型
- 分区分配策略演进
- 位移提交语义与三种消息语义
- 幂等生产者与事务
- lag 观测

<!-- ============ 文档分隔线：054-message-queue/007-RocketMQQuickStart.md ============ -->

# RocketMQ 快速上手

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- NameServer/Broker/Proxy 架构与启动
- 顺序、延时、事务、批量消息
- 重试队列与死信
- 三大队列选型对比

<!-- ============ 文档分隔线：054-message-queue/008-MonitoringCapacityOperations.md ============ -->

# 监控、容量与运维

> 本篇为占位文档：主题已规划进学习路径，正文内容待补全。

**计划覆盖要点**：

- 核心监控指标
- Prometheus + exporter 落地
- 容量估算方法与算例
- 故障手册与混沌演练
