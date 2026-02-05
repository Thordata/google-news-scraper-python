"""
Google News Scraper
Main scraper class for fetching Google News via SERP API
"""
import os
import logging
import time
from typing import List, Dict, Optional
from thordata import ThordataClient
from thordata.types import SerpRequest
from .config import ENGINE_CONFIG
from .utils import parse_serp_news
from .retry import retry_with_backoff
from .cache import cached, clear_cache

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("GoogleNewsScraper")

class GoogleNewsScraper:
    """
    Google News Scraper using Thordata SERP API
    
    This class provides methods to search Google News using the advanced
    SERP API with support for various parameters like country, language,
    device type, and cache control.
    """
    
    def __init__(self):
        """
        Initialize the scraper with API token from environment variables.
        
        Raises:
            ValueError: If THORDATA_SCRAPER_TOKEN is not set in .env file
        """
        self.api_key = os.getenv("THORDATA_SCRAPER_TOKEN")
        if not self.api_key:
            raise ValueError("THORDATA_SCRAPER_TOKEN is required in .env")
            
        # Only Scraper Token is needed, not Public Token (since we use SERP)
        self.client = ThordataClient(scraper_token=self.api_key)

    @retry_with_backoff(max_retries=3, initial_delay=1.0, backoff_factor=2.0)
    def _perform_search(
        self,
        query: str,
        num: int,
        country: str,
        language: Optional[str],
        device: Optional[str],
        no_cache: bool
    ) -> Dict:
        """
        Internal method to perform the actual API call with retry logic.
        
        Args:
            query: Search query string
            num: Number of results to return
            country: Country code
            language: Language code
            device: Device type
            no_cache: Whether to bypass cache
        
        Returns:
            Raw API response dictionary
        
        Raises:
            Exception: If API call fails after retries
        """
        req = SerpRequest(
            query=query,
            engine="google_news",
            num=num,
            country=country,
            language=language or ENGINE_CONFIG.get("default_lang"),
            device=device,
            output_format="json",
            no_cache=no_cache
        )
        
        return self.client.serp_search_advanced(req)
    
    def search(
        self, 
        query: str, 
        num: int = 20, 
        country: str = "us",
        language: Optional[str] = None,
        device: Optional[str] = None,
        no_cache: bool = False
    ) -> List[Dict]:
        """
        Search Google News by keyword using advanced SERP API.
        
        Features:
        - Automatic retry with exponential backoff
        - Response caching (when no_cache=False)
        - Comprehensive error handling
        
        Args:
            query: Search query string
            num: Number of results to return (default: 20)
            country: Country code (e.g., "us", "uk", "jp", "cn")
            language: Language code (e.g., "en", "zh", "ja"). If None, uses default from config
            device: Device type ("desktop", "mobile", "tablet"). If None, uses default
            no_cache: Whether to bypass cache (default: False)
        
        Returns:
            List of news items with title, source, date, snippet, link, thumbnail
        """
        logger.info(f"Searching Google News for: '{query}' (Country: {country}, Num: {num})")
        
        try:
            # Check cache first (if caching is enabled)
            if not no_cache:
                from .cache import _cache
                cache_key = _cache._make_key("search", query, num, country, language, device)
                cached_result = _cache.get(cache_key)
                if cached_result is not None:
                    logger.info(f"Returning cached results for '{query}' (cache hit)")
                    return cached_result
                logger.debug(f"Cache miss for '{query}'")
            
            # Perform search with retry logic
            start_time = time.time()
            response = self._perform_search(
                query=query,
                num=num,
                country=country,
                language=language,
                device=device,
                no_cache=no_cache
            )
            elapsed = time.time() - start_time
            
            # Parse and clean the data
            news_items = parse_serp_news(response)
            
            # Limit returned results (API may return more than requested)
            if len(news_items) > num:
                news_items = news_items[:num]
                logger.info(f"Found {len(news_items)} news items (limited to {num} as requested) in {elapsed:.2f}s.")
            else:
                logger.info(f"Found {len(news_items)} news items in {elapsed:.2f}s.")
            
            # Cache the results (if caching is enabled)
            if not no_cache:
                from .cache import _cache
                cache_key = _cache._make_key("search", query, num, country, language, device)
                _cache.set(cache_key, news_items, ttl=300)  # Cache for 5 minutes
                logger.debug(f"Cached results for '{query}' (TTL: 300s)")
            
            return news_items

        except Exception as e:
            logger.error(f"Search Failed after retries: {e}", exc_info=True)
            return []
    
    def clear_cache(self):
        """Clear the response cache"""
        clear_cache()
        logger.info("Cache cleared")