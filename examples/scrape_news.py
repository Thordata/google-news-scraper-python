"""
Google News Scraper powered by Thordata SERP API.

Features:
- Search Google News for a given query.
- Print results as a table.
- Optionally save to CSV.

Usage:

    1. Copy .env.example to .env and fill in THORDATA_* variables.
    2. Install deps: pip install -r requirements.txt
    3. Run:

        python examples/scrape_news.py \
            --query "AI data infrastructure" \
            --num 10 \
            --outfile news_ai_data.csv
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
from dotenv import load_dotenv

from thordata import ThordataClient, Engine


ROOT_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(ENV_PATH)


def build_client() -> ThordataClient:
    scraper_token = os.getenv("THORDATA_SCRAPER_TOKEN")
    public_token = os.getenv("THORDATA_PUBLIC_TOKEN")
    public_key = os.getenv("THORDATA_PUBLIC_KEY")

    if not scraper_token:
        raise RuntimeError(
            "THORDATA_SCRAPER_TOKEN is missing. "
            "Please create a .env file and set your tokens."
        )

    return ThordataClient(
        scraper_token=scraper_token,
        public_token=public_token or "",
        public_key=public_key or "",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Google News scraper using Thordata SERP API",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Search query for Google News.",
    )
    parser.add_argument(
        "--num",
        type=int,
        default=10,
        help="Number of news results to fetch.",
    )
    parser.add_argument(
        "--location",
        type=str,
        default=None,
        help="Optional location (e.g. 'United States', 'London').",
    )
    parser.add_argument(
        "--outfile",
        type=str,
        default=None,
        help="Optional CSV file to save results (e.g. news_results.csv).",
    )
    return parser.parse_args()


def search_google_news(
    client: ThordataClient,
    query: str,
    num: int,
    location: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Call Thordata SERP API in 'news' mode and normalize results.

    Note: The exact response structure may vary; we try 'news_results' first
    and fall back to 'organic' if needed.
    """
    extra_params: Dict[str, Any] = {"type": "news"}  # news mode
    if location:
        extra_params["location"] = location

    print(f"Searching Google News for: {query!r}")
    results = client.serp_search(
        query=query,
        engine=Engine.GOOGLE,
        num=num,
        **extra_params,
    )

    # Prefer dedicated news_results if available
    raw_list: List[Dict[str, Any]] = results.get("news_results") or results.get("organic") or []

    cleaned: List[Dict[str, Any]] = []
    for item in raw_list:
        cleaned.append(
            {
                "title": item.get("title"),
                "link": item.get("link"),
                "source": item.get("source") or item.get("news_source"),
                "snippet": item.get("snippet"),
                "date": item.get("date") or item.get("published_time"),
            }
        )

    print(f"Received {len(cleaned)} results.")
    return cleaned


def main() -> None:
    args = parse_args()
    client = build_client()

    articles = search_google_news(
        client,
        query=args.query,
        num=args.num,
        location=args.location,
    )

    if not articles:
        print("No news results found.")
        return

    df = pd.DataFrame(articles)
    print("\nTop results:")
    print(df.head(10).to_string(index=False))

    if args.outfile:
        out_path = Path(args.outfile).resolve()
        df.to_csv(out_path, index=False, encoding="utf-8")
        print(f"\nSaved {len(df)} results to {out_path}")


if __name__ == "__main__":
    main()