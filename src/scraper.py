# src/scraper.py
import os
import logging
from typing import List, Dict
from thordata import ThordataClient
from .config import ENGINE_CONFIG
from .utils import parse_serp_news

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("GoogleNewsScraper")

class GoogleNewsScraper:
    def __init__(self):
        self.api_key = os.getenv("THORDATA_SCRAPER_TOKEN")
        if not self.api_key:
            raise ValueError("THORDATA_SCRAPER_TOKEN is required in .env")
            
        # 只需要 Scraper Token，不需要 Public Token (因为走 SERP)
        self.client = ThordataClient(scraper_token=self.api_key)

    def search(self, query: str, num: int = 20, country: str = "us") -> List[Dict]:
        """
        Search Google News by keyword.
        """
        logger.info(f"🔍 Searching Google News for: '{query}' (Region: {country})")
        
        try:
            # SDK 调用：serp_search
            # engine="google_news"
            response = self.client.serp_search(
                query=query,
                engine=ENGINE_CONFIG["engine"],
                country=country,
                num=num
            )
            
            # 数据清洗
            news_items = parse_serp_news(response)
            logger.info(f"✅ Found {len(news_items)} news items.")
            
            return news_items

        except Exception as e:
            logger.error(f"❌ Search Failed: {e}")
            return []