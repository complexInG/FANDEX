---
order: 56
title: 云安全
module: cybersecurity
category: 网络安全
difficulty: advanced
description: 云安全：共享责任模型、CSPM、CWPP、云原生安全与合规
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/SSRF攻击
  - cybersecurity/恶意代码分析
  - cybersecurity/对称加密
  - cybersecurity/应急响应
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 共享责任模型

### 1.1 责任划分

| 层级     | 云厂商 | 客户       |
| -------- | ------ | ---------- |
| 物理安全 |        | -          |
| 基础设施 |        | -          |
| 网络     |        | 安全组/ACL |
| 操作系统 | -      |            |
| 运行时   | -      |            |
| 应用     | -      |            |
| 数据     | -      |            |

### 1.2 IaaS/PaaS/SaaS 责任

| 模式 | 客户责任   |
| ---- | ---------- |
| IaaS | OS以上     |
| PaaS | 应用和数据 |
| SaaS | 仅数据     |

## 2. CSPM（云安全态势管理）

### 2.1 检查项

| 类别 | 检查项           |
| ---- | ---------------- |
| 身份 | MFA、最小权限    |
| 网络 | 安全组、公开端口 |
| 存储 | 加密、公开访问   |
| 日志 | 审计日志启用     |
| 加密 | 传输/存储加密    |

### 2.2 常见错误配置

| 错误配置        | 风险       |
| --------------- | ---------- |
| S3公开读写      | 数据泄露   |
| 安全组0.0.0.0/0 | 暴露服务   |
| 无MFA           | 账号被入侵 |
| 硬编码凭证      | 凭证泄露   |
| 未加密EBS       | 数据泄露   |

## 3. CWPP（云工作负载保护）

### 3.1 保护层次

```
应用层：WAF、API安全
  ↓
容器层：镜像扫描、运行时保护
  ↓
OS层：HIDS、漏洞管理
  ↓
基础设施：网络策略、加密
```

### 3.2 容器安全

- 镜像扫描（Trivy）
- 运行时保护（Falco）
- 网络策略（NetworkPolicy）
- 安全上下文（SecurityContext）

## 4. 云原生安全

### 4.1 安全左移

| 阶段 | 安全措施          |
| ---- | ----------------- |
| 代码 | SAST、密钥扫描    |
| 构建 | 镜像扫描、签名    |
| 部署 | IaC扫描、策略检查 |
| 运行 | 运行时保护、监控  |

### 4.2 CNAPP

云原生应用保护平台，整合CSPM和CWPP：

- 代码到运行时全生命周期
- 统一安全策略
- 上下文关联分析

## 5. 云合规

### 5.1 合规标准

| 标准     | 适用     |
| -------- | -------- |
| SOC2     | 美国企业 |
| ISO27001 | 全球     |
| GDPR     | 欧盟数据 |
| PCI DSS  | 支付卡   |
| HIPAA    | 医疗     |
| 等保     | 中国     |

### 5.2 合规自动化

- AWS Config Rules
- Azure Policy
- GCP Organization Policy
- OPA/Gatekeeper

## 参考文献

OWASP Top 10：https://owasp.org/www-project-top-ten/
OWASP Cheat Sheets：https://cheatsheetseries.owasp.org/
NIST 网络安全框架：https://www.nist.gov/cyberframework
CWE 数据库：https://cwe.mitre.org/
PortSwigger Web Security Academy：https://portswigger.net/web-security

## 延伸阅读

密码学与证书，见 033-cybersecurity 模块文档。
Web 攻击与防御，见 033-cybersecurity 模块相关文档。
网络层安全，见 032-networking 模块。
黑马程序员 Bilibili 空间（https://space.bilibili.com/37974444 ）提供网络安全课程。

## 深度专题扩展

以下专题从不同角度深入本文主题，供有进阶需求的读者研读。每个专题独立成节，内容相互补充。

### 13.1 Web 攻击链详解

注入类：SQLi（参数化防御）、XSS（输出编码 + CSP）、命令注入（白名单）。
身份类：会话固定/劫持（HttpOnly + SameSite）、JWT 算法混淆（固定算法 + 校验）。
逻辑类：越权（IDOR）、竞态（TOCTOU）、支付篡改（服务端重算）。
防护纵深：WAF 拦截已知模式 + 应用层校验 + 监控异常。

### 13.2 零信任架构

核心原则：永不信任、始终验证；身份驱动策略而非网络位置。
组件：身份代理（IdP）、策略引擎（PDP）、网关（PEP）、微隔离。
落地路径：先高价值资产试点，逐步覆盖；配合 MFA 与设备合规。
成本与体验平衡：无密码（passkey）与连续评估是方向。
