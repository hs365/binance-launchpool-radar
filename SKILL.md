---
name: binance-crypto-radar
description: 加密货币雷达工具，支持两种模式：(1)现货实时监控-查询BTC/ETH等已上线币种的实时行情和技术分析 (2)Launchpool估值-测算币安新币盘前估值和买卖建议。用于加密货币投资分析。
metadata:
  version: 2.0.0
  author: hs365
license: MIT
---

# OpenClaw 加密货币雷达工具 v2.0

支持两种模式：现货实时监控 + Launchpool盘前估值

## 模式一：现货实时监控

查询已上线币种的实时行情和技术分析。

### 使用方法

```bash
python launchpool_radar.py --mode spot --ticker 代币符号
```

### 示例

```bash
# 查询 BTC 实时行情
python launchpool_radar.py --mode spot --ticker BTC

# 查询 ETH 实时行情
python launchpool_radar.py --mode spot --ticker ETH

# 查询 SOL 实时行情
python launchpool_radar.py --mode spot --ticker SOL
```

### 输出示例

```
🔍 正在启动 OpenClaw 现货监控雷达...
📡 正在查询 BTC 实时行情...

========================================
📊 【BTC】现货实时监控报告 📊
========================================
💰 当前价格: $67,000.00
📈 24h涨跌: +2.50%
📊 24h成交量: 1,000,000,000 USDT
🔺 24h最高: $69,010.00
📉 24h最低: $64,990.00
----------------------------------------
💡 【OpenClaw 智能分析】:
⚖️ 价格处于中性区间(50%)，建议观望
========================================
🛡️ 风险提示：本报告仅供参考，不构成投资建议。
```

### 支持的币种

BTC, ETH, BNB, SOL, XRP, ADA, DOGE, AVAX, DOT, MATIC, LINK, UNI, ATOM, LTC, FIL 等

---

## 模式二：Launchpool盘前估值

测算币安Launchpool新币的盘前估值和买卖建议。

### 使用方法

```bash
python launchpool_radar.py --mode launchpool --ticker 代币符号 --supply 初始流通量
```

### 示例

```bash
# 分析 SAGA 代币，流通量 9000万
python launchpool_radar.py --mode launchpool --ticker SAGA --supply 90000000
```

### 输出示例

```
🔍 正在启动 OpenClaw Binance Launchpool 估值雷达...
📡 正在抓取 SAGA 的场外 Aevo 盘前价格...

========================================
📊 【SAGA】Launchpool 首日估值测算报告 📊
========================================
💰 Aevo 场外盘前价格: $2.8500 (基于智能预估)
🪙 初始流通量: 90.00 百万枚
💎 测算初始流通市值 (MC): $256.50 百万
----------------------------------------
💡 【OpenClaw 智能操作建议】:
🟢 提示: 当前测算市值($256M) 低于近期均值。
📈 建议: 存在被低估可能。可考虑小仓位分批建仓博反弹。
========================================
🛡️ 安全提示：本报告由 OpenClaw Agent 自动生成，仅供参考，不构成投资建议。
```

---

## 风险提示

⚠️ 本工具仅供参考，不构成投资建议。加密货币投资有风险，入市需谨慎。
