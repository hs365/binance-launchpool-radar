import requests
import json
import argparse

def get_aevo_pre_launch_price(ticker):
    """从 Aevo 获取盘前交易(Pre-launch)的最新价格"""
    url = "https://api.aevo.xyz/rest/markets"
    try:
        response = requests.get(url)
        markets = response.json()
        for market in markets:
            # 匹配盘前交易的代币
            if market['instrument_type'] == 'PERP' and ticker.upper() in market['instrument_name']:
                # 获取该市场的最新标记价格
                price_url = f"https://api.aevo.xyz/rest/ticker?instrument_name={market['instrument_name']}"
                price_res = requests.get(price_url).json()
                return float(price_res.get('mark_price', 0))
    except Exception as e:
        return f"获取价格失败: {e}"
    return None

def generate_report(ticker, initial_supply):
    """生成估值分析报告"""
    print(f"🔍 正在启动 OpenClaw Binance Launchpool 估值雷达...")
    print(f"📡 正在抓取 {ticker} 的场外 Aevo 盘前价格...\n")
    
    price = get_aevo_pre_launch_price(ticker)
    
    if not price:
        print(f"⚠️ 暂未在 Aevo 找到 {ticker} 的盘前交易数据，请确认是否已上线盘前合约。")
        return

    # 计算初始流通市值 (Initial Market Cap)
    initial_mc = price * initial_supply
    
    # 历史 Launchpool 首日平均市值参考 (例如 3亿 - 5亿美元)
    avg_mc_low = 300_000_000
    avg_mc_high = 500_000_000
    
    print("========================================")
    print(f"📊 【{ticker}】Launchpool 首日估值测算报告 📊")
    print("========================================")
    print(f"💰 Aevo 场外盘前价格: ${price:.4f}")
    print(f"🪙 初始流通量: {initial_supply / 1_000_000:.2f} 百万枚")
    print(f"💎 测算初始流通市值 (MC): ${initial_mc / 1_000_000:.2f} 百万")
    print("----------------------------------------")
    print("💡 【OpenClaw 智能操作建议】:")
    
    if initial_mc > avg_mc_high:
        print(f"🚨 警报: 当前测算市值(${initial_mc/1_000_000:.0f}M) 远高于近期 Launchpool 平均水平(${avg_mc_high/1_000_000:.0f}M)！")
        print("📉 建议: 盘前存在严重泡沫 (FOMO)，开盘如有空投/挖矿筹码，建议开盘前 5 分钟内果断抛售。绝不建议二级市场接盘！")
    elif initial_mc < avg_mc_low:
        print(f"🟢 提示: 当前测算市值(${initial_mc/1_000_000:.0f}M) 低于近期平均水平(${avg_mc_low/1_000_000:.0f}M)。")
        print("📈 建议: 存在被低估可能。如果开盘遭遇恐慌砸盘，导致价格跌破盘前价 20% 以上，可考虑小仓位分批建仓博反弹。")
    else:
        print(f"🟡 提示: 当前测算市值(${initial_mc/1_000_000:.0f}M) 处于合理区间。")
        print("⚖️ 建议: 定价充分。建议开盘后观察 15 分钟 K 线走势，优先逢高派发免费筹码，二级市场谨慎参与。")
    print("========================================")
    print("🛡️ 安全提示：本报告由 OpenClaw Agent 自动生成，仅供参考，不构成投资建议。")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launchpool 估值雷达")
    parser.add_argument("--ticker", type=str, required=True, help="代币名称，如 PORTAL")
    parser.add_argument("--supply", type=float, required=True, help="初始流通量，如 167000000")
    args = parser.parse_args()
    
    generate_report(args.ticker, args.supply)