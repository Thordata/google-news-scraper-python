"""
Configuration module for Google News Scraper
Contains default settings and mappings
"""

# SERP Engine Configuration
# Google News engine ID is "google_news"
ENGINE_CONFIG = {
    "engine": "google_news",
    "default_country": "us",
    "default_lang": "en",
    "default_num": 20,
    "default_device": None  # None = auto, or "desktop", "mobile", "tablet"
}

# Export field definitions (for data cleaning)
EXPORT_FIELDS = ["title", "source", "date", "snippet", "link", "thumbnail"]

# Supported device types
SUPPORTED_DEVICES = ["desktop", "mobile", "tablet"]

# Common country code mappings
COUNTRY_CODES = {
    "us": "United States",
    "uk": "United Kingdom",
    "jp": "Japan",
    "cn": "China",
    "de": "Germany",
    "fr": "France",
    "es": "Spain",
    "it": "Italy",
    "br": "Brazil",
    "in": "India",
    "au": "Australia",
    "ca": "Canada"
}