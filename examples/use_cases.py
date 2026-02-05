"""
Use Case Examples for Google News Scraper
Demonstrates various real-world scenarios
"""
import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.scraper import GoogleNewsScraper
from src.ai_news import AINewsBriefing
from src.utils import save_to_json, save_to_csv

load_dotenv()

def example_1_daily_ai_briefing():
    """
    Use Case 1: Daily AI News Briefing
    Perfect for staying updated on AI developments
    """
    print("\n" + "="*60)
    print("Use Case 1: Daily AI News Briefing")
    print("="*60)
    
    ai_briefing = AINewsBriefing()
    briefing = ai_briefing.get_latest_ai_news(num=30, no_cache=True)
    
    save_to_json(briefing["latest_news"], "daily_ai_briefing.json")
    print(f"Saved {len(briefing['latest_news'])} articles")
    print(f"Covered {briefing['summary']['topics_covered']} topics")

def example_2_research_topic_monitoring():
    """
    Use Case 2: Research Topic Monitoring
    Track specific research areas over time
    """
    print("\n" + "="*60)
    print("Use Case 2: Research Topic Monitoring")
    print("="*60)
    
    scraper = GoogleNewsScraper()
    
    research_topics = [
        "quantum computing",
        "climate change solutions",
        "renewable energy"
    ]
    
    all_results = []
    for topic in research_topics:
        results = scraper.search(topic, num=10, no_cache=True)
        all_results.extend(results)
        print(f"Found {len(results)} articles for '{topic}'")
    
    save_to_csv(all_results, "research_monitoring.csv")
    print(f"\nTotal articles collected: {len(all_results)}")

def example_3_market_intelligence():
    """
    Use Case 3: Market Intelligence
    Compare news across different countries
    """
    print("\n" + "="*60)
    print("Use Case 3: Market Intelligence")
    print("="*60)
    
    scraper = GoogleNewsScraper()
    countries = ["us", "uk", "jp", "cn"]
    topic = "tech industry"
    
    for country in countries:
        results = scraper.search(topic, num=15, country=country)
        filename = f"market_intelligence_{country}.json"
        save_to_json(results, filename)
        print(f"{country.upper()}: {len(results)} articles saved to {filename}")

def example_4_competitive_intelligence():
    """
    Use Case 4: Competitive Intelligence
    Monitor competitor news and announcements
    """
    print("\n" + "="*60)
    print("Use Case 4: Competitive Intelligence")
    print("="*60)
    
    scraper = GoogleNewsScraper()
    competitors = ["OpenAI", "Google DeepMind", "Anthropic"]
    
    for competitor in competitors:
        results = scraper.search(competitor, num=10, no_cache=True)
        filename = f"competitor_{competitor.replace(' ', '_')}.json"
        save_to_json(results, filename)
        print(f"{competitor}: {len(results)} recent articles")

def example_5_ai_breakthroughs_tracking():
    """
    Use Case 5: AI Breakthroughs Tracking
    Focus on major AI announcements and breakthroughs
    """
    print("\n" + "="*60)
    print("Use Case 5: AI Breakthroughs Tracking")
    print("="*60)
    
    ai_briefing = AINewsBriefing()
    breakthroughs = ai_briefing.get_ai_breakthroughs(num=15)
    
    save_to_json(breakthroughs, "ai_breakthroughs.json")
    print(f"Tracked {len(breakthroughs)} AI breakthroughs")
    
    # Display top 3
    print("\nTop 3 Breakthroughs:")
    for i, item in enumerate(breakthroughs[:3], 1):
        print(f"{i}. {item.get('title', 'N/A')[:70]}...")
        print(f"   Source: {item.get('source', 'N/A')}")

def example_6_content_aggregation():
    """
    Use Case 6: Content Aggregation
    Aggregate news from multiple sources for content creation
    """
    print("\n" + "="*60)
    print("Use Case 6: Content Aggregation")
    print("="*60)
    
    scraper = GoogleNewsScraper()
    topics = [
        "artificial intelligence",
        "machine learning",
        "data science"
    ]
    
    aggregated = []
    for topic in topics:
        results = scraper.search(topic, num=20)
        aggregated.extend(results)
    
    # Remove duplicates
    seen = set()
    unique = []
    for item in aggregated:
        link = item.get("link", "")
        if link and link not in seen:
            seen.add(link)
            unique.append(item)
    
    save_to_json(unique, "content_aggregation.json")
    print(f"Aggregated {len(unique)} unique articles from {len(topics)} topics")

if __name__ == "__main__":
    print("Google News Scraper - Use Case Examples")
    print("="*60)
    
    # Run examples (comment out ones you don't want to run)
    example_1_daily_ai_briefing()
    # example_2_research_topic_monitoring()
    # example_3_market_intelligence()
    # example_4_competitive_intelligence()
    # example_5_ai_breakthroughs_tracking()
    # example_6_content_aggregation()
    
    print("\n" + "="*60)
    print("Examples completed!")
    print("="*60)
