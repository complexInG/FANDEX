---
order: 57
title: 非对称加密
module: cybersecurity
category: 'eng-infra'
difficulty: intermediate
description: '非对称加密原理：RSA、ECC、Diffie-Hellman 等算法详解与应用。'
author: fanquanpp
updated: '2026-08-01'
related:
  - cybersecurity/对称加密
  - cybersecurity/应急响应
  - cybersecurity/哈希算法
  - cybersecurity/安全开发
prerequisites:
  - cybersecurity/安全基础与防御
---

## 1. 非对称加密基础

### 1.1 基本概念

非对称加密使用一对密钥：**公钥**（公开）和**私钥**（保密）。

$$E_{pub}(M) = C, \quad D_{priv}(C) = M$$

### 1.2 核心应用

| 应用     | 方式               |
| -------- | ------------------ |
| 加密通信 | 公钥加密，私钥解密 |
| 数字签名 | 私钥签名，公钥验证 |
| 密钥交换 | 协商共享密钥       |

### 1.3 与对称加密对比

| 对比项   | 对称加密     | 非对称加密    |
| -------- | ------------ | ------------- |
| 密钥     | 1 个共享密钥 | 公钥+私钥对   |
| 速度     | 快（1000x+） | 慢            |
| 密钥分发 | 困难         | 简单          |
| 典型用途 | 数据加密     | 密钥交换/签名 |

## 2. RSA 算法

### 2.1 数学基础

RSA 安全性基于**大整数分解困难性**。

**密钥生成**：

1. 选择两个大素数 $p, q$（通常 1024+ 位）
2. 计算 $n = pq$
3. 计算欧拉函数 $\phi(n) = (p-1)(q-1)$
4. 选择 $e$，满足 $1 < e < \phi(n)$，$\gcd(e, \phi(n)) = 1$（通常 $e = 65537$）
5. 计算 $d$，满足 $ed \equiv 1 \pmod{\phi(n)}$

- 公钥：$(n, e)$
- 私钥：$(n, d)$

**加密**：$C = M^e \mod n$

**解密**：$M = C^d \mod n$

### 2.2 正确性证明

由 $ed \equiv 1 \pmod{\phi(n)}$，存在 $k$ 使 $ed = k\phi(n) + 1$

$$C^d = (M^e)^d = M^{ed} = M^{k\phi(n)+1} = M^{k\phi(n)} \cdot M \equiv M \pmod{n}$$

（由欧拉定理 $M^{\phi(n)} \equiv 1 \pmod{n}$，当 $\gcd(M, n) = 1$）

### 2.3 RSA 填充方案

| 方案        | 全称                                  | 安全性                   |
| ----------- | ------------------------------------- | ------------------------ |
| PKCS#1 v1.5 | RSAES-PKCS1-v1_5                      | 存在 Bleichenbacher 攻击 |
| OAEP        | Optimal Asymmetric Encryption Padding | 推荐                     |
| PSS         | Probabilistic Signature Scheme        | 签名推荐                 |

**OAEP 填充**：

```
m' = m || 0...0  ← 填充到 n 的长度
m' = MGF(seed) XOR m' || seed = MGF(m') XOR seed
C = (m')^e mod n
```

### 2.4 RSA 代码示例

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# 生成密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# 加密
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 解密
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
```

### 2.5 RSA 攻击

| 攻击           | 条件              | 描述                 |
| -------------- | ----------------- | -------------------- |
| 分解攻击       | $n$ 较小          | 直接分解 $n$         |
| 共模攻击       | 同一 $n$ 不同 $e$ | 利用扩展欧几里得算法 |
| 低指数攻击     | $e$ 过小且 $M$ 短 | $M^e < n$ 时直接开方 |
| Bleichenbacher | PKCS#1 v1.5       | Oracle 攻击          |
| 侧信道         | 时间/功耗         | Montgomery 乘法泄露  |

## 3. ECC 椭圆曲线加密

### 3.1 数学基础

椭圆曲线定义：

$$y^2 = x^3 + ax + b \pmod{p}$$

**点加法**：$P + Q = R$

**标量乘法**：$kP = P + P + \cdots + P$（$k$ 次）

**离散对数问题**（ECDLP）：已知 $P$ 和 $kP$，求 $k$ 是困难的。

### 3.2 常用曲线

| 曲线       | 密钥长度 | 等效 RSA  | 用途     |
| ---------- | -------- | --------- | -------- |
| secp256k1  | 256 位   | 3072 位   | Bitcoin  |
| P-256      | 256 位   | 3072 位   | TLS/通用 |
| P-384      | 384 位   | 7680 位   | 高安全   |
| Curve25519 | 256 位   | 3072 位   | 密钥交换 |
| Ed448      | 448 位   | ~14000 位 | 高安全   |

### 3.3 ECDH 密钥交换

```
Alice: 生成私钥 a，计算 aG（G 为基点）
Bob:   生成私钥 b，计算 bG

交换: Alice → aG → Bob
      Bob   → bG → Alice

共享密钥:
Alice: a(bG) = abG
Bob:   b(aG) = abG
```

### 3.4 ECDSA 签名

```python
from cryptography.hazmat.primitives.asymmetric import ec

# 生成密钥
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# 签名
signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

# 验证
public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
```

### 3.5 EdDSA（Ed25519）

```python
from cryptography.hazmat.primitives.asymmetric import ed25519

# 生成密钥
private_key = ed25519.Ed25519PrivateKey.generate()

# 签名（无需指定哈希算法）
signature = private_key.sign(message)

# 验证
public_key = private_key.public_key()
public_key.verify(signature, message)
```

**Ed25519 优势**：

- 确定性签名（无随机数依赖）
- 快速
- 抗侧信道
- 无歧义验证

## 4. Diffie-Hellman 密钥交换

### 4.1 经典 DH

$$A = g^a \mod p, \quad B = g^b \mod p$$

$$s = B^a \mod p = A^b \mod p = g^{ab} \mod p$$

### 4.2 安全参数

| 参数 | 推荐值   |
| ---- | -------- |
| $p$  | 2048+ 位 |
| $g$  | 2 或 5   |

### 4.3 前向保密

使用临时密钥（Ephemeral DH / DHE），每次会话生成新的 DH 参数，即使长期私钥泄露，历史会话仍安全。

## 5. 算法选择指南

| 场景       | 推荐算法              |
| ---------- | --------------------- |
| 密钥交换   | X25519（ECDH）        |
| 数字签名   | Ed25519 / ECDSA P-256 |
| 加密       | RSA-OAEP 2048+        |
| 兼容旧系统 | RSA 2048+             |
| 禁止使用   | RSA 1024、DH 768      |

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
