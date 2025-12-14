from src.plugin_system import ConfigField

# 配置Schema定义 - v1.3.0 优化版本
CONFIG_SCHEMA = {
    "plugin": {
        "enabled": ConfigField(
            type=bool,
            default=False,
            description="是否启用月经周期状态插件"
        ),
        "config_version": ConfigField(
            type=str,
            default="1.4.0",
            description="配置文件版本"
        ),
        "debug_mode": ConfigField(
            type=bool,
            default=False,
            description="是否启用调试模式，会输出更多日志信息"
        )
    },
    "cycle": {
        "cycle_length": ConfigField(
            type=int,
            default=30,
            description="完整月经周期长度（天），从月经第一天到下次月经前一天。正常范围21-35天，平均30天",
            example="30"
        ),
        "menstrual_duration": ConfigField(
            type=int,
            default=5,
            description="月经期持续天数（正常3-7天）",
            example="5"
        ),
        "auto_detect": ConfigField(
            type=bool,
            default=True,
            description="是否自动检测和适应周期变化"
        ),
        "immediate_start": ConfigField(
            type=bool,
            default=False,
            description="启用插件时是否立即进入月经期。true=立即月经；false=从周期中随机一天开始"
        )
    },
    "impacts": {
        # 月经期影响（优化：不再极端）
        "menstrual_physical": ConfigField(
            type=float,
            default=0.5,  # 从0.8降低到0.5
            description="月经期生理影响强度 (0-1)，建议0.3-0.6之间",
            example="0.5"
        ),
        "menstrual_psychological": ConfigField(
            type=float,
            default=0.4,  # 从0.7降低到0.4
            description="月经期心理影响强度 (0-1)，建议0.3-0.5之间",
            example="0.4"
        ),
        # 新增：月经期痛苦波动配置
        "menstrual_discomfort_variation": ConfigField(
            type=bool,
            default=True,
            description="月经期痛苦是否随时间波动（true=前3天重，后2天轻）"
        ),
        "menstrual_recovery_moments": ConfigField(
            type=bool,
            default=True,
            description="是否允许月经期出现缓解时刻（温暖关怀、转移注意力时减轻痛苦）"
        ),
        
        # 卵泡期影响
        "follicular_physical": ConfigField(
            type=float,
            default=0.1,
            description="卵泡期生理影响强度 (0-1)",
            example="0.1"
        ),
        "follicular_psychological": ConfigField(
            type=float,
            default=0.1,
            description="卵泡期心理影响强度 (0-1)",
            example="0.1"
        ),
        
        # 排卵期影响
        "ovulation_physical": ConfigField(
            type=float,
            default=0.4,
            description="排卵期生理影响强度 (0-1)",
            example="0.4"
        ),
        "ovulation_psychological": ConfigField(
            type=float,
            default=0.2,
            description="排卵期心理影响强度 (0-1)",
            example="0.2"
        ),
        
        # 黄体期影响
        "luteal_physical": ConfigField(
            type=float,
            default=0.6,
            description="黄体期生理影响强度 (0-1)",
            example="0.6"
        ),
        "luteal_psychological": ConfigField(
            type=float,
            default=0.5,
            description="黄体期心理影响强度 (0-1)",
            example="0.5"
        )
    },
    "kfc_integration": {
        "enabled": ConfigField(
            type=bool,
            default=True,
            description="是否启用KFC（私聊模式）集成"
        ),
        "mode": ConfigField(
            type=str,
            default="unified",
            description="KFC工作模式: unified(统一模式) 或 split(分离模式)",
            example="unified"
        ),
        "priority": ConfigField(
            type=int,
            default=100,
            description="KFC模式下提示词注入的优先级"
        )
    },
    "jailbreak": {
        "enabled": ConfigField(
            type=bool,
            default=True,
            description="是否启用破限系统（开放世界观设定）"
        ),
        "intensity": ConfigField(
            type=str,
            default="medium",
            description="破限强度等级: low(低), medium(中), high(高)",
            example="medium"
        ),
        "enhanced_mode": ConfigField(
            type=bool,
            default=True,
            description="是否在KFC模式下启用增强破限（更深度的内容解锁）"
        )
    },
    "lust_system": {
        "enabled": ConfigField(
            type=bool,
            default=True,
            description="是否启用淫乱度与高潮值子系统（仅KFC模式）"
        ),
        "menstrual_suppression": ConfigField(
            type=float,
            default=0.6,
            description="月经期淫乱度抑制系数（0-1）。0.6表示经期淫乱度降低60%，建议0.5-0.8之间",
            example="0.6"
        ),
        "orgasm_threshold": ConfigField(
            type=float,
            default=100.0,
            description="高潮阈值，达到此值触发高潮",
            example="100.0"
        ),
        "foreplay_threshold": ConfigField(
            type=float,
            default=20.0,
            description="前戏阈值",
            example="20.0"
        ),
        "main_threshold": ConfigField(
            type=float,
            default=60.0,
            description="正戏阈值",
            example="60.0"
        ),
        "base_score_weight": ConfigField(
            type=float,
            default=1.0,
            description="基础得分权重，用于调整LLM评分对高潮值的影响",
            example="1.0"
        ),
        "decay_rate": ConfigField(
            type=float,
            default=0.1,
            description="高潮值衰减率（每秒减少的分数）",
            example="0.1"
        ),
        "post_orgasm_recovery_ratio": ConfigField(
            type=float,
            default=0.4,
            description="高潮后高潮值恢复比例，相对于 main_threshold（例如0.4表示恢复至正戏阈值的40%）",
            example="0.4"
        ),
        "initial_ratio": ConfigField(
            type=float,
            default=0.5,
            description="初始高潮值系数，用于计算初始高潮值（lust_level * foreplay_threshold * initial_ratio）",
            example="0.5"
        ),
        "passive_active_ratio": ConfigField(
            type=float,
            default=0.3,
            description="被动主动阈值系数，用于划分被动未开始和主动未开始（passive_active_threshold = foreplay_threshold * passive_active_ratio）",
            example="0.3"
        ),
        "low_score_threshold": ConfigField(
            type=float,
            default=3.0,
            description="低评分阈值，低于此值视为低评分",
            example="3.0"
        ),
        "low_score_count_to_terminate": ConfigField(
            type=int,
            default=3,
            description="连续低评分次数触发终止",
            example="3"
        ),
        "termination_decay_multiplier": ConfigField(
            type=float,
            default=2.0,
            description="递减机制中的衰减率乘数，用于加速高潮值下降",
            example="2.0"
        ),
        "cooldown_duration": ConfigField(
            type=int,
            default=300,
            description="冷却持续时间（秒），仅用于体力不支终止（高潮次数用尽）",
            example="300"
        ),
        "llm_model": ConfigField(
            type=str,
            default="judge_model",
            description="用于评分的LLM模型名称（可选），使用系统默认judge模型",
            example="judge_model"
        )
    },
    "backup": {
        "auto_backup": ConfigField(
            type=bool,
            default=True,
            description="是否自动备份配置和数据"
        ),
        "backup_days": ConfigField(
            type=int,
            default=30,
            description="备份保留天数"
        )
    }
}
