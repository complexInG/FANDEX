# Java 安全与加密 MessageDigest/Cipher/KeyStore/SecureRandom 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## MessageDigest 摘要

**基本写法：获取摘要实例**
`MessageDigest.getInstance(<算法名>);`
```java
// 创建 SHA-256 摘要计算器
MessageDigest md = MessageDigest.getInstance("SHA-256");
```

---

**基本写法：计算字节数组摘要**
`<md>.digest(<字节数组>);`
```java
// 一次性计算哈希
byte[] hash = md.digest("hello".getBytes(StandardCharsets.UTF_8));
```

---

**基本写法：分块更新**
`<md>.update(<字节数组>);`
```java
// 分块输入数据
md.update("part1".getBytes());
md.update("part2".getBytes());
byte[] h = md.digest();
```

---

## SecureRandom 随机数

**基本写法：创建安全随机数**
`new SecureRandom();`
```java
// 密码学安全的随机数生成器
SecureRandom sr = new SecureRandom();
```

---

**基本写法：生成随机字节**
`<sr>.nextBytes(<字节数组>);`
```java
// 填充随机字节
byte[] salt = new byte[16];
sr.nextBytes(salt);
```

---

**基本写法：生成随机整数**
`<sr>.nextInt(<上界>);`
```java
// 生成 0(含) 到 bound(不含) 的随机数
int code = sr.nextInt(1000000);
```

---

## KeyGenerator 密钥生成

**基本写法：生成对称密钥**
`KeyGenerator.getInstance(<算法>);`
```java
// 创建 AES 密钥生成器
KeyGenerator kg = KeyGenerator.getInstance("AES");
kg.init(256);
SecretKey key = kg.generateKey();
```

---

## Cipher 加解密

**基本写法：获取 Cipher 实例**
`Cipher.getInstance(<算法/模式/填充>);`
```java
// 创建 AES/GCM 加密器
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
```

---

**基本写法：初始化加密**
`<cipher>.init(Cipher.ENCRYPT_MODE, <密钥>);`
```java
// 用密钥初始化为加密模式
cipher.init(Cipher.ENCRYPT_MODE, key);
```

---

**基本写法：执行加密**
`<cipher>.doFinal(<明文>);`
```java
// 加密并返回密文
byte[] ct = cipher.doFinal("secret".getBytes());
```

---

**基本写法：解密**
`<cipher>.init(Cipher.DECRYPT_MODE, <密钥>);`
```java
// 用密钥初始化为解密模式
cipher.init(Cipher.DECRYPT_MODE, key, params);
byte[] pt = cipher.doFinal(ct);
```

---

## KeyStore 密钥库

**基本写法：加载默认密钥库**
`KeyStore.getInstance(<类型>);`
```java
// 创建 JKS 类型密钥库
KeyStore ks = KeyStore.getInstance("PKCS12");
ks.load(null, null); // 新建空密钥库
```

---

**基本写法：存储密钥**
`<ks>.setKeyEntry(<别名>, <密钥>, <密码>, <证书链>);`
```java
// 把密钥存入密钥库
ks.setKeyEntry("myKey", key, "pass".toCharArray(), null);
```

---

## Mac 消息认证码

**基本写法：计算 HMAC**
`Mac.getInstance(<算法>);`
```java
// 创建 HMAC-SHA256
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(key);
byte[] tag = mac.doFinal("data".getBytes());
```

---

## Signature 签名

**基本写法：数字签名**
`Signature.getInstance(<算法>);`
```java
// 创建 SHA256withRSA 签名对象
Signature sig = Signature.getInstance("SHA256withRSA");
sig.initSign(privateKey);
sig.update("data".getBytes());
byte[] sign = sig.sign();
```

---
