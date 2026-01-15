# src/utils.py
import os
import json
import pandas as pd
from typing import List, Dict

def parse_serp_news(data: Dict) -> List[Dict]:
    """
    Parse raw SERP API response into flat news items.
    Robustly handles different API response keys.
    """
    results = []
    
    # 1. 尝试匹配所有可能的列表 Key
    # 优先级：news_results > news > organic_results > organic
    target_key = None
    possible_keys = ["news_results", "news", "organic_results", "organic"]
    
    for key in possible_keys:
        if key in data and isinstance(data[key], list) and len(data[key]) > 0:
            target_key = key
            break
            
    # 2. 调试逻辑：如果找不到数据，打印现有 Keys 帮助排查
    if not target_key:
        print(f"\n⚠️  [DEBUG] No news list found. Response Keys: {list(data.keys())}")
        # 如果返回了错误信息，打印出来
        if "error" in data:
            print(f"⚠️  [DEBUG] API Error: {data['error']}")
        # 如果有 search_metadata，打印状态
        if "search_metadata" in data:
            print(f"⚠️  [DEBUG] Metadata: {data['search_metadata']}")
        return []

    raw_list = data[target_key]
    
    for item in raw_list:
        news = {
            "title": item.get("title"),
            "source": item.get("source"),
            "date": item.get("date"),
            "snippet": item.get("snippet"),
            "link": item.get("link"),
            "thumbnail": item.get("thumbnail")
        }
        results.append(news)
        
    return results

def save_to_csv(data: List[Dict], filename: str):
    """Save list of dicts to CSV"""
    if not data:
        return
    
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    print(f"💾 Saved {len(data)} items to: {filepath}")

def save_to_json(data: List[Dict], filename: str):
    if not data:
        return
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💾 Saved {len(data)} items to: {filepath}")