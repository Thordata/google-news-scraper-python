"""
Google News Scraper powered by Thordata SERP API.

This script is a "full" implementation following the Thordata docs for
`engine=google_news` and its parameters:

Required:
  - q                : search query

Localization:
  - gl               : country code (e.g. 'us', 'ru', 'uk')
  - hl               : interface language (e.g. 'en', 'es', 'zh-CN')

Advanced:
  - topic_token      : top-level topic (e.g. 'World', 'Business', 'Technology')
  - publication_token: publisher token (e.g. 'CNN', 'BBC')
  - section_token    : section token (e.g. 'Business', 'Economy')
  - story_token      : story token (specific story ID)
  - so               : sort order (e.g. '1' for sort by date, default relevance)

Usage (from repo root):

    python examples/scrape_news.py \\
        --query "AI data infrastructure" \\
        --num 10 \\
        --gl us \\
        --hl en \\
        --topic Technology \\
        --outfile news_ai_data.csv
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
from dotenv import load_dotenv

from thordata import ThordataClient

# -------------------------------------------------------------
# Env & client
# -------------------------------------------------------------

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


# -------------------------------------------------------------
# CLI parsing
# -------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Google News scraper using Thordata SERP API (engine=google_news)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    # Required
    parser.add_argument(
        "--query",
        "-q",
        type=str,
        required=True,
        help="Search query for Google News (q).",
    )

    # Basic options
    parser.add_argument(
        "--num",
        type=int,
        default=10,
        help="Number of news results to fetch.",
    )

    # Localization
    parser.add_argument(
        "--gl",
        type=str,
        default=None,
        help="Country code (gl), e.g. 'us', 'ru', 'uk'.",
    )
    parser.add_argument(
        "--hl",
        type=str,
        default=None,
        help="Interface language (hl), e.g. 'en', 'es', 'zh-CN'.",
    )

    # Advanced parameters
    parser.add_argument(
        "--topic-token",
        type=str,
        default=None,
        help="topic_token: top-level topic (e.g. 'World', 'Business', 'Technology').",
    )
    parser.add_argument(
        "--publication-token",
        type=str,
        default=None,
        help="publication_token: publisher token (e.g. 'CNN', 'BBC').",
    )
    parser.add_argument(
        "--section-token",
        type=str,
        default=None,
        help="section_token: section token (e.g. 'Business', 'Economy').",
    )
    parser.add_argument(
        "--story-token",
        type=str,
        default=None,
        help="story_token: story ID for a specific story.",
    )
    parser.add_argument(
        "--so",
        type=str,
        default=None,
        help="so: sort order (e.g. '1' for sort by date; default is relevance).",
    )

    # Output
    parser.add_argument(
        "--outfile",
        type=str,
        default=None,
        help="Optional CSV file to save results (e.g. news_results.csv).",
    )

    return parser.parse_args()


# -------------------------------------------------------------
# SERP call: engine=google_news
# -------------------------------------------------------------

def search_google_news(
    client: ThordataClient,
    query: str,
    num: int,
    gl: Optional[str] = None,
    hl: Optional[str] = None,
    topic_token: Optional[str] = None,
    publication_token: Optional[str] = None,
    section_token: Optional[str] = None,
    story_token: Optional[str] = None,
    so: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Call Thordata SERP API with engine=google_news and the parameters
    defined in the official documentation.
    """
    # Build kwargs according to docs
    kwargs: Dict[str, Any] = {}

    if gl:
        kwargs["gl"] = gl
    if hl:
        kwargs["hl"] = hl
    if topic_token:
        kwargs["topic_token"] = topic_token
    if publication_token:
        kwargs["publication_token"] = publication_token
    if section_token:
        kwargs["section_token"] = section_token
    if story_token:
        kwargs["story_token"] = story_token
    if so:
        kwargs["so"] = so

    print(f"Searching Google News for: {query!r}")
    if kwargs:
        print("Parameters:", {k: v for k, v in kwargs.items() if v is not None})

    # 按官方示例使用 engine=google_news
    results = client.serp_search(
        query=query,
        engine="google_news",
        num=num,
        **kwargs,
    )

    # 如果有 code 字段且不是 200，优先报错
    if isinstance(results, dict) and results.get("code") and results.get("code") != 200:
        raise RuntimeError(
            f"SERP API error: code={results.get('code')} msg={results.get('msg')}"
        )

    # 1. 优先使用 'news' 字段（你返回里就是这个）
    raw_list = results.get("news")

    # 2. 若 'news' 为空，再尝试 'news_results' / 'organic' / 'data'
    if not isinstance(raw_list, list) or not raw_list:
        for key in ("news_results", "organic", "data"):
            value = results.get(key)
            if isinstance(value, list) and value:
                print(f"Using key '{key}' as result list.")
                raw_list = value
                break

    if not isinstance(raw_list, list):
        raw_list = []

    articles: List[Dict[str, Any]] = []
    for item in raw_list:
        articles.append(
            {
                "title": item.get("title"),
                "link": item.get("link"),
                "source": item.get("source") or item.get("news_source"),

                "date": item.get("date") or item.get("published_time"),
            }
        )

    print(f"Received {len(articles)} results.")
    return articles


# -------------------------------------------------------------
# Main
# -------------------------------------------------------------

def main() -> None:
    args = parse_args()
    client = build_client()

    articles = search_google_news(
        client=client,
        query=args.query,
        num=args.num,
        gl=args.gl,
        hl=args.hl,
        topic_token=args.topic_token,
        publication_token=args.publication_token,
        section_token=args.section_token,
        story_token=args.story_token,
        so=args.so,
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