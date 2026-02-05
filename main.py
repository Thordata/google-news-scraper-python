"""
Google News Scraper - Main Entry Point
Command-line tool for scraping Google News via SERP API
"""
import argparse
from dotenv import load_dotenv
from src.scraper import GoogleNewsScraper
from src.ai_news import AINewsBriefing
from src.utils import save_to_csv, save_to_json

load_dotenv()

def main():
    parser = argparse.ArgumentParser(
        description="Google News Scraper (SERP API)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # AI News Briefing (One-command feature!)
  python main.py --ai-brief
  python main.py --ai-brief --limit 30 --format csv
  
  # AI Breakthroughs
  python main.py --ai-breakthroughs --limit 10
  
  # Basic search
  python main.py "Artificial Intelligence"
  
  # Search with custom limit and country
  python main.py "Crypto Market" --limit 50 --country uk
  
  # Search with language and device type
  python main.py "Tesla News" --limit 30 --country us --language en --device mobile
  
  # Export to CSV
  python main.py "Elon Musk" --format csv --no-cache
        """
    )
    
    parser.add_argument("query", nargs="?", help="Search topic (e.g. 'Artificial Intelligence'). Use --ai-brief for AI news briefing")
    parser.add_argument("--ai-brief", action="store_true", help="Get latest AI industry news and breakthroughs (one-command feature)")
    parser.add_argument("--ai-breakthroughs", action="store_true", help="Get latest AI breakthroughs and major announcements")
    parser.add_argument("--limit", type=int, default=20, help="Max results (default: 20)")
    parser.add_argument("--country", type=str, default="us", help="Country code (us, uk, jp, cn, etc.)")
    parser.add_argument("--language", type=str, default=None, help="Language code (en, zh, ja, etc.). If not specified, uses default")
    parser.add_argument("--device", type=str, default=None, choices=["desktop", "mobile", "tablet"], 
                       help="Device type (default: auto)")
    parser.add_argument("--format", type=str, default="json", choices=["json", "csv"], help="Output format (default: json)")
    parser.add_argument("--no-cache", action="store_true", help="Bypass cache for fresh results")

    args = parser.parse_args()
    
    try:
        # Handle AI news briefing feature
        if args.ai_brief or args.ai_breakthroughs:
            print(f"\n{'='*60}")
            print(f"AI News Briefing")
            print(f"{'='*60}")
            print(f"[INFO] Fetching latest AI industry news...")
            
            ai_briefing = AINewsBriefing()
            
            if args.ai_breakthroughs:
                print(f"[MODE] AI Breakthroughs & Major Announcements")
                results = ai_briefing.get_ai_breakthroughs(
                    num=args.limit,
                    country=args.country
                )
                query_label = "AI_Breakthroughs"
            else:
                print(f"[MODE] Comprehensive AI News Briefing")
                briefing_data = ai_briefing.get_latest_ai_news(
                    num=args.limit,
                    country=args.country,
                    language=args.language or "en",
                    no_cache=True
                )
                results = briefing_data["latest_news"]
                query_label = "AI_News_Briefing"
                
                # Display summary
                summary = briefing_data.get("summary", {})
                print(f"\n[SUMMARY]")
                print(f"  Total Articles: {summary.get('total_articles', 0)}")
                print(f"  Topics Covered: {summary.get('topics_covered', 0)}")
                print(f"  Keywords: {', '.join(summary.get('keywords_searched', []))}")
        else:
            # Regular search
            if not args.query:
                parser.error("Query is required unless using --ai-brief or --ai-breakthroughs")
            
            print(f"\n{'='*60}")
            print(f"Google News Scraper")
            print(f"{'='*60}")
            print(f"[INFO] Initializing...")
            scraper = GoogleNewsScraper()
            
            print(f"\n[SEARCH] Query: '{args.query}'")
            params = []
            if args.country != "us":
                params.append(f"Country: {args.country}")
            if args.language:
                params.append(f"Language: {args.language}")
            if args.device:
                params.append(f"Device: {args.device}")
            if args.no_cache:
                params.append("Cache: Disabled")
            if params:
                print(f"[PARAMS] {', '.join(params)}")
            print(f"[LIMIT] Max results: {args.limit}")
            print(f"\n[STATUS] Searching... Please wait...")
            
            results = scraper.search(
                query=args.query,
                num=args.limit,
                country=args.country,
                language=args.language,
                device=args.device,
                no_cache=args.no_cache
            )
            query_label = args.query
        
        if results:
            # Sanitize filename for safe file system usage
            safe_query = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in query_label)
            filename = f"news_{safe_query.replace(' ', '_')[:50]}.{args.format}"
            if args.format == "csv":
                save_to_csv(results, filename)
            else:
                save_to_json(results, filename)
            print(f"\n{'='*60}")
            print(f"[SUCCESS] Successfully saved {len(results)} news items")
            print(f"[FILE] output/{filename}")
            print(f"{'='*60}")
            
            # Display preview of top 3 results
            print(f"\n[PREVIEW] Top {min(3, len(results))} results:")
            print(f"{'-'*60}")
            for i, item in enumerate(results[:3], 1):
                title = item.get('title', 'N/A')
                if title and len(title) > 70:
                    title = title[:70] + '...'
                source = item.get('source', 'N/A')
                date = item.get('date', 'N/A')
                print(f"\n{i}. {title}")
                print(f"   Source: {source}")
                print(f"   Date: {date}")
                if item.get('snippet'):
                    snippet = item['snippet'][:100] + '...' if len(item['snippet']) > 100 else item['snippet']
                    print(f"   {snippet}")
            print(f"\n{'-'*60}")
            print(f"[TIP] View full results in: output/{filename}")
        else:
            print("\n[WARNING] No results found.")
            print("[TIP] Try:")
            print("  - Using English keywords for better results")
            print("  - Adjusting country/language parameters")
            print("  - Checking if the query is too specific or too broad")
            
    except ValueError as e:
        print(f"\n[ERROR] Configuration Error: {e}")
        print("[TIP] Please make sure THORDATA_SCRAPER_TOKEN is set in your .env file")
    except KeyboardInterrupt:
        print("\n[INFO] Search cancelled by user.")
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        print("[TIP] Check your internet connection and API token validity")

if __name__ == "__main__":
    main()