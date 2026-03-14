# binance-launchpool-radar

监控 Binance Launchpool 项目的技能，可实时获取新项目信息、价格提醒和项目分析。

## 版本：v2.1.0

### 主要更新 (2026-03-14)
1. **适配Binance API变更**
   - 新增 `projectStatus` 字段处理
   - 优化错误处理逻辑

2. **新增代币上市提醒功能**
   - 在代币上市现货市场时发送通知
   - 可自定义通知阈值和通知方式

3. **新增项目基本分析功能**
   - 获取项目基本信息（tokenomics、团队背景）
   - 提供简单的项目评估指标

4. **性能优化**
   - 数据获取逻辑优化
   - 实现数据缓存机制

---

## 功能特性

### 1. Launchpool 项目监控
- 实时获取 Binance Launchpool 新项目
- 项目状态追踪（即将上线、进行中、已结束）
- 历史项目查询

### 2. 价格提醒
- 自定义价格阈值提醒
- 多币种支持（BTC、ETH、BNB等）
- 实时价格监控

### 3. 项目分析
- 项目基本信息
- Tokenomics 分析
- 初步风险评估

### 4. 现货监控
- 支持 BTC/ETH 等主流币种实时查询
- 价格数据实时更新
- 市场趋势分析

---

## 安装

```bash
npx skills add -s binance-launchpool-radar@latest -y -g hs365/binance-launchpool-radar
```

或

```bash
npx skills add -s binance-launchpool-radar -y -g hs365/binance-launchpool-radar
```

---

## 使用方法

### 基本用法

```bash
# 查看帮助
fluxa-wallet help

# 获取 Launchpool 项目列表
fluxa-wallet launchpool list

# 获取特定项目详情
fluxa-wallet launchpool details --project <项目名称>

# 设置价格提醒
fluxa-wallet alert set --token <代币符号> --price <价格阈值>

# 查看项目分析
fluxa-wallet analysis --project <项目名称>
```

### 配置说明

1. **代币上市提醒配置**：
   - 在配置文件中设置通知阈值
   - 支持多种通知方式（TG、邮件等）

2. **项目分析配置**：
   - 可自定义分析指标
   - 支持导出分析报告

---

## 更新日志

### v2.1.0 (2026-03-14)
- ✅ 适配 Binance API 最新变更
- ✅ 新增代币上市提醒功能
- ✅ 新增项目基本分析功能
- ✅ 性能优化和数据缓存

### v2.0 (2026-02)
- ✅ 添加现货监控功能
- ✅ 支持 BTC/ETH 等主流币种实时查询
- ✅ 优化数据获取逻辑

### v1.0 (2026-01)
- ✅ 初始版本
- ✅ 基本 Launchpool 项目监控

---

## 技术栈

- Node.js
- Binance API
- OpenClaw Skills

---

## 贡献

欢迎提交 Issue 和 Pull Request！

---

## 许可证

MIT License

---

## 联系方式

- GitHub: https://github.com/hs365/binance-launchpool-radar
- 作者: hs365
