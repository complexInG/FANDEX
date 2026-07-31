# 应用签名与发布 语法速查手册

> **符号约定**：`< >` 必填参数 | `[ ]` 可选参数

---

## 密钥与证书

**基本写法：生成密钥库**
`keytool -genkeypair -alias <别名> -keyalg EC -keysize 256 -sigalg SHA256withECDSA -keystore <文件.p12> -storetype PKCS12 -validity <天数>`
```bash
# 生成 EC 密钥对（有效期 25 年）
keytool -genkeypair -alias myapp -keyalg EC -keysize 256 -sigalg SHA256withECDSA -keystore myapp.p12 -storetype PKCS12 -validity 36500 -dname "CN=MyCompany, O=MyCompany, C=CN"
```

---

**基本写法：生成证书请求文件**
`keytool -certreq -alias <别名> -keystore <文件.p12> -file <文件.csr>`
```bash
# 生成 CSR 提交至 AppGallery Connect
keytool -certreq -alias myapp -keystore myapp.p12 -file myapp.csr
```

---

**基本写法：查看密钥库信息**
`keytool -list -v -keystore <文件.p12> -storepass <密码>`
```bash
# 查看密钥库中的证书详情
keytool -list -v -keystore myapp.p12 -storepass 123456
```

---

## 命令行签名

**基本写法：hap-sign-tool 签名**
`java -jar hap-sign-tool.jar sign-app -keyAlias <别名> -signAlg SHA256withECDSA -mode localSign -appCertFile <证书.cer> -profileFile <配置.p7b> -inFile <输入.hap> -keystoreFile <密钥库.p12> -outFile <输出.hap> -keyPwd <密码> -keystorePwd <密码> -signCode 1`
```bash
# 命令行对 HAP 包进行签名
java -jar hap-sign-tool.jar sign-app -keyAlias myapp -signAlg SHA256withECDSA -mode localSign -appCertFile myapp.cer -profileFile myapp.p7b -inFile entry-unsigned.hap -keystoreFile myapp.p12 -outFile entry-signed.hap -keyPwd 123456 -keystorePwd 123456 -signCode 1
```

---

**基本写法：验证签名**
`java -jar hap-sign-tool.jar verify-app -inFile <已签名.hap>`
```bash
# 验证 HAP 包签名信息
java -jar hap-sign-tool.jar verify-app -inFile entry-signed.hap
```

---

## 拆包与调试签名

**基本写法：APP 拆包为 HAP**
`java -jar app_unpacking_tool.jar --mode app --app-path <输入.app> --out-path <输出目录> --force true`
```bash
# 将 APP 包拆分为多个 HAP
java -jar app_unpacking_tool.jar --mode app --app-path my-app.app --out-path ./out --force true
```

---

**基本写法：调试签名 HAP**
`java -jar hap-sign-tool.jar sign-app -keyAlias <别名> -signAlg SHA256withECDSA -mode localSign -appCertFile <调试证书.cer> -profileFile <调试Profile.p7b> -inFile <hap> -keystoreFile <p12> -outFile <输出> -keyPwd <密码> -keystorePwd <密码> -signCode 1`
```bash
# 使用调试证书签名 HAP 用于真机调试
java -jar hap-sign-tool.jar sign-app -keyAlias myapp -signAlg SHA256withECDSA -mode localSign -appCertFile debug.cer -profileFile debug.p7b -inFile entry-default.hap -keystoreFile myapp.p12 -outFile entry-debug.hap -keyPwd 123456 -keystorePwd 123456 -signCode 1
```

---

## hvigor 构建命令

**基本写法：构建 HAP**
`hvigorw --mode module -p module=<模块>@default -p product=default assembleHap`
```bash
# 构建 entry 模块的 HAP 包
hvigorw --mode module -p module=entry@default -p product=default assembleHap --parallel --incremental --daemon
```

---

**基本写法：构建 APP（多模块）**
`hvigorw --mode project -p product=<产品> assembleApp`
```bash
# 构建整个项目的 APP 包
hvigorw --mode project -p product=default assembleApp
```

---

**基本写法：清理构建**
`hvigorw clean`
```bash
# 清理构建产物
hvigorw clean
```

---

## build-profile.json5 签名配置

**基本写法：配置签名信息**
`"signingConfigs": [{ "name": "<名称>", "type": "HarmonyOS", "material": { "cert": { "file": "<证书.cer>" }, "store": { "file": "<密钥库.p12>", "password": "<密码>" }, "key": { "alias": "<别名>", "password": "<密码>" }, "profile": { "file": "<配置.p7b>" } } }]`
```json5
// build-profile.json5 配置 release 签名
{
  "app": {
    "signingConfigs": [
      {
        "name": "release",
        "type": "HarmonyOS",
        "material": {
          "cert": { "file": "myapp.cer" },
          "store": { "file": "myapp.p12", "password": "123456" },
          "key": { "alias": "myapp", "password": "123456" },
          "profile": { "file": "myapp.p7b" }
        }
      }
    ],
    "products": [
      { "name": "default", "signingConfig": "release" }
    ]
  }
}
```

---

**基本写法：自动签名**
`"signingConfigs": [{ "name": "default", "type": "HarmonyOS", "material": { "cert": { "file": "debug.cer" } } }]`
```json5
// 开启自动签名（DevEco Studio 管理证书）
{
  "app": {
    "signingConfigs": [
      { "name": "default", "type": "HarmonyOS", "material": {} }
    ]
  }
}
```

---

## hdc 设备管理

**基本写法：安装应用**
`hdc install <文件.hap>`
```bash
# 安装 HAP 到连接设备
hdc install entry-signed.hap
```

---

**基本写法：卸载应用**
`hdc uninstall <包名>`
```bash
# 按包名卸载应用
hdc uninstall com.example.myapp
```

---

**基本写法：查看已安装应用**
`hdc shell bm dump -n <包名>`
```bash
# 查看应用签名信息
hdc shell bm dump -n com.example.myapp
```

---

**基本写法：查看设备列表**
`hdc list targets`
```bash
# 列出所有连接的设备
hdc list targets
```
