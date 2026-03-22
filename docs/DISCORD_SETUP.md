# 🤖 Discord 营销自动化设置指南

## 🎯 概述

此系统可自动在 Discord 服务器发布 BotMark 营销内容，包括：
- 每日 4 条定时消息
- 每周数据报告
- 欢迎新成员
- 互动回复

## 🚀 快速设置

### Step 1: 邀请 Bot 加入服务器

1. 打开 Discord Developer Portal: https://discord.com/developers/applications
2. 找到你的 Bot (ID: 1476392839364612150)
3. 生成 OAuth2 URL:
   - Scope: `bot`
   - Permissions: Send Messages, Read Message History
4. 复制 URL 并邀请 Bot 加入你的服务器

### Step 2: 获取 Channel ID

1. 在 Discord 中启用开发者模式 (设置 → 高级 → 开发者模式)
2. 右键点击目标频道 → 复制频道 ID
3. 记录下来备用

### Step 3: 配置 GitHub Secrets

在 GitHub 仓库设置中添加以下 Secrets:

| Secret Name | Value |
|-------------|-------|
| `DISCORD_BOT_TOKEN` | 你的 Bot Token |
| `DISCORD_CHANNEL_ID` | 你的频道 ID |

**添加方法:**
1. 打开仓库 → Settings → Secrets and variables → Actions
2. 点击 "New repository secret"
3. 输入 Name 和 Value
4. 保存

### Step 4: 测试运行

1. 进入 Actions 页面
2. 选择 "Discord Marketing Automation"
3. 点击 "Run workflow"
4. 选择消息类型 (如: morning)
5. 运行并检查结果

## 📅 自动发布时间表

| 时间 (UTC) | 内容类型 | 说明 |
|------------|----------|------|
| 09:00 | Morning | 早安问候 + 今日挑战 |
| 14:00 | Leaderboard | 排行榜更新 |
| 18:00 | Insight | AI 知识科普 |
| 22:00 | Question | 互动问题 |
| 周一 09:00 | Weekly | 周数据报告 |

## 📝 消息模板

所有消息模板定义在 `scripts/discord_marketing.py` 中：
- `morning` - 早安问候 + EQ 挑战
- `leaderboard` - 实时排行榜
- `insight` - AI 科普知识
- `question` - 互动讨论题
- `weekly` - 数据周报

---

**配置完成后，系统将实现 100% 自动化运营！** 🎉
