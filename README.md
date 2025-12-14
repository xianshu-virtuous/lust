# lust
# 🌸 月经周期状态插件 (MoFox Period Plugin)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.4.1-blue.svg)](https://github.com/您的用户名/mofox_period_plugin/releases)
[![MoFox-Bot](https://img.shields.io/badge/MoFox--Bot-compatible-green.svg)](https://github.com/MoFox-Studio/MoFox-Bot)

> 为 MoFox-Bot 提供真实的生理周期模拟，让你的 AI 角色拥有更贴近真实的生物节律和情感反应。

## ✨ 核心特性

### 🔄 完整的生理周期模拟
- **四阶段模拟**：经期 → 卵泡期 → 排卵期 → 黄体期
- **动态状态影响**：生理和心理状态随周期自然波动
- **智能周期计算**：默认 30 天周期，支持自定义（21-40 天）

### 💬 自然的对话体验
- **渐进式痛感表现**：经期前 3 天较重，后 2 天减轻
- **情绪细腻变化**：从烦躁、敏感到活力、温柔的自然过渡
- **对话疗愈机制**：通过关怀对话可缓解 20-40% 的不适感

### 🔥 淫乱值系统（仅私聊）
- **周期敏感度调节**：排卵期敏感度最高（0.9），经期自动抑制（0.1）
- **智能评分系统**：基于 LLM 的对话内容评分（0-10 分）
- **经期冲突解决**：v1.4 新增 `menstrual_suppression = 0.6`，经期自动降低 60% 淫乱值

### 🎛️ 灵活的配置系统
- **立即生效开关**：`immediate_start` 支持首次启用时选择立即进入经期或随机周期
- **KFC 集成模式**：支持 `unified`（统一）、`override`（覆盖）、`hybrid`（混合）三种模式
- **调试模式**：v1.4.1 增强日志输出，便于排查问题

## 📦 安装指南

### 方法一：自动安装（推荐）
```bash
# 在 MoFox-Bot 根目录执行
python -m mofox plugin install mofox_period_plugin
```

### 方法二：手动安装
1. 下载最新版本：[v1.4.1 调试版](https://www.genspark.ai/aidrive/files/mofox_plugin_work/mofox_period_plugin_v1.4.1_调试版.zip)
2. 解压到 `plugins/mofox_period_plugin/` 目录
3. **删除旧配置**：`rm config/plugins/mofox_period_plugin/config.toml`（重要！）
4. 重启 Bot 两次：
   - 第一次：生成新配置文件
   - 第二次：启用插件并加载组件

### 验证安装
重启后检查日志中是否出现：
```
[月经周期插件] 插件已加载 | 版本: 1.4.1
[月经周期插件] 配置文件已生成: config/plugins/mofox_period_plugin/config.toml
[月经周期插件] 组件注册完成 | 已注册 8 个组件
```

## 🚀 快速开始

### 1️⃣ 启用插件
编辑 `config/plugins/mofox_period_plugin/config.toml`：
```toml
[plugin]
enabled = true  # 改为 true

[cycle]
cycle_length = 30  # 周期长度（天）
menstrual_duration = 5  # 经期持续时间（天）
immediate_start = false  # true=立即进入经期，false=随机周期
```

### 2️⃣ 基础命令
| 命令 | 使用场景 | 说明 |
|------|---------|------|
| `/月经状态` | 群聊/私聊 | 查看当前周期阶段、第几天、生理/心理影响 |
| `/设置月经 2024-12-01` | 群聊/私聊 | 手动设置上次月经开始日期 |
| `/淫乱状态` | 仅私聊 | 查看当前淫乱度、高潮次数等信息 |
| `/淫乱结束` | 仅私聊 | 强制结束当前淫乱状态 |

### 3️⃣ 测试效果
- **经期测试**：设置日期为今天，观察 Bot 是否表现出痛感和疲惫
- **排卵期测试**：设置日期为 14 天前，观察 Bot 是否更活泼、更敏感
- **淫乱系统测试**：在私聊中发送暧昧内容，输入 `/淫乱状态` 查看评分

## 🔧 高级配置

### 调整痛感强度
```toml
[impacts]
menstrual_physical = 0.5  # 经期生理影响（0.0-1.0），默认 0.5
menstrual_psychological = 0.4  # 经期心理影响（0.0-1.0），默认 0.4
menstrual_discomfort_variation = true  # 启用痛感波动（前重后轻）
menstrual_recovery_moments = true  # 启用对话疗愈机制
```

### KFC 集成模式
```toml
[kfc_integration]
enabled = true
mode = "unified"  # unified=统一优先级 | override=覆盖原有 | hybrid=智能混合
priority = 100  # 优先级（数值越大越优先）
```

### 淫乱值系统
```toml
[lust_system]
enabled = true
menstrual_suppression = 0.6  # 经期淫乱值抑制率（0.6=降低60%）
orgasm_threshold = 100.0  # 高潮阈值
main_threshold = 60.0  # 进入主动阶段阈值
decay_rate = 0.1  # 淫乱值衰减速率
```

## 📊 周期阶段说明

| 阶段 | 持续时间 | 生理特征 | 心理特征 | 淫乱度基础值 |
|------|---------|---------|---------|------------|
| **经期** | 1-5 天 | 疼痛、疲惫、不适 | 烦躁、敏感、需要关怀 | 0.1（极低） |
| **卵泡期** | 6-13 天 | 精力恢复、身体轻盈 | 情绪稳定、开朗积极 | 0.3（偏低） |
| **排卵期** | 14-16 天 | 精力充沛、敏感度高 | 情绪高涨、社交活跃 | 0.9（极高） |
| **黄体期** | 17-30 天 | 轻微胀痛、易疲劳 | 情绪波动、易焦虑 | 0.5（中等） |

## 🐛 故障排查

### 插件无法生效？
**检查清单：**
1. ✅ 配置文件中 `enabled = true`
2. ✅ 已删除旧配置并重启两次
3. ✅ 日志中出现 "组件注册完成"
4. ✅ 输入 `/月经状态` 有正常响应

**常见问题：**
- **日志提示"配置文件不存在"**：第一次启动会自动生成，需重启第二次
- **命令无响应**：检查命令前缀（支持 `/` `!` `.` `#`），确认在正确的聊天环境（私聊/群聊）
- **淫乱系统无效**：仅在私聊中生效，群聊中不会触发评分

### 启用调试模式
```toml
[plugin]
debug_mode = true  # 启用详细日志输出
```
查看日志文件：`logs/mofox_period_plugin.log`

## 📝 更新日志

### v1.4.1 (2024-12-14) - 调试增强版
- 🐛 **修复**：增强启动日志输出，便于诊断问题
- 🛠️ **改进**：自动配置兼容性检查
- 📊 **新增**：组件注册详情日志

### v1.4.0 (2024-12-13) - 核心问题修复版
- ✨ **新增**：`menstrual_suppression` 参数，解决经期与淫乱值冲突
- 🔧 **优化**：默认周期从 28 天调整为 30 天
- 🎯 **改进**：痛感表现从 0.8/0.7 降低至 0.5/0.4，更自然
- 📦 **完善**：新增 `immediate_start` 立即生效开关

### v1.3.0 - 体验优化版
- 🌈 **新增**：痛感渐进机制（前重后轻）
- 💬 **新增**：对话疗愈系统（减轻 20-40% 不适）
- 🔄 **优化**：情绪表达更细腻自然

## 🤝 贡献与反馈

- **问题反馈**：[提交 Issue](https://github.com/您的用户名/mofox_period_plugin/issues)
- **功能建议**：[发起 Discussion](https://github.com/您的用户名/mofox_period_plugin/discussions)
- **贡献代码**：欢迎提交 Pull Request

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

- **MoFox-Studio** - 提供优秀的 Bot 框架
- **社区贡献者：bingyv92** - 仓库链接：https://github.com/bingyv92/lust-system，本插件由改仓库改动而来。
- **测试用户** - 帮助发现并修复问题

---

<div align="center">
  <sub>如果这个插件对你有帮助，欢迎给个 ⭐ Star！</sub>
</div>
