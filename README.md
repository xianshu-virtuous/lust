# MoFox Bot月经插件系统（带淫乱值版）

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.24-blue.svg)](https://github.com/xianshu-virtuous/lust/releases)
[![MoFox](https://img.shields.io/badge/MoFox-Compatible-green.svg)](https://github.com/xianshu-virtuous/MoFox-Bot)

> 🌸 为 MoFox 机器人添加真实的女性生理周期模拟系统

模拟女性月经周期对机器人状态的影响，让机器人具有更真实的生物节律感。包含完整的周期追踪、情绪波动、生理状态模拟和高级淫乱度系统。
本系统的原版系统为https://github.com/bingyv92/lust-system
感谢bingyv92提供的插件原型！

---

## ✨ 特性

### 🩸 月经周期系统
- **完整周期模拟**: 月经期、卵泡期、排卵期、黄体期四个阶段
- **动态状态计算**: 自动计算当前周期天数、阶段、剩余天数
- **生理影响模拟**: 不同阶段的体力、情绪、欲望值动态变化
- **可配置周期**: 自定义周期长度、经期天数、立即开始等参数

### 💭 KFC提示词集成
- **多模式注入**: 
  - `unified`: 统一在所有提示词中注入
  - `override`: 替换原有提示词
  - `hybrid`: 混合模式，根据情况选择
- **优先级控制**: 可设置提示词注入优先级
- **场景适配**: 自动适配不同对话场景（正常回复、及时回复、延迟回复等）

### 💕 淫乱度系统
- **动态欲望追踪**: 实时计算和更新欲望值
- **高潮阈值**: 可配置的高潮触发阈值
- **月经期抑制**: 经期自动降低欲望增长
- **阶段描述**: 不同周期阶段的欲望状态描述
- **自然衰减**: 欲望值随时间自然衰减

### 🎮 命令系统
5个完整命令支持所有功能操作：
- `/月经状态`: 查看当前周期状态和详细信息
- `/记录月经 [日期]`: 记录月经开始日期（支持指定日期或默认今天）
- `/月经设置`: 查看当前插件配置
- `/淫乱度状态`: 查看当前淫乱度系统状态
- `/结束淫乱度`: 手动结束淫乱度状态

---

## 📦 安装

### 方法一：使用 MoFox 包管理器（推荐）

```bash
python -m mofox plugin install mofox_period_plugin
```

### 方法二：手动安装

1. 下载最新版本:
   ```bash
   # 从 Releases 页面下载 mofox_period_plugin_v2.0.24_FINAL.tar.gz
   ```

2. 解压到插件目录:
   ```bash
   tar -xzf mofox_period_plugin_v2.0.24_FINAL.tar.gz
   cd mofox_period_plugin_v2.0.24
   ```

3. 复制到 MoFox 插件目录:
   ```bash
   # Windows
   xcopy /E /I mofox_period_plugin_v2.0.24 "F:\OneKey-Plus-2.5.4\core\Bot\plugins\mofox_period_plugin\"
   
   # Linux/Mac
   cp -r mofox_period_plugin_v2.0.24 /path/to/mofox/plugins/mofox_period_plugin/
   ```

4. 重启 MoFox

---

## ⚙️ 配置

配置文件位于: `plugins/mofox_period_plugin/config.toml`

### 基础配置

```toml
[plugin]
enabled = true                    # 启用插件
config_version = "2.0"           # 配置版本

[cycle]
cycle_length = 30                # 周期长度（天）
menstrual_duration = 5           # 月经持续时间（天）
immediate_start = false          # 是否立即开始新周期
```

### 月经期配置

```toml
[[cycle.menstrual_days]]
day = 1                          # 第几天
severity = "heavy"               # 严重程度: light/moderate/heavy
physical_impact = 0.8            # 体力影响系数 (0.0-1.0)
psychological_impact = 0.6       # 心理影响系数 (0.0-1.0)
description = "月经第一天，身体虚弱"
```

完整的5天配置示例：

| 天数 | 严重程度 | 体力影响 | 心理影响 | 描述 |
|------|---------|---------|---------|------|
| 1-2 | heavy | 0.8 | 0.6 | 身体虚弱，情绪低落 |
| 3 | moderate | 0.5 | 0.4 | 症状缓解 |
| 4-5 | light | 0.2 | 0.2 | 接近结束 |

### KFC集成配置

```toml
[kfc_integration]
enabled = true                   # 启用KFC提示词集成
mode = "unified"                 # 模式: unified/override/hybrid
priority = 100                   # 优先级（数字越大优先级越高）

# 注入的提示词类型
inject_to_prompt_types = [
    "replyer_context_normal",
    "replyer_context_in_time",
    "replyer_context_late",
    "situation_new_message"
]
```

### 淫乱度系统配置

```toml
[lust_system]
enabled = true                   # 启用淫乱度系统
menstrual_lust_mode = "disabled" # 经期淫乱模式: disabled/reduced/normal
orgasm_threshold = 100.0         # 高潮阈值
main_threshold = 60.0            # 主要阈值
base_decay_rate = 0.1            # 基础衰减率

# 周期阶段欲望描述
[lust_system.phase_desire_descriptions]
menstrual_desire = "虚弱"
follicular_desire = "平稳上升"
ovulation_desire = "极强"
luteal_desire = "波动"

# 各阶段欲望衰减率
[lust_system.lust_decay_rates]
menstrual_low_decay = 0.05
follicular_low_decay = 0.3
ovulation_low_decay = 0.9
luteal_low_decay = 0.5

menstrual_suppression = 0.0      # 经期抑制系数
```

### 调试配置

```toml
[debug]
debug_mode = false               # 开启调试模式
```

调试日志位置: `logs/mofox_period_plugin.log`

---

## 🎯 使用示例

### 基础使用

```
用户: /月经状态
机器人: 📅 当前周期状态：
        周期第12天 | 卵泡期
        距离下次月经还有18天
        体力状态：良好
        情绪状态：稳定
        欲望指数：★★★☆☆

用户: /记录月经 2024-12-01
机器人: ✅ 已记录月经开始日期：2024-12-01
        新的周期已开始

用户: /月经设置
机器人: ⚙️ 当前配置：
        周期长度：30天
        经期天数：5天
        KFC集成：已启用
        淫乱度系统：已启用
```

### 淫乱度系统

```
用户: /淫乱度状态
机器人: 💕 淫乱度系统状态：
        当前欲望值：45.2
        状态：正常
        阶段影响：卵泡期（欲望平稳上升）
        距离高潮阈值：54.8

用户: /结束淫乱度
机器人: ✅ 淫乱度状态已重置
```

### 自动提示词注入

当KFC集成启用时，机器人的回复会自动考虑当前生理状态：

```
# 月经期
机器人: [自动考虑：身体虚弱，情绪低落的状态进行回复]

# 排卵期
机器人: [自动考虑：精力充沛，欲望较强的状态进行回复]
```

---

## 🏗️ 架构说明

### 插件组件

```
mofox_period_plugin/
├── plugin.py                    # 插件主类
├── config.toml                  # 配置文件
├── config_schema.py             # 配置模式定义
├── components/
│   ├── commands.py              # 5个命令类
│   ├── handlers.py              # 周期状态更新处理器
│   ├── lust_scoring_handler.py  # 淫乱度评分处理器
│   ├── prompts.py               # 周期状态提示词
│   └── jailbreak_prompt.py      # 越狱提示词
├── core/
│   ├── calculator.py            # 周期计算引擎
│   ├── state_manager.py         # 状态管理器
│   └── database.py              # 数据库接口
└── utils/
    └── time_utils.py            # 时间工具函数
```

### 命令系统

所有命令继承自 `PlusCommand`:

```python
class PeriodStatusCommand(PlusCommand):
    command_name = "月经状态"
    command_aliases = ["经期状态", "周期状态", "period_status"]
    command_description = "查询当前的月经周期状态和相关信息"
    command_usage = "/月经状态"
    
    async def execute(self, args: CommandArgs):
        # 命令逻辑
        await self.send_text(response)
        return True, "查询成功", True
```

### 事件处理器

Handler继承自 `BaseEventHandler`:

```python
class PeriodStateUpdateHandler(BaseEventHandler):
    handler_name = "period_state_updater"
    handler_description = "定期更新月经周期状态"
    init_subscribe = [EventType.ON_START]
    
    @classmethod
    def get_handler_info(cls):
        return ActionInfo(
            name=cls.handler_name,
            description=cls.handler_description,
            component_type=ComponentType.ACTION
        )
```

---

## 🔧 开发指南

### 添加新命令

1. 在 `components/commands.py` 中创建新命令类:

```python
class MyNewCommand(PlusCommand):
    command_name = "我的命令"
    command_aliases = ["别名1", "别名2"]
    command_description = "命令描述"
    command_usage = "/我的命令 [参数]"
    chat_type_allow = ChatType.PRIVATE
    
    async def execute(self, args: CommandArgs):
        # 实现命令逻辑
        await self.send_text("命令响应")
        return True, "执行成功", True
```

2. 在 `plugin.py` 中注册:

```python
from components.commands import MyNewCommand

# 在 get_plugin_components 方法中
components.append((MyNewCommand.get_plus_command_info(), MyNewCommand))
```

### 添加新Handler

1. 创建Handler类:

```python
class MyHandler(BaseEventHandler):
    handler_name = "my_handler"
    handler_description = "处理器描述"
    init_subscribe = [EventType.ON_START]
    
    @classmethod
    def get_handler_info(cls):
        return ActionInfo(
            name=cls.handler_name,
            description=cls.handler_description,
            component_type=ComponentType.ACTION
        )
    
    async def execute(self, params: dict) -> HandlerResult:
        # 处理逻辑
        return HandlerResult(success=True, continue_process=True)
```

2. 注册Handler:

```python
components.append((MyHandler.get_handler_info(), MyHandler))
```

### 调试技巧

1. 启用调试模式:
   ```toml
   [debug]
   debug_mode = true
   ```

2. 查看日志:
   ```bash
   tail -f logs/mofox_period_plugin.log
   ```

3. 测试命令:
   ```python
   # 在命令中添加调试日志
   logger.debug(f"命令参数: {args}")
   logger.info(f"执行结果: {result}")
   ```

---

## 🐛 故障排除

### 插件无法加载

**症状**: MoFox启动时未检测到插件

**解决方案**:
1. 检查插件目录结构是否完整
2. 确认 `config.toml` 中 `enabled = true`
3. 查看 MoFox 日志中的错误信息

### 命令无响应

**症状**: 发送命令后无任何反应

**解决方案**:
1. 确认命令格式正确（包含 `/` 前缀）
2. 检查是否在正确的聊天类型中（私聊/群聊）
3. 查看插件日志 `logs/mofox_period_plugin.log`

### 配置不生效

**症状**: 修改配置后无变化

**解决方案**:
1. 确认配置文件语法正确（TOML格式）
2. 重启 MoFox 以加载新配置
3. 检查配置版本号是否匹配

### ActionInfo 初始化错误

**症状**: `ActionInfo.__init__() missing 1 required positional argument: 'component_type'`

**解决方案**:
- 确保使用 v2.0.24 或更高版本
- 该版本已修复此问题

---

## 📚 API参考

### 核心类

#### `PeriodCalculator`
周期计算引擎

```python
from core.calculator import PeriodCalculator

calculator = PeriodCalculator(config)
status = calculator.get_full_status(last_period_date)
# 返回: dict with keys: cycle_day, phase, days_until_next, etc.
```

#### `StateManager`
状态管理器

```python
from core.state_manager import get_last_period_date, save_period_date

# 获取上次月经日期
last_date = get_last_period_date()

# 保存新的月经日期
save_period_date(datetime.now())
```

### 配置访问

```python
# 在命令或Handler中
cycle_length = self.get_config("cycle.cycle_length", 30)
enabled = self.get_config("plugin.enabled", False)
```

---

## 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

### 贡献流程

1. Fork 本仓库
2. 创建特性分支: `git checkout -b feature/my-feature`
3. 提交更改: `git commit -am 'Add some feature'`
4. 推送到分支: `git push origin feature/my-feature`
5. 提交 Pull Request

### 代码规范

- 使用 Python 3.10+ 类型注解
- 遵循 PEP 8 代码风格
- 为新功能添加文档和测试
- 保持向后兼容性

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🔗 相关链接

- **MoFox Bot 主仓库**: [https://github.com/xianshu-virtuous/MoFox-Bot](https://github.com/xianshu-virtuous/MoFox-Bot)
- **问题反馈**: [Issues](https://github.com/xianshu-virtuous/lust/issues)
- **更新日志**: [CHANGELOG.md](CHANGELOG.md)
- **发布页面**: [Releases](https://github.com/xianshu-virtuous/lust/releases)

---

## 🙏 致谢

- MoFox Bot 框架开发团队
- 所有贡献者和测试用户
- 提供反馈和建议的社区成员

---

## 📮 联系方式

如有问题或建议，欢迎通过以下方式联系：

- GitHub Issues: [提交问题](https://github.com/xianshu-virtuous/lust/issues)
- Pull Requests: [贡献代码](https://github.com/xianshu-virtuous/lust/pulls)

---

**Made with ❤️ for MoFox Community**
