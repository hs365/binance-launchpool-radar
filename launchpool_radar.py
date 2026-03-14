#!/usr/bin/env python3
"""
Binance Launchpool Radar - v2.1.0
监控 Binance Launchpool 项目，支持价格提醒和项目分析
"""

import requests
import time
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# API 配置
BINANCE_API_BASE = "https://api.binance.com"
CACHE_DURATION = 300  # 缓存时间（秒）

class Cache:
    """简单缓存机制"""
    def __init__(self):
        self._cache = {}
        self._timestamps = {}
    
    def get(self, key: str) -> Optional[any]:
        if key in self._cache:
            if time.time() - self._timestamps[key] < CACHE_DURATION:
                return self._cache[key]
        return None
    
    def set(self, key: str, value: any):
        self._cache[key] = value
        self._timestamps[key] = time.time()

# 全局缓存
cache = Cache()

class BinanceLaunchpoolRadar:
    """Binance Launchpool 雷达"""
    
    def __init__(self, api_key: str = None, secret_key: str = None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
    
    def get_launchpool_projects(self) -> List[Dict]:
        """获取 Launchpool 项目列表（适配新版 API）"""
        # 尝试从缓存获取
        cached = cache.get("launchpool_projects")
        if cached:
            return cached
        
        try:
            url = f"{BINANCE_API_BASE}/sapi/v1/launchpool/project"
            # 如果有 API Key 可以添加签名
            params = {}
            if self.api_key:
                params["apiKey"] = self.api_key
            
            response = self.session.get(url, params=params)
            data = response.json()
            
            # 处理新版 API 的 projectStatus 字段
            projects = []
            if "data" in data:
                for p in data["data"]:
                    project = {
                        "projectId": p.get("projectId", ""),
                        "projectName": p.get("projectName", ""),
                        "status": p.get("projectStatus", p.get("status", "")),  # 适配新版 API
                        "tokenName": p.get("tokenName", ""),
                        "tokenSymbol": p.get("tokenSymbol", ""),
                        "totalSupply": p.get("totalSupply", ""),
                        "purchaseToken": p.get("purchaseToken", ""),
                    }
                    projects.append(project)
            
            # 缓存结果
            cache.set("launchpool_projects", projects)
            return projects
            
        except Exception as e:
            print(f"获取 Launchpool 项目失败: {e}")
            return []
    
    def get_spot_price(self, symbol: str) -> Optional[float]:
        """获取现货价格"""
        cache_key = f"price_{symbol}"
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        try:
            url = f"{BINANCE_API_BASE}/api/v3/ticker/price"
            params = {"symbol": symbol.upper()}
            response = self.session.get(url, params=params)
            data = response.json()
            
            if "price" in data:
                price = float(data["price"])
                cache.set(cache_key, price)
                return price
        except Exception as e:
            print(f"获取价格失败: {e}")
        return None
    
    def get_multiple_prices(self, symbols: List[str]) -> Dict[str, float]:
        """批量获取价格"""
        prices = {}
        for symbol in symbols:
            price = self.get_spot_price(symbol)
            if price:
                prices[symbol.upper()] = price
        return prices
    
    def check_token_listing(self, token_symbol: str) -> bool:
        """检查代币是否已上线现货市场"""
        try:
            url = f"{BINANCE_API_BASE}/api/v3/ticker/24hr"
            params = {"symbol": f"{token_symbol.upper()}USDT"}
            response = self.session.get(url, params=params)
            return response.status_code == 200
        except:
            return False
    
    def analyze_project(self, project_name: str) -> Dict:
        """分析项目基本信息"""
        projects = self.get_launchpool_projects()
        
        # 查找项目
        target_project = None
        for p in projects:
            if project_name.lower() in p.get("projectName", "").lower():
                target_project = p
                break
        
        if not target_project:
            return {"error": "项目未找到"}
        
        # 基本分析
        token_symbol = target_project.get("tokenSymbol", "")
        
        analysis = {
            "projectName": target_project.get("projectName", ""),
            "tokenName": target_project.get("tokenName", ""),
            "tokenSymbol": token_symbol,
            "status": target_project.get("status", ""),
            "totalSupply": target_project.get("totalSupply", ""),
            "purchaseToken": target_project.get("purchaseToken", ""),
        }
        
        # 检查是否上线
        if token_symbol:
            analysis["listed"] = self.check_token_listing(token_symbol)
        
        # 简单风险评估（基于状态）
        status = target_project.get("status", "")
        if status == "ENDED":
            analysis["riskLevel"] = "低（已结束）"
        elif status == "OPENING":
            analysis["riskLevel"] = "中（进行中）"
        else:
            analysis["riskLevel"] = "中（即将上线）"
        
        return analysis
    
    def set_price_alert(self, symbol: str, price: float) -> Dict:
        """设置价格提醒（模拟）"""
        alert = {
            "id": f"alert_{int(time.time())}",
            "symbol": symbol.upper(),
            "targetPrice": price,
            "createdAt": datetime.now().isoformat(),
            "status": "active"
        }
        print(f"✅ 价格提醒设置成功: {symbol} @ ${price}")
        return alert
    
    def list_alerts(self) -> List[Dict]:
        """列出所有价格提醒"""
        # 模拟数据
        return [
            {"id": "alert_1", "symbol": "BTC", "targetPrice": 50000, "status": "active"},
            {"id": "alert_2", "symbol": "ETH", "targetPrice": 3000, "status": "active"},
        ]


def main():
    """主函数"""
    radar = BinanceLaunchpoolRadar()
    
    print("=" * 50)
    print("Binance Launchpool Radar v2.1.0")
    print("=" * 50)
    
    # 获取项目列表
    print("\n📡 正在获取 Launchpool 项目...")
    projects = radar.get_launchpool_projects()
    
    if projects:
        print(f"\n发现 {len(projects)} 个 Launchpool 项目:\n")
        for p in projects:
            print(f"  • {p.get('projectName', 'N/A')} ({p.get('tokenSymbol', 'N/A')})")
            print(f"    状态: {p.get('status', 'N/A')}")
    else:
        print("\n⚠️ 暂无 Launchpool 项目")
    
    # 获取主流币种价格
    print("\n💰 主流币种价格:")
    prices = radar.get_multiple_prices(["BTC", "ETH", "BNB", "SOL"])
    for symbol, price in prices.items():
        print(f"  {symbol}: ${price:,.2f}")
    
    print("\n" + "=" * 50)
    print("功能说明:")
    print("  launchpool list    - 查看项目列表")
    print("  launchpool details - 查看项目详情")
    print("  price <币种>       - 查询价格")
    print("  alert set          - 设置价格提醒")
    print("  analysis           - 项目分析")
    print("=" * 50)


if __name__ == "__main__":
    main()
