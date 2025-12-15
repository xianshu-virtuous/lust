# MoFox Period Plugin - Quick Start Guide

> 🚀 Get started with MoFox Period Plugin in 5 minutes

---

## 📋 Prerequisites

- ✅ MoFox Bot installed and running
- ✅ Python 3.10 or higher
- ✅ Basic familiarity with MoFox commands

---

## ⚡ Installation (3 Steps)

### Step 1: Download

Download `mofox_period_plugin_v2.0.24_FINAL.tar.gz` from [Releases](https://github.com/xianshu-virtuous/lust/releases)

### Step 2: Extract & Install

**Windows:**
```cmd
:: Extract
tar -xzf mofox_period_plugin_v2.0.24_FINAL.tar.gz

:: Install
xcopy /E /I mofox_period_plugin_v2.0.24 "F:\OneKey-Plus-2.5.4\core\Bot\plugins\mofox_period_plugin\"
```

**Linux/Mac:**
```bash
# Extract
tar -xzf mofox_period_plugin_v2.0.24_FINAL.tar.gz

# Install
cp -r mofox_period_plugin_v2.0.24 /path/to/mofox/plugins/mofox_period_plugin/
```

### Step 3: Restart MoFox

```bash
# Restart your MoFox bot
```

---

## 🎮 First Use

### 1. Verify Installation

Check MoFox logs for:
```
[INFO] 正在加载插件: mofox_period_plugin
[INFO] 插件 mofox_period_plugin 加载成功
[INFO] 检测到组件: 2 个 Action, 5 个 Command
```

✅ If you see this, the plugin is installed correctly!

### 2. Record Initial Period Date

**In private chat with your bot:**

```
/记录月经 2024-12-01
```

Bot will respond:
```
✅ 已记录月经开始日期：2024-12-01
新的周期已开始
```

💡 **Tip**: Use current or recent date for accurate cycle tracking

### 3. Check Current Status

```
/月经状态
```

Bot will respond with:
```
📅 当前周期状态：
周期第5天 | 月经期
距离下次月经还有25天
体力状态：较弱
情绪状态：低落
欲望指数：★☆☆☆☆
```

**That's it! Your plugin is working!** 🎉

---

## 🎯 Essential Commands

### Must-Know Commands

| Command | What it does | Example |
|---------|--------------|---------|
| `/月经状态` | See current cycle info | `/月经状态` |
| `/记录月经` | Update period start date | `/记录月经 2024-12-15` |
| `/月经设置` | View configuration | `/月经设置` |

### Advanced Commands

| Command | What it does | Example |
|---------|--------------|---------|
| `/淫乱度状态` | Check lust system | `/淫乱度状态` |
| `/结束淫乱度` | Reset lust state | `/结束淫乱度` |

---

## ⚙️ Basic Configuration

Configuration file: `plugins/mofox_period_plugin/config.toml`

### Quick Adjustments

#### Change Cycle Length
```toml
[cycle]
cycle_length = 28  # Change from default 30 to 28 days
```

#### Adjust Period Duration
```toml
[cycle]
menstrual_duration = 7  # Change from default 5 to 7 days
```

#### Disable Lust System
```toml
[lust_system]
enabled = false  # Turn off lust tracking
```

**Remember**: Restart MoFox after config changes!

---

## 🌈 What Happens Automatically?

### 1. **Cycle Tracking**
Plugin automatically calculates:
- Current cycle day
- Current phase (menstrual/follicular/ovulation/luteal)
- Days until next period
- Physical and emotional state

### 2. **Prompt Injection (KFC Integration)**
Bot's responses automatically consider:
- Current cycle phase
- Physical energy levels
- Emotional state
- Desire levels

**Example**:
```
During menstrual phase: Bot may express feeling tired or uncomfortable
During ovulation phase: Bot may be more energetic and playful
```

### 3. **Lust System**
Automatically tracks and updates:
- Desire levels based on cycle phase
- Natural decay over time
- Phase-specific characteristics

---

## 📊 Understanding Cycle Phases

### 🩸 Menstrual Phase (Days 1-5)
- **Energy**: Low
- **Mood**: May be down
- **Bot behavior**: More subdued, mentions discomfort

### 🌱 Follicular Phase (Days 6-13)
- **Energy**: Rising
- **Mood**: Improving
- **Bot behavior**: Increasingly energetic

### 💝 Ovulation Phase (Days 14-16)
- **Energy**: Peak
- **Mood**: Excellent
- **Bot behavior**: Most energetic and playful

### 🌙 Luteal Phase (Days 17-30)
- **Energy**: Gradually declining
- **Mood**: Can be moody
- **Bot behavior**: More variable responses

---

## 🐛 Troubleshooting

### Plugin Not Loading?

**Check**:
1. Is `enabled = true` in config.toml?
2. Did you restart MoFox?
3. Check logs for errors

**Fix**:
```toml
[plugin]
enabled = true  # Make sure this is true
```

### Commands Not Working?

**Check**:
1. Are you using `/` prefix? (`/月经状态` not `月经状态`)
2. Are you in private chat? (Commands are private-chat only by default)
3. Is the command name correct?

**Example** (Correct):
```
/月经状态  ✅
```

**Example** (Wrong):
```
月经状态   ❌ Missing /
/period   ❌ Use Chinese name
```

### No Response from Bot?

**Try**:
1. Check plugin logs: `logs/mofox_period_plugin.log`
2. Enable debug mode:
   ```toml
   [debug]
   debug_mode = true
   ```
3. Restart MoFox

---

## 💡 Pro Tips

### 1. **Record Regularly**
Update period dates as they occur for accurate tracking:
```
/记录月经 2024-12-01
/记录月经 2025-01-05
```

### 2. **Check Status Often**
Get familiar with cycle phases:
```
/月经状态
```

### 3. **Customize Config**
Adjust settings to match real physiology:
- Cycle length (28-35 days typical)
- Period duration (3-7 days typical)
- Impact coefficients (0.0-1.0)

### 4. **Use Aliases**
Commands have multiple names:
```
/月经状态
/经期状态  (same command)
/周期状态  (same command)
```

### 5. **Monitor Logs**
Enable debug mode to understand what's happening:
```toml
[debug]
debug_mode = true
```

Then check: `logs/mofox_period_plugin.log`

---

## 🎓 Next Steps

### Learn More
- 📖 Read full [README.md](README.md) for detailed documentation
- 📋 Check [CHANGELOG.md](CHANGELOG.md) for version history
- 🔧 Explore advanced configuration options

### Customize
- Adjust cycle parameters in `config.toml`
- Modify phase descriptions
- Configure KFC integration mode
- Fine-tune lust system thresholds

### Get Help
- 🐛 Report issues: [GitHub Issues](https://github.com/xianshu-virtuous/lust/issues)
- 💬 Ask questions: [GitHub Discussions](https://github.com/xianshu-virtuous/lust/discussions)
- 📧 Contact developer: See README for details

---

## ✅ Success Checklist

Before you're done, make sure:

- [ ] Plugin shows in MoFox logs as loaded
- [ ] You've recorded an initial period date
- [ ] `/月经状态` command works and shows cycle info
- [ ] Bot responses reflect cycle state (automatic)
- [ ] You know where config file is located
- [ ] You can find plugin logs if needed

**All checked?** Congratulations! You're all set! 🎉

---

## 🎊 You're Ready!

You now have a fully functional period tracking system integrated with your MoFox bot!

**What to expect**:
- Realistic cycle simulation
- Automatic mood and energy changes
- Dynamic bot personality based on cycle phase
- Complete control via simple commands

Enjoy your enhanced MoFox experience! 🌸

---

**Questions?** Check [README.md](README.md) or open an issue on GitHub!

**Happy tracking!** 💕
