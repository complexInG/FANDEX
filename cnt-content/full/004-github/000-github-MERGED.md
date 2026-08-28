---
order: 10
title: github 模块文档合集
module: 'github'
category: 工具链
difficulty: intermediate
description: 本模块全部文档合并生成的完整合集，按学习顺序排列。
author: fanquanpp
updated: '2026-08-13'
related: []
prerequisites: []
---

<!-- ============ 文档分隔线：004-github/001-GitHubOverview.md ============ -->



## 0. 从一个生活场景说起：GitHub 就像一座"代码图书馆"

想象你第一次走进一家大型图书馆：有图书上架区（存放书籍）、检索台（查找书籍）、阅览室（阅读书籍）、以及"读者留言墙"（讨论书籍）。**GitHub 就是为程序员建造的这座图书馆**，只不过"书籍"换成了代码仓库，"读者留言"换成了 Issue 和 Pull Request。

但 GitHub 又比图书馆多了一样东西——**它是活的**。图书馆里的书只能读不能改，而 GitHub 上的代码仓库可以被复制、修改、合并，还能记录每一次修改是谁、在什么时候、为什么做的。这正是它被称为"程序员社交平台"的原因：全球超过 1 亿开发者在这里存放代码、协作开发、交流学习。

本文将以**一位新手开发者"小明"的完整旅程**为主线：注册账户 → 认识首页 → 创建第一个仓库 → 完成第一次提交 → 发起第一个 Pull Request，带你走一遍 GitHub 的核心功能。

## 1. 第一站：GitHub 是什么

### 1.1 直观理解

- **代码托管**：把你的代码"上传"到云端，随时随地可以下载，不用担心硬盘损坏。
- **版本记录**：每一次修改都留下"快照"，改坏了可以随时回退到任意历史版本。
- **协作平台**：多个人可以同时在同一个项目上工作，互不干扰，最后合并成果。
- **开源社区**：全球大量知名项目（Linux、React、Vue、Python 等）都托管在 GitHub 上，你可以免费阅读、学习甚至参与贡献。

### 1.2 原理讲解：Git 与 GitHub 的分工

先理解两个容易混淆的概念：

| 方面 | Git | GitHub |
| :--- | :--- | :--- |
| 本质 | 分布式版本控制系统（软件） | 基于 Git 的代码托管平台（云服务） |
| 运行位置 | 本地命令行工具 | 互联网上的网站服务 |
| 核心能力 | 在本地记录文件每次修改、支持分支与合并 | 在云端保存仓库、提供协作/CI/CD 等能力 |
| 是否需要联网 | 否，纯本地操作 | 是，拉取与推送需要联网 |

可以这样理解：**Git 是你的"日记本"（本地记录），GitHub 是"图书馆"（云端的公共/私有存档）**。你平时写代码用 Git 在本地记账，需要分享或备份时再推送到 GitHub。

### 1.3 发展历程快览

| 时间 | 里程碑 |
| :--- | :--- |
| 2008 | GitHub 成立，提供 Git 仓库托管服务 |
| 2018 | 微软以 75 亿美元收购 GitHub |
| 2019 | 推出 GitHub Actions（CI/CD 自动化） |
| 2020 | 代码仓库数量突破 2 亿 |
| 2022 | GitHub Copilot 正式发布（AI 编程助手） |
| 2023 | 要求贡献代码的用户启用 2FA 双因素认证 |
| 2025 | 用户数突破 1 亿，仓库数超过 4 亿 |

## 2. 第二站：注册账户（旅程起点）

打开 https://github.com/ ，点击 **Sign up**，依次填写邮箱、密码、用户名即可完成注册（详细步骤见 002 篇《账户注册与双因素认证》）。

注册完成后建议立即做三件事：

1. **验证邮箱**：GitHub 会发送验证邮件，未验证邮箱将无法创建仓库等基础操作。
2. **设置 2FA**：2023 年 3 月起 GitHub 要求贡献代码的用户必须启用双因素认证，这是保护账户的第一道防线。
3. **完善个人资料**：设置头像、姓名和简介，让他人更容易识别你。

## 3. 第三站：认识你的首页

登录后的首页包含几个关键区域：

- **个人 Profile**：展示你的头像、简介、置顶仓库和贡献图（contributions graph，绿色小格子记录你每天的提交活跃度）。
- **News Feed**：展示你关注的用户和仓库的最新动态。
- **顶部分区**：`Pull requests`（待审查的拉取请求）、`Issues`（分配给你或你参与的问题）、`Notifications`（通知）、`Explore`（探索发现）。

## 4. 第四站：创建第一个仓库（hello-world）

按照 GitHub 官方"你好，世界"教程，创建第一个仓库：

### 4.1 网页端创建

1. 点击页面右上角的 **+** → **New repository**。
2. 仓库名称输入 `hello-world`，描述输入"我的第一个仓库"。
3. 可见性选择 **Public**（公开）或 **Private**（私有）。
4. 勾选 **Add a README file**（初始化一个说明文档）。
5. 点击 **Create repository**。

创建成功后，你会进入仓库主页。**仓库（repository）就是项目容器**，里面可以放代码文件、文档、图片，同时绑定 Issue、Pull Request、Actions 等协作功能。

### 4.2 认识仓库关键文件

| 文件 | 作用 |
| :--- | :--- |
| `README.md` | 项目说明文档，自动显示在仓库首页，是访客的第一印象 |
| `.gitignore` | 声明哪些文件不需要 Git 跟踪（如编译产物、密钥文件） |
| `LICENSE` | 开源许可证，规定他人如何使用你的代码 |
| `CONTRIBUTING.md` | 贡献指南，告诉他人如何参与项目 |
| `.github/` | 存放 GitHub 特殊配置（Actions 工作流、Issue 模板等） |

### 4.3 命令行创建（GitHub CLI 方式）

如果你已安装 `gh`（见 020 篇），也可以直接在终端创建：

```bash
# 创建公开仓库并克隆到本地
gh repo create hello-world --public --clone
# 或创建私有仓库
gh repo create hello-world --private
```

## 5. 第五站：完成第一次提交（Commit）

**提交（commit）** 就像给当前所有文件拍一张"快照"，并写下"这张快照改了什么"。以下用命令行完成第一次提交：

```bash
# 1. 进入仓库目录
cd hello-world

# 2. 配置本地身份（邮箱必须是 GitHub 已验证邮箱）
git config --global user.name "xiaoming"
git config --global user.email "xiaoming@example.com"

# 3. 新建一个文件
echo "# Hello World" > hello.md

# 4. 把文件加入暂存区（staging area）
git add hello.md

# 5. 提交，-m 后面是提交说明
git commit -m "docs: add hello markdown file"

# 6. 推送到 GitHub 远程仓库（-u 建立本地与远程的关联）
git push -u origin main
```

执行完第 6 步，刷新 GitHub 仓库页面，就能看到 `hello.md` 文件了。**本地 → 暂存区 → 本地仓库 → 远程仓库**，这就是一次完整的提交旅程。

## 6. 第六站：发起第一个 Pull Request（协作核心）

Pull Request（PR，拉取请求）是 GitHub 协作的精髓：**你请求把某个分支的改动合并进另一个分支**，合并前可以讨论、审查、跑自动化检查。

### 6.1 PR 协作流程（简明版）

```bash
# 1. 从 main 创建功能分支（详细见 007 篇分支模型）
git checkout -b feature/add-intro

# 2. 修改代码并提交
git add .
git commit -m "feat: add project intro"
git push -u origin feature/add-intro
```

3. 在 GitHub 仓库页面点击 **Compare & pull request**。
4. 确认 `base`（目标分支，通常是 main）和 `compare`（来源分支）正确。
5. 填写标题和描述，点击 **Create pull request**。
6. 邀请同事审查，审查通过后点击 **Merge pull request** 合并。

> 完整流程见 027 篇《Pull Request 完整协作流程》。

### 6.2 与 PR 配套的协作功能

| 功能 | 一句话说明 |
| :--- | :--- |
| Issues | 记录 Bug、功能需求、任务（详见 017 篇） |
| Actions | 自动化 CI/CD，如推送后自动跑测试（详见 029 篇） |
| Projects | 看板式项目管理，可视化任务进度 |
| Discussions | 社区讨论区，适合长期话题沉淀 |
| Wiki | 项目文档中心 |
| Releases | 发布版本，附下载包与更新说明 |

## 7. 第七站：GitHub 的账户类型与订阅计划

### 7.1 账户类型

- **个人账户（Personal account）**：每个开发者的身份标识，可以属于多个组织。
- **组织账户（Organization）**：适合团队与企业，支持成员管理、权限分级、审计日志。

### 7.2 订阅计划（个人账户）

| 计划 | 价格 | 核心特性 |
| :--- | :--- | :--- |
| Free | 免费 | 无限公开/私有仓库，2,000 Actions 分钟/月，Codespaces 120 核心小时/月 |
| Pro | $4/月 | 高级代码审查工具，3,000 Actions 分钟/月 |
| Team | $4/用户/月 | 组织权限管理，代码所有者（CODEOWNERS）等 |
| Enterprise | $21/用户/月 | SAML SSO、审计日志、更多安全合规能力 |

### 7.3 高效探索：搜索语法与快捷键

GitHub 的站内搜索能力非常强大，学会几招就能快速找到目标代码或仓库：

```text
language:python stars:>1000        # Python 项目，星标超过 1000
topic:react fork:true              # React 主题，且包含 Fork
owner:facebook path:src            # Facebook 仓库的 src 目录下
is:pr is:merged author:alice       # alice 已合并的 PR
```

网页端常用的键盘快捷键：

| 快捷键 | 功能 |
| :--- | :--- |
| `.` | 在 Web 编辑器中打开当前仓库 |
| `T` | 文件搜索 |
| `W` | 分支切换 |
| `L` | 跳转到指定行 |
| `B` | 查看 Blame（每行代码的最后修改者） |
| `?` | 显示全部快捷键帮助 |

## 8. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 提交者身份未配置 | `Please tell me who you are` | 未设置 `user.name` 和 `user.email` | 执行 `git config --global user.name "你的名字"` 和 `git config --global user.email "你的邮箱"` |
| 推送被拒绝 | `Authentication failed` | 使用了旧密码而非 PAT，或令牌过期 | 生成新的个人访问令牌（PAT）代替密码（详见 002/004 篇） |
| 邮箱未验证 | 无法创建仓库 | 注册后未点击邮件验证链接 | 检查收件箱，点击 GitHub 发送的验证链接 |
| 提交没显示在贡献图上 | 贡献图空白 | 本地 `user.email` 与 GitHub 账户邮箱不一致 | 使用 GitHub 已验证邮箱重新配置并提交 |
| 推错分支 | PR 合到了错误的 base | 未确认 base/compare 分支 | 创建 PR 时检查页面顶部的 base repository 和 branch |
| 仓库找不到 | `Repository not found` | 仓库私有、URL 错误或已被删除 | 确认 URL 拼写、检查可见性与访问权限 |

## 10. 一句话记忆

**GitHub 是程序员存放代码、记录版本、协作开发的"代码图书馆"：Git 负责本地记账，GitHub 负责云端存档与协作，而 Pull Request 是协作的大门。**

### 延伸阅读

- 账户安全与 2FA，见 002 篇《账户注册与双因素认证》。
- 仓库的创建、克隆、归档与删除，见 003 篇。
- 分支模型与分支保护规则，见 007 篇。
- Pull Request 完整协作流程，见 027 篇。
- GitHub CLI 命令行操作，见 020 篇。



<!-- ============ 文档分隔线：004-github/002-AccountRegister2FA2FA.md ============ -->



## 0. 从一个生活场景说起：账户安全就像"实名认证 + 家门双锁"

想象你入住一栋公寓：办理入住（注册账户）后，物业管理处会要求你**实名认证**（验证邮箱），以防有人冒用身份；为了防小偷，你给家门装了两道锁——**第一道锁是钥匙（密码），第二道锁是指纹或手机 App 动态码（2FA）**。小偷即使偷到了钥匙，没有你的指纹或手机，依然进不了门。

GitHub 账户安全遵循同样的逻辑：**密码是第一道锁，双因素认证（2FA）是第二道锁**。GitHub 上不仅有你的代码，还有私有仓库、Issues、CI/CD 配置等关键资产。一旦账户被盗，攻击者可能窃取代码、篡改项目、甚至用你的名义发布恶意内容。因此，**从注册的第一天起，就把安全措施配置到位**，是本篇的核心主线。

## 1. 注册账户：安全的第一步

### 1.1 注册流程

1. 打开 https://github.com/ ，点击 **Sign up**（也可选择"使用 Google 继续"社交登录）。
2. 依次填写**邮箱、密码、用户名**：
   - **用户名**：会成为你的主页地址（如 `github.com/你的用户名`），建议与你的常用网名一致，便于他人识别。
   - **密码**：建议至少 16 位，包含大小写字母、数字和特殊字符的组合，不要与其他网站共用。
3. 完成人机验证（CAPTCHA），点击 **Create account**。
4. 到邮箱中点击 GitHub 发送的**验证链接**完成验证。

> 官方提醒：**未验证邮箱将无法完成创建仓库等基础操作**，所以验证邮箱是必做项。

### 1.2 密码策略要点

- **使用强密码**：GitHub 官方要求创建"强且唯一的密码"。
- **不要复用**：同一密码用于多个平台，一旦某个平台泄露，其他账户全部受威胁。
- **使用密码管理器**：推荐用 Bitwarden、1Password 等工具生成并保管强密码，避免明文记录。

## 2. 双因素认证（2FA）原理讲解

### 2.1 什么是 2FA：先直观理解

密码属于"**你知道的**"（knowledge factor）；2FA 增加"**你持有的**"（possession factor）或"**你具备的**"（inherence factor）。攻击者要同时拿到"知道"和"持有"两样东西才能登录，难度大幅提升。

### 2.2 TOTP 原理：逐步深入

最常见的方式是 **TOTP（基于时间的一次性密码）**，工作流程如下：

1. 开启 2FA 时，GitHub 展示一个**二维码**，内含一段密钥（secret）。
2. 手机验证器 App（如 Google Authenticator、Microsoft Authenticator）扫描二维码并保存密钥。
3. App 使用密钥 + **当前时间**，通过哈希算法计算出一个 **6 位动态码**，每 30 秒自动更新一次。
4. 登录时输入这 6 位动态码，GitHub 用相同的密钥和当前时间独立计算并比对，一致则通过。

因为动态码依赖"你手机里的密钥 + 当前时间"，且 30 秒即失效，所以即使密码泄露，攻击者也无法在短时间内冒充你。

### 2.3 可选验证方式与安全等级

| 方式 | 说明 | 安全等级 |
| :--- | :--- | :--- |
| 安全密钥（Security Key / WebAuthn） | 硬件密钥如 YubiKey，USB 触碰验证 | 高 |
| TOTP 验证器 App | 手机 App 生成 6 位动态码 | 高 |
| 通行密钥（Passkey） | 基于 WebAuthn 的无密码认证 | 高 |
| GitHub Mobile | 手机 App 推送确认 | 中高 |
| 短信（SMS） | 短信验证码 | 低（易受 SIM 卡交换攻击，不推荐） |

> 官方建议：**优先使用 TOTP 应用，并额外添加安全密钥作为备份**；尽量不用短信。

### 2.4 政策背景

自 2023 年 3 月起，GitHub 要求所有在 GitHub.com 上**贡献代码的用户启用 2FA**。就算你的账户暂未被强制，也强烈建议立即开启——这是官方对账户安全的最基本要求。

## 3. 开启 2FA：操作步骤

### 3.1 使用 TOTP 验证器（推荐主方式）

1. 手机安装任意 TOTP 应用（Google Authenticator、Microsoft Authenticator、Authy 等）。
2. 登录 GitHub，点击头像 → **Settings** → **Password and authentication**。
3. 在 "Two-factor authentication" 区域点击 **Enable two-factor authentication**。
4. 选择 **Set up using an app**（使用身份验证应用）。
5. 用手机 App 扫描屏幕上的二维码，App 中会出现 GitHub 条目并显示 6 位动态码。
6. 把动态码输入网页验证框，点击 **Verify**。
7. 页面会显示**恢复代码（recovery codes）**，点击 **Download** 下载保存（默认文件名为 `github-recovery-codes.txt`）。

> 注意：开启 2FA 后账户进入 **28 天检查期**，期间成功完成一次 2FA 登录即可结束检查期。

### 3.2 添加安全密钥（推荐备份方式）

1. 进入 **Settings → Password and authentication**。
2. 在 "Security keys" 区域点击 **Add security key**。
3. 将 YubiKey 等硬件密钥插入 USB 接口，按提示触摸按钮完成绑定。
4. 之后登录时可选择用安全密钥代替动态码。

### 3.3 保存恢复代码（保命操作）

恢复代码是**失去手机/验证器时的唯一后门**，GitHub 官方明确警告：**启用 2FA 后如果丢失凭证且无恢复方法，GitHub 支持团队也无法帮你恢复账户访问**。所以请：

- 下载恢复代码文件并保存在安全位置（密码管理器）。
- 打印纸质副本放在可靠处。
- **不要**把恢复代码截图发到聊天工具或网盘公开分享。

## 4. 2FA 与命令行访问：PAT 与 SSH

启用 2FA 后，通过 HTTPS 使用命令行访问仓库时，**不能再使用账户密码**，需要改用**个人访问令牌（PAT）** 或 **SSH 密钥**。

### 4.1 生成个人访问令牌（PAT）

1. 进入 **Settings → Developer settings → Personal access tokens → Tokens (classic)**。
2. 点击 **Generate new token** → **Generate new token (classic)**。
3. 填写 **Note**（令牌用途，如 "my-laptop-https"），设置 **Expiration**（建议 30-90 天）。
4. 勾选需要的 **Scopes**（权限范围）：推送代码勾选 `repo`；删除仓库另需 `delete_repo`；遵循**最小权限原则**，只勾必需的。
5. 点击 **Generate token**，**立即复制保存**——离开页面后无法再次查看。

### 4.2 使用 PAT 完成 HTTPS 操作

```bash
# 首次克隆/推送时提示输入用户名和密码
git clone https://github.com/用户名/仓库.git
# 提示 Username 时：输入 GitHub 用户名
# 提示 Password 时：粘贴 PAT（不是账户密码！）
```

配置凭据管理器可避免每次输入：

```bash
# Windows：Git Credential Manager
git config --global credential.helper manager
# macOS
git config --global credential.helper osxkeychain
# Linux
git config --global credential.helper libsecret
```

### 4.3 备选方案：SSH 密钥

SSH 密钥使用非对称加密，配置一次即可长期使用，且不受 2FA 动态码影响（详见 004 篇《SSH 与 HTTPS 远程配置》）。对频繁推送的开发者，SSH 是更省心的选择。

### 4.4 账户恢复的最后防线：多条恢复路径

GitHub 官方建议**配置两种以上恢复方式**，避免单一方式失效时被锁在门外。除恢复代码外，以下方法也可用于找回账户：

| 恢复方式 | 说明 |
| :--- | :--- |
| 恢复代码 | 一次性代码，用一条少一条，可用完生成新的一批 |
| SSH 密钥 | 已注册的 SSH 密钥可作为 2FA 恢复凭证 |
| 个人访问令牌（PAT） | 未过期的 PAT 也可用于恢复验证 |
| 已验证设备 | 之前成功登录过 2FA 的设备可用来验证身份 |
| 通行密钥/安全密钥 | WebAuthn 类凭证，绑定后可独立完成认证 |

> 官方明确警告：**如果以上恢复方式全部丢失，GitHub 支持团队也无法恢复账户访问**。建议开启 2FA 后在 Settings → Password and authentication 中逐一确认这些恢复路径仍可访问。

## 5. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 恢复码丢失且手机不可用 | 无法登录，提示需要 2FA | 未妥善保存恢复代码 | 若还有备用恢复方式（SSH 密钥、已验证设备、PAT）可尝试恢复；否则按官方恢复流程尝试，最坏情况账户无法找回 |
| 输入动态码报错 | `Authentication code incorrect` | 手机时间不准或输入过快 | 校准手机时间（TOTP 依赖时间），等动态码刷新后重试 |
| 推送时提示认证失败 | `Authentication failed` | HTTPS 下误用了账户密码而非 PAT | 重新生成 PAT 并粘贴到凭据管理器 |
| PAT 权限不足 | 推送被拒绝（403） | 生成 PAT 时未勾选 `repo` 权限 | 重新生成令牌，勾选所需最小权限范围 |
| 贡献统计不显示 | 提交未计入贡献图 | 本地 `user.email` 未在 GitHub 验证 | 在 Settings → Emails 添加并验证该邮箱，再用新配置提交 |
| 公司 SSO 登录问题 | 组织要求 SAML 单点登录 | 企业强制统一身份认证 | 遵循公司 IT 政策，使用企业提供的登录入口 |

## 7. 一句话记忆

**GitHub 账户安全 = 强密码（第一道锁）+ 2FA 双因素认证（第二道锁）+ 妥善保存的恢复代码（备用钥匙），三者缺一不可。**

### 延伸阅读

- GitHub 平台整体概览，见 001 篇《GitHub 概述》。
- SSH 密钥与 HTTPS+PAT 的完整对比配置，见 004 篇《SSH 与 HTTPS 远程配置》。
- 令牌管理与多账户切换，见 020 篇《GitHub CLI》。



<!-- ============ 文档分隔线：004-github/003-RepositoryCreateCloneArchiveDelete.md ============ -->



## 0. 从一个生活场景说起：仓库就像一家"店铺"

想象你开一家网店：先**选址注册**（创建仓库），把商品上架（添加代码文件）；开业后可以**开分店**（克隆仓库到多台电脑）；生意不做了可以**挂牌歇业**（归档仓库）——店铺还在、门面还展示，但不再营业；如果彻底不想干了，就**注销店铺**（删除仓库）——注意，注销是永久性的，所有货物、交易记录都没了。

GitHub 仓库（repository）就是代码的"店铺"：创建、克隆、归档、删除是它的四个生命周期操作。本篇作为**操作向导**，手把手带你走完这四步的完整流程。

## 1. 原理讲解：仓库是什么

### 1.1 直观理解

仓库是一个**项目容器**，不仅存放代码文件，还聚合了协作功能：

- 代码与版本历史（Git 对象）
- Issues（问题跟踪）
- Pull Requests（代码审查与合并）
- Actions（CI/CD 自动化）
- Wiki / Discussions / Projects 等

### 1.2 仓库可见性（三种"店面类型"）

| 类型 | 谁可见 | 适用场景 |
| :--- | :--- | :--- |
| Public（公开） | 所有人 | 开源项目、学习分享 |
| Private（私有） | 仅你和受邀协作者 | 商业项目、内部开发 |
| Internal（内部） | 仅组织成员（需企业计划） | 企业组织内部共享 |

### 1.3 关键概念

- **默认分支**：仓库的主分支，默认名为 `main`。
- **README**：显示在仓库首页的说明文档。
- **.gitignore**：声明哪些文件不被 Git 跟踪（如 `node_modules/`、`.env`）。
- **License**：开源许可证，规定代码的使用方式。

## 2. 第一步：创建仓库（开店）

### 2.1 网页端创建

1. 登录 GitHub，点击右上角 **+** → **New repository**。
2. 填写信息：
   - **Repository name**：建议小写字母 + 连字符，如 `my-notes-app`（名称规则：仅字母、数字、`-`、`_`、`.`，不能以点开头或结尾）。
   - **Description**：一句话描述项目用途。
   - **Visibility**：选择 Public 或 Private。
   - **Initialize this repository with**：勾选 **Add a README file**（推荐，便于立即克隆和展示）；可按需选择 `.gitignore` 模板和 License。
3. 点击 **Create repository**。

### 2.2 组织内创建

进入组织主页 → **Repositories** → **New**，与个人创建流程相同，但仓库所有权归属组织，创建后可为成员配置访问权限。

### 2.3 命令行创建（gh）

```bash
# 创建公开仓库并克隆到本地
gh repo create my-notes-app --public --clone
# 创建私有仓库
gh repo create my-notes-app --private
```

## 3. 第二步：克隆仓库（开分店）

**克隆（clone）** 是把远程仓库完整复制到本地，包含全部历史版本。

### 3.1 克隆命令

```bash
# HTTPS 克隆（需要 PAT，见 004 篇）
git clone https://github.com/OWNER/REPO.git

# SSH 克隆（需要配置 SSH 密钥，见 004 篇）
git clone git@github.com:OWNER/REPO.git

# 克隆指定分支
git clone -b dev https://github.com/OWNER/REPO.git

# 浅克隆：只取最近 1 次历史，适合大仓库
git clone --depth 1 https://github.com/OWNER/REPO.git

# 进入仓库目录并查看远程配置
cd REPO
git remote -v
```

### 3.2 从空仓库开始：本地推送已有项目

如果先在 GitHub 创建了**空的仓库**（未勾选 README），需要把本地项目推上去：

```bash
# 1. 进入已有项目目录
cd existing-project

# 2. 初始化 Git 仓库（如果还没有）
git init

# 3. 添加所有文件到暂存区
git add .

# 4. 提交初始版本
git commit -m "chore: initial commit"

# 5. 确保分支名为 main
git branch -M main

# 6. 关联远程仓库（使用 GitHub 页面提供的 URL）
git remote add origin https://github.com/OWNER/REPO.git

# 7. 推送并设置上游追踪
git push -u origin main
```

### 3.3 远程仓库管理常用命令

```bash
git remote -v                          # 查看远程地址
git remote add upstream <URL>          # 添加上游远程（Fork 工作流常用）
git remote set-url origin <新URL>      # 修改远程地址
git remote remove upstream             # 删除远程
git pull origin main                   # 拉取远程更新
git push origin main                   # 推送本地更新
```

### 3.4 切换仓库可见性与协作权限

**可见性切换**（公开 ↔ 私有）：进入仓库 **Settings → Danger Zone → Change repository visibility**。

- 公开转私有：仓库立即从公开索引消失，原公开链接变 404；之前别人 Fork 的副本不受影响。
- 私有转公开：**务必先审计**历史提交、Issue、Wiki 中是否有密钥、密码、个人信息，再执行切换。

**协作者权限级别**（Settings → Collaborators and teams → Add people）：

| 级别 | 能力 |
| :--- | :--- |
| Read | 只读：查看、克隆、提 Issue/PR |
| Triage | Read + 管理 Issue/PR 标签与里程碑 |
| Write | Triage + 推送代码、编辑仓库内容 |
| Maintain | Write + 管理仓库设置（不含敏感/破坏性操作） |
| Admin | 完全控制，含删除仓库、改可见性 |

> 遵循最小权限原则：能 Read 就不给 Write，避免误操作破坏主分支。

## 4. 第三步：归档仓库（挂牌歇业）

**归档（archive）** 使仓库变为**只读**：不能新建 Issue/PR、不能推送提交，但代码仍可浏览、克隆和 fork。适合已完成或不再维护的项目。

### 4.1 网页端归档

1. 进入仓库 → **Settings** → 下拉到 **Danger Zone**。
2. 点击 **Archive this repository**。
3. 阅读警告，在输入框中输入仓库名称确认。
4. 点击 **I understand the consequences, archive this repository**。

> 官方建议：归档前先关闭所有打开的 Issue 和 PR，并更新 README 说明项目状态。

### 4.2 归档后的影响

- 仓库标记为 "Archived"（只读徽章）。
- 无法创建新 Issue、PR、无法推送提交。
- 仍可克隆、fork、加星。
- 现有内容（代码、Wiki、Release）保持不变。
- 可随时**取消归档**（Settings → Danger Zone → Unarchive this repository）恢复写权限。

### 4.3 命令行归档

```bash
gh repo archive OWNER/REPO --yes       # 归档
gh repo unarchive OWNER/REPO --yes     # 取消归档
```

## 5. 第四步：删除仓库（注销店铺）

**删除是不可逆操作**：代码、提交历史、Issue、PR、Wiki、Release 全部销毁。删除前务必备份。

### 5.1 删除前备份

```bash
# 镜像克隆：包含所有分支和引用
git clone --mirror https://github.com/OWNER/REPO.git
```

### 5.2 网页端删除

1. 进入仓库 → **Settings** → **Danger Zone**。
2. 点击 **Delete this repository**。
3. 输入 `OWNER/REPO`（完整仓库名，大小写敏感）确认。
4. 点击 **I understand the consequences, delete this repository**。

### 5.3 命令行删除

```bash
gh repo delete OWNER/REPO --yes
```

> 提示：误删后 GitHub 支持在有限窗口内申请恢复，但**不要依赖这个"后悔药"**。归档（Archive）是比删除更稳妥的选择——先归档观察，确认无需保留再删除。

### 5.4 进阶技巧：仓库模板与镜像迁移

**仓库模板（Template repository）**：把某个仓库标记为模板后，其他人可一键复制出"相同结构、不含历史提交"的新仓库，适合统一项目骨架。

1. 在仓库 Settings 中勾选 **Template repository**。
2. 别人进入该仓库后点击 **Use this template** 即可创建同结构新仓库。
3. 模板仓库会忽略 fork 关系，新仓库是全新的独立项目。

**仓库镜像（Mirror）迁移**：把整个仓库（含所有分支与标签）迁移到新位置：

```bash
# 1. 镜像克隆（裸仓库，含全部引用）
git clone --mirror https://github.com/ORIGIN/REPO.git
cd REPO.git

# 2. 推送到新位置
git push --mirror https://github.com/NEW/REPO.git
```

**批量管理仓库**（适合组织场景）：

```bash
# 列出组织全部仓库
gh repo list ORGANIZATION --limit 100
# 批量创建
gh repo create ORG/repo-a --public --description "desc"
```

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 仓库名非法 | 创建失败 | 名称含空格或非法字符（如 `.hidden`、连续点） | 使用小写字母、数字、连字符，不以点开头/结尾 |
| 克隆大仓库很慢 | 长时间无响应 | 仓库历史提交多、体积大 | 使用浅克隆 `git clone --depth 1`，需要历史时再 `git fetch --depth=100` 加深 |
| 克隆报 LFS 错误 | `git-lfs: command not found` | 仓库使用 Git LFS 但本地未安装 | 安装并初始化：`git lfs install`，再执行 `git lfs pull` |
| 推送被拒，提示权限不足 | `Permission denied` / 403 | 没有仓库写权限，或 PAT 权限不足 | 检查协作者角色（Write 及以上）；重新生成含 `repo` 权限的 PAT |
| 推送到 main 失败 | `protected branch` | 分支启用了保护规则 | 按保护规则走 PR 流程合并，或由管理员临时调整规则 |
| 找不到删除/归档按钮 | Danger Zone 无选项 | 不是仓库 Owner/Admin | 只有 Owner 或 Admin 角色才能归档/删除；组织仓库需组织管理员授权 |

## 8. 一句话记忆

**仓库生命周期四步走：创建（开店）→ 克隆（开分店）→ 归档（挂牌歇业，随时复业）→ 删除（注销店铺，不可恢复，务必先备份）。**

### 延伸阅读

- 仓库与 GitHub 整体概念，见 001 篇《GitHub 概述》。
- HTTPS 与 SSH 远程配置，见 004 篇《SSH 与 HTTPS 远程配置》。
- 分支模型与分支保护规则，见 007 篇《分支模型与分支保护规则》。
- 仓库迁移、镜像与批量管理，见 049 篇《Gh Repo 管理》。



<!-- ============ 文档分隔线：004-github/004-SSHHTTPS.md ============ -->



## 0. 从一个生活场景说起：钥匙与门禁卡

想象你所在的公司大楼有两种进门方式：**钥匙（SSH）** 和 **门禁卡（HTTPS）**。

- **钥匙**：配好之后天天随身带，开门不需要联网验证、不用输密码——但第一次配钥匙要花点功夫（生成密钥对），而且钥匙丢了很麻烦。
- **门禁卡**：人人都有、发卡简单，但每次进门都要"刷卡 + 输入临时口令"（输入 PAT），口令还会过期，过期就得重新领。

GitHub 远程连接正好对应这两种方式：**SSH** 用非对称密钥对认证，配置一次长期免密；**HTTPS** 用"用户名 + 个人访问令牌（PAT）"认证，简单但每次操作需要凭据。本篇采用**对比驱动**的写法，把两种方式从原理到配置全程对照，帮你做出适合自己的选择。

## 1. 原理讲解：两种认证方式对比

### 1.1 直观对比表

| 特性 | SSH | HTTPS |
| :--- | :--- | :--- |
| 认证方式 | 非对称密钥对（公钥 + 私钥） | 用户名 + PAT（个人访问令牌） |
| 默认端口 | 22（可改用 443） | 443 |
| 首次配置 | 稍复杂：生成密钥、添加公钥 | 简单：生成 PAT 即可 |
| 日常体验 | 配置后免密，适合高频推送 | 凭据管理器记住后基本免密 |
| 安全性 | 私钥保存在本地，安全性高 | PAT 泄露风险需注意保管 |
| 网络兼容性 | 部分企业防火墙会拦截 22 端口 | 几乎不被拦截（走 HTTPS 443） |
| 适用场景 | 多设备高频开发、长期项目 | 偶尔操作、受限网络环境 |

### 1.2 SSH 原理：一步步看懂

1. 本地生成一对密钥：**公钥（.pub）** 和 **私钥（无后缀）**。
2. 把**公钥**上传到 GitHub 账户（Settings → SSH and GPG keys）。
3. 连接时，GitHub 用公钥加密一段"挑战"发送给你，本地用**私钥**解密并回应。
4. GitHub 验证通过，完成认证。

> 关键点：**私钥绝不外传**，公钥随便分享。私钥泄露 = 钥匙被复制，攻击者可冒充你访问仓库。

### 1.3 HTTPS + PAT 原理

- 2021 年后 GitHub 不再接受账户密码做 Git 认证，改为 **PAT（个人访问令牌）**。
- PAT 是你在 GitHub 设置中生成的"带权限的临时密码"，可以设置**有效期**（30/60/90 天等）和**权限范围**（scopes）。
- 本地通过**凭据管理器**（Windows 的 Git Credential Manager、macOS 的 keychain）保存 PAT，避免每次输入。

## 2. SSH 配置：从生成到使用

### 2.1 生成密钥对

```bash
# 推荐 Ed25519 算法（更安全、文件更小）
ssh-keygen -t ed25519 -C "you@example.com" -f ~/.ssh/id_ed25519_github
# 参数说明：
#   -t ed25519  使用 Ed25519 算法
#   -C "..."    添加注释（建议用你的 GitHub 邮箱）
#   -f 路径     指定密钥保存路径和文件名（Windows 可写 %USERPROFILE%\.ssh\id_ed25519_github）
#   -N ""       空密码短语；生产环境建议设置密码短语
```

### 2.2 启动 ssh-agent 并加载私钥

```bash
# Windows（PowerShell）
Start-Service ssh-agent
ssh-add "$env:USERPROFILE\.ssh\id_ed25519_github"
# macOS / Linux
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github
# 查看已加载的密钥
ssh-add -l
```

### 2.3 复制公钥并添加到 GitHub

```bash
# 查看公钥内容（把整行复制下来）
cat ~/.ssh/id_ed25519_github.pub
# Windows: type %USERPROFILE%\.ssh\id_ed25519_github.pub
```

网页操作：头像 → **Settings** → **SSH and GPG keys** → **New SSH key** → 填写标题（如 "My Laptop"）→ 粘贴公钥 → **Add SSH key**。

### 2.4 测试连接

```bash
ssh -T git@github.com
# 首次连接会提示确认主机指纹，输入 yes 回车
# 成功输出：Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

> 官方提醒：如果输出包含你的用户名即成功；若提示 `Permission denied (publickey)`，按第 5 节排查。

### 2.5 使用 SSH 克隆与推送

```bash
# 克隆（注意是 git@github.com: 开头）
git clone git@github.com:username/repository.git

# 日常推送流程
cd repository
git add .
git commit -m "feat: update"
git push origin main
```

## 3. HTTPS 配置：从生成 PAT 到使用

### 3.1 生成 PAT

1. 进入 **Settings → Developer settings → Personal access tokens**。
2. **Fine-grained token（细粒度令牌，推荐）**：可选择仅授权特定仓库、按需勾选具体权限、设置过期时间。
3. 或 **Tokens (classic)**：勾选 scopes，推送代码选 `repo`。
4. 点击 **Generate token**，**立即复制保存**（离开页面后无法再次查看）。

### 3.2 配置凭据管理器

```bash
# Windows：Git Credential Manager
git config --global credential.helper manager
# macOS
git config --global credential.helper osxkeychain
# Linux
git config --global credential.helper libsecret
# 验证配置
git config --global --get credential.helper
```

### 3.3 使用 HTTPS 克隆与推送

```bash
# 克隆
git clone https://github.com/username/repository.git

# 首次推送会提示输入：
#   用户名：GitHub 用户名
#   密码：粘贴 PAT（不是账户密码！）
git push origin main

# 查看远程地址 / 切换协议
git remote -v
git remote set-url origin https://github.com/username/repository.git   # HTTPS -> 已是 HTTPS
git remote set-url origin git@github.com:username/repository.git        # 切到 SSH
```

## 4. 多账户场景：SSH config 配置

同时使用个人账户和公司账户时，用 `~/.ssh/config` 区分：

```sshconfig
# 文件：~/.ssh/config
# 个人账户
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal
  IdentitiesOnly yes

# 公司账户
Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
  IdentitiesOnly yes
```

```bash
# 对应克隆命令
git clone git@github.com-personal:username/personal-repo.git
git clone git@github.com-work:company/work-repo.git
```

## 5. 高级配置：代理、自动加载与凭据安全

### 5.1 SSH 走代理（企业网络）

企业网络常需代理才能出网，可在 `~/.ssh/config` 中为 GitHub 配置代理命令：

```sshconfig
Host github.com
  HostName github.com
  User git
  ProxyCommand nc -X 5 -x proxy.example.com:1080 %h %p
  IdentityFile ~/.ssh/id_ed25519_github
```

### 5.2 自动加载密钥（免每次输密码短语）

```bash
# Windows：在 PowerShell 配置文件中添加
Start-Service ssh-agent
ssh-add ~/.ssh/id_ed25519_github

# macOS/Linux：在 ~/.bashrc 或 ~/.zshrc 中添加
if [ -z "$SSH_AUTH_SOCK" ]; then
  eval "$(ssh-agent -s)"
  ssh-add ~/.ssh/id_ed25519_github
fi
```

### 5.3 凭据安全要点

- **私钥权限**：Linux/macOS 执行 `chmod 600 ~/.ssh/id_ed25519`，防止其他用户读取。
- **PAT 不落盘**：不要把 PAT 写进脚本或提交到仓库；CI 环境用 GitHub Actions 的 `GITHUB_TOKEN` / secrets 代替个人 PAT。
- **定期轮换**：PAT 到期前生成新令牌；SSH 密钥若疑泄露立即在 GitHub 上删除并重新生成。
- **备份私钥**：把私钥加密备份到安全位置，换机时不必重新注册。

### 5.4 故障诊断命令速查

遇到连接问题，按顺序执行以下命令定位：

```bash
# 1. 详细查看 SSH 连接过程（关键：确认使用的密钥文件）
ssh -vT git@github.com

# 2. 确认私钥已加载
ssh-add -l

# 3. 测试远程仓库可读性（HTTPS / SSH 各试一次）
git ls-remote https://github.com/username/repository.git
git ls-remote git@github.com:username/repository.git

# 4. 检查凭据配置
git config --list | grep credential

# 5. 检查远程地址是否用错协议
git remote -v
```

典型流程：先用 `ssh -vT` 看是"密钥被拒"还是"连接超时"；密钥被拒查公钥是否在 GitHub 上、私钥是否加载；连接超时查网络与防火墙。

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 权限被拒绝 | `Permission denied (publickey)` | 公钥未添加到 GitHub、私钥未加载到 ssh-agent、连接了错误的主机 | 检查 Settings → SSH and GPG keys 是否有该公钥；`ssh-add -l` 确认私钥已加载；确认始终用 `git@github.com` 而非你的用户名 |
| 主机密钥验证失败 | `Host key verification failed` | 主机指纹不匹配（可能是中间人攻击或 known_hosts 混乱） | 对比 GitHub 官方公布的 SSH 密钥指纹，确认无误后再连接；必要时清理 `~/.ssh/known_hosts` 对应条目 |
| 认证失败 | `Authentication failed` | HTTPS 下误用账户密码；PAT 过期或权限不足 | 重新生成 PAT 并粘贴；设置凭据管理器自动保存 |
| PAT 过期 | 推送突然失败（401/403） | Classic token 设置了有效期 | 到期前生成新 PAT，用 `git credential-manager` 更新缓存 |
| 多账户串号 | 提交身份混乱 | 多个密钥/PAT 管理混乱 | 用 SSH config 的 Host 别名区分；为不同账户设置不同 `user.email` |
| 端口 22 被拦截 | `Connection timed out`（企业网络） | 防火墙阻止 SSH 22 端口 | 改用 HTTPS，或配置 SSH over HTTPS 端口 443（`~/.ssh/config` 中设置 `HostName ssh.github.com` + `Port 443`） |

## 8. 一句话记忆

**SSH 像配好的钥匙——配一次长期免密；HTTPS 像门禁卡——发卡简单但要保管好 PAT 并定期换卡；高频开发选 SSH，偶尔访问选 HTTPS。**

### 延伸阅读

- 2FA 与 PAT 的关系，见 002 篇《账户注册与双因素认证》。
- gh CLI 自动管理凭据，见 020 篇《GitHub CLI》。
- 仓库克隆与远程管理，见 003 篇《仓库创建、克隆、归档、删除》。



<!-- ============ 文档分隔线：004-github/005-CollaborationDevelopmentStandard.md ============ -->



## 0. 从一个生活场景说起：团队协作公约

想象一个 10 人合租的厨房：如果每个人用完厨具随手乱放、做完菜不贴标签、买了食材不登记，厨房很快会乱成一团。于是大家制定一份**协作公约**：刀具放哪、调料贴标签、垃圾谁倒。公约不是限制自由，而是让每个人都知道"该怎么做"，减少摩擦、提高效率。

软件团队的协作开发也是同一个道理。**GitHub 协作开发规范**就是团队的"厨房公约"：统一的提交信息格式、分支命名规则、PR 模板、代码审查清单、贡献授权协议。本篇采用**规范驱动**的结构，围绕"约定（Convention）→ 落地（Practice）→ 合规（Compliance）"三层讲解。

## 1. 原理讲解：为什么需要协作规范

### 1.1 三个痛点

- **提交历史不可读**：`fix bug`、`update`、`asdf` 这类提交信息三个月后没人看得懂，无法回溯"这次改了什么、为什么改"。
- **审查低效**：没有 PR 模板，审查者要反复追问背景、影响范围、测试情况。
- **法律风险**：开源项目接收外部贡献，若不明确知识产权归属，日后可能引发版权纠纷。

### 1.2 规范解决什么

| 痛点 | 对应规范 | 效果 |
| :--- | :--- | :--- |
| 提交历史混乱 | Commit Message 约定 | 可检索、可自动生成 CHANGELOG |
| 分支混乱 | 分支命名规范 | 见名知义，知道分支在做什么 |
| PR 信息缺失 | PR 模板 | 审查者一次拿到所有上下文 |
| 审查走过场 | 代码审查清单 | 正确性、安全性、可维护性全覆盖 |
| 贡献权属不明 | CLA / DCO | 明确代码知识产权归属 |

## 2. Commit Message 约定：让历史可读

### 2.1 标准格式（Conventional Commits）

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 2.2 类型（Type）说明

| 类型 | 含义 | 示例 |
| :--- | :--- | :--- |
| feat | 新功能 | `feat(auth): add refresh token rotation` |
| fix | 修复 bug | `fix(api): handle 429 from upstream` |
| docs | 文档更新 | `docs(readme): clarify install steps` |
| style | 代码风格（不影响功能） | `style: format code with prettier` |
| refactor | 重构（不加功能不修 bug） | `refactor: extract common utility` |
| test | 测试相关 | `test: add unit tests for auth module` |
| chore | 构建/工具变动 | `chore: update dependencies` |
| perf | 性能优化 | `perf: optimize database query` |
| revert | 回滚 | `revert: revert commit abc123` |

### 2.3 撰写要点

- **Subject（主题）**：不超过 50 字符，用祈使句（"add" 而非 "added"），英文小写开头，结尾不加句号。
- **Scope（作用域）**：可选，标出模块名，如 `auth`、`api`、`ui`。
- **Body（正文）**：每行不超过 72 字符，说明变更的原因和影响。
- **Footer（页脚）**：`BREAKING CHANGE:` 标记破坏性变更；`Closes #123` 关联 Issue；`Signed-off-by:` 用于 DCO 签名。

### 2.4 完整示例

```text
feat(auth): add refresh token rotation

Implement refresh token rotation to improve security.
Clients must now handle token rotation properly.

BREAKING CHANGE: Clients must now handle refresh token rotation.
Closes #456
Signed-off-by: John Doe <john@example.com>
```

### 2.5 配套工具

- **commitizen**：交互式生成规范提交信息。
- **commitlint**：提交时校验格式，不符合即拦截。
- **standard-version / semantic-release**：根据提交类型自动生成 CHANGELOG 与版本号。

## 3. 分支命名与 PR 规范

### 3.1 分支命名规范

```
<type>/<description>
```

示例：`feat/add-login`、`fix/api-error-handling`、`docs/update-readme`。

> 分支规范与 Commit 类型保持一致，看到分支名就知道它在做什么、属于哪类改动。

### 3.2 PR 模板：放在 `.github/pull_request_template.md`

```markdown
## 背景
简要描述本次 PR 的背景和目的。

## 关联 Issue
- Closes #123

## 变更说明
- 新增登录接口
- 修复 token 刷新逻辑

## 测试情况
- 单元测试：通过
- 手工验证：本地启动验证登录流程

## 检查清单
- [ ] 代码符合项目规范
- [ ] 无敏感信息（密钥/密码）
- [ ] 测试已补充
- [ ] README 已同步更新
```

创建模板后，仓库中的每个新 PR 都会自动预填该结构，审查者不必反复追问基本信息。

### 3.3 PR 标题与描述最佳实践

- 标题沿用 `feat(auth): ...` 格式，便于自动生成 CHANGELOG。
- 描述说明"改了什么 + 为什么改 + 怎么验证"。
- 用 `Closes #123` 关联 Issue，合并时自动关闭对应 Issue。
- 涉及 UI 改动附截图；破坏性变更明确标注。

## 4. 代码审查（Code Review）规范

### 4.1 审查者职责

- 理解 PR 目的，先读描述再读代码。
- 按清单检查正确性、安全性、可维护性、性能、测试覆盖。
- 给出**具体可执行**的反馈，而不是空泛的"看不懂"。
- 确认 CI 状态检查通过后再批准。

### 4.2 审查清单（可直接复制使用）

**正确性**：逻辑正确、边界情况处理、错误处理完善、并发安全。

**安全性**：无注入漏洞、无路径遍历、无敏感信息泄露、依赖无已知漏洞、权限控制正确。

**可维护性**：风格一致、命名规范、注释充分、无重复代码、模块化设计。

**测试**：单元/集成测试覆盖、测试用例合理、边界用例存在。

### 4.3 反馈类型

| 反馈类型 | 含义 | 示例 |
| :--- | :--- | :--- |
| 必须修改 | 存在严重问题，不修不能合并 | "这里缺少空指针判断，会崩溃" |
| 建议修改 | 可优化，不阻塞合并 | "建议把这段提取为公共函数" |
| 疑问 | 需要作者解释 | "这里的超时时间是刻意设置的吗？" |
| 赞赏 | 值得肯定 | "这个错误处理写得很严谨" |

### 4.4 审查流程（七步）

1. 分配审查者（CODEOWNERS 自动分配或手动指定）→ 2. 检查 PR 描述与变更范围 → 3. 逐行审查 → 4. 跑测试验证无回归 → 5. 反馈并等待修改 → 6. 复核确认 → 7. 选择合并策略合并。

## 5. CLA 与 DCO：贡献授权的两种方案

### 5.1 概念对比

| 特性 | CLA（贡献者许可协议） | DCO（开发者来源证书） |
| :--- | :--- | :--- |
| 本质 | 正式法律协议，明确知识产权归属 | 轻量声明，签名确认有权提交 |
| 复杂度 | 高（需律师参与起草） | 低（一个 `Signed-off-by` 签名） |
| 法律约束力 | 强 | 中等 |
| 适用场景 | 大型项目、企业项目 | 开源项目、中小型项目 |

### 5.2 CLA 落地

- 使用 **CLA Assistant** 等 GitHub App：贡献者首次提 PR 时自动弹出协议，签署后才可合并。
- 分为**个人 CLA** 与**企业 CLA**（员工代表公司贡献时签署）。

### 5.3 DCO 落地

1. 提交时用 `git commit -s` 自动附加签名行：

```bash
git commit -s -m "feat(auth): add refresh token rotation"
# 提交信息中自动包含：
# Signed-off-by: 你的名字 <your@email.com>
```

2. 用 GitHub Action（如 `actions/dco`）在 CI 中校验每个提交是否带签名，未签名则检查失败。

```yaml
# .github/workflows/dco.yml
name: DCO Check
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  dco:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/dco@v2
```

> 补签历史提交：`git rebase --signoff` 可给旧提交补上签名。

### 5.4 文档规范与团队落地清单

规范要落地，配套文档不可少。在仓库中维护以下"健康文件"（详见 026 篇《社区健康文件》）：

| 文件 | 作用 |
| :--- | :--- |
| `README.md` | 项目概述、安装、使用说明 |
| `CONTRIBUTING.md` | 贡献指南：如何提 Issue、如何开发、如何提交 PR |
| `CODE_OF_CONDUCT.md` | 社区行为准则 |
| `SECURITY.md` | 安全漏洞上报流程 |
| `CODEOWNERS` | 按模块指定代码审查负责人（详见 025 篇） |

**团队落地五步**：

1. 先定 Commit 规范与分支命名规范，写入 README 或 CONTRIBUTING。
2. 配置 PR 模板与 Issue 模板，用工具（commitlint/DCO Action）强制校验。
3. 主分支开启保护规则，要求 PR 合并 + 审查 + CI 通过（详见 007 篇）。
4. 用 CODEOWNERS 把关键模块的审查责任落到具体人。
5. 每季度回顾一次流程，根据痛点迭代规范。

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 提交信息不规范 | 被 commitlint 拦截 | 未遵循约定式提交格式 | 按 `<type>(<scope>): <subject>` 重写；用 commitizen 交互生成 |
| PR 描述太敷衍 | 审查者反复追问 | 没写背景、影响、测试 | 使用 PR 模板，按"背景/变更/测试/清单"填写 |
| DCO 检查失败 | CI 红叉：missing Signed-off-by | 提交未加签名 | `git commit -s` 重新提交；历史提交用 `git rebase --signoff` 补签 |
| 分支命名随意 | 分支堆积难维护 | 无命名规范 | 统一 `<type>/<description>`；合并后及时删除分支 |
| 审查意见无回应 | PR 长时间无人跟进 | 作者未回复或修改 | 作者及时回复每条评论；设置提醒；必要时礼貌催促 |
| 合并冲突反复出现 | PR 冲突不断 | 功能分支长期未同步 main | 定期 `git pull origin main` 同步；保持 PR 小而聚焦 |

## 8. 一句话记忆

**协作规范就是团队的"厨房公约"：提交信息让历史可读，PR 模板让审查高效，审查清单把好质量关，CLA/DCO 明确权属，四者共同支撑可持续的团队协作。**

### 延伸阅读

- 分支模型与保护规则落地，见 007 篇《分支模型与分支保护规则》。
- 团队健康文件（CONTRIBUTING/CODE_OF_CONDUCT），见 026 篇《社区健康文件》。
- 代码所有者（CODEOWNERS）自动分配审查者，见 025 篇。
- PR 全流程实操，见 027 篇《Pull Request 完整协作流程》。



<!-- ============ 文档分隔线：004-github/006-READMEFile.md ============ -->



## 0. 从一家饭店说起：README 就是店铺的招牌和产品说明书

想象你住的小区门口开了两家新饭店，你下班路过想随便吃点：

- **第一家饭店**只在门口挂了一块木板，上面写着"饭店"两个字。没有店名、没有菜单、没有价格、没有营业时间。你走进去问："你们卖什么？"老板头也不抬："自己看。"你只好悻悻离开。
- **第二家饭店**挂出了招牌"老王川菜馆"，旁边立着一块菜单板：招牌菜、价格、营业时间、是否支持打包，甚至写着"新店开业，水煮鱼 8 折"。你在 30 秒内就决定了：今天吃它！

你的 GitHub 仓库就是这家"饭店"，而 **README 文件**就是它的招牌加产品说明书。任何一个访客（同学、未来的同事、潜在用户、招聘你的面试官）点进你的仓库，第一眼看到的就是 README。它决定了对方是"转身就走"还是"留下来看看"。

在正式讲解之前，先记住一个结论：**README 回答访客最关心的五个问题**——这个项目是做什么的？为什么有用？怎么开始用？遇到问题去哪求助？谁在维护和贡献它？（这五个问题来自 GitHub 官方文档对 README 的定义。）

## 1. 直观理解：没有 README 的仓库 vs 有 README 的仓库

### 1.1 两个仓库的对比

假设你负责的两个仓库放在一起，一个是空的，一个写好了 README：

| 对比维度 | 仓库 A：没有 README | 仓库 B：有 README |
| :--- | :--- | :--- |
| 访客第一印象 | 一堆陌生文件，不知道从哪看起 | 一段话讲清项目定位，30 秒进入状态 |
| 想试用的人 | 找不到安装方法，放弃 | 按"快速开始"三步跑起来 |
| 想贡献的人 | 不知道能不能改、怎么改 | 按"贡献指南"提交第一个 PR |
| 出了 Bug 的人 | 不知道去哪反馈 | 看到 Issue 链接和联系渠道 |
| 搜索可见性 | 仓库描述缺省，难以被发现 | 关键词丰富，更容易被搜索到 |
| 项目可信度 | 像"半成品"，不放心使用 | 像"成熟产品"，敢于依赖 |

### 1.2 一个真实的心理过程

GitHub 上有一个著名的规律：**访客点开仓库后，平均只停留几十秒**。在这几十秒里，访客会扫一眼文件列表，然后立刻去找 README。找不到的话，大多数新手会直接关闭页面；只有经验丰富的开发者才会去翻代码目录碰运气。

所以 README 的本质是"**降低理解成本**"：把"看懂这个项目"的成本从"读完所有源码"降到"读完一页文档"。这是性价比最高的一次投入。

## 2. 原理讲解：GitHub 如何识别和展示 README

### 2.1 先直观理解

你在 GitHub 上打开一个仓库主页，代码文件列表上方那块自动渲染出来的图文区域，就是 README 的"展示位"。你不需要点开任何文件，它就在那里。

### 2.2 再讲原理

GitHub 对 README 的识别有一套固定规则（官方文档明确说明）：

- README 文件名必须是 `README.md`（扩展名也可以是 `.txt`、`.markdown` 等，但 Markdown 最通用）。
- 文件放在**三个位置之一**会被自动识别展示：仓库根目录、`.github` 目录（隐藏目录）、`docs` 目录。
- 如果仓库里同时存在多个 README，展示优先级为：**`.github` 目录 > 根目录 > `docs` 目录**。
- README 渲染视图超过 **500 KiB** 的内容会被截断，所以不要把所有内容都塞进 README。
- GitHub 会根据 README 中的各级标题**自动生成目录**（网页右上角的"大纲"图标），所以善用标题层级就等于免费获得导航。
- 有一个彩蛋：如果你的用户名是 `zhangsan`，在一个公开仓库根目录放一个名为 `README.md` 且仓库名也叫 `zhangsan` 的文件，它会**自动显示在你的个人主页**上，这就是"个人主页 README"。

### 2.3 最后看示例

以本学习平台项目为例（示意）：

```mermaid
graph TD
  A["my-project/（仓库根目录）"] --> B["README.md（会被 GitHub 自动展示）"]
  A --> C[".github/"]
  C --> D["README.md（如果存在，优先展示这个）"]
  A --> E["docs/"]
  E --> F["README.md（优先级最低）"]
  A --> G["src/（源代码不影响 README 展示）"]
```

## 3. 操作示例：一份带注释的完整 README 模板

下面是一份工程实践中常见的 README 结构，每段都标注了"为什么这么写"。你可以直接复制修改。

```markdown
# 待办清单 Web 应用

<!-- 1. 徽章区：状态一览，通常用 shields.io 生成 -->
![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![Build](https://github.com/yourname/todo-app/actions/workflows/ci.yml/badge.svg)

<!-- 2. 一句话简介：回答"这是什么、为什么有用" -->
一个使用 Vue 3 + TypeScript 开发的轻量待办清单应用，
支持本地存储、拖拽排序和深浅色主题，适合个人效率管理。

<!-- 3. 功能特性：让访客快速判断是否匹配需求 -->
## 功能特性

- 任务增删改查，支持截止日期与优先级标记
- 数据自动保存到浏览器 localStorage，无需后端
- 深色/浅色主题一键切换
- 响应式布局，移动端可用

<!-- 4. 快速开始：让新手 3 分钟跑起来，必须有完整前置条件 -->
## 快速开始

### 环境要求

- Node.js 18 及以上版本
- npm 9 及以上版本

### 安装与运行

```bash
git clone https://github.com/yourname/todo-app.git
cd todo-app
npm install          # 安装依赖
npm run dev          # 启动开发服务器，默认 http://localhost:5173
```

### 使用示例

```typescript
import { createTodoStore } from 'todo-app';

const store = createTodoStore();
store.add('学习 README 写作', { priority: 'high' });
console.log(store.list()); // 输出所有待办
```

<!-- 5. 文档与帮助：大型项目把详细文档放到 Wiki 或 docs 目录 -->
## 文档

- [完整 API 文档](docs/api.md)
- [常见问题 FAQ](docs/faq.md)

<!-- 6. 贡献指南：让想帮忙的人知道怎么加入 -->
## 贡献

欢迎贡献代码、文档或反馈 Bug。请先阅读 [贡献指南](CONTRIBUTING.md)，
提交 PR 前请运行 `npm run lint` 和 `npm test`。

<!-- 7. 许可证：开源项目的法律底线，不可省略 -->
## 许可证

本项目采用 [MIT](LICENSE) 许可证。
```

### 3.4 进阶格式技巧：让 README 更好读

基础模板之上，GitHub Flavored Markdown 还提供几个高频技巧，工程实践中几乎必用：

```markdown
<!-- 1. 表格：展示功能对比、版本信息、目录 -->
| 功能 | 免费版 | 专业版 |
| :--- | :---: | :---: |
| 本地存储 | 支持 | 支持 |
| 云同步 | 不支持 | 支持 |

<!-- 2. 任务列表：展示开发进度，可勾选 -->
## 开发进度

- [x] 完成登录模块
- [x] 完成待办列表
- [ ] 完成数据导出（开发中）

<!-- 3. 折叠区块：收起长截图、日志、多版本说明 -->
<details>
<summary>点击展开：v1.0 迁移说明</summary>

1. 备份 `config.json`
2. 运行 `npm run migrate`
3. 重启服务

</details>

<!-- 4. 告警块：突出注意事项（GitHub 原生支持） -->
> [!NOTE]
> 本工具依赖 Node.js 18+，旧版本无法运行。

> [!WARNING]
> 生产环境请务必先备份数据库再升级。
```

要点：表格用于结构化对比；任务列表让进度可视化；`<details>` 折叠长内容保持首屏清爽；`> [!NOTE]` 等告警语法让"重要提醒"不被淹没。

## 4. 常见错误与对策表

新手写 README 时最容易踩的坑，整理如下：

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 忘记初始化 README | 新建仓库时没勾选"Add a README file"，主页光秃秃 | 创建仓库时默认未生成 README | 仓库首页点 Add file → Create new file，输入 `README.md` |
| 文件名写错 | README 不展示，显示为普通文本文件 | 写成 `readme.md`、`README.txt` 外的名字 | 使用 `README.md`，注意大小写 |
| 代码块没有标注语言 | 代码没有语法高亮 | 省略了 ` ```javascript ` 的标注 | 每个代码块第一行写明语言，如 ` ```python ` |
| 相对链接 404 | 图片、文档链接点开是 404 | 使用了绝对路径或错误的相对路径 | 使用 `docs/images/logo.png` 这类仓库内相对路径 |
| README 过短或过长 | 要么只有两行，要么 500 KiB 被截断 | 内容失衡 | 概览放 README，详细内容放 Wiki 或 docs 目录 |
| 忘写许可证 | 访客不敢使用你的代码 | 没有 LICENSE 文件 | README 引用 LICENSE 文件，并说明开源协议类型 |
| 代码示例不可运行 | 访客复制后直接报错 | 示例缺少上下文或依赖 | 写完后在干净环境实测一遍再发布 |

## 6. 一句话记忆

**README 就是仓库的招牌和产品说明书——用最少的文字回答"这是什么、为什么有用、怎么开始用、去哪求助、谁在维护"，让访客 30 秒内决定要不要继续了解你的项目。**

### 延伸阅读（站内文档）

- 开源许可证如何选择，见 004-github 模块《开源许可证选择》。
- 贡献指南与社区健康文件，见 004-github 模块《社区健康文件》。
- 详细文档如何组织，见 004-github 模块《Wikis》。
- 协作开发规范与分支保护，见 004-github 模块《协作开发规范》。



<!-- ============ 文档分隔线：004-github/007-BranchModelBranchRule.md ============ -->



## 0. 从一个生活场景说起：主干道与支路

想象一座城市：**主干道（main 分支）** 必须时刻畅通，任何驶入主干道的车辆（代码）都要经过**收费站（Code Review）** 和**检查站（CI 状态检查）**；**支路（feature 分支）** 是施工区，工人们（开发者）在这里安心施工；**匝道（Pull Request）** 是支路汇入主干道的入口，不合格的车辆进不了主干道；**交警（分支保护规则）** 负责强制执行这一切——禁止直接从支路冲上主干道，违者拦下。

这个"交通模型"就是**分支模型 + 分支保护规则**：先用**模型**规划"道路怎么修"，再用**保护规则**确保"车辆不能乱闯"。本篇采用**模型驱动**的结构，先讲两种主流分支模型，再讲如何用保护规则把模型强制落地。

## 1. 原理讲解：为什么要分分支

### 1.1 不分分支的代价

如果 10 个人都直接往 `main` 推送：冲突频繁、代码不可审查、main 随时处于"半成品"状态——没人敢说"main 现在可以发布"。**分支的本质是把"开发中"和"可发布"两种状态隔离在不同的"车道"上**。

### 1.2 分支模型的角色

| 概念 | 生活类比 | 作用 |
| :--- | :--- | :--- |
| main | 主干道 | 始终可部署的稳定分支 |
| feature/* | 施工支路 | 功能开发，完成后经 PR 并入主线 |
| release/* | 试运行线路 | 发布前的测试与修复 |
| hotfix/* | 应急抢险通道 | 线上紧急缺陷修复 |
| develop | 汇集线路 | 集成所有已完成功能的开发分支 |

## 2. 模型一：GitHub Flow（轻量，推荐起步）

### 2.1 核心思想

GitHub 官方推荐的模型，**只有一个长期分支 `main`**，且始终可部署：

1. 从 `main` 创建功能分支 → 2. 在功能分支开发并提交 → 3. 推送到远程 → 4. 发起 PR 审查 → 5. 合并回 `main` → 6. 合并后立即部署。

### 2.2 适用场景

持续交付的 Web 服务、中小团队、快速迭代项目。优点是简单易学、部署频率高；缺点是不适合需要长期维护多个版本的项目。

### 2.3 GitHub Flow 实操

```bash
# 1. 确保本地 main 最新
git checkout main
git pull origin main

# 2. 创建并切换到功能分支
git checkout -b feature/add-login

# 3. 开发、提交、推送
git add .
git commit -m "feat: add login"
git push -u origin feature/add-login

# 4. 在 GitHub 上创建 PR，审查合并
# 5. 合并后清理本地分支
git checkout main
git pull origin main
git branch -d feature/add-login
```

## 3. 模型二：Git Flow（完整，适合版本发布）

### 3.1 核心分支

| 分支 | 说明 |
| :--- | :--- |
| `main` | 生产环境稳定代码，只接受 release/hotfix 合并 |
| `develop` | 开发集成分支，feature 合并到这里 |
| `feature/*` | 从 develop 创建，完成后合并回 develop |
| `release/*` | 从 develop 创建，用于发布前测试，完成后合并回 main 和 develop |
| `hotfix/*` | 从 main 创建，紧急修复生产问题，完成后合并回 main 和 develop |

### 3.2 工作流程

1. 从 `develop` 创建 `feature/*` → 2. 开发完成合并回 `develop` → 3. 积累足够功能后从 `develop` 切 `release/*` → 4. 在 release 分支测试修复 → 5. 合并回 `main` 并打 tag → 6. 同时合并回 `develop` → 7. 线上紧急问题从 `main` 切 `hotfix/*` 修复。

### 3.3 Git Flow 实操

```bash
# 从 develop 创建功能分支
git checkout develop
git pull origin develop
git checkout -b feature/add-login

# 开发完成后合并回 develop
git checkout develop
git merge feature/add-login

# 准备发布
git checkout -b release/v1.0.0
# 测试修复后合并到 main 并打标签
git checkout main
git merge release/v1.0.0
git tag v1.0.0
git checkout develop
git merge release/v1.0.0

# 线上紧急热修复
git checkout main
git checkout -b hotfix/security-patch
# 修复后合并回 main 和 develop，打 tag v1.0.1
```

## 4. 模型对比：怎么选

| 特性 | GitHub Flow | Git Flow |
| :--- | :--- | :--- |
| 长期分支数量 | 1（main） | 2（main + develop） |
| 分支复杂度 | 低 | 高 |
| 学习成本 | 低 | 高 |
| 部署频率 | 高（持续部署） | 较低（版本节奏发布） |
| 多版本并行维护 | 困难 | 支持（release/hotfix） |
| 适用项目 | Web 服务、快速迭代 | 有明确发布周期的软件 |

**选择建议**：团队新起步、项目持续部署 → GitHub Flow；产品有版本节奏、需长期维护多个版本 → Git Flow。

### 4.1 其他分支策略一览

除两大主流模型外，还有两种常见策略值得了解：

| 策略 | 核心思想 | 适用场景 |
| :--- | :--- | :--- |
| Trunk-Based（主干开发） | 所有人都直接开发 main，用特性开关（feature flag）控制上线 | 高频发布、大规模团队协作 |
| Release Flow（发布流） | 在 GitHub Flow 基础上增加 release 分支管理发布周期 | 有明确发布节奏且需快速迭代的产品 |

- **Trunk-Based** 优点是无合并负担、部署频繁；缺点是依赖完善的测试与特性开关体系，不适合初学者团队。
- **Release Flow** 是 GitHub 官方在 GitHub Flow 之外推荐的另一种模式：功能开发合入 main，需要发版时从 main 切 release 分支做版本化发布。

## 5. 分支保护规则：让模型强制落地

光有模型不执行等于没有。**分支保护规则（branch protection rules）** 在 GitHub 上强制执行：

路径：仓库 **Settings → Branches → Branch protection rules → Add rule**。

### 5.1 常用规则项

| 规则 | 作用 |
| :--- | :--- |
| Branch name pattern | 匹配要保护的分支（如 `main`、`release/*`，支持 fnmatch 通配符） |
| Require a pull request before merging | 禁止直接推送，所有改动必须走 PR |
| Require approvals | 至少 N 人批准才能合并 |
| Require status checks to pass | 所有 CI 检查通过才能合并 |
| Require branches to be up to date | 合并前必须与基础分支同步 |
| Require review from Code Owners | 需要 CODEOWNERS 指定的人审查 |
| Restrict who can push | 限制谁可以直接推送 |
| Allow force pushes / deletions | 是否允许强推与删除（生产分支建议禁用） |

### 5.2 推荐配置模板

**main 分支（最严格）**：

- 必须 PR 合并 + 至少 2 人批准 + 所有状态检查通过 + 禁止强推 + 禁止删除 + 对管理员同样生效。

**develop 分支（中等）**：

- 必须 PR 合并 + 至少 1 人批准 + 状态检查通过。

**feature/* 分支（宽松）**：

- 不设保护，开发者自由操作，合并后自动删除。

> 注意：状态检查只能选**已运行过至少一次**的检查，否则下拉框里看不到该检查项；GitHub 官方也提醒，各工作流中 job 名称必须唯一，否则状态检查结果会歧义、卡住合并。

### 5.3 其他保护机制：Rulesets 与 CODEOWNERS

- **Rulesets（规则集）**：较新的替代方案，支持把多条规则打包应用于整个分支/标签，比单条保护规则更易管理。
- **CODEOWNERS**：在 `.github/025-CODEOWNERS` 中按路径指定负责人，改动该路径文件时自动要求对应负责人审查：

```gitignore
# .github/025-CODEOWNERS
# 整个仓库的默认所有者
* @maintainer
# src/ 目录需要前端团队审查
/src/ @frontend-team
# 安全相关文件必须安全负责人审查
SECURITY.md @security-lead
```

### 5.4 合并策略：与保护规则配套的最后一环

分支保护管"能不能合"，合并策略管"怎么合"，两者配套使用：

| 策略 | 历史形态 | 使用建议 |
| :--- | :--- | :--- |
| Create a merge commit | 保留全部提交 + 一个合并提交 | 需要保留完整开发过程 |
| Squash and merge | 压缩为一个提交 | 功能分支提交琐碎时最常用 |
| Rebase and merge | 线性历史，无合并提交 | 追求干净线性的提交图 |

在仓库 **Settings → General → Merge button** 中可以只开放允许的策略（例如团队统一只用 Squash）。配合保护规则中的 "Require branches to be up to date"，能保证合入 main 的代码永远基于最新主干。

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 直接推送 main 被拒 | `You are not allowed to push code to this branch` | main 开启了"必须 PR 合并"保护 | 创建功能分支 → 发起 PR → 审查通过后合并 |
| 状态检查名称不匹配 | PR 永远等不到绿灯 | Actions job 改名后保护规则仍是旧名称 | 在 PR 页面查看实际检查名称，更新保护规则 |
| 强制推送被禁止 | `You're not allowed to force push` | 保护规则禁用了 force push | 遵守规则走 PR 流程；确需强推时联系管理员评估后放开 |
| 无法批准自己的 PR | GitHub 界面无 Approve 按钮 | GitHub 不允许作者自审自批 | 邀请团队成员审查；配置 CODEOWNERS 指定审查者 |
| 保护规则不生效 | 管理员仍能绕过 | 未勾选 "Include administrators" | 在规则中勾选"对管理员同样生效" |
| 找不到所需检查项 | 状态检查下拉列表没有目标项 | 该检查从未运行过 | 先推送代码让检查运行一次，之后即可勾选为 required |

## 8. 一句话记忆

**分支模型决定"路怎么修"（GitHub Flow 轻、Git Flow 全），分支保护决定"车怎么管"（PR 是收费站，CI 是检查站，强推与直推都被拦下），模型 + 规则共同保证 main 始终安全可用。**

### 延伸阅读

- 分支命令操作速查（创建/切换/删除/重命名），见 037-045 篇 Git 模块文档。
- 团队协作规范（提交信息/PR 模板/审查清单），见 005 篇《协作开发规范》。
- 代码所有者自动分配审查，见 025 篇《CODEOWNERS》。



<!-- ============ 文档分隔线：004-github/008-GitignoreConfig.md ============ -->



## 0. 先来一个生活场景：搬家打包清单

假设你要搬家。搬家师傅给你一个大箱子，让你把所有东西装进去。你会怎么做？

- 你不会把**垃圾桶里的果皮纸屑**装进去——那是垃圾，随时可以再产生。
- 你不会把**旧快递盒、旧报纸**装进去——它们占了大量空间却没有价值。
- 你更不会把**写了银行卡密码的纸条**装进去——万一箱子丢了，后果不堪设想。
- 但你一定会在箱子里放一份**搬家清单**，告诉师傅"哪些东西不要装箱"。

`.gitignore` 就是 Git 仓库的"搬家清单"。它是一份**排除清单**，明确告诉 Git："这个箱子（仓库）里，哪些文件不要追踪、不要提交、不要推到 GitHub 上"。

Git 默认会追踪目录里的所有文件。如果你不做任何声明，`node_modules`（几十万个依赖文件）、`__pycache__`（Python 缓存）、`.env`（含数据库密码的环境变量）都会被一股脑推送到 GitHub。这就好比把垃圾、旧报纸和密码纸条都装进了搬家箱。

本篇文章将按照"**清单**"的思路组织：先列出"什么东西不该装箱"（文件类型），再教你"怎么写清单"（语法），然后讲"多张清单谁说了算"（优先级），最后给出"现成的清单模板"。

## 1. 先列清单：应该忽略的文件类型

在动手写 `.gitignore` 之前，先搞清楚"什么文件不该进仓库"。下表是新手最常遇到的 7 大类：

| 类型 | 示例 | 为什么要忽略 |
| :--- | :--- | :--- |
| **构建产物** | `dist/`、`build/`、`*.class` | 由源代码编译生成，任何时刻都可以重新构建 |
| **依赖目录** | `node_modules/`、`vendor/`、`.venv/` | 体积巨大（可达几十万个文件），且可通过 `npm install` 等命令恢复 |
| **环境配置** | `.env`、`config.local.js`、`secrets.json` | 通常包含数据库密码、API 密钥等敏感信息 |
| **IDE 配置** | `.idea/`、`.vscode/`、`*.iml` | 属于个人编辑器偏好，不同开发者配置不同 |
| **系统文件** | `.DS_Store`、`Thumbs.db` | 操作系统自动生成的缩略图/元数据文件 |
| **日志文件** | `*.log`、`logs/` | 运行时产生，内容动态变化 |
| **临时文件** | `*.tmp`、`*.swp`、`*~` | 编辑器或程序崩溃留下的临时残留 |

### 1.1 一个记忆口诀

> **"能再生的、能重装的、不能给别人看的、别人不需要的——都不要装箱。"**

- 能再生：构建产物（dist/build）。
- 能重装：依赖目录（node_modules 一条命令就能装回来）。
- 不能给别人看：密钥、密码、Token。
- 别人不需要：你的 IDE 设置、操作系统缓存。

### 1.2 直观理解：一个 Node.js 项目装箱前 vs 装箱后

```mermaid
flowchart LR
  subgraph before["项目目录（未配置 .gitignore）"]
    direction TB
    B1["package.json"]
    B2["package-lock.json"]
    B3["src/"]
    B4["node_modules/（5万+文件）"]
    B5["dist/（编译产物）"]
    B6[".env（数据库密码）"]
    B7[".vscode/"]
  end
  subgraph after["项目目录（已配置 .gitignore）"]
    direction TB
    A1["package.json"]
    A2["package-lock.json"]
    A3["src/"]
    A4[".gitignore"]
  end
```

右侧才是"干净"的仓库：只有源代码、配置文件清单和 `.gitignore` 本身。任何协作者克隆后执行 `npm install` 即可恢复完整环境。

## 2. 怎么写清单：语法规则详解

`.gitignore` 是一个纯文本文件，每行一条规则。Git 官方手册（gitignore(5)）对语法有精确的定义，下面按"先直观、后原理、再示例"的方式讲解。

### 2.1 最基本的五条规则

```gitignore
# 注释以 # 开头（这是注释行）

# 规则1：忽略所有 .log 结尾的文件（匹配任意目录层级）
*.log

# 规则2：忽略 node_modules 目录（目录名后带斜杠，只匹配目录）
node_modules/

# 规则3：忽略根目录下的 .env 文件
/.env

# 规则4：忽略特定文件
config.local.json

# 规则5：取反——前面忽略了所有 .log，但 debug.log 例外，要保留
!debug.log
```

逐条拆解：

| 写法 | 含义 | 原理说明 |
| :--- | :--- | :--- |
| `*.log` | 忽略所有 `.log` 文件 | `*` 匹配任意多个字符（但不能跨目录层级） |
| `node_modules/` | 忽略所有名为 node_modules 的目录 | **结尾带斜杠**表示只匹配目录 |
| `/.env` | 只忽略仓库根目录的 `.env` | **开头带斜杠**表示锚定在 `.gitignore` 所在目录 |
| `!debug.log` | 例外保留 debug.log | `!` 开头表示取反（negation），必须放在对应忽略规则**之后** |
| `config.local.json` | 忽略任意层级的同名文件 | 不带斜杠的模式会匹配所有层级 |

### 2.2 进阶：Glob 通配符

`.gitignore` 的匹配规则与 Git 的 fnmatch 机制一致，支持以下通配符：

| 模式 | 含义 | 示例 | 匹配结果 |
| :--- | :--- | :--- | :--- |
| `*` | 匹配任意字符（不含 `/`） | `*.js` | `a.js`、`b/c.js`（后者在 `src/b/c.js` 这种场景下会匹配任意层级的 .js） |
| `**` | 匹配任意层级目录 | `**/temp/` | `temp/`、`src/temp/`、`src/a/b/temp/` |
| `?` | 匹配单个字符（不含 `/`） | `file?.txt` | `file1.txt`，不匹配 `file10.txt` |
| `[abc]` | 匹配括号内任一字符 | `file[123].txt` | `file1.txt`、`file2.txt` |
| `[0-9]` | 匹配字符范围 | `file[0-9].txt` | `file0.txt` ~ `file9.txt` |
| `\` | 转义特殊字符 | `\#important.txt` | 匹配字面的 `#important.txt` |

### 2.3 进阶：`**` 的三种位置

`**` 是新手最容易用错的通配符，Git 官方文档给出了精确语义：

```gitignore
# 场景1：开头 —— 匹配任意层级下的 foo 目录
**/foo

# 场景2：中间 —— 匹配 a 与 b 之间任意层级
a/**/b        # 匹配 a/b、a/x/b、a/x/y/b

# 场景3：结尾 —— 等价于普通星号，匹配该层全部内容
abc/**        # 等价于 abc/ 下的所有内容
```

### 2.4 最容易踩的坑：`!` 取反的"父目录陷阱"

Git 官方文档明确指出：**如果父目录被忽略，那么子目录的取反规则无效**。

```gitignore
# 错误示范：忽略了 build/ 目录，又想保留其中的 important.js
build/
!build/important.js    # 不会生效！

# 正确写法：不忽略目录本身，只忽略目录里的内容
build/*
!build/important.js    # 生效
```

原理：Git 出于性能考虑不会列出被忽略的目录，因此目录内部的规则根本不会被检查。要想保留子文件，必须让父目录"可见"。

## 3. 多张清单：优先级规则

你的仓库里可能同时存在多份规则来源。Git 检查忽略规则时按以下优先级从高到低排列（来源级别高的覆盖级别低的；**同一级别内，后写的规则覆盖先写的**）：

| 优先级 | 来源 | 说明 |
| :--- | :--- | :--- |
| 1（最高） | 命令行规则 | 如 `git ls-files --exclude` 传入的模式，仅本次命令生效 |
| 2 | 目录层级中的 `.gitignore` | **越深的目录优先级越高** |
| 3 | `$GIT_DIR/info/exclude` | 仓库本地规则，不随 clone 分发 |
| 4（最低） | `core.excludesFile` 全局文件 | 对所有仓库生效 |

```mermaid
flowchart TD
    T0[".gitignore（仓库根目录）"]
    T1["src/.gitignore（src 目录，优先级更高）"]
    T2["src/utils/.gitignore（更深层，优先级最高）"]
    T3["info/exclude（仓库本地）"]
    T4["全局 .gitignore_global（所有仓库）"]
    T0 --> T3
    T3 --> T4
```

### 3.1 深层 .gitignore 覆盖浅层的例子

```gitignore
# 仓库根目录 .gitignore：忽略所有 .md
*.md

# src/.gitignore：src 目录下保留 README.md
!README.md
```

效果：`根目录/README.md` 被忽略；`src/README.md` 由于 `src/.gitignore` 的取反规则生效，被正常追踪。同一目录内，规则按**自上而下**顺序判断，**后写的覆盖先写的**。

## 4. 直接抄作业：常用模板

GitHub 官方维护了一个模板仓库 [github/gitignore](https://github.com/github/gitignore)，收录了 100+ 种语言和工具的模板。以下三个模板是使用率最高的。

### 4.1 Node.js 项目模板

```gitignore
# 依赖
node_modules/

# 构建产物
dist/
build/

# 环境变量（绝对不要提交真实密钥！）
.env
.env.local
.env.*.local

# 日志
logs/
*.log
npm-debug.log*

# 测试覆盖率
coverage/
.nyc_output/

# 编辑器
.vscode/
.idea/
```

### 4.2 Python 项目模板

```gitignore
# 字节码缓存
__pycache__/
*.py[cod]

# 虚拟环境
.venv/
venv/
env/

# 打包产物
dist/
build/
*.egg-info/

# 环境变量
.env

# 测试与类型检查缓存
.pytest_cache/
.mypy_cache/
.ruff_cache/
```

### 4.3 Java 项目模板（Maven + IntelliJ IDEA）

```gitignore
# 编译产物
*.class
*.jar
*.war

# 构建目录
/target/
/build/

# IDE 配置
.idea/
*.iml
*.ipr
*.iws
.vscode/

# 系统文件
.DS_Store
Thumbs.db
```

### 4.4 下载官方模板的三种方式

```bash
# 方式1：GitHub 官方模板库（推荐）
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore

# 方式2：GitHub 官方 API
curl -L https://api.github.com/gitignore/templates/Java

# 方式3：gitignore.io 组合生成器（多技术栈组合）
# 浏览器打开 https://www.toptal.com/developers/gitignore/api/java,maven,intellij
```

## 5. 亡羊补牢：已跟踪文件的处理

`.gitignore` 有一个新手必须知道的特性：**它只对"尚未被跟踪"的文件生效**。如果一个文件已经被 `git commit` 过，再把它写进 `.gitignore` 也不会让 Git 停止跟踪它。

### 5.1 停止跟踪但保留本地文件

```bash
# 从版本控制中移除（本地文件保留在磁盘上）
git rm --cached .env
git rm --cached -r node_modules/

# 提交这次移除
git commit -m "chore: 停止跟踪敏感与依赖文件"

# 之后正常推送
git push
```

### 5.2 临时忽略已跟踪文件的修改

某些场景（例如本地配置文件随环境变化）不需要从仓库移除文件，只想让 Git 忽略它的改动：

```bash
# 临时忽略 config.local.js 的修改
git update-index --assume-unchanged config.local.js

# 查看哪些文件被标记了
git ls-files -v | grep '^h'

# 恢复跟踪修改
git update-index --no-assume-unchanged config.local.js
```

### 5.3 验证忽略是否生效

```bash
# 查看哪些文件会被忽略（不真正删除）
git status --ignored

# 只查看被忽略的文件列表
git status --ignored --short

# 检查某个特定文件是否被忽略（0 表示会跟踪，1 表示被忽略）
git check-ignore -v .env
# 输出示例：.gitignore:2:/.env  .env
# 格式：来源文件:行号:规则  目标文件
```

`git check-ignore -v` 是排查"为什么这个文件被忽略了"的利器，它会告诉你命中了哪一行规则。

## 6. 全局配置：一份清单管所有仓库

操作系统文件（`.DS_Store`、`Thumbs.db`）和 IDE 配置（`.idea/`、`.vscode/`）几乎在每一个仓库都会被忽略。与其在每个仓库重复写，不如配置一份**全局忽略文件**。

### 6.1 Windows 配置全局忽略

```powershell
# 创建全局忽略文件（路径可自定义）
New-Item $env:USERPROFILE\.gitignore_global -ItemType File

# 配置 Git 使用它
git config --global core.excludesfile "$env:USERPROFILE\.gitignore_global"
```

### 6.2 macOS / Linux 配置全局忽略

```bash
touch ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

### 6.3 全局忽略文件推荐内容

```gitignore
# 操作系统生成文件
.DS_Store
Thumbs.db
desktop.ini

# 编辑器临时文件
.idea/
.vscode/
*.swp
*.swo
*~
```

## 7. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 明明写了 `node_modules/`，`git push` 还是把依赖推上去了 | 仓库里能看到 `node_modules` | 文件在添加 `.gitignore` **之前**已被提交跟踪 | 执行 `git rm --cached -r node_modules/` 再提交 |
| `!important.log` 写在 `*.log` 前面，取反不生效 | important.log 仍被忽略 | 取反规则必须写在对应的忽略规则**之后** | 调整顺序：先 `*.log` 后 `!important.log` |
| 忽略了 `build/` 又想保留 `build/hot.js`，取反无效 | 子文件仍被忽略 | 父目录被忽略后 Git 不会检查其内部规则 | 改用 `build/*` + `!build/hot.js` |
| 在 `.gitignore` 里写了 `/temp/`，其他目录的同名文件也被忽略了 | 表现不一致 | 对 `/temp/`（锚定根目录）与 `temp/`（匹配所有层级）的理解混淆 | 记住：**开头斜杠 = 锚定当前层级**，不带斜杠 = 匹配所有层级 |
| `.env` 里的密钥还是被推送了，事后才发现 | 安全事故 | 忽略了 `.env` 但密钥硬编码在 `src/config.js` 中 | 全局搜索密钥（`git grep "sk_live"`），轮换密钥，并使用环境变量 + GitHub Secrets |
| `git status` 不显示某文件，但 `git add` 报错 | `The following paths are ignored by one of your .gitignore files` | 想添加一个被忽略的文件 | 确认是否真的要添加；若要添加，用 `git add -f 文件名` 强制添加，或调整忽略规则 |

## 9. 一句话记忆

> **`.gitignore` 就是仓库的"搬家清单"——只列"不装什么"：能再生的构建产物、能重装的依赖、不能给别人看的密钥，以及别人不需要的 IDE 和系统文件。**

### 官方文档

- Git 官方手册 gitignore(5)：https://git-scm.com/docs/gitignore
- GitHub 官方模板库 github/gitignore：https://github.com/github/gitignore
- GitHub 文档（中文）：https://docs.github.com/zh
- gitignore.io 组合模板生成器：https://www.toptal.com/developers/gitignore

### 延伸阅读
- 分支模型与分支保护规则，见 004-github 模块 007 文档。
- 开源许可证选择（LICENSE 文件的管理思路与 .gitignore 类似），见 004-github 模块 009 文档。
- 依赖安全选项（锁定文件与 Dependabot 的配合使用），见 004-github 模块 010 文档。
- Git 协作基础（git add / commit / push 流程），见 003-git 模块。



<!-- ============ 文档分隔线：004-github/009-OpenSourceLicense.md ============ -->



## 0. 先来一个生活场景：作品版权授权合同

你写了一首歌，把它发到网上，希望别人能唱。但你需要先回答三个问题：

- 别人**可不可以拿去卖钱**（商业使用）？
- 别人**改了歌词**再唱，算不算侵权（修改与衍生）？
- 别人用你的歌做了个翻唱专辑，**专辑里的其他歌**要不要也归你管（传染性）？

如果你什么都不说，法律默认"**保留所有权利**"——任何人都不能合法地复制、修改、分发你的作品。如果你想说"大家随便用，但有几条规矩"，你就需要一份**授权合同**。

在开源世界里，这份"授权合同"就叫**开源许可证（Open Source License）**。你发布代码时附上一份许可证，就相当于说："这份作品我授权大家使用，使用条件如下。"

GitHub 官方文档明确指出：**没有许可证的公开仓库，默认适用版权法——你保留源代码的所有权利，任何人都不得复制、分发或创作衍生作品**。你如果希望代码真正"开源"，就必须选择并添加一份许可证。

本文采用**对比驱动**的结构：先用一张总表对比 MIT / Apache 2.0 / GPL 三大类许可证，再逐一详解，最后给出"怎么选"的决策方法。

## 1. 先搞懂原理：为什么"公开"不等于"开源"

### 1.1 直观理解：三步递进

1. **把代码公开在 GitHub 上**：别人能看、能 fork。但 fork 不等于能随便用——fork 只是"复制了一份到我这里"。
2. **没有许可证**：从法律上讲，任何人使用你的代码（包括商业使用、修改后发布）都可能侵权。
3. **加上许可证**：你主动授予使用、修改、分发等权利，同时可以附加条件（比如保留版权声明、衍生作品必须开源）。

### 1.2 原理：许可证的本质是"权利授予"

许可证的本质是版权人（你）对使用者（全世界）的**单方授权**。它回答三类问题：

| 问题 | 对应许可证条款 |
| :--- | :--- |
| 能不能用？ | 使用权（Use） |
| 能不能改？ | 修改权（Modify） |
| 能不能给别人？ | 分发权（Distribute） |

不同许可证对这三类权利附加的条件不同，于是形成了"宽松"与"传染"两大阵营。

## 2. 一张总表：三大类许可证对比

这是全文的核心。先看总表，再逐项解释：

| 特性 | MIT | Apache 2.0 | GPL v3 | AGPL v3 |
| :--- | :---: | :---: | :---: | :---: |
| 商业使用 | 允许 | 允许 | 允许 | 允许 |
| 自由修改 | 允许 | 允许 | 允许 | 允许 |
| 自由分发 | 允许 | 允许 | 允许 | 允许 |
| 闭源分发 | 允许 | 允许 | **禁止**（必须开源） | **禁止** |
| 专利授权 | 无 | **有**（明确条款） | 有（条款） | 有（条款） |
| 网络服务（SaaS）需开源 | 否 | 否 | 否 | **是** |
| 衍生作品必须开源 | 否 | 否 | **是** | **是** |
| 必须保留版权声明 | 是 | 是 | 是 | 是 |
| 修改需声明变更 | 否 | **是** | 是 | 是 |
| 附带 NOTICE 文件 | 否 | 建议 | 否 | 否 |

### 2.1 直观理解：用"授权程度"排一条线

```
最宽松 ────────────────────────────────────────→ 最严格
MIT    <  Apache 2.0   <   GPL v3   <   AGPL v3
自由     多专利保护      传染性        网络也算分发
```

- **MIT**：你用我的代码，只要保留我的版权声明，其他随便。
- **Apache 2.0**：MIT 基础上加**专利授权**和**变更声明**条款，适合企业。
- **GPL**：你的程序只要**分发**了，就必须以 GPL 提供源代码（"传染"）。
- **AGPL**：连**通过网络提供服务**（SaaS）也算分发，也必须开源。

### 2.2 原理：什么是"传染性"（Copyleft）

"传染"这个词来自 Copyleft 理念，是 GPL 的核心设计。它的意思是：如果你分发一个**基于 GPL 代码修改而来**的作品，那么你的衍生作品也必须采用 GPL 许可证，把源代码开放给下游使用者。

反过来说，MIT 这类宽松许可证没有传染性：你可以把 MIT 代码嵌入闭源商业软件，无需开放你的代码。

## 3. 许可证详解

### 3.1 MIT License：程序员最爱的"佛系"许可证

**核心条款**（全文极短，约 170 字）：

```
Copyright (c) <年份> <版权人>

特此免费授予任何获得本软件及关联文档（下称"软件"）副本的人，
不受限制地处理本软件的权利，包括但不限于使用、复制、修改、合并、
发布、分发、再许可和/或销售软件的副本，并允许向其提供软件的人
这样做，但须满足以下条件：

上述版权声明和本许可声明应包含在本软件的所有副本或实质性部分中。

本软件按"现状"提供，不作任何明示或默示的担保……
```

**要点总结**：

- 允许：商业使用、修改、分发、闭源使用、再授权。
- 唯一要求：**保留版权声明和许可证文本**。
- 不提供：专利保护、担保。

**适用场景**：个人项目、工具库、希望最大范围传播的代码。React、jQuery、Vue 等知名项目都采用 MIT。

### 3.2 Apache License 2.0：企业级"商务精英"许可证

在 MIT 基础上增加三块内容：

| 新增内容 | 含义 |
| :--- | :--- |
| **专利授权（Grant of Patent License）** | 贡献者自动授予使用者专利许可，明确"你用了我的代码不会被我告专利侵权" |
| **变更声明（NOTICE）** | 修改衍生作品时，需在 NOTICE 文件中声明你做了哪些修改 |
| **商标保护** | 明确许可证**不**授予商标使用权 |

**要点总结**：

- 包含 MIT 的全部权利。
- 专利授权条款保护使用者免受专利诉讼。
- 要求保留版权声明 + 声明变更 + 附 NOTICE 文件（如有）。

**适用场景**：企业级项目、涉及专利风险的项目。Kubernetes、TensorFlow、Android 相关项目大量采用 Apache 2.0。

### 3.3 GPL v3：自由软件运动的"理想主义"许可证

**核心逻辑**：GPL 关注的是"分发"环节。

- 你可以商业使用、修改、分发 GPL 代码。
- 但**分发**衍生作品时，必须以 GPL 提供完整源代码。
- GPL v3 还加入反 Tivoization（禁止硬件锁定）条款和专利授权条款。

**要点总结**：

- 传染性：衍生作品必须 GPL。
- 不能闭源分发：分发时必须提供源码。
- 允许内部使用不触发开源义务（只要不分发）。

**适用场景**：希望代码及其衍生作品永远开源的项目。Linux、Git、WordPress 采用 GPL。

### 3.4 AGPL v3：面向 SaaS 时代的"网络增强版" GPL

GPL 有一个著名的"漏洞"：如果你的软件部署为**网络服务**（用户通过浏览器使用，不"分发"代码副本），则不需要开源。AGPL v3 堵上了这个漏洞：

- 继承 GPL v3 全部条款。
- **通过网络提供服务 = 分发**：只要别人能通过网络使用你的 AGPL 代码，你就必须开放源码。

**适用场景**：SaaS 服务、防止云厂商白嫖闭源的场景。MongoDB（旧版）等曾使用 AGPL。

### 3.5 顺带一提：BSD 与 LGPL

| 许可证 | 一句话说明 | 典型项目 |
| :--- | :--- | :--- |
| BSD 3-Clause | 与 MIT 类似，额外要求"不得用作者名义背书" | Nginx、FreeBSD |
| LGPL | 库的"温和版 GPL"：修改库本身才需开源，动态链接使用不受传染 | FFmpeg、GTK |

## 4. 怎么选：决策方法

### 4.1 决策树：三个问题搞定选择

```mermaid
flowchart TD
    T0["你要回答：希望别人如何使用你的代码？"]
    T1["任意使用，包括闭源商用"]
    T2["任意使用，但担心专利风险"]
    T3["衍生作品必须开源"]
    T4["网络服务（SaaS）也必须开源"]
    R1["选 MIT"]
    R2["选 Apache 2.0"]
    R3["选 GPL v3"]
    R4["选 AGPL v3"]
    T0 --> T1 --> R1
    T0 --> T2 --> R2
    T0 --> T3 --> R3
    T0 --> T4 --> R4
```

### 4.2 按项目类型速查

| 项目类型 | 推荐许可证 | 理由 |
| :--- | :--- | :--- |
| 工具库 / SDK | MIT | 最大程度推广，降低商业采用门槛 |
| 框架 | MIT 或 Apache 2.0 | 便于大厂闭源集成（如 Vue 选 MIT 收获生态） |
| 应用程序 | GPL v3 | 防止竞争对手闭源分叉 |
| SaaS / 云服务 | AGPL v3 | 防止云厂商闭源白嫖 |
| 企业内项目 | Apache 2.0 | 专利保护 + 变更声明管理 |
| 学术 / 机构 | BSD 3-Clause | 禁止用作者名义背书，风格保守 |

### 4.3 官方决策工具

GitHub 官方维护了 **choosealicense.com**，用交互式问答帮你选择许可证。步骤：打开网站 → 回答 4-5 个问题 → 获得推荐。选型时建议同时查阅 SPDX 许可证清单（https://spdx.org/licenses/）确认许可证的规范化标识符（如 `MIT`、`Apache-2.0`、`GPL-3.0-only`）。

## 5. 在 GitHub 上添加许可证

### 5.1 方式一：创建仓库时直接选择（推荐新手）

创建新仓库时，在 "Add a license" 下拉列表中选择许可证，GitHub 会自动在仓库根目录生成对应的 `LICENSE` 文件，并自动填入年份与用户名。

### 5.2 方式二：为已有仓库添加（Web 界面）

1. 进入仓库主页，点击 "Add file" → "Create new file"。
2. 文件名输入 `LICENSE`（大小写均可，行业惯例大写）。
3. 此时右侧会出现 "Choose a license template" 按钮，点击进入模板选择页。
4. 选择许可证模板（如 MIT License），GitHub 自动填充 `[year]` 与 `[fullname]`。
5. 点击 "Commit changes" 提交。

### 5.3 方式三：命令行添加

```bash
# 从 GitHub 官方 choosealicense 仓库下载 MIT 模板
curl -o LICENSE https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/mit.txt

# 打开 LICENSE，把 [year] 和 [fullname] 替换为实际年份与姓名
# 例如：Copyright (c) 2026 Zhang San

git add LICENSE
git commit -m "docs: 添加 MIT 许可证"
git push
```

### 5.4 在项目配置中声明许可证

除了 LICENSE 文件，还应在生态配置中声明（GitHub 会根据配置文件自动识别）：

```json
// package.json（npm 项目）
{
  "name": "my-lib",
  "version": "1.0.0",
  "license": "MIT"
}
```

```toml
# pyproject.toml（Python 项目）
[project]
name = "my-lib"
version = "1.0.0"
license = { text = "MIT" }
```

### 5.5 搜索与识别

- **按许可证搜索仓库**：GitHub 搜索框支持 `license:mit` 限定符，如 `topic:chatbot license:mit`。
- **许可证识别**：GitHub 会自动检测仓库根目录的 LICENSE 文件并在仓库首页显示许可证徽章；若使用 SPDX 标识符（如 `License: MIT`）声明，识别更准确。

## 6. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 以为"公开 = 开源"，仓库没有 LICENSE | 仓库首页无许可证徽章，他人不敢使用 | 没有许可证时默认"保留所有权利" | 按第 5 节添加 LICENSE 文件 |
| 直接复制了别人项目里的 LICENSE | 许可证上的版权人还是原作者 | LICENSE 文本中保留了他人的版权声明 | 使用官方模板，把 `[year]`、`[fullname]` 替换为自己 |
| 选择了 GPL 却希望他人能闭源使用 | 有用户反馈"无法闭源集成" | GPL 有传染性，与需求冲突 | 若希望被广泛闭源使用，改用 MIT 或 Apache 2.0 |
| LICENSE 文件名写错 | GitHub 不识别许可证 | 文件名应为 `LICENSE`、`LICENSE.txt`、`LICENSE.md` 等标准命名 | 重命名为标准文件名，放在仓库根目录 |
| 项目里用了 GPL 依赖却未开源自己的代码 | 法律风险 / 下游投诉 | GPL 传染性要求衍生作品开源 | 评估依赖许可证；无法满足则替换依赖或咨询法务 |
| 改了别人 MIT 代码却不保留版权声明 | 违反 MIT 唯一硬性要求 | 分发副本必须包含原版权声明和许可证文本 | 在代码头部或 LICENSE 中保留原作者声明 |

## 8. 一句话记忆

> **许可证是开源代码的"授权合同"——MIT 随便用只要留名，Apache 再加专利保护，GPL 改了必须开源，AGPL 连网络服务也要开源；不写许可证，默认就是"版权所有，翻版必究"。**

### 官方文档

- GitHub 官方文档：为仓库添加许可证：https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- 许可证选择工具 choosealicense.com：https://choosealicense.com/
- Open Source Guide（法律与许可证指南）：https://opensource.guide/legal/
- SPDX 许可证清单：https://spdx.org/licenses/

### 延伸阅读
- Gitignore 配置（仓库内其他关键配置文件的写法），见 004-github 模块 008 文档。
- 依赖安全选项（许可证合规是依赖审查的一环），见 004-github 模块 010 文档。
- Fork 工作流（fork 与许可证的兼容性问题），见 004-github 模块 011 文档。



<!-- ============ 文档分隔线：004-github/010-DependencySecurityOptions.md ============ -->



## 0. 先来一个生活场景：家庭安防系统

假设你家装了一套安防系统，它由四道防线组成：

1. **监控摄像头（看清家里有什么）**：进门先知道家里有哪些物品、哪些是别人送的。
2. **烟雾报警器（发现隐患）**：一旦检测到起火苗头，立刻拉响警报。
3. **自动灭火器（快速处置）**：警报响的同时，自动喷淋灭火，不用等你手动操作。
4. **门禁检查（防止带危险品进门）**：每次有人进门，先检查他带进来的东西是否安全。

现代软件的"家"也一样。你写的代码很少是 100% 原创——npm、pip、Maven 等包管理器会帮你引入几百甚至上千个**依赖包**。GitHub 工程师曾做过一个实验：一个只有 **21 个直接依赖**的项目，展开传递依赖后竟有 **1000 个依赖**。你的程序里 95%~97% 的代码其实是别人的代码。

问题来了：**如果某个依赖包被植入恶意代码，或者被发现存在安全漏洞，你的项目就跟着遭殃**。这种攻击方式叫**供应链攻击（Supply Chain Attack）**——攻击者不打你的房子，而是打你"进货的渠道"。

GitHub 为此提供了一整套"家庭安防系统"。本文按**原理驱动**的结构讲解：先讲清供应链攻击为什么可怕（原理），再讲 GitHub 的四道防线如何协同工作（组合），最后给出手把手的配置操作。

## 1. 原理：为什么"别人的代码"会威胁到你

### 1.1 直观理解：什么是依赖

```json
// package.json 中声明的依赖
{
  "dependencies": {
    "express": "^4.18.0",   // 直接依赖：你直接引用的框架
    "lodash": "^4.17.21"
  }
}
```

- **直接依赖**：你在清单文件里明确写下的包（如 express）。
- **传递依赖（间接依赖）**：express 自己依赖的包、那些包再依赖的包……形成一个依赖树。

GitHub 官方将你的项目及其所有依赖的集合称为**软件供应链（Software Supply Chain）**。

### 1.2 原理：供应链攻击的三条路径

| 攻击路径 | 攻击手法 | 典型后果 |
| :--- | :--- | :--- |
| **漏洞利用** | 依赖包存在已知安全漏洞（CVE），攻击者利用它入侵你的应用 | 数据泄露、服务器被控制 |
| **恶意包投毒** | 攻击者发布名称相似（typosquatting）或已被攻陷的恶意包，诱导你安装 | 植入木马、窃取环境变量中的密钥 |
| **维护者失守** | 依赖包的维护者账号被盗，往正规包里注入后门 | 下游所有使用者中招 |

三条路径的共性：**问题出在你的供应链上，而不是你的代码里**。这也是"依赖安全"与"代码安全"的本质区别——你无法审查每一个依赖的每一行代码，必须依靠工具来持续监控。

### 1.3 直观理解：Log4j 事件

2021 年底爆发的 Log4Shell 漏洞（CVE-2021-44228）是教科书级案例：Java 日志库 Log4j 的一个功能存在远程代码执行漏洞，攻击者只需发送一段特殊字符串即可控制服务器。全球无数 Java 应用因传递依赖引入了 Log4j 而中招，修复工作持续了数月。它的教训是：**你甚至可能不知道自己用了 Log4j**——它可能是某个依赖的依赖的依赖。

## 2. GitHub 依赖安全功能矩阵：四道防线

| 功能 | 对应"安防系统" | 作用 | 免费可用范围 |
| :--- | :--- | :--- | :--- |
| **Dependency Graph（依赖图谱）** | 监控摄像头 | 看清全部直接/传递依赖及漏洞信息 | 所有仓库 |
| **Dependabot Alerts（漏洞告警）** | 烟雾报警器 | 发现依赖漏洞后自动告警 | 所有仓库 |
| **Dependabot Security Updates（安全更新）** | 自动灭火器 | 针对漏洞自动创建修复 PR | 所有仓库 |
| **Dependency Review（依赖审查）** | 门禁检查 | 在 PR 合并前检查新增依赖的安全性 | 组织仓库（启用后） |

四道防线的**依赖关系**：依赖图谱是地基，其他三个功能都依赖它提供的数据。GitHub 官方供应链安全文档明确：Dependency review 与 Dependabot alerts 都使用依赖图谱的信息进行交叉比对。

## 3. 第一道防线：依赖图谱（Dependency Graph）

### 3.1 原理：它是怎么"看清"你的依赖的

依赖图谱自动解析仓库中的**清单文件（manifest）**与**锁定文件（lockfile）**，构建出依赖关系图：

- 清单文件：`package.json`、`requirements.txt`、`pom.xml`、`go.mod` 等（声明直接依赖）。
- 锁定文件：`package-lock.json`、`Pipfile.lock`、`go.sum` 等（锁定精确版本，含传递依赖）。

当你在默认分支推送修改清单/锁定文件的提交时，依赖图谱自动更新。

### 3.2 支持的主要生态系统

| 生态系统 | 清单文件 | 锁定文件 |
| :--- | :--- | :--- |
| npm / yarn | `package.json` | `package-lock.json` / `yarn.lock` |
| pip | `requirements.txt` / `Pipfile` | `Pipfile.lock` |
| Maven | `pom.xml` | — |
| Gradle | `build.gradle` | — |
| Go | `go.mod` | `go.sum` |
| Cargo | `Cargo.toml` | `Cargo.lock` |
| NuGet | `*.csproj` / `packages.config` | — |
| GitHub Actions | 工作流文件 | — |
| Docker | `Dockerfile` | — |

### 3.3 操作：查看与启用依赖图谱

```
仓库 → Insights（洞察）→ Dependency graph
```

- 公开仓库默认启用。
- 私有仓库可在 Settings → Code security and analysis 中启用。
- 图谱页面会显示：直接依赖、传递依赖、每个依赖的版本、已知漏洞标记（红色徽章）。

### 3.4 最佳实践：提交锁定文件

```bash
# npm 项目：务必提交 package-lock.json
git add package-lock.json && git commit -m "chore: 提交锁定文件"

# 好处：依赖图谱能精确解析版本；Dependabot 能精确定位受影响的依赖
```

不提交锁定文件是新手最常见的错误——依赖图谱无法确定实际安装版本，告警也会失去精确性。

## 4. 第二道防线：Dependabot Alerts（漏洞告警）

### 4.1 原理：告警是怎么产生的

```
GitHub Advisory Database（漏洞数据库）
        ↓ 与依赖图谱中的依赖交叉比对
发现：你的依赖 X 的版本 v1.2.0 存在 CVE-2024-xxxxx
        ↓
生成 Dependabot Alert（在 Security 选项卡显示）
```

Dependabot 持续监控 GitHub Advisory Database 和其他漏洞源。**触发告警的时机**：

- 新漏洞被披露并进入数据库时。
- 漏洞信息更新（严重性、受影响版本范围变化）时。
- 依赖图谱变化导致新引入漏洞时。

### 4.2 告警内容示例

Dependabot Alert 页面会展示：

- 受影响的依赖名称与版本范围。
- 漏洞描述与 CVSS 严重性评分（如 7.2 High）。
- 受影响的路径（哪个直接依赖带入了它）。
- 修复建议：升级到哪个版本。

### 4.3 操作：启用与查看

1. 仓库 Settings → Code security and analysis。
2. 找到 Dependabot alerts，点击 Enable。
3. 查看：仓库 → Security → Dependabot。

### 4.4 设置通知

告警默认通过邮件/网页通知。可在 Settings → Notifications 中调整接收方式与频率。

## 5. 第三道防线：Dependabot Security Updates（自动安全更新）

### 5.1 原理：从"发现"到"修复"的自动化

发现漏洞后，Dependabot 不会只报警，它会直接创建一个 **Pull Request** 把依赖升级到安全版本：

```markdown
# Dependabot 自动创建的 PR 标题与说明示例

## Bump lodash from 4.17.15 to 4.17.21

修复以下漏洞：
- CVE-2021-23337: Command injection（命令注入）
- CVE-2020-28500: ReDoS vulnerability（正则拒绝服务）

CVSS Score: 7.2 (High)
```

你只需要审查并合并这个 PR，无需手动改版本号。

### 5.2 操作：启用安全更新

1. 仓库 Settings → Code security and analysis。
2. 找到 Dependabot security updates，点击 Enable。
3. 之后每个相关漏洞都会自动生成修复 PR。

### 5.3 使用配置文件微调（dependabot.yml）

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
    open-pull-requests-limit: 10      # 同时最多打开的 PR 数量
    reviewers:
      - 'security-team'              # 自动指派审查人
    labels:
      - 'security'
      - 'dependencies'
    ignore:
      - dependency-name: 'lodash'
        versions: ['4.x']            # 忽略指定版本的更新
```

## 6. 第四道防线：Dependency Review（依赖审查）

### 6.1 原理：在"进门"前检查

Dependabot 解决的是"家里已有隐患"；Dependency Review 解决的是"**别把新隐患带进门**"。每当 PR 修改了清单/锁定文件，Dependency Review 会在 PR 的 "Files Changed" 选项卡中展示依赖变更的**富文本差异**：

- 新增/删除/更新的依赖及发布日期。
- 这些依赖的已知漏洞数据。
- 被多少项目使用。
- 许可证信息。

### 6.2 操作：作为 GitHub Actions 强制检查（推荐）

```yaml
# .github/workflows/dependency-review.yml
name: Dependency Review
on: [pull_request]                     # 每个 PR 都检查

permissions:
  contents: read

jobs:
  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
        with:
          # 严重级别达到 moderate 及以上则让检查失败
          fail-on-severity: moderate
          # 禁止引入以下许可证的依赖
          deny-licenses: GPL-3.0, AGPL-3.0
```

合并此工作流后，任何引入中危以上漏洞依赖的 PR 都会被 CI 拦截，直到依赖被替换或升级。

### 6.3 与许可证检查配合

Dependency Review 同时输出许可证信息，可用于合规管理（例如禁止引入 AGPL 依赖到企业闭源项目）。这正好与本模块 009 文档的许可证知识衔接。

## 7. 组合拳：一个完整的依赖安全基线

把四道防线串起来，就是生产环境的最低安全基线：

```mermaid
flowchart LR
    A["提交锁定文件"] --> B["依赖图谱自动生成"]
    B --> C["Dependabot Alerts 持续监控漏洞"]
    C --> D["Security Updates 自动创建修复 PR"]
    B --> E["Dependency Review 拦截 PR 新风险"]
    D --> F["人工审查后合并 PR"]
    E --> F
```

**日常动作清单**：

1. 提交所有锁定文件（图谱精度的前提）。
2. 启用 Dependabot alerts 与 security updates。
3. 提交 dependency-review 工作流到仓库。
4. 定期查看 Security 选项卡的告警面板。
5. 审查 Dependabot 创建的 PR（含 CI 通过）后再合并。

## 8. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 依赖图谱里看不到依赖 | Insights 中没有 Dependency graph 数据 | 清单/锁定文件未提交，或位于默认分支 | 提交锁定文件；确认清单在默认分支 |
| 有漏洞但没收到告警 | 邮件无通知 | Dependabot alerts 未启用，或通知被关闭 | Settings → Code security and analysis 启用；检查通知设置 |
| Dependabot 不创建安全更新 PR | 有告警无 PR | Security updates 未启用，或目标版本不存在安全版本 | 启用 Security updates；手动升级到修复版本 |
| Dependency Review 不生效 | PR 中看不到依赖差异 | 依赖图谱未启用，或仓库非组织所有 | 启用依赖图谱；确认组织已启用相应功能 |
| `dependabot.yml` 配置报错 | `Dependabot couldn't parse the config file` | YAML 缩进错误或键名拼写错误 | 使用官方配置选项参考逐项核对；`version` 必须为 2 |
| 升级依赖后应用崩溃 | 合并 PR 后线上故障 | 依赖大版本升级存在破坏性变更 | 为 Dependabot PR 配置 CI 测试；用 `ignore` 限制大版本升级 |

## 10. 一句话记忆

> **依赖安全是一套"家庭安防系统"：依赖图谱看清家底、Dependabot alerts 报警、安全更新自动灭火、Dependency Review 在 PR 门口检查危险品——四道防线缺一不可。**

### 官方文档

- GitHub 供应链安全概念（官方）：https://docs.github.com/zh/code-security/supply-chain-security
- 依赖图谱：https://docs.github.com/zh/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph
- Dependabot alerts：https://docs.github.com/zh/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
- Dependabot 配置选项参考：https://docs.github.com/zh/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file

### 延伸阅读
- Dependabot 深度专题（配置与自动合并），见 004-github 模块 016 文档。
- 开源许可证选择（许可证合规是依赖审查的一部分），见 004-github 模块 009 文档。
- Gitignore 配置（提交锁定文件与忽略敏感文件），见 004-github 模块 008 文档。
- GitHub Actions CI/CD（Dependency Review 的载体），见 004-github 模块 029 文档。



<!-- ============ 文档分隔线：004-github/011-ForkWorkflow.md ============ -->



## 0. 从一道菜说起：Fork 就像"复刻菜谱"

你在一家很出名的川菜馆吃到一道招牌菜"水煮鱼"，想自己做，但厨师不可能把秘方给你，更不可能让你进他的后厨。

怎么办？你在网上找到一位美食博主的"复刻教程"——他把这道菜的食材、步骤、火候全部公开了，并且说："你可以照着做，也可以改进，如果你做出了更好的版本，欢迎提交给我，我把它收录进教程。"

于是你的操作过程是：

1. **把教程复制一份到自己手里**（相当于 Fork）；
2. **在自己家照着做**，自由发挥，不会影响博主原来的教程；
3. **做出改进后，向博主发起申请**："我改进了三步，你看能不能收录"（相当于 Pull Request）；
4. 博主审查后觉得不错，**把你的改进合并进原教程**。

这就是开源世界最核心的协作模式——**Fork 工作流**。本文按"fork → clone → 改 → PR → 合回"的完整流程逐步讲解。

## 1. 流程总览：先建立整体地图

在动手之前，先记住整条链路涉及"三个仓库、一个申请"：

```mermaid
flowchart TD
  A["原始仓库 upstream（别人的，你无权修改）"]
  B["你的云端副本 origin（在你自己的账号下）"]
  C["本地仓库（在你自己电脑上，随便改）"]
  D["你的云端副本 origin"]
  E["原始仓库 upstream（维护者审查、合并）"]
  A -->|"① Fork（在网页上点一下按钮）"| B
  B -->|"② Clone（复制到你电脑上）"| C
  C -->|"③ 修改、提交"| D
  C -->|"④ Push（推回你的 origin）"| D
  D -->|"⑤ Pull Request（向原作者发起合并申请）"| E
```

术语速记：

| 术语 | 含义 | 类比 |
| :--- | :--- | :--- |
| **upstream** | 原始仓库（别人的项目） | 博主的原教程 |
| **origin** | 你 Fork 出来的副本 | 你复刻的教程副本 |
| **Fork** | 在 GitHub 云端复制仓库到你的账号 | 复制教程 |
| **Clone** | 把云端仓库下载到本地电脑 | 把教程打印成纸质版 |
| **PR（Pull Request）** | 请求原作者合并你的改动 | 申请把改进收录进原教程 |

### 1.1 Fork 和 Branch 有什么区别

很多新手会混淆这两个概念，一张表说清楚：

| 对比维度 | Fork | Branch（分支） |
| :--- | :--- | :--- |
| 位置 | 独立的新仓库（在你的账号下） | 同一个仓库内部 |
| 权限要求 | 无需原始仓库任何权限 | 需要该仓库的写权限 |
| 适用场景 | 开源贡献、无写权限的协作 | 团队内部开发 |
| 是否影响原仓库 | 不影响，完全隔离 | 分支合回前不影响默认分支 |
| CI/CD 配置 | 各自独立 | 共享仓库的配置 |

一句话：**没权限改别人的仓库时用 Fork，有权限时用 Branch**。

## 2. 流程第一步：Fork 仓库

### 2.1 网页操作

1. 打开目标仓库主页，例如 `https://github.com/torvalds/linux`；
2. 点击右上角 **Fork** 按钮；
3. 在弹出的页面选择归属（你的个人账号或组织），仓库名可以保持默认；
4. 点击 **Create fork**，几秒钟后你就拥有了一个一模一样的仓库副本，地址为 `https://github.com/你的用户名/linux`。

### 2.2 用 GitHub CLI 操作（可选）

```bash
# 安装 gh 后登录
gh auth login

# Fork 指定仓库到你的账号
gh repo fork torvalds/linux --clone
# 说明：--clone 表示 Fork 后自动克隆到本地
```

## 3. 流程第二步：克隆并配置两个远程仓库

### 3.1 操作示例

Fork 之后，你的云端副本是"静止的"——它不会自动跟随原仓库更新。要让它跟上进度，需要把**两个**远程地址都配置好：

```bash
# 1. 克隆你 Fork 的副本（origin）
git clone https://github.com/你的用户名/linux.git
cd linux

# 2. 把原始仓库添加为 upstream（"上游"）
git remote add upstream https://github.com/torvalds/linux.git

# 3. 查看配置结果：应该能看到两个 fetch/push 地址
git remote -v
# origin    https://github.com/你的用户名/linux.git (fetch)
# origin    https://github.com/你的用户名/linux.git (push)
# upstream  https://github.com/torvalds/linux.git (fetch)
# upstream  https://github.com/torvalds/linux.git (push)
```

### 3.2 为什么需要两个远程

- **origin** 指向你自己的副本，你推代码只能推到这里（原仓库没有你的写权限）；
- **upstream** 指向原仓库，用来**拉取**原仓库的最新代码，保证你的副本不落后。

可以这样记忆：origin 是"你能写字的草稿本"，upstream 是"别人的正稿，你只能读"。

## 4. 流程第三步：建分支、改代码、推上去

```bash
# 1. 确保 main 分支是最新的（第一次可以先跳过）
git fetch upstream
git checkout main
git merge upstream/main

# 2. 为这次改动创建功能分支（分支名要有意义）
git checkout -b fix/readme-typo

# 3. 修改文件，然后提交
git add README.md
git commit -m "docs: 修正 README 中的拼写错误"

# 4. 推送到你自己的副本（origin）的对应分支
git push origin fix/readme-typo
# 推送成功后，GitHub 会提示你点击 Compare & pull request
```

新手必记的三个分支纪律：

- **永远不要直接改 main 分支**，每个改动开一个分支；
- **分支名用"类型/描述"格式**，如 `feat/xxx`、`fix/xxx`、`docs/xxx`；
- **一次 PR 只做一个主题**，方便维护者审查和回滚。

## 5. 流程第四步：发起 Pull Request

1. 推完代码后，GitHub 会自动出现黄色横幅"Compare & pull request"，点击它；
2. 确认对比方向：**base 是原仓库的 main 分支，compare 是你副本的功能分支**；
3. 填写 PR 标题（一句话说清楚改动）和描述（为什么改、改了什么、如何验证）；
4. 如果改动是为了修复某个 Issue，在描述中写 `Fixes #123`，PR 合并时会自动关闭该 Issue；
5. 点击 **Create pull request**。

### 5.1 PR 描述模板参考

```markdown
## 改动内容

修复 README 中的三处拼写错误（installation → install 等）。

## 为什么改

拼写错误影响项目专业度，且容易被搜索工具误判。

## 验证方式

- 本地渲染 Markdown 无语法错误
- 链接均可正常访问

Fixes #102
```

### 5.2 PR 被审查后的常见反馈与应对

| 审查反馈 | 应对命令 |
| :--- | :--- |
| "请补充测试" | 加代码、提交、`git push`（PR 自动更新） |
| "代码风格不符" | 按项目规范修改后重新 push |
| "和 main 冲突了" | 见下文"同步与冲突解决" |
| "需要 rebase 到最新" | `git rebase upstream/main` 后 `git push --force-with-lease` |

## 6. 流程第五步：合回（Merge）与后续清理

PR 被维护者批准并合并后：

```bash
# 1. 把本地 main 同步到最新（含你被合并的改动）
git fetch upstream
git checkout main
git merge upstream/main

# 2. 删除已经没用的功能分支（本地 + 远程）
git branch -d fix/readme-typo
git push origin --delete fix/readme-typo
```

## 7. 保持 Fork 同步：三种方式对比

Fork 出来的副本不会自动同步，需要定期"跟上"上游，否则 PR 容易冲突。三种方式：

### 7.1 方式一：命令行（推荐，最可控）

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main    # 记得把同步结果推回你自己的云端副本
```

### 7.2 方式二：GitHub 网页按钮

打开你的 Fork 仓库主页 → 点击 **Sync fork**（同步分支）→ 点击 **Update branch**。适合不想记命令的场景，但只能同步 main 等分支，无法处理复杂冲突。

### 7.3 方式三：GitHub API / CLI

```bash
# 用 gh 触发 GitHub 服务端的同步
gh api repos/你的用户名/linux/merge-upstream -f branch=main
```

## 8. 冲突解决：PR 提示 "This branch has conflicts"

这是新手最怕、也最常遇到的场景。冲突的本质是：**你和别人改了同一段代码**。解决步骤：

```bash
# 1. 拉取上游最新代码到本地
git fetch upstream

# 2. 切到你的功能分支
git checkout fix/readme-typo

# 3. 把上游 main 合进来（或 rebase，二选一）
git rebase upstream/main
# 或：git merge upstream/main

# 4. 这时 Git 会提示冲突文件，逐个打开手动解决
#    冲突标记示例：
#    <<<<<<< HEAD
#    你写的内容
#    =======
#    上游的内容
#    >>>>>>> upstream/main

# 5. 解决完所有冲突后
git add 冲突文件
git rebase --continue   # 如果用 rebase
# 或
git commit -m "merge: 解决与 upstream 的冲突"   # 如果用 merge

# 6. 强制推送更新 PR（必须用 --force-with-lease，比 --force 安全）
git push origin fix/readme-typo --force-with-lease
```

**安全红线**：推送到自己 Fork 的分支时，优先用 `--force-with-lease` 而不是 `--force`。前者只在"远程分支没有被别人动过"时才覆盖，能避免误伤他人的改动。

## 9. 常见错误与对策表

| 常见错误 | 现象/报错信息 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 忘了配置 upstream | 提示 `fatal: 'upstream' does not appear to be a git repository` | 克隆后没执行 `git remote add upstream` | 按 3.1 节补上 upstream 配置 |
| 直接往原仓库推代码 | `Permission to owner/repo denied to 你的用户名` | 原仓库没有你的写权限 | 推送到自己的 Fork（origin），再发 PR |
| 往 main 分支开发 | PR 里混入大量无关历史 | 直接基于旧 main 建了改动 | 先同步 main，再 `checkout -b` 新功能分支 |
| 推送失败：分支落后 | `rejected ... non-fast-forward` | 远程分支和本地分叉了 | `git pull --rebase origin 分支名` 后再推 |
| 用了 `--force` 误伤他人 | 别人的提交被覆盖 | 强推覆盖了远程新提交 | 改用 `--force-with-lease`，除非确认独占分支 |
| PR 冲突不知道怎么办 | 网页提示 `This branch has conflicts` | 和上游改动同一段代码 | 按第 8 节 rebase + 手动解决 |
| PR 描述没关联 Issue | 合并后 Issue 还开着 | 描述里没写 `Fixes #编号` | PR 描述中加上 `Fixes #123` 格式 |

## 11. 一句话记忆

**Fork 工作流 = 把别人的仓库复制到自己账号（Fork）→ 克隆到本地（Clone）→ 在独立分支上修改 → 推送回自己的副本 → 向原作者发起合并申请（PR）→ 维护者审查合回，期间通过 upstream 持续同步保持不落后。**

### 延伸阅读（站内文档）

- 分支模型与分支保护规则，见 004-github 模块《分支模型与分支保护规则》。
- 从 Issue 到 PR 的完整协作流程，见 004-github 模块《PullRequest完整协作流程》。
- 冲突解决的更多细节，见 003-git 模块《Git冲突解决》。
- 开源许可证选择（Fork 公开仓库前必读），见 004-github 模块《开源许可证选择》。



<!-- ============ 文档分隔线：004-github/012-ProjectsBoard.md ============ -->



## 0. 从一块白板说起：Projects 就是团队的"项目白板 + 便利贴墙"

想象你们小组要办一场校园编程马拉松。没有电脑辅助的年代，大家会怎么管这件事？

教室墙上挂一块大白板，画上几列：**待办 → 进行中 → 待验收 → 完成**。然后每个人把任务写在便利贴上，往相应列一贴。谁认领了任务，就把自己的便利贴拖到"进行中"；做完一张，撕下来贴到"完成"列。白板旁边还贴着截止日期、负责人、优先级小标记。

这块白板解决的核心问题只有一个：**让所有人在一眼之间看清"现在做到哪了、接下来做什么"**。

GitHub Projects（项目）就是这块白板的数字化升级版，而便利贴变成了 **Issue（议题）和 Pull Request（拉取请求）**。它不仅保留了"拖拽便利贴"的直观体验，还多了几个实体白板做不到的能力：数据自动同步、多维视图切换、统计图表、自动化流转。

本文就沿着"白板"这条线索，把 Projects 讲透。

## 1. 直观理解：Projects 是什么

### 1.1 一个项目长什么样

Projects 是 GitHub 内置的项目管理工具。它的核心是一张可定制的"大表"（背后是数据），但提供三种看它的"视角"（视图）：

| 视图 | 长相 | 对应白板类比 | 适合场景 |
| :--- | :--- | :--- | :--- |
| **表格（Table）** | 像 Excel，每行一条任务，每列一个属性 | 白板旁边那张"任务登记表" | 批量编辑、筛选、排序 |
| **看板（Board）** | 按"状态"分列的卡片墙 | 教室白板本体 | 日常拖拽流转 |
| **时间线（Roadmap/Timeline）** | 按日期排的横条图 | 墙上贴的甘特图 | 规划里程碑、汇报进度 |

三者看的是**同一批数据**，只是展示方式不同。这就好比同一份班级名单，既可以按身高排队，也可以按学号排队，还可以画成座位表——人还是那些人。

### 1.2 它能管理什么

Projects 里的"便利贴"有三种来源：

- **Issue**：任务、Bug、功能请求（最常用）；
- **Pull Request**：代码改动；
- **草稿条目（Draft）**：还没转成 Issue 的临时想法，直接在白板上写，比如"下一步要调研 X 方案"。

## 2. 原理讲解：数据为什么是"活"的

### 2.1 先直观理解

普通便利贴墙的最大痛点：便利贴上的字和实际工作**不同步**。代码里 Bug 修好了，白板上还贴着"进行中"；任务改了负责人，白板没更新。

Projects 用"**双向同步**"解决了这个问题。

### 2.2 再讲原理

当你把某个 Issue 添加到 Project 后，两者之间就建立了**直接引用关系**（官方文档称 projects 由你添加的 Issue 和 PR 构建，信息在变更时自动同步到视图和图表中）：

- **Issue → 项目**：Issue 被关闭时，如果项目配置了内置工作流，卡片状态自动变为"完成"；
- **项目 → Issue**：你在项目表格里改了负责人、里程碑，Issue 页面上同步生效；
- **拖拽即修改**：在看板视图把卡片从"进行中"拖到"待验收"，本质上是修改了该条目的"Status 字段"，数据层完全一致。

这种"一处修改、处处生效"的机制，是 Projects 与静态表格的本质区别。

### 2.3 最后看示例

```mermaid
flowchart TD
  A["Issue #42：登录页按钮样式错位（在仓库里创建的 Issue）"] -->|"添加到项目"| B["Projects 条目"]
  B --> C["Status 字段：In Progress（看板视图的进行中列）"]
  B --> D["Priority 字段：High（自定义字段）"]
  B --> E["Sprint 字段：Sprint 2（迭代字段）"]
  B --> F["与 Issue #42 双向同步"]
```

## 3. 操作示例：从创建到投入使用

### 3.1 创建项目

**组织项目**（适合团队）：进入组织主页 → 点顶部 **Projects** 标签 → **New project** → 选择模板（内置模板有"Bug 追踪""团队待办"等）或从空白开始选 Table/Board/Roadmap 布局。

**用户/仓库项目**（适合个人）：个人主页或仓库页面 → **Projects** → **New project**。仓库项目会自动关联当前仓库。

### 3.2 添加条目

```text
方法一：在项目页点 "+" → 搜索仓库里的 Issue / PR 添加
方法二：打开 Issue 页面 → 右侧边栏 "Projects" 选择项目
方法三：在项目里直接创建草稿条目（Draft）
```

### 3.3 配置自定义字段（白板上的"便利贴属性"）

新建项目后，项目自带一个 `Status` 单选字段（Backlog → Todo → In Progress → In Review → Done 等默认选项）。团队通常还要加这些字段：

| 字段类型 | 用途示例 | 白板类比 |
| :--- | :--- | :--- |
| **Single select（单选）** | 状态、优先级（Critical/High/Medium/Low）、类型（Bug/Feature/Docs） | 便利贴颜色 |
| **Iteration（迭代）** | Sprint 1 / Sprint 2，支持设置休假期 | 白板上的周计划表 |
| **Number（数字）** | 工作量估算（1/2/3/5/8/13） | 便利贴角落的工时 |
| **Date（日期）** | 截止日期、目标发布日期 | 便利贴上的截止日 |
| **Text（文本）** | 备注、验收标准 | 便利贴背面小字 |
| **Milestone / Assignee** | 内置字段，直接引用 | 便利贴上的负责人签名 |

官方文档说明：单个项目最多可添加 **50 个字段**，字段配置一次，团队所有人共享。

## 4. 三种视图的切换与配置

### 4.1 表格视图

适合批量操作：每行一个条目，点击单元格即可修改字段，支持按任意列排序、筛选（如只看 `Sprint 2` 且 `Priority: High`）、按字段分组。

```text
| Title              | Status      | Priority | Sprint   | Assignee |
| :----------------- | :---------- | :------- | :------- | :------- |
| 登录页按钮错位     | In Progress | High     | Sprint 2 | 张三     |
| API 限流文档       | Done        | Medium   | Sprint 1 | 李四     |
| 性能监控告警       | Todo        | Low      | Sprint 3 | 王五     |
```

### 4.2 看板视图

按"分组依据"（默认按 Status）分列，卡片可拖拽。想按负责人分组？把分组依据改成 Assignee 即可。拖拽卡片换组 = 修改字段值，这是看板最顺手的地方。

### 4.3 时间线（Roadmap）视图

把时间轴设为日期字段（如截止日期），每个条目变成一根横条，用于向团队和管理层展示里程碑进度。官方快速入门中，常用它"规划迭代、向协作者传达优先级和进度"。

### 4.4 视图保存

每个视图可以命名保存（如"我的待办""本轮迭代"），团队成员可以共享视图，也可以建个人私有视图。同一条数据，多种看法，互不干扰。

## 5. 自动化：让白板自己动起来

### 5.1 内置工作流（Built-in workflows）

这是 Projects 最有价值的能力之一。配置路径：项目 → 顶部 **Workflows** → **Configure**。常用规则：

| 触发条件 | 自动执行 | 白板类比 |
| :--- | :--- | :--- |
| Issue 刚添加时 | 设置状态为 Todo | 新便利贴自动贴到"待办"列 |
| 对应的 PR 标记为 Ready for review | 状态改为 In Review | 有人喊"我做好了"，卡片自己挪过去 |
| Issue / PR 被关闭（或 PR 合并） | 状态改为 Done | 任务做完，便利贴自动撕到"完成" |
| 条目被重新打开 | 状态改回 Todo | 复活的任务自己回到待办列 |

### 5.2 用 GitHub Actions 做更复杂的自动化

内置工作流不够用时，可以用 Actions。经典场景：**给打上指定标签的 Issue 自动加入项目**。

```yaml
# .github/workflows/add-to-project.yml
name: Add issues to project
on:
  issues:
    types: [opened, labeled]        # Issue 新建或被打标签时触发
jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/orgs/your-org/projects/1
          github-token: ${{ secrets.PROJECT_TOKEN }}
          labeled: bug, feature      # 只有带这些标签的 Issue 才加入
```

注意：`actions/add-to-project` 需要一个人格化令牌（PAT）或细粒度令牌，权限至少包含读写项目。

### 5.3 用 GraphQL API 自动化（进阶）

```graphql
mutation {
  addProjectV2ItemById(input: {
    projectId: "PVT_xxxxxx",      # 项目 ID
    contentId: "I_xxxxxx"         # Issue ID
  }) {
    item { id }
  }
}
```

## 6. 洞察图表（Insights）：白板的"数据看板"

项目 → **Insights** 标签可以基于项目数据生成图表，所有有项目查看权限的人都能看到。两类图表：

- **当前图表（Current charts）**：快照式统计，比如"每个成员名下有多少条目""每个迭代分配了多少问题""按标签分布"；
- **历史图表（Historical charts）**：随时间变化，比如默认的 **Burn up（燃尽）图**，展示"已完成工作 vs 剩余工作"随时间的变化，用来发现瓶颈、预测进度。

官方提示：洞察**不追踪已归档或删除的条目**，所以想保留历史统计，别急着归档。

## 7. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 找不到新建项目入口 | 页面没有 New project 按钮 | 权限不足或无组织归属 | 组织项目需组织成员身份；个人项目在个人主页 Projects 下创建 |
| 添加条目时搜索不到 Issue | 列表为空 | 项目权限未包含该仓库 | 在项目设置中添加仓库，或确认仓库归属 |
| 改了 Issue 状态但项目没变 | 卡片状态不变 | 未配置内置工作流 | 项目 → Workflows → 开启"关闭时设为完成"等规则 |
| 拖拽换列没生效 | 卡片弹回原列 | 分组的字段不是 Status | 确认看板按 Status 分组，拖拽本质是改字段值 |
| Actions 自动化失败 | `Resource not accessible by integration` | 令牌权限不够 | 使用带 `read:project`/`write:project` 的 PAT，存在仓库 Secrets 中 |
| 多人看到的视图不一致 | 各自字段不同 | 改了私有视图而非共享视图 | 保存视图时选择"保存到共享视图"（团队需要时可复制） |
| 图表数据对不上 | Insights 缺条目 | 洞察不含已归档/已删除条目 | 统计期内不要归档条目，或使用筛选修正口径 |

## 9. 一句话记忆

**Projects 就是把团队白板搬进 GitHub：Issue 和 PR 是便利贴，表格/看板/时间线是三种看法，自定义字段是便利贴上的属性，内置工作流让便利贴自动流转——所有数据双向同步，一处改动处处生效。**

### 延伸阅读（站内文档）

- Issue 模板、标签与里程碑，见 004-github 模块《Issues模板-标签与里程碑》。
- GitHub Actions 触发方式，见 004-github 模块《Actions触发》。
- 社区讨论与需求收集，见 004-github 模块《Discussions》。
- 用 GraphQL 操作项目，见 004-github 模块《REST与GraphQL-API》。



<!-- ============ 文档分隔线：004-github/013-Wikis.md ============ -->



## 0. 从一个场景说起：团队知识都去哪了

你的社团要做一个校园二手交易平台，10 个人分了三组：前端、后端、测试。三个月过去了，你发现一个可怕的现象：

- 后端组长离职，他脑子里那套"数据库怎么设计的、为什么这么设计"的决策理由，随着他的离开一起消失了；
- 新人小周接手前端，只能靠翻聊天记录和问人，同一个问题被问了五遍；
- 项目验收时，评审问"你们的接口文档在哪"，全组面面相觑——散落在三份不同的共享文档里，版本还对不上。

这就是**知识沉淀缺失**的典型症状：知识只存在于个别人的脑子里和聊天记录里，项目越做越大，知识越散越碎。

GitHub 仓库自带一个解决这个问题的"知识库"区域——**Wiki（维基）**。本文围绕"团队知识沉淀"这个场景，讲解 Wiki 怎么用、怎么组织、怎么长期维护。

## 1. 场景判断：什么时候该用 Wiki

### 1.1 先直观理解

Wiki 是每个 GitHub 仓库自带的文档托管区域，适合放**长篇幅、多页面、需要持续积累**的文档。它的定位一句话可以概括：**README 讲"是什么"，Wiki 讲"怎么做、为什么这么设计"**。

### 1.2 再对照场景

| 内容类型 | 放哪 | 场景举例 |
| :--- | :--- | :--- |
| 项目一句话介绍、快速开始 | README | "这是什么、怎么跑起来" |
| 使用教程、设计文档、架构说明 | Wiki | "数据库为什么这么设计""部署手册" |
| API 自动生成的参考文档 | docs 目录 + 工具生成 | 类型定义、接口签名 |
| 讨论与问答 | Discussions / Issues | "这个功能该不该做""我遇到了 Bug" |

具体来说，出现以下情况之一，就该考虑开 Wiki 了：

- 新成员加入时，需要一份"从零到能干活"的文档；
- 团队经常重复解释同一个问题；
- 设计决策（为什么用这个方案而不是另一个）无处记录；
- 文档超过 5 个页面，README 已经塞不下。

### 1.3 最后看示例

```mermaid
flowchart TD
  A["Wiki"] --> B["Home.md（首页：知识库入口/目录）"]
  A --> C["Getting-Started.md（新人上手指南）"]
  A --> D["Architecture.md（架构设计与决策记录 ADR）"]
  A --> E["Database-Design.md（数据库设计说明）"]
  A --> F["Deployment.md（部署手册）"]
  A --> G["Meeting-Notes.md（会议纪要归档）"]
  A --> H["_Sidebar.md（全局侧边栏导航）"]
```

## 2. 启用与权限配置

### 2.1 启用 Wiki

仓库默认开启了 Wiki 功能。如果没看到 **Wiki** 标签页：

1. 进入仓库 **Settings（设置）**；
2. 找到 **Features（功能）** 区，勾选 **Wikis**；
3. 回到仓库主页，顶部就会出现 Wiki 标签，访问地址为 `https://github.com/你的用户名/仓库名/wiki`。

### 2.2 权限设置

在 Settings → Features → Wiki 下方可以设置谁能编辑：

| 选项 | 说明 | 适用场景 |
| :--- | :--- | :--- |
| **Restrict editing to collaborators only（仅协作者可编辑）** | 只有有写权限的人能改 Wiki | 团队内部文档、私有仓库 |
| **Anyone on GitHub can edit（任何人都可编辑）** | 公开仓库中所有人都能贡献 | 开源项目文档众包 |

提示：如果希望搜索引擎收录 Wiki 内容，GitHub 官方说明——**只有配置为"禁止公开编辑"且星标数达到 500 的公开仓库 Wiki 才会被搜索引擎索引**。普通 Wiki 内容对搜索并不友好，需要被收录的内容建议用 GitHub Pages 发布。

## 3. 创建和组织 Wiki 页面

### 3.1 创建首页

第一次进入 Wiki 页，点击 **Create the first page（创建第一页）**。首页默认文件名是 `Home.md`。建议首页就做"入口"：一段简短介绍 + 指向各页面的链接树。

### 3.2 添加新页面

1. Wiki 页面右上角点 **New Page（新建页面）**；
2. 标题栏输入页面标题（标题会成为文件名，如 `Getting-Started` → `Getting-Started.md`）；
3. 编辑模式默认是 Markdown，也可以从下拉框切换为其他格式（如 Textile、Asciidoc）；
4. 填写"编辑消息"（类似提交信息），点击 **Save Page** 保存。

### 3.3 页面间链接

Wiki 里链接其他页面，推荐用双括号语法，渲染后自动生成链接：

```markdown
了解更多请访问 [[架构设计]] 和 [[部署手册]]。
```

### 3.4 侧边栏（_Sidebar.md）

侧边栏显示在 Wiki 所有页面右侧，是全局导航。创建方法：Wiki 主页 → **Add a custom sidebar（添加自定义侧边栏）**，编辑 `_Sidebar.md`：

```markdown
**文档导航**

- [[Home|首页]]
- [[Getting-Started|新人上手]]
- [[Architecture|架构设计]]
  - [[Frontend-Design|前端设计]]
  - [[Backend-Design|后端设计]]
- [[Deployment|部署手册]]
- [[FAQ|常见问题]]
```

### 3.5 页脚（_Footer.md）

页脚显示在每个页面底部，适合放版权、更新说明、反馈入口。创建方法与侧边栏类似（**Add a custom footer**）：

```markdown
---

文档最后更新于 2026-08-02
发现错误？请提交 [Issue](../../issues) 或直接编辑本页。
```

## 4. 本地编辑：Wiki 其实是个 Git 仓库

### 4.1 原理

Wiki 页面支持在网页上直接编辑，但它的底层是一个**独立的 Git 仓库**（和你项目的主仓库分开）。这意味着你可以像管理代码一样管理文档：克隆、分支、提交、推送。

### 4.2 克隆 Wiki

```bash
# 克隆格式：仓库名后加 .wiki.git
git clone https://github.com/你的用户名/你的仓库.wiki.git
cd 你的仓库.wiki

# 目录结构示例
# Home.md            ← 首页
# _Sidebar.md        ← 侧边栏
# _Footer.md         ← 页脚
# Getting-Started.md ← 自定义页面
```

### 4.3 本地编辑并推送

```bash
# 修改页面
vim Deployment.md

# 提交并推送（注意分支通常是 master）
git add .
git commit -m "docs: 更新部署手册，补充回滚步骤"
git push origin master
```

### 4.4 命名注意事项（官方明确提醒）

- 文件名就是页面标题，扩展名决定渲染方式：`foo.md` / `foo.markdown` 用 Markdown 渲染，`foo.textile` 用 Textile；
- **页面标题中不要使用这些字符**：`\ / : * ? " < > |`，否则部分操作系统的用户无法正常处理文件名；
- 多人协作时可以建分支，但**只有推送到默认分支的修改才会生效展示**。

## 5. 维护最佳实践：让知识库"活"下去

Wiki 最大的敌人是"写完就忘"。以下实践能让文档持续更新：

- **首页当目录**：首页只做导航，不堆正文，所有知识按主题拆页；
- **统一侧边栏**：用 `_Sidebar.md` 维持全局导航，新增页面后及时登记；
- **文档随代码走**：接口变了，当天就更新对应页面，约定"改代码的人负责改文档"；
- **记录决策**：架构选型、方案权衡写进"决策记录（ADR）"页面，格式固定为"背景→方案→理由→代价"；
- **定期体检**：每轮迭代结束，安排 30 分钟清理过期页面、合并重复内容；
- **明确权限**：团队内部仓库一律"仅协作者可编辑"，避免内容被误改。

## 6. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 找不到 Wiki 标签 | 仓库顶部没有 Wiki 页签 | 功能被关闭 | Settings → Features → 勾选 Wikis |
| 页面标题含特殊字符 | 克隆后部分文件无法检出 | 标题含 `\ / : * ? " < > \|` | 去掉这些字符再重命名页面 |
| 本地改了不生效 | 网页上还是旧内容 | 推到了非默认分支 | 确认推送目标是默认分支（master/main） |
| 链接 404 | 双括号链接点开是空页 | 目标页面尚未创建 | 先创建目标页面，再检查文件名大小写 |
| 内容不显示 | 一片空白或渲染异常 | 扩展名与内容格式不匹配 | 内容用 Markdown 就存为 `.md`，并检查语法 |
| 文档与代码脱节 | 页面内容过时 | 没有维护机制 | 采用"改代码者同步改文档"约定 + 定期体检 |
| Wiki 太多页打不开 | 部分页面访问缓慢 | 官方对 Wiki 有软限制（约 5000 个文件） | 超过规模改用 GitHub Pages 或 docs 目录 |

## 8. 一句话记忆

**Wiki 是仓库自带的"项目百科"：README 讲是什么，Wiki 讲怎么做和为什么这么设计；用首页做目录、侧边栏做导航、页脚做版权与反馈，把它当独立 Git 仓库来维护，知识才能持续沉淀。**

### 延伸阅读（站内文档）

- README 与 Wiki 的分工，见 004-github 模块《README文件》。
- 从 Issue 到 PR 的协作流程，见 004-github 模块《PullRequest完整协作流程》。
- 社区问答与公告，见 004-github 模块《Discussions》。
- 用 GitHub Pages 发布可被搜索引擎收录的文档站，见 004-github 模块《GitHubPages多站点方案》。



<!-- ============ 文档分隔线：004-github/014-Discussions.md ============ -->



## 0. 从一个困惑说起：我该用 Issue 还是 Discussion？

你第一次参与开源项目，想问一个问题："这个项目支持 Windows 吗？"你打开仓库，看到两个入口：**Issues（议题）** 和 **Discussions（讨论）**。

你犹豫了：这俩有什么区别？问问题到底该点哪个？填错了会不会被维护者嫌弃？

这个困惑，几乎所有 GitHub 新手都经历过。要回答它，先看一个生活类比：

- **Issue 像"保修单/工单系统"**：你买了冰箱坏了，填一张保修单，注明故障现象，厂家会安排人处理，处理完这张单子就结案归档，有编号可追踪；
- **Discussions 像"社区论坛/商品评论区"**：大家在论坛里聊"这个牌子的冰箱怎么样""怎么保养能延长寿命"，没有结案一说，谁都可以加入，好的回答会被点赞顶到最上面。

它们的本质区别：**Issue 是"任务"，需要被解决、被追踪；Discussion 是"话题"，适合开放交流、沉淀问答**。本文就从这个问题切入，把 Discussions 讲透。

## 1. 直观理解：Discussions 是什么

### 1.1 一句话定义

GitHub Discussions 是仓库（或组织）自带的一个**论坛式沟通区**。官方文档的定义是：它为项目周围的开源或内部社区提供协作式沟通论坛——适合需要透明、开放访问，但**不需要在项目里追踪、也不直接关联代码**的对话。

### 1.2 和论坛对照

| 论坛概念 | Discussions 对应物 |
| :--- | :--- |
| 板块 | 分类（Category），如"问答""公告""想法" |
| 帖子 | 讨论（Discussion） |
| 回帖 | 评论（Comment），可以多级回复 |
| 采纳答案 | 标记答案（Answer），Q&A 分类专用 |
| 置顶帖 | 置顶讨论（Pinned） |
| 投票贴 | 投票（Poll） |

## 2. 核心问题：Issue 还是 Discussion？一张决策表搞定

### 2.1 决策对照表

| 判断维度 | 用 Issue | 用 Discussion |
| :--- | :--- | :--- |
| 对话性质 | 有明确交付物：Bug、任务、功能请求 | 开放式：提问、想法、闲聊、公告 |
| 是否需要解决 | 需要，有"关闭"状态 | 不需要，持续存在 |
| 是否关联代码 | 常关联 PR、提交 | 独立于代码 |
| 负责人 | 有明确负责人（Assignee） | 通常没有 |
| 输出 | 任务被完成、修复 | 讨论被沉淀、达成共识 |
| 生命周期 | 创建 → 讨论 → 关闭 | 长期滚动，可归档 |

### 2.2 决策速查

```mermaid
flowchart LR
  A["想报告 Bug / 要求修东西 / 分配任务"] --> B["用 Issue（贴模板、打标签、挂里程碑）"]
  C["想问用法 / 讨论方案 / 收集想法 / 发公告 / 展示作品"] --> D["用 Discussion"]
```

官方文档给出的"Discussion 场景"清单：

- 我有一个问题，但不一定和仓库里某个文件相关；
- 我想和协作者或团队分享资讯；
- 我想发起或参与一次开放式的讨论；
- 我想向社区发布公告。

### 2.3 两个工具配合的完整图景

在一个成熟的开源项目里，它们这样配合：

```mermaid
flowchart TD
  A["Discussions（前期：聊想法、问问题）"] -->|"想法成熟、确认要做"| B["Issues（中期：转为任务，排期、指派）"]
  B -->|"开发完成"| C["Pull Requests（后期：提交代码改动）"]
  C -->|"合并后"| A
```

## 3. 启用 Discussions 并配置分类

### 3.1 启用（仓库级）

1. 仓库主页进入 **Settings**；
2. 滚动到 **Features** 区，点击 **Set up discussions**；
3. 编辑"欢迎贴"内容（决定社区基调的第一条讨论），点击 **Start discussion**。

启用后访问地址：`https://github.com/你的用户名/仓库名/discussions`。

### 3.2 组织级启用（可选）

组织管理员可在组织 **Settings → Discussions** 勾选启用，并指定一个"源仓库"来承载组织讨论。注意：**讨论权限与源仓库权限一致，更换源仓库不会迁移已有讨论**。

### 3.3 分类体系（板块设计）

所有讨论都必须属于一个分类。分类有三种格式：

| 格式 | 说明 | 谁能发帖 |
| :--- | :--- | :--- |
| **开放式讨论（Open-ended）** | 普通话题，任何人可发起 | 所有人 |
| **问答（Question & answer）** | 问题贴，可标记最佳答案 | 所有人 |
| **公告（Announcement）** | 只读发布区，评论开放 | 仅管理员/维护者 |

仓库默认带五个分类，建议保留并理解用途：

| 默认分类 | 格式 | 用途 | 论坛类比 |
| :--- | :--- | :--- | :--- |
| **Announcements** | 公告 | 版本发布、重大变更通知 | 置顶公告区 |
| **General** | 开放式 | 通用讨论 | 综合版块 |
| **Ideas** | 开放式 | 功能想法、头脑风暴 | 建议区 |
| **Q&A** | 问答 | 使用问题求助 | 问答版块 |
| **Show and Tell** | 开放式 | 展示基于项目的作品 | 展示区 |

自定义分类：仓库管理员在 Discussions 页面 → **Manage categories** → 新建分类（可设图标、颜色、格式、发帖模板）。

## 4. 问答的正确用法：提问 → 回答 → 采纳

### 4.1 流程

1. 在 **Q&A** 分类发帖，标题写成问题（如"如何配置代理？"），正文给出：环境、想做什么、尝试过什么、期望结果；
2. 别人回复后，你可以把某个回答标记为 **答案**（Answer）；
3. 被采纳的回答会置顶展示，形成"人肉 FAQ"。

### 4.2 官方机制：最有帮助的贡献者

GitHub 会自动识别"答案被采纳次数最多"的社区成员，在讨论页展示**最有帮助的贡献者**列表。这意味着：认真回答别人的问题，不只是做好事，还会获得社区的公开认可。

### 4.3 提问模板示例

```markdown
## 环境

- 项目版本：v2.3.0
- 操作系统：Windows 11
- 复现方式：运行 `npm run dev` 后访问 /login

## 问题描述

登录接口返回 500，日志如下：

```
TypeError: Cannot read properties of undefined (reading 'token')
```

## 我已尝试

- 重新安装依赖（无效）
- 检查环境变量（配置正确）
```

## 5. 公告、投票与展示

### 5.1 发布公告

把分类设为"公告"格式后，只有管理员能发新帖，其他人只能评论。适合：版本发布、安全通告、迁移通知、社区规则更新。发布后建议**置顶（Pin）**，让新访客第一眼看到。

### 5.2 发起投票（Poll）

在支持的分类里新建讨论时可以附加投票选项，适合社区决策：

```markdown
## 下季度优先做哪个功能？

- [ ] 移动端适配
- [ ] 暗色主题
- [ ] 插件系统
- [ ] 性能优化
```

### 5.3 展示作品（Show and Tell）

鼓励用户发帖展示自己的用法、衍生作品、教程，是低成本高回报的社区运营手段——用户获得展示机会，项目获得传播和案例。

## 6. 与 Issue 的相互转换

### 6.1 Discussion → Issue

讨论中的想法成熟后，转成 Issue 进入任务队列：

1. 打开讨论，右侧边栏选择 **Convert to issue**；
2. 选择目标仓库和 Issue 模板，补充必要信息；
3. 转换后，原讨论会保留并链接到新 Issue，两边的讨论不丢失。

### 6.2 Issue → Discussion

反过来，如果某个 Issue 只是开放式讨论、没有明确任务，维护者可以把它转为讨论（**Convert to discussion**），让 Issue 列表保持"全部是待办任务"的清爽状态。

## 7. 维护者运营最佳实践

- **写好欢迎贴**：置顶一条欢迎贴，说明"这个社区聊什么、提问前先搜索、提问格式"；
- **规定提问纪律**：在欢迎贴或 README 中说明"技术求助去 Q&A，Bug 报告去 Issue"；
- **及时采纳答案**：Q&A 帖子有了好回答，第一时间标记答案，降低重复提问；
- **定期转化沉淀**：每周把成熟讨论转成 Issue，把常见问答整理进 Wiki 或 FAQ；
- **用好公告分类**：所有正式通知走公告分类并置顶，保持信息权威性；
- **维护社区公约**：参照 GitHub 社区行为准则，对不当内容使用锁定（Lock）和删除功能。

## 8. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 把 Bug 报告发到 Discussions | 讨论区被任务淹没，维护者不看 | 混淆了任务与话题 | Bug 走 Issue 模板；讨论区只放开放话题 |
| 问答帖没人答/不采纳 | 问题质量低或无人标记答案 | 提问信息不足 | 按 4.3 模板补齐环境/复现/已尝试；有好答案立即标记 |
| 找不到新建讨论按钮 | 页面没有 New discussion | 未启用或分类权限受限 | Settings → Features 启用；确认分类允许你发帖 |
| 公告被普通人刷屏 | 公告区出现非官方帖子 | 分类格式未设为"公告" | 把该分类改为公告格式（仅管理员可发帖） |
| 转换 Issue 后内容丢失 | 转完后讨论区找不到了 | 误以为转换是"移动" | 转换会保留原讨论并互相链接，无需担心 |
| 分类混乱 | 帖子发错版块 | 分类设计不合理 | 精简分类数量，每个分类写清用途说明 |
| 讨论区冷清 | 发帖无人响应 | 社区未运营 | 维护者主动发起话题、欢迎贴置顶、展示问答 |

## 10. 一句话记忆

**Discussions 是仓库的社区论坛：Issue 管"要完成的任务"，Discussion 管"开放的话题"——问题、想法、公告、展示都放这儿，问答可标记答案，想法成熟后转成 Issue 继续推进，一静一动配合使用。**

### 延伸阅读（站内文档）

- Issue 模板、标签与里程碑，见 004-github 模块《Issues模板-标签与里程碑》。
- 团队任务看板，见 004-github 模块《Projects看板》。
- 知识沉淀与 FAQ 整理，见 004-github 模块《Wikis》。
- 社区公约与健康文件，见 004-github 模块《社区健康文件》。



<!-- ============ 文档分隔线：004-github/015-GitHubCopilot.md ============ -->



## 0. 从一次"被补全"的体验说起：像有个结对编程的老手坐在旁边

想象这样一个瞬间：你在 VS Code 里刚敲完一行注释：

```python
# 把用户列表按注册时间排序，时间最新的排最前
```

光标还在闪烁，灰字已经出现了——代码自动"浮现"在下一行，像是有人替你把思路写了出来。你按下 Tab 键，它被采纳；继续往下写，它继续接。整个过程流畅得像是**输入法的联想功能学会了写代码**。

这就是 GitHub Copilot 的第一次体验。把它类比成一句话：**Copilot 就像一个结对编程的 AI 助手**——老手程序员在你身边，你写注释它接代码，你提问它解释，你写错它帮你找 Bug。区别是这位"老手"读过海量的公开代码，响应速度以毫秒计，而且 24 小时不打烊。

本文就从"体验"出发，带你走一遍 Copilot 的订阅、安装、使用、调教和安全。

## 1. 直观理解：Copilot 是什么、能做什么

### 1.1 一句话定义

GitHub Copilot 是 GitHub 推出的 **AI 编程助手**，能在你写代码时提供代码补全，并支持对话式提问（Copilot Chat）、终端命令辅助（Copilot CLI）等能力。

### 1.2 体验维度总览

| 功能 | 体验描述 | 类比 |
| :--- | :--- | :--- |
| **代码补全** | 写注释/函数名时自动给出后续代码，Tab 采纳 | 输入法的"智能联想" |
| **Copilot Chat** | 选中代码直接问"这段在干嘛""帮我写测试" | 身边的老手随问随答 |
| **代理/多文件编辑** | 跨文件重构、批量修改 | 老手帮你通读全仓库改完 |
| **Copilot CLI** | 终端里解释命令、生成命令 | 命令行老师傅 |

### 1.3 第一次体验的完整路径

1. 在 VS Code 安装 **GitHub Copilot** 扩展（以及可选的 Copilot Chat 扩展）；
2. 用 GitHub 账号登录并授权；
3. 打开一个 Python/JavaScript 文件，输入一行注释，等待灰色建议出现；
4. 按 **Tab** 采纳，按 **Esc** 拒绝，按 **Ctrl+→**（macOS 为 Cmd+→）只采纳下一行。

## 2. 原理讲解：它怎么知道我要写什么

### 2.1 先直观理解

Copilot 不是"读心术"，它的工作方式很像你实习时看老师傅写代码：**老师傅会先看你的项目背景、你刚写的代码、你写的注释，再判断你接下来想干什么**。

### 2.2 再讲原理

Copilot 基于大语言模型（LLM）构建。当你在编辑器里停下时，它会把你"编辑器中的上下文"打包发给模型，让模型预测"最可能的后续代码"：

- **当前文件内容**：你写了一半的函数、变量名、注释；
- **相邻文件**：同目录下相关文件（取决于语言和插件版本）；
- **打开的标签页**：你正在看的相关代码；
- **仓库指令文件**：`.github/copilot-instructions.md` 中声明的项目规范。

模型给出的建议可能不止一条，用 **Alt+]**（macOS 为 Option+]）可以循环切换候选方案。

### 2.3 最后看示例

```python
# 输入：注释 + 函数名
def validate_email(email):
    # Copilot 建议：
    if "@" not in email or "." not in email.split("@")[1]:
        return False
    return True
```

## 3. 订阅计划：先免费体验，再按需升级

### 3.1 个人计划（2026 年官方定价）

| 计划 | 价格 | 关键权益 | 适合谁 |
| :--- | :--- | :--- | :--- |
| **Copilot Free** | 免费 | 每月约 2000 次补全 + 少量 AI 额度 | 新手尝鲜、学生 |
| **Copilot Student** | 免费（需学生认证） | 无限补全 + 更多模型 | 学生 |
| **Copilot Pro** | 10 美元/月 | 无限补全 + Chat + 模型选择 | 个人开发者主力 |
| **Copilot Pro+** | 39 美元/月 | 更多 AI 额度、高级模型优先 | AI 重度用户 |

官方说明：已验证的**教师和流行开源项目维护者可以免费获得 Pro**；验证学生免费使用 Student 计划。

### 3.2 团队/企业计划

| 计划 | 价格 | 关键能力 |
| :--- | :--- | :--- |
| **Copilot Business** | 19 美元/人/月 | 团队管理、策略控制、审计日志 |
| **Copilot Enterprise** | 39 美元/人/月 | 企业知识库、自定义模型、更多管理 |

### 3.3 管理入口

GitHub 右上角头像 → **Settings（设置）** → **Billing and plans（计费与许可证）** → GitHub Copilot 区段，可以查看当前计划、升级、降级或取消。提示：**如果是组织分配给你的席位，个人无法修改计划**。

## 4. 操作示例：三个高频场景

### 4.1 场景一：注释驱动开发（补全）

```python
# 写清意图，建议质量会明显提升
# 接收 CSV 文件路径，返回去重后的用户邮箱列表
def load_unique_emails(csv_path):
    # Copilot 建议：
    import csv
    emails = set()
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            emails.add(row["email"])
    return list(emails)
```

### 4.2 场景二：Copilot Chat 提问

选中一段看不懂的代码，打开 Chat 面板，输入：

```text
解释这段代码做了什么，用中文回答，并指出潜在的性能问题。
```

Copilot 会结合你选中的上下文回答。常用指令示例：

```text
为这个函数生成单元测试
把这个组件重构为函数式组件
找出这段代码里的边界条件问题
用更易读的方式重写这个正则
```

### 4.3 场景三：Copilot CLI（终端）

```bash
# 安装扩展
gh extension install github/gh-copilot

# 解释命令：像让老师傅翻译
gh copilot explain "git rebase -i HEAD~5"

# 生成命令：描述目标，得到命令
gh copilot suggest "找出上周修改过、且包含 debug 的所有 JS 文件"
```

## 5. 提示词工程：让 AI 更懂你的项目

### 5.1 注释写清楚，补全更准确

对比两个例子：

```javascript
// 模糊：处理数据（模型只能瞎猜）
function process(data) { ... }

// 清晰：把用户数据转换为 API 请求格式，过滤无效邮箱
// 输入: User[] 输出: APIUser[]（无重复、邮箱有效）
function formatUserForAPI(users) { ... }
```

要点：**意图（做什么）+ 约束（输入输出/边界）+ 示例**是三大要素。

### 5.2 仓库级指令：copilot-instructions.md

这是官方提供的"给 Copilot 立规矩"的文件。在仓库根目录创建 `.github/copilot-instructions.md`：

```markdown
# 项目编码规范（Copilot 必须遵守）

## 技术栈

Vue 3 + TypeScript + Pinia，后端 Python FastAPI。

## 编码规范

- 前端使用 Composition API，禁止 Options API
- 使用 `<script setup>` 语法
- 组件命名用 PascalCase，文件命名用 kebab-case
- 类型优先用 interface 而非 type

## 测试要求

- 使用 Vitest
- 每个组件必须有对应测试文件
```

### 5.3 忽略敏感文件

在 `.github/copilot-ignore` 中列出不想让 Copilot 读取的文件：

```text
.env
*.secret
config/credentials.json
```

## 6. 安全与最佳实践

- **不要把密钥喂给 AI**：不要选中含密码、Token 的代码提问或让它生成；
- **审查每一行建议**：补全不代表正确，尤其涉及安全逻辑（鉴权、SQL、加密）时必须人工核对；
- **注意许可边界**：AI 可能生成与训练数据相似度高的代码，商业项目建议团队版并确认合规策略；
- **团队用 Business 版**：获得数据保护承诺与策略控制（是否允许公共代码补全等）；
- **给 Copilot 足够的上下文**：提问时附上相关文件或代码段，而不是问"我有个 Bug 怎么办"；
- **学而不抄**：把 Copilot 当"快速起草工具"，理解之后再用，避免"代码会跑但讲不出为什么"。

## 7. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 安装后没建议 | 灰字不出现 | 未登录授权，或扩展未激活 | 命令面板运行 `Sign in with GitHub` 完成授权 |
| 提示配额用尽 | 补全明显变少/停止 | Free 计划额度用完 | 升级 Pro，或等待月度重置 |
| 建议质量差 | 生成代码与意图不符 | 注释模糊、上下文不足 | 按 5.1 写清意图+约束+示例 |
| 生成敏感信息 | 建议中出现假 Token | 训练数据特征 | 不要采信；配置 copilot-ignore 排除密钥文件 |
| 报权限错误 | `GitHub Copilot could not connect to server` | 网络受限或代理问题 | 检查网络与代理；确认能访问 github.com |
| 组织席位限制 | 无法修改计划 | 由组织统一分配 | 联系组织管理员，个人不能改 |
| 代码无法运行 | 采纳后编译报错 | 建议只是"最可能的后续"，不保证正确 | 运行测试验证；不信任 AI 写的边界逻辑 |

## 9. 一句话记忆

**Copilot 是坐在你身边的 AI 结对编程助手：注释写清楚它就能接代码，选中代码就能问它；订阅先免费后按需升级，用 copilot-instructions.md 给它立规矩——但永远记住：AI 的建议要审查，正确性最终由你负责。**

### 延伸阅读（站内文档）

- 用 GitHub CLI 安装 Copilot 扩展，见 004-github 模块《GitHubCLI》。
- AI 生成代码的安全审查，见 004-github 模块《CodeQL代码扫描》。
- 自动更新依赖的机器人，见 004-github 模块《Dependabot》。
- 项目代码规范文件（配合 copilot-instructions 使用），见 004-github 模块《Gitignore配置》。



<!-- ============ 文档分隔线：004-github/016-Dependabot.md ============ -->



## 0. 先讲一个故事：依赖被攻击的那个夜晚

凌晨 2 点，运维群里炸了锅。

"线上服务异常，请求大量 500 报错！"

你爬起来打开日志，发现攻击者的 payload 正在利用一个**已知漏洞**——而漏洞所在的地方，不是你的代码，而是你三个月前安装的一个 npm 依赖包。你翻遍 release notes 才发现：这个包上个月就发布了修复版本，漏洞公告也早就公开了，只是**没有人看到，也没有人更新**。

第二天复盘时，大家总结出一个扎心的结论：**不是不会出问题，而是问题出在"没人及时发现、没人及时更新"上**。

如果那晚，你的仓库里有一位"自动体检医生"，故事的结局会完全不同：

- 漏洞公开的**当天**，它就会拉响警报，告诉你"你的依赖 X 中招了"。
- 修复版本发布后，它会**自动开好"处方"**——一个升级依赖的 PR，附带 CI 检查。
- 你白天打开电脑，只需要像审阅普通 PR 一样点一下"合并"。

这位"自动体检医生"就是 **Dependabot**——GitHub 内置的依赖管理机器人。它承担三件工作：**体检（漏洞告警）、开药（安全更新）、保健（版本更新）**。

本文用**故事驱动**的结构展开：从"出事那晚"出发，带你认识 Dependabot 的三大职责，然后手把手配置它，最后学会让机器人"听话"（分组、忽略、自动合并）。

## 1. Dependabot 是谁：三种角色一张表

Dependabot 本质上是 GitHub 的官方机器人账号（`dependabot[bot]`）。它有三个相互独立的职责：

| 职责 | 触发条件 | 动作 | 是否需要配置文件 |
| :--- | :--- | :--- | :--- |
| **Dependabot Alerts（体检）** | 依赖被披露存在漏洞/恶意包 | 在 Security 选项卡生成告警 | 否（设置页开关） |
| **Security Updates（开药）** | 存在漏洞告警且可用安全版本 | 自动创建修复 PR | 否（设置页开关） |
| **Version Updates（保健）** | 按计划定期检查新版本 | 自动创建版本升级 PR | **是（dependabot.yml）** |

注意一个关键区别：**Dependabot alerts 不能用 dependabot.yml 配置**，它由仓库设置控制；`dependabot.yml` 只控制版本更新（部分选项同时影响安全更新 PR 的样式）。

## 2. 第一幕：体检——Dependabot Alerts

### 2.1 原理：警报是怎么响起来的

Dependabot 做两件事：

1. 扫描仓库中的清单文件与锁定文件（依赖图谱提供数据）。
2. 与 GitHub Advisory Database（GitHub 漏洞公告数据库）交叉比对。

一旦发现你的依赖版本落在漏洞影响范围内，就在仓库的 **Security → Dependabot** 页面生成告警。**触发的三种时机**：

- 新漏洞披露并进入数据库。
- 已有漏洞公告更新（严重性、受影响版本变化）。
- 依赖图谱变化引入了新的脆弱依赖。

### 2.2 告警长什么样

一条典型的告警包含：

- 依赖名称、当前版本、受影响版本范围。
- 漏洞描述与 CVSS 严重性评分。
- 传播路径（哪个直接依赖把漏洞包带进来的）。
- 推荐的修复版本。

### 2.3 操作：启用体检

```
仓库 → Settings → Code security and analysis → Dependabot alerts → Enable
```

对**公开仓库免费且默认启用**（视账号设置）；私有仓库需在设置中开启。

### 2.4 管理告警

- 每个告警可标记为：打开 / 关闭（需说明理由：已修复、误报、暂不处理）。
- 支持按严重性、生态系统、依赖名筛选。
- 告警数据可通过 REST API 拉取，用于团队安全看板。

## 3. 第二幕：开药——Security Updates

### 3.1 原理：从告警到 PR 的自动化

启用安全更新后，当存在漏洞告警且**存在可用的安全版本**时，Dependabot 会自动创建修复 PR，把依赖升级到安全版本。PR 会：

- 自动触发仓库的 CI（如有）。
- 在说明中列出修复的 CVE 与严重性。
- 关联对应告警。

```markdown
# 典型的 Dependabot 安全更新 PR 说明

## Bumps lodash from 4.17.15 to 4.17.21

修复漏洞：
- CVE-2021-23337: Command injection（命令注入）
- CVE-2020-28500: ReDoS vulnerability（正则拒绝服务）

CVSS Score: 7.2 (High)

所有 CI 检查通过后可合并此 PR。
```

### 3.2 操作：启用开药

```
仓库 → Settings → Code security and analysis → Dependabot security updates → Enable
```

### 3.3 安全更新的边界

- 只升级到**修复漏洞的版本**，不做多余升级。
- 若生态系统中没有安全版本，则不创建 PR（需要你手动升级或换依赖）。
- 安全更新的 PR 同样受 `dependabot.yml` 中部分选项影响（如 reviewers、labels、groups）。

## 4. 第三幕：保健——Version Updates（版本更新）

### 4.1 原理：主动保持依赖新鲜

安全更新是"被动响应"（有漏洞才动）；版本更新是"主动保健"（按计划检查所有依赖是否有新版本，有就开 PR）。它**依赖语义化版本（SemVer）**而非依赖图谱，即使依赖没有漏洞也会工作。

### 4.2 操作：创建 dependabot.yml（核心步骤）

版本更新**必须**通过提交 `.github/dependabot.yml` 配置文件启用。文件有两个必需的顶层键：`version`（必须为 2）和 `updates`。

```yaml
# .github/dependabot.yml
version: 2
updates:
  # 配置块1：npm 前端依赖
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'          # 每周检查一次
      day: 'monday'               # 周一执行
      time: '09:00'
      timezone: 'Asia/Shanghai'

  # 配置块2：Python 后端依赖
  - package-ecosystem: 'pip'
    directory: '/backend'
    schedule:
      interval: 'monthly'

  # 配置块3：GitHub Actions 本身（工作流文件也要保持最新）
  - package-ecosystem: 'github-actions'
    directory: '/'
    schedule:
      interval: 'weekly'
```

提交该文件会**立即触发一次版本更新检查**，之后按 schedule 周期执行。

### 4.3 支持的生态系统速查

| 生态系统 | package-ecosystem 取值 | 识别文件 |
| :--- | :--- | :--- |
| npm / yarn | `npm` | `package-lock.json`、`yarn.lock` |
| pip | `pip` | `requirements.txt`、`Pipfile.lock` |
| Maven | `maven` | `pom.xml` |
| Gradle | `gradle` | `build.gradle` |
| Go | `gomod` | `go.mod`、`go.sum` |
| Cargo | `cargo` | `Cargo.lock` |
| NuGet | `nuget` | `*.csproj` |
| Docker | `docker` | `Dockerfile` |
| GitHub Actions | `github-actions` | 工作流文件 |

### 4.4 更新频率选择

| interval 取值 | 含义 | 适用场景 |
| :--- | :--- | :--- |
| `daily` | 每天检查 | 活跃开发、安全敏感项目 |
| `weekly` | 每周检查（推荐默认） | 大多数项目 |
| `biweekly` | 每两周 | 节奏稳定的团队 |
| `monthly` | 每月 | 维护模式、低频项目 |

## 5. 让机器人"听话"：高级配置

### 5.1 完整配置示例（带注释）

```yaml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
      day: 'saturday'
      time: '02:00'
    # 同时最多保持 5 个打开的更新 PR，避免刷屏
    open-pull-requests-limit: 5
    # 自动指派审查人与受让人
    reviewers:
      - 'dev-team'
    assignees:
      - 'tech-lead'
    # 自动打标签
    labels:
      - 'dependencies'
      - 'automated'
    # 提交信息风格
    commit-message:
      prefix: 'chore'
      include: 'scope'
    # 允许只更新生产依赖
    allow:
      - dependency-type: 'production'
    # 忽略特定依赖或大版本
    ignore:
      - dependency-name: 'webpack'
        versions: ['>=5.0.0']
      - dependency-name: 'lodash'
    # 有冲突时自动变基
    rebase-strategy: 'auto'
    # 目标分支
    target-branch: 'develop'
```

### 5.2 分组更新：把多个小 PR 合成一个

依赖多时，每天开 5 个 PR 会淹没团队。用 `groups` 把同类的合并成一个 PR：

```yaml
version: 2
updates:
  - package-ecosystem: 'npm'
    directory: '/'
    schedule:
      interval: 'weekly'
    groups:
      # 把所有测试相关依赖的更新合并为一个 PR
      test-dependencies:
        patterns:
          - 'jest*'
          - '*vitest*'
      # 所有小版本升级合并为一个 PR
      minor-and-patch-updates:
        applies-to: version-updates
        update-types:
          - 'minor'
          - 'patch'
```

分组后 PR 数量大幅减少，审查成本显著下降。

### 5.3 检查 Dependabot 运行状态

```
仓库 → Insights → Dependency graph → Dependabot
```

可查看每个更新作业的状态、日志与最近一次检查结果，排查"为什么没开 PR"。

## 6. 自动化流水线：让 PR 自己跑完 CI 并自动合并

### 6.1 原理：Dependabot PR 也是 PR

Dependabot 创建的 PR 与普通 PR 一样会触发 CI。合理配置后，安全补丁类更新可以做到"CI 通过即合并"，把人工负担降到最低。

### 6.2 自动合并工作流

```yaml
# .github/workflows/auto-merge.yml
name: Auto Merge Dependabot PRs
on: pull_request

permissions:
  contents: write
  pull-requests: write

jobs:
  auto-merge:
    runs-on: ubuntu-latest
    # 只处理 Dependabot 机器人创建的 PR
    if: ${{ github.actor == 'dependabot[bot]' }}
    steps:
      - name: 查看 PR 元数据
        id: metadata
        uses: dependabot/fetch-metadata@v2
        with:
          alert-lookup: true

      - name: 启用自动合并
        run: gh pr merge --auto --merge "$PR_URL"
        env:
          PR_URL: ${{ github.event.pull_request.html_url }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 6.3 条件自动合并：只合并安全更新

```yaml
      - name: 只对安全更新启用自动合并
        run: |
          if [ "${{ steps.metadata.outputs.update-type }}" = "version-update:semver-patch" ] || \
             [ "${{ steps.metadata.outputs.update-type }}" = "version-update:semver-minor" ]; then
            gh pr merge --auto --squash "$PR_URL"
          fi
```

注意：自动合并仍受**分支保护规则**约束（如"必须通过 CI""必须有代码所有者批准"）。如果团队对某些目录设置了 CODEOWNERS 强制审查，自动合并同样会等待批准，这是有意为之的安全兜底。

## 7. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 配置后没有 PR | Dependabot 页面显示 "no updates" | `directory` 写错、清单文件不在该目录，或依赖已是最新 | 用 Insights → Dependency graph → Dependabot 查看作业日志 |
| YAML 报错 | `Dependabot couldn't parse the config file` | 缩进错误、键名拼写错误 | 对照官方配置选项参考逐项核对；文件必须以 `version: 2` 开头 |
| 每天 PR 太多，刷屏 | 邮件轰炸 | 未设置 `open-pull-requests-limit`，或 interval 过密 | 设置 `open-pull-requests-limit: 5`；改用 weekly；用 `groups` 合并 |
| 大版本升级导致构建失败 | CI 红 | 破坏性变更（breaking changes） | 用 `ignore` 排除大版本；升级前阅读 release notes；分批升级 |
| 安全更新不自动开 PR | 有告警但无 PR | 安全更新开关未启用，或无安全版本可用 | Settings 启用 Security updates；手动升级或更换依赖 |
| 自动合并不生效 | PR 挂起不合并 | 分支保护要求审查/CI 未通过；或 workflow 权限不足 | 确认保护规则放行；为 workflow 声明 `pull-requests: write`、`contents: write` 权限 |
| 私有注册源（私有 npm 包）无法更新 | 401 认证失败 | Dependabot 无法访问私有仓库 | 在 dependabot.yml 中添加 `registries` 配置并设置认证凭据 |

## 9. 一句话记忆

> **Dependabot 是你的"自动体检医生"：Alerts 负责发现漏洞（体检）、Security Updates 负责自动修复（开药）、Version Updates 按计划保持依赖新鲜（保健），一份 dependabot.yml 就能让它在你的仓库"上岗"。**

### 官方文档

- Dependabot 版本更新配置（dependabot.yml 选项参考）：https://docs.github.com/zh/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file
- Dependabot alerts 文档：https://docs.github.com/zh/code-security/dependabot/dependabot-alerts/about-dependabot-alerts
- 配置 Dependabot 安全更新：https://docs.github.com/zh/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates
- Dependabot 官方元数据 Action（fetch-metadata）：https://github.com/dependabot/fetch-metadata

### 延伸阅读
- 依赖安全选项（供应链攻击原理与四道防线），见 004-github 模块 010 文档。
- 密钥扫描（另一种自动安全防线），见 004-github 模块 018 文档。
- GitHub Actions CI/CD（自动合并工作流的载体），见 004-github 模块 029 文档。



<!-- ============ 文档分隔线：004-github/017-IssuesTemplateTagMilestone.md ============ -->



## 0. 从一个生活场景说起：意见箱与工单系统

想象一家公司在大堂放了一个**意见箱**：起初大家随手写纸条，内容五花八门——有吐槽、有报障、有提建议，字迹潦草、信息不全，客服根本没法处理。后来公司升级成**工单系统**：每张工单必须填"问题类型、紧急程度、复现步骤、期望结果"；系统给工单打上**分类标签**（故障/建议/行政），并按**月度目标**统计解决进度。公司顿时高效起来。

GitHub 的 **Issues** 就是这套"工单系统"：**Issue 模板** 统一填写格式，**Labels（标签）** 分类筛选，**Milestones（里程碑）** 聚合进度。本篇采用**清单驱动**的结构，以"可照做的清单"为主线，教你搭好这套问题跟踪体系。

## 1. 原理讲解：Issue 体系三件套

| 组件 | 生活类比 | 作用 |
| :--- | :--- | :--- |
| Issue 模板 | 工单格式 | 让报告者按标准填写，信息完整可处理 |
| Labels | 分类标签 | 一眼看清类型、优先级、状态 |
| Milestones | 月度目标 | 聚合一批 Issue，跟踪版本/迭代进度 |

三者配合：**模板保证"输入规范"，标签保证"分类清晰"，里程碑保证"目标可见"**。

## 2. 清单一：Issue 模板配置

### 2.1 目录结构清单

在仓库创建 `.github/ISSUE_TEMPLATE/` 目录，放入模板文件：

```mermaid
graph TD
  A[".github/"] --> B["ISSUE_TEMPLATE/"]
  B --> C["bug_report.md（Bug 报告模板）"]
  B --> D["feature_request.md（功能请求模板）"]
  B --> E["question.md（提问模板，可选）"]
  B --> F["config.yml（模板选择页配置）"]
```

### 2.2 Bug 报告模板（可直接使用）

每个模板文件开头用 YAML frontmatter 声明元数据，后面是 Markdown 正文：

```markdown
---
name: Bug 报告
about: 报告可复现的缺陷
title: "[BUG] "
labels: bug
assignees: ''
---

## 环境信息
- 操作系统：
- 浏览器/版本：
- 应用版本：

## 复现步骤
1.
2.
3.

## 期望行为
（描述你期望的结果）

## 实际行为
（描述实际发生的情况）

## 截图
（如有，请附截图）

## 额外信息
```

### 2.3 功能请求模板（可直接使用）

```markdown
---
name: 功能请求
about: 建议新功能
title: "[FEATURE] "
labels: enhancement
assignees: ''
---

## 功能描述
（简要描述希望添加的功能）

## 问题背景
（解释为什么需要这个功能，它解决什么问题）

## 实现建议
（描述希望如何实现）

## 额外信息
```

### 2.4 模板选择页配置（config.yml）

```yaml
blank_issues_enabled: false
contact_links:
  - name: 社区讨论
    url: https://github.com/org/repo/discussions
    about: 一般问题请到讨论区提问
  - name: 官方文档
    url: https://docs.example.com
    about: 先查文档，避免重复提问
```

> 设置 `blank_issues_enabled: false` 后，用户必须从模板中选择一种创建 Issue，空模板被禁用。

## 3. 清单二：标签体系（Labels）

### 3.1 建议标签分类清单

| 分类 | 标签示例 | 用途 |
| :--- | :--- | :--- |
| 类型 | `bug`、`enhancement`、`documentation`、`question` | 这是什么问题 |
| 优先级 | `priority:high`、`priority:medium`、`priority:low` | 多紧急 |
| 状态 | `needs-triage`、`in-progress`、`review-needed` | 处理到哪一步 |
| 难度 | `good-first-issue`、`help-wanted` | 适合谁来做 |
| 模块 | `frontend`、`backend`、`api`、`database` | 涉及哪个模块 |

> `good first issue` 是 GitHub 官方推荐的引导新手标签：标了它，新手可以在仓库的 "Good first issues" 筛选器里找到合适任务，开源项目常用它培养贡献者。

### 3.2 标签使用规范清单

- **命名**：小写字母 + 连字符，如 `good-first-issue`。
- **颜色**：同类标签用相似颜色（优先级用红/黄/绿渐变）。
- **数量**：控制在 20-30 个以内，避免膨胀。
- **描述**：每个标签配一句用途说明，避免歧义。
- **统一**：组织内统一命名规范，跨仓库通用。

### 3.3 命令行管理标签

```bash
# 列出标签
gh label list
# 创建标签
gh label create bug --description "代码缺陷" --color d73a4a
# 修改标签
gh label edit bug --description "可复现的缺陷" --color d73a4a
# 删除标签
gh label delete bug --yes
```

## 4. 清单三：里程碑（Milestones）

### 4.1 创建里程碑清单

1. 仓库 **Issues → Milestones** → **New milestone**。
2. 填写**标题**（建议版本号或迭代名，如 `v1.0.0`、`Sprint 12`）、**描述**、**截止日期**。
3. 创建后把相关 Issue/PR 关联到里程碑（在 Issue 右侧栏选择）。

### 4.2 使用里程碑的收益

- 里程碑页面自动显示**完成百分比**（已关闭 / 总数）。
- 接近截止日期时高亮提醒，便于规划。
- 同一里程碑内的 Issue 聚合到一次发布中，发布后统一验证关闭。

### 4.3 里程碑规划建议

- 一个里程碑装 **10-20 个** Issue 比较合理，避免"过大无法交付"或"过小没有意义"。
- 每个里程碑有明确**目标与交付物**，拒绝把无关任务塞进来。
- 定期检查进度，发现无法按时完成时及时裁剪范围或调整日期。

### 4.4 Issue 撰写与维护最佳实践清单

无论用不用模板，以下习惯都能提升 Issue 的可处理性：

- **搜索先于创建**：开新 Issue 前先搜仓库，避免重复工单；重复的直接链接到旧 Issue 并关闭。
- **标题即结论**：用"现象一句话"做标题，如 `[BUG] 登录页在 Safari 下表单无法提交`，而不是"求助"。
- **描述五要素**：环境 / 复现步骤 / 期望行为 / 实际行为 / 截图（Bug 类必填）。
- **善用 Markdown**：用任务列表 `- [ ]` 拆分子任务，用 `@mention` 通知负责人，用 `#123` 交叉引用关联 Issue。
- **及时更新状态**：解决后关闭并简要说明"在 #PR 中修复"；长期搁置的 Issue 定期 triage（分类处理）。

## 5. 清单四：自动化与衔接

### 5.1 自动关闭 Issue 关键词

在 **commit message 或 PR 描述**中写入以下关键词，合并 PR 时会自动关闭对应 Issue：

- `Fixes #123`
- `Closes #123`
- `Resolves #123`
- `Closes #123, #456`（同时关闭多个）

> 注意：只有 PR 合并到**默认分支**时才会触发自动关闭；fork 仓库需使用跨仓库引用格式。

### 5.2 GitHub Actions 自动打标签

```yaml
name: Label issues
on:
  issues:
    types: [opened]
jobs:
  label:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: actions/labeler@v5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          configuration-path: .github/labeler.yml
```

配合 `.github/labeler.yml` 按路径/标题关键词自动分配标签。

### 5.3 自动分配 Issue

```yaml
name: Auto assign
on:
  issues:
    types: [opened]
jobs:
  assign:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - uses: pozil/auto-assign-issue@v2
        with:
          assignees: dev-team
          numOfAssignee: 1
```

### 5.4 与项目板（Projects）衔接

把 Issue 拖入项目板（To Do / In Progress / Review / Done 列），通过移动卡片更新状态，看板即"工单流转墙"——新工单进 To Do，认领后进 In Progress，修复合并后进 Done 并自动关闭。

### 5.5 安全漏洞上报：Security advisories

**不要在公开 Issue 中报告安全漏洞**——漏洞细节一旦公开，等于给攻击者递刀。正确做法：

1. 在仓库创建 `SECURITY.md`，说明漏洞上报渠道（建议用"私密漏洞报告"功能，见 019/018 篇）。
2. 维护者通过 **Security → Security advisories** 创建私有通告，与报告者私密沟通细节。
3. 修复发布后，再选择公开通告并登记 CVE 编号。

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 模板不显示 | 新建 Issue 时没有模板选项 | 模板路径错误或 YAML frontmatter 语法错误 | 确认文件在 `.github/ISSUE_TEMPLATE/` 下；检查 `---` 块格式；确认仓库启用了 Issues 功能 |
| 空模板无法禁用 | 用户仍可开空白 Issue | config.yml 未配置或格式错误 | 配置 `blank_issues_enabled: false` 并推送到默认分支 |
| 自动关闭不生效 | 合并后 Issue 仍开着 | 关键词未写进 PR 描述/提交信息；PR 未合并到默认分支 | 在 PR 描述写 `Closes #123`；确认合并到默认分支 |
| 标签过多难管理 | 标签列表失控 | 无规范随意创建 | 清理合并相似标签；按第 3.2 节规范统一命名 |
| 里程碑进度不准 | 完成百分比与实情不符 | 部分 Issue 未关联里程碑或状态未更新 | 把所有相关 Issue 关联到里程碑；及时关闭已解决的 Issue |
| Actions 自动化失败 | 打标签/分配任务工作流报错 | GITHUB_TOKEN 权限不足或 workflow 语法错误 | 检查 `permissions` 字段；查看 Actions 日志定位语法问题 |

## 8. 一句话记忆

**Issue 是"工单"，模板保证工单填得全，标签让工单分得清，里程碑让目标看得见，Actions 让流转自动化——四件套齐了，问题跟踪不再靠吼。**

### 延伸阅读

- gh CLI 管理 Issue 与标签的命令速查，见 048 篇《Gh Issue 管理》与 056 篇《Gh Label》。
- 项目看板（Projects）使用，见 012 篇《Projects 看板》。
- 社区健康文件（CONTRIBUTING 等），见 026 篇《社区健康文件》。
- 安全漏洞上报（Security advisories），见 019/018 篇。



<!-- ============ 文档分隔线：004-github/018-SecretScanning.md ============ -->



## 0. 先来一个生活场景：保险箱与监控

你家的保险箱里放着银行卡、存折和房产证。你给自己定了三条规矩：

1. **保险箱不随手放在客厅**——它的存在本身就容易被盯上。
2. **出门前检查门窗**——别等小偷进屋了再后悔。
3. **如果钥匙真的丢了，第一时间换锁**——而不是祈祷小偷不来。

软件世界里的"保险箱"就是你的**密钥（Secret）**：API Key、Token、数据库密码、SSH 私钥。而最危险的存放方式，就是把它**硬编码进代码并推到 GitHub**。

为什么这么危险？因为 GitHub 是给全世界看的。你推送到**公开仓库**的每一个 commit 都会被永久保存——即使你马上删除，克隆过、fork 过、缓存过的副本依然存在。GitHub 官方的说法很直接：**推送到公共仓库的密钥应视为已泄露**。攻击者会用自动化爬虫扫描 GitHub 上所有公开的密钥模式，一秒钟就能把你的 AWS 账号、云服务器、支付接口接管。

GitHub 的**密钥扫描（Secret Scanning）**就是你的"监控 + 门窗检查 + 换锁提醒"：

- 扫描仓库历史，找出已泄露的密钥（监控）。
- **推送保护（Push Protection）**在你 push 之前拦截含密钥的代码（门窗检查）。
- 发现泄露后告诉你**立即撤销密钥**（换锁提醒）。

本文按**原理驱动**的结构展开：先讲透"密钥泄露为什么可怕"，再讲 GitHub 如何自动发现（两类扫描：事后扫描与推送保护），最后讲泄露后的补救。

## 1. 原理：密钥泄露为什么可怕

### 1.1 直观理解：密钥 = 通行证

```javascript
// 危险写法：密钥直接写在代码里
const AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE";

// 危险：一旦这个文件被 push 到公开仓库
// → 爬虫扫描到 → 用你的 AWS 密钥调用云服务 → 账单爆炸 / 数据泄露
```

密钥的本质是**服务的通行证**：AWS Access Key 可以操作你的云资源，Stripe Secret Key 可以扣用户的钱，GitHub Token 可以读写你的仓库。拿到通行证，攻击者不需要攻破你的服务器，直接以你的身份登录。

### 1.2 原理：公开仓库的"永久存档"效应

很多人以为"我删掉文件再 push 一次就没事了"。事实是：

1. **历史记录保留**：Git 的每一次 commit 都永久保存在 `.git` 历史中，`git log` 随时能翻出来。
2. **fork 扩散**：别人 fork 过的副本，不会因为你的删除而消失。
3. **缓存与爬虫**：GitHub 的缓存、第三方爬虫、代码搜索索引都会留下副本。

所以结论只有一个：**密钥一旦进入公开仓库，就当它已经泄露，立即撤销重建**。这正是 GitHub 密钥扫描存在的意义——帮你"尽早发现，尽早换锁"。

### 1.3 原理：GitHub 如何"认出"密钥

密钥扫描使用**模式匹配（Pattern Matching）**技术：为每一种密钥类型定义"指纹"（正则表达式），例如 GitHub Token 以 `ghp_` 开头，AWS Access Key 以 `AKIA` 开头。扫描时逐行比对，命中即告警。GitHub 支持的模式分三类：

| 类别 | 说明 | 检测方式 | 示例 |
| :--- | :--- | :--- | :--- |
| **通用模式** | 不绑定具体服务商，如私钥、数据库连接串 | 正则 | `rsa_private_key` |
| **服务商模式** | 绑定具体服务商，如 AWS、Azure、Stripe | 正则 | `aws_access_key_id` |
| **AI 检测模式** | 密码等非结构化密钥 | AI 模型 | `password` |

目前 GitHub 支持检测 **200 种以上**的密钥类型，且持续扩充（GitHub 官方 changelog 显示每个季度都会新增模式）。

## 2. 密钥扫描：事后扫描（发现已泄露的密钥）

### 2.1 原理：扫描什么

密钥扫描会对仓库的**全部内容**进行检查，包括：

- 所有分支的提交历史。
- PR 描述、Issue 描述、评论。
- 上传到仓库的文件（拖拽上传）。

**三种告警类型**：

| 告警类型 | 展示位置 | 触发场景 |
| :--- | :--- | :--- |
| **用户告警** | 仓库 Security 与质量选项卡 | 检测到受支持的密钥模式 |
| **推送保护告警** | 同上 | 有人绕过推送保护强行推送 |
| **合作伙伴告警** | 直接通知密钥对应的服务商 | 命中 Partner 计划内模式，服务商可协助撤销 |

特别值得一提的是 **Partner 告警**：GitHub 与 AWS、Azure、Google、Slack、Stripe 等服务商合作，发现对应模式的密钥后会**直接通知服务商**，服务商可以主动采取保护措施（如封禁该密钥）。

### 2.2 操作：查看告警

```
仓库 → Security → Secret scanning alerts
```

每条告警显示：密钥类型、文件路径、所在行、检测时间、泄露位置（commit/PR/Issue）。

### 2.3 处理告警

- **撤销密钥**：到对应服务平台删除并重新生成（第 5 节详述）。
- **标记告警状态**：修复后标记为"已解决"；误报可关闭并说明原因。
- **告警分级**：可按严重性、密钥类型筛选，优先处理服务商模式的真实密钥。

## 3. 推送保护：出门前的门窗检查

### 3.1 原理：把风险挡在 push 之前

事后扫描是"进门后的监控"——密钥已经进了仓库才报警。**推送保护（Push Protection）**更进一步：在 `git push` 提交到 GitHub 的瞬间检查内容，发现密钥就**拦截推送**，并提示开发者处理。

推送保护覆盖的入口不仅限于命令行 push，还包括：GitHub 网页编辑提交、文件上传、REST API 请求等。

### 3.2 工作流程

```mermaid
flowchart TD
    T0["开发者执行 git push"]
    T1["GitHub 检查推送内容"]
    T2["发现密钥模式？"]
    T3["是 → 拦截推送，显示警告"]
    T4["选项1：移除密钥后重新推送"]
    T5["选项2：确认为误报 → 申请放行"]
    T6["否 → 正常推送"]
    T0 --> T1
    T1 --> T2
    T2 -->|是| T3
    T3 --> T4
    T3 --> T5
    T2 -->|否| T6
```

### 3.3 操作：启用推送保护

```
仓库 → Settings → Code security and analysis → Secret scanning → Push protection → Enable
```

也可以在组织级别统一启用，对所有仓库生效。

### 3.4 被拦截时的处理

当你 push 被拦截，GitHub 会给出详细提示：

```
remote: error: Push blocked.
remote: 检测到疑似密钥：AWS Access Key ID
remote: 文件：src/config.js，第 12 行
remote: 请移除密钥后重试，或确认这是测试数据后提交绕过申请。
```

- **正确做法**：移除硬编码的密钥，改用环境变量，重新提交。
- **确认是测试数据/误报**：在网页端填写原因申请放行（管理员可审核放行记录）。
- **强烈不建议**：绕过保护。每次绕过都会生成"推送保护绕过告警"，管理员可见。

## 4. 自定义模式：识别"你家的专属密钥"

内置模式覆盖主流服务商，但你可能有用自家服务的密钥格式（例如 `MYCOMPANY_API_KEY_` 开头）。此时可定义**自定义模式（Custom Patterns）**。

### 4.1 操作：添加自定义模式

```
仓库（或组织）→ Settings → Code security and analysis → Custom patterns → New pattern
```

配置要点：

- **Pattern name**：模式名称。
- **Secret format**：正则表达式（描述密钥格式）。
- **Test strings**：提供测试样例，验证匹配效果。
- **Save and dry run**：先"试运行"扫描，查看命中结果，确认无误报后再发布（Publish）。

### 4.2 正则示例

```regex
# 示例：检测自家服务的 API Key（32 位字母数字）
MYCOMPANY_API_KEY=[A-Za-z0-9]{32}

# 示例：检测带前缀的密钥对
# 前缀 MYCO-，后接 4 组 4 位十六进制
MYCO-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}
```

**写自定义模式的三个原则**：

1. **宁可漏报、不要误报**：太宽泛的正则（如 `[A-Za-z0-9]{20}`）会匹配大量正常文本，淹没真实告警。
2. **利用周边上下文**：把密钥名（如 `api_key =`）也纳入正则，提高精度。
3. **先用 dry run 验证**：在仓库上试运行，检查命中样本是否符合预期。

## 5. 泄露了怎么办：四步换锁流程

如果密钥已经泄露（无论是被扫描发现还是自己发现），按以下顺序操作：

### 5.1 第一步：撤销并重建密钥（最重要）

```
1. 登录密钥对应的服务平台（AWS / GitHub / Stripe 等）
2. 删除/撤销泄露的密钥
3. 生成新的密钥
4. 更新使用方（环境变量、CI 配置、服务器）
```

**注意顺序**：先撤销旧的，再启用新的，避免服务中断。

### 5.2 第二步：从代码与历史中移除

```bash
# 把密钥从当前代码中移除，改用环境变量
# 使用 git filter-repo 从历史中彻底清除（如有需要）
git filter-repo --path src/config.js --invert-paths

# 强制推送（会改写历史，需与团队协调）
git push --force --all
```

**重要**：改写历史只能减少扩散，不能消除已泄露的事实——**撤销密钥才是根本**。另外 `git push --force` 会改写历史，破坏团队协作，操作前必须与协作者沟通并遵守分支保护规则。

### 5.3 第三步：审查暴露范围

- 在 GitHub 搜索框用 `"泄露密钥片段"` 搜索你的密钥是否出现在其他公开仓库。
- 检查该仓库的 fork 列表、Actions 日志（密钥可能被写入日志）。
- 检查密钥是否有对应服务的操作记录（账单、登录日志），评估实际损失。

### 5.4 第四步：防止再次发生

- 用 `.gitignore` 排除含密钥的文件（见 008 文档）。
- 使用环境变量 + GitHub Secrets 存储密钥。
- 安装本地预提交钩子，push 前本地检测：

```bash
# 安装 detect-secrets 并配置 pre-commit 钩子
pip install detect-secrets pre-commit
detect-secrets scan > .secrets.baseline
pre-commit install
```

## 6. 配套知识：用 GitHub Secrets 存储密钥（而不是硬编码）

密钥扫描解决"发现"；**存储方案**解决"根本不用硬编码"。GitHub 提供多层密钥存储：

### 6.1 仓库级 Secrets（Actions 使用）

```bash
# 设置密钥（交互式输入）
gh secret set DATABASE_URL

# 从字符串设置
gh secret set API_KEY --body "sk-12345"

# 从文件读取
gh secret set DEPLOY_KEY < ~/.ssh/id_rsa

# 列出（不显示值）与删除
gh secret list
gh secret delete API_KEY
```

### 6.2 组织与环境级 Secrets

```bash
# 组织级密钥（对指定仓库可见）
gh secret set DEPLOY_TOKEN --org myorg --repos "repo1,repo2"

# 环境级密钥（仅生产环境部署可用）
gh secret set DB_PASS --env production
```

### 6.3 在 Actions 工作流中使用

```yaml
# .github/workflows/deploy.yml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: 使用密钥
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: ./deploy.sh
```

## 7. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| push 被拦截 | `Push blocked. Secret detected...` | 推送内容包含密钥模式 | 移除硬编码密钥改用环境变量后重推；确为测试数据再申请放行 |
| 以为删除文件就安全了 | 密钥扫描仍提示历史泄露 | Git 历史永久保留、fork 扩散 | 撤销密钥重建（第一优先级）；需要时用 git filter-repo 清理历史 |
| 自定义模式疯狂误报 | 告警全是正常文本 | 正则过宽 | 缩小匹配范围；利用密钥名上下文；先用 dry run 验证 |
| 密钥扫描不生效 | 设置页无密钥扫描选项 | 仓库类型/套餐不支持，或未启用 | 公开仓库免费；私有仓库需组织启用对应安全功能 |
| 泄露后只清理不撤销 | 攻击者仍在用密钥 | 清理代码不影响已泄露的密钥 | 先在服务端撤销重建，再清理代码 |
| 把密钥放进 .env 却提交了 .env | 密钥随仓库公开 | `.gitignore` 未配置或 .env 已被跟踪 | 用 `git rm --cached .env` 停止跟踪；撤销密钥；配置 .gitignore |

## 9. 一句话记忆

> **密钥是服务的通行证，进了公开仓库就等于交了底——Secret Scanning 负责找出已泄露的密钥（监控），Push Protection 负责在 push 前拦截（门窗检查），而真正的救命稻草永远是"撤销重建"（换锁）。**

### 官方文档

- 关于密钥扫描（GitHub 官方）：https://docs.github.com/zh/code-security/secret-scanning/introduction/about-secret-scanning
- 关于推送保护：https://docs.github.com/zh/code-security/secret-scanning/push-protection-for-repositories/about-push-protection-for-repositories
- 支持的密钥扫描模式（200+ 类型清单）：https://docs.github.com/zh/code-security/secret-scanning/introduction/supported-secret-scanning-patterns
- 定义自定义模式：https://docs.github.com/zh/code-security/secret-scanning/customizing-secret-scanning/defining-custom-patterns-for-secret-scanning

### 延伸阅读
- Gitignore 配置（用 .gitignore 排除敏感文件），见 004-github 模块 008 文档。
- CodeQL 代码扫描（另一类自动安全防线），见 004-github 模块 019 文档。
- Dependabot（依赖漏洞自动修复），见 004-github 模块 016 文档。



<!-- ============ 文档分隔线：004-github/019-CodeQLCodeScanning.md ============ -->



## 0. 先来一个生活场景：安检机

坐飞机时，你的行李箱会经过一台**安检机（X 光安检机）**。它不需要打开你的箱子，就能"看透"里面的物品结构：那把剪刀是不是藏在雨伞里、那个瓶子里的液体是不是超规——它分析的是**物品的形状、材质、结构关系**，而不是只看表面标签。

传统的代码检查工具（Linter）就像"看标签"：只检查"这行代码是不是符合语法格式"，看到 `=` 少了、分号丢了就报警。但很多漏洞**长得完全正常**：

```python
# 这行代码语法完美，但它是 SQL 注入漏洞
cursor.execute("SELECT * FROM users WHERE name = '" + user_input + "'")
```

语法检查器看不出问题，因为它不理解"`user_input` 是用户的输入，被拼进了 SQL 语句"这层**语义关系**。而 **CodeQL** 就是代码世界的"安检机"——它不打开你的"箱子"（不运行你的程序），但能通过分析代码的**结构关系**（谁调用谁、数据从哪里流到哪里）发现深藏的危险。

CodeQL 是 GitHub 开发的**静态代码分析引擎**，是 GitHub **代码扫描（Code Scanning）**功能的默认引擎。它的工作方式极具特色：先把你的代码"编译"成一个**CodeQL 数据库**（相当于给箱子拍了一张 3D 透视照片），然后在这张"照片"上运行**查询**（相当于安检员用培训过的眼睛扫描），最后把发现的问题作为**代码扫描告警（Code scanning alerts）**展示在 GitHub 上。

本文以"安检机"为线索展开：先讲 CodeQL 的透视原理（数据库与查询），再讲如何部署这台安检机（默认设置与高级设置），最后讲如何看懂告警并定制自己的"安检规则"（自定义查询）。

## 1. 原理：CodeQL 这台"安检机"是怎么工作的

### 1.1 直观理解：三步流程

```
源代码（你的行李）
    ↓ 第一步：提取（透视拍照）
CodeQL 数据库（3D 结构照片）
    ↓ 第二步：查询（安检扫描）
安全漏洞 / 代码缺陷（可疑物品清单）
    ↓ 第三步：上传（出具报告）
GitHub 上的代码扫描告警
```

### 1.2 原理：数据库（Database）

CodeQL 数据库不是"代码的副本"，而是代码的**关系化表示**。它提取了代码中的实体（类、函数、变量）和关系（谁调用谁、谁继承谁、数据流经哪些路径），存入关系数据库。这一步对**编译型语言**（C/C++、C#、Go、Java、Kotlin、Swift）尤其重要：需要先**构建代码**再提取数据；对解释型语言（JavaScript、Python、Ruby）则直接解析。

### 1.3 原理：查询（Query）

CodeQL 自带一套用 **QL 语言**写成的"标准安检规则库"（查询套件），覆盖常见漏洞类型：

| 漏洞类型 | 通俗解释 |
| :--- | :--- |
| SQL 注入 | 把用户输入拼进 SQL 语句 |
| XSS（跨站脚本） | 把用户输入直接输出到网页 |
| 路径遍历 | 用用户输入拼文件路径 |
| 不安全的反序列化 | 解析不可信数据时执行任意代码 |
| 硬编码凭证 | 代码里写死了密码/密钥 |
| 不安全的随机数 | 用可预测的随机数做安全用途 |

### 1.4 关键概念：语义分析 vs 语法检查

| 维度 | 传统 Linter | CodeQL |
| :--- | :--- | :--- |
| 分析对象 | 单行语法 | 全库结构关系 |
| 能否跨函数追踪 | 否 | 能（数据流分析） |
| 理解用户输入传播 | 否 | 能（污点分析） |
| 误报率 | 低 | 中（需人工确认） |
| 发现深层漏洞 | 差 | 强 |

**污点分析（Taint Analysis）**是 CodeQL 最核心的能力：它标记"不可信输入"（如 HTTP 请求参数），追踪它如何流经函数调用链，最终到达危险操作（如数据库查询）。这正是安检机"看透箱子内部结构"的技术实现。

## 2. 部署这台"安检机"：两种配置方式

GitHub 提供**默认设置（Default Setup）**和**高级设置（Advanced Setup）**两种部署方式。

### 2.1 方式一：默认设置（推荐新手，零配置）

仓库 → Settings → Code security and analysis → Code scanning → Set up → Default

默认设置自动完成三件事：

- 自动选择需要分析的语言。
- 自动选择查询套件（默认 security-and-quality）。
- 自动配置扫描触发时机（push / pull_request / 每周定时全量扫描）。

适合绝大多数项目，几分钟内即可上线。

### 2.2 方式二：高级设置（可定制工作流）

高级设置会在仓库生成一个可编辑的工作流文件 `.github/workflows/codeql.yml`：

```yaml
# .github/workflows/codeql.yml
name: "CodeQL"

on:
  push:
    branches: [ "main" ]            # 推送到 main 时扫描
  pull_request:
    branches: [ "main" ]            # PR 时扫描（早发现）
  schedule:
    - cron: '0 0 * * 1'             # 每周一 00:00 全量扫描

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      security-events: write         # 允许写入扫描结果
      actions: read
      contents: read

    strategy:
      fail-fast: false
      matrix:
        language: [ 'javascript-typescript', 'python' ]   # 要分析的语言

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      # 初始化 CodeQL（创建数据库）
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{ matrix.language }}
          config-file: ./.github/codeql/codeql-config.yml   # 可选：自定义配置

      # 自动构建（编译型语言自动识别构建方式）
      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      # 运行查询并上传结果
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v3
```

### 2.3 自定义配置：圈定扫描范围

```yaml
# .github/codeql/codeql-config.yml
name: "Custom CodeQL Config"

# 只扫描 src 和 lib 目录
paths:
  - src
  - lib

# 跳过测试目录（减少误报与耗时）
paths-ignore:
  - '**/test/**'
  - '**/tests/**'
  - '**/node_modules/**'

# 使用的查询套件
queries:
  - uses: security-and-quality          # GitHub 内置套件之一
  - uses: ./custom-queries/sql-injection.ql   # 自定义查询（第 4 节）
```

工作流中通过 `config-file` 引用该文件即可。

### 2.4 支持的语言

CodeQL 官方文档列出的支持范围（截至 2026 年）：

| 语言 | 数据库构建方式 | 分析类型 |
| :--- | :--- | :--- |
| JavaScript / TypeScript | 直接解析 | 安全 + 质量 |
| Python | 直接解析 | 安全 + 质量 |
| Java / Kotlin | 构建 | 安全 + 质量 |
| C / C++ | 构建 | 安全 + 质量 |
| C# | 构建 | 安全 + 质量 |
| Go | 构建 | 安全 + 质量 |
| Ruby | 直接解析 | 安全 |
| Swift | 构建 | 安全（beta 级支持） |
| Rust | 直接解析 | 安全（新支持） |

提示：`matrix` 中的语言标识符与日常叫法不同（如 JavaScript 在 CodeQL 中叫 `javascript-typescript`），配置时以官方文档为准。

## 3. 看懂安检报告：处理代码扫描告警

### 3.1 查看告警

```
仓库 → Security → Code scanning
```

每条告警包含：

- **漏洞类型**与严重级别。
- **触发位置**（文件 + 行号）。
- **数据流路径**（从输入到危险操作的完整链条，这是 CodeQL 的独门优势）。
- **修复建议**。

### 3.2 严重级别

| 级别 | 含义 | 处理建议 |
| :--- | :--- | :--- |
| Critical / Error | 确定的高危漏洞 | 立即修复 |
| Warning | 潜在安全问题 | 尽快评估 |
| Note | 建议性改进 | 择机处理 |

### 3.3 处理告警的三种动作

- **创建 Issue**：把告警转成 Issue 分派给负责人。
- **标记为已修复**：修复代码后让 GitHub 复核（扫描通过后自动关闭）。
- **关闭（忽略）**：误报时关闭，**必须填写原因**（如"此输入仅来自内部信任来源"），便于审计。

### 3.4 在 PR 中拦截漏洞

代码扫描默认会作为 PR 检查运行。可在分支保护规则中勾选 "Require status checks to pass before merging"，让存在高危告警的 PR 无法合并，把漏洞挡在合并之前。

## 4. 定制安检规则：编写 CodeQL 查询

CodeQL 的"安检规则"（查询）用 **QL 语言**编写。语法与 SQL 相似（`from` / `where` / `select`），但查询对象是代码结构而非数据表。

### 4.1 第一个查询：找出所有硬编码的密码赋值

```ql
/**
 * @name Hardcoded password
 * @description 检测硬编码的密码赋值
 * @kind problem
 * @id python/hardcoded-password
 * @severity warning
 */

import python

from Assignment a
where
  // 变量名包含 password / passwd / pwd
  a.target().toString().toLowerCase().matches("%password%") and
  // 赋值来源是字符串常量
  a.value() instanceof StrConst
select a, "疑似硬编码密码，请改用环境变量或密钥管理"
```

### 4.2 查询的结构解析

| 部分 | 作用 |
| :--- | :--- |
| 注释头（@name / @description / @kind / @severity） | 元数据，GitHub 据此展示告警 |
| `import python` | 导入语言库（换成 `javascript`、`java` 等即支持其他语言） |
| `from Assignment a` | 声明要遍历的实体（这里是"赋值语句"） |
| `where ...` | 过滤条件（这里是"目标含 password 且值为字符串"） |
| `select a, "提示信息"` | 输出命中的位置与提示 |

### 4.3 让自定义查询生效

```bash
# 方式1：通过配置文件（推荐）
# 在 codeql-config.yml 中：
#   queries:
#     - uses: ./custom-queries/sql-injection.ql
# 然后工作流 init 步骤传入 config-file

# 方式2：本地用 CodeQL CLI 验证
codeql database create mydb --language=python
codeql query run mydb ./custom-queries/sql-injection.ql
```

### 4.4 官方查询库（抄作业）

不必从零写查询。GitHub 官方维护了 [codeql](https://github.com/github/codeql) 仓库，内含海量查询。内置查询套件：

- `security-extended`：安全漏洞扩展套件。
- `security-and-quality`：安全 + 质量（推荐默认）。
- `security-experimental`：实验性查询（误报较多）。

## 5. 安检机的维护：最佳实践

1. **PR 阶段必扫**：在 pull_request 事件上运行，漏洞早发现、成本最低。
2. **定期全量扫描**：用 schedule 事件每周扫描一次，覆盖 PR 之外的代码。
3. **优先处理高危**：按严重级别排序，先修 Critical / High。
4. **误报要留痕**：关闭告警时写明原因，方便日后审计与模型改进。
5. **与其他防线配合**：CodeQL 查"自己代码"的漏洞，Dependabot 管"依赖"漏洞，Secret Scanning 管"密钥"泄露——三者互补（见 016、018 文档）。
6. **关注数据流路径**：告警自带"输入→危险操作"链路图，修代码时修源头（输入校验），而不是修末端。

## 6. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 编译型语言扫描失败 | `Autobuild failed` / 数据库为空 | 构建环境或构建命令未配置 | 高级设置中手动指定 build 步骤；确认依赖安装完整 |
| 扫描没覆盖所有代码 | 告警集中在部分目录 | 默认路径限制或语言未全选 | 在 codeql-config.yml 调整 paths；matrix 中补充语言 |
| `languages` 配置报错 | `Invalid language: javascript` | CodeQL 语言标识符与日常叫法不同 | 改用官方标识符（如 `javascript-typescript`） |
| 告警太多无从下手 | 上千条告警 | 默认套件 + 未排除测试代码 | 用 paths-ignore 排除测试；按严重级别筛选；用 default 设置的重扫减少噪音 |
| 误报处理不当 | 真实漏洞被误关闭 | 关闭告警未填写原因，或关闭条件判断错误 | 关闭时如实填写理由；高危误报建议先在本地复现验证 |
| 扫描时间过长 | CI 超时 | 仓库过大或语言过多 | 并行矩阵（fail-fast: false）；按目录拆分扫描；只扫改动文件（PR 模式） |
| 想让 PR 阻止合并 | 有漏洞仍合并了 | 未启用状态检查强制 | 分支保护规则勾选对应 status check 为 required |

## 8. 一句话记忆

> **CodeQL 是代码世界的"安检机"：它不看代码表面（语法），而是给代码拍"透视照片"（数据库）再用"规则眼睛"（查询）扫描——发现 SQL 注入、XSS 这类藏在结构里的深层漏洞，并在 PR 合并前拦下它们。**

### 官方文档

- 关于 CodeQL 代码扫描（GitHub 官方）：https://docs.github.com/zh/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning-with-codeql
- CodeQL 支持的语言与框架：https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/
- 自定义代码扫描（工作流与配置）：https://docs.github.com/zh/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/customizing-code-scanning
- GitHub 官方查询库 github/codeql：https://github.com/github/codeql

### 延伸阅读
- 密钥扫描（保护另一类资产：密钥），见 004-github 模块 018 文档。
- Dependabot（扫描"别人的代码"——依赖），见 004-github 模块 016 文档。
- 依赖安全选项（供应链安全全景），见 004-github 模块 010 文档。
- GitHub Actions 触发器（push / pull_request / schedule 详解），见 004-github 模块 030 文档。



<!-- ============ 文档分隔线：004-github/020-GitHubCLI.md ============ -->



## 0. 从一个生活场景说起：GitHub 的"遥控器"

看电视时，你很少走到电视机前按物理按钮，而是用**遥控器（GitHub CLI）** 懒洋洋地换台、调音量。GitHub CLI（命令 `gh`）就是 GitHub 网页版的"遥控器"：不用在浏览器里点来点去，在终端里敲一行命令，就能完成建仓库、提 PR、管 Issue、查 Actions 等几乎全部操作。

本篇采用**工具驱动**的结构：先安装"遥控器"（安装认证），再逐个"换台"（仓库/PR/Issue/Actions 等常用命令），最后分享把"遥控器"调教得更顺手的技巧（别名、扩展）。与 046-057 篇的 gh 专项命令速查相呼应，本篇侧重**整体上手路径与组合使用**。

## 1. 安装与认证：拿到遥控器

### 1.1 安装

```bash
# Windows（winget）
winget install --id GitHub.cli

# macOS（Homebrew）
brew install gh

# Linux（Ubuntu/Debian）
sudo apt install gh

# 验证安装
gh --version
```

> Windows 除 winget 外，也可用 MSI 安装包或 Scoop 安装；macOS 还可通过第三方包管理器安装。安装后建议定期升级：Windows 用 `winget upgrade --id GitHub.cli`，macOS 用 `brew upgrade gh`，确保使用最新的命令与安全修复。

### 1.2 登录认证

```bash
# 启动交互式登录
gh auth login

# 按提示选择：
#   1) GitHub.com（或个人/企业服务器）
#   2) 认证方式：浏览器登录（推荐）或粘贴 Token
#   3) 选择 Git 操作协议：HTTPS 或 SSH

# 查看登录状态
gh auth status
```

> 认证成功后，gh 会自动接管 Git 凭据（选择 HTTPS 时），`git push`/`git pull` 不再需要单独配置 PAT 或 SSH。官方把这称为"无需单独的凭据管理器"。

### 1.3 获取帮助：--help 与官方手册

gh 有完善的帮助体系，遇到不确定的命令先查帮助：

```bash
# 顶层帮助（列出所有命令族）
gh help

# 具体命令帮助
gh pr create --help

# 查看命令手册页
gh help pr
```

> 官方资料：完整命令手册见 https://cli.github.com/manual/ ，每个子命令都有参数说明和示例。

## 2. 换台一：仓库操作（gh repo）

```bash
# 创建仓库（--clone 表示同时克隆到本地）
gh repo create my-project --public --clone
gh repo create my-project --private

# 克隆别人的仓库
gh repo clone octo-org/octo-repo

# 查看仓库信息（README 摘要）
gh repo view octo-org/octo-repo
# 在浏览器打开仓库
gh repo view octo-org/octo-repo --web

# Fork 仓库并克隆
gh repo fork octo-org/octo-repo --clone

# 列出自己的仓库
gh repo list --limit 50
gh repo list --language TypeScript

# 归档 / 删除（危险操作，谨慎使用）
gh repo archive OWNER/REPO --yes
gh repo delete OWNER/REPO --yes
```

## 3. 换台二：Pull Request（gh pr）

```bash
# 创建 PR（--fill 用提交信息自动填充标题与描述）
gh pr create --title "feat: add auth" --body "描述内容"
gh pr create --fill

# 列出 / 查看 PR
gh pr list --state open
gh pr view 123

# 检出某 PR 到本地（自动切换分支）
gh pr checkout 123

# 审查 PR
gh pr review 123 --approve
gh pr review 123 --request-changes -b "需要修改"

# 合并 PR（三种合并策略）
gh pr merge 123 --merge     # 合并提交
gh pr merge 123 --squash    # 压缩合并（推荐，历史干净）
gh pr merge 123 --rebase    # 变基合并

# 合并后自动删除远程分支
gh pr merge 123 --squash --delete-branch
```

## 4. 换台三：Issue（gh issue）

```bash
# 创建 Issue
gh issue create --title "Bug: login fails" --body "描述"
# 从文件读取描述
gh issue create --title "Bug" --body-file bug-template.md

# 列出 / 查看
gh issue list
gh issue list --label bug
gh issue list --assignee @me
gh issue view 123

# 关闭 / 重新打开
gh issue close 123
gh issue reopen 123
```

## 5. 换台四：Actions 与 Workflow（gh workflow / gh run）

```bash
# 列出仓库的工作流
gh workflow list

# 手动触发工作流（可指定分支）
gh workflow run ci.yml
gh workflow run ci.yml --ref feature-branch

# 查看运行记录
gh run list
gh run view 123456

# 实时跟随日志（Ctrl+C 停止）
gh run watch

# 只看失败日志
gh run view 123456 --log-failed
```

## 6. 换台五：其他高频命令

```bash
# Gist（代码片段）
gh gist create file.txt
gh gist list

# Release 发布
gh release create v1.0.0 --title "v1.0.0" --notes "Release notes"
gh release list
gh release download v1.0.0

# 直接调用 REST API
gh api repos/owner/repo/issues
# 调用 GraphQL
gh api graphql -f query='{ viewer { login } }'

# 搜索代码 / 仓库 / Issue
gh search code "TODO" --repo owner/repo
gh search repos --topic machine-learning --limit 20

# 扩展（如 Copilot CLI）
gh extension install github/gh-copilot
gh extension list
```

### 6.1 输出格式化与脚本化：--json + jq

gh 默认输出给人看的文本，加 `--json` 可输出结构化数据，配合 `jq` 处理，适合脚本自动化：

```bash
# 输出 PR 的编号、标题、状态
gh pr list --json number,title,state

# 用 jq 提取特定字段
gh pr list --json number,title --jq '.[] | "\(.number) \(.title)"'

# 输出仓库信息
gh repo view owner/repo --json name,visibility,defaultBranchRef

# 脚本中跳过交互（--yes、--repo 显式指定）
gh issue close 12 --repo owner/repo --comment "已修复" --yes
```

> 官方常见用法示例：`gh issue list --assignee "@me"` 列出分配给你的议题，`gh pr list --author alice` 列出某人的 PR。

### 6.2 gh search 搜索详解

站内搜索也能在命令行完成，适合脚本化筛选：

```bash
# 搜索代码片段
gh search code "TODO" --repo owner/repo

# 搜索仓库（按语言/星标/主题筛选）
gh search repos --language python --stars ">1000" --limit 20
gh search repos --topic machine-learning --limit 10

# 搜索 Issue 与 PR
gh search issues --label bug --state open --repo owner/repo
gh search prs --author alice --state merged

# 结构化输出配合 jq
gh search repos --topic golang --json fullName,stargazersCount \
  --jq 'sort_by(-.stargazersCount)[0:5] | .[].fullName'
```

## 7. 把遥控器调顺手：别名与组合拳

### 7.1 设置别名

```bash
gh alias set pc 'pr create --fill'
gh alias set pm 'pr merge --squash --delete-branch'
gh alias set il 'issue list'

# 使用别名
gh pc    # 等价于 gh pr create --fill
```

### 7.2 工作流组合示例

日常"开 PR"一条龙：

```bash
# 1. 从 main 创建分支
git switch -c feat/add-login
# 2. 开发提交后推送
git push -u origin feat/add-login
# 3. 一键创建 PR 并合并时删除分支
gh pr create --fill
gh pr merge --squash --delete-branch
```

"看板式"查看自己手头所有工作：

```bash
gh status
# 汇总：你创建的/分配给你的 PR 与 Issue 概览
```

### 7.3 多账户切换

```bash
# 查看当前账户
gh auth status
# 切换账户（按需登录第二个账号后）
gh auth switch
```

### 7.4 命令补全与全局配置

- **命令补全**：按 shell 生成补全脚本，Tab 键补全子命令与参数：

```bash
# bash
gh completion -s bash > ~/.gh_completion
echo 'source ~/.gh_completion' >> ~/.bashrc
# zsh
gh completion -s zsh > "${fpath[1]}/_gh"
# PowerShell
gh completion -s powershell >> $PROFILE
```

- **全局配置**：`gh config` 管理默认设置（如默认仓库所有者、首选编辑器、Git 协议）。

```bash
# 设置默认 Git 协议为 SSH
gh config set git_protocol ssh
# 设置首选编辑器
gh config set editor "code --wait"
# 查看全部配置
gh config list
```

### 7.5 与 046-057 系列的关系

本篇是 gh 的**整体上手路径**；046-057 篇按命令族给出速查手册：

| 主题 | 对应篇目 |
| :--- | :--- |
| 认证与多账户 | 046《Gh CLI 认证》 |
| PR 管理 | 047《Gh PR 管理》 |
| Issue 管理 | 048《Gh Issue 管理》 |
| 仓库管理 | 049《Gh Repo 管理》 |
| Release / Workflow / Gist | 050-052 |
| 扩展 / API / 搜索 / 标签 / 别名 | 053-057 |

遇到具体命令的完整参数时，查对应篇目或 `gh <命令> --help`。

### 7.6 安全使用习惯

- **不要用 sudo**：gh 认证信息存在用户目录，用 sudo 反而可能读到错误的配置。
- **危险命令加确认**：`gh repo delete`、`gh release delete` 等破坏性命令习惯性带 `--yes` 前先确认仓库名。
- **最小 scope**：认证时按需授权，`gh auth refresh` 只补缺的权限（如 `-s repo`、`-s workflow`），不图省事全选。
- **secrets 不落地**：敏感信息通过仓库 secrets / 环境变量注入，不要写进 gh 脚本。
- **定期检查**：`gh auth status` 定期查看账户与 scope，离职或换机后 `gh auth logout` 清理。

## 8. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 未认证执行命令 | `To use GitHub CLI, run gh auth login` | 尚未登录 | 运行 `gh auth login` 完成浏览器或 Token 认证 |
| 权限不足 | `GraphQL: Resource not accessible` / 403 | 令牌 scope 不足（如未含 `repo`） | 用 `gh auth refresh -s repo,workflow` 重新授权所需 scope |
| 命令作用域不对 | 提示 `no GitHub repository found` | 不在仓库目录内执行仓库相关命令 | `cd` 进入仓库目录，或用 `--repo OWNER/REPO` 显式指定 |
| 推送需要 workflow 权限 | `gh auth status` 提示 scope 缺失 | 首次创建 workflow 文件推送被拒 | 重新登录时授权 `workflow` scope：`gh auth refresh -s workflow` |
| 别名冲突 | `alias` 设置失败 | 别名与现有命令同名 | 换一个别名，或用 `gh alias delete <名称>` 清理 |
| 交互提示卡住 | 脚本中命令等待输入 | 缺少 `--yes`/`--confirm` 等非交互参数 | 脚本化时补充 `--yes`、`--json` 等参数跳过交互 |

## 10. 一句话记忆

**gh 是 GitHub 的"遥控器"：一条命令搞定仓库、PR、Issue、Actions，认证一次长期免密，别名与扩展让它越用越顺手。**

### 延伸阅读

- gh 认证与多账户详解，见 046 篇《Gh CLI 认证》。
- gh PR 管理速查，见 047 篇《Gh PR 管理》。
- gh Issue 管理速查，见 048 篇《Gh Issue 管理》。
- gh 仓库/Release/Workflow/Gist/扩展/API 命令，见 049-057 篇。
- 凭据与 PAT 的底层原理，见 002/004 篇。



<!-- ============ 文档分隔线：004-github/021-RESTGraphQLAPI.md ============ -->



## 0. 先来一个生活场景：餐厅点餐菜单

去餐厅吃饭，你有两种点餐方式：

**方式一：套餐菜单（REST API）**

服务员递给你一本固定菜单，每个套餐都写好了内容：A 套餐（饭 + 汤 + 小菜），B 套餐（面 + 饮料）。你想吃"只要饭和汤，不要小菜"？抱歉，套餐是固定的——你只能点 A 套餐，然后**浪费掉**不想要的小菜，或者再点一个 B 套餐多付一份钱。想要完整信息，你可能要点好几个套餐。

**方式二：自助点餐（GraphQL API）**

餐厅提供一张"食材清单"，你想怎么搭配就怎么搭配：饭 + 汤，只要这两个。一份订单（一次请求），精确拿到你要的东西，不多不少。

这就是 **REST API** 与 **GraphQL API** 的本质区别：

| 维度 | REST（套餐菜单） | GraphQL（自助点餐） |
| :--- | :--- | :--- |
| 端点数量 | 多个固定端点 | 一个统一端点 |
| 返回内容 | 服务器固定，可能多余 | 你指定要什么字段，返回什么 |
| 请求次数 | 复杂数据常需多次请求 | 通常一次请求搞定 |
| 灵活度 | 低 | 高 |
| 学习门槛 | 低 | 中 |

GitHub 同时提供这两种 API，供不同场景选用。本文采用**对比驱动**的结构：从点餐类比出发，先对比两条路线的核心差异，再分别实战（REST 用 curl、GraphQL 用查询语句，两者都用 `gh api`），最后讲清楚认证与速率限制这两个绕不开的话题。

## 1. 两条路线总览

### 1.1 核心差异表

| 特性 | REST API | GraphQL API |
| :--- | :--- | :--- |
| 版本 | v3 | v4 |
| 基础 URL | `https://api.github.com` | `https://api.github.com/graphql` |
| 数据格式 | JSON | JSON |
| 获取数据 | 按端点固定返回 | 按需声明字段 |
| 组合数据 | 多次请求拼装 | 一次请求嵌套获取 |
| 变更操作 | POST / PATCH / DELETE | mutation |
| 文档形态 | 端点清单 | 交互式 Schema 浏览器 |

### 1.2 直观理解：一个例子看出差距

需求："获取我最近 5 个仓库的名称、Star 数和最近一次提交信息。"

**REST 方式**（至少两次请求）：

```bash
# 第一次：拿仓库列表
curl -H "Authorization: Bearer ghp_xxx" \
  "https://api.github.com/user/repos?sort=updated&per_page=5"
# 返回：5 个仓库 + 每个仓库的几十个字段（大量用不到）

# 第二次：对每个仓库再查最近提交（5 次额外请求）
curl -H "Authorization: Bearer ghp_xxx" \
  "https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"
```

**GraphQL 方式**（一次请求）：

```graphql
query {
  viewer {
    repositories(first: 5, orderBy: { field: UPDATED_AT, direction: DESC }) {
      nodes {
        name
        stargazerCount
        defaultBranchRef {
          target {
            ... on Commit {
              messageHeadline
            }
          }
        }
      }
    }
  }
}
```

对比结论：REST 适合简单、直接的单资源操作；GraphQL 适合"一次拿全关联数据"的复杂场景。

## 2. 认证：进入餐厅的"会员卡"

调用 API 前必须先认证。GitHub 支持四类凭据：

| 凭据类型 | 适用场景 | 权限控制 |
| :--- | :--- | :--- |
| **Personal Access Token（Classic）** | 个人脚本、命令行 | 粗粒度（scope，如 `repo`） |
| **Personal Access Token（Fine-grained）** | 个人使用（官方推荐） | 细粒度（限定仓库 + 精确权限） |
| **GitHub App Token** | 应用/机器人长期集成 | 按安装授权 |
| **OAuth App Token** | 第三方网站/应用 | 用户授权 |

### 2.1 创建 Token

1. GitHub → Settings → Developer settings → Personal access tokens。
2. 选择 Fine-grained（推荐）或 Classic。
3. 配置权限范围（如仓库读写、Issue 管理）。
4. 生成后**立即复制保存**（只显示一次）。

### 2.2 使用 Token

```bash
# REST：Authorization 头（推荐 Bearer 前缀）
curl -H "Authorization: Bearer ghp_xxxxx" https://api.github.com/user

# GraphQL：同样是 Bearer，但必须用 POST
curl -H "Authorization: Bearer ghp_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { login } }"}' \
  https://api.github.com/graphql

# gh CLI：登录一次，自动带 Token
gh auth login
gh api user
```

### 2.3 Token 安全要点

- Token 等同于密码，**不要提交到仓库**（见 018 文档密钥扫描）。
- 用环境变量或 `gh auth` 管理，而不是写进脚本。
- 泄露后立即在 Developer settings 中撤销重建。

## 3. 路线一：REST API 实战

### 3.1 常用端点速查

| 操作 | 方法 | 端点 |
| :--- | :--- | :--- |
| 获取当前用户 | GET | `/user` |
| 列出我的仓库 | GET | `/user/repos` |
| 获取仓库详情 | GET | `/repos/{owner}/{repo}` |
| 列出 Issue | GET | `/repos/{owner}/{repo}/issues` |
| 创建 Issue | POST | `/repos/{owner}/{repo}/issues` |
| 列出 PR | GET | `/repos/{owner}/{repo}/pulls` |
| 合并 PR | PUT | `/repos/{owner}/{repo}/pulls/{n}/merge` |
| 创建 Release | POST | `/repos/{owner}/{repo}/releases` |

### 3.2 用 curl 调用（带注释）

```bash
# 获取用户信息
curl -H "Authorization: Bearer ghp_xxxxx" \
  https://api.github.com/user

# 列出仓库（分页参数 per_page，默认 30，最大 100）
curl -H "Authorization: Bearer ghp_xxxxx" \
  "https://api.github.com/user/repos?per_page=10&sort=updated"

# 创建 Issue（POST + JSON 请求体）
curl -X POST \
  -H "Authorization: Bearer ghp_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{"title":"Bug report","body":"描述一下问题","labels":["bug"]}' \
  https://api.github.com/repos/octocat/Hello-World/issues
```

### 3.3 用 gh api 调用（推荐）

`gh api` 是 GitHub 官方 CLI 对 REST API 的封装，自动处理认证、JSON 格式化、错误输出：

```bash
# 等价于上面的操作，语法更简洁
gh api user
gh api "user/repos?per_page=10&sort=updated"
gh api repos/octocat/Hello-World/issues \
  -f title="Bug report" \
  -f body="描述一下问题" \
  -f labels='["bug"]'

# 处理 JSON 结果（配合 jq 提取字段）
gh api user --jq '.login, .followers'
```

### 3.4 分页处理

REST API 的分页是新手常踩的坑：默认一页 30 条，超过部分不返回。

```bash
# 方式1：手动翻页（Link 响应头）
curl -I "https://api.github.com/user/repos"
# 响应头中的 Link 字段包含 next 页 URL

# 方式2：gh api 自动翻页（--paginate）
gh api --paginate "user/repos" --jq '.[].name'
```

## 4. 路线二：GraphQL API 实战

### 4.1 基本查询语法

GraphQL 三个基本操作：`query`（查询）、`mutation`（变更）、`subscription`（订阅，GitHub 未提供）。结构为"要什么写什么"：

```graphql
# 查询：获取当前用户及其前 10 个仓库
query {
  viewer {
    login
    repositories(first: 10, orderBy: { field: UPDATED_AT, direction: DESC }) {
      nodes {
        name
        description
        stargazerCount
      }
    }
  }
}
```

要点：

- `viewer`：代表当前认证用户。
- `first: 10`：连接分页参数（REST 用 per_page，GraphQL 用 first/after 游标）。
- 字段嵌套即关联查询：仓库里直接带出 Star 数，不用二次请求。

### 4.2 变更操作（mutation）

```graphql
# 创建 Issue
mutation {
  createIssue(input: {
    repositoryId: "R_kgXXXXX"
    title: "Bug report"
    body: "描述一下问题"
    labelIds: ["LA_XXXX"]
  }) {
    issue {
      number
      url
    }
  }
}
```

注意：mutation 通常需要**对象 ID**（如 `repositoryId`），而对象 ID 一般要通过查询先拿到：

```graphql
query {
  repository(owner: "octocat", name: "Hello-World") {
    id          # 拿到的 ID 再传给 mutation
  }
}
```

### 4.3 用 gh api 调用 GraphQL

```bash
# -F 传变量（比字符串拼接安全）
gh api graphql -F query='
  query($owner: String!, $name: String!) {
    repository(owner: $owner, name: $name) {
      name
      stargazerCount
    }
  }
' -f owner=octocat -f name=Hello-World

# 简单查询直接内联
gh api graphql -f query='{ viewer { login repositories(first: 5) { nodes { name } } } }'
```

### 4.4 什么时候选 GraphQL

- 需要一次获取多层关联数据（仓库 + Star + 最近提交）。
- 希望减少网络请求次数、按需取字段。
- 移动端/低带宽场景（省流量）。

## 5. 速率限制：餐厅的"限流规则"

为了防止滥用，GitHub 对 API 调用有明确配额。**配额按认证方式计算**，未认证的请求与匿名用户无异。

### 5.1 REST 主速率限制

| 认证状态 | 限制 |
| :--- | :--- |
| 未认证 | 60 次/小时（按 IP 计） |
| 个人访问 Token / OAuth / GitHub App | 5,000 次/小时 |
| GitHub Enterprise Cloud 组织拥有的应用 | 15,000 次/小时 |

### 5.2 GraphQL 点数限制

GraphQL 不用"次数"，而是**点数（points）**：每个查询按复杂度计分，普通查询通常 1 点。认证用户限额 **5,000 点/小时**。一次复杂查询可能消耗多点数，但远低于多次 REST 请求的消耗。

### 5.3 检查剩余配额

```bash
# REST：查看响应头
curl -I https://api.github.com/user
# X-RateLimit-Limit: 5000
# X-RateLimit-Remaining: 4999
# X-RateLimit-Reset: 1785638400   （UTC 时间戳）

# REST：专用端点（认证后）
gh api rate_limit

# GraphQL：查询 rateLimit 字段
gh api graphql -f query='{ rateLimit { limit cost remaining resetAt } }'
```

### 5.4 避免触发限制的五个习惯

1. **总是认证**：未认证只有 60 次/小时，很快耗尽。
2. **用条件请求**：利用 ETag / If-Modified-Since 头，未变化时返回 304，不消耗配额。
3. **优先 GraphQL**：一次请求代替多次 REST 请求。
4. **用 Webhooks 替代轮询**：让 GitHub 主动推送事件，而不是反复查询（见 022 文档）。
5. **处理好 403/429**：遇到 `rate limit exceeded` 时，按 `Retry-After` 头或 `X-RateLimit-Reset` 等待后重试。

## 6. 场景选型：REST 还是 GraphQL？

| 场景 | 推荐 | 理由 |
| :--- | :--- | :--- |
| 简单单资源操作（查用户、建 Issue） | REST | 端点直接，文档清晰 |
| 脚本化批量操作 | REST + gh api | 语法简单，易调试 |
| 一次拿全关联数据 | GraphQL | 减少请求数，按需取字段 |
| 移动端应用 | GraphQL | 省流量、省电量 |
| 实时事件推送 | Webhooks | 比任何轮询都高效 |

## 7. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 401 Unauthorized | `Bad credentials` | Token 无效、过期或权限不足 | 重新生成 Token；检查 scope 是否覆盖目标操作 |
| 403 rate limit | `API rate limit exceeded` | 配额耗尽（常见于未认证或循环调用） | 认证后调用；用 `rate_limit` 端点查看；等待 Reset 时间 |
| 404 找不到资源 | `Not Found` | 常见原因：Token 无该仓库权限（GitHub 对无权限返回 404 而非 403） | 检查 Token 权限范围；确认仓库名/路径拼写 |
| GraphQL 报 `Field must not have selection` | 语法错误 | 查询了对象字段但未展开子字段 | 为对象字段补充 `{ ... }` 子选择集 |
| 只想取部分数据却拿到一大包 | 响应体积大、慢 | 用了 REST 套餐端点 | 改用 GraphQL 按需声明字段 |
| 分页只返回一页 | 数据不全 | REST 默认 per_page=30 且未处理分页 | 用 `per_page=100` + `--paginate` 或 Link 头翻页 |
| Token 误提交到仓库 | 密钥扫描告警 | Token 硬编码进代码 | 撤销 Token；改用环境变量或 gh auth |

## 9. 一句话记忆

> **REST 是"套餐菜单"，端点固定、简单直接；GraphQL 是"自助点餐"，一次请求按需取字段——记住：简单操作用 REST，关联数据用 GraphQL，实时事件用 Webhooks，所有调用都要带上认证并留意速率限制。**

### 官方文档

- REST API 速率限制（官方）：https://docs.github.com/zh/rest/using-the-rest-api/rate-limits-for-the-rest-api
- GraphQL 速率限制与查询限制（官方）：https://docs.github.com/zh/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api
- REST API 认证：https://docs.github.com/zh/rest/authentication/authenticating-to-the-rest-api
- GraphQL 文档与 Schema 浏览器：https://docs.github.com/zh/graphql

### 延伸阅读
- Webhooks（事件驱动的另一种数据获取方式），见 004-github 模块 022 文档。
- GitHub CLI（gh api 的完整语法），见 004-github 模块 020 与 054 文档。
- 密钥扫描（Token 的安全管理），见 004-github 模块 018 文档。



<!-- ============ 文档分隔线：004-github/022-Webhooks.md ============ -->



## 0. 先来一个生活场景：订杂志与门铃

你订了一份杂志。杂志社有两种送刊方式：

**方式一：你自己去报摊问（轮询）**

你每天跑去报摊问："出新刊了吗？""出新刊了吗？"——多数时候得到的答案是"没有"，时间和精力全浪费在路上。

**方式二：订阅杂志（Webhook）**

你在杂志社填一张订阅单：留下地址（接收 URL）、说明只订技术类（选择事件）、约定取件暗号（Secret）。从此，杂志**一出刊就自动送到你家门口**，你什么都不用做。

**Webhook 就是 GitHub 的"杂志订阅服务"**。它与"轮询 API"（自己去问"有没有新事件"）的本质区别：

| 方式 | 方向 | 实时性 | 资源消耗 |
| :--- | :--- | :--- | :--- |
| API 轮询 | 你 → GitHub（主动问） | 有延迟（取决于轮询间隔） | 高（浪费配额，见 021 文档） |
| **Webhook** | GitHub → 你（主动推） | 即时 | 低（只在你关心的时刻触发） |

GitHub 官方定义：**Webhook 允许你在 GitHub 上发生特定事件时收到通知**——GitHub 向指定的 URL 发送 HTTP POST 请求，请求体（Payload）包含事件的全部数据。你只需要在自己的服务器上开一个"门"，等 GitHub 按门铃。

本文按**流程驱动**的结构展开，完整走一遍"事件 → Webhook → Payload → 响应"的生命周期，然后讲安全验证（防伪造）与服务器实现。

## 1. 完整流程总览：一扇"门铃"的一生

```mermaid
flowchart LR
    A["事件发生<br/>（如 git push）"] --> B["GitHub 匹配已订阅的 Webhook"]
    B --> C["组装 Payload（事件数据 JSON）"]
    C --> D["按 Secret 计算 HMAC 签名<br/>放入 X-Hub-Signature-256 头"]
    D --> E["HTTP POST 到你的 URL"]
    E --> F["你的服务器验证签名"]
    F --> G["处理业务逻辑"]
    G --> H["返回 2xx 响应"]
    H --> I["投递完成"]
    E --> J["未收到 2xx → GitHub 自动重试"]
```

五个环节缺一不可：

1. **事件（Event）**：仓库里发生了什么（push、PR、Issue 等）。
2. **订阅（Webhook）**：你告诉 GitHub"我对哪些事件感兴趣、推到哪个 URL"。
3. **负载（Payload）**：GitHub 组装的事件数据 JSON。
4. **投递（Delivery）**：GitHub 发送 HTTP POST，失败自动重试。
5. **响应（Response）**：你的服务器验证并处理，返回 2xx 确认。

## 2. 第一步：创建 Webhook（填写订阅单）

### 2.1 通过网页界面创建

```
仓库 → Settings → Webhooks → Add webhook
```

需要填写的**五个核心配置项**：

| 配置项 | 说明 | 建议 |
| :--- | :--- | :--- |
| **Payload URL** | 接收 POST 请求的公网地址 | 必须公网可达，如 `https://api.example.com/github/webhook` |
| **Content type** | 负载编码格式 | 选 `application/json`（解析最简单，官方推荐） |
| **Secret** | 订阅暗号，用于签名验证 | 必填，随机长字符串（至少 32 位） |
| **Events** | 订阅哪些事件 | 只勾选需要的，不要选 "Send me everything" |
| **Active** | 是否启用 | 默认启用；维护时先关闭 |

### 2.2 通过 API 创建（gh api）

```bash
gh api repos/octocat/Hello-World/hooks \
  -f name=web \
  -f active=true \
  -f "events[]=push" \
  -f "events[]=pull_request" \
  -f "config[url]=https://api.example.com/github/webhook" \
  -f "config[content_type]=json" \
  -f "config[secret]=my-secret-key-1234567890abcdef"
```

### 2.3 两种 Webhook 类型

| 类型 | 作用范围 | 适用场景 |
| :--- | :--- | :--- |
| **仓库级 Webhook** | 单个仓库的事件 | 个人项目、单仓库 CI 触发 |
| **组织级 Webhook** | 组织内所有仓库的事件 | 统一审计、全仓库合规监控 |

## 3. 第二步：选择事件（勾选订阅内容）

### 3.1 常用事件速查

| 事件 | 触发时机 | 典型用途 |
| :--- | :--- | :--- |
| `push` | 代码推送到分支 | 触发构建/部署 |
| `pull_request` | PR 创建/更新/关闭/合并 | 触发测试、通知审查者 |
| `issues` | Issue 创建/更新/关闭 | 同步到项目管理工具 |
| `issue_comment` | Issue 或 PR 评论 | 客服机器人、自动回复 |
| `pull_request_review` | PR 审查提交 | 审查状态看板 |
| `release` | Release 发布 | 自动打包镜像、发公告 |
| `star` | 仓库被标星 | 感谢自动化、数据统计 |
| `workflow_run` | Actions 工作流完成 | 工作流间联动 |
| `ping` | Webhook 创建/更新时 | 连通性测试（GitHub 自动发） |

### 3.2 选择原则

- **只订阅需要的**：每多一个事件就多一批请求，噪音会淹没真实信号。
- **`*`（所有事件）不推荐**：除非做全量审计，否则会造成大量无效投递。
- **先小后大**：先用 `push` 跑通全流程，再逐步加事件。

## 4. 第三步：查看 Payload（读懂门铃传来的信息）

每个事件的 Payload 是结构化 JSON，包含 `repository`、`sender`、事件专属字段等。以下是一个 `push` 事件的实际负载（已注释）：

```json
{
  "ref": "refs/heads/main",
  "before": "7d8f1a2b3c4d5e6f708192a3b4c5d6e7f8a9b0c1",
  "after": "8e9f0a1b2c3d4e5f60718293a4b5c6d7e8f9a0b2",
  "repository": {
    "id": 123456789,
    "name": "my-repo",
    "full_name": "octocat/my-repo",
    "private": false,
    "html_url": "https://github.com/octocat/my-repo"
  },
  "sender": {
    "login": "octocat",
    "id": 583231,
    "type": "User"
  },
  "commits": [
    {
      "id": "8e9f0a1b2c3d4e5f60718293a4b5c6d7e8f9a0b2",
      "message": "feat: 添加登录功能",
      "author": {
        "name": "octocat",
        "email": "octocat@users.noreply.github.com"
      },
      "url": "https://github.com/octocat/my-repo/commit/8e9f0a..."
    }
  ],
  "head_commit": {
    "message": "feat: 添加登录功能"
  }
}
```

**Payload 里的关键信息**：ref（分支）、before/after（提交前后 SHA）、commits（提交列表）、sender（触发者）、repository（仓库信息）。你的业务逻辑主要消费这些字段。

### 4.1 投递头（Delivery Headers）

每次投递还带有 HTTP 头，比 Payload 更先到：

| 请求头 | 含义 |
| :--- | :--- |
| `X-GitHub-Event` | 事件名称（如 `push`、`issues`） |
| `X-GitHub-Delivery` | 投递唯一 ID（用于排查） |
| `X-Hub-Signature-256` | HMAC-SHA256 签名（验证身份用） |
| `User-Agent` | `GitHub-Hookshot/*`（GitHub 官方标识） |

**最佳实践**：先看 `X-GitHub-Event` 头决定处理分支，再解析 Body；而不是先解析 Body 再猜事件。

## 5. 第四步：安全验证（防伪门铃）

任何人都可能向你的 URL 发 POST 请求（伪造"门铃"）。**Secret + 签名验证**是唯一可靠的身份校验方式。

### 5.1 签名原理

```
GitHub 端：
  签名 = HMAC-SHA256(secret, 原始请求体)
  放入请求头 X-Hub-Signature-256: sha256=签名值

你的服务器端：
  用同样的 secret 对收到的原始请求体计算签名
  与请求头中的签名比对
  一致 → 确认真实来自 GitHub；不一致 → 拒绝（401）
```

### 5.2 关键细节（GitHub 官方强调）

- 签名**永远以 `sha256=` 开头**。
- 必须使用**原始请求体**（未做任何格式化）计算，否则签名对不上。
- 比对用**恒定时间比较**（`crypto.timingSafeEqual`），防止时序攻击，不要用 `==`。
- Payload 可能包含 Unicode 字符，注意 UTF-8 处理。

### 5.3 Node.js 验证示例（带注释）

```javascript
const crypto = require('crypto');

/**
 * 验证 GitHub Webhook 签名
 * @param {Buffer|string} payload 原始请求体
 * @param {string} signature 请求头 X-Hub-Signature-256
 * @param {string} secret 创建 Webhook 时填写的 Secret
 * @returns {boolean} 签名是否有效
 */
function verifyWebhook(payload, signature, secret) {
  // GitHub 发送的签名格式：sha256=十六进制摘要
  const expected = 'sha256=' +
    crypto.createHmac('sha256', secret).update(payload).digest('hex');
  // 恒定时间比较，防时序攻击
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}
```

### 5.4 安全基线清单

1. **Secret 必须设置**（测试环境也一样）。
2. 端点**必须 HTTPS**。
3. 验证签名**通过后才处理业务**。
4. 可选：校验 `User-Agent` 是否以 `GitHub-Hookshot` 开头。
5. 处理逻辑**必须幂等**（同一事件可能重试多次）。

## 6. 第五步：响应与服务器实现（开门迎客）

### 6.1 响应约定

- 收到请求后**尽快返回 2xx**（如 `200 OK`），确认收到。
- 返回非 2xx（如 500、超时）时，GitHub 会按策略**自动重试**，重试时间逐渐拉长。
- 建议先返回 200，再异步处理耗时逻辑（避免 GitHub 等待超时）。

### 6.2 Express 完整示例（带注释）

```javascript
const express = require('express');
const app = express();

// 用 raw body 接收，保证签名验证时用的是原始字节
app.post('/webhook', express.raw({ type: 'application/json' }), (req, res) => {
  // 1. 取签名头
  const signature = req.headers['x-hub-signature-256'];
  const event = req.headers['x-github-event'];

  // 2. 先验签：失败直接拒绝，不做任何业务处理
  if (!signature ||
      !verifyWebhook(req.body, signature, process.env.WEBHOOK_SECRET)) {
    return res.status(401).send('Invalid signature');
  }

  // 3. 解析事件类型（用请求头，而不是猜）
  switch (event) {
    case 'push':
      const push = JSON.parse(req.body);
      console.log(`[push] ${push.repository.full_name}: ${push.ref}`);
      break;
    case 'pull_request':
      const pr = JSON.parse(req.body);
      console.log(`[PR] #${pr.number} ${pr.action} by ${pr.sender.login}`);
      break;
    case 'ping':
      console.log('[ping] Webhook 配置成功');
      break;
    default:
      console.log(`[${event}] 未处理的事件`);
  }

  // 4. 先回 2xx，再处理耗时逻辑（如有）
  res.status(200).send('OK');
});

app.listen(3000, () => console.log('Webhook 服务运行在 3000 端口'));
```

### 6.3 本地调试：内网穿透

服务器在本地（如 `localhost:3000`）时，GitHub 无法访问。可用内网穿透工具暴露公网地址：

```bash
# 示例：使用 cloudflared 免费隧道
cloudflared tunnel --url http://localhost:3000
# 输出一个 https://xxx.trycloudflare.com 公网地址，填入 Payload URL 即可
```

### 6.4 查看投递记录与排查

```
仓库 → Settings → Webhooks → 点击 Webhook → Recent deliveries
```

每次投递都有：请求/响应头、Payload 体、响应状态码、耗时。排查流程：

1. 看最近一次投递的状态码（200 成功；4xx/5xx 失败）。
2. 点开 "Redeliver" 重新投递（修复代码后重放同一次投递）。
3. 对比 `X-GitHub-Delivery` 与服务器日志，定位丢失的投递。

## 7. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 投递显示失败 | `Response code: 404` | Payload URL 路径写错，或服务器未监听该路径 | 检查 URL 与 Express 路由是否一致；先 curl 本地验证 |
| 签名验证不通过 | `Invalid signature`，投递 401 | 用格式化后的 body 算签名，或 Secret 不一致 | 用 `express.raw()` 接收原始字节；核对 Secret |
| 收不到任何投递 | Recent deliveries 为空 | 未选择事件，或 Webhook 未启用（Active 关闭） | 检查 Events 配置；确认 Active 为启用状态 |
| 重复处理同一次事件 | 业务重复执行 | GitHub 对失败投递自动重试；或订阅了重复事件 | 业务逻辑做到**幂等**（按 delivery ID 去重） |
| 订阅了全部事件导致刷屏 | 大量无关投递 | 事件选择过宽（`*`） | 改为只勾选需要的具体事件 |
| 本地调试收不到 | 投递全部超时 | GitHub 无法访问 localhost | 用内网穿透暴露公网 URL |
| 请求被伪造 | 恶意 POST 触发了部署 | 未设置 Secret 或未验证签名 | 设置强随机 Secret；验证 X-Hub-Signature-256 后再处理 |

## 9. 一句话记忆

> **Webhook 是 GitHub 的"杂志订阅"——你填好地址（URL）、选好刊物（事件）、约定暗号（Secret），GitHub 出刊即送（事件即推）；收到后先验暗号（签名），再拆信（Payload），最后回执（2xx），全程无需轮询。**

### 官方文档

- 关于 Webhooks（GitHub 官方中文文档）：https://docs.github.com/zh/webhooks/about-webhooks
- Webhook 事件与负载（全量事件清单与 Payload 结构）：https://docs.github.com/zh/webhooks/webhook-events-and-payloads
- 验证 Webhook 投递（签名验证详解）：https://docs.github.com/zh/webhooks/using-webhooks/validating-webhook-deliveries
- 创建 Webhooks：https://docs.github.com/zh/webhooks/using-webhooks/creating-webhooks

### 延伸阅读
- REST 与 GraphQL API（Webhook 的"反面"——主动拉取），见 004-github 模块 021 文档。
- GitHub Actions（工作流 `workflow_run` 事件与 Webhook 联动），见 004-github 模块 029 文档。
- GitHub CLI（用 gh api 管理 Webhook），见 004-github 模块 020 文档。



<!-- ============ 文档分隔线：004-github/023-GitHubPackages.md ============ -->



## 0. 从一个原理说起：软件世界的"超市货架"

你写的每个项目都会"依赖"别的东西：一个日期处理库、一个 HTTP 框架、一个数据库驱动。这些可复用的软件片段叫做**包（Package）**。而"下载包"这件事，如果全靠人肉拷贝，很快就会乱套。

先看一个生活原理：**超市是怎么解决"每个人都要买东西"这个问题的？**

- 生产方（厂商）把商品统一打包、贴标签、定版本，送到超市上架；
- 需求方（顾客）走进超市，按货架找到商品，扫码结账拿走；
- 超市负责：统一存放、按名称检索、保证版本可追溯、防止买到假货。

软件世界完全复刻了这套逻辑：

| 超市概念 | 软件包世界 |
| :--- | :--- |
| 商品 | 包（Package），如 `lodash`、`requests` |
| 超市 | 包注册表（Registry），如 npmjs.com、Docker Hub |
| 货架编号 | 包名 + 版本号，如 `lodash@4.17.21` |
| 扫码结账 | 包管理器下载并记录依赖（`npm install`） |
| 生产方 | 发布者（你） |
| 顾客 | 使用方（开发者/项目） |

而 **GitHub Packages** 就是 GitHub 自己开的一家"超市"——它不生产商品，但允许你把包发布到上面，并且和你的代码仓库、权限体系深度绑定。本文先从原理讲起，再讲怎么用。

## 1. 原理篇：包管理器到底在做什么

### 1.1 先直观理解

你用 `npm install` 装依赖时，其实发生了三件事：

1. 查看项目里声明的依赖清单（`package.json`）；
2. 去注册表（默认 npmjs.com）查询这些包；
3. 下载到本地 `node_modules` 目录，并记录锁定版本。

### 1.2 再讲原理：Registry 是关键

注册表（Registry）是整个机制的枢纽。它维护了"包名 → 版本列表 → 下载地址"的索引。关键认知：

- **npm** 默认指向 `https://registry.npmjs.org`；
- **Docker** 默认指向 `https://hub.docker.com`（即 Docker Hub）；
- 注册表是**可配置的**——你可以告诉 npm "请去 GitHub 的超市买"。

这就是 GitHub Packages 的基础：**它实现了多种注册表的"兼容接口"，让 npm、Docker、Maven、NuGet 等工具指向它，就能把包发布/下载到 GitHub 上**。工具不变，只是"超市"换了。

### 1.3 最后看示例

```bash
# 默认：去 npmjs.com 买包
npm install lodash

# 配置后：去 GitHub Packages（npm.pkg.github.com）买包
npm install @your-org/private-lib
```

## 2. 为什么需要自己的"超市"：GitHub Packages 的定位

| 需求 | 公共超市（npmjs.com / Docker Hub） | GitHub Packages |
| :--- | :--- | :--- |
| 私有包 | 要付费 | 复用仓库权限，天然私有 |
| 与代码关联 | 无关联 | 包和仓库、PR、CI 深度集成 |
| 认证体系 | 独立账号 | 直接用 GitHub Token |
| 发布流程 | 手动或额外配置 | 可与 Actions 一键打通 |

一句话定位：**当你的团队需要"私有、和代码同权限、和 CI 打通"的软件包仓库时，GitHub Packages 是最顺手的答案**——它消灭了"代码在 GitHub、包在别处"的分裂状态。

### 2.1 支持的注册表一览

| 包类型 | 生态 | 地址格式 |
| :--- | :--- | :--- |
| **npm** | JavaScript/TypeScript | `npm.pkg.github.com`，包名 `@OWNER/PACKAGE` |
| **Docker（GHCR）** | 容器镜像 | `ghcr.io/OWNER/IMAGE` |
| **Maven / Gradle** | Java/Kotlin | `maven.pkg.github.com` |
| **NuGet** | .NET | `nuget.pkg.github.com` |
| **RubyGems** | Ruby | `rubygems.pkg.github.com` |

## 3. 认证原理：Token 是"超市会员卡"

### 3.1 先直观理解

去 GitHub 的超市拿私有商品，需要证明"你是谁、有没有权限"。GitHub 用 **Personal Access Token（PAT，个人访问令牌）** 充当会员卡。

### 3.2 再讲原理

| 场景 | 用什么认证 | 需要的最小权限 |
| :--- | :--- | :--- |
| 发布包 | PAT（classic，建议设过期时间） | `write:packages` + `repo`（私有仓库） |
| 下载私有包 | PAT 或 `GITHUB_TOKEN` | `read:packages` |
| GitHub Actions 发布本仓库包 | `GITHUB_TOKEN`（自动注入） | 工作流中声明 `permissions: packages: write` |

原则：**令牌权限最小化、设置过期时间、绝不提交到代码库**（放在本地环境变量或 GitHub Secrets 中）。

### 2.3 最后看示例

```bash
# 发布 npm 包到 GitHub Packages
npm config set //npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
```

## 4. 操作示例：发布 npm 包到 GitHub Packages

### 4.1 配置 .npmrc（告诉 npm "去哪家超市"）

在项目根目录创建 `.npmrc`：

```ini
# 声明作用域包（@your-org/ 开头的包）走 GitHub 注册表
@your-org:registry=https://npm.pkg.github.com

# 认证令牌从环境变量读取（不要把真实令牌写进文件）
//npm.pkg.github.com/:_authToken=${GITHUB_TOKEN}
```

### 4.2 配置 package.json

```json
{
  "name": "@your-org/my-utils",
  "version": "1.0.0",
  "description": "团队内部通用工具函数库",
  "repository": {
    "type": "git",
    "url": "https://github.com/your-org/my-utils.git"
  },
  "publishConfig": {
    "registry": "https://npm.pkg.github.com"
  }
}
```

要点：包名必须带**组织作用域**（`@your-org/`），否则可能与其他来源冲突。

### 4.3 发布与安装

```bash
# 发布（需要 write:packages 权限）
npm publish

# 在另一个项目里安装（需要 read:packages 权限，且 .npmrc 同样指向 GitHub）
npm install @your-org/my-utils
```

## 5. 操作示例：发布 Docker 镜像（GHCR）

### 5.1 登录

```bash
# GHCR 支持匿名拉取公开镜像；发布/拉私有镜像需要登录
echo $GITHUB_TOKEN | docker login ghcr.io -u 你的用户名 --password-stdin
```

### 5.2 构建并推送

```bash
# 镜像名格式：ghcr.io/OWNER/镜像名:标签
docker build -t ghcr.io/your-org/my-app:v1.0.0 .
docker push ghcr.io/your-org/my-app:v1.0.0
```

### 5.3 拉取

```bash
docker pull ghcr.io/your-org/my-app:v1.0.0
```

## 6. CI/CD 集成：让 Actions 自动发布

包发布最好交给 GitHub Actions，人只需要打标签或发 Release。完整示例：

```yaml
# .github/workflows/publish.yml
name: Publish npm package
on:
  release:
    types: [created]          # 创建 Release 时自动触发
jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write          # 关键：授予写入 packages 的权限
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          registry-url: 'https://npm.pkg.github.com'
      - run: npm ci
      - run: npm publish
        env:
          NODE_AUTH_TOKEN: ${{ secrets.GITHUB_TOKEN }}   # 自动注入的令牌
```

说明：`GITHUB_TOKEN` 由 GitHub 自动注入工作流，无需手动创建密钥；如果包与当前仓库关联，`GITHUB_TOKEN` 默认具备足够的 packages 权限。

## 7. 访问控制与可见性

### 7.1 可见性（谁能看见）

| 设置 | 说明 |
| :--- | :--- |
| **公开包（Public）** | 所有人可查看、下载；公开镜像在 GHCR 上甚至支持匿名拉取 |
| **私有包（Private）** | 仅授权用户/团队可见可下载 |

### 7.2 权限继承（官方机制）

- 支持细粒度权限的注册表（如 npm、Docker）中，**包默认继承关联仓库的访问权限**：有仓库读权限的人就有包的读权限；
- 关联仓库中的 GitHub Actions 工作流自动获得该包的访问权限；
- 包可以在设置页单独调整权限，或选择"不继承仓库权限"。

### 7.3 与仓库的关联方式

发布前先在包设置里关联仓库，或通过 Docker 标签（如 `org.opencontainers.image.source`）声明来源仓库——这样权限继承才生效。

## 8. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 401 Unauthorized | `npm ERR! code E401 ... Unauthorized` | Token 缺失或权限不足 | 配置 `.npmrc` 认证；确认 token 含 `read:packages`/`write:packages` |
| 404 Package not found | 安装私有包报 404 | 未登录、或包未关联到你可见的仓库 | 用带 `read:packages` 的 token 认证；确认包权限 |
| 包名冲突 | `403 ... already exists` | 包名与已有包冲突 | 使用带作用域的唯一名称 `@your-org/xxx` |
| 发布到错误的注册表 | 包发布到了 npmjs.com | package.json 缺 `publishConfig.registry` | 在 package.json 声明 `publishConfig` 或 .npmrc 指定 registry |
| Actions 发布失败 | `Resource not accessible by integration` | 工作流缺 `packages: write` 权限 | 在 job 级声明 `permissions: packages: write` |
| Docker 拉私有镜像失败 | `denied: requested access to the resource is denied` | 未登录 GHCR 或无权 | `docker login ghcr.io`；确认 PAT 含 `read:packages` |
| 权限继承不生效 | 协作者读不了包 | 包未关联仓库 | 在包设置中关联仓库，或通过 Docker 标签声明来源 |
| 令牌泄露风险 | 发现 token 出现在代码里 | 把令牌写进了文件并提交 | 立即吊销 token，改用环境变量/Secrets |

## 10. 一句话记忆

**GitHub Packages 是 GitHub 自营的"软件包超市"：它兼容 npm、Docker、Maven 等常见工具，把"包"和你的仓库权限、CI 流程绑定在一起——认证靠 Token，发布用原生命令，私有包复用仓库权限，让团队不再需要把代码和包分开管理。**

### 延伸阅读（站内文档）

- 用 Actions 自动化发布流程，见 004-github 模块《GitHubActionsCICD》。
- 工作流权限与 Secrets 管理，见 004-github 模块《Actions环境部署》。
- 依赖安全与自动更新，见 004-github 模块《Dependabot》。
- 用 API 管理包版本，见 004-github 模块《REST与GraphQL-API》。



<!-- ============ 文档分隔线：004-github/024-Codespaces.md ============ -->



## 0. 从一个生活场景说起：云端电脑与远程办公

过去，你要用电脑必须坐在自己那台"配置了好久的台式机"前：装系统、装编辑器、配环境变量、装依赖……换台新电脑就得重来一遍，还常常"在我电脑上好好的，在你电脑上就报错"。

GitHub Codespaces 改变了这个体验——它相当于**一台放在云端的电脑**：打开浏览器就能"远程办公"（写代码），环境配置写在"装修图纸"（devcontainer.json）里，团队任何成员都能一键复制出**一模一样的开发环境**。本篇采用**体验驱动**的结构：从"在浏览器里写代码"的第一印象开始，逐步深入原理（远程容器）、配置（devcontainer.json）、提速（预构建）与日常管理。

## 1. 体验起步：30 秒走进"浏览器里的 IDE"

### 1.1 第一次创建 Codespace

1. 打开任意 GitHub 仓库，点击绿色 **Code** 按钮。
2. 切换到 **Codespaces** 标签页。
3. 点击 **Create codespace on main**。
4. 等待几十秒，浏览器中出现一个完整的 VS Code 界面——代码已经打开，终端可用，`git`、Node.js/Python 等工具已就绪。
5. 直接写代码、跑测试、`git commit`、`git push`，全程不需要在本地安装任何东西。

### 1.2 三种打开方式

| 方式 | 命令/操作 | 适用场景 |
| :--- | :--- | :--- |
| 网页版 | 仓库 → Code → Codespaces → Create codespace | 快速试用、平板/公共电脑 |
| VS Code 桌面版 | 安装 Remote - Codespaces 扩展，连接已有 codespace | 用自己熟悉的桌面 IDE |
| GitHub CLI | `gh codespace create -r owner/repo -b main` | 命令行玩家、脚本化 |

## 2. 原理讲解：Codespaces 到底是怎么工作的

### 2.1 直观理解：三层结构

```
你的浏览器/VS Code（客户端）
        ↓ 远程连接（SSH / 端口转发）
云端虚拟机（专属于你的 Linux 机器）
        ↓ 里面运行
开发容器（dev container，Docker 容器）
```

- 每个 codespace 都运行在**独立的云端虚拟机**上，里面有一个 **dev container（开发容器）**——这是关键：你的开发环境整体打包在 Docker 容器中。
- 你在浏览器里看到的编辑器只是"遥控界面"，真正的代码、依赖、进程都在云端容器里运行。
- 容器与仓库绑定：**任何人为这个仓库创建的 codespace，环境都一样**——"在我电脑上好好的"从此成为历史。

### 2.2 关键概念：dev container

- 开发容器是**专门配置成完整开发环境**的 Docker 容器，预装语言运行时、包管理器、git、常用 CLI 工具。
- 它的配置文件（`devcontainer.json`）放在仓库的 **`.devcontainer`** 目录中，随代码一起版本管理。
- 如果仓库没有配置，Codespaces 会使用**默认容器配置**（已包含多种语言运行时和常用工具）。
- 官方文档明确定义：*"Whenever you work in a codespace, you are using a dev container on a virtual machine"*——在 codespace 里工作，本质上就是在虚拟机里的开发容器中工作。

### 2.3 免费额度（个人账户参考）

| 账户类型 | 每月核心小时 | 存储空间 |
| :--- | :--- | :--- |
| Free | 120 核心小时 | 15 GB |
| Pro | 180 核心小时 | 20 GB |
| Team/Enterprise | 按使用计费 | 按使用计费 |

> 计费按"核心数 × 使用小时"计算：2 核机器跑 1 小时 = 2 核心小时。不用的 codespace 及时停止/删除可省额度。

### 2.4 从模板与多种入口创建

- **从模板创建**：GitHub 提供大量官方模板仓库（如 `microsoft/vscode-remote-try-node`），仓库页面点 **Use this template** → **Open in a codespace** 即可秒开一个预配置环境，适合学习与测试。
- **从任意分支创建**：在仓库的 Branches 页面选择分支后创建 codespace，或 `gh codespace create -b dev` 指定分支。
- **从 Issue / PR 创建**：在 Issue 或 PR 页面也可直接打开 codespace，直接针对该 Issue/PR 对应的代码工作，改完原地提交。

## 3. 配置开发环境：devcontainer.json

### 3.1 最简配置：直接用现成镜像

```json
// .devcontainer/devcontainer.json
{
  "name": "My Node Dev Environment",
  // 使用官方预构建镜像（Node 20）
  "image": "mcr.microsoft.com/devcontainers/javascript-node:20",
  // 附加特性：安装 git 与 GitHub CLI
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  // 自动转发端口（浏览器访问 http://localhost:3000）
  "forwardPorts": [3000, 5173],
  // 容器创建完成后执行的命令（安装依赖）
  "postCreateCommand": "npm install",
  // VS Code 定制：自动安装扩展与设置
  "customizations": {
    "vscode": {
      "extensions": [
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode"
      ],
      "settings": {
        "editor.formatOnSave": true
      }
    }
  }
}
```

### 3.2 Dockerfile 方式：完全自定义

```dockerfile
# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/javascript-node:20

# 安装项目需要的系统级工具
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y postgresql-client

WORKDIR /workspace
```

```json
// .devcontainer/devcontainer.json
{
  "name": "Custom Environment",
  "build": { "dockerfile": "Dockerfile" }
}
```

> 改完 devcontainer 配置后需要**重建容器**（VS Code 命令面板：Codespaces: Rebuild Container，或 `gh codespace rebuild`）才会生效。

## 4. 日常管理：从创建到回收

```bash
# 创建（指定仓库与分支）
gh codespace create -r owner/repo -b main

# 列出所有 codespace
gh codespace list

# 查看详情 / 日志
gh codespace view
gh codespace logs

# 停止（停止计费！）
gh codespace stop

# 重建（应用 devcontainer 改动）
gh codespace rebuild

# 删除（清理额度）
gh codespace delete --force
gh codespace delete --days 7   # 删除 7 天前停止的

# 端口管理
gh codespace ports
gh codespace ports visibility 3000:public
```

### 4.1 端口转发：让云端服务可访问

容器里的服务（如 `npm run dev` 启动的 3000 端口）通过**端口转发**暴露给你，浏览器直接访问 `http://localhost:3000` 即可——虽然服务在云端，体验如同本地。

### 4.2 个性化：dotfiles 与 Codespaces secrets

- **dotfiles（个人配置仓库）**：在你的个人仓库创建一个名为 `dotfiles` 的公开仓库，把 `.bashrc`、`.zshrc`、`.gitconfig` 等配置文件放进去，并在 GitHub 的 Settings → Codespaces 中启用，之后每个新 codespace 都会自动应用你的个性化配置。
- **Codespaces secrets（环境密钥）**：需要注入容器的敏感信息（如 NPM token、云服务密钥），在 **Settings → Codespaces → Codespaces secrets** 或**仓库级 Settings → Secrets and variables → Codespaces** 中配置，容器内以环境变量形式使用，不进入代码仓库。

## 5. 提速技巧：预构建（Prebuilds）

### 5.1 为什么要预构建

没有预构建时，每次创建 codespace 都要现场安装依赖（npm install、构建产物），可能要等 5-10 分钟。**预构建（prebuild）** 在后台提前完成"镜像 + 依赖安装 + 构建"这些耗时步骤，创建时直接复用，启动可缩短到 30 秒左右。

### 5.2 配置预构建

1. 仓库 **Settings → Codespaces → Prebuilds** → **Set up prebuild**。
2. 选择分支（生产常用 main）、devcontainer 配置、区域。
3. 设置触发条件：推送时触发 / 配置变更时触发。

### 5.3 生命周期命令的最佳分工

在 `devcontainer.json` 中合理分配命令，把耗时的放预构建阶段：

- `onCreateCommand`：最耗时的操作（如 `npm ci` 安装依赖）——预构建时执行。
- `updateContentCommand`：随内容更新的构建（如 `npm run build`）。
- `postCreateCommand`：只依赖密钥/用户的个性化操作（尽量轻量）。

### 5.4 机器规格与成本估算

创建 codespace 时可选择机器规格，规格越大越快也越费额度：

| 规格 | 核心 | 内存 | 典型场景 |
| :--- | :--- | :--- | :--- |
| 2-core | 2 | 4 GB | 轻量编辑、文档 |
| 4-core | 4 | 8 GB | 常规前端/后端开发 |
| 8-core | 8 | 16 GB | 编译、测试较重的项目 |
| 16-core | 16 | 32 GB | 大型构建、数据分析 |
| 32-core | 32 | 64 GB | 重型 CI 式任务 |

**成本估算示例**：Free 账户每月 120 核心小时。4 核机器每天用 2 小时，一个月约 240 核心小时——超过免费额度，需注意停止空闲环境或升级计划。

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 创建超时/失败 | codespace 卡在 "Creating" | 依赖安装慢、镜像拉取失败、网络受限 | 配置预构建；检查 devcontainer.json 的镜像地址；查看 `gh codespace logs` |
| 启动非常慢 | 每次创建都要等几分钟 | 依赖安装在创建时现场执行 | 把 `npm install`/`npm ci` 移到 `onCreateCommand` 并启用预构建 |
| 端口打不开 | 浏览器访问 localhost:3000 无响应 | 服务未启动或端口未转发 | 确认服务运行；`gh codespace ports` 查看转发状态；按需设为 public |
| 改配置不生效 | 新代码不出现在环境里 | devcontainer 未重建 | VS Code 命令面板执行 Rebuild Container 或 `gh codespace rebuild` |
| 额度耗尽 | 提示超出配额 | 未及时停止/删除不用的 codespace | 习惯性 `gh codespace stop`；删除陈旧 codespace；必要时升级套餐 |
| 权限/密钥问题 | 推送被拒或拉私有依赖失败 | 容器内未配置凭据 | 在 Settings → Codespaces secrets 配置仓库级密钥；或重新登录 gh |

## 8. 一句话记忆

**Codespaces 是"云端电脑"：devcontainer.json 是环境图纸，容器保证团队环境一致，预构建把启动从 5 分钟压到 30 秒，用完记得停止和删除省额度。**

### 延伸阅读

- 在 codespace 中使用 GitHub CLI 操作仓库/PR，见 020 篇《GitHub CLI》。
- 容器与镜像相关概念，可参考 023 篇《GitHub Packages》。
- 云端环境下的 CI/CD 自动化，见 029 篇《GitHub Actions 与 CI/CD》。



<!-- ============ 文档分隔线：004-github/025-CODEOWNERS.md ============ -->



## 0. 先来一个生活场景：小区的楼栋长

你住的小区有 10 栋楼、30 个单元、上百户人家。物业公司收到报修单后，怎么处理最高效？

- 如果所有报修都堆给物业经理一个人，他既不懂 A 栋的水管问题，也不了解 C 栋的电路老化，处理又慢又容易出错。
- 于是小区选了**楼栋长**：每栋楼选一位熟悉本楼情况的负责人。水管问题找 A 栋长，电路问题找 C 栋长，门禁问题找物业工程部——**谁的问题找谁，专业的人管专业的事**。

大型软件仓库和小区一样：一个仓库可能包含前端、后端、数据库、DevOps、文档等多个模块。如果没有分工，所有 PR 都堆给仓库管理员一个人审查，就会：

- 前端改一行 CSS，也要等管理员有空才能合并。
- 后端的安全相关改动，管理员可能看不出问题。

**CODEOWNERS** 就是 GitHub 的"楼栋长制度"。它在仓库里定义一份"责任分工表"：**哪些文件由哪些人或团队负责**。当 PR 修改了这些文件时，GitHub 自动把对应负责人加为审查者（Reviewer），关键文件甚至要求**必须获得负责人批准**才能合并。

GitHub 官方定义：CODEOWNERS 文件用于定义仓库中代码的**负责人（Code Owners）**——当有人打开修改这些代码的 PR 时，会自动请求负责人审查。

本文采用**场景驱动**的结构：从"大型团队代码审查"的真实场景出发，一步步搭建自己的"楼栋长制度"——先写职责表（语法），再分工（路径匹配），然后加保险（分支保护集成），最后给出全套示例。

## 1. 场景：一个 20 人团队仓库的审查困境

### 1.1 没有 CODEOWNERS 时

```
张三（仓库管理员）收到 PR #123：修改了 /src/auth/ 的登录逻辑
      ↓
张三自己审查？—— 他是前端组长，看不懂 Go 的认证实现
      ↓
改到第 3 轮才合并 —— 浪费 2 天

同时，PR #124（前端按钮样式）也在等张三
张三忙不过来 —— 前端同学排队等待
```

### 1.2 有了 CODEOWNERS 之后

```
PR #123：修改 /src/auth/ → GitHub 自动指派安全团队 + 后端团队审查
PR #124：修改 /src/components/ → GitHub 自动指派前端团队审查
PR #125：修改 .github/workflows/ → GitHub 自动指派 DevOps 团队审查
```

每个 PR 一打开，**最懂这块代码的人**立刻出现在审查者列表里，不再依赖人工派单。

### 1.3 CODEOWNERS 解决的三个问题

| 问题 | 没有 CODEOWNERS | 有 CODEOWNERS |
| :--- | :--- | :--- |
| 审查者指派 | 管理员手动找，靠记忆 | 按文件自动匹配，不会漏 |
| 关键代码把关 | 谁来审不确定 | 安全/核心代码固定由指定团队把关 |
| 责任边界 | 模糊 | 文件级归属清晰，可审计 |

## 2. 搭建制度：CODEOWNERS 文件基础

### 2.1 文件放在哪里（按优先级）

GitHub 官方规定，`CODEOWNERS` 文件可放在三个位置之一，若多处存在则按以下顺序**只使用第一个找到的**：

1. 仓库根目录 `CODEOWNERS`
2. `docs/CODEOWNERS`
3. `.github/025-CODEOWNERS`（**推荐**）

官方推荐放在 `.github/` 目录，与 CI 配置、模板文件放在一起。注意：**文件在哪个分支，就对该分支的 PR 生效**——可以为不同分支配置不同的负责人（如 main 分支与 gh-pages 分支）。

### 2.2 基本语法：一行一条"职责"

```
# 格式：<路径模式> <一个或多个所有者>

# 模式（前面） + 所有者（后面，用 @ 提及）
*                       @octocat
/src/auth/              @org/security-team
*.js                    @org/frontend-team
```

三个要素：

| 要素 | 语法 | 说明 |
| :--- | :--- | :--- |
| **路径模式** | 与 `.gitignore` 语法一致 | 支持 `*`、`**`、`?`、`[a-z]` 通配符 |
| **所有者** | `@username` | 单个用户（需有仓库写权限） |
| **所有者** | `@org/team-name` | 组织团队（需可见且有写权限） |
| **所有者** | `user@example.com` | 邮箱（绑定了 GitHub 账号） |

### 2.3 三个注意事项（官方强调）

- **所有者必须有仓库写权限**：即使是团队，也必须是"可见且有写权限"的团队——即使所有成员已经通过其他途径拥有权限。
- **草案 PR 不自动通知**：把 PR 标记为草案（Draft）时不会自动请求负责人审查；转为正式后才会通知。
- **文件大小限制**：CODEOWNERS 文件过大（超过 3 MB）会失效，保持精简。

## 3. 分工细则：路径匹配规则

### 3.1 匹配规则（与 .gitignore 同源）

| 模式 | 匹配对象 | 示例 |
| :--- | :--- | :--- |
| `*` | 所有文件（默认兜底） | `* @org/core-team` |
| `*.js` | 任意层级的 .js 文件 | `*.js @org/frontend-team` |
| `/src/` | 仅根目录的 src 目录 | `/src/ @org/backend-team` |
| `src/` | 任意层级的 src 目录 | `src/ @org/backend-team` |
| `**/auth/**` | 任意层级的 auth 目录 | `**/auth/** @org/security-team` |
| `docs/README.md` | 精确文件 | `docs/README.md @org/docs-team` |

### 3.2 优先级：具体规则覆盖通用规则

与 .gitignore 不同，CODEOWNERS 的规则是**所有匹配的规则都会生效**（每个匹配的规则都添加审查者），但**后面的规则优先级更高**（更具体的匹配会额外添加所有者）。GitHub 官方明确：**最后一个匹配文件的规则（以及任何更具体的规则）决定了文件的代码所有者**。

```gitignore
# 兜底：所有文件默认由核心团队负责
*                              @org/core-team

# 更具体：auth 目录的 JS 文件额外由安全团队负责
/src/auth/*.js                 @org/security-team

# 最具体：特定的关键文件由安全负责人直接负责
/src/auth/AdminAuth.js         @security-lead
```

修改 `AdminAuth.js` 时，审查者包括：core-team（兜底）+ security-team（目录规则）+ security-lead（文件规则）。规则越具体、越靠后，越能"加人"。

### 3.3 只匹配目录时

`/src/` 只匹配目录本身，不含子目录内容。要匹配整个目录树：

```gitignore
# 只匹配 src 目录本身（不含子目录）——容易漏
/src/             @org/backend-team

# 推荐：匹配 src 下所有内容（目录 + 子目录 + 文件）
/src/**           @org/backend-team
```

## 4. 加保险：与分支保护规则集成

仅自动指派审查还不够——如果有权合并的人强行跳过审查，制度就形同虚设。**分支保护规则**给 CODEOWNERS 加上"法律强制力"。

### 4.1 配置步骤

```
仓库 → Settings → Branches → Branch protection rules → 编辑 main 分支规则
    [x] Require a pull request before merging
        [x] Require review from Code Owners
```

### 4.2 效果对比

| 配置 | 效果 |
| :--- | :--- |
| 仅 CODEOWNERS | 自动添加审查者，但任何人可以批准合并 |
| CODEOWNERS + Require review from Code Owners | **必须获得代码所有者批准**才能合并，即使其他审查者已批准 |

这意味着：修改 `src/auth/` 的 PR，如果没有安全团队的批准，**任何方式都无法合并**（包括仓库管理员直接合并，除非有管理员豁免权限）。

### 4.3 与 CI 检查的配合

在同一个分支保护规则中，还可以要求：

- 必须通过 CI 状态检查（如 CodeQL、Dependency Review，见 019、010 文档）。
- 必须通过 Dependabot 自动合并前的检查。

三层叠加后，PR 合并的完整门槛为：**CI 通过 + 代码所有者批准 + 常规审查通过**。

## 5. 完整示例：一个全栈仓库的 CODEOWNERS

```gitignore
# .github/025-CODEOWNERS
# 规则说明：后面的规则优先级更高；匹配的规则都会添加审查者

# ========== 兜底规则 ==========
# 未匹配到任何其他规则的文件，由核心团队负责
*                                                @myorg/core-team

# ========== 前端 ==========
/src/components/                                 @myorg/frontend-team
/src/styles/                                     @myorg/frontend-team
*.vue                                            @myorg/frontend-team
*.css                                            @myorg/frontend-team
*.tsx                                            @myorg/frontend-team

# ========== 后端 ==========
/src/api/                                        @myorg/backend-team
/src/services/                                   @myorg/backend-team
*.py                                             @myorg/backend-team

# ========== 安全（关键代码，最高优先级） ==========
/src/auth/**                                     @myorg/security-team
/src/payment/**                                  @myorg/security-team
.env.example                                     @myorg/security-team
security/**                                      @myorg/security-team

# ========== DevOps ==========
Dockerfile                                       @myorg/devops-team
docker-compose*.yml                              @myorg/devops-team
.github/workflows/**                             @myorg/devops-team

# ========== 文档 ==========
/docs/**                                         @myorg/docs-team
README.md                                        @myorg/docs-team

# ========== 数据库迁移 ==========
/db/migrations/**                                @myorg/backend-team
```

**验证技巧**：在 PR 的 "Files Changed" 选项卡中，可以预览每个文件归属哪些负责人；在仓库中浏览文件时，悬停文件图标也可看到负责人提示。

## 6. 常见错误与对策

| 错误现象 | 报错/表现 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 负责人没被自动添加 | PR 审查者为空 | 所有者没有仓库写权限；或团队不可见 | 给用户/团队授予 write 权限；确认团队可见性 |
| 文件位置写错导致不生效 | 完全没有任何效果 | CODEOWNERS 不在三个规定位置 | 移到根目录、docs/ 或 .github/（推荐后者） |
| 规则漏匹配 | 部分文件没人负责 | 目录规则未加 `/**`，只匹配了目录本身 | 目录用 `dir/**` 覆盖子内容 |
| 必须所有者批准不生效 | 无所有者批准也能合并 | 分支保护未勾选 "Require review from Code Owners" | 在分支保护规则中勾选该选项 |
| 草案 PR 无通知 | 转正式前没通知 | 官方行为：草案 PR 不自动请求负责人 | 转正式（Ready for review）后即自动通知 |
| 规则顺序混乱 | 该加的人没加上 | 具体规则写在兜底规则之前被覆盖 | 把通用规则放前面、具体规则放后面 |
| 单个用户作为负责人 | 请假/离职后无人审查 | 单点故障 | 用团队（@org/team-name）代替单用户 |

## 8. 一句话记忆

> **CODEOWNERS 是仓库的"楼栋长制度"——一行规则把文件划给最懂它的人，PR 一开自动指派审查，再配合分支保护的"必须经代码所有者批准"，让专业的人把关专业的代码。**

### 官方文档

- 关于代码所有者（GitHub 官方中文文档）：https://docs.github.com/zh/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- 分支保护与强制审查（About protected branches）：https://docs.github.com/zh/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- Gitignore 语法（CODEOWNERS 的路径模式同源）：https://git-scm.com/docs/gitignore

### 延伸阅读
- 分支模型与分支保护规则（保护规则完整配置），见 004-github 模块 007 文档。
- Pull Request 完整协作流程，见 004-github 模块 027 文档。
- 社区健康文件（CONTRIBUTING、SECURITY 等配套文件），见 004-github 模块 026 文档。
- GitHub Actions CI/CD（与代码所有者审查配合的合并门槛），见 004-github 模块 029 文档。



<!-- ============ 文档分隔线：004-github/026-CommunityHealthFile.md ============ -->



## 0. 从一个类比说起：开源项目就像一个新建成的小区

你搬进一个新小区，物业塞给你一本《业主手册》。打开一看，里面写得很清楚：

- 《小区公约》：遛狗要牵绳、晚上十点后不要大声喧哗（**行为准则**）；
- 《装修须知》：什么时间可以施工、垃圾放哪、找谁审批（**贡献指南**）；
- 《报修指引》：水管坏了打哪个电话、电梯困人找谁（**支持资源**）；
- 《访客登记》：陌生人进小区要登记（**安全策略**）。

没有这些文件会怎样？垃圾乱扔、半夜开派对、水管漏了三天没人管——小区看起来"能住人"，但没人愿意长期住下去，更没人愿意搬进来。

**开源项目就是一个"数字小区"**，而社区健康文件（Community Health Files）就是它的《业主手册》合集。它们不包含技术文档和代码，而是**支持健康协作的"规则框架"**：告诉别人如何参与、什么行为可接受、遇到问题找谁、发现漏洞怎么办。

本文按一份"社区健康文件清单"逐项讲解，你可以把清单当作装修验收表来用。

## 1. 清单总览：社区健康文件全家福

### 1.1 核心文件清单

| 文件 | 作用 | 类比 | 建议位置 |
| :--- | :--- | :--- | :--- |
| **README.md** | 介绍项目、如何开始 | 小区宣传册 | 仓库根目录 |
| **CONTRIBUTING.md** | 如何参与贡献（流程、规范） | 装修须知 | 根目录或 `.github/` |
| **CODE_OF_CONDUCT.md** | 行为准则与举报渠道 | 小区公约 | 根目录或 `.github/` |
| **SUPPORT.md** | 如何获取帮助 | 报修指引 | 根目录或 `.github/` |
| **SECURITY.md** | 如何报告安全漏洞 | 访客登记与安保 | 根目录或 `.github/` |
| **CODEOWNERS** | 文件/目录由谁负责审查 | 每栋楼的楼长 | 根目录或 `.github/` |
| **FUNDING.yml** | 赞助按钮配置 | 小区会所募捐箱 | `.github/` |
| **Issue/PR 模板** | 规范问题与改动提交格式 | 各类申请表格 | `.github/ISSUE_TEMPLATE/` 等 |

### 1.2 检查工具：社区标准（Community standards）

GitHub 自带检查器：公开仓库 → **Insights（洞察）** 标签 → **Community standards（社区标准）**，页面会列出上述文件的完备情况，打勾即达标。这是你判断"项目健不健康"的第一份体检报告。

## 2. 清单第一项：CONTRIBUTING.md（贡献指南）

### 2.1 作用

告诉新人：**怎么报告 Bug、怎么提功能请求、怎么提交代码、开发环境怎么搭、代码规范是什么**。它的存在能大幅减少"无效 Issue"和"格式错误的 PR"。

### 2.2 推荐结构模板

```markdown
# 贡献指南

感谢你愿意参与本项目！请先阅读以下内容。

## 如何报告 Bug

1. 先搜索现有 Issue，确认没有重复
2. 使用"Bug 报告"模板创建 Issue
3. 附上：环境、复现步骤、期望行为、实际行为

## 如何提交功能请求

1. 描述你想要的场景与理由
2. 说明替代方案（如果有）

## 如何提交代码（Fork 工作流）

1. Fork 本仓库并克隆到本地
2. 创建功能分支：git checkout -b feature/xxx
3. 修改并提交（提交信息遵循 Conventional Commits）
4. 推送分支并创建 Pull Request，描述中关联 Issue（Fixes #123）

## 开发环境

```bash
git clone https://github.com/你的用户名/仓库.git
cd 仓库
npm install
npm run dev
```

## 代码规范

- 使用 ESLint + Prettier，提交前运行 `npm run lint`
- 所有新功能必须包含测试
```

## 3. 清单第二项：CODE_OF_CONDUCT.md（行为准则）

### 3.1 作用

定义社区的**行为底线**和**举报渠道**，保护参与者免受骚扰，营造包容环境。GitHub 官方推荐使用成熟的 **Contributor Covenant（贡献者公约）** 模板，你只需要改联系方式即可。

### 3.2 快速添加方式

GitHub 提供一键模板：仓库 → **Add file → Create new file** → 文件名输入 `CODE_OF_CONDUCT.md` → 点击右上角 **Choose a code of conduct template** 选择模板。

### 3.3 核心内容示例（精简版）

```markdown
# 行为准则（Contributor Covenant 2.1）

## 我们的承诺

作为贡献者和维护者，我们承诺为每个人提供无骚扰的参与体验，
无论其年龄、体型、残障、族裔、性别认同与表达、经验水平、
国籍、外貌、种族、宗教或性取向如何。

## 我们的标准

积极行为：使用友好包容的语言；尊重不同观点；优雅接受建设性批评；
对社区其他成员表示同理心。

不可接受行为：性化语言或图像；挑衅、侮辱或人身攻击；公开或私下骚扰；
未经许可泄露他人隐私。

## 执行

违规行为请通过 conduct@example.com 报告。
维护者将对违规行为进行审查并采取适当处理（警告、临时/永久移除）。
```

注意：**光有文件不够，还要有真的会执行的维护者**——举报邮箱要有人定期查看。

## 4. 清单第三项：SECURITY.md（安全策略）

### 4.1 作用

告诉安全研究者：**支持哪些版本、如何私密地报告漏洞**（而不是公开发 Issue 暴露漏洞）。

### 4.2 模板

```markdown
# 安全策略

## 支持的版本

| 版本 | 支持状态 |
| :--- | :--- |
| 2.x | 完全支持（安全更新） |
| 1.x | 仅关键修复 |
| < 1.0 | 不再支持 |

## 报告安全漏洞

**请不要通过公开 Issue 报告漏洞。**

请发送邮件至 security@example.com，包含：

1. 漏洞描述与影响范围
2. 复现步骤（最小示例最佳）
3. 受影响的版本
4. 建议的修复方案（如有）

## 响应承诺

- 48 小时内确认收到报告
- 7 天内给出初步评估与修复计划
- 修复发布后公开致谢（除非报告者要求匿名）
```

## 5. 清单第四项：SUPPORT.md（支持资源）

### 5.1 作用

让用户知道"遇到问题去哪求助"，避免所有问题都涌向 Issue。

```markdown
# 获取帮助

## 自助文档

- [快速开始](docs/getting-started.md)
- [常见问题](docs/faq.md)
- [Wiki 知识库](../../wiki)

## 社区渠道

- [GitHub Discussions](../../discussions)：问答与讨论
- 邮件列表 / Discord / 微信群（按项目实际情况填写）

## 官方渠道

- 报告 Bug：[创建 Issue](../../issues/new?template=bug_report.md)
- 功能请求：[功能模板](../../issues/new?template=feature_request.md)

## 商业支持（如适用）

- 联系 support@example.com
```

## 6. 清单其余项：CODEOWNERS、FUNDING、Issue/PR 模板

### 6.1 CODEOWNERS：指定代码审查负责人

在 `.github/025-CODEOWNERS` 中声明"谁负责哪些路径"，PR 改动这些路径时自动指定审查人：

```text
# 全局默认
* @owner-team

# docs 目录由文档组负责
/docs/ @doc-maintainers

# 安全相关文件由核心成员负责
src/auth/ @admin-user
```

### 6.2 FUNDING.yml：开源赞助入口

在 `.github/FUNDING.yml` 配置后，仓库会显示"Sponsor（赞助）"按钮：

```yaml
github: [你的用户名, 组织名]      # GitHub Sponsors
patreon: 用户名                   # Patreon
custom: [https://你的赞助页地址]
```

### 6.3 Issue/PR 模板

在 `.github/ISSUE_TEMPLATE/` 下放模板文件，让新手也能提交规范的问题单（模板语法支持 YAML frontmatter 形式的表单）。

## 7. 进阶机制：默认社区健康文件（.github 仓库）

如果组织/账号下有多个仓库，不必在每个仓库重复维护同样文件。**官方机制**：在组织或用户名下创建一个名为 `.github` 的**公开**仓库，把默认社区健康文件放进去（根目录），其他没有自带对应文件的仓库会自动"继承"使用这些默认文件。

```mermaid
graph TD
  A["your-org/.github（公开仓库）"] --> B["CONTRIBUTING.md（所有仓库默认使用）"]
  A --> C["CODE_OF_CONDUCT.md"]
  A --> D["SUPPORT.md"]
  A --> E["ISSUE_TEMPLATE/"]
```

优先级规则（官方明确）：单个仓库的查找顺序为 `.github` 文件夹 → 仓库根目录 → `docs` 文件夹；都没有时，才使用 `.github` 默认仓库中的文件。注意：**LICENSE 不能作为默认文件**，许可证必须放到每个仓库本身；私有 `.github` 仓库不生效。

## 8. 常见错误与对策表

| 常见错误 | 现象/报错 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| 文件名大小写错误 | 社区标准检查不通过 | 写成 `contributing.md` 等 | 使用规范大小写：`CONTRIBUTING.md`、`SECURITY.md` |
| 行为准则没人执行 | 违规无人处理 | 只放文件未设举报邮箱/负责人 | 填真实邮箱并指定维护者定期查看 |
| 漏洞公开报告 | 漏洞被发成公开 Issue | 没有 SECURITY.md 引导 | 加 SECURITY.md；已有公开漏洞可转私密安全通告 |
| 默认文件不生效 | 其他仓库看不到默认 CONTRIBUTING | `.github` 仓库是私有或位置不对 | 公开 `.github` 仓库；文件放根目录；Issue 模板放 `.github/ISSUE_TEMPLATE/` |
| 许可证缺失 | 访客不敢使用代码 | 未添加 LICENSE | LICENSE 必须每个仓库单独添加，不能走默认文件 |
| 模板文件名不对 | 新建 Issue 时模板不出现 | 模板未放对目录 | Issue 模板必须位于 `.github/ISSUE_TEMPLATE/` |
| 内容与现实脱节 | 新人按指南操作失败 | 文件写完从不更新 | 每轮迭代同步检查健康文件，用社区标准页面体检 |

## 10. 一句话记忆

**社区健康文件是开源项目的《业主手册》：CONTRIBUTING 讲怎么干活，CODE_OF_CONDUCT 讲什么不能干，SUPPORT 讲去哪求助，SECURITY 讲漏洞怎么报——用 Insights 的社区标准页面做体检，用 .github 公开仓库做默认模板，一次维护、全组织生效。**

### 延伸阅读（站内文档）

- README 的写法，见 004-github 模块《README文件》。
- CODEOWNERS 自动审查，见 004-github 模块《CODEOWNERS》。
- Issue 模板与标签，见 004-github 模块《Issues模板-标签与里程碑》。
- 社区问答与公告，见 004-github 模块《Discussions》。



<!-- ============ 文档分隔线：004-github/027-PullRequestCompleteCollaborationFlow.md ============ -->



## 0. 从一个生活场景说起：完整走一遍"交作业"流程

想象你写一篇小组报告：先把草稿放到共享文件夹的**独立子文件夹**（创建分支）→ 写完初稿（提交推送）→ 通过系统提交"审阅申请"（创建 PR）→ 老师批注修改意见（代码审查）→ 你逐条修改后重新提交（更新 PR）→ 老师签字通过（批准）→ 归档进主文件夹（合并）→ 关闭审阅记录（关闭 Issue）。

**Pull Request（PR）就是软件开发里的这套"交作业"流程**。本篇采用**流程驱动**的结构，按照"创建分支 → 提交推送 → 发起 PR → 审查 → 修改 → 合并 → 关闭清理 → 同步上游"的真实顺序，完整走一遍 PR 协作全流程。

## 1. 原理讲解：PR 到底是什么

### 1.1 直观理解

PR（拉取请求）是**请求把某个分支的改动合并进另一个分支**的"审查单元"。它承载：

- **diff（差异）**：改动了哪些文件、哪些行。
- **讨论区**：审查者与作者的对话记录。
- **审查意见**：逐行评论、批准/请求修改。
- **CI 结果**：自动化检查（测试、构建）的通过情况。

### 1.2 两种典型场景

| 场景 | 流程 | 适用 |
| :--- | :--- | :--- |
| 团队内部 | 直接在同一仓库建分支 → PR 合并到 main | 有写权限的成员 |
| 开源贡献 | Fork 上游仓库 → 在 fork 开发 → 跨仓库 PR | 外部贡献者 |

> 开源贡献的 Fork 流程详见 011 篇《Fork 工作流》，本篇以**团队内部**为主线，结尾补充 Fork 差异点。

### 1.3 为什么不用直接推送

直接推 main 没有审查、没有讨论记录、无法拦截低级错误。PR 把"开发中"与"可合并"之间加了一道**人工 + 自动化双重闸门**。

## 2. 阶段一：准备（分支与远程）

```bash
# 1. 确保本地 main 最新
git checkout main
git pull origin main

# 2. 创建功能分支（命名规范见 005 篇）
git checkout -b feat/add-login

# 3. 开发完成，提交（使用约定式提交）
git add .
git commit -m "feat: add login page"

# 4. 推送并设置上游追踪
git push -u origin feat/add-login
```

> 分支从**最新的 main** 创建，能大幅减少合并冲突。推送后 GitHub 仓库页会显示黄色横幅"Compare & pull request"。

## 3. 阶段二：发起 PR

### 3.1 网页操作

1. 点击 **Compare & pull request**（或 Pull requests → New pull request）。
2. **base** 选目标分支（上游的 `main`），**compare** 选功能分支（`feat/add-login`）——这一步最容易出错，务必确认页面顶部的 base repository 和 base branch。
3. 填写标题与描述（参考模板见 005 篇）。
4. 右侧栏可：指派审查者（Reviewers）、关联 Issue（Development）、打标签、选里程碑。
5. 点击 **Create pull request**。

### 3.2 关联 Issue 自动关闭

在描述中写入 `Closes #12`，合并时会自动关闭 Issue #12。

### 3.3 用 gh 创建

```bash
gh pr create --title "feat: add login" --body "Closes #12"
# 或 --fill 用提交信息自动填充
gh pr create --fill
```

## 4. 阶段三：代码审查

### 4.1 审查者的操作

1. 收到 PR 通知，进入 PR 页面看 **Files changed** 标签页。
2. 逐行阅读 diff，在具体行上留下评论。
3. 对 PR 做出三种结论之一：

| 结论 | 含义 | 后续 |
| :--- | :--- | :--- |
| Comment | 仅评论，不阻塞 | 作者可选择性回复 |
| Approve | 批准合并 | 满足其他条件即可合并 |
| Request changes | 请求修改 | 作者必须修改后重新请求审查 |

### 4.2 作者的配合

- 对每条评论**逐条回复**：修改说明或解释原因。
- 修改代码后推送到**同一分支**，PR 自动更新，审查者重新审查。
- 回复评论时可用 `@用户名` 通知审查者"已修改，请复核"。

```bash
# 作者根据意见修改
git add .
git commit -m "fix: address review feedback"
git push
```

> 小提示：功能分支合入前，如果 main 有了新提交，先 `git pull origin main` 同步再推，可避免合并时冲突。

## 5. 阶段四：合并

### 5.1 三种合并策略

| 策略 | 效果 | 适用 |
| :--- | :--- | :--- |
| Create a merge commit | 保留全部提交历史，多一个合并提交 | 希望保留开发过程 |
| Squash and merge | 全部压缩成一个提交，历史最干净 | 功能分支提交琐碎时（最常用） |
| Rebase and merge | 线性历史，不产生合并提交 | 追求整洁线性历史 |

### 5.2 合并操作

1. 确认所有**状态检查（CI）通过**（绿灯）。
2. 确认所有审查已批准（若配置了分支保护）。
3. 点击 **Merge pull request**，可选勾选 **Delete branch** 自动删除已合并分支。
4. 合并后，PR 描述中关联的 Issue 自动关闭。

### 5.3 命令行合并

```bash
gh pr merge 12 --squash --delete-branch
```

### 5.4 进阶合并机制：Draft PR、自动合并与合并队列

- **Draft PR（草稿 PR）**：功能还没完成时创建，标记为草稿，明确"暂不可合并"。适合早期征求反馈。准备就绪后点 **Ready for review** 转正。

```bash
# 创建草稿 PR
gh pr create --title "feat: big refactor" --body "WIP" --draft
```

- **自动合并（Auto-merge）**：PR 满足全部合并条件（审查通过、CI 通过）后自动执行合并，不用人等按钮。

```bash
# 标记 PR 在条件满足时自动合并
gh pr merge 12 --squash --auto
```

- **合并队列（Merge queue）**：团队协作繁忙时，PR 全部汇入队列，按序逐个验证合并，避免"合一个、坏一批"。

> 这些机制与分支保护规则配合使用（见 007 篇）：保护规则定义"什么条件能合"，自动合并/合并队列负责"条件满足就合"。

## 6. 阶段五：关闭与清理

```bash
# 删除本地已合并分支
git checkout main
git pull origin main
git branch -d feat/add-login

# 删除远程分支（若合并时未自动删除）
git push origin --delete feat/add-login
```

> 若 PR 最终**未合并而被关闭**（如需求取消）：直接在 PR 页面点 **Close pull request** 即可，本地分支删除同理。

## 7. 阶段六：Fork 场景的差异与同步上游

Fork 场景与团队内部唯一区别在于**远程来源**：

```bash
# 1. Fork 后克隆自己的 fork
git clone git@github.com:your-name/upstream-repo.git
cd upstream-repo

# 2. 添加"上游"远程（原始仓库）
git remote add upstream git@github.com:original-owner/upstream-repo.git
git remote -v   # origin=你的 fork，upstream=原仓库

# 3. 开发前先同步上游最新
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# 4. 创建分支开发，推送后到 GitHub 点 "Compare & pull request"
# 5. 提交 PR 时 base 选原仓库 main，compare 选你的分支
```

### 7.1 Fork PR 的常见坑

- **忘了同步上游**：fork 落后于上游时提 PR，diff 可能包含大量过时代码——先 `git fetch upstream` 再合并同步。
- **base 选错仓库**：Fork 场景的 base 是**原仓库**（不是你的 fork），compare 才是你的分支。
- **CI 权限受限**：部分开源项目要求维护者批准后才能运行 fork 的 Actions 工作流（"first-time contributor" 场景）。
- **提交身份**：确保 fork 仓库提交邮箱与你 GitHub 账户一致，避免贡献统计丢失。

## 8. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| :--- | :--- | :--- | :--- |
| base 分支选错 | PR 合并进了错误仓库/分支 | 未核对页面顶部的 base repository/branch | 关闭错误 PR，重新创建；确认 base 是目标仓库的目标分支 |
| 大范围无关改动 | diff 几百个文件，审查困难 | 把格式化/重构混进了功能 PR | 撤销无关改动；格式化单独开一个 PR |
| 合并冲突 | `This branch has conflicts` | 与目标分支改动重叠 | 本地 `git pull origin main` 解决冲突后 `git push`；或用网页冲突编辑器 |
| CI 检查失败 | 状态检查红叉，无法合并 | 测试/构建/语法未通过 | 查看 CI 日志定位问题，修复后重新推送 |
| 无法合并 | Merge 按钮灰色 | 分支保护规则未满足（缺批准/缺检查） | 补齐审查与状态检查；确认分支与 main 已同步 |
| 审查长期无回应 | PR 无人问津 | 未指派审查者或描述不清 | 明确指派 Reviewers；补全 PR 描述与测试说明 |

### 8.1 安全审查要点（供审查者使用）

审查时除了功能正确性，重点检查以下安全隐患：

- **敏感信息**：diff 中是否出现 `.env`、密钥、Token、连接串、个人信息。
- **依赖风险**：依赖升级是否引入破坏性变更或已知漏洞（配合 Dependabot 提醒，见 016 篇）。
- **权限控制**：新接口/新功能是否缺少权限校验，是否存在越权访问。
- **注入风险**：字符串拼接 SQL/命令/HTML 的地方是否做了参数化或转义。
- **错误处理**：异常是否被静默吞掉，是否会泄露内部堆栈信息。

## 10. 一句话记忆

**PR 全流程六步走：分支开发 → 推送 → 发起 PR（核对 base）→ 审查修改 → 合并（Squash 最常用）→ 清理关闭；Fork 场景多配一个 upstream 远程同步即可。**

### 延伸阅读

- Fork 工作流详解，见 011 篇《Fork 工作流》。
- 分支模型与保护规则（PR 的闸门配置），见 007 篇《分支模型与分支保护规则》。
- 协作规范（Commit 信息/PR 模板/审查清单），见 005 篇《协作开发规范》。
- CODEOWNERS 自动指派审查者，见 025 篇。
- gh 命令行操作 PR 速查，见 047 篇《Gh PR 管理》。



<!-- ============ 文档分隔线：004-github/028-GitHubPagesMultiSolution.md ============ -->


## 1. 背景

**GitHub Pages** 可从分支或 **GitHub Actions** 发布静态文件到 `*.github.io` 或自定义域名。常见生成器：**Jekyll（Ruby）**、**VitePress（Vite + Vue 文档框架）**、**Hugo（Go）**。三者均输出 HTML/CSS/JS，差异在 **模板语言**、**构建速度** 与 **生态**。

## 2. GitHub Pages 概述

### 2.1 类型

- **用户/组织站点**：`username.github.io` 或 `orgname.github.io`，从 `main` 分支构建
- **项目站点**：`username.github.io/repo`，从 `gh-pages` 分支或 `main` 分支的 `docs` 目录构建

### 2.2 特点

- **免费**：GitHub Pages 是免费的静态站点托管服务
- **自动 HTTPS**：为所有站点提供免费的 HTTPS 证书
- **集成 GitHub**：与 GitHub 仓库无缝集成
- **支持自定义域名**：可以使用自己的域名
- **静态内容**：只支持静态文件，不支持服务器端脚本

## 3. 静态站点生成器对比

| 特性     | Jekyll                  | VitePress             | Hugo                 |
| -------- | ----------------------- | --------------------- | -------------------- |
| 语言     | Ruby                    | JavaScript (Vue)      | Go                   |
| 构建速度 | 中等                    | 快                    | 极快                 |
| 模板语言 | Liquid                  | Vue 模板              | Go 模板              |
| 生态系统 | 丰富（GitHub 官方支持） | 现代（Vue 生态）      | 快速（Go 生态）      |
| 学习曲线 | 中等                    | 中等（熟悉 Vue 者快） | 中等                 |
| 适用场景 | 博客、个人网站          | 技术文档              | 博客、文档、企业网站 |

## 4. 部署方式

### 4.1 从分支部署

1. **设置分支**：在仓库的 **Settings → Pages → Build and deployment** 中选择：

- **Source**：`Deploy from a branch`
- **Branch**：选择分支（如 `main` 或 `gh-pages`）和目录（如 `/` 或 `/docs`）

2. **推送代码**：将静态文件推送到选定的分支
3. **等待构建**：GitHub 会自动构建并部署站点

### 4.2 使用 GitHub Actions 部署

1. **设置 Pages**：在仓库的 **Settings → Pages → Build and deployment** 中选择：

- **Source**：`GitHub Actions`

2. **创建 workflow**：在 `.github/workflows/` 目录下创建部署 workflow 文件
3. **运行 workflow**：推送代码后，Actions 会自动构建并部署站点

## 5. 方案 A：Jekyll

### 5.1 环境搭建

```bash
 # 安装 Ruby 和 Bundler
 # Windows：使用 RubyInstaller
 # macOS：使用 Homebrew: brew install ruby
 # Linux：使用包管理器
 # 安装 Jekyll 和 Bundler
 gem install jekyll bundler
 # 检查安装
 jekyll -v
```

### 5.2 创建站点

```bash
 # 创建新站点
 jekyll new my-site
 cd my-site
 # 安装依赖
 bundle install
 # 本地预览
 bundle exec jekyll serve
 # 访问 http://localhost:4000
```

### 5.3 配置文件

`_config.yml`：

```yaml
title: My Site
email: your-email@example.com
description: >- # this means to ignore newlines until "baseurl":
  Write an awesome description for your new site here. You can edit this
  line in _config.yml. It will appear in your document head meta (for
  Google search results) and in your feed.xml site description.
baseurl: '' # the subpath of your site, e.g. /blog
url: 'https://yourusername.github.io' # the base hostname & protocol for your site, e.g. http://example.com
twitter_username: jekyllrb
github_username: jekyll
# Build settings
theme: minima
plugins:
  - jekyll-feed
# Exclude from processing.
# The following items will not be processed, by default. Create a custom list
# to override the default setting.
exclude:
  - Gemfile
  - Gemfile.lock
  - node_modules
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
```

### 5.4 目录结构

```mermaid
flowchart TD
    T0["my-site/"]
    T1["_config.yml"]
    T2["_data/"]
    T3["_drafts/"]
    T4["_includes/"]
    T5["_layouts/"]
    T6["_posts/"]
    T7["_sass/"]
    T8["assets/"]
    T9["Gemfile"]
    T10["Gemfile.lock"]
    T11["index.md"]
    T0 --> T1
    T0 --> T2
    T0 --> T3
    T0 --> T4
    T0 --> T5
    T0 --> T6
    T0 --> T7
    T0 --> T8
    T0 --> T9
    T0 --> T10
    T0 --> T11
```

### 5.5 GitHub Actions 部署

`.github/workflows/jekyll.yml`：

```yaml
 name: Deploy Jekyll site to Pages
 on:
  push:
  branches: [main]
  workflow_dispatch:
 permissions:
  contents: read
  pages: write
  id-token: write
 concurrency:
  group: "pages"
  cancel-in-progress:
 jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - name: Checkout
  uses: actions/checkout@v4
  - name: Setup Ruby
  uses: ruby/setup-ruby@v1
  with:
  ruby-version: '3.1'
  bundler-cache:
  - name: Build with Jekyll
  run: bundle exec jekyll build
  env:
  JEKYLL_ENV: production
  - name: Upload artifact
  uses: actions/upload-pages-artifact@v2
  deploy:
  needs: build
  runs-on: ubuntu-latest
  environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
  steps:
  - name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v2
```

## 6. 方案 B：VitePress

### 6.1 环境搭建

```bash
 # 安装 Node.js（推荐 16+）
 # 检查安装
 node -v
 npm -v
```

### 6.2 创建站点

```bash
 # 创建 VitePress 站点
 npm create vitepress@latest docs
 # 进入目录
 cd docs
 # 安装依赖
 npm install
 # 本地预览
 npm run docs:dev
 # 访问 http://localhost:5173
 # 构建
 npm run docs:build
 # 构建产物在 .vitepress/dist 目录
```

### 6.3 配置文件

`.vitepress/config.ts`：

```typescript
 import { defineConfig } from 'vitepress'
 export default defineConfig({
  title: 'My Site',
  description: 'A VitePress site',
  base: '/repo/', // 项目站点需要设置
  themeConfig: {
  nav: [
  { text: 'Home', link: '/' },
  { text: 'Guide', link: '/guide/' },
  { text: 'API', link: '/api/' }
  ],
  sidebar: {
  '/guide/': [
  { text: 'Introduction', link: '/guide/' },
  { text: 'Getting Started', link: '/guide/getting-started' }
  ],
  '/api/': [
  { text: 'Overview', link: '/api/' },
  { text: 'Reference', link: '/api/reference' }
  ]
  }
  }
 }
```

### 6.4 目录结构

```mermaid
flowchart TD
    T0["docs/"]
    T1[".vitepress/"]
    T2["config.ts"]
    T3["dist/"]
    T4["guide/"]
    T5["index.md"]
    T6["getting-started.md"]
    T7["api/"]
    T8["index.md"]
    T9["reference.md"]
    T10["index.md"]
    T0 --> T1
    T3 --> T4
    T6 --> T7
    T9 --> T10
```

### 6.5 GitHub Actions 部署

`.github/workflows/vitepress.yml`：

```yaml
 name: Deploy VitePress site to Pages
 on:
  push:
  branches: [main]
  workflow_dispatch:
 permissions:
  contents: read
  pages: write
  id-token: write
 concurrency:
  group: "pages"
  cancel-in-progress:
 jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - name: Checkout
  uses: actions/checkout@v4
  with:
  fetch-depth: 0
  - name: Setup Node.js
  uses: actions/setup-node@v4
  with:
  node-version: '18'
  cache: npm
  - name: Install dependencies
  run: npm ci
  - name: Build
  run: npm run docs:build
  - name: Upload artifact
  uses: actions/upload-pages-artifact@v2
  with:
  path: docs/.vitepress/dist
  deploy:
  needs: build
  runs-on: ubuntu-latest
  environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
  steps:
  - name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v2
```

## 7. 方案 C：Hugo

### 7.1 环境搭建

```bash
 # 安装 Hugo（推荐 Extended 版本）
 # Windows：使用 Chocolatey: choco install hugo-extended
 # macOS：使用 Homebrew: brew install hugo
 # Linux：使用包管理器或二进制文件
 # 检查安装
 hugo version
```

### 7.2 创建站点

```bash
 # 创建新站点
 hugo new site my-site --format yaml
 cd my-site
 # 添加主题（使用 git submodule）
 git init
 git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
 # 配置主题
 echo 'theme: ananke' >> config.yaml
 # 创建内容
 hugo new posts/my-first-post.md
 # 本地预览
 hugo server -D
 # 访问 http://localhost:1313
 # 构建
 hugo --minify
 # 构建产物在 public 目录
```

### 7.3 配置文件

`config.yaml`：

```yaml
baseURL: https://yourusername.github.io/repo/ # 项目站点需要设置
languageCode: en-us
title: My New Hugo Site
theme: ananke
params:
  description: 'My Hugo site'
  author: 'Your Name'
  social:
  twitter: 'yourusername'
  github: 'yourusername'
```

### 7.4 目录结构

```mermaid
flowchart TD
    T0["my-site/"]
    T1["archetypes/"]
    T2["content/"]
    T3["posts/"]
    T4["my-first-post.md"]
    T5["data/"]
    T6["layouts/"]
    T7["static/"]
    T8["themes/"]
    T9["ananke/"]
    T10["config.yaml"]
    T11["go.mod"]
    T0 --> T1
    T0 --> T2
    T4 --> T5
    T4 --> T6
    T4 --> T7
    T4 --> T8
    T9 --> T10
    T9 --> T11
```

### 7.5 GitHub Actions 部署

`.github/workflows/hugo.yml`：

```yaml
 name: Deploy Hugo site to Pages
 on:
  push:
  branches: [main]
  workflow_dispatch:
 permissions:
  contents: read
  pages: write
  id-token: write
 concurrency:
  group: "pages"
  cancel-in-progress:
 jobs:
  build:
  runs-on: ubuntu-latest
  steps:
  - name: Checkout
  uses: actions/checkout@v4
  with:
  submodules:
  fetch-depth: 0
  - name: Setup Hugo
  uses: peaceiris/actions-hugo@v2
  with:
  hugo-version: 'latest'
  extended:
  - name: Build
  run: hugo --minify
  - name: Upload artifact
  uses: actions/upload-pages-artifact@v2
  deploy:
  needs: build
  runs-on: ubuntu-latest
  environment:
  name: github-pages
  url: ${{ steps.deployment.outputs.page_url }}
  steps:
  - name: Deploy to GitHub Pages
  id: deployment
  uses: actions/deploy-pages@v2
```

## 8. 自定义域名设置

### 8.1 配置 DNS

1. **A 记录**：指向 GitHub Pages 的 IP 地址

- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

2. **CNAME 记录**：指向 `username.github.io`

### 8.2 仓库设置

1. 在仓库的 **Settings → Pages → Custom domain** 中输入自定义域名
2. 点击 **Save**
3. 等待 GitHub 验证域名
4. 启用 **Enforce HTTPS** 选项

### 8.3 验证配置

```bash
 # 验证 DNS 配置
 dig yourdomain.com +noall +answer
 # 验证 HTTPS
 curl -I https://yourdomain.com
```

## 9. 常见问题与解决方案

### 9.1 资源 404 错误

- **问题**：静态资源（CSS、JS、图片）无法加载
- **解决方案**：

1.  检查 base URL 配置是否正确
2.  确保资源路径使用相对路径
3.  检查构建输出目录结构

### 9.2 CNAME 文件被覆盖

- **问题**：构建后 CNAME 文件被删除
- **解决方案**：

1.  在静态目录中添加 CNAME 文件
2.  配置构建工具保留 CNAME 文件
3.  在 CI 流程中重新创建 CNAME 文件

### 9.3 构建失败

- **问题**：GitHub Actions 构建失败
- **解决方案**：

1.  查看 Actions 日志，了解失败原因
2.  确保依赖安装正确
3.  检查配置文件语法
4.  确认主题或插件正确安装

### 9.4 部署权限不足

- **问题**：GitHub Actions 部署失败，提示权限不足
- **解决方案**：

1.  在 workflow 文件中添加正确的权限配置
2.  确保 `GITHUB_TOKEN` 有足够的权限
3.  检查仓库的 Pages 设置

## 10. 最佳实践

### 10.1 性能优化

- **压缩资源**：启用 minify 选项
- **缓存策略**：设置合理的缓存头
- **图片优化**：使用适当的图片格式和尺寸
- **CDN**：使用 CDN 加速静态资源
- **按需加载**：实现代码分割和按需加载

### 10.2 SEO 优化

- **元标签**：设置合适的 title、description 和其他元标签
- **站点地图**：生成并提交 sitemap.xml
- **robots.txt**：配置 robots.txt 文件
- **结构化数据**：添加 JSON-LD 结构化数据
- **canonical URL**：设置规范 URL

### 10.3 维护与更新

- **定期更新**：定期更新依赖和主题
- **备份**：定期备份站点内容
- **监控**：监控站点状态和性能
- **测试**：在部署前进行本地测试
- **版本控制**：使用 Git 管理站点源码

### 10.4 安全

- **HTTPS**：启用 HTTPS
- **依赖扫描**：使用 Dependabot 扫描安全漏洞
- **访问控制**：合理设置仓库访问权限
- **输入验证**：确保用户输入安全

## 11. 实际应用案例

### 11.1 个人博客

- **生成器**：Jekyll 或 Hugo
- **主题**：选择适合博客的主题
- **内容**：定期更新博客文章
- **部署**：使用 GitHub Actions 自动部署

### 11.2 技术文档

- **生成器**：VitePress
- **结构**：清晰的文档结构和导航
- **搜索**：启用文档搜索功能
- **版本**：支持多版本文档

### 11.3 企业网站

- **生成器**：Hugo
- **设计**：定制化主题和设计
- **内容**：公司介绍、产品信息、联系方式
- **集成**：集成表单和其他服务

## 12. 与其他静态站点托管服务对比

| 服务             | 优势                             | 劣势                   |
| ---------------- | -------------------------------- | ---------------------- |
| GitHub Pages     | 免费、与 GitHub 集成、自动 HTTPS | 构建时间限制、功能有限 |
| Netlify          | 功能丰富、CI/CD 集成、自定义域名 | 免费计划有流量限制     |
| Vercel           | 速度快、Next.js 优化、自动 HTTPS | 免费计划有项目数量限制 |
| GitLab Pages     | 免费、与 GitLab 集成、CI/CD      | 界面不如 GitHub 友好   |
| Cloudflare Pages | 速度快、CDN 集成、免费           | 功能相对有限           |

## Actions 部署 Pages

**基本用法:部署静态站点**
`uses: actions/deploy-pages@v4`

```yaml
name: Deploy Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## gh-pages 分支方式

**基本用法:推送构建产物到 gh-pages**
`git push origin <子树>:gh-pages`

```bash
# 把 dist 子目录作为 gh-pages 分支根推送
git subtree push --prefix dist origin gh-pages

# 强制更新 gh-pages
git push origin `git subtree split --prefix dist`:gh-pages --force
```

---

## 配置 Pages 源

**基本用法:通过 gh 配置 Pages**
`gh api repos/<owner>/<repo>/pages`

```bash
# 设置 Pages 源为 GitHub Actions
gh api repos/owner/repo/pages -X POST -f source[branch]=main -f source[path]=/

# 修改 Pages 源
gh api repos/owner/repo/pages -X PUT -f source[branch]=gh-pages

# 查看 Pages 配置
gh api repos/owner/repo/pages
```

---

## 自定义域名

**基本用法:配置自定义域名**
`echo "<域名>" > CNAME`

```bash
# 在站点根目录创建 CNAME 文件
echo "docs.example.com" > dist/CNAME

# 配置 DNS:把 www 指向 <user>.github.io
```

---

## 通过 gh-pages 工具发布

**基本用法:用 gh-pages 工具**
`npx gh-pages -d <目录>`

```bash
# 把 dist 发布到 gh-pages 分支
npx gh-pages -d dist

# 指定分支与消息
npx gh-pages -d dist -b gh-pages -m "deploy [skip ci]"
```



<!-- ============ 文档分隔线：004-github/029-GitHubActionsCICD.md ============ -->


## 0. 开始之前：一座"智能工厂流水线"的故事

想象一座现代化工厂：原材料进厂（代码提交），传送带把零件送到各个工位——质检工位自动检查（lint）、测试工位自动试运行（test）、组装工位打包成品（build）、发货工位把货送到客户（deploy）。整条流水线由一套**中央控制系统**自动调度：原料一到，各工位按顺序自动开工；质量不合格，立刻亮红灯拦截；货品信息全部记录在案。

GitHub Actions 就是 GitHub 内置的这套"智能工厂流水线"——一套 **CI/CD（持续集成 / 持续交付）** 自动化平台。你只需要用 YAML 描述"工位清单"（workflow 工作流），GitHub 就会在云端"传送带"（runner 运行器）上自动完成：**构建、测试、打包、部署**，还能对仓库里的其他事件（开 Issue、发 Release）自动响应。

本文是 Actions 系列的**总纲**：先把 CI/CD 概念讲明白，再拆解 workflow 文件结构，最后给出 Actions 市场使用指南与最佳实践。后续各篇（触发器、矩阵、缓存、制品、环境）都是本篇某个环节的深入。

## 1. CI/CD 是什么：为什么每个仓库都需要

### 1.1 CI（持续集成，Continuous Integration）

**核心思想**：频繁地把代码**合并**到主干，并在每次合并前**自动构建和测试**，尽早发现集成问题。

- 开发者在 PR 里提交代码 → 自动跑一遍测试 → 通过才能合并。
- 好处：问题在几小时内暴露，而不是发布前一天才发现。

### 1.2 CD（持续交付/持续部署，Continuous Delivery/Deployment）

**持续交付**：代码合并后自动准备好"随时可发布"的产物（构建 + 测试 + 打包）。
**持续部署**：在持续交付基础上，把发布这一步也自动化——合并到 main 自动上生产。

```
CI：   代码提交 → 自动构建 → 自动测试 → 汇报结果
CD：   CI 通过 → 自动打包 → 部署 staging → （审批）→ 部署生产
```

### 1.3 为什么用 GitHub Actions

| 优势 | 说明 |
| --- | --- |
| 零配置接入 | 与 GitHub 仓库天然集成，不用单独搭服务器 |
| 生态丰富 | GitHub Marketplace 有大量现成 Action 可复用 |
| 免费用量 | 公开仓库免费，私有仓库有免费分钟额度 |
| 事件驱动 | push、PR、Release、定时、外部 API 都能触发 |
| 可观测 | Actions 页面可视化查看每次运行日志与状态 |

## 2. 核心组件总览：认识流水线的"零件"

GitHub 官方把 Actions 的组件划分为六个概念，层级从小到大依次是：

```
workflow（工作流）→ jobs（任务）→ steps（步骤）→ actions（动作）/ shell 命令
                                        ↕
                    runner（运行器：执行这些任务的机器）
                    event（事件：触发流水线开动的信号）
```

| 组件 | 中文 | 说明 |
| --- | --- | --- |
| Workflow | 工作流 | 一个 `.github/workflows/*.yml` 文件就是一个可配置的自动化流程 |
| Event | 事件 | 触发工作流的仓库活动（push、PR、schedule 等） |
| Job | 任务 | 一组在同一运行器上按顺序执行的步骤；不同 job 默认并行 |
| Step | 步骤 | job 内最小的执行单元：一条 shell 命令或一个 Action |
| Action | 动作 | 可复用的扩展单元，封装常用操作（检出代码、装环境等） |
| Runner | 运行器 | 执行 job 的虚拟机（GitHub 托管或自托管） |

**理解要点**：job 内的 steps 按顺序执行、可以共享数据（同一台机器）；job 之间互相独立、默认并行，用 `needs` 声明依赖。

## 3. workflow 文件结构：读懂流水线的"图纸"

### 3.1 文件位置与命名

工作流文件必须放在仓库根目录的固定文件夹中：

```mermaid
graph TD
  A["仓库根目录"] --> B[".github"]
  B --> C["workflows（固定目录名，不能改名）"]
  C --> D["ci.yml（每个 .yml 文件 = 一个独立工作流）"]
  C --> E["deploy.yml"]
  C --> F["nightly.yml"]
```

### 3.2 顶层结构总览

一个标准的 workflow 文件由三大部分组成：

```yaml
name: CI                    # 1. 工作流名称（显示在 Actions 页面）

on:                         # 2. 触发条件（什么时候跑）
  push:
    branches: [main]

permissions:                # （可选）最小权限声明
  contents: read

jobs:                       # 3. 任务集合（要干什么）
  build:                    #   job 标识
    runs-on: ubuntu-latest  #   在什么机器上跑
    steps:                  #   步骤列表（按顺序执行）
      - uses: actions/checkout@v4
      - run: npm ci
```

### 3.3 name 与 on

```yaml
name: CI                    # 页面展示名，建议起名清晰（如 "Build and Test"）
on: [push, pull_request]    # 简写：多个事件
```

`on` 的详细配置（分支过滤、路径过滤、定时、手动触发）见《Actions 触发器》（030），这里不展开。

### 3.4 jobs：任务编排

```yaml
jobs:
  lint:                      # job 1：静态检查
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint

  test:                      # job 2：测试（依赖 lint 完成）
    needs: lint              # 声明依赖：lint 成功后才跑 test
    runs-on: ubuntu-latest
    strategy:                # 矩阵：多版本并行测试
      matrix:
        node-version: [18, 20]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci && npm test

  deploy:                    # job 3：部署（依赖 test）
    needs: test
    if: github.ref == 'refs/heads/main'   # 仅 main 分支部署
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

job 关键字段速查：

| 字段 | 作用 |
| --- | --- |
| `runs-on` | 指定运行器（`ubuntu-latest` / `[self-hosted, linux]`） |
| `needs` | 依赖其他 job，串行化 |
| `strategy.matrix` | 矩阵并行（见 032） |
| `if` | 条件执行 |
| `timeout-minutes` | 超时控制（默认 360 分钟） |
| `continue-on-error` | 失败不阻断（实验性任务常用） |
| `env` | job 级环境变量 |

### 3.5 steps：步骤详解

step 只有两种形态：**运行命令**（`run`）或 **调用 Action**（`uses`）。

```yaml
steps:
  # 形态一：调用市场 Action
  - name: Checkout code
    uses: actions/checkout@v4
    with:                    # 给 Action 传参
      fetch-depth: 0

  # 形态二：运行 shell 命令
  - name: Install dependencies
    run: |
      npm ci
      npm run build

  # 条件步骤
  - name: Deploy
    if: github.ref == 'refs/heads/main'
    run: ./deploy.sh

  # 环境变量（步骤级）
  - name: Print version
    run: echo "VERSION=$VERSION"
    env:
      VERSION: 1.0.0
```

## 4. Actions 市场：站在巨人肩膀上

### 4.1 在哪里找 Action

GitHub Marketplace（https://github.com/marketplace?type=actions）是官方 Action 市场，也可以在 `uses: owner/repo@版本` 中直接引用任意公开仓库的 Action。

### 4.2 高频 Action 清单（新手必备）

| Action | 用途 |
| --- | --- |
| `actions/checkout` | 检出仓库代码（几乎每个工作流第一步） |
| `actions/setup-node` | 配置 Node.js 环境 |
| `actions/setup-python` | 配置 Python 环境 |
| `actions/setup-java` | 配置 JDK（如 temurin） |
| `actions/cache` | 缓存依赖加速（见 033） |
| `actions/upload-artifact` | 上传构建产物（见 035） |
| `actions/download-artifact` | 下载构建产物（见 035） |
| `peaceiris/actions-gh-pages` | 部署静态站到 GitHub Pages |
| `docker/login-action` | 登录容器镜像仓库 |
| `docker/build-push-action` | 构建并推送 Docker 镜像 |

### 4.3 版本固定：安全第一

Action 用 `@版本` 引用，建议固定**主版本号**（`@v4`）甚至**提交 SHA**（`@a1b2c3d...`）：

```yaml
- uses: actions/checkout@v4          # 主版本：随 v4.x 自动更新（推荐）
# - uses: actions/checkout@<完整SHA> # 最高安全：完全锁定代码
```

固定到 SHA 是官方安全加固建议——第三方 Action 若被篡改，固定 SHA 可避免意外执行恶意版本。

## 5. 完整 CI/CD 示例：三种语言的流水线

### 5.1 Node.js 完整流水线（lint → test → build → deploy）

```yaml
name: Node.js CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run lint

  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20]        # 多版本测试
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: ${{ matrix.node-version }}, cache: npm }
      - run: npm ci
      - run: npm test

  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v4   # 产物上传，供部署用
        with: { name: build, path: dist/ }

  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'    # 仅 main 分支部署
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: build, path: dist/ }
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

### 5.2 Java（Maven）流水线

```yaml
name: Java CI/CD
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'
          cache: maven                 # 内置 Maven 缓存
      - run: mvn -B package --file pom.xml
      - uses: actions/upload-artifact@v4
        with: { name: jar, path: target/*.jar }
```

### 5.3 Python 流水线

```yaml
name: Python CI/CD
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: |
          python -m pip install --upgrade pip
          pip install pytest
          pip install -r requirements.txt || true
      - run: pytest
```

## 6. 环境变量与密钥管理

### 6.1 环境变量（env）

支持工作流级、job 级、step 级三层：

```yaml
env:                          # 工作流级
  NODE_ENV: production

jobs:
  build:
    env:                      # job 级
      BUILD_VERSION: 1.0.0
    steps:
      - name: Print env
        run: |
          echo "$NODE_ENV / $BUILD_VERSION"
          echo "分支: ${{ github.ref }}"     # 上下文变量
```

### 6.2 密钥（Secrets）

- **仓库级 secrets**：Settings → Secrets and variables → Actions，所有工作流可用。
- **环境级 secrets**：环境设置里配置，更安全（见 036）。
- 使用方式：`${{ secrets.XXX }}`，日志中自动打码。

```yaml
steps:
  - name: Deploy
    run: ./deploy.sh
    env:
      API_KEY: ${{ secrets.API_KEY }}       # 不要硬编码密钥
```

## 7. 最佳实践清单

### 7.1 结构设计

- **一个仓库多个工作流**：CI、部署、定时任务拆开，互不影响。
- **needs 明确依赖**：能并行的 job 就并行，需要结果的用 `needs` 串行。
- **if 控制分支**：构建/测试全分支跑，部署只 main 跑。
- **路径过滤**：只改文档时不触发 CI（见 030 的 paths-ignore）。

### 7.2 安全

- **最小权限**：用 `permissions` 声明只读默认，按需放开：

```yaml
permissions:
  contents: read
  pull-requests: write
```

- **密钥入库**：所有密钥放 Secrets，代码里绝不硬编码。
- **固定版本**：Action 固定主版本或 SHA。
- **开启 CodeQL**：集成代码扫描（见 019 篇）。

### 7.3 性能

- **缓存依赖**：`setup-node` 内置 cache 或 `actions/cache`（见 033）。
- **矩阵并行**：多 OS / 多版本并行测试（见 032）。
- **产物按需**：制品设置合理保留期（见 035）。
- **超时兜底**：job 设 `timeout-minutes`，防止死循环烧分钟数。

### 7.4 可维护性

- 工作流文件**命名清晰**（`ci.yml`、`deploy.yml`、`nightly-security-scan.yml`）。
- 复杂逻辑加**中文注释**。
- 使用 `gh workflow list`、`gh run list` 查看状态与历史（见 gh CLI 篇）。

## 8. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 工作流不触发 | 推了代码没反应 | `on` 写错、文件名不在 `.github/workflows/`、默认分支问题 | 核对文件路径与 `on` 语法；确认已合入默认分支 |
| YAML 缩进错误 | `Invalid workflow file` | 缩进不一致（GitHub 报错红叉） | 用空格缩进（禁用 Tab），检查层级 |
| `uses: xxx` 找不到 | `Unable to resolve action` | 拼写/版本错误，或仓库不存在 | 核对 `owner/repo@版本`，去 Marketplace 复制 |
| 密钥为空 | secrets 取不到值 | 密钥名拼错、作用域不对（仓库级 vs 环境级） | 检查 Secrets 配置与 `${{ secrets.XXX }}` 拼写 |
| job 并行导致乱序 | 部署先于测试完成 | 未用 `needs` 声明依赖 | 下游 job 加 `needs: [lint, test]` |
| 私有仓库超分钟额度 | 任务排队/被拒 | 私有仓库有免费分钟限制 | 用缓存/矩阵并行优化；或自托管运行器 |
| 只改文档也跑 CI | 浪费分钟数 | 没做路径过滤 | 加 `paths-ignore: ['docs/**', '*.md']` |

## 10. 一句话记忆

**GitHub Actions 是仓库内置的"智能工厂"：用 `.github/workflows/*.yml` 描述 name/on/jobs/steps，事件一响，流水线自动跑完构建、测试、部署，全程可观测、可复用、可控制。**



<!-- ============ 文档分隔线：004-github/030-ActionsTrigger.md ============ -->


## 0. 开始之前：一个关于"闹钟"的故事

想象你家里有很多**定时触发装置**：早上 7 点的闹钟、门口感应灯、厨房的定时烤箱、还有你亲手按下按钮的咖啡机。它们平时静静躺着，但一旦"事件"发生（时间到了、有人经过、按下按钮），对应的装置就会立刻开始工作——有的会响、有的会亮、有的会烤面包。

GitHub Actions 的**触发器**就是工作流的"闹钟"。每个工作流（workflow）都在等一个特定的信号：可能是你推了一次代码（push），可能是有人开了个 Pull Request（pull_request），可能是每天凌晨 2 点的定时器（schedule），也可能是你在网页上手动按下的"Run workflow"按钮（workflow_dispatch）。

你写的 `.github/workflows/*.yml` 文件中的 `on:` 字段，就是给 GitHub 下达的"触发指令清单"：**什么信号来了，这个工作流才开始跑**。本文就按这份"触发事件清单"逐一讲解。

## 1. 触发器是什么：先直观理解，再看原理

### 1.1 直观理解

工作流本身是一套"要执行的活儿"（比如跑测试、构建、部署），触发器解决的是"**什么时候干**"的问题。两者配合，就像收音机等待特定频率的信号：信号对上了，节目就开始播放。

```yaml
name: CI
on: push   # 最简单的触发器：只要代码被推送到仓库，就运行
```

### 1.2 工作原理（官方流程）

根据 GitHub 官方文档，一次触发背后其实有三个步骤：

1. **事件发生**：仓库上发生某个活动（推送提交、打开 PR、创建 Issue 等），该事件带有对应的提交 SHA（commit SHA）和 Git 引用（ref）。
2. **搜索工作流文件**：GitHub 在该事件关联的 SHA 或 ref 中，查找仓库根目录 `.github/workflows` 文件夹下的工作流文件。
3. **匹配并运行**：凡是在 `on:` 中声明了与该事件匹配的工作流，都会启动一次运行（run）。每次运行使用的是事件关联提交中的工作流版本，同时 GitHub 会在运行器环境中注入 `GITHUB_SHA`（提交 SHA）和 `GITHUB_REF`（Git 引用）两个环境变量。

一个值得注意的细节（官方文档明确说明）：**使用仓库自带的 `GITHUB_TOKEN` 执行任务所触发的事件，除 `workflow_dispatch` 和 `repository_dispatch` 外，不会产生新的工作流运行**。这是为了防止"工作流触发工作流"造成无限递归。如果你确实需要从一个工作流里触发另一个，就得使用 GitHub App 安装令牌或个人访问令牌（PAT）。

## 2. 触发事件清单：逐一认识"闹钟"的种类

GitHub Actions 支持的触发事件非常丰富（详见官方"触发工作流的事件"页面）。下面按常用程度列出一张清单，然后逐一细讲：

| 事件 | 触发时机 | 使用频率 | 备注 |
| --- | --- | --- | --- |
| `push` | 推送提交或标签到仓库 | 极高 | CI 主力 |
| `pull_request` | 打开/更新/关闭 PR 等 | 极高 | PR 检查主力 |
| `pull_request_target` | 同上，但在基础分支上下文运行 | 较高 | 用于 fork 仓库，注意安全 |
| `schedule` | 按 cron 定时触发 | 中 | 定时任务 |
| `workflow_dispatch` | 手动点击按钮触发 | 中 | 支持带参数 |
| `release` | 发布 Release | 中 | 版本发布 |
| `repository_dispatch` | 外部 API 调用触发 | 低 | 系统集成 |
| `issue_comment` | 有人评论 Issue/PR | 低 | 可做斜杠命令 |
| `workflow_run` | 另一个工作流完成时 | 中 | 工作流间联动 |
| `workflow_call` | 被其他工作流调用 | 中 | 复用工作流 |

### 2.1 push 触发器：最常见的"门铃"

只要有人把代码推送到仓库，就触发。但通常我们不希望任何推送都触发构建，所以要加**过滤条件**：

```yaml
on:
  push:
    branches:            # 仅这些分支的推送触发
      - main
      - 'release/**'     # 通配符：release/1.0、release/2.1 都匹配
    tags:                # 仅这些标签的推送触发（配合发布流程）
      - 'v*'             # 匹配 v1.0、v2.0.1
    paths:               # 仅这些路径下的文件变更才触发
      - 'src/**'
      - 'package.json'
      - '!src/docs/**'   # 排除 src/docs 目录
```

### 2.2 pull_request 触发器：代码合入前的"体检"

PR 生命周期里有很多个时刻（activity types），你可以选择在哪些时刻触发：

```yaml
on:
  pull_request:
    types:               # 事件子类型，决定 PR 的哪个动作触发
      - opened           # PR 刚创建
      - synchronize      # PR 分支有新提交被推送
      - reopened         # 被关闭的 PR 重新打开
      - ready_for_review # 从草稿（Draft）转为正式可审查
      - labeled          # PR 被添加标签
      - closed           # PR 被关闭（合并或拒绝）
    branches:
      - main             # 只检查合并目标为 main 的 PR
    paths:
      - 'src/**'         # 只检查改动涉及 src 的 PR
```

### 2.3 pull_request_target：fork 仓库的特殊按钮

当别人 fork 你的仓库并提交 PR 时，`pull_request` 事件运行的是**PR 分支的代码**，因此拿不到仓库 secrets（防止恶意代码偷密钥）。而 `pull_request_target` 运行的是**基础分支（目标仓库）的代码**，可以访问 secrets，但也因此有被注入攻击的风险。

| 维度 | pull_request | pull_request_target |
| --- | --- | --- |
| 代码来源 | PR 分支（fork 仓库的代码） | 基础分支（目标仓库的代码） |
| secrets 访问 | 不可访问 | 可访问 |
| 安全风险 | 低 | 高（需防范注入） |
| 适用场景 | 普通项目内 PR | fork 仓库的 PR（如自动化合并、生成检查报告） |

### 2.4 schedule 触发器：定时"闹钟"

```yaml
on:
  schedule:
    - cron: '0 2 * * *'     # 每天 UTC 02:00
    - cron: '30 4 1 * *'    # 每月 1 日 UTC 04:30
```

cron 表达式共 5 个字段，从左到右依次是：分钟（0-59）、小时（0-23）、日（1-31）、月（1-12）、星期（0-6，0 表示周日）。

使用 schedule 的几个官方注意事项：

- GitHub 使用 **UTC 时区**，中国用户需换算为北京时间（UTC+8）。
- 最小调度间隔为 **5 分钟**，更短的间隔会被忽略。
- 定时触发存在延迟，不保证精确到秒。
- 仓库 **60 天无活动**后，scheduled workflow 会被自动禁用。

### 2.5 workflow_dispatch 触发器：手动"按钮"

在仓库 Actions 页面点击 "Run workflow" 手动触发，还能通过 `inputs` 定义参数，让运行变得可交互：

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:          # 参数名
        description: '部署环境'
        required: true
        default: 'staging'
        type: choice        # 下拉选择
        options:
          - development
          - staging
          - production
      version:
        description: '部署版本号'
        required: true
        type: string        # 文本输入
      dry-run:
        description: '试运行（不真正部署）'
        required: false
        type: boolean       # 布尔开关
        default: false
```

在 job 中通过 `github.event.inputs.<参数名>` 读取用户填写的值。

### 2.6 其他常用触发器

**release**：发布版本时触发，常用于"打标签自动发版"。

```yaml
on:
  release:
    types: [published, created, edited]
```

**repository_dispatch**：由外部系统通过 REST API 调用触发，适合"CI 与外部平台联动"：

```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/OWNER/REPO/dispatches \
  -d '{"event_type": "deploy", "client_payload": {"env": "production"}}'
```

**issue_comment**：有人评论时触发，可实现"在评论里输入 `/deploy` 就部署"的斜杠命令：

```yaml
on:
  issue_comment:
    types: [created]

jobs:
  command:
    if: github.event.issue.pull_request && startsWith(github.event.comment.body, '/deploy')
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploy triggered by comment"
```

**workflow_run**：另一个工作流跑完（无论成功失败）后触发，常用于"构建完成后自动部署"：

```yaml
on:
  workflow_run:
    workflows: ['Build']   # 监听名为 Build 的工作流
    types: [completed]
```

## 3. 过滤条件详解：给"闹钟"加精细的开关

触发器配过滤条件，就像给闹钟设置"只在工作日响"。

### 3.1 通配符模式（官方语法）

| 模式 | 匹配示例 | 说明 |
| --- | --- | --- |
| `main` | `main` | 精确匹配 |
| `release/**` | `release/1.0`、`release/a/b` | `**` 匹配任意深度 |
| `feature/*` | `feature/a`，不匹配 `feature/a/b` | `*` 只匹配一层 |
| `v*` | `v1`、`v2.0.1` | `*` 可匹配任意字符 |
| `!pattern` | 排除匹配 | 否定模式，用于从结果中剔除 |

### 3.2 branches 与 branches-ignore / tags 与 tags-ignore

注意使用规则：`branches`（正面清单）与 `branches-ignore`（负面清单）**不能同时使用**，`tags` 与 `tags-ignore` 同理。

```yaml
# 正确：使用正面清单
on:
  push:
    branches: [main, develop]
    tags: ['v*']

# 正确：使用负面清单
on:
  push:
    branches-ignore: ['docs/**', 'experiment/*']

# 错误：两者同时出现会报错
on:
  push:
    branches: [main]
    branches-ignore: ['release/**']   # 语法错误
```

### 3.3 paths 与 paths-ignore：路径级过滤

`paths` 与 `paths-ignore` 同样**互斥**。它基于变更文件列表做判断：若存在与 `paths` 匹配的文件，则触发；若所有变更文件都被 `paths-ignore` 匹配，则不触发。

```yaml
# 只有 src/ 与根目录 package.json 变更时才触发
on:
  push:
    branches: [main]
    paths: ['src/**', 'package.json']

# 只改文档时不触发（省 CI 分钟数）
on:
  push:
    branches: [main]
    paths-ignore: ['docs/**', '*.md', 'README.md']
```

## 4. 多事件组合与触发优化

### 4.1 一个工作流响应多个事件

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:
```

### 4.2 避免冗余触发

同一份代码既推了 main 又发起了 PR，可能触发两次。可以用 `if` 条件跳过重复：

```yaml
jobs:
  build:
    # PR 来自 fork 或同仓库时只跑一次构建
    if: github.event_name != 'pull_request' || github.event.pull_request.head.repo.fork == false
    runs-on: ubuntu-latest
    steps:
      - run: npm ci && npm test
```

### 4.3 提交信息里"跳过 CI"

在 commit message 中写入 `[skip ci]` 或 `[ci skip]`，本次推送不会触发工作流——适合纯文档、纯注释的改动：

```bash
git commit -m "docs: 更新说明文档 [skip ci]"
```

### 4.4 用权限控制触发后的动作

触发器只管"何时跑"，跑起来能做什么由 `permissions` 决定。遵循最小权限原则，只授予本次工作流需要的权限：

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write
```

## 5. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| `branches` 与 `branches-ignore` 同时使用 | `Unable to resolve action` 或语法校验失败 | 正负面清单互斥 | 只保留其中一个，改用 `!` 否定模式 |
| `paths` 与 `paths-ignore` 同时使用 | 校验失败 | 互斥配置 | 二选一，或拆分为两个工作流 |
| schedule 不按预期时间执行 | 触发时间与本地时间不符 | GitHub 使用 UTC 时区 | 换算为 UTC 时间，北京时间减 8 小时 |
| 手动触发后找不到按钮 | Actions 页面没有 "Run workflow" | 工作流文件不在默认分支，或未声明 `workflow_dispatch` | 确认 `on: workflow_dispatch` 已声明且文件已合入默认分支 |
| fork 的 PR 触发后拿不到 secrets | secrets 为空 | `pull_request` 事件运行 fork 代码，不暴露 secrets | 改用 `pull_request_target`（注意防注入），或把需要密钥的步骤放受控环境 |
| 工作流无限互相触发 | 运行数量异常增长 | 工作流 A 触发 B、B 又触发 A | 使用 `GITHUB_TOKEN` 时不会递归；必须跨工作流触发时换用 PAT/GitHub App 令牌 |
| cron 写了秒或 5 分钟以内间隔 | 定时不触发或很晚才触发 | 最小调度间隔 5 分钟，且调度有延迟 | 调整 cron，至少间隔 5 分钟，并接受延迟 |

## 7. 一句话记忆

**触发器是工作流的"闹钟"：在 `on:` 里声明事件清单和过滤条件，信号对了，工作流才开始跑。**



<!-- ============ 文档分隔线：004-github/031-FAQTroubleshoot.md ============ -->



## 1. 背景

本地与 CI 常见问题多与 **认证**、**历史中的二进制大文件**、**跨平台换行**、**子模块未初始化**、**签名密钥** 与 **配额** 相关。本节给出 **可复制的诊断命令** 与 **修复方向**。

## 2. 认证问题

### 2.1 Permission denied (publickey)

**现象**：`git push` 或 `ssh -T git@github.com` 失败，提示 `Permission denied (publickey)`。
**诊断**：

```bash
 # 检查 SSH 连接详细信息
 ssh -vT git@github.com
 # 检查 SSH 密钥列表
 ssh-add -l
 # 检查 SSH 配置
 cat ~/.ssh/config
```

**修复**：

1. **生成新的 SSH 密钥**（如果没有）：

```bash
 ssh-keygen -t ed25519 -C "your_email@example.com"
```

2. **添加 SSH 密钥到 ssh-agent**：

```bash
 eval "$(ssh-agent -s)"
 ssh-add ~/.ssh/id_ed25519
```

3. **将公钥添加到 GitHub**：

- 复制公钥内容：`cat ~/.ssh/id_ed25519.pub`
- 登录 GitHub，进入 **Settings → SSH and GPG keys → New SSH key**
- 粘贴公钥并保存

4. **检查 SSH 配置**：

```bash
 # 编辑 ~/.ssh/config
 Host github.com
 HostName github.com
 User git
 IdentityFile ~/.ssh/id_ed25519
```

### 2.2 HTTPS 认证失败

**现象**：`git push` 失败，提示输入用户名和密码，但输入后仍然失败。
**诊断**：

```bash
 # 检查远程仓库 URL
 git remote -v
 # 检查 Git 凭据缓存
 git credential-cache status
```

**修复**：

1. **使用个人访问令牌（PAT）**：

- 登录 GitHub，进入 **Settings → Developer settings → Personal access tokens → Fine-grained tokens**
- 创建新令牌，设置适当的权限
- 使用令牌作为密码进行认证

2. **配置 Git 凭据缓存**：

```bash
 # 缓存凭据 1 小时
 git config --global credential.helper 'cache --timeout=3600'
```

3. **更新远程仓库 URL**：

```bash
 # 使用 HTTPS URL 并包含令牌
 git remote set-url origin https://<token>@github.com/username/repo.git
```

## 3. 大文件问题

### 3.1 推送被拒（超过 100MB）

**现象**：`git push` 失败，提示文件超过 100MB 限制。
**诊断**：

```bash
 # 查找仓库中的大文件
 git lfs ls-files
 # 查找历史中的大文件
 git rev-list --objects --all | grep -E "^[0-9a-f]{40} .{10,}$" | sort -k 2 -n -r | head -20
```

**修复**：

1. **使用 Git LFS** 跟踪大文件：

```bash
 # 安装 Git LFS
 git lfs install
 # 跟踪大文件类型
 git lfs track "*.psd"
 git lfs track "*.zip"
 # 提交 .gitattributes 文件
 git add .gitattributes
 git commit -m "Add Git LFS tracking"
```

2. **移除历史中的大文件**：

- 使用 `git filter-repo`：

```bash
 # 安装 git-filter-repo
 # 过滤大文件
 git filter-repo --path LARGE_FILE.bin --invert-paths
 # 强制推送
 git push --force origin main
```

- 使用 BFG Repo-Cleaner：

```bash
 # 下载 BFG
 java -jar bfg.jar --strip-blobs-bigger-than 100M
 git reflog expire --expire=now --all
 git gc --prune=now --aggressive
```

### 3.2 Git LFS 相关问题

**现象**：Git LFS 跟踪的文件无法正确推送或拉取。
**诊断**：

```bash
 # 检查 Git LFS 状态
 git lfs status
 # 检查 Git LFS 配置
 git lfs config --list
```

**修复**：

1. **确保 Git LFS 已安装**：

```bash
 git lfs install
```

2. **重新推送 LFS 对象**：

```bash
 git lfs push --all origin
```

3. **拉取 LFS 对象**：

```bash
 git lfs pull
```

## 4. 换行符问题

### 4.1 LF / CRLF 冲突

**现象**：Windows 下整文件 **CRLF** 导致 diff 噪声或脚本 **shebang** 失败。
**诊断**：

```bash
 # 检查 Git 换行符配置
 git config --get core.autocrlf
 # 检查文件换行符类型
 file -k file.txt
```

**修复**：

1. **配置 Git 换行符处理**：

- Windows：`git config --global core.autocrlf `
- macOS/Linux：`git config --global core.autocrlf input`

2. **使用 .gitattributes 文件**：

```gitattributes
 # 自动处理文本文件
 * text=auto
 # 强制使用 LF
 *.sh text eol=lf
 *.py text eol=lf
 *.js text eol=lf
 # 强制使用 CRLF
 *.bat text eol=crlf
 *.cmd text eol=crlf
 # 二进制文件
 *.png binary
 *.jpg binary
 *.zip binary
```

3. **重新规范化所有文件**：

```bash
 git add --renormalize .
 git commit -m "Normalize line endings"
```

## 5. 子模块问题

### 5.1 子模块未初始化

**现象**：克隆后子目录空或旧版本。
**诊断**：

```bash
 # 检查子模块状态
 git submodule status
```

**修复**：

1. **初始化并更新子模块**：

```bash
 # 初始化子模块
 git submodule init
 # 更新子模块
 git submodule update
 # 递归初始化和更新（包含嵌套子模块）
 git submodule update --init --recursive
```

2. **克隆时直接初始化子模块**：

```bash
 git clone --recursive https://github.com/username/repo.git
```

### 5.2 子模块版本更新

**现象**：子模块有新的提交，但主仓库未更新。
**修复**：

1. **更新子模块到最新版本**：

```bash
 cd submodule_directory
 git pull origin main
 cd ..
 git add submodule_directory
 git commit -m "Update submodule to latest version"
```

2. **批量更新所有子模块**：

```bash
 git submodule foreach git pull origin main
 git add .
 git commit -m "Update all submodules"
```

## 6. 提交签名问题

### 6.1 GPG 签名失败

**现象**：`git commit` 失败，提示 GPG 签名错误。
**诊断**：

```bash
 # 检查 GPG 密钥
  gpg --list-secret-keys --keyid-format LONG
 # 检查 Git GPG 配置
  git config --get user.signingkey
  git config --get commit.gpgsign
```

**修复**：

1. **生成 GPG 密钥**（如果没有）：

```bash
 gpg --full-generate-key
```

2. **配置 Git 使用 GPG 密钥**：

```bash
 # 获取 GPG 密钥 ID
 gpg --list-secret-keys --keyid-format LONG
 # 配置 Git
 git config --global user.signingkey <GPG_KEY_ID>
 git config --global commit.gpgsign
```

3. **将 GPG 公钥添加到 GitHub**：

```bash
 # 导出公钥
 gpg --armor --export <GPG_KEY_ID>
```

- 复制公钥内容
- 登录 GitHub，进入 **Settings → SSH and GPG keys → New GPG key**
- 粘贴公钥并保存

4. **解决 TTY 问题**：

```bash
 # 在 ~/.bashrc 或 ~/.zshrc 中添加
 export GPG_TTY=$(tty)
```

### 6.2 SSH 签名

**现象**：使用 SSH 密钥进行提交签名。
**配置**：

1. **设置 Git 使用 SSH 签名**：

```bash
 git config --global gpg.format ssh
 git config --global user.signingkey ~/.ssh/id_ed25519.pub
 git config --global commit.gpgsign
```

2. **将 SSH 公钥添加到 GitHub**：

- 确保 SSH 公钥已添加到 GitHub
- 进入 **Settings → SSH and GPG keys** 确认

## 7. GitHub Actions 问题

### 7.1 Actions 分钟数耗尽

**现象**：私有库 workflow **排队/失败**，账单显示 **minutes** 用尽。
**诊断**：

```bash
 # 查看 Actions 使用情况
 # 在 GitHub 仓库 → Settings → Billing and plans → Actions
```

**修复**：

1. **优化 workflow**：

- 使用 **矩阵构建** 时合理设置组合
- 添加 **缓存** 减少依赖安装时间
- 限制 **并发** 运行的 workflow
- 使用 **条件执行** 减少不必要的运行

2. **使用自托管 runner**：

- 在 GitHub 仓库 → Settings → Actions → Runners → New self-hosted runner
- 按照说明安装和配置自托管 runner

3. **考虑开源仓库**：

- 公共仓库有更多的免费分钟数

### 7.2 Actions 权限问题

**现象**：Actions 运行失败，提示权限不足。
**诊断**：

```yaml
# 检查 workflow 文件中的权限配置
permissions:
  contents: read
  packages: write
  # 其他需要的权限
```

**修复**：

1. **在 workflow 文件中设置正确的权限**：

```yaml
permissions:
contents: write
pull-requests: write
# 根据需要添加其他权限
```

2. **使用 `GITHUB_TOKEN`**：

- Actions 自动提供 `GITHUB_TOKEN` 环境变量
- 确保 workflow 中正确使用 `secrets.GITHUB_TOKEN`

3. **检查仓库设置**：

- 进入 GitHub 仓库 → Settings → Actions → General
- 确保 **Workflow permissions** 设置正确

### 7.3 Actions 构建失败

**现象**：Actions 构建过程中失败。
**诊断**：

1. **查看 Actions 日志**：

- 进入 GitHub 仓库 → Actions
- 点击失败的 workflow → 查看详细日志

2. **常见失败原因**：

- 依赖安装失败
- 测试失败
- 构建命令错误
- 环境配置问题
  **修复**：

1. **修复依赖问题**：

- 检查 `package.json`、`requirements.txt` 等依赖文件
- 确保依赖版本兼容

2. **修复测试问题**：

- 检查测试代码和测试数据
- 确保测试环境配置正确

3. **修复构建命令**：

- 检查构建脚本和命令
- 确保构建环境正确

4. **添加调试信息**：

```yaml
 steps:
 - name: Debug information
 run: |
 echo "Node version: $(node -v)"
 echo "npm version: $(npm -v)"
 echo "Current directory: $(pwd)"
 ls -la
```

## 8. 其他常见问题

### 8.1 分支保护规则导致推送失败

**现象**：`git push` 失败，提示分支受保护。
**诊断**：

- 检查 GitHub 仓库 → Settings → Branches → Branch protection rules
  **修复**：

1. **创建 PR**：

- 推送到新分支
- 创建 PR 并请求审核

2. **临时禁用分支保护**（仅维护者）：

- 进入分支保护规则设置
- 临时禁用相关规则
- 推送后重新启用

### 8.2 合并冲突

**现象**：合并 PR 时出现冲突。
**修复**：

1. **本地解决冲突**：

```bash
 # 拉取最新代码
 git pull origin main
 # 解决冲突
 # 编辑冲突文件
 # 标记冲突已解决
 git add .
 # 继续合并
 git commit
 # 推送
 git push
```

2. **使用 GitHub 网页界面解决冲突**：

- 进入 PR 页面
- 点击 "Resolve conflicts"
- 在网页编辑器中解决冲突
- 提交解决后的代码

### 8.3 标签推送失败

**现象**：`git push --tags` 失败。
**修复**：

1. **检查权限**：确保有推送标签的权限
2. **强制推送标签**：

```bash
 git push --tags --force
```

3. **单独推送特定标签**：

```bash
 git push origin <tag_name>
```

## 9. 综合诊断与预防

### 9.1 综合诊断脚本

```bash
 #!/usr/bin/env bash
 set -euo pipefail
 # 基本信息
 echo "== 系统信息 =="
 uname -a
 echo "== Git 版本 =="
 git --version
 # 仓库信息
 echo "== 远程仓库 =="
 git remote -v
 echo "== 当前分支 =="
 git branch -vv
 echo "== 最近提交 =="
 git log -1 --oneline
 # 配置信息
 echo "== Git 配置 =="
 git config --list
 echo "== SSH 配置 =="
 cat ~/.ssh/config 2>/dev/null || echo "No SSH config"
 # 子模块信息
 echo "== 子模块状态 =="
 git submodule status 2>/dev/null || echo "No submodules"
 # LFS 信息
 echo "== LFS 状态 =="
 command -v git-lfs && git lfs version || echo "LFS not installed"
 command -v git-lfs && git lfs status 2>/dev/null || echo "No LFS status"
 # 换行符配置
 echo "== 换行符配置 =="
 git config --get core.autocrlf
 ls -la .gitattributes 2>/dev/null || echo "No .gitattributes"
 # GPG 信息
 echo "== GPG 状态 =="
 gpg --list-secret-keys --keyid-format LONG 2>/dev/null || echo "No GPG keys"
 git config --get user.signingkey 2>/dev/null || echo "No signing key configured"
 # 网络测试
 echo "== 网络测试 =="
 ping -c 3 github.com 2>/dev/null || echo "Ping failed"
 ssh -T git@github.com 2>&1 || echo "SSH test failed"
```

### 9.2 预防措施

1. **使用 Git hooks**：

- **pre-commit**：检查提交信息、代码风格、大文件等
- **pre-push**：检查推送前的状态

2. **配置模板**：

- 提交信息模板
- PR 模板
- Issue 模板

3. **自动化工具**：

- **Dependabot**：自动更新依赖
- **Code Scanning**：自动代码安全扫描
- **Secret Scanning**：自动敏感信息扫描

4. **文档**：

- **CONTRIBUTING.md**：贡献指南
- **README.md**：项目说明
- **SECURITY.md**：安全漏洞上报流程

5. **培训**：

- 团队 Git 最佳实践培训
- 定期代码审查
- 常见问题分享会

## 10. 实际案例分析

### 10.1 案例一：SSH 认证失败

**问题**：开发者在新机器上克隆仓库时，提示 `Permission denied (publickey)`。
**原因**：新机器没有配置 SSH 密钥，或者密钥未添加到 GitHub。
**解决方案**：

1. 生成新的 SSH 密钥
2. 添加密钥到 ssh-agent
3. 将公钥添加到 GitHub
4. 验证连接

### 10.2 案例二：大文件导致推送失败

**问题**：开发者尝试推送包含大文件的提交，提示文件超过 100MB 限制。
**原因**：GitHub 限制单个文件大小为 100MB。
**解决方案**：

1. 使用 Git LFS 跟踪大文件
2. 移除历史中的大文件
3. 重新推送

### 10.3 案例三：Actions 构建失败

**问题**：GitHub Actions 构建失败，提示依赖安装失败。
**原因**：依赖版本不兼容，或者网络问题导致依赖下载失败。
**解决方案**：

1. 检查依赖文件
2. 配置缓存
3. 添加重试机制
4. 检查网络连接



<!-- ============ 文档分隔线：004-github/032-ActionsMatrixBuild.md ============ -->


## 0. 开始之前：一条"批量生产线"的故事

想象一家饮料厂。过去，工厂里每种口味（橙汁、苹果汁、葡萄汁）都要**单独建一条生产线**，工人重复做同样的事：灌装、贴标、装箱。三倍口味 = 三倍设备、三倍人力、三倍维护成本。

后来工厂引进了一条**柔性生产线**：一条线上有一个"配方参数面板"，工人在面板上切换 `口味: [橙汁, 苹果汁, 葡萄汁]`、`包装: [瓶装, 罐装]`，机器就自动按每种组合各产一批。一套设备，同时覆盖 3×2=6 种产品。参数一变，全线跟着变，再也不用复制三套产线。

GitHub Actions 的**矩阵构建（Matrix Strategy）** 正是这条"柔性生产线"：你只写**一个 job 定义**，声明若干"配方参数"（操作系统、语言版本、浏览器……），GitHub 自动按所有组合生成多个并行的 job 实例。配置一份，处处运行。

## 1. 矩阵构建要解决的问题：先看清痛点

### 1.1 没有矩阵时的痛苦

假设你要在 Node.js 18、20、22 三个版本上跑测试。没有矩阵，你只能**复制粘贴三份 job**：

```yaml
jobs:
  test-node18:                 # 第一份：Node 18
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '18' }
      - run: npm test

  test-node20:                 # 第二份：Node 20（几乎一样的代码）
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm test

  test-node22:                 # 第三份：Node 22
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '22' }
      - run: npm test
```

问题一目了然：

- **改一处要改三处**：想加 `--reporter=json` 要同步改三个 job，极易漏改。
- **难以扩展**：想再加 macOS/Windows 两个系统？组合变 3×2=6 份，复制粘贴灾难升级。
- **可读性差**：一个工作流文件几百行，一半是重复代码。

### 1.2 矩阵的解法

```yaml
jobs:
  test:
    strategy:
      matrix:                  # 声明两个"维度"
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: [18, 20, 22]
    runs-on: ${{ matrix.os }}              # 读取当前组合的 os
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}  # 读取当前组合的 node-version
      - run: npm test
```

一份定义，GitHub 自动生成 **3 × 3 = 9 个并行 job**，分别对应每种 (os, node-version) 组合。

## 2. 原理：一次配置，多种环境

### 2.1 笛卡尔积：矩阵的数学内核

矩阵的本质是**笛卡尔积**：把每个维度（变量）的所有取值两两组合。`os: [A, B]`、`node-version: [X, Y, Z]` 会生成 2×3=6 种组合：

```
{os: A, node-version: X}   {os: A, node-version: Y}   {os: A, node-version: Z}
{os: B, node-version: X}   {os: B, node-version: Y}   {os: B, node-version: Z}
```

GitHub 官方文档确认了这一行为：**对矩阵中定义的每个变量组合，工作流都会运行一个 job**。

### 2.2 matrix 上下文：每个 job 如何知道自己该用哪个值

每个矩阵 job 运行时，`matrix` 上下文里装着**当前组合的完整取值**。通过 `${{ matrix.<变量名> }}` 引用：

```yaml
- name: 打印当前组合
  run: echo "正在 ${{ matrix.os }} 上测试 Node ${{ matrix.node-version }}"
```

这就像生产线上的工人看一眼参数面板，就知道这一批该灌什么口味。

### 2.3 递进理解：从"复制"到"模板化"

| 阶段 | 做法 | 维护成本 |
| --- | --- | --- |
| 复制粘贴 | 每个环境写一个 job | 高，改一处要改 N 处 |
| 模板化 | 一个 job + 矩阵变量 | 低，改一处全线生效 |
| 动态矩阵 | 矩阵由前置 job 用 JSON 生成 | 极低，按需生成组合 |

## 3. 语法详解：strategy.matrix 全家桶

### 3.1 基础定义

```yaml
jobs:
  example:
    strategy:
      matrix:                  # 矩阵定义
        version: [10, 12, 14]  # 维度一：版本
        os: [ubuntu-latest, windows-latest]  # 维度二：系统
    runs-on: ${{ matrix.os }}
```

### 3.2 include：给矩阵"加料"

`include` 有两个作用（官方文档）：

- **给已有组合追加额外变量**：当 include 条目中的键值对与某个已有组合匹配时，只在该组合上追加新变量。
- **新增一个独立组合**：当 include 条目不匹配任何已有组合时，直接新增一个 job。

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node-version: [18, 20]
    include:
      # 场景一：匹配已有组合（ubuntu + node 20），追加 experimental 变量
      - os: ubuntu-latest
        node-version: 20
        experimental: true

      # 场景二：不匹配任何组合，新增一个独立 job（macos + node 22）
      - os: macos-latest
        node-version: 22
        experimental: true

      # 场景三：只写部分键，其余键取 include 条目中补充的默认值
      - node-version: 22
        os: ubuntu-latest
        flag: nightly
# 最终 job 数：基础 2×2=4 个 + include 新增 2 个 = 6 个
```

注意：`include` 条目匹配判断只针对**已存在的组合**（笛卡尔积 + 之前 include 新增的组合），这是新手最容易误解的点。

### 3.3 exclude：剔除不需要的组合

有些组合毫无意义（比如"Windows 上跑 Linux 专用脚本"）或已知不兼容，用 `exclude` 去掉：

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    python: ['3.10', '3.11', '3.12']
    exclude:
      # 不在 Windows 上测 Python 3.10
      - os: windows-latest
        python: '3.10'
      # 不在 Ubuntu 上测 Python 3.10
      - os: ubuntu-latest
        python: '3.10'
# 结果：2×3=6 个组合，剔除 2 个，剩 4 个 job
```

### 3.4 执行顺序（重要）

GitHub 处理矩阵的完整顺序：

```
1. 先计算所有维度的笛卡尔积，得到基础组合集合
2. 应用 include：为匹配的组合追加变量，或新增组合
3. 应用 exclude：从当前集合中剔除匹配的组合
```

官方文档特别说明：`exclude` 会剔除 include 之前或之后产生的组合，建议把"先 include 再 exclude"作为习惯，逻辑更清晰。

### 3.5 fail-fast 与 max-parallel：失败策略与并发闸门

```yaml
strategy:
  fail-fast: true     # 默认值：任一矩阵 job 失败，立即取消其余所有 job
  # fail-fast: false  # 所有组合都跑完，收集完整失败信息
  max-parallel: 4     # 最多同时运行 4 个矩阵 job
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    node: [18, 20, 22]
```

- **fail-fast: true**：某个组合一旦失败就"叫停全场"，省运行分钟数，适合发现根本性问题时快速止损。
- **fail-fast: false**：9 个 job 全部执行完毕，适合"想收集所有环境下的失败清单"的场景。CI 中常用 false。
- **max-parallel**：限制同时运行的 job 数，防止目标系统（如共享数据库）被并发打爆。

## 4. 实战配置示例

### 4.1 多操作系统 + 多版本测试（最典型）

```yaml
name: Test Matrix
on: [push, pull_request]
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false          # 收集所有环境的失败信息
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node-version: [18, 20, 22]
        exclude:                # Windows + Node 18 已知有问题，跳过
          - os: windows-latest
            node-version: 18
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: npm
      - run: npm ci
      - run: npm test
```

### 4.2 多语言多命令组合（include 充当"配置表"）

用 include 直接定义"每种语言的构建/测试命令"，一条 job 通吃多语言：

```yaml
jobs:
  build:
    strategy:
      fail-fast: false
      matrix:
        include:
          - language: typescript
            build: npm run build
            test: npm test
          - language: python
            build: pip install -e .
            test: pytest
          - language: go
            build: go build ./...
            test: go test ./...
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build
        run: ${{ matrix.build }}
      - name: Test
        run: ${{ matrix.test }}
```

### 4.3 浏览器测试分片（并发放大）

E2E 测试很慢，用矩阵把测试**分片**并行跑：

```yaml
jobs:
  e2e:
    strategy:
      fail-fast: false
      matrix:
        browser: [chromium, firefox, webkit]
        shard: [1/4, 2/4, 3/4, 4/4]     # 4 个分片
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx playwright test --project=${{ matrix.browser }} --shard=${{ matrix.shard }}
```

### 4.4 容器多架构构建

```yaml
jobs:
  docker:
    strategy:
      matrix:
        platform: [linux/amd64, linux/arm64]
    runs-on: ubuntu-latest
    steps:
      - uses: docker/setup-qemu-action@v3   # 模拟其他 CPU 架构
      - uses: docker/setup-buildx-action@v3
      - uses: docker/build-push-action@v6
        with:
          platforms: ${{ matrix.platform }}
          push: true
          tags: myapp:latest-${{ matrix.platform }}
```

## 5. 动态矩阵：让矩阵自己长出来

静态矩阵在组合数量固定时很好用；但组合数量不确定（比如 monorepo 里包越来越多）时，可以用**动态矩阵**：先跑一个"探测 job"，把矩阵 JSON 输出，再让下游 job 用 `fromJSON` 消费它。

### 5.1 基于目录列表生成矩阵

```yaml
jobs:
  setup:                              # 探测 job：读取 packages/ 下的包名
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}   # 输出 JSON 给下游
    steps:
      - id: set-matrix
        run: |
          echo "matrix={\"include\":$(ls packages/ | jq -R -s -c 'split("\n") | map(select(length > 0)) | map({"package": .})')}" >> $GITHUB_OUTPUT

  test:                               # 消费 job：按 JSON 生成矩阵
    needs: setup
    strategy:
      matrix: ${{ fromJson(needs.setup.outputs.matrix) }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing package ${{ matrix.package }}"
```

### 5.2 基于文件变更生成矩阵

配合 `dorny/paths-filter`，只有被改动的模块才进入测试矩阵，省下大量分钟数：

```yaml
jobs:
  detect:
    runs-on: ubuntu-latest
    outputs:
      services: ${{ steps.filter.outputs.changes }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            auth: src/auth/**
            user: src/user/**
            order: src/order/**

  test:
    needs: detect
    if: needs.detect.outputs.services != '[]'
    strategy:
      matrix:
        service: ${{ fromJson(needs.detect.outputs.services) }}
    runs-on: ubuntu-latest
    steps:
      - run: npm test --workspace=src/${{ matrix.service }}
```

### 5.3 调试技巧：查看矩阵展开结果

在 step 里把矩阵 JSON 打印出来，一目了然：

```yaml
- name: Debug matrix
  run: echo "${{ toJson(matrix) }}"
```

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| include 条目没生效 | 期望新增的 job 不存在 | include 条目恰好匹配了某个已有组合，只追加了变量而未新增 job | 检查匹配逻辑；想让 include 条目不匹配现有组合，可用不同的变量值 |
| exclude 顺序理解错误 | 被排除的组合仍在运行 | exclude 放在 include 之前或组合规则混乱 | 记住顺序：笛卡尔积 → include → exclude |
| 矩阵组合数爆炸 | 一次运行几十上百个 job，分钟数耗尽 | 多维变量全排列组合过大 | 控制矩阵规模（建议不超过 20 个 job），用 exclude 剔除无意义组合，或改用动态矩阵 |
| Windows 上跑 Linux 命令失败 | `Command not found` | 没按系统区分命令 | 用 `if: runner.os == 'Windows'` 等条件分支，或使用跨平台写法 |
| fail-fast 导致信息丢失 | 第一个失败后其余 job 全被取消 | fail-fast 默认为 true | CI 场景显式设置 `fail-fast: false` |
| 在 `runs-on` 中引用错误变量名 | job 无法启动 | `${{ matrix.os }}` 与矩阵定义中变量名不一致 | 核对矩阵变量名与引用处拼写一致 |

## 8. 一句话记忆

**矩阵 = 一条柔性生产线：一份 job 定义 + 多个维度变量，GitHub 按笛卡尔积自动生成并行的多环境 job，include 加料、exclude 减料、fail-fast 控止损。**



<!-- ============ 文档分隔线：004-github/033-ActionsCacheDependency.md ============ -->


## 0. 开始之前：一个"厨房储物柜"的故事

想象你开了一家小餐馆，每天要做 50 道菜。没有储物柜的话，厨师每次做菜都要**从零开始**：去买菜、洗菜、切菜、备料，做完一道菜再全部重来一遍——哪怕今天和昨天的菜单一模一样。

后来你买了**厨房储物柜**：昨天买好的酱油、面粉、香料都存在柜子里，今天做菜直接"取用"，只有用完了或过期了才重新采购。做菜时间从 1 小时缩短到 10 分钟。你还在柜子上贴了标签（`key`），比如"酱油-大瓶-2026-07 批"，方便精准找到该用哪一瓶；万一指定的那瓶用完了，你还有备用的（`restore-keys`），凑合着先做，再补货。

GitHub Actions 的**依赖缓存**就是 CI 世界的"厨房储物柜"：把 npm/pip/go 下载好的依赖包存起来，下次构建直接复用，避免每次都从网络重新下载。本文从一个具体痛点出发，把缓存讲透。

## 1. 问题：每次 CI 都重新下载依赖，太慢了

### 1.1 痛点场景

一个典型的前端项目 CI 流水线是这样跑的：

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
    with:
      node-version: 20
  - run: npm ci          # 每次都从 npm 源下载几百 MB 依赖，耗时数分钟
  - run: npm test
```

每次提交、每个 PR 都会触发一次 `npm ci`，把几百 MB 的依赖从网络重新拉一遍。遇到网络波动还会更慢。对于一个几十上百人提交的仓库，这些"重复下载"浪费的分钟数和金钱非常可观。

### 1.2 缓存要解决的问题

缓存真正要解决的不是"让所有步骤都变快"，而是**减少重复下载和重复计算**：

- 依赖文件没变化时，就不要每次重新下载——直接复用缓存。
- 构建产物只用于本次交付，不要拿它当长期缓存（那是 Artifacts 的职责，见 035）。
- 把"依赖缓存"与"产物传递"的边界分清楚，优化才会清晰。

### 1.3 缓存的收益（官方实践数据）

GitHub 官方文档给出典型的收益预期：启用依赖缓存后，工作流运行时间可以从几分钟缩短到几十秒，尤其在依赖体积大的项目中效果显著。缓存对每个仓库最多可存 10 GB，超限后按"最久未访问"策略自动清理旧缓存。

## 2. 缓存原理：命中、未命中与匹配顺序

### 2.1 整体工作流程

```mermaid
flowchart TD
    T0["Job 开始"] --> T1["用 key 查找缓存"]
    T1 -->|"精确命中 key"| T2["恢复缓存到指定路径<br/>(cache hit)"]
    T1 -->|"未精确命中"| T3["按 restore-keys 顺序前缀匹配"]
    T3 -->|"部分命中"| T4["恢复最近的匹配缓存"]
    T3 -->|"都未命中"| T5["跳过恢复<br/>(cache miss)"]
    T2 --> T6["正常安装/执行"]
    T4 --> T6
    T5 --> T6
    T6 -->|"job 成功完成且未精确命中"| T7["保存新缓存<br/>(使用新 key)"]
```

### 2.2 命中与未命中的官方定义

根据 GitHub 官方文档（Dependency caching reference），恢复缓存时按以下顺序尝试：

1. **精确匹配 `key`**：如果找到了与 `key` 完全一致的缓存，视为 **cache hit**（缓存命中），直接恢复。
2. **按 `restore-keys` 顺序前缀匹配**：没有精确命中时，逐个用 `restore-keys` 做前缀匹配，取最近创建的匹配缓存。
3. **仍未命中**：视为 **cache miss**（缓存未命中），不恢复任何内容。

关键规则：**缓存未命中时，只要 job 最终成功完成，actions/cache 会自动用你提供的 `key` 保存一份新缓存**（内容为 `path` 指定的文件）。缓存保存后**不能原地修改**，只能通过新 key 生成新缓存——所以缓存策略有变时，改一下 key 里的版本号（如 `v2` → `v3`）就能自然切换到新缓存。

### 2.3 缓存范围与限制

| 限制项 | 值 | 说明 |
| --- | --- | --- |
| 单个缓存大小 | 最大 10 GB | 超大缓存会导致上传/下载变慢 |
| 仓库总缓存 | 最大 10 GB | 超限按最久未访问自动清理 |
| 缓存保留 | 7 天未访问自动删除 | 与 Artifacts 的保留策略不同 |
| 跨分支访问 | 当前分支 + 默认分支 | PR 还能访问 base 分支（目标分支）的缓存 |
| 缓存内容 | 禁止存放敏感信息 | 官方明确建议不要缓存 Token、凭据等 |

补充说明（官方文档）：PR 触发时创建的缓存会挂在 `refs/pull/.../merge` 下，通常只适合该 PR 自己重跑时使用；兄弟分支、不同 tag 之间不能随意互相读取缓存。

## 3. actions/cache 使用：从基础到各语言

### 3.1 基础用法

```yaml
steps:
  - uses: actions/cache@v4
    with:
      path: |                    # 要缓存/恢复的路径（支持多行、glob）
        ~/.npm
        node_modules
      key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}   # 精确键
      restore-keys: |            # 回退键（前缀匹配，按顺序尝试）
        npm-${{ runner.os }}-
```

参数详解：

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `path` | 是 | 缓存/恢复的路径，支持多路径和 glob；相对路径基于工作区目录解析 |
| `key` | 是 | 保存缓存时生成的键，也是查找缓存的键；最长 512 字符，超长会报错 |
| `restore-keys` | 否 | 回退键列表，每行一个，按顺序做前缀匹配 |
| `enableCrossOsArchive` | 否 | 设为 true 允许 Windows 运行器跨操作系统恢复缓存（默认 false） |

### 3.2 各语言缓存配置

**Node.js / npm**（缓存 npm 全局缓存目录，而非 node_modules）：

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
    restore-keys: npm-${{ runner.os }}-

- run: npm ci     # 缓存命中时秒装，未命中时才全量下载
```

**Python / pip**：

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: pip-${{ runner.os }}-${{ hashFiles('requirements.txt') }}
    restore-keys: pip-${{ runner.os }}-

- run: pip install -r requirements.txt
```

**Go**：

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/go/pkg/mod
      ~/.cache/go-build
    key: go-${{ runner.os }}-${{ hashFiles('go.sum') }}
    restore-keys: go-${{ runner.os }}-

- run: go mod download
```

**Java / Gradle**：

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.gradle/caches
      ~/.gradle/wrapper
    key: gradle-${{ runner.os }}-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}
    restore-keys: gradle-${{ runner.os }}-
```

**Rust / Cargo**：

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cargo/registry
      ~/.cargo/git
      target
    key: cargo-${{ runner.os }}-${{ hashFiles('**/Cargo.lock') }}
    restore-keys: cargo-${{ runner.os }}-
```

### 3.3 更省事的做法：setup-* 内置缓存

对主流语言，`setup-node`、`setup-python` 等官方 Action 已经内置缓存能力，**一行配置即可**，不必手写 actions/cache：

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm                     # 自动缓存 npm 全局缓存目录
    cache-dependency-path: package-lock.json   # monorepo 场景指定锁文件位置
```

注意：`setup-node` 的内置缓存**不缓存 node_modules**，而是缓存 npm 的全局包缓存目录，并根据 `package-lock.json` / `yarn.lock` 等锁文件自动生成缓存键。

## 4. 缓存策略设计：key 怎么设计才科学

### 4.1 key 的三层信息（官方推荐组合）

最常见的 key 写法是把"操作系统 + 语言版本 + 锁文件哈希"三要素放进去：

```yaml
key: ${{ runner.os }}-node-20-npm-v2-${{ hashFiles('**/package-lock.json') }}
```

- `runner.os`：区分 Linux/macOS/Windows。不同系统的依赖缓存不能混用（尤其带原生扩展的依赖）。
- `node-20`：区分运行时版本。Node/Python/Java 版本变了，缓存最好跟着变。
- `hashFiles(...)`：监听依赖变化。锁文件变了就生成新缓存，没变就尽量复用旧缓存。
- `v2`（可选）：手动版本号。未来调整缓存策略时，把 v2 改成 v3 即可自然切换到新缓存。

### 4.2 key 设计的两大误区

| 误区 | 后果 | 正确做法 |
| --- | --- | --- |
| key 太宽（如固定 `linux-node`） | 依赖换了还复用旧缓存，易污染、难排查 | key 至少包含 OS + 锁文件哈希 |
| key 太细（如把 `github.sha` 放进 key） | 每次提交 key 都不同，永远命中不了 | key 只放"会反映依赖变化"的信息，不要放提交 SHA |

### 4.3 多级回退：restore-keys 的正确打开方式

restore-keys 是"降级匹配"：精确 key 未命中时，按前缀尽量恢复一份**最近创建的**缓存，恢复后包管理器再补齐缺失依赖。注意：**restore-keys 命中的缓存不代表依赖完全一致，后续仍需执行安装命令**，不能因为恢复成功就跳过安装。

```yaml
key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
restore-keys: |
  npm-${{ runner.os }}-    # 一级回退：同系统最近缓存
  npm-                     # 二级回退：跨系统兜底
```

### 4.4 缓存命中判断：cache-hit 输出

通过 `cache-hit` 输出可以精确控制后续步骤（比如命中时用离线安装，未命中时全量安装）：

```yaml
- uses: actions/cache@v4
  id: cache-npm
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}

- name: Install dependencies (cache miss)
  if: steps.cache-npm.outputs.cache-hit != 'true'
  run: npm ci

- name: Install dependencies (cache hit)
  if: steps.cache-npm.outputs.cache-hit == 'true'
  run: npm ci --prefer-offline
```

### 4.5 条件缓存：只在需要的分支保存

```yaml
- uses: actions/cache@v4
  if: github.ref == 'refs/heads/main'   # 仅 main 分支保存新缓存，PR 只恢复不保存
  with:
    path: ~/.npm
    key: npm-${{ runner.os }}-${{ hashFiles('package-lock.json') }}
```

## 5. 缓存管理：查看、清理与监控

### 5.1 用 gh 命令管理缓存

```bash
# 列出仓库所有缓存
gh cache list

# 按键前缀删除缓存
gh cache delete <key>

# 删除所有缓存
gh cache delete --all
```

### 5.2 通过 REST API 精确清理

```bash
# 获取所有缓存 ID 并逐个删除
gh api repos/OWNER/REPO/actions/caches \
  --jq '.actions_caches[].id' | \
  xargs -I {} gh api repos/OWNER/REPO/actions/caches/{} --method DELETE
```

### 5.3 缓存大小监控

```yaml
- name: Check cache size
  run: |
    du -sh ~/.npm || true
    du -sh ~/.cache/pip || true
    du -sh ~/go/pkg/mod || true
```

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 缓存永远不命中 | 每次构建都重新下载依赖 | key 中包含了每次提交都变化的变量（如 `github.sha`） | key 只保留 OS、语言版本、锁文件哈希等稳定信息 |
| 把 node_modules 塞进缓存 | 缓存巨大、跨平台冲突 | node_modules 含平台相关二进制，且体积大 | 只缓存包管理器缓存目录（如 `~/.npm`），不缓存 node_modules |
| 缓存命中后跳过安装导致依赖缺失 | 构建报找不到模块 | 误以为恢复缓存 = 依赖完整（restore-keys 部分命中时依赖可能不全） | 命中后仍执行安装命令，用 `npm ci --prefer-offline` 加速 |
| key 超过 512 字符 | actions/cache 执行失败 | key 太长 | 精简 key，去掉冗余变量 |
| 缓存里混入敏感文件 | 凭据泄露风险 | 把含 Token 的文件一起缓存了 | 官方明确建议：缓存中不要存放访问令牌、登录凭据等敏感信息 |
| 分支间互相读不到缓存 | 缓存命中率低 | 不了解缓存范围：兄弟分支、不同 tag 之间不能互读 | 依赖"当前分支 + 默认分支"的缓存规则设计 key 与恢复策略 |
| 缓存策略变更后旧缓存干扰 | 出现奇怪构建结果 | 新逻辑与旧缓存内容不兼容 | 在 key 中加手动版本号（v2 → v3），自然淘汰旧缓存 |

## 8. 一句话记忆

**缓存是 CI 的"厨房储物柜"：用 key 精确存取依赖包，锁文件不变就复用，变了就自动换新钥匙，restore-keys 兜底降级，让依赖安装从"重新买菜"变成"开柜取用"。**



<!-- ============ 文档分隔线：004-github/034-ActionsSelfHostedRunner.md ============ -->


## 0. 开始之前："自家健身房"与"商业健身房"的选择

想健身，你有两种选择：

- **商业健身房**：办卡就能去，器械全新、环境干净，有教练指导，不操心维护。缺点：器械规格固定（没有你家那台祖传跑步机）、人多要排队、月卡按时间收费。
- **自家健身房**：把自家车库改造成健身房，器械随你挑（可以买专业深蹲架、上跑步机还能看内网监控）。缺点：设备自己买、坏了自己修、还要操心防盗。

GitHub Actions 的**运行器（Runner）** 就是"执行工作流的机器"，同样有这两种形态：

- **GitHub 托管运行器（GitHub-hosted runner）**：商业健身房。GitHub 提供现成的虚拟机（Linux/macOS/Windows），用完即焚，干净隔离。
- **自托管运行器（Self-hosted runner）**：自家健身房。你把**自己的服务器/电脑**接入 GitHub 来跑任务，硬件、环境、网络全由你掌控，但也由你负责安全与维护。

本文采用**对比驱动**的方式，把这两种运行器从头到尾比一遍，再深入讲自托管运行器的注册、标签与安全。

## 1. 运行器是什么：先直观理解

### 1.1 一个朴素的问题

工作流（workflow）是写在 YAML 里的"指令"，指令总得有台机器去执行吧？`runs-on: ubuntu-latest` 里的 `ubuntu-latest` 就是告诉 GitHub："这次任务给我一台最新的 Ubuntu 虚拟机来跑"。这台"执行机器"就是运行器。

```yaml
jobs:
  build:
    runs-on: ubuntu-latest        # GitHub 托管运行器：标准虚拟机
    steps:
      - run: echo "Hello"

  build-local:
    runs-on: [self-hosted, linux] # 自托管运行器：你自己的机器
    steps:
      - run: echo "Hello"
```

### 1.2 运行器在 Actions 体系中的位置

```
事件（push/PR/定时）→ 触发工作流 → 分配 job → 匹配运行器 → 在运行器上依次执行 steps
                                              │
                        runs-on: ubuntu-latest（托管） 或 [self-hosted, linux]（自托管）
```

## 2. 全程对比：GitHub 托管运行器 vs 自托管运行器

### 2.1 大对比表

| 维度 | GitHub 托管运行器 | 自托管运行器 |
| --- | --- | --- |
| 硬件规格 | 固定（标准型约 2 核 CPU/7 GB 内存/14 GB SSD） | 完全自定义（大内存、多核、GPU 都行） |
| 环境洁净度 | 每次任务都是全新虚拟机，用完销毁 | 持久环境，上一个任务可能留下文件 |
| 费用 | 公开仓库免费；私有仓库按分钟计费（含免费额度） | 自行承担硬件、电费与运维成本 |
| 网络 | 公网环境 | 可访问内网资源（数据库、私有 API） |
| GPU | 不支持 | 可配置 GPU（ML/AI 训练） |
| 运行时长限制 | 有超时限制 | 可跑更长时间的任务 |
| 安全 | 隔离环境，风险低 | 需要自行加固，风险高 |
| 维护 | GitHub 全权维护 | 自己负责升级、监控、排障 |

### 2.2 什么场景该选自托管（官方建议 + 实践经验）

- 需要 **GPU** 的 ML/AI 训练任务。
- 需要访问**内网资源**（公司数据库、内部 API、私有镜像仓库）。
- 需要**特殊硬件/架构**（ARM 芯片、特定 CPU 指令集）。
- 需要**持久缓存**（大体积依赖、Docker 镜像，见 033 缓存主题）。
- 需要**更长运行时间**的任务。
- **成本优化**：私有仓库高频使用时，按分钟计费可能比自建更贵；官方给出的经验是"运行时间较多时自托管更划算"。

### 2.3 什么时候别选自托管

一个极其重要的官方警告：**GitHub 官方强烈建议只对私有仓库使用自托管运行器**。因为公开仓库的 fork 可能通过 PR 在工作流中执行任意代码——一旦这些代码跑在你的自托管机器上，就相当于陌生人拿到了你服务器的执行权限。如果必须用于公开仓库，务必做好隔离与加固（见第 5 节）。

## 3. 注册与安装：把"自家健身房"开起来

### 3.1 前置条件

- 能安装并运行自托管运行器应用的机器（支持 Linux、Windows 10/11、macOS 11.0+，以及 x64/ARM64/ARM32 架构）。
- 机器能与 GitHub 通信（出站 HTTP/HTTPS 连接）。
- 硬件资源足够跑目标工作流（运行器应用本身占用极小）。
- 若工作流使用 Docker 容器或服务容器，必须是 Linux 机器且安装了 Docker。

### 3.2 添加运行器（官方标准流程）

在仓库 **Settings → Actions → Runners → New self-hosted runner** 页面，选择操作系统与架构后，GitHub 会给出完整的安装命令，核心四步如下：

```bash
# 1. 下载运行器应用（以 Linux x64 为例，版本号以页面提示为准）
mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.311.0.tar.gz -L \
  https://github.com/actions/runner/releases/download/v2.311.0/actions-runner-linux-x64-2.311.0.tar.gz

# 2. 解压
tar xzf ./actions-runner-linux-x64-2.311.0.tar.gz

# 3. 配置并注册（--token 为页面生成的限时令牌，约 1 小时后过期，过期需重新生成）
./config.sh --url https://github.com/OWNER/REPO --token ABC123

# 4. 启动运行器
./run.sh
```

Windows 上的对应命令为 `.\config.cmd` 与 `.\run.cmd`；若要把运行器安装为 Windows 服务，需要用管理员权限的 shell 打开。

### 3.3 作为服务运行（Linux/macOS，推荐生产用法）

直接跑 `./run.sh` 会占用一个终端，机器重启后还要手动再跑。推荐用官方自带的 systemd 服务脚本：

```bash
# 安装为 systemd 服务
sudo ./svc.sh install

# 启动 / 查看状态 / 停止
sudo ./svc.sh start
sudo ./svc.sh status
sudo ./svc.sh stop

# 卸载服务
sudo ./svc.sh uninstall
```

### 3.4 自动补全：注册时的可选参数

```bash
# 配置时指定自定义标签（逗号分隔）
./config.sh --url https://github.com/OWNER/REPO --token ABC123 --labels gpu,linux-arm64,high-memory

# 不添加默认标签（默认标签见第 4 节）
./config.sh --url https://github.com/OWNER/REPO --token ABC123 --no-default-labels

# 临时运行器：每次任务执行后自动注销（安全场景推荐，见第 5 节）
./config.sh --url https://github.com/OWNER/REPO --token ABC123 --ephemeral
```

## 4. 标签与路由：如何把任务"派"到正确的机器

### 4.1 默认标签

运行器注册后会自动获得以下默认标签（官方定义）：

| 标签 | 含义 |
| --- | --- |
| `self-hosted` | 所有自托管运行器默认带此标签 |
| `linux` / `windows` / `macOS` | 按操作系统自动打标 |
| `x64` / `ARM` / `ARM64` | 按硬件架构自动打标 |

### 4.2 在 workflow 中按标签选择运行器

```yaml
jobs:
  build:
    # 需要同时满足三个标签才派单：自托管 + Linux + ARM64
    runs-on: [self-hosted, linux, ARM64]
    steps:
      - run: echo "在 ARM64 的 Linux 自托管机器上执行"
```

自定义标签示例（给装了 GPU 的机器打 `gpu` 标）：

```yaml
jobs:
  train:
    runs-on: [self-hosted, gpu]     # 只派给带 gpu 标签的机器
    steps:
      - run: nvidia-smi
```

### 4.3 运行器组（Runner Groups）

组织级运行器可以分组，组内的仓库才可用该组运行器——适合"敏感环境只给特定仓库用"：

```yaml
jobs:
  deploy:
    runs-on: [self-hosted, linux, x64]   # 从匹配的运行器组中调度
    steps:
      - run: ./deploy.sh
```

### 4.4 路由规则（官方行为）

GitHub 调度 job 到自托管运行器的规则：

1. 查找与 job 的 `runs-on` **标签和组全部匹配**的在线空闲运行器，把任务派过去。
2. 若运行器在 **60 秒内**未接单，任务会被重新排队，换一台运行器接。
3. 若一直没有匹配的在线运行器，job 会一直排队，**排队超过 24 小时**则失败。

## 5. 安全加固：自家健身房要有"门禁"

### 5.1 安全风险清单

| 风险 | 说明 |
| --- | --- |
| 任意代码执行 | PR 中的恶意代码可直接在运行器上执行（官方警告的核心） |
| 凭据泄露 | 运行器上的环境变量、文件、密钥可被读取 |
| 持久化攻击 | 修改运行器环境（装后门、改全局配置）影响后续所有 job |
| 内网渗透 | 自托管运行器可访问内网，成为攻击跳板 |

### 5.2 官方推荐的安全措施

**措施一：只对私有仓库使用自托管运行器**（官方首要建议）。fork 无法在私有仓库创建 PR。

**措施二：使用临时（ephemeral）运行器**。每个 job 结束后自动注销，不留持久环境：

```bash
./config.sh --url https://github.com/OWNER/REPO --token ABC123 --ephemeral
```

**措施三：限制 PR 触发**。即使要用，也只允许同仓库内部 PR 触发：

```yaml
jobs:
  build:
    # 仅当 PR 来自本仓库（而非 fork）时运行
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: [self-hosted, linux]
```

**措施四：用容器隔离任务**。让任务跑在容器里，降低对宿主机的污染：

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux]
    container:
      image: node:22
      options: --user 1001        # 以非 root 用户运行
    steps:
      - run: npm test
```

**措施五：最小权限 + 专用账号**。用专用低权限系统账号运行运行器，避免用 root/管理员：

```bash
sudo useradd -m -s /bin/bash github-runner
sudo -u github-runner ./config.sh --url https://github.com/OWNER/REPO --token ABC123
```

**措施六：任务结束后清理现场**：

```yaml
steps:
  - name: Cleanup
    if: always()
    run: |
      rm -rf $RUNNER_TEMP/*
      rm -rf $GITHUB_WORKSPACE/*
      docker system prune -af 2>/dev/null || true
```

## 6. 自动扩展：健身房按客流调整营业面积

任务多时要多台机器，任务少时要省钱，就需要**自动扩展**。官方推荐方案是 **Actions Runner Controller（ARC）**——基于 Kubernetes 的官方参考实现。

### 6.1 ARC 部署要点

```bash
# 1. 安装 cert-manager（ARC 依赖）
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.1/cert-manager.yaml

# 2. 用 Helm 安装 ARC
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
helm install arc actions-runner-controller/actions-runner-controller \
  --namespace arc-systems --create-namespace

# 3. 应用 RunnerDeployment 配置（见下）
kubectl apply -f runnerdeployment.yaml
```

### 6.2 RunnerDeployment 示例

```yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: org-runner
spec:
  replicas: 2                 # 基础副本数
  template:
    spec:
      organization: my-org    # 注册到组织
      labels:
        - k8s-runner          # 自定义标签
      resources:
        limits:
          cpu: '4'
          memory: 8Gi
      dockerEnabled: false
```

### 6.3 按队列长度扩缩容

```yaml
autoscaling:
  enabled: true
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: External
      external:
        metric:
          name: github_runner_queue_length   # 按待执行 job 队列长度扩容
        target:
          type: AverageValue
          averageValue: '1'
```

## 7. 运维管理：日常体检与排障

### 7.1 健康检查

```yaml
- name: Runner health check
  run: |
    echo "OS: $RUNNER_OS / Arch: $RUNNER_ARCH"
    df -h          # 磁盘
    free -h        # 内存
```

### 7.2 更新运行器

```bash
# 停止服务 → 重新配置 → 启动
sudo ./svc.sh stop
./config.sh --url https://github.com/OWNER/REPO --token NEW_TOKEN
sudo ./svc.sh start
```

### 7.3 常见排障手段

```bash
# 查看运行器诊断日志
cat ~/actions-runner/_diag/Runner_*.log

# 查看 systemd 服务日志
journalctl -u actions.runner.*

# 用 API 查看注册的运行器列表与状态
curl -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/actions/runners
```

### 7.4 生命周期

```
Online（在线空闲）→ Running（执行中）→ Idle → ...
                       ↓
                  Offline（手动停止/故障）
                       ↓
                  Online（重新连接）
```

## 8. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| job 一直排队不运行 | 任务卡在 queued 状态 | 没有与 `runs-on` 标签匹配的在线运行器 | 检查运行器是否在线、标签是否匹配；注意排队超 24 小时会失败 |
| 注册 token 失效 | `Invalid registration token` | 注册令牌约 1 小时后过期 | 回到 Settings → Runners 页面重新生成 token |
| fork 的 PR 在自托管运行器上跑恶意代码 | 机器被攻击 | 公开仓库 + 自托管运行器的固有风险 | 官方建议仅私有仓库使用；必须用时加 `--ephemeral` 与同仓库 PR 限制 |
| 工作流需要 Docker 但运行器不支持 | 容器相关步骤报错 | 自托管运行器跑容器任务需 Linux + 已装 Docker | 用 Linux 机器并安装 Docker，或改用托管运行器 |
| 运行器被前一个任务"污染" | 任务结果不稳定 | 持久环境残留文件/环境变量 | 任务里做清理，或使用 ephemeral 运行器 |
| 60 秒未接单导致重派 | job 在运行器间反复跳转 | 运行器启动慢或网络抖动 | 检查运行器资源与网络，确保及时接单 |
| 队列超 24 小时 | job 直接失败 | 一直没有匹配运行器在线 | 监控运行器在线率，必要时上 ARC 自动扩展 |

## 10. 一句话记忆

**自托管运行器 = 自家健身房：硬件网络全自控，安全维护全自负——官方只建议私有仓库使用，标签路由派单、ephemeral 隔离、最小权限加固是三条保命底线。**



<!-- ============ 文档分隔线：004-github/035-ActionsArtifact.md ============ -->


## 0. 开始之前：一个"快递驿站"的故事

小区里有个**快递驿站**。你在淘宝下单，快递员（构建 Job A）把包裹放到驿站（GitHub 存储），你在驿站取了包裹回家（测试 Job B / 部署 Job C 下载使用）。驿站还有三个特点：

1. **中转不保存**：驿站只是中转站，包裹放久了会被清退（保留期到了自动删除）。
2. **凭单取件**：驿站不代收现金，你的"取件码"就是制品名称（artifact name）。
3. **跨网点不行**：驿站在哪个小区，就只能服务这个小区的居民（制品归属于特定工作流运行，跨工作流取件需要特殊"凭证"）。

GitHub Actions 的**制品（Artifacts）** 就是 CI 世界的"快递驿站"：把构建产物、测试报告、日志等文件**存起来**，供同一个工作流里的后续 job 下载，或供你在 Actions 页面手动下载查看。本文按**"上传 → 下载 → 过期管理"**的完整流程展开。

## 1. 制品是什么：先直观理解

### 1.1 一个关键痛点

每个 job 都跑在**独立的运行器**上，job 之间的文件系统是隔离的：构建 job 编译出的 `dist/` 目录，测试 job 根本看不到。要传递数据，靠什么？

- **job 输出（outputs）**：只能传字符串，传不了文件。
- **制品（Artifacts）**：专为传递文件设计——上传到 GitHub 存储，下游 job 下载。

```mermaid
flowchart LR
    JA[Job A 构建<br/>编译代码<br/>上传制品] -->|制品| JB[Job B 测试<br/>下载制品 运行测试]
    JB -->|测试报告| JC[Job C 部署<br/>下载制品 部署]
```

### 1.2 官方对制品的定义

GitHub 官方文档的定义：制品是工作流运行过程中产生的**一个文件或一组文件**。例如：

- 日志文件与核心转储（core dumps）
- 测试结果、失败截图
- 二进制或压缩文件
- 压测性能输出与代码覆盖率结果

制品允许你在 job 完成后**持久化数据**，并与同一工作流中的其他 job 共享。默认情况下，GitHub 会**保留构建日志和制品 90 天**，保留期可自定义。

### 1.3 制品 vs 缓存：别把两种"存储"搞混

| 维度 | 制品（Artifacts） | 缓存（Caches） |
| --- | --- | --- |
| 目的 | 传递/交付文件 | 加速重复步骤 |
| 生命周期 | 默认保留 90 天 | 7 天未访问自动删除 |
| 典型用途 | 构建产物、测试报告、安装包 | npm/pip 依赖包 |
| 访问方式 | 显式上传/下载 | key 自动命中 |
| 最佳实践 | 每次运行按需上传 | 依赖不变就复用 |

一句话：**缓存省"重复下载"，制品做"传递交付"**。

## 2. 流程第一步：上传（actions/upload-artifact）

### 2.1 基本用法

```yaml
- name: Upload build artifacts
  uses: actions/upload-artifact@v4
  with:
    name: dist-files            # 制品名称（同一工作流内唯一）
    path: |                     # 要上传的路径（支持多路径、glob）
      dist/
      package.json
    retention-days: 5           # 保留天数（1-90，默认跟随仓库设置 90 天）
    compression-level: 6        # 压缩级别 0-9（默认 6；大文件可选 0 提速）
    if-no-files-found: error    # 无匹配文件时的行为：warn | error | ignore
```

### 2.2 参数详解

| 参数 | 说明 |
| --- | --- |
| `name` | 制品名称，默认 `artifact`；在同一工作流运行内应唯一 |
| `path` | 必填。文件、目录或通配符模式；路径基于运行器工作区解析 |
| `retention-days` | 保留天数，1-90，0 表示使用默认（仓库设置，通常 90 天） |
| `compression-level` | 压缩级别 0-9，默认 6；不易压缩的大文件建议 0 以显著加快上传 |
| `if-no-files-found` | `warn`（默认，警告不报错）/ `error`（报错）/ `ignore`（静默跳过） |
| `overwrite` | true 时同名制品会被删除后重新上传；false 时同名直接报错 |

### 2.3 v4 版本的重要变化（迁移须知）

官方已在 2024 年弃用 v3 及更早版本，请使用 **v4**。v4 的关键行为变化：

| 变更项 | v3 行为 | v4 行为 |
| --- | --- | --- |
| 制品名称冲突 | 同名自动覆盖 | 报错，必须唯一（除非 `overwrite: true`） |
| 跨工作流下载 | 默认可下载 | 需指定 `run-id` + `github-token` |
| 上传合并 | 同名自动合并 | 不再自动合并 |
| 下载默认行为 | 不带 name 下载全部并平铺 | 行为更严格，推荐显式指定 |

## 3. 流程第二步：下载（actions/download-artifact）

### 3.1 基本用法

```yaml
- name: Download build artifacts
  uses: actions/download-artifact@v4
  with:
    name: dist-files        # 指定制品名称
    path: dist/             # 下载到指定目录（默认解压到当前目录）
```

不指定 `name` 时下载该运行的所有制品（v4 起更推荐显式指定，避免歧义）。

### 3.2 同工作流内跨 Job 传递（最常见流程）

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/

  test:
    needs: build                      # 必须等 build 完成（上传先于下载）
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/
      - run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          path: dist/
      - run: ./deploy.sh
```

**易错点**：下载 job 必须用 `needs` 声明依赖上传 job，否则下载可能发生在上传之前，报"找不到制品"。

### 3.3 矩阵构建中的制品命名

矩阵的每个组合是独立 job，但共享同一运行内的制品命名空间——**同名制品会冲突**。解法：名称里带上矩阵变量：

```yaml
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - run: npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-${{ matrix.os }}    # 名称包含矩阵变量，避免冲突
          path: dist/
```

### 3.4 跨工作流下载（需要"取件凭证"）

制品归属于**特定工作流运行**。另一个工作流要取件，必须提供 `run-id`（来源运行 ID）与 `github-token`：

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          name: build-output
          run-id: ${{ github.event.workflow_run.id }}   # 来源工作流运行 ID
          github-token: ${{ secrets.GITHUB_TOKEN }}     # 访问令牌
```

配合 `workflow_run` 触发器（监听"Build"工作流完成后自动触发）更常见：

```yaml
# deploy.yml
on:
  workflow_run:
    workflows: ['Build']      # 监听构建工作流
    types: [completed]        # 无论成败都触发（也可加 branches 过滤）

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with:
          run-id: ${{ github.event.workflow_run.id }}
```

## 4. 流程第三步：过期与管理

### 4.1 保留期策略（官方默认 90 天）

- 默认保留 **90 天**，可通过 `retention-days` 单独设置（1-90）。
- 对 PR 而言，**每次向 PR 推送新提交，保留期会重新计时**。
- 制品存储占用仓库存储空间，私有仓库超出免费额度会按量计费——**默认 90 天几乎总是太长**。

按用途设置合理的保留期（社区实践参考）：

| 制品用途 | 建议保留期 |
| --- | --- |
| PR 构建产物（仅 job 间传递） | 1 天 |
| 测试报告、截图 | 3-5 天 |
| 失败调试快照 | 3 天 |
| main 分支构建产物（供回滚排查） | 7-14 天 |
| Release 交付包 | 30 天 |

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: temp-build
    path: dist/
    retention-days: 1          # 1 天后自动删除
```

### 4.2 只在需要时上传（省存储）

测试报告只有失败时才有用，用 `if: failure()` 条件上传：

```yaml
- name: Upload debug snapshot
  if: failure()                # 仅在失败时上传
  uses: actions/upload-artifact@v4
  with:
    name: debug-${{ github.run_id }}
    path: |
      logs/
      screenshots/
    retention-days: 3
```

### 4.3 手动删除

```bash
# 用 GitHub CLI 删除指定名称的制品
gh api repos/OWNER/REPO/actions/artifacts \
  --jq '.artifacts[] | select(.name == "temp-build") | .id' | \
  xargs -I {} gh api repos/OWNER/REPO/actions/artifacts/{} --method DELETE
```

### 4.4 体积优化

```yaml
- uses: actions/upload-artifact@v4
  with:
    name: build
    path: |
      dist/
      !dist/**/*.map            # 排除 source map
    compression-level: 9        # 最高压缩（更慢上传但更省空间）
```

## 5. 典型应用场景

### 5.1 测试报告 + 覆盖率（配合 always()）

```yaml
- name: Run tests
  run: npm test -- --reporter=json --output=test-results.json

- name: Upload test results
  if: always()                  # 测试失败也要上传，便于排查
  uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: test-results.json
    retention-days: 7

- name: Upload coverage report
  uses: actions/upload-artifact@v4
  with:
    name: coverage-report
    path: coverage/
    retention-days: 14
```

### 5.2 多平台安装包分发

```yaml
- name: Build all platforms
  run: npm run build:all

- name: Upload Linux binary
  uses: actions/upload-artifact@v4
  with: { name: app-linux, path: dist/app-linux }

- name: Upload macOS binary
  uses: actions/upload-artifact@v4
  with: { name: app-macos, path: dist/app-macos }

- name: Upload Windows binary
  uses: actions/upload-artifact@v4
  with: { name: app-windows, path: dist/app-windows }
```

### 5.3 E2E 失败视频/截图快照

```yaml
- name: Upload E2E failure artifacts
  if: failure()                 # 只在失败时上传，省空间
  uses: actions/upload-artifact@v4
  with:
    name: e2e-failures-${{ github.run_id }}
    path: |
      cypress/videos/
      cypress/screenshots/
    retention-days: 3
```

## 6. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 上传后提示无文件 | `Warning: No files were found with the provided path: dist/` | 上传路径基于运行器工作区解析，可能与前一步 `cd subdir` 后的实际路径不符 | 确认路径写的是工作区相对路径；必要时先 `ls` 验证产物位置 |
| 下载 job 报找不到制品 | `Error: Unable to find artifact 'build-output'` | 下载先于上传发生（未用 `needs` 建立依赖） | 下载 job 加 `needs: build` |
| 矩阵 job 制品互相覆盖/冲突 | v4 直接报错 | 所有矩阵组合共用同一命名空间，同名制品冲突 | 制品名带矩阵变量，如 `name: build-${{ matrix.os }}` |
| 跨工作流下载失败 | 提示权限不足或找不到 | 制品归属于来源运行，跨工作流需 `run-id` + `github-token` | 补全 `run-id` 与 `github-token` 参数 |
| 存储空间被占满 | `Artifact storage quota has been hit` | 每次运行都上传大制品 + 默认 90 天保留期过长 | 设置合理 `retention-days`、用 `if: failure()` 条件上传、压缩级别调优 |
| 升级 v3 → v4 后行为异常 | 同名覆盖变报错、下载行为变化 | v4 对命名冲突与下载做了更严格限制 | 按 v4 迁移指南调整：名称唯一或用 `overwrite: true`，显式指定 name |

## 8. 一句话记忆

**制品是 CI 的"快递驿站"：上传（upload-artifact）寄存、下载（download-artifact）取件、过期自动清退；同工作流靠名称取件，跨工作流要 run-id 加令牌。**



<!-- ============ 文档分隔线：004-github/036-ActionsEnvironmentDeploy.md ============ -->


## 0. 开始之前：一次"考场分区"的旅程

一所学校办大型考试，考生要经过**四个教室**，每个教室的"门禁"不一样：

- **开发教室（dev）**：随便进，学生自己练习（自动部署，无门禁）。
- **测试教室（test）**：扫码自动进入，机器阅卷（自动化测试，自动放行）。
- **预演教室（staging）**：和正式考场一模一样，但要值班老师在场才能开门（自动触发 + 人工确认）。
- **正式考场（production）**：最难进——必须监考组长批条（审批）、考生名单限定（分支限制）、考场钥匙只能放保险柜（环境密钥）。

每一次代码发布，就像一批"考生"走过这趟旅程：**开发 → 测试 → 预发布 → 生产**。GitHub Actions 的**环境（Environments）** 就是这套"考场分区 + 发布许可门禁"系统。本文按这条"旅程"展开。

## 1. 环境是什么：先直观理解

### 1.1 官方定义

GitHub 官方文档的定义：环境用于描述一般的**部署目标**，如 `production`、`staging` 或 `development`。当工作流部署到某个环境时，该环境会显示在仓库主页上（部署历史一目了然）。

你可以用**保护规则（protection rules）**和**机密（secrets）**来配置环境。关键机制是：

> **引用环境的工作流作业，在运行或访问该环境的机密之前，必须先通过该环境的全部保护规则。**

一句话：**环境 = 部署目标 + 保护规则 + 独立密钥的三合一容器**。

### 1.2 环境旅程地图

```
代码提交 → CI 构建 → 部署 dev → 验证 test → 预发布 staging → 生产 production
                       │           │            │              │
                     自动部署      自动验证      人工确认        严格审批+分支限制
```

| 环境 | 用途 | 建议保护规则 |
| --- | --- | --- |
| dev | 开发环境，快速验证 | 无或最少 |
| test | 自动化测试环境 | 自动触发 |
| staging | 预发布，模拟生产 | 自动触发 + 人工确认 |
| production | 生产环境 | 必需审查者 + 分支限制（+ 等待计时器） |

### 1.3 适用计划说明

环境、环境机密与部署保护规则在**公共仓库**对所有现行 GitHub 计划开放；私有/内部仓库需要 **GitHub Pro、Team 或 Enterprise** 计划。

## 2. 创建环境：给旅程设"站点"

### 2.1 通过网页界面

仓库 **Settings → Environments → New environment**，输入环境名（如 `production`）创建。

### 2.2 通过 API / gh 命令

```bash
# 创建（或更新）名为 production 的环境
gh api repos/OWNER/REPO/environments/production --method PUT
```

### 2.3 在工作流中引用环境

```yaml
jobs:
  deploy:
    environment: production      # 引用环境：必须先过保护规则才能跑
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

## 3. 环境密钥与环境变量：每个考场的"保险柜"

### 3.1 环境密钥（Environment Secrets）

不同环境可以配置**同名的不同密钥值**——这是环境的核心价值：生产数据库密码绝不给 dev 用。

```yaml
jobs:
  deploy:
    environment: production
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        env:
          DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}      # 生产环境专属密钥
          DATABASE_URL: ${{ secrets.DATABASE_URL }}  # 生产数据库地址
        run: ./deploy.sh
```

三个环境的"同名不同值"示意：

```
dev:
  DATABASE_URL: postgres://localhost:5432/dev
staging:
  DATABASE_URL: postgres://staging-db:5432/app
production:
  DATABASE_URL: postgres://prod-db:5432/app
```

### 3.2 密钥优先级（官方规则）

如果同一个密钥在**仓库级**和**环境级**都配置了，**环境级密钥自动覆盖仓库级密钥**。这正是安全边界所在：生产凭据只在满足所有保护规则的生产环境 job 中可见，其他分支、其他 job 都拿不到。

### 3.3 环境变量

```yaml
jobs:
  deploy:
    environment:
      name: production
    runs-on: ubuntu-latest
    env:
      DEPLOY_ENV: production
    steps:
      - run: echo "Deploying to $DEPLOY_ENV"
```

## 4. 保护规则：旅程中的"门禁"

保护规则要求特定条件满足后，引用该环境的 job 才能继续。官方提供的规则包括：**必需审查者、等待计时器、部署分支限制、自定义保护规则（GitHub Apps）**。注意：仓库中可以安装任意数量的自定义保护规则，但**一个环境同时最多启用 6 条**。

### 4.1 必需审查者（Required Reviewers）：人工审批流

在 **Settings → Environments → production → Required reviewers** 中配置 1-6 个审查者（人或团队）。规则生效后：

- 工作流跑到引用该环境的 job 时**自动暂停**，等待审批。
- 审查者在 Actions 页面点击 **Approve**（批准）或 **Reject**（拒绝）。
- **只要其中一位必需审查者批准即可继续**（不必全员批准）。
- 审查者至少需要仓库的**读取权限**。

```yaml
jobs:
  deploy-production:
    environment: production      # 该 job 会等待人工审批
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

可选增强：启用"禁止自我审查"（prevent self-review），发起部署的人即使是指定审查者也不能自己批准自己，确保"部署的人 ≠ 批准的人"。

### 4.2 等待计时器（Wait Timer）：延迟放行

在环境设置中配置 0-43200 分钟（最长 30 天）的等待时间，job 会**先等待再开始**——适合给相关方留出最终检查窗口。

### 4.3 部署分支限制（Deployment Branches）：限定"考生名单"

配置允许部署到该环境的分支：

- **All branches**：任何分支都能部署。
- **Protected branches**：仅受保护分支。
- **Selected branches**：指定分支名模式（支持通配符）。

```
release/*     → 匹配 release/1.0、release/2.0
main          → 精确匹配 main
feature/*     → 匹配 feature/xxx
```

### 4.4 自定义保护规则（GitHub Apps）

官方支持通过 GitHub App 实现第三方保护规则，用于接入可观测性系统、变更管理系统、代码质量系统等——在部署安全落地前评估就绪度。

## 5. 部署工作流设计：多环境渐进部署

### 5.1 完整渐进式部署（build → dev → staging → production）

```yaml
name: Deploy Pipeline

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci && npm run build
      - uses: actions/upload-artifact@v4
        with:
          name: build-output
          path: dist/

  deploy-dev:                       # 第一站：开发环境（无门禁）
    needs: build
    environment: dev
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: build-output, path: dist/ }
      - run: ./deploy.sh dev

  deploy-staging:                   # 第二站：预发布（可能有人工确认）
    needs: deploy-dev
    environment: staging
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: build-output, path: dist/ }
      - run: ./deploy.sh staging

  deploy-production:                # 第三站：生产（严格审批 + 分支限制）
    needs: deploy-staging
    environment: production
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
        with: { name: build-output, path: dist/ }
      - run: ./deploy.sh production
```

### 5.2 条件选择环境

```yaml
jobs:
  deploy:
    # main 分支 → production，其他分支 → staging
    environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

### 5.3 手动触发指定环境

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: '目标环境'
        type: choice
        options: [dev, staging, production]

jobs:
  deploy:
    environment: ${{ github.event.inputs.environment }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "部署到 ${{ github.event.inputs.environment }}"
```

## 6. 部署状态记录与回滚

### 6.1 记录部署状态（Deployment API）

环境部署会在 GitHub 上产生**部署记录**（关联到具体提交与操作者），形成可审计的部署历史。可用社区 Action 标记部署起止状态：

```yaml
- name: Set deployment status
  uses: bobheadxi/deployments@v1
  id: deployment
  with:
    step: start
    token: ${{ secrets.GITHUB_TOKEN }}
    env: production

- name: Deploy
  run: ./deploy.sh

- name: Mark deployment success
  if: success()
  uses: bobheadxi/deployments@v1
  with:
    step: finish
    token: ${{ secrets.GITHUB_TOKEN }}
    status: success
    deployment_id: ${{ steps.deployment.outputs.deployment_id }}
    env_url: https://app.example.com
```

### 6.2 回滚策略

```yaml
jobs:
  rollback:
    runs-on: ubuntu-latest
    steps:
      - name: Get previous deployment SHA
        id: prev
        run: |
          PREV_SHA=$(gh api repos/${{ github.repository }}/deployments \
            --jq '[.[] | select(.environment == "production")] | .[1].sha')
          echo "sha=$PREV_SHA" >> $GITHUB_OUTPUT
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Rollback to previous version
        run: |
          git checkout ${{ steps.prev.outputs.sha }}
          ./deploy.sh production
```

## 7. 环境与并发控制

### 7.1 环境级并发（同一环境同时只允许一个部署）

```yaml
concurrency:
  group: deploy-${{ github.environment }}   # 按环境分组
  cancel-in-progress: false                 # 不取消正在进行的部署（排队等待）
```

### 7.2 分环境并发矩阵

```yaml
jobs:
  deploy:
    environment: ${{ matrix.env }}
    concurrency: deploy-${{ matrix.env }}
    strategy:
      matrix:
        env: [staging, production]
      fail-fast: false
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh ${{ matrix.env }}
```

## 8. 最佳实践

### 8.1 环境命名规范

```
dev / development       → 开发环境
test / testing          → 测试环境
staging / pre-prod      → 预发布环境
production / prod       → 生产环境
```

### 8.2 密钥管理

- 生产环境密钥只存在 production 环境中，仓库级不放生产凭据。
- 按最小权限原则配置密钥。
- 定期轮换密钥。
- 云厂商场景优先用 **OIDC** 替代长期密钥（无需存储 AK/SK）：

```yaml
# 使用 OIDC 连接 AWS（无需在仓库存储长期密钥）
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789:role/github-actions
    aws-region: us-east-1
```

### 8.3 审批强度建议

```
dev:         0 人（自动）
staging:     1 人（运维确认）
production:  2 人（运维 + 负责人双重确认）
```

### 8.4 安全边界认知

环境保护规则的意义不止于"流程规范"：**即使某个工作流被攻破（如恶意 Action、fork 的 pull_request_target），只要目标环境配置了必需审查者等规则，攻击者也无法在未通过门禁前触达环境密钥**。这是把生产凭据从仓库级下沉到环境级的核心收益。

## 9. 常见错误与对策

| 常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 环境密钥取不到 | job 中 secrets 为空 | job 未声明 `environment`，或保护规则未通过前无法访问环境密钥 | 在 job 中显式写 `environment: production`；确认保护规则已通过 |
| 部署 job 一直"等待" | job 卡在 pending/waiting | 环境配置了必需审查者，等待批准 | 审查者在 Actions 页面点击 Approve；或调整审查者配置 |
| 从非允许分支部署被拒 | job 失败或跳过 | 环境配置了部署分支限制 | 检查 Deployment branches 规则与通配符是否匹配当前分支 |
| 私有仓库无法配置环境 | 功能不可用 | 私有仓库需要 Pro/Team/Enterprise 计划 | 升级计划，或确认公共仓库场景 |
| 环境密钥与仓库密钥同名混淆 | 取到意外值 | 环境级密钥自动覆盖仓库级密钥 | 明确环境级优先规则，避免在仓库级存同名生产密钥 |
| 保护规则超过 6 条 | 无法启用更多 | 单环境最多同时启用 6 条保护规则 | 精简规则，把规则分散到多个环境 |
| 并发部署互相踩踏 | 两个部署同时改生产 | 未配置环境级并发 | 用 `concurrency.group` 按环境分组，`cancel-in-progress: false` |

## 11. 一句话记忆

**环境 = 部署旅程中的"考场分区"：job 声明 environment 才会进入对应站点，必须先过保护规则（审查者/等待计时器/分支限制）才能跑任务、读环境密钥；生产凭据只放在生产环境的保险柜里。**



<!-- ============ 文档分隔线：004-github/037-GitRepoInit.md ============ -->


## 开篇：像建房打地基一样初始化仓库

想象你要在空地上建一栋房子。第一步不是砌墙，而是**打地基**：把地面整平、浇筑混凝土，划定"这块地属于这栋房子"。地基打好了，后面的砌墙、封顶、装修才有依靠。

Git 仓库也是这样。你的项目文件（代码、文档）就是"房子"，而 `git init` 就是"打地基"——它在项目目录里悄悄埋下一个名叫 `.git` 的隐藏文件夹，告诉 Git："从这一刻起，这块目录归我管，之后所有的版本历史都存在这里。"

本篇文章就是一份**手把手操作向导**，带你走完从"一个普通文件夹"到"第一个提交诞生"的全过程。学完这一篇，你就拥有了"打地基 + 浇筑第一块楼板"的能力。

---

## 一、动手前的准备：安装与身份设置

### 1.1 检查 Git 是否安装

打开命令行（Windows 用 PowerShell 或 Git Bash，macOS/Linux 用终端），输入：

```bash
# 查看 Git 版本，验证是否安装成功
git --version
```

输出示例（版本号以你实际安装为准）：

```
git version 2.43.0.windows.1
```

如果提示"command not found"或"无法识别"，说明尚未安装 Git，请到官网下载安装包（见文末参考链接）。

### 1.2 设置提交身份（第一次必做）

Git 要求每一次提交（commit）都记录"谁做的"，这个身份由 `user.name` 和 `user.email` 两个配置决定。注意：**这不是 GitHub 登录账号，而是写在提交记录里的署名**。

```bash
# 全局配置（对这台电脑上的所有仓库生效，建议只配一次）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

配置说明：

| 配置命令 | 作用范围 | 存储位置 |
| --- | --- | --- |
| `git config --global ...` | 当前用户所有仓库 | 用户主目录下的 `~/.gitconfig` |
| `git config ...`（不带 --global） | 仅当前仓库 | 仓库内的 `.git/config` |

> 原理小贴士：`--global` 写在前面是"全局"，不写就是"局部"。局部配置会覆盖全局配置。如果跳过这一步直接提交，Git 会报错并要求你先配置身份，这是新手最常见的第一个拦路虎。

---

## 二、操作向导第一步：让普通目录变成仓库

### 2.1 进入你的项目目录

```bash
# 创建练习目录（示例路径，可自行修改）
mkdir my-first-project
cd my-first-project
```

### 2.2 初始化仓库：git init

```bash
# 在当前目录初始化 Git 仓库
git init
```

真实输出示例：

```
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, run:
hint:
hint:   git config --global init.defaultBranch main
Initialized empty Git repository in C:/Users/you/my-first-project/.git/
```

**这一步发生了什么？** 原理上，`git init` 只做三件事：

1. 创建 `.git` 隐藏文件夹——仓库的核心数据库（对象、引用、配置）都存在这里；
2. 建立默认分支（新版 Git 多为 `master`，也可指定 `main`）；
3. 准备暂存区（Index），等待第一个文件进入。

> 重要提醒：**永远不要手工修改或删除 `.git` 文件夹**，它一坏，整个仓库的版本历史就没了。

### 2.3 常用变体

```bash
# 方式一：初始化时直接指定目录（目录不存在会自动创建）
git init myproject

# 方式二：指定默认分支名为 main（与 GitHub 默认一致，团队常用）
git init -b main

# 方式三：初始化裸仓库（没有工作区的"纯数据库"，仅用于服务器端）
git init --bare project.git
```

三种变体对比：

| 命令 | 用途 | 适用场景 |
| --- | --- | --- |
| `git init` | 当前目录建仓库 | 本地新项目 |
| `git init -b main` | 建仓库且默认分支叫 main | 准备推送到 GitHub 的项目 |
| `git init --bare` | 裸仓库（无工作区） | 自建服务器、GitHub 内部存储原理 |

---

## 三、操作向导第二步：创建文件并查看状态

### 3.1 创建第一个文件

```bash
# 创建一个 README 文件（Windows 的 PowerShell 也支持 echo 写法）
echo "# 我的第一个项目" > README.md
```

### 3.2 查看仓库状态：git status

```bash
# 查看工作区和暂存区状态（养成随时查看的习惯）
git status
```

真实输出示例：

```
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

看懂输出：`Untracked files` 表示 README.md 是**未跟踪文件**——文件存在，但 Git 还没纳入管理。这正是"地基打好但砖还没码"的阶段。

### 3.3 简洁模式与细节模式

```bash
# 简洁输出（?? 表示未跟踪，A 表示已暂存，M 表示已修改）
git status -s

# 详细输出：附加文件差异内容
git status -v
```

---

## 四、操作向导第三步：把文件放入暂存区

### 4.1 添加文件：git add

```bash
# 将指定文件加入暂存区（暂存区 = 本次提交的"候选清单"）
git add README.md

# 查看状态确认（此时 README.md 前面出现 A）
git status -s
```

输出示例：

```
A  README.md
```

### 4.2 git add 的常见用法

```bash
# 添加当前目录下所有改动（最常用）
git add .

# 添加所有变化（新增、修改、删除都算，等价于 git add -A）
git add -A

# 只添加已跟踪文件的修改和删除（不含新文件）
git add -u

# 添加指定目录
git add src/components/

# 交互式选择部分改动加入暂存区（精细控制）
git add -p
```

### 4.3 文件移除与重命名

```bash
# 从工作区和暂存区同时移除文件
git rm oldfile.txt

# 仅从暂存区移除，但保留本地文件（例如不想把 .env 提交上去）
git rm --cached .env

# 递归移除整个目录
git rm -r olddir/

# 重命名文件并记录到暂存区
git mv old.txt new.txt

# 将文件移动到目录
git mv file.txt src/

# 把已暂存的文件撤出暂存区（内容不丢）
git restore --staged index.js
```

> 原理说明：`git add` 不是"上传文件"，而是把文件的**当前快照**写入暂存区（Index）。如果你 add 之后又修改了文件，下一次提交记录的是暂存区里的旧版本，必须重新 add。理解这一点，很多"我改了为什么没生效"的困惑就解开了。

---

## 五、操作向导第四步：完成首次提交

### 5.1 提交：git commit

```bash
# 提交暂存区内容，-m 后面跟提交说明
git commit -m "chore: 项目初始化，添加 README"
```

真实输出示例：

```
[master (root-commit) 7a3f9c1] chore: 项目初始化，添加 README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

看懂输出：`root-commit` 表示这是该仓库的**第一个提交**（没有父提交）；`7a3f9c1` 是提交 ID（SHA-1 哈希的前 7 位）；`1 file changed, 1 insertion(+)` 表示本次改动规模。

### 5.2 查看提交成果

```bash
# 确认提交成功
git status
# 输出应为：nothing to commit, working tree clean（工作区干净）

# 查看提交历史
git log --oneline
# 输出示例：7a3f9c1 (HEAD -> master) chore: 项目初始化，添加 README
```

### 5.3 其他初始化相关命令

```bash
# 查看仓库配置（确认身份已生效）
git config --list

# 删除仓库重新初始化（慎用！会清空 .git 中的所有历史）
# 在项目根目录执行：rm -rf .git  然后重新 git init
```

---

## 六、克隆远程仓库（另一种"拿地"方式）

除了从零 `git init`，更常见的做法是**克隆（clone）**——把 GitHub 上已有的仓库完整复制到本地，历史记录、分支、标签全都带过来。

```bash
# 克隆仓库到当前目录（自动生成同名文件夹）
git clone https://github.com/user/repo.git

# 克隆到指定目录名
git clone https://github.com/user/repo.git myapp

# 仅克隆指定分支
git clone -b develop https://github.com/user/repo.git

# 浅克隆：只取最近 1 次提交（适合大仓库，速度快）
git clone --depth 1 https://github.com/user/repo.git

# 浅克隆：只取最近 5 次提交
git clone --depth 5 https://github.com/user/repo.git

# SSH 方式克隆（需先配置 SSH 密钥，免输密码）
git clone git@github.com:user/repo.git
```

> 原理说明：`git clone` 内部做了三件事——下载仓库所有对象、建立默认分支并检出工作区、自动添加名为 `origin` 的远程仓库引用。所以克隆完成后直接 `git remote -v` 就能看到远程地址，不需要再手动配置。

---

## 七、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 命令找不到 | `fatal: not a git repository (or any of the parent directories): .git` | 当前目录不是 Git 仓库 | 确认已进入项目目录，先执行 `git init` |
| 身份未配置 | `Author identity unknown` / `Please tell me who you are` | 没设置 user.name 和 user.email | 执行 `git config --global user.name "名字"` 和 `git config --global user.email "邮箱"` |
| 提交时没内容 | `nothing added to commit but untracked files present` | 文件从未执行过 `git add` | 先 `git add <文件>` 或 `git add .` 再 commit |
| 改了文件却提交了旧版 | 提交内容与最新修改不一致 | add 之后再编辑，暂存区还是旧快照 | 修改后重新执行 `git add`，或改用 `git commit -am "说明"`（仅限已跟踪文件） |
| 误删 .git | 仓库历史全部丢失，无法回退 | 手工删除或移动了 .git 文件夹 | 无法恢复，只能重新 init；切记永远不动 .git |
| 克隆报认证失败 | `Authentication failed for 'https://github.com/...'` | HTTPS 克隆私有仓库需要凭证 | 使用 SSH 方式克隆，或配置 credential helper（见 043 篇） |

---

## 九、一句话记忆

**`git init` 是给项目打地基（生成 .git 数据库），`git add` 是把材料搬进候选区（暂存区），`git commit` 是浇下第一块楼板（生成首个快照）——地基打好，版本控制的大厦从此拔地而起。**



<!-- ============ 文档分隔线：004-github/038-GitCommitPush.md ============ -->


## 开篇：像盖章存档一样提交代码

想象你是单位的档案管理员。领导交给你一份重要文件，你要做三件事才能让它"正式生效"：

1. **核稿**：把文件放进"待盖章"的筐里（暂存区）；
2. **盖章存档**：盖上公章、登记日期，放进本地档案柜（本地仓库）；
3. **报送上级**：把档案复印件报送上级单位存档（远程仓库）。

这个过程环环相扣、缺一不可，而且顺序不能乱：还没核稿就盖章，是无效文件；只盖章不报送，上级单位永远不知道你有这份文件。

Git 的提交与推送，就是这套"档案管理流程"的数字化版本。本篇采用**流程驱动**的叙事方式，沿着"工作区 → 暂存区 → 本地仓库 → 远程仓库"这条流水线，把 `git add`、`git commit`、`git push` 三个动作一次讲透。

---

## 一、先建立全局认知：代码的"四站旅程"

在你动手敲命令之前，先记住这张流程图：

```
工作区(Working Tree)  --git add-->  暂存区(Index)  --git commit-->  本地仓库(Local Repo)  --git push-->  远程仓库(Remote Repo)
   改代码的地方              挑选本次要提交的内容          生成正式版本快照            同步到 GitHub
```

每一站的职责：

| 站点 | 对应命令 | 类比 | 关键特点 |
| --- | --- | --- | --- |
| 工作区 | 编辑文件 | 写草稿 | 改动最多，随时可丢弃 |
| 暂存区 | `git add` | 待盖章的筐 | 挑选哪些改动进入本次提交 |
| 本地仓库 | `git commit` | 盖章存档 | 每次提交生成永久快照 |
| 远程仓库 | `git push` | 报送上级 | 团队共享的"官方档案" |

> 原理提示：`git commit` 生成的不是"补丁"，而是**完整快照**（Snapshot）。Git 会为提交时所有文件的内容建立索引并算出一个 SHA-1 哈希作为提交 ID。这也是为什么 Git 回退任何版本都能 100% 还原——每个版本都存了全套文件。

---

## 二、流程第一站：工作区改动

```bash
# 先确认你在哪个分支、工作区是否干净
git status
# 输出：On branch main / nothing to commit, working tree clean

# 修改或新建文件（示例）
echo "def add(a, b): return a + b" > calc.py
```

此时 `calc.py` 是"未跟踪"（Untracked）状态，用 `git status -s` 可以看到 `?? calc.py`。它还没有进入流程。

---

## 三、流程第二站：git add——把改动放入暂存区

### 3.1 基本用法

```bash
# 把单个文件加入暂存区
git add calc.py

# 把当前目录所有改动加入暂存区（最常用，但注意会包含所有新文件）
git add .

# 只看已跟踪文件的修改和删除（不含新文件，适合"只提交改过的"）
git add -u

# 交互式选择部分片段（精细控制，适合大改动拆小提交）
git add -p
```

### 3.2 验证暂存结果

```bash
# 暂存后状态检查（A 表示 Added，M 表示 Modified，左列是暂存区状态）
git status -s
```

输出示例：

```
A  calc.py
M  README.md
```

### 3.3 撤销暂存（反悔按钮）

```bash
# 把文件从暂存区移回工作区（内容不丢）
git restore --staged calc.py

# 旧写法（等效）
git reset HEAD calc.py
```

---

## 四、流程第三站：git commit——盖章存档

### 4.1 提交暂存区内容

```bash
# -m 后跟提交说明（必须有，否则会打开编辑器）
git commit -m "feat: 添加加法函数"
```

真实输出示例：

```
[main 8f4b2c1] feat: 添加加法函数
 1 file changed, 1 insertion(+)
 create mode 100644 calc.py
```

看懂输出：`main` 是分支名，`8f4b2c1` 是提交 ID 前 7 位，`1 file changed, 1 insertion(+)` 是改动统计。

### 4.2 常用提交方式

```bash
# 方式一：跳过 add，直接提交所有已跟踪文件的改动（新文件不包含）
git commit -am "fix: 修复样式问题"

# 方式二：多行提交信息（标题 + 描述）
git commit -m "feat: 添加搜索功能" -m "支持按关键词和日期范围搜索"

# 方式三：打开默认编辑器写详细提交信息
git commit
```

### 4.3 提交信息规范（Conventional Commits）

规范的提交信息让历史可读、可检索，团队必备：

```bash
# feat：新功能
git commit -m "feat: 添加购物车功能"

# fix：Bug 修复
git commit -m "fix: 修复登录页面崩溃问题"

# 带作用域（指出改的是哪个模块）
git commit -m "feat(auth): 添加 OAuth 登录"

# 破坏性变更（BREAKING CHANGE 必须大写）
git commit -m "feat: 重构 API 接口" -m "BREAKING CHANGE: 响应格式改为 JSON"
```

| 前缀 | 含义 | 示例 |
| --- | --- | --- |
| `feat:` | 新功能 | `feat: 添加支付页面` |
| `fix:` | 修复 Bug | `fix: 修复空指针异常` |
| `docs:` | 文档变更 | `docs: 更新使用说明` |
| `style:` | 格式调整（不影响逻辑） | `style: 统一缩进` |
| `refactor:` | 重构（不改功能） | `refactor: 抽取公共方法` |
| `chore:` | 杂务（构建、配置） | `chore: 升级依赖版本` |

### 4.4 修改上次提交（amend 后悔药）

```bash
# 修改最近一次提交的信息
git commit --amend -m "feat: 添加用户注册功能"

# 把漏掉的文件追加进上次提交（不修改信息）
git add forgotten.js
git commit --amend --no-edit

# 修改上次提交的作者信息（少用）
git commit --amend --author="张三 <zhangsan@example.com>"
```

> 原理与警告：`--amend` 不是"修改"旧提交，而是**生成一个新提交替换它**（提交 ID 会变）。因此，**amend 只适合本地还没 push 的提交**；如果已经 push 到远程且别人可能已经拉取，就不要再 amend，否则会造成历史分叉。

---

## 五、流程第四站：git push——报送远程

### 5.1 首次推送：建立追踪关系

```bash
# -u 是 --set-upstream 的简写：推送的同时记录"本地分支 跟踪 远程分支"
git push -u origin main
```

输出示例：

```
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 222 bytes | 222.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), reused 0 (delta 0)
To https://github.com/yourname/my-repo.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

看懂输出：最后一行 `branch 'main' set up to track 'origin/main'` 表示追踪关系已建立。**以后在这个分支上直接 `git push` 即可**，不用再写远程名和分支名。

### 5.2 日常推送

```bash
# 推送当前分支（需已建立追踪关系）
git push

# 推送指定分支
git push origin main

# 推送所有本地分支
git push --all origin

# 删除远程分支（推送"删除指令"）
git push origin --delete old-feature

# 推送标签
git push origin v1.0.0

# 推送所有本地标签
git push origin --tags
```

### 5.3 推送被拒绝怎么办

当远程分支有你本地没有的提交时，`git push` 会拒绝并提示 `non-fast-forward`。这是**保护机制**，不是故障。正确处理流程：

```bash
# 1. 先拉取远程更新（把远程的新提交合并到本地）
git pull

# 2. 解决可能出现的冲突（见 041 篇）
# 3. 再推送
git push
```

### 5.4 强制推送：谨慎使用

```bash
# 推荐方式：--force-with-lease（仅在远程没有被别人更新的前提下才覆盖）
git push --force-with-lease origin feature/login

# 危险方式：-f 无脑覆盖远程（可能覆盖别人的提交，团队协作严禁使用）
git push -f origin feature/login
```

> 安全原则：**永远不要对共享分支（main/master）使用强制推送**。`--force-with-lease` 相比 `-f` 多了一道"远程是否被他人更新"的检查，是个人分支上相对安全的选择。

---

## 六、提交后复盘：查看历史

```bash
# 查看完整提交历史
git log

# 每条提交一行（最常用的历史视图）
git log --oneline

# 图形化展示所有分支的提交历史
git log --oneline --graph --all

# 只看最近 5 条
git log -5

# 按作者筛选
git log --author="zhangsan"

# 按日期范围筛选
git log --since="2026-01-01" --until="2026-07-31"
```

---

## 七、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 提交时提示没有内容 | `nothing to commit, working tree clean` | 忘了 `git add`，或提交前改动已丢失 | 先 `git add` 再 commit；确认确实有改动 |
| commit 卡在编辑器里 | 执行 `git commit` 后弹出 vim 等编辑器 | 没带 `-m` 参数，Git 打开编辑器等输入 | 输入信息后保存退出（vim 按 `i` 输入、`Esc` 后 `:wq` 保存）；或以后都用 `git commit -m "..."` |
| push 被拒绝 | `! [rejected] main -> main (non-fast-forward)` | 远程有你本地没有的提交 | 先 `git pull` 合并远程更新，再 push |
| push 要求认证 | `Authentication failed` / `Username for 'https://github.com'` | 凭证缺失或过期 | 配置 credential helper，或改用 SSH 方式（见 043、004 篇） |
| 提交信息写得没意义 | 历史中全是 "update" "fix" | 没有遵循提交规范 | 使用 Conventional Commits 前缀（feat/fix/docs 等），见上文 4.3 节 |
| amend 后 push 失败 | `! [rejected] ... (non-fast-forward)` | 已推送的提交被 amend，本地历史与远程分叉 | 只在推送前使用 amend；若已推送，与团队确认后用 `--force-with-lease` |
| push 卡住无响应 | 长时间无输出 | 网络问题或代理未配置 | 检查网络；配置代理后重试 |

---

## 九、一句话记忆

**四站旅程一句话记牢：`git add` 把改动放进暂存区，`git commit` 盖章生成版本快照，`git push -u` 首次推送并建立追踪，此后 `git push` 直达远程——顺序不能乱，反悔用 amend，拒绝先 pull。**



<!-- ============ 文档分隔线：004-github/039-GitPullFetch.md ============ -->


## 开篇：像收发室取件一样拉取更新

想象你所在的小区有个收发室，快递员把新包裹送到收发室后，会发短信通知你。这时你有两种取件方式：

- **方式 A（先看一眼再决定）**：到收发室看到包裹的**面单信息**（谁寄的、什么时候到的），不着急拆开，先回家想想这份快递要不要、怎么处理，想清楚了再拆；
- **方式 B（直接拆开用）**：到了收发室直接拆包，把东西用起来——如果里面的东西和你家里的旧家具摆放冲突，就得现场重新摆放。

对应到 Git：

- **`git fetch`（方式 A）**：只把远程仓库的**新提交信息**下载到本地（更新 `origin/main` 这类"远程跟踪分支"），**你的工作区代码完全不动**，可以慢慢看、对比、确认后再决定要不要合并；
- **`git pull`（方式 B）**：`fetch` 完**自动执行合并**（默认是 merge），直接把远程更新并进你的当前分支，一步到位，但也可能当场触发冲突。

官方文档说得更直白：**`git pull` 本质就是 `git fetch` 加 `git merge` 的简写**。本篇采用**对比驱动**的叙事方式，把这两个命令放在同一张桌子上逐项对照，让你彻底分清"什么时候用 fetch、什么时候用 pull"。

---

## 一、先看结论：一张表分清 fetch 与 pull

| 对比维度 | `git fetch` | `git pull` |
| --- | --- | --- |
| 本质 | 只下载远程新提交，更新远程跟踪分支 | `git fetch` + 自动合并（merge 或 rebase） |
| 是否修改工作区 | 不修改，本地代码纹丝不动 | 立即合并进当前分支，可能改动代码 |
| 是否可能冲突 | 不会（不合并） | 可能触发合并冲突 |
| 安全性 | 高，完全可控 | 中，自动合并有风险 |
| 典型场景 | 先看远程改了什么再决定 | 快速同步最新代码 |
| 命令组合 | fetch 后手动 `git merge origin/main` | 一步完成 |

一句话记忆版：**fetch 是"只看不拆"，pull 是"拆了就用"**。

---

## 二、原理讲解：远程跟踪分支是什么

要理解 fetch 和 pull，必须先搞懂"远程跟踪分支"（remote-tracking branch）。它的原理可以这样理解：

Git 在本地仓库里为远程的每个分支保存了一个**"分身"**，命名规则是 `远程名/分支名`，例如 `origin/main`。这个分身记录的是"**我上次从远程同步时，远程分支长什么样**"。它只是一个引用（指针），不是你工作区里的真实文件。

```bash
# 查看远程跟踪分支（克隆后自动生成）
git branch -r
# 输出示例：
#   origin/HEAD -> origin/main
#   origin/main

# 查看本地 + 远程全部分支
git branch -a
```

`git fetch` 干的事就是：**把这个分身更新到远程的最新状态**——`origin/main` 指向最新的提交，但你的本地分支 `main` 和工作区文件保持不变。

图解（fetch 前后）：

```
fetch 前：                     fetch 后：
本地 main --- A --- B          本地 main --- A --- B
远程 origin/main --- A         远程 origin/main --- A --- B --- C   (C 是远程新增)
工作区文件：仍是 A/B 版本        工作区文件：仍是 A/B 版本（没变！）
```

只有你手动执行 `git merge origin/main` 或 `git pull`，本地分支和工作区才会前进到 C。

---

## 三、git fetch 全解

### 3.1 基本用法

```bash
# 获取默认远程（origin）所有分支的更新（只更新分身，不合并）
git fetch

# 获取指定远程的更新
git fetch origin

# 获取指定远程的指定分支
git fetch origin main

# 获取所有远程仓库的更新
git fetch --all

# 获取更新并清理远程已删除分支的本地引用
git fetch --prune

# 获取指定标签
git fetch origin v1.0.0

# 获取所有标签
git fetch --tags
```

### 3.2 fetch 之后能做什么

fetch 的完整价值在于"先侦查，后决策"：

```bash
# 1. 查看远程 main 比你本地多哪些提交
git log --oneline main..origin/main

# 2. 对比本地与远程的差异
git diff origin/main

# 3. 确认无误后，手动合并（这才是真正把更新并进来）
git merge origin/main

# 4. 或者用 rebase 方式整合（历史更线性）
git rebase origin/main
```

### 3.3 典型输出解读

```bash
git fetch origin
```

输出示例：

```
From https://github.com/user/repo
 * [new branch]      feature/login -> origin/feature/login
   8f4b2c1..c9d3e7a  main         -> origin/main
```

看懂输出：第一行表示远程出现了新分支；第二行表示 `main` 从 `8f4b2c1` 推进到 `c9d3e7a`。**注意：你的本地 main 和工作区没有任何变化**。

---

## 四、git pull 全解

### 4.1 基本用法

```bash
# 拉取并合并（默认 merge 方式）：fetch + merge
git pull

# 指定远程和分支
git pull origin main

# 拉取并使用 rebase 方式整合（避免多余的合并提交）
git pull --rebase

# 指定分支 + rebase
git pull --rebase origin main
```

### 4.2 默认合并 vs --rebase

同样是 `git pull`，内部可以选择两种整合策略：

```bash
# 默认：merge（生成一个合并提交，历史会出现分叉）
git pull

# 推荐给个人分支：--rebase（把本地提交"垫到"远程提交之后，历史呈直线）
git pull --rebase
```

两条路线的区别与取舍，在 040-GitMergeRebase 篇有详细对比，这里只需记住：**团队要求历史整洁就用 `git pull --rebase`，想保留完整合并记录就用默认 `git pull`**。也可以在配置里一劳永逸：

```bash
# 全局设置 pull 默认使用 rebase
git config --global pull.rebase true
```

### 4.3 特殊参数

```bash
# 允许合并不相关历史（例如：本地 init 的仓库首次和远程仓库合并时）
git pull origin main --allow-unrelated-histories

# 拉取但不自动创建合并提交（先检查再自己提交）
git pull --no-commit
```

> 场景说明：如果你在本地 `git init` 建了仓库并提交过，再 `git remote add origin` 关联远程，此时本地与远程没有任何共同祖先，直接 `git pull` 会报 `refusing to merge unrelated histories`。加上 `--allow-unrelated-histories` 才能强行合并。

---

## 五、拉取冲突处理（提前预告）

`git pull` 合并时若双方改了同一处代码，就会停下等你解决。完整解法见 041 篇，这里先给出"止血三板斧"：

```bash
# 合并冲突：中止（回到 pull 之前的状态）
git merge --abort

# 变基冲突：中止
git rebase --abort

# 解决完冲突后：继续合并
git merge --continue

# 解决完冲突后：继续变基
git rebase --continue

# 变基时跳过当前有问题的提交
git rebase --skip
```

---

## 六、远程分支操作补充

```bash
# 查看远程分支及其追踪关系
git branch -vv
# 输出示例：* main 8f4b2c1 [origin/main] feat: 添加加法函数

# 基于远程分支创建本地分支并切换
git switch -c feature origin/feature

# 本地分支自动追踪同名远程分支（远程存在时才有效）
git switch feature

# 查看远程仓库详情（含分支、落后/领先状态）
git remote show origin

# 列出远程仓库的所有引用
git ls-remote origin

# 查看远程默认分支名
git remote show origin | grep "HEAD branch"
```

---

## 七、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 工作区有未提交改动时 pull | `Your local changes to the following files would be overwritten by merge` | 本地未提交改动与远程更新重叠 | 先 `git stash` 暂存改动，pull 后再 `git stash pop` 恢复（见 045 篇） |
| pull 报不相关历史 | `refusing to merge unrelated histories` | 本地 init 仓库与远程仓库没有共同祖先 | 加 `--allow-unrelated-histories`（首次合并时用） |
| pull 后出现冲突标记 | `Automatic merge failed; fix conflicts and then commit the result` | 双方修改了同一处代码 | 按 041 篇解决：编辑文件 → `git add` → `git merge --continue` |
| 误以为 fetch 后代码更新了 | fetch 后本地代码没变化 | 对 fetch 的认知偏差——它只更新 origin/main 分身 | 主动执行 `git merge origin/main` 或改用 `git pull` |
| pull --rebase 冲突后不会收场 | 变基进行中，不知道下一步 | 没掌握 continue/abort/skip | 解决冲突后 `git add` + `git rebase --continue`；想放弃就 `git rebase --abort` |
| 远程分支列表有"幽灵分支" | `git branch -r` 里出现远程已删除的分支 | 远程分支被删，但本地引用未清理 | `git fetch --prune` 或 `git remote prune origin` |
| 拉取慢/卡住 | fetch/pull 长时间无响应 | 大仓库全量下载或网络受限 | 用 `git fetch --depth 1` 浅获取，或检查网络代理 |

---

## 九、一句话记忆

**`git fetch` 只更新远程"分身"（origin/main）不碰你的代码，`git pull` 是 fetch 加 merge（或 rebase）一步到位——先侦查用 fetch，快同步用 pull，冲突了记得 abort 或 continue。**



<!-- ============ 文档分隔线：004-github/040-GitMergeRebase.md ============ -->


## 开篇：像双人写作合并一样整合分支

假设你和同事合写一本书：你负责"第 1-3 章"，他负责"第 4-6 章"。你俩在各自的文档副本上写作，最后要把两份稿子合成一本完整的书。此时有两条路线：

- **路线一（merge，合并）**：把两份稿子**原样装订在一起**，加上一个"合并页"记录"本书由两份稿件合成"。书的正文里，你的章节和同事的章节**完整保留各自历史**，合订本能清楚看到每个章节各自的发展过程，缺点是目录结构有分叉，读起来略乱。
- **路线二（rebase，变基）**：把同事写完的第 4-6 章作为"基准"，把你的第 1-3 章**拆散重写**，按顺序重新誊抄到基准之上。最终书稿是一份**连续、直线**的完整稿子，历史干净，但你的原始草稿（原提交）被"重写"了——誊抄稿和原稿不是同一份。

对应到 Git：**`git merge` 保留双方完整历史并生成合并提交；`git rebase` 把你的提交"重放"到对方最新提交之后，历史呈一条直线**。本篇采用**对比驱动**方式，把这两条路线掰开揉碎，讲清原理、场景和选择原则。

---

## 一、先看结论：merge 与 rebase 速览表

| 对比维度 | `git merge` | `git rebase` |
| --- | --- | --- |
| 本质 | 三方合并，生成合并提交 | 提取提交补丁，在目标基底上重放 |
| 历史形态 | 有分叉（能看到分支合并痕迹） | 直线（历史整洁） |
| 是否改写已有提交 | 否，原提交不变 | 是，生成全新提交（ID 改变） |
| 对共享分支的风险 | 无，安全 | 高，禁止对已推送的共享分支使用 |
| 可追溯性 | 强，合并提交记录两个父提交 | 较弱，分支独立开发过程被抹平 |
| 适用场景 | 长期分支、公共分支、保留合并记录 | 个人功能分支、push 前整理历史 |
| 命令形态 | `git merge <分支>` | `git rebase <基底>` |

官方结论（Pro Git）：**两种方式整合的最终代码快照完全一样，区别只在提交历史**。变基让历史更整洁，合并让历史更完整。

---

## 二、原理讲解：从"共同祖先"说起

### 2.1 分支为什么会分叉

Git 的分支本质上是一个**指向提交的可移动指针**。当两个分支从同一个提交（共同祖先）各自前进时，历史就分叉了：

```
A --- B --- C   (main)
       \
        D --- E   (feature)
```

### 2.2 merge 的三方合并原理

`git merge feature`（在 main 上执行）时，Git 取三个点做三方合并：

1. **我方**（ours）：当前分支 main 的最新提交 C；
2. **对方**（theirs）：要合并进来的分支 feature 的最新提交 E；
3. **共同祖先**（base）：两个分支最近共同祖先 B。

Git 逐文件比较三个版本：只有一方改的，自动采用；双方改了同一处且不一致的，标记为冲突等你裁决。合并成功后生成**合并提交 M**（有两个父提交），历史变成：

```
A --- B --- C --- M   (main)
       \         /
        D --- E   (feature)
```

### 2.3 快进合并（fast-forward）的特殊情况

如果被合并的分支是当前分支的**直接后代**（没分叉），Git 不需要创建合并提交，直接把指针往前移即可：

```bash
# 前提：main 在 B，feature 在 C，且 C 直接继承 B
git merge feature
# 输出：Updating a1b2c3d..e4f5g6h (Fast-forward)
```

### 2.4 rebase 的"重放"原理

`git rebase main`（在 feature 上执行）分四步走（官方文档描述）：

1. **找分叉点**：定位 feature 与 main 的共同祖先 B；
2. **提取补丁**：把 feature 自 B 以来的提交（D、E）的修改内容存为临时补丁；
3. **移动基底**：把 feature 指针指向 main 的最新提交 C；
4. **依次重放**：把补丁按原顺序应用到 C 之上，生成新提交 D'、E'。

结果：

```
A --- B --- C           (main)
             \
              D' --- E'   (feature)
```

> 关键区别再强调：merge 后 D、E 原封不动；rebase 后 D'、E' 是**全新的提交**（哈希 ID 变了，作者信息保留）。所以 rebase 等于"重写了自己这一侧的历史"。

---

## 三、git merge 命令全解

### 3.1 基本用法

```bash
# 把 feature 分支合并到当前分支
git switch main
git merge feature

# 强制创建合并提交（即使可以快进也创建一个，保留"分支曾存在"的记录）
git merge --no-ff feature

# 仅当可以快进时才合并，否则报错退出（适合不想产生合并提交的场景）
git merge --ff-only feature

# 压缩合并：把 feature 的所有提交压成一个改动，暂存到暂存区（需再 commit）
git merge --squash feature
git commit -m "feat: 用户登录功能"

# 合并时打开编辑器修改合并信息
git merge -e feature
```

### 3.2 合并输出示例

```bash
git merge feature
```

输出示例：

```
Merge made by the 'ort' strategy.
 app.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
```

### 3.3 合并后清理

```bash
# 删除已合并的本地分支（-d 只允许删除已合并的分支，安全）
git branch -d feature

# 删除远程分支
git push origin --delete feature

# 查看已合并到 main 的分支（可用于批量清理）
git branch --merged main

# 查看尚未合并的分支（-d 会拒绝删除它们）
git branch --no-merged
```

### 3.4 cherry-pick：只摘取某个提交

不是整条分支合并，而是只把某一个提交"移植"过来：

```bash
# 把指定提交应用到当前分支
git cherry-pick abc1234

# 一次移植多个提交
git cherry-pick abc1234 def5678

# 遇到冲突时：解决后继续
git cherry-pick --continue

# 放弃整个 cherry-pick
git cherry-pick --abort
```

---

## 四、git rebase 命令全解

### 4.1 基本用法

```bash
# 把当前分支变基到 main 之上
git switch feature
git rebase main

# 简写形式：直接指定分支（等价于 switch + rebase）
git rebase main feature

# 把当前分支变基到远程分支
git rebase origin/main

# 变基时保留空提交
git rebase --keep-empty main
```

### 4.2 变基冲突处理三板斧

```bash
# 解决冲突后继续
git rebase --continue

# 跳过当前有问题的提交
git rebase --skip

# 中止变基，回到变基前状态
git rebase --abort
```

### 4.3 交互式变基：整理自己的历史

`git rebase -i` 是重写本地历史的利器，常用于 push 前把多个零碎提交合并成一个清晰提交：

```bash
# 交互式整理最近 5 次提交
git rebase -i HEAD~5

# 从指定提交开始整理
git rebase -i abc1234
```

执行后会打开编辑器，列出待办清单，常用命令：

```
pick abc1234 添加登录功能
reword def5678 修改提交说明
squash e9f0123 修复样式       # 合并到上一个提交，并合并说明
fixup f1a2b3c 小修复          # 合并到上一个提交，丢弃说明
drop g4h5i6j 废弃的实验代码    # 删除该提交
edit 7k8l9m0 需要暂停修改      # 在该提交处暂停
```

> 使用原则：交互式变基**只允许用于还没推送到共享远程的本地提交**。已 push 的提交被改写，会让拉取过它的队友陷入历史冲突。

### 4.4 常用变体

```bash
# --onto：把 A 分支上基于 X 的提交，改放到 Y 之上
git rebase --onto main server client

# 编辑变基待办列表（进行中时用）
git rebase --edit-todo

# 查看当前变基正在应用的补丁
git rebase --show-current-patch
```

---

## 五、merge vs rebase：怎么选

| 场景 | 推荐 | 理由 |
| --- | --- | --- |
| main 合并功能分支（发布） | `git merge --no-ff` | 保留"功能曾独立开发"的合并记录 |
| 个人功能分支同步 main | `git rebase main` | 历史整洁，push 前顺手整理 |
| 多人协作的共享分支同步 | `git merge` | 不改写他人可能已拉取的提交 |
| PR 合并到 main | GitHub 默认 Squash 或 Merge | 平台内配置，避免本地操作 |
| 本地提交太碎想合并 | `git rebase -i` | 交互式压缩提交 |
| 只想要别人的某一个提交 | `git cherry-pick` | 精准移植 |

**黄金原则（Pro Git 原话）**：**不要对已推送到远程、且可能被别人拉取的提交执行 rebase**。变基是"重写历史"，只能用于自己还没共享的提交。

---

## 六、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| merge 想快进却被拒绝 | `fatal: Not possible to fast-forward, aborting.` | 用了 `--ff-only` 但两分支已分叉 | 去掉 `--ff-only`，接受普通三方合并 |
| rebase 后 push 被拒 | `! [rejected] feature -> feature (non-fast-forward)` | 改写历史后与远程分叉 | 个人分支可用 `--force-with-lease`；共享分支禁止 |
| merge 出现冲突 | `Automatic merge failed; fix conflicts...` | 双方改同一处 | 按 041 篇解决：编辑 → `git add` → `git merge --continue` |
| rebase 到一半想反悔 | 变基进行中 | 不知道可以中止 | `git rebase --abort` 一键回到起点 |
| 删分支被拒 | `error: The branch 'feature' is not fully merged` | `git branch -d` 只删已合并分支 | 确认内容不要后改用 `git branch -D` 强删 |
| 交互式变基里填错命令 | 编辑器里看到 `pick` 等命令不知道干嘛 | 不熟悉 rebase -i 指令 | 查阅 4.3 节命令表；`drop` 删提交、`squash` 合并、`reword` 改信息 |
| 对已推送提交 amend/rebase | 队友拉取后历史混乱 | 改写公共历史 | 只重写未推送提交；已推送的用新提交修正（如 revert） |

---

## 八、一句话记忆

**merge 保留双方历史、生成合并提交（安全、适合共享分支）；rebase 把提交重放成直线（整洁、只用于未推送的本地提交）——快进是特权，公共历史禁改写，push 前整理用 rebase -i。**



<!-- ============ 文档分隔线：004-github/041-GitConflictResolve.md ============ -->


## 开篇：冲突了怎么办——先别慌

想象这样一个场景：你和同事在同一张纸上写会议纪要。你在第 3 行写上"预算 5 万元"，同事也在第 3 行写上"预算 8 万元"。最后要把两份纪要合成一份，尴尬的时刻来了——**第 3 行到底听谁的？**

你把两份纪要交给主管，主管也拿不定主意，只能把两份内容都标出来，请你们两个当事人当面说清楚。

Git 遇到的情况一模一样：当两个分支**修改了同一文件的同一处内容，且修改不一致**时，Git 无法替你决定保留哪一份，于是它停下来，在文件里插入"争论标记"，把决定权交还给你。这就是**冲突（Conflict）**。

本篇采用**问题驱动**的叙事方式，从"遇到冲突的恐慌"切入，依次回答四个问题：**冲突从哪来？冲突长什么样？怎么解决？怎么预防？** 学完这一篇，你会把冲突从"灾难现场"变成"日常工作"。

---

## 一、原理讲解：冲突从哪来

### 1.1 冲突的唯一来源：三方合并

回顾 040 篇的三方合并机制：合并时 Git 比较三个版本——我方（ours）、对方（theirs）、共同祖先（base）。冲突的产生规则只有一条：

| 比较结果 | Git 的处理 |
| --- | --- |
| 只有一方改了某处 | 自动采用，无冲突 |
| 双方改了不同的地方 | 自动合并，无冲突 |
| 双方改了**同一处**且内容**不一致** | **冲突**，停下等人裁决 |

注意：**"同一处"** 是关键。你和同事一个改第 3 行、一个改第 30 行，Git 能自动合并；只有两人都改了第 3 行还改得不一样，才会冲突。

### 1.2 什么操作会触发冲突

```bash
# 最常见的触发场景
git merge feature        # 合并冲突
git pull                 # 拉取远程更新时的合并冲突（本质也是 merge）
git pull --rebase        # 变基冲突
git cherry-pick abc1234  # 移植提交冲突
git stash pop            # 恢复暂存冲突（见 045 篇）
```

### 1.3 冲突发生时的现象

执行合并命令后，终端会出现类似提示：

```
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

同时 `git status` 会把冲突文件标记出来：

```
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   app.py
```

> 原理提示：冲突发生时，Git 进入"合并中"（MERGING）状态，此时**不要慌、不要乱敲命令**。你只有三个选择：解决并继续（continue）、放弃合并（abort）、或用工具辅助。Git 也贴心地生成了 `.git/MERGE_HEAD` 等临时状态文件，`git merge --abort` 就是靠它们还原现场的。

---

## 二、冲突长什么样：解读冲突标记

用编辑器打开冲突文件，你会看到 Git 插入的三段式标记：

```
<<<<<<< HEAD
当前分支（我方）的代码
=======
feature/login 分支（对方）的代码
>>>>>>> feature/login
```

标记含义逐行拆解：

| 标记 | 含义 |
| --- | --- |
| `<<<<<<< HEAD` | 冲突区域开始，下方是**当前分支**（我方）的内容 |
| `=======` | 分界线：上面是我方，下面是对方 |
| `>>>>>>> feature/login` | 冲突区域结束，标注对方分支名（或提交 ID） |

示例（一个真实的冲突文件）：

```python
def get_discount(price):
<<<<<<< HEAD
    return price * 0.9        # 我方：打九折
=======
    return price * 0.8        # 对方：打八折
>>>>>>> feature/login
```

### 2.1 快速查看冲突文件清单

```bash
# 仅列出有冲突的文件名
git diff --name-only --diff-filter=U

# 查看冲突的具体内容（带标记）
git diff

# 查看冲突文件在各自版本中的内容
git show HEAD:app.py         # 我方版本
git show feature/login:app.py  # 对方版本
```

---

## 三、怎么解决：完整流程四步走

冲突解决的标准流程是：**找文件 → 改内容 → 标记解决 → 收尾提交**。

### 3.1 第一步：定位冲突文件

```bash
git status
# 找到 both modified 的文件，就是需要处理的
```

### 3.2 第二步：手动编辑，做出裁决

打开冲突文件，做三件事：

1. 删除冲突标记行（`<<<<<<<`、`=======`、`>>>>>>>`）；
2. 决定保留哪份内容——我方、对方、或融合两者（三者均可）；
3. 确保文件语法正确、逻辑完整。

保留技巧：

```bash
# 想直接保留当前分支（我方）的版本
git checkout --ours app.py

# 想直接保留对方分支的版本
git checkout --theirs app.py

# 注意：checkout --ours/--theirs 只对冲突文件生效，且会覆盖整个文件
```

### 3.3 第三步：告诉 Git"这个冲突解决了"

```bash
# 编辑完成后，git add 即表示该文件冲突已解决
git add app.py
```

### 3.4 第四步：按操作类型收尾

```bash
# 如果是在 merge / pull 中：完成合并提交
git commit -m "merge: 合并 feature/login 分支"

# 或用默认合并信息（Git 自动生成）
git commit --no-edit

# 如果是在 rebase 中：继续变基
git rebase --continue

# 如果是在 cherry-pick 中：继续
git cherry-pick --continue
```

### 3.5 图形化工具辅助

```bash
# 用 VS Code 打开冲突文件（界面会提供 Accept Current/Incoming 按钮）
code app.py

# 启动配置好的图形化合并工具
git mergetool

# 指定具体工具
git mergetool --tool=vimdiff
```

---

## 四、想反悔：中止操作

解决到一半觉得太乱？Git 允许一键回到操作前状态：

```bash
# 中止合并（回到 merge 之前）
git merge --abort

# 中止变基
git rebase --abort

# 中止 cherry-pick
git cherry-pick --abort
```

> 注意：`--abort` 会丢弃本次合并带来的所有改动（包括你已做的冲突编辑）。要谨慎使用；不过它至少不会动你已经提交过的历史。

---

## 五、怎么预防：让冲突少发生

冲突无法 100% 避免，但可以大幅减少：

```bash
# 1. 拉取前先把本地改动收好（避免"工作区脏"导致的额外麻烦）
git stash && git pull && git stash pop

# 2. 用 rebase 方式拉取，减少多余的合并提交
git pull --rebase

# 3. 定期同步主分支：先看远程变化，再变基自己的分支
git fetch origin
git rebase origin/main

# 4. 合并前先看两分支差异，评估冲突风险
git diff main...feature

# 5. 查看两分支的共同祖先（分叉点）
git merge-base main feature
```

日常预防习惯（比命令更重要）：

- **小步提交、勤同步**：改动越小越少，冲突面就越小；
- **分工明确**：尽量避免多人同时改同一文件同一区域；
- **配置文件谨慎改**：如 `package.json`、`.env.example` 这类高频文件最容易冲突；
- **提交前先 pull**：这是团队协作的第一铁律。

---

## 六、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 冲突后直接乱提交 | 提交信息里残留 `<<<<<<<` 标记 | 忘记删除冲突标记就 commit | 搜索并删除所有 `<<<<<<<`、`=======`、`>>>>>>>` 行再 add+commit |
| add 了文件但仍提示冲突未解决 | `you have unmerged paths` | 还有别的冲突文件没处理 | `git status` 检查所有 `both modified` 文件，逐一处理 |
| 不知道怎么退出冲突状态 | 执行任何命令都提示合并中 | 停在 MERGING/Rebasing 状态 | 走完收尾流程（commit / rebase --continue），或 `--abort` 放弃 |
| 误用 --abort 丢失编辑 | 冲突解决到一半，abort 后改动全没了 | 理解偏差——abort 是放弃不是保存 | 想保留处理结果就继续走 add+commit；abort 前确认放弃 |
| checkout --ours 不生效 | 文件内容没变成我方的 | 该文件不是冲突文件，或拼写错误 | 先 `git status` 确认文件确实处于 unmerged 状态 |
| 冲突后 push 被拒 | `non-fast-forward` | 只解决完没 commit，或没重新 add | 走完 3.4 节收尾：add → commit（或 continue）→ push |
| 解决冲突时误删对方代码 | 功能上线后缺失对方的功能 | 裁决时只留了自己那份 | 融合双方内容，而不是简单二选一；重大合并建议先讨论 |

---

## 八、一句话记忆

**冲突 = 双方改了同一处且不一致，Git 交回裁决权——看标记（<<<<<<< 我方 / ======= 对方 / >>>>>>>），编辑裁决，add 标记已解决，merge --continue 或 commit 收尾；不想玩了就 --abort，想少冲突就小步提交勤同步。**



<!-- ============ 文档分隔线：004-github/042-GitTagManage.md ============ -->


## 开篇：像里程碑书签一样打标签

长途自驾时，你会在导航里设置几个**途经点**：出发 100 公里是服务区、300 公里是加油站、终点是目的地。这些途经点让你的行程有了"可回溯的刻度"——无论开到哪，都知道离哪个节点还有多远。

Git 的**标签（tag）** 就是版本历史里的"途经点"：它给某一个提交打上一个固定的、有意义的名字，比如 `v1.0.0`、`v2.1.0-rc.1`。与分支不同，标签**不会随着新提交移动**，它是"静止的书签"——永远指向那一个提交。

对发布流程来说，标签就是**里程碑**：`v1.0.0` 代表"1.0 正式版在这里"，团队只要 checkout 这个标签，就能精确复现当时的代码。

本篇采用**清单驱动**的叙事方式，把标签的"全生命周期"拆成一张任务清单，逐项勾选：**创建 → 查看 → 推送 → 检出 → 删除**，最后补上语义化版本规范。

---

## 一、先认识两种标签：附注 vs 轻量

官方文档把标签分为两类，新手务必先分清：

| 对比维度 | 附注标签（Annotated） | 轻量标签（Lightweight） |
| --- | --- | --- |
| 创建命令 | `git tag -a v1.0.0 -m "说明"` | `git tag v1.0.0` |
| 存储形式 | 完整的 Git 对象（含创建者、邮箱、日期、说明，可 GPG 签名） | 只是一个指向提交的引用（指针） |
| 查看信息 | `git show` 能看到完整标签信息 | `git show` 只显示提交信息 |
| 适用场景 | **正式发布、里程碑标记（推荐）** | 临时标记、私人标记 |
| 可追溯性 | 强，可签名可验证 | 弱，无额外信息 |

> 原理提示（官方原文）：附注标签"包含创建日期、标签者姓名和电子邮件、标签信息和可选的 GnuPG 签名"；轻量标签"只是一个对象（通常是提交对象）的名字"。**官方建议正式发布的版本一律使用附注标签**。

---

## 二、清单第一项：创建标签

### 2.1 在当前提交创建附注标签（推荐）

```bash
# -a 表示附注标签，-m 写说明；不写 -m 会打开编辑器
git tag -a v1.0.0 -m "发布版本 1.0.0"
```

### 2.2 在历史提交上补标签

忘记给上个版本打标签了？补上即可：

```bash
# 为历史提交 abc1234 补打附注标签
git tag -a v0.9.0 abc1234 -m "历史版本 v0.9.0"

# 为历史提交打轻量标签
git tag v0.9.0 abc1234
```

### 2.3 创建轻量标签

```bash
# 不带 -a/-s/-m 就是轻量标签
git tag v1.0.0-lw
```

### 2.4 创建 GPG 签名标签（开源项目进阶）

```bash
# -s 用你的 GPG 密钥签名
git tag -s v2.0.0 -m "正式发布版本 2.0.0，已签名"

# 验证标签签名
git tag -v v2.0.0
```

### 2.5 命名规范（避免踩坑）

| 要求 | 示例 |
| --- | --- |
| 不能以 `-` 开头 | 不要写成 `-v1.0` |
| 语义化版本命名 | `v1.0.0`、`v2.1.0`、`v1.0.0-rc.1` |
| 预发布带后缀 | `-beta`、`-rc.1`（放在主版本号之后） |
| 不建议包含空格 | 标签名里不要用空格 |

---

## 三、清单第二项：查看标签

```bash
# 列出所有本地标签（按字母顺序）
git tag
# 输出示例：
# v0.9.0
# v1.0.0
# v1.0.0-beta

# 按模式筛选（注意：用通配符时必须带 -l）
git tag -l "v1.*"
# 输出：v1.0.0、v1.0.0-beta

# 查看标签详情（附注标签会显示完整信息）
git show v1.0.0

# 按版本号倒序排列
git tag -l --sort=-v:refname

# 统计标签数量
git tag | wc -l
```

`git show v1.0.0` 的输出示例（附注标签）：

```
tag v1.0.0
Tagger: 张三 <zhangsan@example.com>
Date:   Sat Aug 2 10:00:00 2026 +0800

发布版本 1.0.0

commit 7a3f9c1e2d4b5a6c8f9e0d1b2c3a4b5c6d7e8f9a
Author: 张三 <zhangsan@example.com>
Date:   Sat Aug 2 09:30:00 2026 +0800

    feat: 完成核心功能
```

看懂输出：上面是标签自己的信息（Tagger、Date、说明），下面是标签指向的提交信息。这就是附注标签比轻量标签"信息量大"的直接体现。

---

## 四、清单第三项：推送标签到远程

**重要知识点：`git push` 默认不会推送标签**，必须显式操作：

```bash
# 推送单个标签
git push origin v1.0.0

# 推送所有本地标签
git push origin --tags

# 推送分支的同时推送标签
git push origin main --tags

# 标签已被占用时强制覆盖（慎重！会覆盖远程同名标签）
git push origin -f v1.0.0
```

推送输出示例：

```
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 1.14 KiB | 1.14 MiB/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To https://github.com/user/repo.git
 * [new tag]         v1.0.0 -> v1.0.0
```

> 最佳实践：发布流程建议用 `--follow-tags` 代替 `--tags`——它只推送"附注标签"，避免把临时轻量标签也推上去：
>
> ```bash
> git push --follow-tags origin main
> ```

---

## 五、清单第四项：检出标签

检出标签时要注意：**直接 checkout 标签会进入"分离头指针"（detached HEAD）状态**，此时的新提交不属于任何分支。

```bash
# 检出标签指向的代码（分离 HEAD 状态）
git checkout v1.0.0
# 输出提示：You are in 'detached HEAD' state...

# 想基于标签改代码：从标签创建新分支（推荐做法）
git switch -c hotfix-1.0 v1.0.0

# 旧写法（等价）
git checkout -b hotfix-1.0 v1.0.0
```

> 原则：**只读查看用 `git checkout <标签>`；要修改就必须先建分支**。不要在分离 HEAD 状态下直接提交，否则切走后提交会"找不到归属"。

---

## 六、清单第五项：删除标签

```bash
# 删除本地标签
git tag -d v1.0.0
# 输出：Deleted tag 'v1.0.0' (was 7a3f9c1)

# 删除远程标签（推荐写法）
git push origin --delete v1.0.0

# 删除远程标签（替代写法：推送空引用）
git push origin :refs/tags/v1.0.0

# 批量删除本地标签（例如清掉所有 v0.x 的旧标签）
git tag -l "v0.*" | xargs git tag -d
```

---

## 七、清单之外的进阶操作

```bash
# 查看标签指向的提交 ID
git rev-list -n 1 v1.0.0

# 比较两个标签之间的差异
git diff v1.0.0..v1.1.0

# 查看两个标签之间的提交记录
git log v1.0.0..v1.1.0 --oneline

# 只列出正式版本标签（排除预发布带 - 的）
git tag -l "v[0-9]*.[0-9]*.[0-9]*" | grep -v "-"
```

### 7.1 标签与分支的本质区别（必懂）

| 对比维度 | 分支（branch） | 标签（tag） |
| --- | --- | --- |
| 是否移动 | 会随新提交**自动前移** | **静止不动**，永远指向同一个提交 |
| 本质 | 可移动的指针 | 固定的引用（或指向提交的名字） |
| 用途 | 承载持续开发 | 标记发布点、里程碑 |
| 修改方式 | 提交即前移 | 需显式 `-f` 才能强制移动 |

这个区别是理解"为什么发布版本要用标签而不是分支"的关键：**分支是流动的"河"，标签是固定的"界碑"**。测试、部署、复现线上问题，都应该锚定在标签上，而不是可能被新提交带跑的分支上。

---

## 八、语义化版本（SemVer）规范

标签命名强烈建议遵循语义化版本规范 `主版本.次版本.修订号`：

```
v1.0.0-beta     # 测试版
v1.0.0-rc.1     # 发布候选（Release Candidate）
v1.0.0          # 正式版
v1.1.0          # 新增功能（向后兼容）
v2.0.0          # 不兼容的大改版
```

```bash
# 创建预发布标签
git tag -a v1.0.0-beta -m "1.0.0 测试版"

# 创建发布候选标签
git tag -a v1.0.0-rc.1 -m "1.0.0 候选版本"

# 创建正式版标签
git tag -a v1.0.0 -m "1.0.0 正式发布"
```

版本号变更规则一句话：**修复 Bug 改修订号，加功能改次版本，破坏性变更改主版本**。

---

## 九、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 标签名重复创建 | `fatal: tag 'v1.0.0' already exists` | 标签必须唯一 | 换新名字，或用 `git tag -f` 强制覆盖（先确认影响） |
| push 后远程没标签 | 远程仓库找不到标签 | 忘了 `git push` 默认不推送标签 | 显式执行 `git push origin <标签>` 或 `git push origin --tags` |
| checkout 标签后提交"丢失" | 切回分支后改动找不到了 | 分离 HEAD 状态下提交不属于任何分支 | 先 `git switch -c <新分支>` 再提交 |
| 推标签失败 | `! [rejected] v1.0.0 -> v1.0.0 (already exists)` | 远程已有同名标签 | 确认是否真的要覆盖，需要时 `git push -f origin v1.0.0` |
| 打标签打错提交 | 标签指向了错误的提交 | 没指定提交 ID，默认打在 HEAD | 用 `git tag -a v1.0.0 <正确提交ID> -m "..."` 补打，再删掉错的 |
| 删除远程标签没生效 | 远程仍显示旧标签 | 用了错误的删除语法 | 用 `git push origin --delete <标签>`；本地残留可 `git fetch --prune --tags` 清理 |

---

## 十一、一句话记忆

**标签是静止的书签、发布的里程碑：`-a -m` 建附注标签（正式发布用），`push` 默认不带你得显式推，checkout 后记得建分支，`-d` 删本地、`--delete` 删远程，命名跟着语义化版本走（主.次.修订）。**



<!-- ============ 文档分隔线：004-github/043-GitRemoteManage.md ============ -->


## 开篇：像多台电脑同步一样管理远程

想象你同时用办公室电脑、家里的笔记本和手机处理同一个项目。没有云盘时，你得靠 U 盘来回拷文件，稍不留神就"哪个版本是最新的"都分不清。有了云盘后，所有设备都以**云端为唯一权威**：在办公室改完上传，到家下载接着改。

Git 的**远程仓库（remote）** 就是那个"云端"。它不一定在 GitHub 上——也可以是公司内网、另一台电脑，甚至你本机的另一个文件夹（官方文档明确说："remote"不意味着一定在网络上，只意味着在别处）。

本篇采用**场景驱动**的叙事方式，从"多设备协作"的日常场景出发，串讲 `git remote` 系列命令：**查看关联 → 添加关联 → 修改关联 → 删除关联 → 多远程协作 → 凭证管理**。学完这篇，你在任何一台设备上都能无缝衔接工作。

---

## 一、场景入门：先搞懂 remote 是什么

`git remote` 管理的是**"本地仓库与远程仓库之间的关联关系"**。每个远程有一个**简称（shortname）**，最常见的是 `origin`——这是 `git clone` 时 Git 自动起的默认名字，代表"克隆来源"。

```
本地仓库  --push/pull-->  origin（GitHub 上的仓库）
            --fetch-->     upstream（原作者的仓库，fork 场景）
```

| 简称 | 含义 | 典型场景 |
| --- | --- | --- |
| `origin` | 你自己的远程（克隆来源或主远程） | 日常 push/pull |
| `upstream` | 原作者的远程 | fork 后同步上游代码 |

> 原理提示：远程关联信息存在仓库的 `.git/config` 文件里。`git remote add` 只是往配置文件里加一行记录，**不会下载任何代码**。真正联网的动作是 `git fetch` / `git push` / `git pull`。

---

## 二、场景一：刚 clone 完，先看看关联了谁

```bash
# 列出所有远程的简称
git remote
# 输出：origin

# 查看简称对应的 URL（-v = verbose，最常用）
git remote -v
```

`git remote -v` 输出示例：

```
origin  https://github.com/yourname/my-repo.git (fetch)
origin  https://github.com/yourname/my-repo.git (push)
```

看懂输出：每个远程会显示两行——`(fetch)` 拉取用的地址和 `(push)` 推送用的地址（通常相同）。

```bash
# 查看指定远程的详细信息（分支、跟踪关系、落后/领先状态）
git remote show origin

# 只看远程默认分支名
git remote show origin | grep "HEAD branch"
```

`git remote show origin` 的关键输出段：

```
* remote origin
  Fetch URL: https://github.com/yourname/my-repo.git
  Push  URL: https://github.com/yourname/my-repo.git
  HEAD branch: main
  Remote branches:
    main                     tracked
    feature/login            tracked
  Local branches configured for 'git pull':
    main merges with remote main
```

---

## 三、场景二：本地已有项目，关联到 GitHub（最常踩坑的场景）

你本地 `git init` 建了仓库并提交过，现在想把它推送到 GitHub 上新建的空仓库。此时**没有** `origin`，需要手动添加：

```bash
# 添加名为 origin 的远程（HTTPS 方式）
git remote add origin https://github.com/yourname/my-repo.git

# 添加名为 origin 的远程（SSH 方式，免密，需先配置 SSH 密钥）
git remote add origin git@github.com:yourname/my-repo.git

# 验证添加成功
git remote -v

# 首次推送（-u 建立追踪关系）
git push -u origin main
```

### 3.1 添加多个远程

同一个本地仓库可以关联多个远程，各起各的名：

```bash
# 关联原作者的仓库（fork 工作流用）
git remote add upstream https://github.com/original/repo.git

# 关联一个备份仓库
git remote add backup https://github.com/yourname/backup.git

# 添加 -f 参数：添加的同时立即 fetch 一次
git remote add -f upstream https://github.com/original/repo.git
```

---

## 四、场景三：远程地址变了，改一下关联

仓库改名、账号变更、或从 HTTPS 换 SSH，都需要修改 URL。**推荐用 `set-url` 直接改，而不是"删了重加"**（删了重加会丢失跟踪关系）：

```bash
# 查看当前 URL
git remote get-url origin

# 修改 origin 的 URL
git remote set-url origin https://github.com/yourname/new-repo.git

# 从 HTTPS 切换为 SSH（解决"每次都要输密码"的痛点）
git remote set-url origin git@github.com:yourname/my-repo.git

# 从 SSH 切换为 HTTPS
git remote set-url origin https://github.com/yourname/my-repo.git
```

场景举例：仓库从 GitHub 迁移到 Gitee（码云）后：

```bash
git remote set-url origin https://gitee.com/yourname/my-repo.git
git remote -v        # 验证 URL 已更新
git push             # 直接推送即可
```

### 4.1 重命名远程

```bash
# 把 origin 重命名为 main-remote
git remote rename origin main-remote
# 注意：rename 会同步更新所有相关跟踪分支的名字（origin/main -> main-remote/main）
```

---

## 五、场景四：不再需要某个关联，删掉它

```bash
# 删除远程关联（remove 与 rm 等价）
git remote remove origin

# rm 简写
git remote rm origin

# 删除后重新添加（不推荐，尽量用 set-url）
git remote remove origin
git remote add origin https://github.com/yourname/new.git
```

> 警告：`git remote remove` 只删除本地与远程的**关联配置**，**不会删除 GitHub 上的仓库，也不会动本地代码**。但关联的远程跟踪分支（origin/main 等）和配置会被一并清除，删除前确认不再需要。

---

## 六、场景五：多设备 + fork 协作（远程进阶）

### 6.1 多台电脑同步同一项目

```bash
# 新设备上首次拉取
git clone https://github.com/yourname/my-repo.git
cd my-repo

# 日常流程：先拉后推
git pull
# ...修改代码...
git add . && git commit -m "feat: 新功能"
git push
```

### 6.2 fork 工作流：origin + upstream 双远程

参与开源项目时，你会 **fork**（把别人的仓库复制到自己名下），形成"你的 fork（origin）+ 原作者仓库（upstream）"双远程结构：

```bash
# 1. 克隆自己的 fork（origin 自动生成）
git clone https://github.com/yourname/original-repo.git

# 2. 添加原作者仓库为 upstream
git remote add upstream https://github.com/original-author/original-repo.git

# 3. 定期同步上游最新代码
git fetch upstream
git switch main
git merge upstream/main          # 或 git rebase upstream/main

# 4. 把同步后的代码推送到自己的 fork
git push origin main

# 5. 在 GitHub 上给原作者提 Pull Request（PR）
```

fork 同步的完整图解：

```
upstream（原作者仓库）  --fetch-->  本地 main  --push-->  origin（你的 fork）  --PR-->  upstream
```

---

## 七、凭证管理：不用反复输密码

HTTPS 方式每次 push 都要输用户名密码（或 Token），配置 credential helper 可以自动记忆：

```bash
# 方式一：临时缓存（内存中，默认 15 分钟）
git config --global credential.helper cache

# 缓存 1 小时
git config --global credential.helper 'cache --timeout=3600'

# 方式二：永久存储到磁盘（明文，注意安全）
git config --global credential.helper store

# 方式三：Windows 凭证管理器（推荐，加密存储）
git config --global credential.helper manager

# 方式四：macOS 钥匙串
git config --global credential.helper osxkeychain
```

| 方式 | 存储位置 | 安全级别 | 适用系统 |
| --- | --- | --- | --- |
| `cache` | 内存 | 高（重启失效） | 所有 |
| `store` | 明文文件 | 低 | 所有（慎用） |
| `manager` | Windows 凭据管理器 | 高 | Windows |
| `osxkeychain` | macOS 钥匙串 | 高 | macOS |

> 更推荐的做法：直接改用 **SSH 协议**（配置 SSH 密钥后完全免密），配置方法见 004-SSHHTTPS 篇。

---

## 八、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 添加远程时名字冲突 | `fatal: remote origin already exists.` | 已存在同名远程 | 用 `git remote set-url origin <新URL>` 修改，或先 remove 再 add |
| push 时报找不到远程 | `fatal: 'origin' does not appear to be a git repository` | 本地仓库没有关联 origin | `git remote add origin <URL>` 手动添加 |
| clone 的仓库 push 被拒 | `non-fast-forward` / `rejected` | 远程有你本地没有的提交 | 先 `git pull`，解决冲突后再 push |
| 远程地址配错 | `could not read Username for 'https://github.com'` | URL 拼写错误或没有权限 | `git remote get-url origin` 检查，用 `set-url` 修正 |
| HTTPS 频繁要密码 | 每次 push 都弹认证 | 没配置 credential helper 或没用 SSH | 配置 `credential.helper manager`，或切换 SSH |
| remove 后"远程仓库没了" | 误以为 GitHub 上的仓库被删 | 理解偏差：remove 只删本地关联 | GitHub 上的仓库还在；重新 `git remote add` 即可恢复关联 |
| fork 后同步不到上游更新 | upstream 里看不到新提交 | 没添加 upstream 或没 fetch | `git remote add upstream <原仓库URL>` + `git fetch upstream` |

---

## 十、一句话记忆

**远程是"云端"、origin 是默认关联：`add` 添加、`-v` 查看、`set-url` 改地址（不要删了重加）、`remove` 删除（只删本地关联不删云端）、fork 场景加 upstream 定期同步、凭证用 manager 或换 SSH——多设备协作从此无缝衔接。**



<!-- ============ 文档分隔线：004-github/044-GitHistoryLog.md ============ -->


## 开篇：像侦探查案一样翻阅历史

想象你是一名侦探，接手一桩"代码失踪案"：昨晚还能运行的程序，今天早上突然崩溃了。你需要回答三个问题：

1. **什么时候改的？**（哪一次提交让程序变坏的）
2. **谁改的？**（哪个同事的哪次操作）
3. **改成什么样了？**（具体是哪几行代码出了问题）

Git 的提交历史就是你的"案卷库"，而 `git log` 就是你的"查档系统"。Git 官方甚至把仓库描述为"内容寻址文件系统"——每次提交都是一个不可变的快照，你可以像翻档案一样回到任何一天。

本篇采用**侦探驱动**的叙事方式：以"破案"为线索，依次学习**看总览（log）、筛线索（filter）、对现场（diff）、看单份案卷（show）、追查每行来源（blame）、翻查活动记录（reflog）** 六种取证姿势。

---

## 一、第一招：看总览——git log 基础

### 1.1 完整案卷

```bash
# 查看完整提交历史（按时间倒序）
git log
```

输出示例：

```
commit 8f4b2c1e2d3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c
Author: 张三 <zhangsan@example.com>
Date:   Sat Aug 2 09:30:00 2026 +0800

    feat: 添加加法函数
```

每条提交包含：提交 ID（完整 SHA-1 哈希）、作者、日期、提交信息。

### 1.2 精简案卷

```bash
# 每条提交一行（最常用，一眼扫过全部历史）
git log --oneline
# 输出示例：
# 8f4b2c1 (HEAD -> main) feat: 添加加法函数
# a1b2c3d docs: 更新 README

# 只看最近 N 条
git log -5

# 单行 + 数量
git log -5 --oneline
```

### 1.3 画关系图

```bash
# 图形化显示分支合并历史（能看到 merge 的分叉与交汇）
git log --graph

# 最常用的组合：单行 + 图形 + 所有分支
git log --oneline --graph --all

# 只看合并提交
git log --merges

# 排除合并提交
git log --no-merges
```

`git log --oneline --graph --all` 输出示例：

```
* 8f4b2c1 (HEAD -> main) feat: 添加加法函数
* a1b2c3d docs: 更新 README
|\
| * e4f5g6h (feature) feat: 登录功能
|/
* 7a3f9c1 chore: 项目初始化
```

---

## 二、第二招：筛线索——git log 过滤参数

### 2.1 按作者筛选

```bash
# 查看指定作者的提交
git log --author="zhangsan"

# 模糊匹配（支持正则）
git log --author="zhang"
```

### 2.2 按提交信息搜索

```bash
# 搜索提交信息中包含"登录"的提交
git log --grep="登录"

# 不区分大小写
git log --grep="login" -i
```

### 2.3 按日期筛选

```bash
# 指定日期范围
git log --since="2026-01-01" --until="2026-07-31"

# 相对时间（最近 2 周）
git log --since="2 weeks ago"

# 等价写法：--after / --before
git log --after="2026-06-01" --before="2026-06-30"
```

### 2.4 按文件筛选

```bash
# 查看指定文件的提交历史（注意 -- 分隔）
git log -- src/index.js

# 查看指定目录的历史
git log -- src/

# 跟踪文件重命名前的历史
git log --follow src/index.js
```

### 2.5 按代码内容筛选（Pickaxe 挖掘）

```bash
# 找出"添加或删除过某段代码"的提交（-S 是次数变化）
git log -S "console.log"

# 按正则匹配行变化（-G 是行匹配）
git log -G "function\s+login"
```

### 2.6 提交范围筛选（双点语法）

```bash
# 在 feature 但不在 main 的提交（feature 独有提交）
git log main..feature

# 本地比远程多的提交（push 前检查）
git log origin/main..HEAD
```

---

## 三、第三招：对现场——git diff 差异对比

diff 是"案发现场对比"：同一个文件在提交前后差了什么。

```bash
# 工作区与暂存区的差异（还没 add 的改动）
git diff

# 暂存区与上次提交的差异（已 add 未 commit 的改动）
git diff --staged

# 工作区与上次提交的所有差异（add 没 add 都算）
git diff HEAD

# 指定文件
git diff src/index.js

# 两个提交之间
git diff abc1234 def5678

# 两个分支之间
git diff main..feature

# 三点比较：feature 相对两分支共同祖先的差异（更聚焦）
git diff main...feature

# 只看文件名
git diff --name-only

# 看改动统计
git diff --stat
```

`git diff --stat` 输出示例：

```
 src/index.js | 10 +++++-----
 README.md    |  2 +-
 2 files changed, 8 insertions(+), 4 deletions(-)
```

---

## 四、第四招：看单份案卷——git show

```bash
# 查看指定提交的详情和改动
git show abc1234

# 只看提交改动的文件列表
git show --stat abc1234

# 查看指定提交中某文件的内容（取证"这个版本里这个文件长什么样"）
git show abc1234:src/index.js

# 查看最近一次提交
git show HEAD

# 查看倒数第二次提交
git show HEAD~1
```

`git show HEAD` 输出结构：提交元信息 + 改动 diff。

---

## 五、第五招：追查每行来源——git blame

"这行代码到底是谁写的？"——`git blame` 就是干这个的，它能告诉你**文件每一行最后一次被谁、在哪个提交、什么时候修改**：

```bash
# 显示文件每行的最后修改者
git blame src/index.js

# 只看 10 到 20 行（定位嫌疑区间）
git blame -L 10,20 src/index.js

# 忽略纯空格改动（避免把格式化也算作"修改者"）
git blame -w src/index.js
```

`git blame` 输出示例：

```
8f4b2c1 (张三 2026-08-02 09:30:00 +0800  1) function add(a, b) {
a1b2c3d (李四 2026-07-25 14:20:00 +0800  2)   return a + b;
```

---

## 六、第六招：翻活动记录——git reflog（时光机）

`git log` 只记录**提交历史**，而 `git reflog` 记录**你所有的操作足迹**——包括 reset、checkout、rebase、merge 这些"移动指针"的动作。它是找回"丢失提交"的最后防线：

```bash
# 查看 HEAD 的所有操作历史
git reflog
```

输出示例：

```
8f4b2c1 (HEAD -> main) HEAD@{0}: commit: feat: 添加加法函数
7a3f9c1 HEAD@{1}: reset: moving to HEAD~1
a1b2c3d HEAD@{2}: commit: docs: 更新 README
9fceb02 HEAD@{3}: checkout: moving from feature to main
```

```bash
# 查看指定分支的引用日志
git reflog feature

# 查看所有引用日志
git reflog --all

# 用 reflog 找回误删的提交（reset 之后救命的操作）
git reset --hard HEAD@{2}

# 查看 reflog 中第 N 个状态的提交内容
git show HEAD@{3}
```

> 原理与警告：reflog 是 Git 的"本地保险丝"——只要操作发生在本地，它就留有足迹。但 reflog **不会推送到远程**，且仓库 GC（垃圾回收）后会过期清理（默认 90 天）。所以"误删提交后的急救"要趁早。

### 6.1 自定义输出格式（让案卷按你的口味排版）

`git log` 支持用 `--pretty=format:` 自定义每条提交的排版，适合写进别名长期使用：

```bash
# 自定义格式：哈希 + 分支标记 + 作者 + 相对时间 + 提交信息
git log --pretty=format:'%h %d %an %ar %s'

# 美化版（带颜色）：
git log --pretty=format:'%Cred%h%Creset - %C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --graph

# 配置成别名（一劳永逸）
git config --global alias.lg "log --oneline --graph --all --decorate"
git lg
```

常用格式占位符速查：`%h` 短哈希、`%an` 作者名、`%ae` 作者邮箱、`%ar` 相对时间、`%s` 提交信息、`%d` 引用名（分支/标签）、`%Cred/%Cgreen` 颜色控制。

### 6.2 提交范围语法补充（双点与三点）

```bash
# 双点 A..B：在 B 但不在 A 的提交（B 独有）
git log main..feature

# 三点 A...B：A 和 B 各自独有的提交（对称差）
git log main...feature

# 结合 --left-right 显示每行属于哪一边
git log --left-right --oneline main...feature
```

`--left-right` 输出中 `<` 表示属于左边分支（main），`>` 表示属于右边分支（feature），方便一眼看清两边的分叉内容。

---

## 七、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| 查文件历史没结果 | `git log <文件>` 输出为空 | 路径写错，或未用 `--` 分隔（与分支名歧义） | 用 `git log -- <路径>` 明确是路径 |
| log 输出太长 | 刷屏看不到重点 | 默认输出全部历史 | 用 `--oneline`、`-10` 等参数限制 |
| diff 无输出 | `git diff` 什么都没显示 | 改动已全部暂存（diff 默认只看工作区） | 改用 `git diff --staged` 或 `git diff HEAD` |
| blame 显示不了 | `fatal: no such path` | 文件路径不在当前提交中 | 确认文件存在；旧文件用 `git blame <提交ID> -- <路径>` |
| 误 reset 后提交"消失" | `git log` 找不到那个提交 | 指针移走了，但提交对象还在 | 用 `git reflog` 找到原 ID，`git reset --hard <ID>` 找回 |
| reflog 里找不到记录 | 想找的记录不在了 | 超过 90 天或仓库 GC 过 | 无解；养成"危险操作前先备份分支"的习惯 |
| 想查删除文件的历史 | `git log -- <删除文件>` 没反应 | 默认不追踪删除 | 用 `git log --all --diff-filter=D -- <路径>` 或先定位删除提交 |

---

## 九、一句话记忆

**查历史像破案：`git log` 看总览（--oneline 精简、--graph 画图），`--author/--since/-S` 筛线索，`git diff` 对现场，`git show` 看单份案卷，`git blame` 追每行来源，`git reflog` 是最后保险丝——误删别慌，reflog 里找回来。**



<!-- ============ 文档分隔线：004-github/045-GitStashReset.md ============ -->


## 开篇：像寄存柜与时光机一样管理改动

在大型商场里，你拎着大包小包没法逛街。这时你走到**寄存柜**前，把东西暂存进去、拿走钥匙牌，轻装继续逛；逛完凭牌取回，东西原封不动。

`git stash` 就是代码的"寄存柜"：当你工作到一半、还不能提交，但又必须切换分支或拉取代码时，把当前改动"暂存"起来，让工作区回到干净状态；办完事再"取回"改动，继续干活。

而**时光机**大家都懂：回到过去、修正错误。`git reset` 就是 Git 的时光机——把分支指针拨回过去的某个提交。但它有三个"档位"：**软回退（只拨指针）、混合回退（连暂存区一起拨）、硬回退（连工作区一起拨）**，选错档位，后果天差地别。

本篇采用**类比驱动**的叙事方式：以"寄存柜"讲透 stash，以"时光机"讲透 reset 及其安全替代品 revert，最后用 restore 和 clean 补齐"撤销三兄弟"。

---

## 一、寄存柜：git stash 暂存系列

### 1.1 为什么需要寄存（典型场景）

```bash
# 场景：正在开发登录功能（没写完，不想提交），但 main 分支有个紧急 Bug 要修
git switch main        # 报错！有未提交的改动，切不过去

# 解法：先把改动存起来
git stash
git switch main        # 成功切换，工作区干净
# ...修复 Bug 并提交...
git switch feature/login
git stash pop          # 取回之前未写完的改动
```

> 原理提示：`git stash` 把工作区和暂存区的改动打包成一个"暂存条目"存到 `refs/stash` 引用里，然后把工作区还原成与 HEAD 一致。注意：**它默认不包含未跟踪的新文件**（需要加 `-u`）。

### 1.2 暂存（存包）

```bash
# 暂存当前所有已跟踪改动（最常用）
git stash

# 暂存并附上说明（好找）
git stash push -m "登录功能开发中"

# 连同未跟踪文件一起暂存（新文件也存）
git stash -u

# 连忽略文件也一起暂存（极少数情况用）
git stash -a

# 暂存但保留暂存区内容（--keep-index）
git stash --keep-index
```

### 1.3 查看（看寄存柜里有什么）

```bash
# 列出所有暂存条目（stash@{0} 是最近的一个）
git stash list
# 输出示例：
# stash@{0}: On feature/login: 登录功能开发中
# stash@{1}: On main: 样式调整

# 查看最近暂存的改动摘要
git stash show

# 查看指定暂存的改动摘要
git stash show stash@{1}

# 查看指定暂存的完整差异（-p 补丁格式）
git stash show -p stash@{0}
```

### 1.4 恢复（取包）

```bash
# 恢复最近暂存并删除该条记录（最常用）
git stash pop

# 恢复指定暂存
git stash pop stash@{1}

# 恢复但不删除记录（想保留备份时用）
git stash apply

# 恢复指定暂存且保留记录
git stash apply stash@{1}
```

> 对比记忆：**pop = 取包 + 退钥匙牌（删除记录）；apply = 取包但保留钥匙牌（记录还在）**。

### 1.5 删除（扔包）

```bash
# 删除指定暂存记录
git stash drop stash@{0}

# 清空所有暂存记录
git stash clear

# 基于暂存创建新分支（处理"恢复时与当前分支冲突"的场景）
git stash branch feature/recovery stash@{0}
```

---

## 二、时光机：git reset 回退系列

### 2.1 时光机原理：指针的三档回拨

`git reset` 的本质是**把当前分支指针（以及可选的工作区/暂存区）移回过去的提交**。三个档位的区别，用"指针、暂存区、工作区"三件套来记：

| 档位 | 命令 | 分支指针 | 暂存区 | 工作区 | 适用场景 |
| --- | --- | --- | --- | --- | --- |
| 软回退 | `git reset --soft <目标>` | 回退 | 保留 | 保留 | 想重新提交（改动留在暂存区） |
| 混合回退 | `git reset --mixed <目标>`（默认） | 回退 | 回退 | 保留 | 想重新 add（改动留在工作区） |
| 硬回退 | `git reset --hard <目标>` | 回退 | 回退 | 回退 | 彻底丢弃改动（危险） |

### 2.2 三个档位的命令

```bash
# 软回退：撤销上次提交，改动保留在暂存区（改完再提交）
git reset --soft HEAD~1

# 混合回退（默认）：撤销提交和暂存，改动保留在工作区
git reset HEAD~1
# 或显式写：git reset --mixed HEAD~1

# 硬回退：彻底回到上次提交的状态（所有未提交改动永久丢失）
git reset --hard HEAD~1

# 回退到指定提交
git reset --hard abc1234

# 回退单个文件到上次提交状态（不影响其他文件）
git reset HEAD~1 src/index.js

# 让本地分支与远程分支完全一致
git reset --hard origin/main
```

### 2.3 回退前必读的安全警告

1. `--hard` 会**永久丢弃**工作区和暂存区的未提交改动，无法用 `git status` 找回，只能靠 `reflog` 抢救；
2. 已 push 的提交不要用 reset 回退（历史分叉会坑队友），改用 `git revert`（见第三节）；
3. 回退前养成习惯：先 `git stash` 或 `git branch backup` 备份当前状态。

---

## 三、安全撤销：git revert 反向提交

`git revert` 与 reset 的本质区别：**reset 是"抹掉历史"，revert 是"新增一个反向提交来抵消历史"**。revert 不改变已有提交，因此**可以安全用于已推送的远程提交**：

```bash
# 创建一个新提交，撤销指定提交的改动
git revert abc1234

# 撤销最近一次提交
git revert HEAD

# 反向但不自动提交（先检查再手动提交）
git revert -n abc1234

# 反向一个范围的提交
git revert abc1234..def5678
```

| 对比维度 | `git reset` | `git revert` |
| --- | --- | --- |
| 历史处理 | 移动指针（改写历史） | 新增提交（保留历史） |
| 是否安全用于已推送提交 | 不安全 | 安全 |
| 适用场景 | 本地未推送的提交 | 已推送的提交、公共分支 |
| 命令形态 | `git reset --hard HEAD~1` | `git revert abc1234` |

---

## 四、撤销工作区与暂存区：git restore

`git restore` 是 Git 2.23+ 引入的"撤销专用命令"，把原本混在 `checkout`/`reset` 里的撤销职责独立出来，语义更清晰：

```bash
# 撤销工作区修改（恢复到上次提交/暂存的状态）——危险，改动丢失
git restore index.js

# 旧写法（等价）
git checkout -- index.js

# 撤销当前目录所有工作区改动
git restore .

# 取消暂存（把文件从暂存区移回工作区，内容不丢）
git restore --staged index.js

# 取消所有暂存
git restore --staged .

# 从指定提交恢复文件
git restore --source=abc1234 index.js
```

> 记忆锚点：`git restore` 默认管**工作区**，加 `--staged` 管**暂存区**；`--source` 指定从哪个提交恢复。

---

## 五、清理未跟踪文件：git clean

`git stash` 和 `git reset` 都不管**未跟踪文件**，`git clean` 专门负责清理它们。**注意：它删除的文件无法恢复，务必先 `-n` 预览**：

```bash
# 预览将被删除的未跟踪文件（安全模式，不实际删除）
git clean -n

# 强制删除未跟踪文件
git clean -f

# 删除未跟踪文件和目录
git clean -fd

# 连忽略文件（.gitignore 里的）一起删（最彻底，最危险）
git clean -fdx

# 交互式逐个确认
git clean -i
```

---

## 六、常见错误与对策表

| 错误现象 | 报错信息（节选） | 原因分析 | 解决办法 |
| --- | --- | --- | --- |
| stash 后新文件不见了 | pop 后新建的文件没恢复 | stash 默认不含未跟踪文件 | 暂存时用 `git stash -u` |
| pop 时冲突 | `CONFLICT (content): Merge conflict in ...` | 暂存的改动与当前工作区冲突 | 按 041 篇解决冲突；pop 失败不会删记录，解决后 `git stash drop` 手动清理 |
| 误用 --hard 丢改动 | 工作区改动全部消失 | `--hard` 回退会丢弃未提交改动 | 立即用 `git reflog` + `git reset --hard <原ID>` 抢救 |
| reset 后 push 被拒 | `! [rejected] ... (non-fast-forward)` | 回退的是已推送提交，历史分叉 | 改用 `git revert` 生成反向提交后再 push |
| apply 与 pop 分不清 | 恢复后记录还在/没了 | 混淆两者语义 | pop 删记录、apply 留记录；按需选择 |
| 误以为 reset 能找回 stash | stash clear 后想找回 | 已清空无记录 | 无解；clear 前用 `git stash list` 确认，或改用 drop 单条删除 |
| clean 误删文件 | 文件被删且找不到 | 忘记先 `-n` 预览 | 养成先 `git clean -n` 预览再 `-f` 的习惯；无法恢复 |

---

## 八、一句话记忆

**stash 是寄存柜（存：`stash push -u`，看：`stash list`，取：`pop` 删记录 / `apply` 留记录，清：`clear`）；reset 是时光机（软拨指针、混拨暂存、硬全拨——`--hard` 慎用，先 stash 备份）；已推送的提交用 `revert` 反向抵消；`restore` 撤工作区/暂存区，`clean` 清未跟踪——先 `-n` 预览再动手。**



<!-- ============ 文档分隔线：004-github/046-GhCliAuth.md ============ -->


## gh 安装

**基本写法：winget 安装 gh**
`winget install GitHub.cli`
```bash
# 通过 Windows 包管理器安装 GitHub CLI
winget install GitHub.cli
```

---

**基本写法：Homebrew 安装 gh**
`brew install gh`
```bash
# macOS 通过 Homebrew 安装
brew install gh
```

---

**基本写法：apt 安装 gh（Ubuntu）**
`sudo apt install gh`
```bash
# Ubuntu 系统安装 GitHub CLI
sudo apt install gh
```

---

**基本写法：升级 gh**
`winget upgrade GitHub.cli`
```bash
# 升级到最新版本
winget upgrade GitHub.cli
```

---

**基本写法：验证安装**
`gh --version`
```bash
# 查看 gh 版本验证安装
gh --version
```

---

## 认证登录

**基本写法：交互式登录**
`gh auth login`
```bash
# 通过浏览器交互式登录 GitHub
gh auth login
```

---

**基本写法：使用 token 登录**
`gh auth login --with-token < <token文件>`
```bash
# 通过 token 文件登录（适合脚本）
gh auth login --with-token < token.txt
```

---

**基本写法：通过环境变量登录**
`export GH_TOKEN=<token>`
```bash
# 设置环境变量后 gh 自动认证
export GH_TOKEN=ghp_xxxxxxxxxxxx
```

---

**基本写法：指定企业版登录**
`gh auth login --hostname <企业域名>`
```bash
# 登录 GitHub 企业版
gh auth login --hostname github.example.com
```

---

## 认证状态

**基本写法：查看认证状态**
`gh auth status`
```bash
# 查看当前登录状态和账户
gh auth status
```

---

**基本写法：查看 token**
`gh auth status --show-token`
```bash
# 查看认证状态并显示 token
gh auth status --show-token
```

---

**基本写法：获取当前 token**
`gh auth token`
```bash
# 输出当前 token 用于脚本
gh auth token
```

---

**基本写法：刷新 token 权限**
`gh auth refresh`
```bash
# 刷新凭证添加新的权限范围
gh auth refresh
```

---

**基本写法：添加指定权限**
`gh auth refresh -s <权限>`
```bash
# 添加 repo 和 workflow 权限
gh auth refresh -s repo,workflow
```

---

## 账户管理

**基本写法：切换账户**
`gh auth switch`
```bash
# 交互式切换到其他账户
gh auth switch
```

---

**基本写法：切换到指定账户**
`gh auth switch --user <用户名>`
```bash
# 切换到指定用户账户
gh auth switch --user alice
```

---

**基本写法：登出**
`gh auth logout`
```bash
# 登出当前 GitHub 账户
gh auth logout
```

---

**基本写法：登出指定账户**
`gh auth logout --user <用户名>`
```bash
# 登出指定用户账户
gh auth logout --user alice
```

---

## SSH 密钥管理

**基本写法：上传 SSH 密钥**
`gh ssh-key add <密钥文件>`
```bash
# 上传公钥到 GitHub 账户
gh ssh-key add ~/.ssh/id_ed25519.pub
```

---

**基本写法：上传并添加标题**
`gh ssh-key add <密钥文件> --title "<标题>"`
```bash
# 上传公钥并设置标题
gh ssh-key add ~/.ssh/id_ed25519.pub --title "我的笔记本"
```

---

**基本写法：查看已上传的密钥**
`gh ssh-key list`
```bash
# 列出 GitHub 账户中的所有 SSH 密钥
gh ssh-key list
```

---

**基本写法：删除 SSH 密钥**
`gh ssh-key delete <密钥ID>`
```bash
# 删除指定的 SSH 密钥
gh ssh-key delete 12345
```

---

## 配置管理

**基本写法：设置默认编辑器**
`gh config set editor "<编辑器命令>"`
```bash
# 设置 VS Code 为默认编辑器
gh config set editor "code --wait"
```

---

**基本写法：设置默认浏览器**
`gh config set browser "<浏览器>"`
```bash
# 设置 Firefox 为默认浏览器
gh config set browser firefox
```

---

**基本写法：设置默认协议**
`gh config set git_protocol <协议>`
```bash
# 设置默认 Git 协议为 SSH
gh config set git_protocol ssh
```

---

**基本写法：查看配置**
`gh config get <配置项>`
```bash
# 查看指定配置项的值
gh config get editor
```

---

**基本写法：查看所有配置**
`gh config list`
```bash
# 列出所有 gh 配置
gh config list
```

---

## 帮助与参考

**基本写法：查看 gh 帮助**
`gh --help`
```bash
# 查看 gh 顶层帮助
gh --help
```

---

**基本写法：查看命令帮助**
`gh <命令> --help`
```bash
# 查看指定命令的详细帮助
gh pr --help
```

---

**基本写法：查看命令参考**
`gh reference`
```bash
# 输出所有命令的完整参考
gh reference
```

---

**基本写法：在浏览器中打开**
`gh <命令> --web`
```bash
# 在浏览器中打开对应页面
gh repo view --web
```



<!-- ============ 文档分隔线：004-github/047-GhPrManage.md ============ -->


## 创建 PR

**基本写法：交互式创建 PR**
`gh pr create`
```bash
# 通过交互式提示创建 PR
gh pr create
```

---

**基本写法：指定标题和正文**
`gh pr create --title "<标题>" --body "<正文>"`
```bash
# 直接指定 PR 标题和描述
gh pr create --title "feat: 添加用户认证" --body "实现 OAuth 登录流程"
```

---

**基本写法：使用提交信息填充**
`gh pr create --fill`
```bash
# 使用最近提交信息填充标题和正文
gh pr create --fill
```

---

**基本写法：创建草稿 PR**
`gh pr create --draft --title "<标题>"`
```bash
# 创建草稿 PR 待完善后再标记就绪
gh pr create --draft --title "WIP: 重构认证模块"
```

---

**基本写法：指定基础分支**
`gh pr create --base <分支> --head <分支>`
```bash
# 指定目标分支和源分支
gh pr create --base main --head feature/login
```

---

**基本写法：指定指派人**
`gh pr create --assignee <用户>`
```bash
# 创建 PR 并指派审查人
gh pr create --assignee @me
```

---

**基本写法：添加标签和审查人**
`gh pr create --label "<标签>" --reviewer <用户>`
```bash
# 创建 PR 并添加标签和审查人
gh pr create --label "需要审查" --reviewer alice
```

---

## 查看 PR

**基本写法：列出当前仓库 PR**
`gh pr list`
```bash
# 列出当前仓库的 PR
gh pr list
```

---

**基本写法：列出指定状态 PR**
`gh pr list --state <状态>`
```bash
# 列出指定状态的 PR
gh pr list --state open
```

---

**基本写法：查看自己的 PR**
`gh pr list --author @me`
```bash
# 列出自己创建的 PR
gh pr list --author @me
```

---

**基本写法：查看待审查 PR**
`gh pr list --reviewer @me`
```bash
# 列出等待自己审查的 PR
gh pr list --reviewer @me
```

---

**基本写法：按标签筛选**
`gh pr list --label "<标签>"`
```bash
# 按标签筛选 PR
gh pr list --label "bug"
```

---

**基本写法：限制返回数量**
`gh pr list --limit <数量>`
```bash
# 限制返回的 PR 数量
gh pr list --limit 50
```

---

**基本写法：查看 PR 详情**
`gh pr view <编号>`
```bash
# 查看指定 PR 的详细信息
gh pr view 42
```

---

**基本写法：在浏览器中查看**
`gh pr view <编号> --web`
```bash
# 在浏览器中打开 PR 页面
gh pr view 42 --web
```

---

## PR 代码审查

**基本写法：查看 PR 差异**
`gh pr diff <编号>`
```bash
# 查看 PR 的代码差异
gh pr diff 42
```

---

**基本写法：查看变更文件列表**
`gh pr diff <编号> --name-only`
```bash
# 仅列出 PR 变更的文件名
gh pr diff 42 --name-only
```

---

**基本写法：检出 PR 到本地**
`gh pr checkout <编号>`
```bash
# 检出 PR 分支到本地进行测试
gh pr checkout 42
```

---

**基本写法：强制检出 PR**
`gh pr checkout <编号> --force`
```bash
# 有本地改动时强制检出 PR
gh pr checkout 42 --force
```

---

**基本写法：查看检查状态**
`gh pr checks <编号>`
```bash
# 查看 PR 的 CI 检查状态
gh pr checks 42
```

---

**基本写法：等待检查完成**
`gh pr checks <编号> --watch`
```bash
# 实时监控 PR 检查状态直到完成
gh pr checks 42 --watch
```

---

**基本写法：仅查看必需检查**
`gh pr checks <编号> --required`
```bash
# 仅显示必需通过的检查
gh pr checks 42 --required
```

---

## 提交审查

**基本写法：批准 PR**
`gh pr review <编号> --approve --body "<评论>"`
```bash
# 批准 PR 并附带评论
gh pr review 42 --approve --body "代码质量很好"
```

---

**基本写法：请求修改**
`gh pr review <编号> --request-changes --body "<意见>"`
```bash
# 请求修改并说明原因
gh pr review 42 --request-changes --body "需要补充单元测试"
```

---

**基本写法：评论 PR**
`gh pr review <编号> --comment --body "<评论>"`
```bash
# 仅评论不批准也不拒绝
gh pr review 42 --comment --body "建议优化命名"
```

---

**基本写法：添加行内评论**
`gh api repos/<owner>/<repo>/pulls/<编号>/reviews --input -`
```bash
# 通过 API 提交带行内评论的审查
gh api repos/owner/repo/pulls/42/reviews --input - <<'EOF'
{"event":"COMMENT","body":"总体不错","comments":[{"path":"src/app.js","line":42,"side":"RIGHT","body":"建议使用常量"}]}
EOF
```

---

## PR 评论

**基本写法：添加评论**
`gh pr comment <编号> --body "<评论>"`
```bash
# 在 PR 中添加评论
gh pr comment 42 --body "已修复请重新审查"
```

---

**基本写法：查看评论列表**
`gh api repos/<owner>/<repo>/issues/<编号>/comments`
```bash
# 通过 API 查看 PR 评论
gh api repos/owner/repo/issues/42/comments
```

---

## 合并 PR

**基本写法：合并 PR（默认方式）**
`gh pr merge <编号>`
```bash
# 合并指定 PR
gh pr merge 42
```

---

**基本写法：压缩合并**
`gh pr merge <编号> --squash`
```bash
# 使用 squash 方式合并 PR
gh pr merge 42 --squash
```

---

**基本写法：变基合并**
`gh pr merge <编号> --rebase`
```bash
# 使用 rebase 方式合并 PR
gh pr merge 42 --rebase
```

---

**基本写法：合并并删除分支**
`gh pr merge <编号> --squash --delete-branch`
```bash
# 合并 PR 后删除源分支
gh pr merge 42 --squash --delete-branch
```

---

**基本写法：自动合并**
`gh pr merge <编号> --auto --squash`
```bash
# 检查通过后自动合并
gh pr merge 42 --auto --squash
```

---

## PR 状态管理

**基本写法：关闭 PR**
`gh pr close <编号>`
```bash
# 关闭指定 PR
gh pr close 42
```

---

**基本写法：关闭并添加评论**
`gh pr close <编号> --comment "<评论>"`
```bash
# 关闭 PR 并附带说明
gh pr close 42 --comment "不再需要此功能"
```

---

**基本写法：重新打开 PR**
`gh pr reopen <编号>`
```bash
# 重新打开已关闭的 PR
gh pr reopen 42
```

---

**基本写法：草稿转就绪**
`gh pr ready <编号>`
```bash
# 将草稿 PR 标记为就绪状态
gh pr ready 42
```

---

**基本写法：就绪转草稿**
`gh pr ready <编号> --undo`
```bash
# 将就绪 PR 转回草稿状态
gh pr ready 42 --undo
```

---

**基本写法：更新 PR 分支**
`gh pr update-branch <编号>`
```bash
# 用基础分支更新 PR 分支
gh pr update-branch 42
```

---

**基本写法：编辑 PR**
`gh pr edit <编号> --add-label "<标签>"`
```bash
# 为 PR 添加标签
gh pr edit 42 --add-label "优先级高"
```

---

**基本写法：添加审查人**
`gh pr edit <编号> --add-reviewer <用户>`
```bash
# 为 PR 添加审查人
gh pr edit 42 --add-reviewer alice
```



<!-- ============ 文档分隔线：004-github/048-GhIssueManage.md ============ -->


## 创建 Issue

**基本写法：交互式创建 Issue**
`gh issue create`
```bash
# 通过交互式提示创建 Issue
gh issue create
```

---

**基本写法：指定标题和正文**
`gh issue create --title "<标题>" --body "<正文>"`
```bash
# 直接指定 Issue 标题和描述
gh issue create --title "Bug: 登录页面报错" --body "点击登录按钮无响应"
```

---

**基本写法：从文件读取正文**
`gh issue create --title "<标题>" --body-file <文件>`
```bash
# 从文件读取 Issue 正文内容
gh issue create --title "性能优化" --body-file issue-template.md
```

---

**基本写法：指定指派人**
`gh issue create --assignee <用户>`
```bash
# 创建 Issue 并指派处理人
gh issue create --title "修复 bug" --assignee @me
```

---

**基本写法：添加标签**
`gh issue create --label "<标签>"`
```bash
# 创建 Issue 并添加标签
gh issue create --title "新功能" --label "enhancement"
```

---

**基本写法：指定里程碑**
`gh issue create --milestone "<里程碑>"`
```bash
# 创建 Issue 并关联里程碑
gh issue create --title "任务" --milestone "v1.0"
```

---

**基本写法：在浏览器中创建**
`gh issue create --web`
```bash
# 打开浏览器创建 Issue
gh issue create --web
```

---

## 查看 Issue

**基本写法：列出当前仓库 Issue**
`gh issue list`
```bash
# 列出当前仓库的 Issue
gh issue list
```

---

**基本写法：列出指定状态**
`gh issue list --state <状态>`
```bash
# 列出指定状态的 Issue
gh issue list --state open
```

---

**基本写法：列出已关闭 Issue**
`gh issue list --state closed`
```bash
# 列出已关闭的 Issue
gh issue list --state closed
```

---

**基本写法：查看指派给自己的 Issue**
`gh issue list --assignee @me`
```bash
# 列出指派给自己的 Issue
gh issue list --assignee @me
```

---

**基本写法：查看自己创建的 Issue**
`gh issue list --author @me`
```bash
# 列出自己创建的 Issue
gh issue list --author @me
```

---

**基本写法：按标签筛选**
`gh issue list --label "<标签>"`
```bash
# 按标签筛选 Issue
gh issue list --label "bug"
```

---

**基本写法：限制返回数量**
`gh issue list --limit <数量>`
```bash
# 限制返回的 Issue 数量
gh issue list --limit 30
```

---

**基本写法：查看 Issue 详情**
`gh issue view <编号>`
```bash
# 查看指定 Issue 的详细信息
gh issue view 42
```

---

**基本写法：在浏览器中查看**
`gh issue view <编号> --web`
```bash
# 在浏览器中打开 Issue 页面
gh issue view 42 --web
```

---

**基本写法：查看 Issue 评论**
`gh issue view <编号> --comments`
```bash
# 查看 Issue 及其评论内容
gh issue view 42 --comments
```

---

## Issue 评论

**基本写法：添加评论**
`gh issue comment <编号> --body "<评论>"`
```bash
# 在 Issue 中添加评论
gh issue comment 42 --body "已复现此问题"
```

---

**基本写法：从文件读取评论**
`gh issue comment <编号> --body-file <文件>`
```bash
# 从文件读取评论内容
gh issue comment 42 --body-file comment.md
```

---

**基本写法：编辑评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X PATCH -f body="<新内容>"`
```bash
# 通过 API 编辑指定评论
gh api repos/owner/repo/issues/comments/123 -X PATCH -f body="更新后的评论"
```

---

**基本写法：删除评论**
`gh api repos/<owner>/<repo>/issues/comments/<评论ID> -X DELETE`
```bash
# 通过 API 删除指定评论
gh api repos/owner/repo/issues/comments/123 -X DELETE
```

---

## Issue 状态管理

**基本写法：关闭 Issue**
`gh issue close <编号>`
```bash
# 关闭指定 Issue
gh issue close 42
```

---

**基本写法：关闭并添加评论**
`gh issue close <编号> --comment "<评论>"`
```bash
# 关闭 Issue 并附带说明
gh issue close 42 --comment "已在 v1.2 修复"
```

---

**基本写法：关闭并指定原因**
`gh issue close <编号> --reason <原因>`
```bash
# 关闭 Issue 并指定关闭原因
gh issue close 42 --reason "not planned"
```

---

**基本写法：重新打开 Issue**
`gh issue reopen <编号>`
```bash
# 重新打开已关闭的 Issue
gh issue reopen 42
```

---

## 编辑 Issue

**基本写法：修改标题**
`gh issue edit <编号> --title "<新标题>"`
```bash
# 修改 Issue 标题
gh issue edit 42 --title "Bug: 登录页面 500 错误"
```

---

**基本写法：修改正文**
`gh issue edit <编号> --body "<新正文>"`
```bash
# 修改 Issue 正文内容
gh issue edit 42 --body "更新后的描述"
```

---

**基本写法：添加标签**
`gh issue edit <编号> --add-label "<标签>"`
```bash
# 为 Issue 添加标签
gh issue edit 42 --add-label "优先级高"
```

---

**基本写法：移除标签**
`gh issue edit <编号> --remove-label "<标签>"`
```bash
# 移除 Issue 的标签
gh issue edit 42 --remove-label "优先级高"
```

---

**基本写法：添加指派人**
`gh issue edit <编号> --add-assignee <用户>`
```bash
# 为 Issue 添加处理人
gh issue edit 42 --add-assignee alice
```

---

**基本写法：移除指派人**
`gh issue edit <编号> --remove-assignee <用户>`
```bash
# 移除 Issue 的处理人
gh issue edit 42 --remove-assignee alice
```

---

## 批量操作

**基本写法：批量关闭 Issue**
`gh issue list --label "<标签>" --json number --jq ".[].number" | xargs -I {} gh issue close {}`
```bash
# 批量关闭指定标签的 Issue
gh issue list --label "wontfix" --json number --jq ".[].number" | xargs -I {} gh issue close {}
```

---

**基本写法：批量添加标签**
`gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"`
```bash
# 为所有打开的 Issue 添加标签
gh issue list --state open --json number --jq ".[].number" | xargs -I {} gh issue edit {} --add-label "需要审查"
```

---

## Issue 传输与开发

**基本写法：将 Issue 转为分支开发**
`gh issue develop <编号>`
```bash
# 基于 Issue 创建开发分支
gh issue develop 42
```

---

**基本写法：指定分支名开发**
`gh issue develop <编号> -b <分支名>`
```bash
# 为 Issue 创建指定名称的分支
gh issue develop 42 -b fix/login-error
```

---

**基本写法：查看 Issue 关联的 PR**
`gh issue view <编号> --json trackedIssues`
```bash
# 查看 Issue 关联的追踪问题
gh issue view 42 --json trackedIssues
```

---

## JSON 输出

**基本写法：输出 JSON 格式**
`gh issue list --json <字段>`
```bash
# 以 JSON 格式输出指定字段
gh issue list --json number,title,state
```

---

**基本写法：使用 jq 过滤**
`gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"`
```bash
# 使用 jq 过滤标题含 bug 的 Issue
gh issue list --json number,title | jq ".[] | select(.title | contains(\"bug\"))"
```

---

**基本写法：使用模板输出**
`gh issue list --template "<模板>"`
```bash
# 使用 Go 模板自定义输出格式
gh issue list --template "{{range .}}#{{.number}} {{.title}}{{end}}"
```



<!-- ============ 文档分隔线：004-github/049-GhRepoManage.md ============ -->


## 创建仓库

**基本写法：创建公开仓库**
`gh repo create <仓库名> --public`
```bash
# 创建公开仓库
gh repo create myproject --public
```

---

**基本写法：创建私有仓库**
`gh repo create <仓库名> --private`
```bash
# 创建私有仓库
gh repo create myproject --private
```

---

**基本写法：创建并克隆**
`gh repo create <仓库名> --clone`
```bash
# 创建仓库并克隆到本地
gh repo create myproject --public --clone
```

---

**基本写法：从本地目录创建远程仓库**
`gh repo create <仓库名> --source <目录> --push`
```bash
# 基于本地目录创建远程仓库并推送
gh repo create myproject --source . --push
```

---

**基本写法：指定组织创建**
`gh repo create <组织>/<仓库名>`
```bash
# 在指定组织下创建仓库
gh repo create myorg/myproject --private
```

---

**基本写法：创建并添加描述**
`gh repo create <仓库名> --description "<描述>"`
```bash
# 创建仓库并添加描述
gh repo create myproject --description "我的项目"
```

---

**基本写法：创建带 README 的仓库**
`gh repo create <仓库名> --add-readme`
```bash
# 创建仓库并自动添加 README
gh repo create myproject --public --add-readme
```

---

## 查看仓库

**基本写法：查看当前仓库**
`gh repo view`
```bash
# 查看当前目录对应的仓库信息
gh repo view
```

---

**基本写法：查看指定仓库**
`gh repo view <owner>/<repo>`
```bash
# 查看指定仓库的详情
gh repo view facebook/react
```

---

**基本写法：在浏览器中查看**
`gh repo view --web`
```bash
# 在浏览器中打开仓库页面
gh repo view --web
```

---

**基本写法：查看仓库 README**
`gh repo view <owner>/<repo>`
```bash
# 查看 README 内容
gh repo view microsoft/vscode
```

---

**基本写法：列出自己的仓库**
`gh repo list`
```bash
# 列出自己账户下的仓库
gh repo list
```

---

**基本写法：列出指定用户仓库**
`gh repo list <用户名>`
```bash
# 列出指定用户的公开仓库
gh repo list torvalds
```

---

**基本写法：列出组织仓库**
`gh repo list <组织名>`
```bash
# 列出指定组织的仓库
gh repo list microsoft
```

---

**基本写法：限制返回数量**
`gh repo list --limit <数量>`
```bash
# 限制返回的仓库数量
gh repo list --limit 100
```

---

**基本写法：按语言筛选**
`gh repo list --language <语言>`
```bash
# 按编程语言筛选仓库
gh repo list --language TypeScript
```

---

## 克隆与 Fork

**基本写法：克隆仓库**
`gh repo clone <owner>/<repo>`
```bash
# 克隆指定仓库到本地
gh repo clone facebook/react
```

---

**基本写法：克隆当前仓库**
`gh repo clone`
```bash
# 克隆当前目录对应的仓库
gh repo clone
```

---

**基本写法：克隆到指定目录**
`gh repo clone <owner>/<repo> <目录>`
```bash
# 克隆仓库到指定目录名
gh repo clone facebook/react myreact
```

---

**基本写法：Fork 仓库**
`gh repo fork <owner>/<repo>`
```bash
# Fork 指定仓库到自己的账户
gh repo fork facebook/react
```

---

**基本写法：Fork 并克隆**
`gh repo fork <owner>/<repo> --clone`
```bash
# Fork 仓库并克隆到本地
gh repo fork facebook/react --clone
```

---

**基本写法：Fork 并添加远程**
`gh repo fork <owner>/<repo> --remote`
```bash
# Fork 仓库并自动添加原仓库为 upstream
gh repo fork facebook/react --remote
```

---

**基本写法：指定 upstream 名称**
`gh repo fork <owner>/<repo> --remote --remote-name <名称>`
```bash
# Fork 并自定义 upstream 远程名
gh repo fork facebook/react --remote --remote-name upstream
```

---

## 仓库编辑

**基本写法：修改仓库描述**
`gh repo edit --description "<描述>"`
```bash
# 修改当前仓库的描述
gh repo edit --description "更新后的项目描述"
```

---

**基本写法：修改主页 URL**
`gh repo edit --homepage "<URL>"`
```bash
# 设置仓库的主页地址
gh repo edit --homepage "https://myproject.com"
```

---

**基本写法：修改可见性为私有**
`gh repo edit --visibility private`
```bash
# 将仓库改为私有
gh repo edit --visibility private
```

---

**基本写法：修改可见性为公开**
`gh repo edit --visibility public`
```bash
# 将仓库改为公开
gh repo edit --visibility public
```

---

**基本写法：启用 Issues 功能**
`gh repo edit --enable-issues`
```bash
# 启用仓库的 Issues 功能
gh repo edit --enable-issues
```

---

**基本写法：启用 Wiki 功能**
`gh repo edit --enable-wiki`
```bash
# 启用仓库的 Wiki 功能
gh repo edit --enable-wiki
```

---

**基本写法：添加话题**
`gh repo edit --add-topic <话题>`
```bash
# 为仓库添加话题标签
gh repo edit --add-topic "javascript"
```

---

**基本写法：移除话题**
`gh repo edit --remove-topic <话题>`
```bash
# 移除仓库的话题标签
gh repo edit --remove-topic "javascript"
```

---

## 仓库同步与删除

**基本写法：同步 Fork**
`gh repo sync`
```bash
# 同步 Fork 仓库与上游
gh repo sync
```

---

**基本写法：同步指定 Fork**
`gh repo sync <owner>/<repo>`
```bash
# 同步指定的 Fork 仓库
gh repo sync myname/react
```

---

**基本写法：同步指定分支**
`gh repo sync --source <源> --branch <分支>`
```bash
# 从指定源同步指定分支
gh repo sync --source upstream --branch main
```

---

**基本写法：删除仓库**
`gh repo delete <仓库名>`
```bash
# 删除指定仓库（需确认）
gh repo delete myproject
```

---

**基本写法：删除当前仓库**
`gh repo delete`
```bash
# 删除当前目录对应的仓库
gh repo delete
```

---

**基本写法：强制删除不确认**
`gh repo delete <仓库名> --yes`
```bash
# 跳过确认直接删除
gh repo delete myproject --yes
```

---

## 归档与传输

**基本写法：归档仓库**
`gh repo archive <仓库名>`
```bash
# 将仓库设为只读归档状态
gh repo archive myproject
```

---

**基本写法：归档当前仓库**
`gh repo archive`
```bash
# 归档当前目录对应的仓库
gh repo archive
```

---

**基本写法：取消归档**
`gh repo unarchive <仓库名>`
```bash
# 取消仓库的归档状态
gh repo unarchive myproject
```

---

**基本写法：转移仓库**
`gh repo transfer <仓库> <新所有者>`
```bash
# 将仓库转移给其他用户或组织
gh repo transfer myproject myorg
```

---

## 仓库部署与发布

**基本写法：创建 Release**
`gh release create <标签名>`
```bash
# 基于标签创建发布
gh release create v1.0.0
```

---

**基本写法：创建带说明的 Release**
`gh release create <标签名> --title "<标题>" --notes "<说明>"`
```bash
# 创建发布并指定标题和说明
gh release create v1.0.0 --title "v1.0.0 正式版" --notes "首个正式版本"
```

---

**基本写法：上传附件到 Release**
`gh release upload <标签名> <文件>`
```bash
# 上传构建产物到指定发布
gh release upload v1.0.0 ./dist/app.zip
```

---

**基本写法：查看 Release 列表**
`gh release list`
```bash
# 列出仓库的所有发布
gh release list
```

---

**基本写法：下载 Release 资源**
`gh release download <标签名>`
```bash
# 下载指定发布的所有资源
gh release download v1.0.0
```

---

**基本写法：删除 Release**
`gh release delete <标签名>`
```bash
# 删除指定的发布
gh release delete v1.0.0
```



<!-- ============ 文档分隔线：004-github/050-GhRelease.md ============ -->



## 开篇：把发布当成一场新专辑发布会

想象你是一位歌手，写完了整张专辑的歌曲（代码写完了），现在准备正式发行。发行不是把歌往网上一扔就完事，而是一场"发布会"：

- 你要起一个版本号（比如"第三张专辑"），对应代码里的**标签（tag）**；
- 你要写一段"专辑介绍"（发布说明 Release Notes），告诉大家这版有哪些新歌、修了哪些问题；
- 你要把实体唱片和周边（**构建产物**，如安装包、压缩包）摆上货架；
- 粉丝（用户）来下载、反馈，必要时你还要发"加印版"（补传文件）甚至"召回"（删除发布）。

GitHub 的 **Release（发布）** 就是软件世界的"新专辑发布会"。`gh release` 系列命令，就是让你**不开网页、只敲键盘**就能完成整场发布会。

---

## 旅程地图：从代码到正式发布的 6 站

把发布看成一段旅程，`gh release` 的每个子命令对应一站：

| 站点 | 做什么 | 对应命令 |
| --- | --- | --- |
| 第 1 站 | 打版本号（标签）+ 写发布会文案 + 创建发布 | `gh release create` |
| 第 2 站 | 看看历史上有过哪些发布、详情如何 | `gh release list` / `gh release view` |
| 第 3 站 | 把安装包、压缩包等产物上传或下载 | `gh release upload` / `gh release download` |
| 第 4 站 | 补充说明、修正标题、撤回草稿 | `gh release edit` |
| 第 5 站 | 删除发布（可连标签一起删） | `gh release delete` |
| 第 6 站 | 用 JSON 输出对接脚本自动化 | 各命令的 `--json` / `--jq` 选项 |

下面我们一站一站走完这段旅程。**强烈建议**你先在终端执行 `gh auth login` 完成登录（见《GhCliAuth》文档），并在一个你自己的仓库里实际演练。

---

## 原理先讲清：Release 与 Tag 是什么关系

很多初学者把 Release 和 Tag 混为一谈，先厘清概念：

- **Tag（标签）**：Git 里的一个"书签"，标记某一次提交（commit）。它轻量、只是代码层面的记号。你可以用 `git tag v1.0.0` 打标签。
- **Release（发布）**：GitHub 在 Tag 基础上包装出来的一层"展示与分发"功能。它包含发布标题、说明文字、附件（二进制文件），还会生成一个下载页面。

用专辑类比：Tag 相当于"这张专辑的母带编号"，Release 相当于"摆在商店里的正式商品（含封面、内页文案、周边）"。

`gh release create` 有一个贴心行为：**如果指定的 Tag 还不存在，它会自动帮你从默认分支的最新状态创建这个 Tag**。如果你想从别的分支或某次具体提交发布，用 `--target` 指定。

发布创建成功后，本地仓库可能还没有这个新 Tag，需要执行 `git fetch --tags origin` 把它拉下来。

---

## 第 1 站：创建发布（gh release create）

`gh release create` 是最核心的命令，基本格式：

```bash
gh release create [<标签>] [<文件>... | <模式>...]
```

### 1.1 最简方式：交互式创建

```bash
# 不带任何参数，gh 会像向导一样一步步问你：选哪个标签、写什么说明
gh release create
```

### 1.2 非交互式：一步到位

```bash
# 用 v1.2.3 作为标签，附上发布说明
gh release create v1.2.3 --notes "bugfix release"

# 用 GitHub 的 Release Notes API 自动生成更新日志（自动对比上次发布以来的提交）
gh release create v1.2.3 --generate-notes

# 从文件读取发布说明（适合说明很长、提前写好的场景）
gh release create v1.2.3 -F release-notes.md

# 从标签注解或对应提交信息读取发布说明
gh release create v1.2.3 --notes-from-tag
```

### 1.3 控制发布属性

```bash
# 标记为预发布（测试版，页面上会特殊提示）
gh release create v1.3.0-beta.1 --prerelease --notes "测试版本"

# 先存为草稿，不对外可见，确认无误后再编辑发布
gh release create v1.2.3 --draft

# 明确指定本次发布不作为 "Latest（最新版）"
gh release create v1.2.3 --latest=false

# 指定从 develop 分支（或某次提交 SHA）创建自动 Tag
gh release create v1.2.3 --target develop --notes "从 develop 分支发布"

# 校验 Tag 必须已存在于远端，否则中止（防止误建新 Tag）
gh release create v1.2.3 --verify-tag --notes "已打好的标签"

# 只有自上次发布以来有新提交才创建，否则报错退出（避免重复发布）
gh release create v1.2.3 --fail-on-no-commits
```

### 1.4 顺便上传构建产物

创建发布时可以**同时**上传产物（相当于发布会现场直接摆货）：

```bash
# 把 dist 目录下所有 tgz 包作为附件上传
gh release create v1.2.3 ./dist/*.tgz

# 给附件起一个"显示名"，用 # 分隔（下载页会显示这个友好名称）
gh release create v1.2.3 '/path/to/asset.zip#Windows 安装包'

# 发布的同时在仓库讨论区开一个新话题
gh release create v1.2.3 --discussion-category "General"
```

创建成功后，终端会打印类似输出：

```text
Created release v1.2.3 on owner/repo
https://github.com/owner/repo/releases/tag/v1.2.3
```

---

## 第 2 站：查看发布（gh release list / view）

发布完要检查成果，发布会也要让观众"回头翻录像"。

```bash
# 列出仓库所有发布（默认最新在前）
gh release list

# 只显示最近 5 条
gh release list --limit 5

# 查看某个具体发布的详情（说明文字、附件清单、发布时间等）
gh release view v1.2.3

# 不写标签名，默认查看"最新发布"
gh release view

# 在浏览器中打开发布页面
gh release view v1.2.3 --web

# 输出 JSON 供脚本处理（字段有 tagName、name、isDraft、assets 等）
gh release view v1.2.3 --json tagName,isDraft,assets

# 用 jq 语法只取附件名
gh release view v1.2.3 --jq '.assets[].name'
```

`gh release list` 的典型输出：

```text
TITLE           TAG       PRERELEASE  CREATED_AT
v1.2.3 正式版   v1.2.3                about 2 minutes ago
v1.2.2          v1.2.2                about 3 days ago
v1.3.0 测试版   v1.3.0-beta.1  是     about 1 week ago
```

---

## 第 3 站：上传与下载产物（gh release upload / download）

软件的"货"（安装包、文档包）往往是在发布之后才构建出来的，因此需要**补货**和**取货**。

### 3.1 上传（补货）

```bash
# 给已存在的 v1.2.3 发布追加一个文件
gh release upload v1.2.3 ./build/app.exe

# 上传多个文件（支持通配符）
gh release upload v1.2.3 ./build/*.dmg ./build/*.deb

# 同名文件已存在时，先覆盖再上传（--clobber 意为"覆盖"）
gh release upload v1.2.3 ./app.zip --clobber
```

### 3.2 下载（取货）

```bash
# 下载该发布的所有附件到当前目录
gh release download v1.2.3

# 只下载 zip 文件（--pattern 支持通配符）
gh release download v1.2.3 --pattern "*.zip"

# 下载到指定目录
gh release download v1.2.3 --dir ./downloads

# 下载"最新发布"的附件
gh release download --pattern "*.dmg"
```

下载完成后目录里会出现对应的文件，例如：

```mermaid
graph TD
  A["downloads/"] --> B["app-1.2.3-win-x64.zip"]
  A --> C["app-1.2.3-linux-x64.tar.gz"]
```

---

## 第 4 站：编辑发布（gh release edit）

发布会开完了，发现介绍里有个错别字，或者想把"测试版"转正：

```bash
# 修改标题与说明
gh release edit v1.2.3 --title "v1.2.3 正式版" --notes "更新说明：修复登录闪退"

# 从文件读取新的说明
gh release edit v1.2.3 -F new-notes.md

# 把已发布的版本收回为草稿（相当于"暂时下架"）
gh release edit v1.2.3 --draft

# 去掉预发布标记，正式转正
gh release edit v1.3.0-beta.1 --prerelease=false

# 改为最新发布
gh release edit v1.2.2 --latest
```

---

## 第 5 站：删除发布（gh release delete）

```bash
# 删除发布（--yes 跳过二次确认；注意：默认不会删除 Tag）
gh release delete v1.2.3 --yes

# 删除发布的同时清理对应的 Tag（--cleanup-tag）
gh release delete v1.2.3 --cleanup-tag --yes
```

> 注意：删除 Release 并不会自动删除 Git 标签，代码历史依然保留。是否连标签一起删，取决于你是否还想保留这个"版本记号"。

---

## 完整旅程串联：一次真实的发布脚本

把 6 站连起来，就是一个可复制的小脚本（以发布 Windows 版本为例）：

```bash
# 第 0 步：确认登录状态
gh auth status

# 第 1 步：构建产物
npm run build

# 第 2 步：自动创建发布 + 自动生成说明 + 上传安装包
gh release create v2.0.0 \
  --generate-notes \
  --title "v2.0.0 全新界面" \
  ./dist/app-win-x64.zip \
  ./dist/app-linux-x64.tar.gz

# 第 3 步：验证创建结果
gh release view v2.0.0 --json tagName,name,assets

# 第 4 步：补充漏传的说明文档
gh release upload v2.0.0 ./CHANGELOG.md --clobber

# 第 5 步：本地同步新标签
git fetch --tags origin
```

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 未登录就创建发布 | `To get started with GitHub CLI, please run: gh auth login` | 操作需要身份认证 | 先执行 `gh auth login` 完成登录 |
| 在错误目录执行 | `could not determine current repo` | gh 找不到当前仓库 | 先 `cd` 到仓库目录，或加 `-R owner/repo` 指定仓库 |
| 附件文件名含空格 | 报 `unexpected argument` 或上传失败 | 文件名被 shell 拆成多个参数 | 用引号包裹：`gh release upload v1.0.0 "my app.zip"` |
| 重复上传同名附件 | `failed to upload asset: already exists` | 附件已存在且未被覆盖 | 加 `--clobber` 覆盖，或先下载删除再传 |
| 想从非默认分支发布 | 自动创建的 Tag 指向 main | 忘了指定目标分支 | 加 `--target <branch>` 或指定提交 SHA |
| 发布后发现 Tag 不存在 | `release created but tag not found locally` | 新 Tag 只存在于远端 | 执行 `git fetch --tags origin` |
| 误删发布 | 页面找不到该版本 | `delete` 默认只删发布不删 Tag | 保留 Tag 可随时用 `gh release create <tag>` 重建发布；如已 `--cleanup-tag`，需用 `git push origin --tags` 重新推送标签 |

---

## 一句话记忆

**Release = 带说明、带附件的"货架商品"，`gh release create` 一键上架，`upload/download` 负责补货取货，`edit/delete` 负责售后。**



<!-- ============ 文档分隔线：004-github/051-GhWorkflow.md ============ -->



## 开篇：把 Workflow 想成工厂自动化流水线

想象一家饮料工厂。装瓶、贴标、装箱、码垛，每个环节都有机器在自动运转：原料一到（代码提交），传送带就启动，产品按顺序流向下一站，质检不合格的会被单独挑出来。这就是**自动化流水线**。

GitHub Actions 里的 **Workflow（工作流）** 就是这条流水线：它是一份 YAML 配置文件，里面写好了"什么事件发生时，按什么顺序跑哪些任务"。比如"每次有人提交代码，就自动跑测试、构建、发布"。

`gh workflow` 系列命令，就是给你一套**流水线控制台**：不开网页，就能在终端里查看流水线清单、手动按下启动按钮、给流水线传入原料参数、临时拉闸停线。

先明确一个概念：`gh workflow` 管理的是"流水线本身"（配置文件），而真正跑起来的"一批产品"叫做 **Run（运行实例）**，对应 `gh run` 系列命令。两者配合使用。

---

## 生命周期总览：运行一个 Workflow 的 5 个阶段

按一条流水线从"认识"到"退役"的生命周期，我们把 `gh workflow` 命令串起来：

| 阶段 | 你要做什么 | 对应命令 |
| --- | --- | --- |
| 阶段 1：认识流水线 | 看看仓库里有哪几条流水线、状态如何 | `gh workflow list` |
| 阶段 2：读懂流水线 | 查看某条流水线的定义与最近运行情况 | `gh workflow view` |
| 阶段 3：手动启动 | 按下启动按钮，传入选料参数 | `gh workflow run` |
| 阶段 4：跟踪运行 | 查看运行列表与单次运行的进度、日志 | `gh run list` / `gh run view` |
| 阶段 5：启停管理 | 临时禁用、恢复启用某条流水线 | `gh workflow disable` / `gh workflow enable` |

下面按这 5 个阶段逐步展开。**前提**：已 `gh auth login`，且仓库 `.github/workflows/` 目录下存在 workflow 文件（可参考《GitHubActionsCICD》《ActionsTrigger》文档）。

---

## 原理先讲清：Workflow 是被什么"启动"的

一条流水线要能被启动，必须回答两个问题：**谁来触发？怎么传参？**

- **触发方式（triggers）**：在 workflow 文件的 `on:` 字段里声明。常见的有 `push`（提交时）、`pull_request`（PR 时）、`schedule`（定时）、`workflow_dispatch`（手动触发）。**注意：`gh workflow run` 只能启动声明了 `workflow_dispatch` 的 workflow**——就像工厂只有装了"手动启动按钮"的产线才能被人工开动。

- **手动传参（inputs）**：在 `on.workflow_dispatch.inputs` 里声明参数，比如"发布环境（production/staging）""版本号"。声明之后，`gh workflow run` 才能通过 `-f` / `--json` 传入。

一个支持手动触发的最小示例（`deploy.yml`）：

```yaml
name: deploy                     # 流水线名称（可读名称，也可用文件名定位）
on:
  workflow_dispatch:             # 允许手动触发
    inputs:
      environment:               # 声明一个输入参数
        description: 部署环境
        required: true
        default: staging
      version:
        description: 发布版本
        required: false
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "部署 ${{ github.event.inputs.version }} 到 ${{ github.event.inputs.environment }}"
```

---

## 阶段 1：认识流水线（gh workflow list）

```bash
# 列出仓库中所有 workflow
gh workflow list

# 只查看已启用的流水线
gh workflow list --all=false   # 等价于 gh workflow list --active

# 在另一个仓库中查看
gh workflow list -R owner/repo
```

典型输出：

```text
NAME                          STATE    ID
deploy                        active   254321
test                          active   254322
nightly-report                disabled 254323
```

- `active`：已启用，事件到来会正常触发；
- `disabled`：已被禁用（可能被 `gh workflow disable` 或页面操作禁用）。

> 提示：`gh workflow list` 默认只显示**启用中**的 workflow，加 `--all` 才显示全部。

---

## 阶段 2：读懂流水线（gh workflow view）

想确认某条流水线的定义、最近几次运行是否健康：

```bash
# 查看某条 workflow 的摘要（按文件名/ID/名称定位）
gh workflow view deploy.yml

# 用数字 ID 定位（从 list 输出中取得）
gh workflow view 254321

# 直接看它的 YAML 定义内容
gh workflow view deploy.yml --yaml

# 查看指定分支/标签上的版本
gh workflow view deploy.yml --ref main

# 在浏览器中打开该 workflow 页面
gh workflow view deploy.yml --web

# 不带参数时，gh 会弹出列表让你交互选择
gh workflow view
```

`--yaml` 的输出就是仓库里的原始配置文件，适合快速核对"这条流水线到底配了什么"。

---

## 阶段 3：手动启动（gh workflow run）

这是最常用、也最容易出错的命令。它做的事情是：向 GitHub 发送一个 `workflow_dispatch` 事件，让流水线跑起来。

### 3.1 基础启动

```bash
# 按文件名启动（会使用远端默认分支上的 workflow 版本）
gh workflow run deploy.yml

# 带参数与分支指定
gh workflow run deploy.yml --ref my-branch
```

启动成功后，gh 会返回本次运行的信息；之后可用 `gh run watch` 实时观察进度，或用 `gh run list` 查看。

### 3.2 传入输入参数

```bash
# 用 -f 传字符串参数（key=value）
gh workflow run deploy.yml -f environment=production -f version=1.2.3

# 用 -F 传参数（值支持 @文件 语法，从文件读取）
gh workflow run deploy.yml -F config=@config.json

# 用标准输入传 JSON 参数（适合脚本自动化）
echo '{"environment":"production","version":"1.2.3"}' | gh workflow run deploy.yml --json
```

### 3.3 注意事项

- 目标 workflow 必须声明了 `on.workflow_dispatch`，否则会报错；
- 参数名必须与 `inputs` 中声明的键一致；
- 不传 `--ref` 时使用默认分支上的 workflow 文件版本。

---

## 阶段 4：跟踪运行（gh run list / view / watch）

流水线启动后，要看它跑到哪一步了。`gh run` 系列命令是"监控摄像头"：

```bash
# 查看最近运行记录
gh run list

# 只查看某条 workflow 的运行记录
gh run list --workflow deploy.yml

# 查看某次运行的详细状态（job 列表、结论）
gh run view 123456789

# 实时跟随某次运行，直到结束（按 Ctrl+C 可退出跟随）
gh run watch 123456789

# 直接看失败的步骤日志
gh run view 123456789 --log-failed
```

典型输出（`gh run list`）：

```text
STATUS  CONCLUSION TITLE           WORKFLOW   AGE
completed success   部署到 production deploy     3m ago
in_progress  -     部署到 production deploy     12s ago
completed failure   nightly-report nightly    1d ago
```

---

## 阶段 5：启停管理（gh workflow enable / disable）

```bash
# 临时禁用一条流水线（拉闸停线，事件到来也不会启动）
gh workflow disable deploy.yml

# 恢复启用
gh workflow enable deploy.yml

# 在其他仓库操作
gh workflow disable deploy.yml -R owner/repo
```

典型应用场景：

- 深夜发现发布流水线配置有问题，先 `disable` 止血；
- 暂停不重要的定时任务（如每日报告），降低资源消耗；
- 排查"为什么自动部署没触发"时，检查是否被 `disable`。

---

## 完整生命周期串联：一次实战演练

```bash
# 1. 认识：仓库里有哪几条流水线
gh workflow list

# 2. 读懂：查看 deploy 流水线的定义
gh workflow view deploy.yml --yaml

# 3. 启动：手动触发，传入环境与版本参数
gh workflow run deploy.yml -f environment=production -f version=2.1.0

# 4. 跟踪：列出最近运行，找到刚启动的那条
gh run list --workflow deploy.yml

# 5. 监控：实时跟随运行进度（替换为实际 run ID）
gh run watch 987654321

# 6. 维护：发现问题后临时禁用流水线
gh workflow disable deploy.yml

# 7. 恢复：修复后重新启用
gh workflow enable deploy.yml
```

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 对无 workflow_dispatch 的流水线执行 run | `workflow does not have "workflow_dispatch" trigger` | 目标 workflow 未声明手动触发 | 在 workflow 文件 `on:` 中增加 `workflow_dispatch:` 并提交 |
| 传入未声明的参数 | 运行记录中参数缺失或提示无法找到输入 | 参数名与 `inputs` 声明不一致 | 核对 `on.workflow_dispatch.inputs` 中的键名 |
| 传参时 shell 特殊字符出错 | 参数值被截断或报语法错误 | 值包含空格、`&` 等未加引号 | 用引号包裹：`-f msg="hello world"` |
| 在非仓库目录执行 | `could not determine current repo` | gh 无法确定当前仓库 | `cd` 进仓库目录，或加 `-R owner/repo` |
| 找不到 workflow | `no workflows found in repository` | 仓库没有 `.github/workflows/` 下有效文件 | 确认 YAML 文件名以 `.yml/.yaml` 结尾且语法正确 |
| 启动后看不到运行 | `gh run list` 无记录 | 刚触发尚未注册，或查看的 workflow 不对 | 稍等几秒重试，用 `--workflow <name>` 精确过滤 |
| 误禁用导致不触发 | 明明 push 了代码却没跑 | 流水线处于 disabled 状态 | `gh workflow list` 检查状态，用 `enable` 恢复 |

---

## 一句话记忆

**Workflow 是流水线配置文件，`gh workflow run` 是启动按钮（只对声明了 workflow_dispatch 的流水线有效），`list/view` 负责检查，`disable/enable` 负责拉闸与送电。**



<!-- ============ 文档分隔线：004-github/052-GhGist.md ============ -->



## 开篇：把 Gist 想成办公桌上的便利贴

办公室桌上有一种便利贴：不用建一个完整文件夹，随手撕一张，写上要点，贴在显示器边上，或者撕下来递给同事，大家都能看到。它轻、快、随处可贴，用完还能撕掉。

**Gist（代码片段）** 就是 GitHub 上的"便利贴"：不用建仓库、不用写 README，直接把一段代码、一段配置、一段笔记贴上去，立刻获得一个链接，发给任何人就能看。你可以贴公开的（谁都能搜到），也可以贴私密的（只有有链接的人能看到）。

`gh gist` 系列命令，让你**在终端里直接写便利贴、贴便利贴、翻便利贴**，全程不用开浏览器。

---

## 原理先讲清：Gist 与仓库有什么不同

| 对比项 | Gist | 普通仓库 |
| --- | --- | --- |
| 定位 | 片段级（一段代码/一个文件） | 项目级（完整工程） |
| 创建成本 | 一条命令/一次粘贴 | 需要 init、clone、push 等 |
| 是否走 Git | 是（每个 Gist 本身就是一个微型仓库，支持克隆、提交） | 是 |
| 公开范围 | 公开（可被搜索）或私密（仅链接可见，不可搜索） | public/private |
| 适合场景 | 分享片段、临时笔记、配置备份 | 正式项目协作 |

特别提醒一个容易搞反的点：**`gh gist create` 默认创建的是"私密（secret）"Gist**，想公开必须显式加 `--public`。私密不等于绝对保密——它只是"不在搜索中公开"，任何拿到链接的人都能看。

---

## 场景 1：快速分享代码（分享给朋友/论坛/同事）

你在写代码时遇到一个报错，想把报错相关的几行代码发给论坛求助，或者把一个小技巧分享到群里。Gist 是最合适的载体。

### 1.1 创建并公开分享

```bash
# 把一个文件发布为公开 gist（公开 = 可被搜索）
gh gist create --public hello.py

# 加上描述，方便对方一眼看懂
gh gist create hello.py -d "我的第一个 Python 程序"

# 多个文件打包成一个 gist（比如一个需求 + 对应脚本）
gh gist create solve.py README.md

# 用通配符一次选择多个文件
gh gist create *.md *.txt

# 创建后立刻在浏览器打开（--web）
gh gist create --public hello.py -d "分享片段" --web
```

### 1.2 从标准输入创建（不需要先存文件）

有时候内容就在终端里（比如上一条命令的输出），可以直接"管道"给 gist：

```bash
# 把命令输出直接变成 gist（cat 文件内容管道给 gh）
cat cool.txt | gh gist create

# 手动粘贴内容，-f 指定文件名（否则会没有文件名）
echo "console.log('hello')" | gh gist create -f script.js

# 从标准输入创建并加描述
printf 'def add(a, b):\n    return a + b\n' | gh gist create -f add.py -d "加法函数"
```

### 1.3 拿到链接

创建成功后终端会打印类似输出：

```text
- https://gist.github.com/fanquanpp/8f1a2b3c4d5e6f7a8b9c0d1e
```

把这个链接发给对方即可。对方可以看、可以克隆，甚至可以基于它继续编辑（权限允许时）。

---

## 场景 2：个人笔记与配置备份（给自己留底）

每个人的终端都有一堆"宝贝配置"：`.bashrc` 的别名、`.vimrc`、某段数据库 SQL、某个环境变量清单。把它们丢进私密 Gist，等于给自己建了一个**云端口袋本**——换电脑、换环境时一条命令取回。

### 2.1 创建私密备份

```bash
# 默认就是私密（secret），适合存个人配置
gh gist create .bashrc -d "我的 bash 配置备份"

# 明确强调私密：加 --public=false 或者干脆不加 --public 即可
gh gist create my_sql_notes.sql -d "常用 SQL 备忘"
```

### 2.2 列出与查看自己的片段

```bash
# 列出我所有 gist（最近在前）
gh gist list

# 限制显示条数
gh gist list --limit 20

# 查看某个 gist 的内容
gh gist view 8f1a2b3c4d5e6f7a8b9c0d1e

# 只查看其中某一个文件（多文件 gist 时很有用）
gh gist view 8f1a2b3c4d5e6f7a8b9c0d1e --filename .bashrc

# 列出 gist 里有哪些文件
gh gist view 8f1a2b3c4d5e6f7a8b9c0d1e --files

# 看原始内容（不做任何渲染美化，适合管道给其他命令）
gh gist view 8f1a2b3c4d5e6f7a8b9c0d1e --raw
```

`gh gist list` 典型输出：

```text
ID                  DESCRIPTION         FILES  VISIBILITY  UPDATED
8f1a2b3c4d5e6f7a8b9c0d1e  我的 bash 配置备份  1      secret      2 minutes ago
1a2b3c4d5e6f7a8b9c0d1e2f  面试算法题整理      3      public      3 days ago
```

### 2.3 恢复备份（克隆到本地）

```bash
# 把 gist 克隆为本地目录（它本质是个 git 仓库）
gh gist clone 8f1a2b3c4d5e6f7a8b9c0d1e my-dotfiles

# 克隆后就是一个普通 git 仓库，可以提交修改再推回
cd my-dotfiles
cp ~/.bashrc .
git add .bashrc
git commit -m "更新配置"
git push
```

---

## 场景 3：代码片段管理与复用（维护自己的片段库）

片段攒多了就要整理：改内容、重命名文件、删掉过时的。这就是"便利贴的日常维护"。

### 3.1 编辑内容

```bash
# 编辑 gist 内容（默认会用编辑器打开，可逐行修改）
gh gist edit 8f1a2b3c4d5e6f7a8b9c0d1e

# 直接用本地文件的内容替换 gist 中的同名文件
gh gist edit 8f1a2b3c4d5e6f7a8b9c0d1e new_content.py
```

### 3.2 重命名文件

```bash
# 把 gist 里的 old.js 改名为 new.js
gh gist rename 8f1a2b3c4d5e6f7a8b9c0d1e old.js new.js
```

### 3.3 删除过时片段

```bash
# 删除 gist（--yes 跳过确认；删除不可恢复，谨慎操作）
gh gist delete 8f1a2b3c4d5e6f7a8b9c0d1e --yes
```

### 3.4 在浏览器中管理

```bash
# 在浏览器打开某个 gist
gh gist view 8f1a2b3c4d5e6f7a8b9c0d1e --web

# 打开你自己的全部 gist 列表页
gh gist list --web
```

---

## 三个场景的命令地图

| 场景 | 核心动作 | 用到的命令 |
| --- | --- | --- |
| 分享代码 | 创建公开片段、拿链接 | `create --public`、`create -f`（stdin） |
| 备份笔记 | 存私密片段、翻查、取回 | `create`、`list`、`view`、`clone` |
| 管理复用 | 改内容、改名、删除 | `edit`、`rename`、`delete`、`view --web` |

---

## 进阶技巧：让 Gist 更好用

### 技巧 1：Gist 也是一个 Git 仓库

每个 Gist 底层就是一个微型 Git 仓库，因此 Git 的版本历史、分支、评论功能都适用：

```bash
# 克隆后查看提交历史（每次编辑都是一次提交）
gh gist clone 8f1a2b3c4d5e6f7a8b9c0d1e snippet
cd snippet
git log --oneline

# 拉取最新修改（别人在你的 gist 上提交后）
git pull
```

### 技巧 2：用 --json 配合脚本化统计

```bash
# 输出 JSON 格式的 gist 列表（字段：id、description、files、visibility 等）
gh gist list --json id,description,files

# 统计公开 gist 数量
gh gist list --json visibility --jq '[.[] | select(.visibility == "public")] | length'
```

### 技巧 3：Gist 可以嵌入网页

公开 Gist 支持嵌入（embed），把创建成功后得到的 `<script src="https://gist.github.com/...js"></script>` 代码粘贴到网页/博客/笔记软件中，就能直接展示代码片段——很多技术博客的代码就是这么来的。

### 技巧 4：命名规范建议

- 描述（`-d`）必填：不加描述的 gist 在列表里很难辨认；
- 文件名带后缀：`.py`、`.js`、`.md` 等后缀决定语法高亮，从 stdin 创建时务必用 `-f` 指定；
- 前缀分类：私密片段可用 `todo-`、`conf-`、`note-` 之类前缀，配合 `list --json files` 便于检索。

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 以为默认是公开，结果别人搜不到 | 明明分享出去了却搜不到 | `create` 默认私密（secret） | 需要公开时显式加 `--public` |
| 以为私密=绝对保密 | 链接泄露后被无关人看到 | 私密只是不可搜索，知道链接即可访问 | 不要把私密 gist 当保险箱，敏感信息用 Secret 管理 |
| 从 stdin 创建忘了给文件名 | 生成的 gist 没有文件或文件名怪异 | `-f` 指定文件名 | `echo ... \| gh gist create -f name.py` |
| 把整个目录当参数传 | 报 `no such file or directory` | gist 不是目录，只收文件 | 逐个/通配符列出文件：`gh gist create a.py b.py` |
| view 看不到内容 | 输出为空或提示选择 | 多文件 gist 默认不打印全部 | 用 `--files` 先看清单，再 `--filename` 指定文件 |
| 删除后后悔 | 片段找不回来了 | `delete` 不可恢复 | 删除前先 `clone` 到本地留底；必要时在 Gist 网页端也可能找回（GitHub 支持从垃圾箱恢复，时间有限） |
| 无权限编辑他人 gist | `not found` 或权限错误 | 只能编辑自己的 gist | 对他人片段先 `clone` 修改再作为新 gist 创建 |

---

## 一句话记忆

**Gist 是 GitHub 的"便利贴"：`create` 写贴纸（默认私密，`--public` 才公开），`view/list` 翻贴纸，`edit/rename/delete` 整理贴纸，`clone` 把贴纸变成正式文件。**



<!-- ============ 文档分隔线：004-github/053-GhExtension.md ============ -->



## 开篇：把扩展想成手机 App 应用商店

你的手机出厂时只带系统应用（打电话、发短信、拍照）。但真正让它"强大"的，是你从**应用商店**里安装的各种 App：记账的、修图的、看天气的。每一个 App 都是第三方开发者做好、上传到商店的，你一键安装即可使用，不满意就卸载，更新了版本就升级。

**gh（GitHub CLI）扩展（Extension）** 完全同理：gh 出厂时只有一套内置命令（`gh repo`、`gh issue`、`gh pr` 等），但这套"系统"开放了一个**扩展机制**——任何人都能开发一个小工具，把它做成仓库发布到 GitHub，其他人就能像装 App 一样安装它，获得一个全新的 `gh xxx` 子命令。

本文以"逛商店 → 安装 → 管理 → 开发"的 App 使用动线为线索，带你玩转 `gh extension`。

---

## 原理先讲清：扩展到底是什么

### 2.1 命名规则与工作机制

一个扩展本质上是一个 **GitHub 仓库**，有两个硬性要求：

- 仓库名必须以 `gh-` 开头（如 `gh-dash`）；
- 仓库内必须有一个**与仓库同名的可执行文件**（如 `gh-dash` 这个脚本或编译产物）。

安装后，你在终端敲 `gh dash`，gh 会找到名为 `gh-dash` 的可执行文件，并把**后续的所有参数原样转发**给它。整个过程就像：你的"系统"（gh）多了一个新按钮，按下后由"App"（扩展）处理。

### 2.2 两种扩展形态

| 形态 | 说明 | 例子 |
| --- | --- | --- |
| 脚本扩展（script extension） | 仓库根目录放一个同名可执行脚本（Bash、Python 等），gh 直接把仓库克隆下来用 | 大多数社区小工具 |
| 预编译扩展（precompiled extension） | 发布时把编译好的二进制作为 Release 附件上传，gh 优先下载 Release 附件，速度更快 | 大型 Go 编写的工具 |

gh 安装远端仓库时会先检查：有没有 Release 二进制？有，按预编译扩展处理；没有，就克隆仓库当脚本扩展处理。

### 2.3 安全提示（必须知道）

- **扩展不是 GitHub 官方验证、签名或背书的**。安装和升级扩展，等于信任它的发布者。
- 官方文档明确提示：安装前应自己审查扩展的源码和来源（`gh extension browse <名字>` 直接看仓库）。
- 扩展会定期（每 24 小时）检查新版本并提示升级，可通过环境变量关闭提示（详见 `gh help environment`）。
- 扩展**不能覆盖** gh 的内置命令；若名字与内置命令冲突，可用 `gh extension exec <名字>` 强制调用。

扩展生态的官方发现入口：https://github.com/topics/gh-extension

---

## 第 1 步：逛商店（gh extension search / browse）

装 App 前先逛逛商店，看看有什么好东西。

```bash
# 按关键词搜索扩展
gh extension search notify

# 搜索 dash（仪表盘类工具）
gh extension search dashboard

# 在浏览器中打开扩展仓库主页（浏览源码、看说明、看 star 数）
gh extension browse gh-dash

# browse 也接受完整的 owner/repo 格式
gh extension browse dlvhdr/gh-dash
```

`gh extension search` 会返回扩展名与描述，例如：

```text
dlvhdr/gh-dash
A beautiful CLI dashboard for GitHub
github.com/nektos/gh-act  (这类工具常被社区扩展化)
...
```

> 提示：`gh extension search` 并非搜索所有 GitHub 仓库，而是基于 GitHub 搜索过滤"扩展类"仓库；更全面的发现方式是在网页端搜索 `topic:gh-extension`。

---

## 第 2 步：安装（gh extension install）

```bash
# 最常用：按 owner/repo 格式安装
gh extension install dlvhdr/gh-dash

# 支持完整 URL（尤其当仓库不在 github.com 上时）
gh extension install https://ghe.example.com/owner/gh-extension

# 固定版本安装（--pin 指定标签或提交；脚本扩展用 commit SHA，预编译扩展用 Release tag）
gh extension install dlvhdr/gh-dash --pin v2.0.0

# 强制升级已安装的扩展（相当于"重新安装最新版"）
gh extension install dlvhdr/gh-dash --force

# 从本地目录安装（开发扩展时用，详见第 5 步）
gh extension install .
```

安装成功后的提示与验证：

```bash
# 查看是否安装成功
gh extension list

# 直接调用这个新命令
gh dash
```

---

## 第 3 步：管理已安装的扩展（list / upgrade / remove）

App 装多了要管理：看装了哪些、升级、卸载。

### 3.1 列出已安装扩展

```bash
# 列出所有已安装扩展
gh extension list
```

典型输出：

```text
gh dash  dlvhdr/gh-dash  v2.0.0
gh act   nektos/gh-act   v0.2.50
```

### 3.2 升级扩展

```bash
# 升级所有已安装扩展
gh extension upgrade --all

# 只升级某一个
gh extension upgrade gh-dash

# 升级时强制覆盖（--force 可用于跳过"已是最新"的判定）
gh extension upgrade gh-dash --force
```

### 3.3 移除扩展

```bash
# 卸载某个扩展
gh extension remove gh-dash

# 卸载后确认
gh extension list
```

---

## 第 4 步：在浏览器里继续"逛"与评估

```bash
# 打开扩展的 GitHub 仓库主页
gh extension browse gh-dash

# 查看它的 star、Issues、最近提交，判断是否活跃维护
gh repo view dlvhdr/gh-dash
```

评估一个扩展是否可信、值得装的几个要点：

1. **star 数与活跃度**：star 太少、长期不更新（最后一次提交在一年前）的慎用；
2. **代码审查**：重点看它执行了什么命令、是否会上传数据；
3. **许可证**：确认有开源许可证（如 MIT、Apache-2.0）；
4. **作者声誉**：知名开发者/组织的扩展通常更可靠。

---

## 第 5 步：自己开发一个扩展（create / 本地安装）

gh 提供的扩展机制让"自己做一个 App"非常简单，不需要任何审核。

### 5.1 生成脚手架

```bash
# 交互式创建（会问你扩展名等）
gh extension create

# 创建一个脚本扩展（默认生成一个同名可执行脚本模板）
gh extension create my-ext

# 创建 Go 语言的预编译扩展
gh extension create --precompiled=go my-ext

# 创建非 Go 的预编译扩展（如 Rust 等）
gh extension create --precompiled=other my-ext
```

以脚本扩展为例，生成的结构大致是：

```mermaid
graph TD
  A["my-ext/"] --> B["gh-my-ext（同名可执行脚本，核心）"]
  A --> C["...（其余文件按需补充）"]
```

### 5.2 本地开发调试

```bash
# 进入生成的扩展目录，以"本地安装"方式挂载（符号链接方式，改代码即时生效）
cd my-ext
gh extension install .
```

之后你就能在终端里敲 `gh my-ext` 调试它。每次改完代码直接再执行一次即可，无需重新安装。

> 注意：预编译扩展需要手动构建，并把编译产物放到仓库根目录，命名为与仓库同名的可执行文件，否则运行时会报"找不到可执行文件"。

### 5.3 发布扩展

把仓库推送到 GitHub 即可（仓库名保持 `gh-` 开头）。若做预编译扩展，还需要打 Release 并上传各平台的二进制附件。发布后别人就能 `gh extension install 你的名字/gh-my-ext`。

---

## 一张动线图：App 商店与 gh extension 一一对应

| 手机 App 商店 | gh extension | 对应命令 |
| --- | --- | --- |
| 逛商店搜 App | 搜索扩展 | `gh extension search` |
| 查看 App 详情 | 浏览扩展仓库 | `gh extension browse` |
| 安装 App | 安装扩展 | `gh extension install` |
| 看已装 App | 列出扩展 | `gh extension list` |
| 更新 App | 升级扩展 | `gh extension upgrade` |
| 卸载 App | 移除扩展 | `gh extension remove` |
| 开发者上传 App | 创建并发布扩展 | `gh extension create` + 推送仓库 |

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 仓库名不以 gh- 开头 | 安装成功但命令无法识别 | 扩展命名不符合规范 | 仓库名必须是 `gh-xxx` 形式 |
| 缺少同名可执行文件 | 运行时报 `command not found` 或执行失败 | 仓库根目录没有 `gh-xxx` 可执行文件 | 确认可执行文件存在且具可执行权限（Unix 用 `chmod +x`）；预编译扩展需先构建 |
| 与内置命令同名 | 敲的命令仍是内置行为 | 扩展不能覆盖内置命令 | 用 `gh extension exec <名字>` 强制调用扩展 |
| 安装时网络/版本问题 | `--pin` 的 tag 不存在 | 指定的 Release 标签或 commit 写错 | 到仓库 Releases 页核对标签名 |
| 装到可疑扩展 | 行为异常、疑似窃取数据 | 扩展来自不可信发布者 | 安装前用 `browse` 审查源码；如已装，`remove` 卸载并改密相关令牌 |
| 本地开发找不到可执行文件 | `no executable file found` | 预编译扩展未构建产物 | 先手动构建，将产物放到仓库根目录再 `install .` |
| 升级报错 | `failed to upgrade` | 网络或仓库已被删除/改名 | 检查仓库是否仍存在；必要时 `remove` 后重新 `install` |

---

## 一句话记忆

**扩展就是 gh 的"App 商店"：`search/browse` 逛商店，`install` 安装，`list/upgrade/remove` 管理，`create` 自己做 App——安装前务必审查源码，因为 GitHub 不为扩展背书。**



<!-- ============ 文档分隔线：004-github/054-GhApi.md ============ -->



## 开篇：把 API 想成"万能遥控器 + 电器说明书"

电视遥控器只能按预设按钮；而真正的"万能遥控器"能直接输入指令码，控制任何家电。GitHub 的 **API（应用程序接口）** 就是这样的万能遥控器：任何操作——查仓库、建 Issue、改标签、删发布——都可以不通过网页，而通过一段"指令"完成。

但万能遥控器要能工作，你得有一本**说明书**：哪个地址对应哪个功能？要传什么参数？这本说明书就是 GitHub 的 **API 文档**（REST 参考手册、GraphQL 参考手册）。

`gh api` 命令，就是"**已插好电池、已对准电视**"的万能遥控器：它自动携带你的登录凭证，你只需要照着说明书报指令码即可，不用再手动处理认证、请求头、JSON 解析这些琐事。

---

## 原理第一课：REST API 与 GraphQL API 是什么

### 1.1 直观理解：REST 像"查字典"，GraphQL 像"点菜"

- **REST API（GitHub API v3）**：每个资源都有一个固定网址（端点）。"仓库"在 `/repos/owner/repo`，"Issue 列表"在 `/repos/owner/repo/issues`。你想拿什么数据，就访问对应网址，返回一大坨 JSON。就像查字典：翻到固定页码，能看到这页的所有内容（可能有很多你不需要的）。

- **GraphQL API（GitHub API v4）**：只有一个入口，你在请求里"声明"你要什么字段。就像点菜：告诉服务员"只要这个菜、不加葱"，厨房只按你要的做。返回体更小、结构更精确。

### 1.2 实操层面的差别

| 对比项 | REST（v3） | GraphQL（v4） |
| --- | --- | --- |
| 入口 | 成百上千个网址（端点） | 单一入口 `graphql` |
| 请求方式 | GET / POST / PATCH / DELETE | POST（带查询语句） |
| 返回内容 | 固定结构的 JSON（可能多余） | 完全按你声明的字段返回 |
| 学习曲线 | 直观、文档多 | 需要学查询语法，但更灵活 |

`gh api` 对两者都支持：传一个路径就是 REST，传 `graphql` 就是 GraphQL。

### 1.3 几个"地基"概念

- **端点（endpoint）**：REST 里的网址路径，如 `repos/cli/cli`。
- **占位符**：`gh api` 支持在端点里写 `{owner}`、`{repo}`、`{branch}`，gh 会从当前目录的仓库自动替换。例如在 `cli/cli` 仓库里执行 `gh api repos/{owner}/{repo}` 等价于 `gh api repos/cli/cli`。注意：PowerShell 里含 `{}` 的值最好加引号。
- **认证**：`gh api` 自动使用 `gh auth login` 的凭证，无需手动加 token。
- **方法（method）**：GET（读）、POST（新建）、PATCH（部分修改）、PUT（整体覆盖）、DELETE（删除）。

---

## 原理第二课：gh api 的三个自动行为

理解了以下三点，大部分命令就不会写错：

1. **默认方法**：默认是 GET；**一旦你加了 `-f`/`-F` 参数，自动变为 POST**。想"带参数的 GET"，必须显式写 `--method GET`。
2. **参数类型**：`-f/--raw-field` 永远当**字符串**；`-F/--field` 有**魔法类型转换**（`true`/`false`/`null`/整数自动转成 JSON 类型；值以 `@` 开头则从文件读取）。
3. **输出**：默认打印完整 JSON；可用 `--jq`（jq 语法提取）、`--template`（Go 模板）、`--json`（配合部分命令）。

---

## 场景一：读数据（GET，最常用）

```bash
# 获取当前登录用户信息
gh api user

# 获取某个仓库的信息（在仓库目录内可省略 owner/repo，用占位符）
gh api repos/cli/cli
gh api repos/{owner}/{repo}

# 列出仓库的 issue（返回 JSON 数组）
gh api repos/cli/cli/issues

# 列出当前仓库的所有 release
gh api repos/{owner}/{repo}/releases

# 带查询参数的 GET（注意：必须显式 -X GET，否则会被当成 POST）
gh api -X GET search/issues -f q='repo:cli/cli is:open'

# 自定义请求头（例如获取原始文件内容）
gh api -H 'Accept: application/vnd.github.v3.raw+json' repos/{owner}/{repo}/readme
```

返回示例（`gh api repos/cli/cli` 的一段）：

```json
{
  "id": 212613049,
  "name": "cli",
  "full_name": "cli/cli",
  "description": "GitHub’s official command line tool",
  "stargazers_count": 38000,
  "html_url": "https://github.com/cli/cli"
}
```

---

## 场景二：写数据（POST / PATCH / DELETE）

### 2.1 创建 Issue（POST + 字符串参数）

```bash
# -f 传字符串参数；加了 -f 后自动变成 POST
gh api repos/{owner}/{repo}/issues \
  -f title="Bug 报告：登录闪退" \
  -f body="复现步骤：1. 点击登录 2. 页面闪退"

# 指定标签（某些端点接受 labels 数组；数组语法见 2.3）
gh api repos/{owner}/{repo}/issues \
  -f title="bug: 登录闪退" \
  -f body="详情描述" \
  -F 'labels[]=bug'
```

### 2.2 类型化参数（-F 魔法转换）

```bash
# milestone 是数字，用 -F 才能正确传成 JSON 数字
gh api repos/{owner}/{repo}/issues -F milestone=12 -f title="里程碑 12 的任务"

# 布尔值同样用 -F
gh api user/repos -F name=new-repo -F private=true -F auto_init=true

# 从文件读取字段值（@ 语法；- 表示标准输入）
gh api user/repos -f name=@repo-name.txt
gh api gists -F 'files[myfile.txt][content]=@myfile.txt'
```

### 2.3 嵌套与数组参数

```bash
# 嵌套对象：key[subkey]=value
gh api -X PATCH orgs/{org}/properties/schema \
  -F 'properties[][property_name]=environment' \
  -F 'properties[][default_value]=production'

# 数组：声明多个同名 key[]
gh api repos/{owner}/{repo}/issues -f title="任务" -F 'labels[]=bug' -F 'labels[]=help-wanted'

# 空数组：key[] 不带值
gh api repos/{owner}/{repo}/issues -f title="任务" -F 'assignees[]'
```

### 2.4 请求体从文件读取（--input）

```bash
# 请求体直接来自 JSON 文件（复杂 payload 的推荐做法）
gh api repos/{owner}/{repo}/labels --input labels.json

# 从标准输入读取请求体
echo '{"name":"bug","color":"d73a4a"}' | gh api repos/{owner}/{repo}/labels --input -
```

### 2.5 删除操作

```bash
# 删除（DELETE 方法）
gh api repos/{owner}/{repo}/issues/42 -X DELETE --silent
```

---

## 场景三：处理输出（--jq / --template）

API 返回的 JSON 往往很大，99% 的时候你只想要其中几个字段。

### 3.1 jq 语法提取

```bash
# 只取仓库的 full_name 字段
gh api user/repos --jq '.[].full_name'

# 只取 Issue 的标题与编号
gh api repos/{owner}/{repo}/issues --jq '.[] | "\(.number) \(.title)"'

# 统计数量（length）
gh api repos/{owner}/{repo}/issues --jq 'length'

# 条件过滤：只取被标记为 bug 的 issue 标题
gh api repos/{owner}/{repo}/issues --jq '.[] | select(.labels[].name == "bug") | .title'
```

### 3.2 Go 模板输出

```bash
# 用模板格式化（适合生成报告文本）
gh api repos/{owner}/{repo}/issues --template \
  '{{range .}}{{.title}} ({{.number}}){{"\n"}}{{end}}'
```

### 3.3 静默模式

```bash
# 不打印响应体（只看操作是否成功，用于脚本）
gh api repos/{owner}/{repo}/issues/42 -X PATCH -f state=closed --silent
```

---

## 场景四：分页（--paginate）

列表接口默认每页最多 100 条，数据多时只返回第一页。`--paginate` 自动翻完所有页：

```bash
# 自动获取所有页的 issue 标题
gh api repos/{owner}/{repo}/issues --paginate --jq '.[].title'

# 把多页数组合并成一个外层数组（--slurp）
gh api user/repos --paginate --slurp --jq 'length'
```

---

## 场景五：GraphQL 查询

GraphQL 请求把查询语句放在 `-f query=...` 中，其余字段作为变量传入：

```bash
# 查当前用户最近 3 个仓库的名字
gh api graphql -f query='
  query {
    viewer {
      repositories(first: 3) {
        nodes { name }
      }
    }
  }
'

# 带变量（-F 传入变量值，注意不是字符串）
gh api graphql -F owner='{owner}' -F name='{repo}' -f query='
  query($name: String!, $owner: String!) {
    repository(owner: $owner, name: $name) {
      releases(last: 3) { nodes { tagName } }
    }
  }
'

# GraphQL 分页（查询中需声明 $endCursor 并返回 pageInfo）
gh api graphql --paginate -f query='
  query($endCursor: String) {
    viewer {
      repositories(first: 100, after: $endCursor) {
        nodes { nameWithOwner }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
'
```

---

## 场景六：调试与排查（--include / --verbose）

```bash
# 显示响应头与状态码（看限流、看缓存头）
gh api user --include

# 显示完整请求与响应（排查参数传错等）
gh api user --verbose

# 开启响应缓存（--cache，例如缓存 1 小时，减少重复请求）
gh api user --cache 1h
```

`--include` 输出示例（前面是响应头，空行后是响应体）：

```text
HTTP/2.0 200 OK
content-type: application/json; charset=utf-8
x-ratelimit-remaining: 4999
...

{"login":"fanquanpp", ...}
```

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 加了 -f 却想要 GET | 报方法不允许或行为异常 | 加参数后自动变 POST | 显式写 `-X GET` |
| 数字/布尔传错类型 | 接口提示类型错误 | 用了 `-f`（一律按字符串） | 改用 `-F` 触发类型转换 |
| 未登录调用 | `authentication failed` | 没有凭证 | 先 `gh auth login` |
| PowerShell 中 { } 报错 | 端点被 shell 展开或报错 | `{}` 有特殊含义 | 用引号包裹端点：`gh api "repos/{owner}/{repo}"` |
| 404 找不到资源 | `HTTP 404` | 端点路径写错或资源私有 | 核对 REST 参考手册路径；检查资源可见性 |
| 403 限流 | `rate limit exceeded` | 请求过于频繁 | 查看 `--include` 的 `x-ratelimit-remaining`；稍后重试或加 `--cache` |
| 把 query 当普通字段传 | GraphQL 报语法错误 | GraphQL 的查询必须放在 `query` 字段 | 用 `-f query=...` 传递查询语句 |
| 分页结果重复/不全 | 只有部分数据 | 未理解分页机制 | 加 `--paginate`；多页数组合并用 `--slurp` |

---

## 一句话记忆

**gh api 是带认证的"万能遥控器"：路径是 REST、`graphql` 是 v4，加 `-f` 自动变 POST，`-F` 自动转类型，`--jq` 裁剪输出，`--paginate` 翻页——一切以官方 API 手册为准。**



<!-- ============ 文档分隔线：004-github/055-GhSearch.md ============ -->



## 开篇：把 gh search 想成图书馆检索系统

图书馆很大，书架成千上万。直接逛，你永远找不到想要的书。但图书馆有一套**检索系统**：想找书，按"书名+作者+分类"查；想找某篇期刊文章，按关键词查；想找某位作者的全部著作，按作者查。检索系统的价值就是：**在浩如烟海的资料里，几秒钟锁定目标**。

GitHub 上有上亿个仓库、几十亿行代码。`gh search` 就是 GitHub 的"图书馆检索系统"：不用打开网页、不用一个个仓库翻，直接在终端里用一条命令，从全站范围内筛出你想要的仓库、代码、Issue、PR 甚至提交记录。

本文采用"问题驱动"写法：你想解决什么，就跳到对应小节找答案。

---

## 原理先讲清：搜索的两大要素

### 2.1 搜索范围（要搜什么）

`gh search` 下有 5 个子命令，对应 5 种"馆藏"：

| 子命令 | 搜索范围 | 典型问题 |
| --- | --- | --- |
| `gh search repos` | 仓库 | "想找某语言的开源项目" |
| `gh search code` | 代码内容 | "想找某段代码怎么写的" |
| `gh search issues` | Issue | "有没有人报过这个 bug" |
| `gh search prs` | 拉取请求 | "这个功能有没有人提过 PR" |
| `gh search commits` | 提交记录 | "某段逻辑是什么时候改的" |

### 2.2 搜索语法（怎么搜得更准）

GitHub 搜索由"关键词 + 限定符（qualifier）"组成。限定符就是 `xx:值` 形式的过滤条件，例如 `label:bug`、`author:octocat`、`stars:>1000`。`gh search` 支持两种写法：

- **用参数旗标**：`gh search repos --language=go --stars=">1000"`（每个限定符对应一个旗标，更易读）；
- **直接写语法**：`gh search issues label:bug author:monalisa state:open`（与网页端搜索框一致，灵活但需记语法）。

两者可以混用。建议新手先用旗标，熟悉后再用语法。

---

## 问题 1："我想找某个开源仓库/项目"

这是最常用的搜索：找库、找项目模板、找学习资料。

```bash
# 按关键词搜仓库（多个词之间是"与"关系）
gh search repos "react ui"

# 按编程语言过滤
gh search repos --language=typescript

# 按 star 数过滤（数字写法带引号）
gh search repos --stars=">1000" --language=go

# 按主题（topic）过滤，比如找"低代码"主题的项目
gh search repos --topic=low-code --limit 10

# 限定组织与可见性
gh search repos --owner=microsoft --visibility=public

# 找"适合新手入门"的项目（good first issue 数量 >= 10）
gh search repos --language=go --good-first-issues=">=10"

# 排除已归档仓库
gh search repos --archived=false

# 只搜仓库名（不匹配描述/README）
gh search repos --match=name "chatgpt"

# 按 star 数排序
gh search repos react --sort=stars --order=desc
```

`gh search repos` 典型输出：

```text
NAME                 DESCRIPTION                            STARS  UPDATED
facebook/react       The library for web and native...      229k   2h ago
vercel/next.js       The React Framework                     130k   1h ago
```

---

## 问题 2："我想找某段代码/某个 API 用法"

抄作业（参考优秀代码）是学习利器。`gh search code` 能搜全站公开仓库的代码内容。

```bash
# 搜索同时包含 useState 和 useEffect 的代码
gh search code "useState useEffect"

# 限定在某仓库内搜索
gh search code "TODO" --repo=owner/repo

# 限定文件名搜索（例如找所有 settings.py）
gh search code "DEBUG" --filename="*.py"

# 限定组织与语言
gh search code "config" --org=myorg --language=go
```

> 注意：代码搜索**默认只覆盖公开仓库**，且需要登录才能使用；私有仓库的代码需要额外权限。

---

## 问题 3："这个 bug/功能有没有人提过 Issue？"

写代码遇到报错，先搜 GitHub——大概率有人踩过坑，还能看到解决方案。

```bash
# 搜 open 状态、带 bug 标签的 issue
gh search issues "memory leak" --state=open --label=bug

# 搜分配给自己的 open issue（@me 表示"当前登录用户"）
gh search issues --assignee=@me --state=open

# 限定在某仓库搜
gh search issues --repo=owner/repo "crash"

# 搜自己创建的 issue
gh search issues --author=@me

# 同时搜索 issue 与 PR（--include-prs）
gh search issues --include-prs --owner=cli

# 找"没人认领、适合新手"的 issue（无 assignee + 有标签）
gh search issues --no-assignee --label="good first issue"

# 找评论数多的热门 issue
gh search issues --comments=">50"

# 找没有 bug 标签的 issue（排除语法，注意前面的 --）
gh search issues -- "-label:bug"
```

`gh search issues` 典型输出：

```text
NUMBER  TITLE                    STATE  LABELS         UPDATED
#4521   Fix memory leak in X     open   bug           2d ago
#4498   Crash on startup         open   bug, priority 5h ago
```

---

## 问题 4："这个功能有没有人提过 PR？"

```bash
# 搜自己已合并的 PR
gh search prs --merged --author=@me

# 搜需要自己审查的 PR（很实用）
gh search prs --review-requested=@me --open

# 搜某仓库的已合并 PR
gh search prs --repo=owner/repo --merged

# 搜未合并、带 review 标签的 PR
gh search prs --reviewed-by=@me --state=open

# 搜被标记为 draft（草稿）的 PR
gh search prs --draft --repo=owner/repo
```

---

## 问题 5："某段代码是什么时候引入的？"

```bash
# 按提交信息搜索
gh search commits "fix memory leak" --repo=owner/repo

# 按作者搜索提交
gh search commits --author=zhangsan

# 限定组织范围
gh search commits "bump version" --org=myorg
```

---

## 通用技巧：让结果更可控

### 5.1 控制输出

```bash
# 限制条数（默认 30）
gh search repos react --limit 50

# 按 star 数升序
gh search repos react --sort=stars --order=asc

# 输出 JSON 供脚本处理
gh search repos react --json fullName,stargazersCount

# 配合 jq 只取名字
gh search repos react --json fullName --jq '.[].fullName'

# 在浏览器中打开搜索结果页面
gh search repos react --web
```

### 5.2 排除限定符（重点技巧）

网页端支持 `-label:bug` 这样的"排除"语法，但终端里 `-` 开头的字符串会被 shell 当成参数。解决方法是加一个 `--` 分隔符，告诉 shell"后面是查询串，不是参数"：

```bash
# Unix 系（bash/zsh/macOS）用法
gh search issues -- "-label:bug"

# PowerShell 用法（需要 --% 停止解析）
gh --% search issues -- "-label:bug"
```

---

## 通用技巧：读懂搜索结果与常用字段

`--json` 输出的字段取决于搜索类型，掌握常用字段可让脚本化处理事半功倍：

| 搜索类型 | 常用 JSON 字段 | 说明 |
| --- | --- | --- |
| repos | `fullName`、`description`、`stargazersCount`、`language`、`isArchived` | 仓库全名、描述、star 数、语言、是否归档 |
| issues | `number`、`title`、`state`、`labels`、`assignees`、`isPullRequest` | 编号、标题、状态、标签、指派者、是否为 PR |
| prs | `number`、`title`、`state`、`isDraft`、`mergeable` | 编号、标题、状态、是否为草稿、是否可合并 |
| code | `repository`、`path`、`name` | 所在仓库、文件路径、文件名 |
| commits | `sha`、`message`、`author`、`date` | 提交哈希、提交信息、作者、日期 |

结合 `--jq` 可以拼出任意格式：

```bash
# 输出"仓库名: 描述"格式
gh search repos "react" --json fullName,description --jq '.[] | "\(.fullName): \(.description)"'

# 只看 star 数前 5 的仓库全名
gh search repos --language=python --sort=stars --limit 5 --json fullName --jq '.[].fullName'
```

> 提示：所有 `gh search` 子命令都支持 `--json` 与 `--jq`，想了解某类搜索的全部字段，可在任意仓库执行 `gh search repos --json <Tab>` 或查看官方手册对应页面。

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 排除语法直接写 `-label:bug` | 报 `unknown flag: -label` | 减号被 shell 当成参数 | 查询前加 `--`：`gh search issues -- "-label:bug"` |
| 数字条件不加引号 | `stars:>1000` 报错或行为怪异 | `>` 被 shell 重定向 | 加引号：`--stars=">1000"` |
| 未登录就搜代码 | `code search requires authentication` | 代码搜索必须登录 | 先 `gh auth login` |
| 搜索词含空格被拆开 | 结果对不上 | 多个词被视为"与"关系 | 想搜短语加引号：`gh search repos "vim plugin"` |
| 用 --repo 但值写错 | 结果为空 | 仓库名格式错误 | 用 `owner/repo` 完整格式 |
| 搜私有仓库代码 | 结果为空 | 默认只搜公开仓库 | 确认有权限且在设置中开启代码搜索授权 |
| 分不清 issues 与 prs | 结果混入另一类 | `gh search issues` 默认不含 PR | 需要同时搜加 `--include-prs`；只搜 PR 用 `gh search prs` |

---

## 一句话记忆

**`gh search` 是 GitHub 的"检索台"：找库用 `repos`，找代码用 `code`，找讨论用 `issues/prs`，找历史用 `commits`；记住"关键词 + 限定符 + `--` 排除 + `--json` 输出"四板斧，检索又快又准。**



<!-- ============ 文档分隔线：004-github/056-GhLabel.md ============ -->



## 开篇：把标签想成文件柜的彩色贴纸

整理文件柜时，你会给文件夹贴不同颜色的贴纸：红色代表"紧急"、绿色代表"已完成"、蓝色代表"财务"。有了这些贴纸，你一眼就能知道每个文件夹的状态，找文件不用一个个打开翻。

GitHub 仓库里的 **Issue 和 PR 就是文件夹，Label（标签）就是贴纸**。贴上 `bug`，表示"这是个缺陷"；贴上 `good first issue`，表示"适合新手"；贴上 `priority:high`，表示"很紧急"。标签让成百上千的 Issue 变得**可筛选、可统计、可自动处理**（比如 Actions 可以监听"带某个标签的 Issue 被创建"）。

`gh label` 系列命令，就是你的"贴纸管理工具"：不打开网页，就能查看、创建、修改、删除、批量复制标签。本文按"标签管理的完整流程"（清单式）展开：**看现状 → 建标签 → 改标签 → 删标签 → 复制模板**。

---

## 原理先讲清：标签的三要素

一个标签由三个属性组成：

| 属性 | 说明 | 示例 |
| --- | --- | --- |
| 名称（name） | 唯一标识，会显示在 Issue 上 | `bug`、`type:bug`、`good first issue` |
| 颜色（color） | 6 位十六进制色值，用于视觉区分 | `d73a4a`（红）、`0e8a16`（绿） |
| 描述（description） | 一句话说明这个标签的用途 | "Something isn't working" |

关键规则：

- 颜色是**6 位十六进制**（如 `E99695`），不带 `#` 前缀；
- 创建时不给颜色，gh 会**随机生成**一个颜色（建议显式指定，保持仓库观感一致）；
- 新仓库自带一组默认标签（`bug`、`enhancement`、`documentation`、`good first issue`、`help wanted` 等）；
- 命令可以作用于任何仓库：在仓库目录内省略参数，或加 `-R owner/repo` 指定。

---

## 清单第 1 步：查看现状（gh label list）

动手改之前先"盘点"：仓库里现在有哪些标签？

```bash
# 列出当前仓库全部标签
gh label list

# 按名称模糊搜索（比如找所有含 bug 的标签）
gh label list --search bug

# 在别的仓库里看
gh label list -R owner/repo

# 只看某类标签（如 type: 前缀）
gh label list --search "type:"
```

典型输出：

```text
NAME              DESCRIPTION                      COLOR
bug               Something isn't working         d73a4a
documentation     Improvements or additions       0075ca
enhancement       New feature or request          0e8a16
good first issue  Good for newcomers              7057ff
```

通过这一步，你就能知道：哪些标签已经存在（避免重复创建）、哪些命名风格不统一（后续统一整理）。

---

## 清单第 2 步：创建标签（gh label create）

```bash
# 最简方式：只给名字（颜色随机，不推荐）
gh label create bug

# 标准方式：名称 + 描述 + 颜色
gh label create bug --description "Something isn't working" --color E99695

# 创建带命名空间的标签（团队常用"分类:名称"格式）
gh label create "type:bug" --color "D73A4A" --description "Bug 问题"

# 创建优先级类标签
gh label create "priority:high" --color "B60205" --description "高优先级"
gh label create "priority:low" --color "0E8A16" --description "低优先级"

# 在指定仓库创建
gh label create "needs-triage" --description "待分类" -R owner/repo
```

注意 `--color` 的写法：`--color "D73A4A"` 或 `--color D73A4A` 均可（不带 `#`）。

> 创建时如果标签已存在，默认会报错；想"存在就更新"可加 `--force`：
> ```bash
> gh label create bug --description "新的描述" --color d73a4a --force
> ```

---

## 清单第 3 步：编辑维护（gh label edit）

标签建好后，随着项目演进，常常需要改名、改色、改描述。

```bash
# 修改标签颜色
gh label edit bug --color "B60205"

# 修改标签描述
gh label edit bug --description "程序缺陷，需要修复"

# 重命名标签（--new-name；已打上旧标签的 issue 会自动改用新名字）
gh label edit bug --new-name "type:bug"

# 同时修改多个属性
gh label edit "priority:high" --color "D93F0B" --description "高优先级，尽快处理"
```

重命名是整理仓库标签的重要手段：比如把混乱的 `bug`、`Bug`、`bug!` 统一成 `type:bug`。

---

## 清单第 4 步：删除清理（gh label delete）

标签过时了、命名错了、分类体系调整了，就要清理。**注意：删除标签会让所有已打该标签的 Issue/PR 失去这个标签**（Issue 本身不受影响，只是筛选条件变了）。

```bash
# 删除标签（--yes 跳过确认）
gh label delete "type:bug" --yes

# 删除另一个仓库的标签
gh label delete "needs-triage" --yes -R owner/repo
```

删除前建议先用 `gh label list --search <关键词>` 确认名字没打错，因为该操作不可恢复（除非重新创建并手动重新打标）。

---

## 清单第 5 步：模板复用（gh label clone）

新仓库逐个创建标签很累。如果你有一个"标签体系很完善"的模板仓库，一条命令就能**把它的全部标签复制过来**——这是团队标准化标签体系的利器。

```bash
# 把模板仓库的所有标签复制到当前仓库
gh label clone owner/template-repo

# 指定源仓库与目标仓库
gh label clone owner/template-repo -R my-org/my-new-repo
```

典型应用场景：

- 团队规定所有新项目统一使用一套标签（`type:*`、`priority:*`、`status:*`）；
- 你维护多个同类仓库，希望标签保持一致；
- 新仓库初始化时一键获得"完整标签体系"。

`clone` 是 gh 独有的贴心功能，网页端没有对应按钮。

---

## 标签体系设计建议（进阶）

一个健康的标签体系通常分几类，建议按"前缀命名空间"组织：

| 分类 | 示例标签 | 用途 |
| --- | --- | --- |
| 类型（type） | `type:bug`、`type:feature`、`type:docs` | 说明 Issue 的性质 |
| 优先级（priority） | `priority:high`、`priority:low` | 说明紧急程度 |
| 状态（status） | `status:blocked`、`status:in-progress` | 说明处理进度 |
| 协作（collab） | `good first issue`、`help wanted` | 引导社区贡献 |
| 特殊（special） | `needs-triage`、`won't fix`、`duplicate` | 流程性标记 |

命名空间的优点：`--search "type:"` 能一次筛出一整类标签，后续加标签不冲突、不混乱。

---

## 进阶应用：标签与自动化联动

标签不只是"给人看的"，还能驱动自动化：

### 联动 1：搜索与筛选

```bash
# 找出所有带 bug 标签的 open issue（配合 gh search，见《GhSearch》）
gh search issues --label=bug --state=open --repo=owner/repo

# 找出所有"待分类"的 issue
gh search issues --label="needs-triage" --repo=owner/repo
```

### 联动 2：批量打标（配合 gh api）

给多个 Issue 批量打标签，用 `gh api` 更高效：

```bash
# 给 issue 42 打上 bug 标签
gh api repos/{owner}/{repo}/issues/42 -X PATCH -F 'labels[]=bug'

# 用循环批量处理（bash 示例：给列表中的 issue 编号打标）
for n in 10 11 12; do
  gh api repos/{owner}/{repo}/issues/$n -X PATCH -F 'labels[]=needs-triage'
done
```

### 联动 3：Actions 自动打标

GitHub Actions 可以监听 Issue 事件自动打标签。例如"Issue 标题含 `[urgent]` 时自动打高优先级标签"，这类工作流可在 workflow 文件中用 `gh` 或社区 action 实现。标签名一旦定下，就要尽量避免删除改名，否则已配置的自动化逻辑全部要跟着改。

### 联动 4：统计报表

```bash
# 统计各类标签下有多少 open issue（配合 jq 汇总）
gh api repos/{owner}/{repo}/issues --paginate --jq '.[] | .labels[].name' | sort | uniq -c
```

标签体系是仓库的"分类语言"，**先设计、再落地、少变更**，才能让标签长期稳定地发挥作用。

---

## 完整流程串联：从 0 搭建一套标签体系

```bash
# 1. 盘点：看看默认标签长什么样
gh label list

# 2. 如果已有模板仓库，直接复制（跳过 3-5）
gh label clone owner/template-repo

# 3. 创建类型类标签
gh label create "type:bug" --color "D73A4A" --description "程序缺陷"
gh label create "type:feature" --color "0E8A16" --description "新功能请求"

# 4. 创建优先级与协作标签
gh label create "priority:high" --color "B60205" --description "高优先级"
gh label create "good first issue" --color "7057FF" --description "适合新手入门"

# 5. 清理与统一
gh label edit "enhancement" --new-name "type:feature"   # 合并默认标签
gh label delete "invalid" --yes                          # 删除不用的默认标签

# 6. 验收
gh label list --search "type:"
```

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| 颜色带了 # 前缀 | 报 `invalid color` | 颜色必须是 6 位十六进制，不带 # | 写成 `--color "D73A4A"` 或 `--color D73A4A` |
| 颜色不是 6 位 | 报 `color must be 6 characters` | 色值格式错误 | 使用如 `B60205` 的 6 位格式 |
| 创建已存在的标签 | 报 `label already exists` | 标签名重复 | 改名，或加 `--force` 更新已有标签 |
| 名称含空格/冒号未加引号 | 报 `unknown flag` 或行为异常 | 被 shell 拆成多个参数 | 用引号包裹：`gh label create "type:bug"` |
| 删错标签 | 大量 issue 的标签消失 | 删除不可恢复 | 删除前用 `list --search` 核对；重建后需重新给 issue 打标 |
| clone 来源写错 | 报 `repository not found` | 模板仓库路径错误 | 用 `owner/repo` 完整格式，确认仓库存在且有读取权限 |
| 在错误仓库操作 | 标签出现在奇怪的地方 | 忘了当前目录 | 加 `-R owner/repo` 显式指定目标仓库 |

---

## 一句话记忆

**Label 是 Issue 的"彩色贴纸"：`list` 盘点、`create` 贴新、`edit` 改色改名、`delete` 撕掉、`clone` 一键复制整套——命名用"分类:名称"格式，团队协作才不乱。**



<!-- ============ 文档分隔线：004-github/057-GhAliasConfig.md ============ -->



## 开篇：把别名想成语音助手的"自定义唤醒词"

智能音箱有个功能：你可以设置自定义词。说"回家模式"，音箱会自动执行"关灯、开空调、放音乐"一整套动作；而不是每次都说"请把灯关掉，然后把空调开到 26 度，再放一首歌"。

**gh 别名（alias）** 就是这个"自定义唤醒词"：你给一长串常用命令起一个短名字，之后敲这个短名字，gh 就会展开成完整命令执行。而 **gh config（配置）** 则像音箱的"系统设置"：默认用哪个音乐平台、音量默认多大——一次性设好，以后每次都生效。

本文采用**操作向导**形式，一步一步带你完成：设置第一个别名 → 带参数的别名 → 管道别名 → 管理别名 → 常用配置 → 补全与状态检查。

---

## 原理先讲清：别名如何工作

### 1.1 别名的本质是"字符串展开"

`gh alias set <别名> <展开内容>` 做的事情很简单：把"别名"记录成"展开内容"。你敲 `gh <别名> 附加参数` 时，gh 先做字符串替换，再执行。

```text
gh alias set pv 'pr view'
gh pv -w 123   # 等价于执行：gh pr view -w 123
```

- 展开内容里没有 `$1`、`$2` 之类的**位置占位符**时，你附加的参数会**追加**到展开命令末尾；
- 展开内容里有 `$1` 时，第一个附加参数会**插入**到 `$1` 的位置。

### 1.2 两种别名类型

| 类型 | 判定方式 | 能力 |
| --- | --- | --- |
| gh 命令别名 | 展开内容不是 `!` 开头、未加 `--shell` | 只能展开成 gh 的子命令调用 |
| shell 别名 | 展开内容以 `!` 开头，或加了 `--shell` | 通过 shell 解释器执行，支持管道、重定向、多命令串联 |

### 1.3 配置文件的存储位置

- 别名与配置默认保存在 `~/.config/gh/` 下（Windows 为 `%AppData%\GitHub CLI\`）；
- 配置支持"按主机"（`--host github.com`）区分，适合同时使用 GitHub.com 与企业版 GitHub Enterprise 的用户。

---

## 操作向导 1：设置你的第一个别名

### 第 1 步：检查是否已登录

```bash
gh auth status
```

### 第 2 步：设置别名

```bash
# 为 "pr view" 设置别名 pv
gh alias set pv "pr view"

# 为 "issue list --label=bugs" 设置别名 bugs
gh alias set bugs "issue list --label=bugs"

# 为 "issue list --assignee @me" 设置别名 mine
gh alias set mine "issue list --assignee @me"
```

### 第 3 步：使用别名

```bash
# 查看 PR 123 并打开浏览器（等价于 gh pr view 123 -w）
gh pv 123 -w

# 列出带 bugs 标签的 issue（等价于 gh issue list --label=bugs）
gh bugs
```

### 第 4 步：验证别名已生效

```bash
gh alias list
```

典型输出：

```text
pv: pr view
bugs: issue list --label=bugs
mine: issue list --assignee @me
```

---

## 操作向导 2：带参数的别名（位置占位符）

不想让附加参数都挤在末尾时，用 `$1`、`$2` 控制插入位置：

```bash
# 定义：查某作者的 epic 标签 issue
# 用法：gh epicsBy vilmibm
# 展开：gh issue list --author="vilmibm" --label="epic"
gh alias set epicsBy 'issue list --author="$1" --label="epic"'

# 定义：多参数别名
# 用法：gh lbl repo bug
# 展开：gh label list -R repo --search bug
gh alias set lbl 'label list -R "$1" --search "$2"'
```

> 注意 Windows 使用提示：命令提示符（cmd）下参数需要用**双引号**包裹，例如 `gh alias set pv "pr view"`；PowerShell 与 bash 中单双引号均可，但展开内容含 `$1` 时建议用单引号，避免 shell 提前展开变量。

---

## 操作向导 3：管道与多命令别名（--shell）

别名展开成 gh 命令还不够，想"先列出来再 grep"怎么办？用 shell 别名：

```bash
# 方式一：展开内容以 ! 开头（隐式 shell 别名）
gh alias set igrep '!gh issue list --label="$1" | grep "$2"'
# 用法：gh igrep epic foo

# 方式二：加 --shell 显式声明（推荐，可读性更好）
gh alias set recent 'run list --limit 5' --shell

# 组合示例：查看最近 10 条 issue 的标题并按关键词过滤
gh alias set myissues '!gh issue list --limit 10 --json title --jq ".[].title" | grep "$1"' --shell
```

带 `--shell` 的别名通过 `sh` 解释器执行，因此**管道、重定向、变量、多条命令用 `;` 串联**都可以：

```bash
# 定义一条"发布并打开"的复合别名
gh alias set ship '!gh release create "$1" --generate-notes && gh release view "$1" --web' --shell
# 用法：gh ship v1.0.0
```

---

## 操作向导 4：管理别名（list / delete / import）

### 4.1 列出与删除

```bash
# 查看所有别名
gh alias list

# 删除单个别名
gh alias delete pv

# 删除后确认
gh alias list
```

### 4.2 从标准输入读取展开内容

展开内容很长、引号很复杂时，可以用 `-` 从标准输入读取，避免引号转义地狱：

```bash
echo "issue list --author=@me --state=open" | gh alias set myopen -
```

### 4.3 批量导入（YAML 文件）

```bash
# aliases.yml 内容示例：
# pv: pr view
# bugs: issue list --label=bugs
# --clobber 表示覆盖已存在的同名别名
gh alias import aliases.yml --clobber
```

导出当前别名（反向操作）可配合 `gh alias list --shell` 生成可复用的 shell 片段。

### 4.4 覆盖已存在别名

```bash
# 默认同名会报错，加 --clobber 覆盖
gh alias set pv "pr view --web" --clobber
```

---

## 操作向导 5：常用配置（gh config）

### 5.1 查看配置

```bash
# 列出全部配置
gh config list

# 查看单项配置
gh config get editor
gh config get git_protocol
gh config get prompt
```

### 5.2 设置常用配置项

```bash
# 默认编辑器：VS Code（--wait 表示关闭文件前不返回，符合 git/gh 的等待语义）
gh config set editor "code --wait"

# 默认编辑器：vim（服务器场景）
gh config set editor vim

# Git 传输协议：ssh（改用 SSH 认证克隆/推送，需已配置 SSH key）
gh config set git_protocol ssh

# 关闭交互式提示（脚本自动化场景）
gh config set prompt disabled

# 关闭分页器（输出直接打印，不进入 less）
gh config set pager ""

# 按主机单独设置（企业版 GitHub Enterprise 场景）
gh config set git_protocol ssh --host github.com
```

### 5.3 核心配置项速查表

| 配置键 | 可选值 | 默认值 | 作用 |
| --- | --- | --- | --- |
| `git_protocol` | `https` / `ssh` | `https` | 克隆与推送使用的 Git 协议 |
| `editor` | 任意编辑器命令 | 系统默认 | gh 打开编辑器编写文本时使用 |
| `prompt` | `enabled` / `disabled` | `enabled` | 是否允许交互式询问 |
| `pager` | 任意分页命令 | less | 长输出的分页器 |
| `browser` | 任意浏览器命令 | 系统默认 | `--web` 打开链接时使用 |
| `spinner` | `enabled` / `disabled` | `enabled` | 是否显示加载动画 |
| `telemetry` | `enabled` / `disabled` / `log` | `enabled` | 遥测数据上报开关 |

> 提示：`telemetry` 是遥测（匿名使用数据上报）开关，注重隐私的用户可执行 `gh config set telemetry disabled` 关闭。

### 5.4 清理缓存

```bash
# 清除 gh 的缓存（如版本检查缓存等）
gh config clear-cache
```

---

## 操作向导 6：Shell 补全与账户状态

### 6.1 生成自动补全脚本

敲命令时按 Tab 自动补全，需要为你的 shell 生成补全脚本：

```bash
# bash
gh completion -s bash > ~/.gh-completion.bash
echo "source ~/.gh-completion.bash" >> ~/.bashrc

# zsh（fpath 方式）
gh completion -s zsh > "${fpath[1]}/_gh"

# fish
gh completion -s fish > ~/.config/fish/completions/gh.fish

# PowerShell（当前会话即时生效）
gh completion -s powershell | Out-String | Invoke-Expression
```

### 6.2 查看账户状态与工作概览

```bash
# 查看登录状态、关联的账号与权限
gh auth status

# 查看当前账号在所有仓库的工作概览（待审查 PR、分配给我的 issue 等）
gh status
```

`gh status` 会把"需要你处理的事情"汇总在一个仪表盘式页面里，适合每天开工第一件事执行。

---

## 完整配置范例：新机器 5 分钟配置脚本

```bash
# 1. 登录
gh auth login

# 2. 基础配置
gh config set editor "code --wait"
gh config set git_protocol ssh

# 3. 常用别名
gh alias set pv "pr view" --clobber
gh alias set co "pr checkout" --clobber
gh alias set mine "issue list --assignee @me" --clobber
gh alias set recent "run list --limit 5" --shell --clobber
gh alias set prs "pr list --author @me" --clobber

# 4. 补全（以 bash 为例）
gh completion -s bash > ~/.gh-completion.bash

# 5. 验收
gh alias list
gh config list
gh status
```

---

## 常见错误与对策

| 新手常见错误 | 报错/现象 | 原因 | 解决办法 |
| --- | --- | --- | --- |
| Windows cmd 下单引号 | 别名内容被截断 | cmd 不识别单引号 | 用双引号：`gh alias set pv "pr view"` |
| 展开内容含 $1 却用双引号 | `$1` 被 shell 提前展开为空 | bash 在 set 时就替换了变量 | 用单引号：`gh alias set x 'issue list --author="$1"'` |
| 别名与内置命令同名 | 报 `alias cannot be set` 或行为不变 | 别名不能覆盖 gh 内置命令 | 换个名字，如 `pv` 而不是 `pr` |
| 忘了 --clobber | 报 `alias pv already exists` | 同名别名已存在 | 加 `--clobber` 覆盖 |
| shell 别名没加 --shell / ! | 管道符被当成 gh 参数 | 未声明 shell 解释 | 展开内容加 `!` 前缀或加 `--shell` |
| 设了 git_protocol ssh 却连不上 | clone/push 报权限错误 | SSH key 未配置或未加 agent | 先配置 SSH key 并 `ssh -T git@github.com` 测试 |
| 补全脚本没生效 | Tab 无补全 | 未 source 补全脚本 | 检查 `.bashrc` 中 source 语句；新开终端生效 |
| 多主机配置混淆 | 配置"没生效" | 设置到了其他 host | 用 `--host github.com` 显式指定主机 |

---

## 一句话记忆

**别名是"自定义唤醒词"（`alias set` 定义、`$1` 插参、`--shell` 解锁管道），配置是"系统设置"（`config set` 改编辑器/协议/分页器），两者都是"配一次、爽很久"的生产力工具。**
