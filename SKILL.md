# binance-launchpool-radar Skill

监控 Binance Launchpool 项目的 OpenClaw 技能。

## 版本：v2.1.0 (2026-03-14)

## 新增功能

### 1. Binance API 适配
- 支持最新的 `projectStatus` 字段
- 优化错误处理逻辑

### 2. 代币上市提醒
- 当 Launchpool 代币上市现货市场时自动提醒
- 自定义通知阈值

### 3. 项目分析
- 基本项目信息（tokenomics、团队背景）
- 初步风险评估指标

### 4. 性能优化
- 数据缓存机制
- 优化 API 调用频率

---

## 安装

```bash
npx skills add -s binance-launchpool-radar -y -g hs365/binance-launchpool-radar
```

---

## 命令

### Launchpool 命令

```bash
# 查看所有 Launchpool 项目
launchpool list

# 查看项目详情
launchpool details --project <项目名称>

# 查看项目状态
launchpool status
```

### 提醒命令

```bash
# 设置价格提醒
alert set --token <代币> --price <价格>

# 查看所有提醒
alert list

# 删除提醒
alert delete --id <提醒ID>
```

### 分析命令

```bash
# 分析项目
analysis --project <项目名称>

# 查看分析报告
analysis report --project <项目名称>
```

### 现货命令

```bash
# 查询价格
price <代币符号>

# 批量查询
price --list BTC,ETH,BNB
```

---

## 配置

在 `.env` 文件中配置：

```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
NOTIFICATION_WEBHOOK=your_webhook_url
CACHE_ENABLED=true
CACHE_DURATION=300
```

---

## 示例

### 查看 Launchpool 项目

```bash
$ launchpool list
项目名称: NEW
状态: 即将上线
开始时间: 2026-03-15
结束时间: 2026-03-22
```

### 设置价格提醒

```bash
$ alert set --token BNB --price 500
✅ 提醒设置成功！
```

### 分析项目

```bash
$ analysis --project NEW
项目: NEW
代币总量: 100,000,000
初始流通: 20,000,000
风险等级: 中
```

---

## 更新日志

### 2026-03-14
- v2.1.0: 适配 Binance API，新增代币上市提醒和项目分析功能

### 2026-02
- v2.0: 添加现货监控功能

### 2026-01
- v1.0: 初始版本

---

## 支持

如有问题，请提交 Issue：https://github.com/hs365/binance-launchpool-radar/issues
