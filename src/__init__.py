"""
Google News Scraper Package
A Python library for scraping Google News via Thordata SERP API
"""

__version__ = "2.0.0"
__author__ = "Thordata Developer Team"

from .scraper import GoogleNewsScraper
from .ai_news import AINewsBriefing

__all__ = [
    "GoogleNewsScraper",
    "AINewsBriefing",
]
