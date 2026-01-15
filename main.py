# main.py
import argparse
from dotenv import load_dotenv
from src.scraper import GoogleNewsScraper
from src.utils import save_to_csv, save_to_json

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Google News Scraper (SERP API)")
    
    parser.add_argument("query", help="Search topic (e.g. 'Artificial Intelligence')")
    parser.add_argument("--limit", type=int, default=20, help="Max results")
    parser.add_argument("--country", type=str, default="us", help="Country code (us, uk, jp...)")
    parser.add_argument("--format", type=str, default="json", choices=["json", "csv"], help="Output format")

    args = parser.parse_args()
    
    scraper = GoogleNewsScraper()
    results = scraper.search(args.query, num=args.limit, country=args.country)
    
    if results:
        filename = f"news_{args.query.replace(' ', '_')}.{args.format}"
        if args.format == "csv":
            save_to_csv(results, filename)
        else:
            save_to_json(results, filename)

if __name__ == "__main__":
    main()