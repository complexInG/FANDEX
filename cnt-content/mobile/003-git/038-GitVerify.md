# git verify 签名验证命令速查手册

> **符号约定**:`< >` 必填参数 | `[ ]` 可选参数

---

## 签名提交与标签

**基本用法:GPG 签名提交**
`git commit -S [选项]`

```bash
# 用 GPG 密钥签名提交
git commit -S -m "release v2.0"

# 指定密钥签名
git commit -S --gpg-sign=<KEY_ID> -m "signed commit"
```

---

**基本用法:签名标签**
`git tag -s <标签名>`

```bash
# 创建带 GPG 签名的附注标签
git tag -s v1.0.0 -m "release 1.0"

# 用指定密钥签名
git tag -s v1.0.0 -u <KEY_ID> -m "release 1.0"
```

---

## 验证签名

**基本用法:验证提交签名**
`git verify-commit <提交>`

```bash
# 验证某提交是否被正确签名
git verify-commit a1b2c3d

# 显示原始签名信息
git verify-commit --raw a1b2c3d
```

---

**基本用法:验证标签签名**
`git verify-tag <标签>`

```bash
# 验证标签签名
git verify-tag v1.0.0

# 显示标签签名详情
git tag -v v1.0.0
```

---

## 查看签名信息

**基本用法:在 log 中显示签名**
`git log --show-signature`

```bash
# 查看提交历史时显示签名验证结果
git log --show-signature -5

# 仅显示 Good signature 的提交
git log --pretty="format:%G? %s" | grep "^G"
```

---

## 配置默认签名

**基本用法:开启全局签名**
`git config --global commit.gpgsign true`

```bash
# 默认所有提交都签名
git config --global commit.gpgsign true

# 默认所有标签都签名
git config --global tag.gpgsign true

# 指定签名密钥
git config --global user.signingkey <KEY_ID>
```

---