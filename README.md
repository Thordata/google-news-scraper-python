# 📰 Google News Scraper (Powered by Thordata)

A simple, copy‑pasteable **Google News scraper** using
[Thordata SERP API](https://github.com/Thordata/thordata-python-sdk).

> Disclaimer: This project is not affiliated with or endorsed by Google.

---

## ✨ Features

- Search **Google News** for any query.
- Retrieve title, link, source, snippet, and date.
- Print results as a table.
- Optionally save results to CSV for further analysis.

Under the hood it uses:

- `thordata-sdk` – Official Python SDK for Thordata.
- Thordata **SERP API** in `news` mode.

---

## ⚙️ Setup

### 1. Clone

```bash
git clone https://github.com/Thordata/google-news-scraper.git
cd google-news-scraper
```

### 2. Create .env

Copy the example file and fill in your Thordata tokens from the dashboard:

```bash
cp .env.example .env   # Windows: copy .env.example .env
```

You should set at least:

```
THORDATA_SCRAPER_TOKEN
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the example script from the repo root:

```bash
python examples/scrape_news.py \
  --query "pizza" \
  --num 5 \
  --gl ru \
  --hl es \
  --outfile news_pizza_ru_es.csv
```

Optional flags:

- `--location "United States"` – geo‑target results.
- `--outfile news.csv` – save results to CSV.

Parameters

The script supports the following Google News parameters (as documented in Thordata Docs):

- `--query / -q` → `q`: search query (required)
- `--num`        → `num`: number of results
- `--gl`         → `gl`: country code (e.g. `us`, `ru`, `uk`)
- `--hl`         → `hl`: interface language (e.g. `en`, `es`, `zh-CN`)
- `--topic-token`        → `topic_token` (e.g. `World`, `Business`, `Technology`)
- `--publication-token`  → `publication_token` (e.g. `CNN`, `BBC`)
- `--section-token`      → `section_token` (e.g. `Business`, `Economy`)
- `--story-token`        → `story_token` (story ID)
- `--so`                 → `so`: sort order (`1` for date, default is relevance)

Example output:

```
Searching Google News for: 'AI data infrastructure'
Received 10 results.

Top results:
                                     title                                  link             source  ...
   Thordata raises Series A to build AI data infra  https://example.com/....  SomeTechBlog  ...
   ...
```

---

## 🧩 Related Projects

- [Thordata Python SDK](https://github.com/Thordata/thordata-python-sdk) – Official SDK.
- [Thordata Cookbook](https://github.com/Thordata/thordata-cookbook) – RAG pipelines, GitHub intel, Web QA, MCP tools.
- [Thordata Proxy Examples](https://github.com/Thordata/thordata-proxy-examples) – Simple proxy usage examples in Python & curl.

---

## 📝 Notes

- Please respect the terms of service of the sites you scrape.
- Do not commit your `.env` file or real tokens.

---