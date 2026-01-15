# src/config.py

# SERP Engine Configuration
# Google News 对应的引擎 ID 是 "google_news"
ENGINE_CONFIG = {
    "engine": "google_news",
    "default_country": "us",
    "default_lang": "en",
    "default_num": 20
}

# 输出字段定义 (用于清洗数据)
EXPORT_FIELDS = ["title", "source", "date", "snippet", "link", "thumbnail"]