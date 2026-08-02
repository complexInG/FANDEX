---
order: 130
title: 负载均衡技术
module: 'networking'
category: 云与基础设施
difficulty: advanced
description: 负载均衡技术：四层/七层负载、算法、健康检查、会话保持与全局负载
author: fanquanpp
updated: '2026-08-01'
related:
  - 'networking/011-NetworkDesignPlanning'
  - 'networking/012-DNSDHCP'
  - 'networking/014-NetworkAutomation'
  - 'networking/015-LoadBalanceAlgorithm'
prerequisites:
  - 'networking/001-NetworkBasicsAndProtocol'
---


## 1. 负载均衡概述

### 1.1 四层 vs 七层

| 维度     | L4       | L7                |
| -------- | -------- | ----------------- |
| 工作层   | 传输层   | 应用层            |
| 判断依据 | IP+端口  | URL/Header/Cookie |
| 性能     | 高       | 中                |
| 灵活性   | 低       | 高                |
| 代表     | LVS, NLB | Nginx, HAProxy    |

## 2. 负载均衡算法

| 算法       | 说明           | 适用       |
| ---------- | -------------- | ---------- |
| 轮询       | 依次分配       | 服务器同构 |
| 加权轮询   | 按权重分配     | 服务器异构 |
| 最少连接   | 选连接最少的   | 长连接     |
| 一致性哈希 | 按请求特征哈希 | 有状态     |
| 随机       | 随机选择       | 简单场景   |

## 3. 健康检查

| 类型   | 方法     | 粒度   |
| ------ | -------- | ------ |
| ICMP   | ping     | 基础   |
| TCP    | 端口连接 | 传输层 |
| HTTP   | GET/HEAD | 应用层 |
| 自定义 | 业务接口 | 精确   |

## 4. 会话保持

| 方式      | 说明            | 优缺点       |
| --------- | --------------- | ------------ |
| Source IP | 按源IP哈希      | 简单，不均匀 |
| Cookie    | 插入/改写Cookie | 精确，需支持 |
| Session   | 服务器间同步    | 复杂         |

## 5. 全局负载均衡（GSLB）

基于DNS的跨地域负载均衡：

```
用户 → DNS查询 → GSLB → 返回最近站点IP
```

策略：地理位置、网络延迟、站点可用性、负载。

## 延伸阅读
网络基础与协议，见 032-networking 模块文档。
网络安全（TLS/WAF），见 033-cybersecurity 模块。
负载均衡与网关，见 031-devops 模块相关文档。
## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 TCP 拥塞控制

慢启动：指数增长直到 ssthresh；拥塞避免：线性增长；快速重传/快速恢复处理丢包。
BBR（Google）基于带宽与延迟估计，替代丢包驱动的传统算法。
队列与缓冲膨胀（bufferbloat）导致延迟抖动；AQM（CoDel）缓解。
调优：理解 RTT、窗口与带宽延迟积（BDP）的关系。

### 13.2 HTTPS 与证书体系

TLS 握手：ClientHello -> ServerHello + 证书 -> 密钥交换 -> Finished；1.3 一轮往返完成。
证书链：根 CA -> 中间 CA -> 站点证书；OCSP/CRL 吊销检查。
Let's Encrypt 自动化签发与续期（ACME 协议）。
配置基线：TLS 1.2+、禁用弱套件、HSTS、证书透明度。
