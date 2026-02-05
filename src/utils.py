# src/utils.py
import os
import json
import pandas as pd
import logging
from typing import List, Dict, Any

logger = logging.getLogger("GoogleNewsScraper")

def parse_serp_news(data: Dict) -> List[Dict]:
    """
    Parse raw SERP API response into flat news items.
    Robustly handles different API response keys and formats.
    
    Args:
        data: Raw SERP API response dictionary
        
    Returns:
        List of parsed news items
    """
    results = []
    
    if not isinstance(data, dict):
        logger.warning("Response is not a dictionary")
        return []
    
    # 1. Try to match all possible list keys
    # Priority: news_results > news > organic_results > organic
    target_key = None
    possible_keys = ["news_results", "news", "organic_results", "organic"]
    
    for key in possible_keys:
        if key in data and isinstance(data[key], list) and len(data[key]) > 0:
            target_key = key
            break
    
    # 2. If standard keys not found, try to find other possible news data keys
    if not target_key:
        # Check if there are other keys containing news data
        for key in data.keys():
            if isinstance(data[key], list) and len(data[key]) > 0:
                # Check if the first element in the list contains news-related fields
                first_item = data[key][0] if data[key] else {}
                if isinstance(first_item, dict):
                    if any(field in first_item for field in ["title", "headline", "link", "url"]):
                        target_key = key
                        logger.debug(f"Found news data in key: {key}")
                        break
            
    # 3. Debug logic: If no data found, print available keys for troubleshooting
    if not target_key:
        available_keys = list(data.keys())
        logger.warning(f"No news list found. Response Keys: {available_keys}")
        
        # Check if there's search information
        if "search_metadata" in data:
            metadata = data.get("search_metadata", {})
            status = metadata.get("status", "unknown")
            logger.info(f"Search status: {status}")
        
        # Check if there's AI overview (in some cases, only AI overview may be returned, no news list)
        if "google_ai_overview" in data:
            logger.info("Response contains AI overview but no news results. This may be normal for some queries.")
        
        # If error information is returned, print it
        if "error" in data:
            error_info = data["error"]
            if isinstance(error_info, dict):
                logger.error(f"API Error: {error_info.get('message', error_info)}")
            else:
                logger.error(f"API Error: {error_info}")
        
        return []

    raw_list = data[target_key]
    
    # 3. Parse each news item
    for item in raw_list:
        if not isinstance(item, dict):
            continue
            
        # Extract news information, supporting multiple possible field names
        news = {
            "title": item.get("title") or item.get("headline"),
            "source": item.get("source") or item.get("publisher"),
            "date": item.get("date") or item.get("published_date") or item.get("time"),
            "snippet": item.get("snippet") or item.get("description") or item.get("summary"),
            "link": item.get("link") or item.get("url"),
            "thumbnail": item.get("thumbnail") or item.get("image") or item.get("thumbnail_image")
        }
        
        # Only add news items with both title and link
        if news["title"] and news["link"]:
            results.append(news)
        else:
            logger.debug(f"Skipping incomplete news item: {item}")
        
    return results

def save_to_csv(data: List[Dict], filename: str):
    """Save list of dicts to CSV"""
    if not data:
        return
    
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8-sig")
    _safe_print(f"[SAVED] Saved {len(data)} items to: {filepath}")

def save_to_json(data: List[Dict], filename: str):
    if not data:
        return
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    _safe_print(f"[SAVED] Saved {len(data)} items to: {filepath}")

def _safe_print(message: str):
    """Print message safely, handling encoding issues on Windows"""
    try:
        print(message)
    except UnicodeEncodeError:
        # Fallback: remove emoji and special characters for Windows console
        import re
        safe_message = re.sub(r'[^\x00-\x7F]+', '', message)
        print(safe_message)