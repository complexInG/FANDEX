---
order: 130
title: 进阶学习路线图
module: 'software-architecture'
category: 云与基础设施
difficulty: intermediate
description: 承上启下：从已掌握的三大队列入门出发，给出通往精通的进阶路线与学习建议。
author: fanquanpp
updated: '2026-08-29'
related:
  - 'software-architecture/012-ReliableMessagingPatterns'
prerequisites:
  - 'software-architecture/012-ReliableMessagingPatterns'
---

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
