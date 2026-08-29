# GitHub 仓库 Tag 保护规则关闭教学

## 步骤一：进入仓库设置

1. 打开浏览器，访问 https://github.com/fanquanpp/FANDEX-App
2. 确认已登录 fanquanpp 账号
3. 点击仓库主页右上角的 **Settings**（设置）标签

## 步骤二：进入 Tags 保护规则页面

有两种路径：

### 路径 A（推荐，新 UI）
1. 在左侧侧边栏找到 **Rules** -> **Rulesets** 菜单
2. 查看现有的 rulesets 列表
3. 找到包含 "tag creations" 限制的规则集

### 路径 B（旧 UI，Tag Protection）
1. 在左侧侧边栏点击 **Tags** 菜单（如果可见）
2. 直接进入 Tag Protection Rules 页面

## 步骤三：识别并删除/暂停限制规则

### 如果是 Rulesets（新规则）
1. 点击规则名称进入详情
2. 点击右上角 **Edit**（编辑）或 **Delete**（删除）
3. 若编辑：将状态改为 **Disabled** 或删除限制 tag 创建的条件
4. 若删除：直接删除整个 ruleset
5. 保存更改

### 如果是 Tag Protection Rules（旧规则）
1. 查看受保护 tag 模式列表（如 `v*` 表示所有 v 开头的 tag）
2. 点击每条规则右侧的 **Delete**（垃圾桶图标）
3. 确认删除

## 步骤四：验证规则已关闭

1. 回到 **Rules** -> **Rulesets** 页面
2. 确认没有启用中的 tag 限制规则
3. 通知 AI 重试推送 tag 和创建 Release

## 步骤五：发布完成后恢复保护（可选）

发布完成后，如果需要恢复 tag 保护：
1. 回到 **Rules** -> **Rulesets** 页面
2. 创建新 ruleset 或重新启用之前的规则
3. 目标：`refs/tags/*` 或 `refs/tags/v*` 限制创建权限为管理员

---

## 可能遇到的问题

### Q: 找不到 Settings 菜单
A: 确认你是仓库 owner（fanquanpp），如果是组织仓库需要组织管理员权限。

### Q: Rulesets 列表为空
A: 可能规则是在组织级别设置。访问 https://github.com/organizations/<org-name>/settings/rules 查看组织级规则。

### Q: 关闭后仍然推送失败
A: 可能是 GitHub Actions 的环境保护规则，检查 Settings > Branches > Branch protection rules 中 main 分支的设置。

---

## 关键 URL 直达

- 仓库设置：https://github.com/fanquanpp/FANDEX-App/settings
- Rulesets：https://github.com/fanquanpp/FANDEX-App/settings/rules
- Actions 权限：https://github.com/fanquanpp/FANDEX-App/settings/actions

完成规则关闭后，请告知 AI："tag 规则已关闭"，AI 将重试推送 v3.0.0 tag 和创建 Release。
