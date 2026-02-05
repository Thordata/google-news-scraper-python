"""
AI News Briefing Module
One-command feature to get the latest AI industry news and breakthroughs
"""
import time
import logging
from typing import List, Dict
from .scraper import GoogleNewsScraper
from .progress import show_progress

logger = logging.getLogger("GoogleNewsScraper")

# AI-related keywords for comprehensive coverage
AI_KEYWORDS = [
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "neural networks",
    "large language models",
    "LLM",
    "ChatGPT",
    "GPT",
    "OpenAI",
    "AI breakthrough",
    "AI research",
    "generative AI",
    "AGI",
    "artificial general intelligence"
]

class AINewsBriefing:
    """
    AI News Briefing - Get the latest AI industry news with one command
    """
    
    def __init__(self):
        self.scraper = GoogleNewsScraper()
    
    def get_latest_ai_news(
        self,
        num: int = 20,
        country: str = "us",
        language: str = "en",
        no_cache: bool = True
    ) -> Dict[str, any]:
        """
        Get the latest AI news from multiple relevant queries.
        
        Args:
            num: Number of results per query (default: 20)
            country: Country code (default: "us")
            language: Language code (default: "en")
            no_cache: Whether to bypass cache (default: True for fresh news)
        
        Returns:
            Dictionary containing:
            - latest_news: Combined list of all AI news
            - by_topic: News grouped by topic/keyword
            - summary: Brief summary statistics
        """
        all_news = []
        news_by_topic = {}
        
        # Search for each AI-related keyword
        primary_keywords = AI_KEYWORDS[:5]  # Use top 5 keywords to avoid too many requests
        total_keywords = len(primary_keywords)
        
        logger.info(f"Searching {total_keywords} AI-related topics...")
        
        for idx, keyword in enumerate(primary_keywords, 1):
            try:
                show_progress(idx, total_keywords, f"Searching AI topics")
                results = self.scraper.search(
                    query=keyword,
                    num=num // len(primary_keywords) + 1,  # Distribute results across keywords
                    country=country,
                    language=language,
                    no_cache=no_cache
                )
                
                if results:
                    news_by_topic[keyword] = results
                    all_news.extend(results)
                    logger.debug(f"Found {len(results)} articles for '{keyword}'")
                
                # Small delay to avoid rate limiting
                if idx < total_keywords:
                    time.sleep(0.5)
                    
            except Exception as e:
                logger.warning(f"Failed to fetch news for '{keyword}': {e}")
                continue
        
        print()  # New line after progress
        
        # Remove duplicates based on link
        seen_links = set()
        unique_news = []
        for item in all_news:
            link = item.get("link", "")
            if link and link not in seen_links:
                seen_links.add(link)
                unique_news.append(item)
        
        # Sort by date (most recent first) - approximate sorting
        # Note: Date parsing would be needed for accurate sorting
        
        return {
            "latest_news": unique_news[:num],  # Limit to requested number
            "by_topic": news_by_topic,
            "summary": {
                "total_articles": len(unique_news),
                "topics_covered": len(news_by_topic),
                "keywords_searched": primary_keywords
            }
        }
    
    def get_ai_breakthroughs(
        self,
        num: int = 10,
        country: str = "us"
    ) -> List[Dict]:
        """
        Get the latest AI breakthroughs and major announcements.
        Focuses on breakthrough-related keywords.
        
        Args:
            num: Number of results (default: 10)
            country: Country code (default: "us")
        
        Returns:
            List of breakthrough news items
        """
        breakthrough_keywords = [
            "AI breakthrough",
            "AI research breakthrough",
            "new AI model",
            "AI innovation",
            "AI advancement"
        ]
        
        all_breakthroughs = []
        
        for keyword in breakthrough_keywords:
            try:
                results = self.scraper.search(
                    query=keyword,
                    num=num // len(breakthrough_keywords) + 1,
                    country=country,
                    language="en",
                    no_cache=True
                )
                if results:
                    all_breakthroughs.extend(results)
            except Exception:
                continue
        
        # Remove duplicates
        seen_links = set()
        unique_breakthroughs = []
        for item in all_breakthroughs:
            link = item.get("link", "")
            if link and link not in seen_links:
                seen_links.add(link)
                unique_breakthroughs.append(item)
        
        return unique_breakthroughs[:num]
