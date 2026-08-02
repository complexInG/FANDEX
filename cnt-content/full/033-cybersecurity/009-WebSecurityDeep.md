---
order: 90
title: Web安全深度
module: 'cybersecurity'
category: 云与基础设施
difficulty: advanced
description: Web安全深度：SQL注入、XSS、CSRF、SSRF、JWT安全与API安全
author: fanquanpp
updated: '2026-08-01'
related:
  - 'cybersecurity/008-CryptographyApplication'
  - 'cybersecurity/044-SQLInjection'
  - 'cybersecurity/048-CommandInjection'
  - 'cybersecurity/010-SOC'
prerequisites:
  - 'cybersecurity/001-SecurityBasicsDefense'
---


## 1. SQL 注入

### 1.1 注入类型

| 类型     | 说明          |
| -------- | ------------- |
| 联合查询 | UNION SELECT  |
| 报错注入 | 利用错误信息  |
| 盲注     | 布尔/时间盲注 |
| 堆叠注入 | 多语句执行    |

### 1.2 防御

- 参数化查询（预编译）
- 输入验证
- 最小权限
- WAF

## 2. XSS

### 2.1 类型

| 类型   | 说明        |
| ------ | ----------- |
| 反射型 | URL参数注入 |
| 存储型 | 持久化存储  |
| DOM型  | 客户端渲染  |

### 2.2 防御

- 输出编码
- CSP（Content Security Policy）
- HttpOnly Cookie
- 输入验证

## 3. CSRF

### 3.1 攻击原理

```
用户已登录A网站
→ 访问恶意网站B
→ B自动发送请求到A
→ A认为是用户操作
```

### 3.2 防御

- CSRF Token
- SameSite Cookie
- 验证 Referer/Origin
- 双重Cookie验证

## 4. SSRF

### 4.1 攻击场景

- 访问内网服务
- 读取本地文件
- 云元数据获取凭证

### 4.2 防御

- URL白名单
- 禁止内网地址
- 限制协议（仅HTTP/HTTPS）
- 网络隔离

## 5. JWT 安全

### 5.1 常见漏洞

| 漏洞        | 说明         |
| ----------- | ------------ |
| 算法None    | 删除签名     |
| RS256→HS256 | 公钥作为密钥 |
| 弱密钥      | 暴力破解     |
| 未验证签名  | 忽略验证     |

### 5.2 安全实践

- 使用 RS256/ES256
- 密钥足够长
- 验证签名和声明
- 设置短过期时间
- 不存敏感数据

## 6. API 安全

### 6.1 OWASP API Top 10

| 风险           | 说明         |
| -------------- | ------------ |
| 对象级授权     | 越权访问     |
| 认证失效       | 认证绕过     |
| 对象属性级授权 | 敏感字段暴露 |
| 速率限制       | 无限调用     |
| 功能级授权     | 管理API暴露  |

### 6.2 API 安全措施

- OAuth2/OIDC 认证
- 速率限制
- 输入验证
- 输出过滤
- API 网关
- 审计日志

## 延伸阅读
密码学与证书，见 033-cybersecurity 模块文档。
Web 攻击与防御，见 033-cybersecurity 模块相关文档。
网络层安全，见 032-networking 模块。
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
