#!/usr/bin/env python3
"""
Basic usage example for Google News Scraper
"""
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.scraper import GoogleNewsScraper
from src.utils import save_to_json, save_to_csv

load_dotenv()

def main():
    # Initialize scraper
    scraper = GoogleNewsScraper()
    
    # Example 1: Basic search
    print("=" * 60)
    print("Example 1: Basic Search")
    print("=" * 60)
    results = scraper.search("Artificial Intelligence", num=10)
    print(f"Found {len(results)} news items\n")
    if results:
        for i, item in enumerate(results[:3], 1):
            print(f"{i}. {item['title']}")
            print(f"   Source: {item['source']} | Date: {item['date']}")
            print()
    
    # Example 2: Search with country and language
    print("=" * 60)
    print("Example 2: Search with Country and Language")
    print("=" * 60)
    results = scraper.search(
        "Tesla News", 
        num=5, 
        country="us", 
        language="en"
    )
    print(f"Found {len(results)} news items\n")
    
    # Example 3: Search with device type
    print("=" * 60)
    print("Example 3: Mobile Device Search")
    print("=" * 60)
    results = scraper.search(
        "Crypto Market", 
        num=5, 
        country="uk", 
        device="mobile"
    )
    print(f"Found {len(results)} news items\n")
    
    # Example 4: Save to file
    print("=" * 60)
    print("Example 4: Save Results to File")
    print("=" * 60)
    results = scraper.search("Elon Musk", num=20)
    if results:
        save_to_json(results, "example_news.json")
        save_to_csv(results, "example_news.csv")
        print("Results saved to output/example_news.json and output/example_news.csv")

if __name__ == "__main__":
    main()
