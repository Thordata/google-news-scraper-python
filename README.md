# Google News Scraper for Python

<div align="center">

<img src="https://img.shields.io/badge/Thordata-Official-blue?style=for-the-badge" alt="Thordata Logo">

**Real-time Google News scraping via API. Extract headlines, sources, and dates instantly.**  
*Powered by Thordata's high-speed SERP infrastructure.*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Powered By](https://img.shields.io/badge/Powered%20By-Thordata-orange)](https://www.thordata.com/?utm_source=github&utm_medium=readme&utm_campaign=gnews_scraper)

</div>

---

## 🎯 Quick Start: AI News Briefing

**Get the latest AI industry news with one command!**

```bash
# One command to get latest AI news
python main.py --ai-brief

# Get AI breakthroughs only
python main.py --ai-breakthroughs --limit 10

# Export to CSV
python main.py --ai-brief --format csv --limit 30
```

This feature automatically searches multiple AI-related keywords and combines the results into a comprehensive briefing. Perfect for staying updated on the latest AI developments!

---

## ⚡ Features

*   **🤖 AI News Briefing**: One-command feature to get latest AI industry news and breakthroughs
*   **📰 Real-Time Data**: Get the latest news as it happens (no cache lag when needed).
*   **⚡ Smart Caching**: Automatic response caching (5min TTL) for instant repeated queries
*   **🔄 Auto Retry**: Exponential backoff retry mechanism for reliable requests
*   **📊 Progress Indicators**: Visual feedback for long-running operations
*   **🌍 Global Coverage**: Support for any country (`us`, `uk`, `jp`, `cn`, etc.) and language.
*   **🚀 High Speed**: Synchronous API response (<3s average), cached responses <0.1s
*   **🧹 Clean Output**: Automatically parses complex JSON into simple lists (JSON/CSV).
*   **🌐 Managed Requests:** Uses Thordata's SERP API and proxy infrastructure for request handling.
*   **🔧 Advanced API**: Uses latest `SerpRequest` and `serp_search_advanced` for better control.
*   **📱 Device Support**: Specify device type (desktop, mobile, tablet) for different results.
*   **🌐 Language Control**: Fine-tune language settings for localized results.

---

## 📦 Sample Output

```json
[
  {
    "title": "OpenAI Announces GPT-5 with Revolutionary Capabilities",
    "source": "TechCrunch",
    "date": "2 hours ago",
    "snippet": "OpenAI has unveiled GPT-5, featuring unprecedented reasoning capabilities...",
    "link": "https://techcrunch.com/...",
    "thumbnail": "data:image/png;base64,..."
  },
  {
    "title": "Google DeepMind Breakthrough in Protein Folding",
    "source": "Nature",
    "date": "5 hours ago",
    "snippet": "New AI model predicts protein structures with 95% accuracy...",
    "link": "https://nature.com/...",
    "thumbnail": "data:image/png;base64,..."
  }
]
```

---

## 🚀 Installation & Setup

### 1. Get Your Token

Get your **free** scraping token from the [Thordata Dashboard](https://www.thordata.com/?utm_source=github&utm_medium=readme&utm_campaign=gnews_scraper).

### 2. Install Dependencies

```bash
git clone https://github.com/Thordata/google-news-scraper-python.git
cd google-news-scraper-python
pip install -r requirements.txt
```

### 3. Configure

Copy `.env.example` to `.env` and fill in your token:

```ini
THORDATA_SCRAPER_TOKEN=your_token_here
```

---

## 💡 Usage Examples

### AI News Briefing (Featured!)

```bash
# Get comprehensive AI news briefing
python main.py --ai-brief

# Get AI breakthroughs only
python main.py --ai-breakthroughs --limit 15

# AI news with custom settings
python main.py --ai-brief --limit 50 --country uk --format csv
```

### Basic Search

```bash
# Simple search
python main.py "Artificial Intelligence"

# Search with custom limit
python main.py "Crypto Market" --limit 50
```

### Advanced Search

```bash
# Search with country and language
python main.py "Tesla News" --country uk --language en

# Search with device type
python main.py "AI Updates" --device mobile --no-cache

# Full example with all options
python main.py "Bitcoin Price" \
  --limit 100 \
  --country jp \
  --language ja \
  --device desktop \
  --format csv \
  --no-cache
```

---

## 📋 Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `query` | Search topic (required unless using `--ai-brief`) | - |
| `--ai-brief` | Get latest AI industry news (one-command feature) | False |
| `--ai-breakthroughs` | Get latest AI breakthroughs only | False |
| `--limit` | Maximum number of results | 20 |
| `--country` | Country code (`us`, `uk`, `jp`, `cn`, etc.) | `us` |
| `--language` | Language code (`en`, `zh`, `ja`, etc.) | Auto |
| `--device` | Device type (`desktop`, `mobile`, `tablet`) | Auto |
| `--format` | Output format (`json`, `csv`) | `json` |
| `--no-cache` | Bypass cache for fresh results | False |

---

## 🎨 Use Cases

### 1. Daily AI News Monitoring
```bash
# Run this daily to stay updated
python main.py --ai-brief --limit 30 --format csv
```

### 2. Research & Analysis
```bash
# Collect news for specific research topics
python main.py "machine learning research" --limit 100 --format csv
```

### 3. Market Intelligence
```bash
# Track industry news by country
python main.py "tech industry" --country us --limit 50
python main.py "tech industry" --country uk --limit 50
```

### 4. Content Aggregation
```bash
# Aggregate news from multiple sources
python main.py "climate change" --limit 50 --format json
```

### 5. Competitive Intelligence
```bash
# Monitor competitor news
python main.py "competitor name" --no-cache --limit 20
```

---

## 📁 Output Format

Results are saved to the `output/` directory in your chosen format:

- **JSON**: Structured data with all fields
- **CSV**: Spreadsheet-friendly format

Each file is named based on your query: `news_{query}.{format}`

---

## 🔧 Advanced Configuration

### Environment Variables

```ini
THORDATA_SCRAPER_TOKEN=your_token_here
```

### Programmatic Usage

```python
from src.scraper import GoogleNewsScraper
from src.ai_news import AINewsBriefing

# Basic search (with automatic caching)
scraper = GoogleNewsScraper()
results = scraper.search("AI", num=20, country="us")  # Cached for 5 minutes

# Bypass cache for fresh results
results = scraper.search("AI", num=20, no_cache=True)

# Clear cache manually
scraper.clear_cache()

# AI news briefing
ai_briefing = AINewsBriefing()
briefing = ai_briefing.get_latest_ai_news(num=30)
```

### Performance Features

**Caching**:
- Automatic caching of API responses
- Default TTL: 5 minutes
- Instant response for cached queries (<0.1s)
- Manual cache control available

**Retry Mechanism**:
- Automatic retry on transient failures
- Exponential backoff (1s, 2s, 4s delays)
- Up to 3 retry attempts
- Prevents cascading failures

---

## 🌟 Why This Scraper?

### Compared to Other Solutions

| Feature | This Scraper | Others |
|---------|-------------|--------|
| **AI News Briefing** | ✅ One-command feature | ❌ Manual keyword setup |
| **Smart Caching** | ✅ Automatic (5min TTL) | ❌ No caching |
| **Auto Retry** | ✅ Exponential backoff | ⚠️ Single attempt |
| **Progress Indicators** | ✅ Visual feedback | ❌ No feedback |
| **Real-time Data** | ✅ <3s response, <0.1s cached | ⚠️ Varies |
| **No Bans** | ✅ Managed by Thordata | ⚠️ Risk of blocking |
| **Global Coverage** | ✅ 195+ countries | ⚠️ Limited |
| **Easy Setup** | ✅ 2 minutes | ⚠️ Complex |
| **Output Formats** | ✅ JSON + CSV | ⚠️ Limited |
| **Error Handling** | ✅ Robust with retries | ⚠️ Basic |

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

* Powered by [Thordata](https://www.thordata.com) SERP API
* Built with ❤️ by the Thordata Developer Team

---

## 📞 Support

* **Documentation**: Check this README
* **Issues**: [GitHub Issues](https://github.com/Thordata/google-news-scraper-python/issues)
* **Email**: support@thordata.com

---

## What This Example Does Not Collect

This repository is an example client for authorized Thordata SERP API requests. It does not include Google account credentials, browser cookies, private sessions, or local browser automation.

The example does not grant rights to collect, reuse, train on, or redistribute third-party news content. Use it only for lawful and authorized workflows.

Never place API keys, private URLs, personal information, or private data in source files, logs, README files, or commits.

## Failure Behavior

Requests may fail because of invalid credentials, unsupported parameters, rate limits, endpoint restrictions, or temporary service errors.

When a request fails, treat the response as an error rather than valid news data. Check the terminal output and returned API response for details. Exact error codes and limits depend on the account and endpoint.

## For Coding Assistants

When modifying or running this example:

- Read `.env.example` and keep credentials in environment variables.
- Check the existing configuration before inventing request parameters.
- Preserve the current SERP API request flow.
- Never print or commit API keys, private URLs, or personal data.
- Review returned headlines, sources, dates, and links before sharing them.
- Treat returned news data as third-party data subject to applicable terms and usage restrictions.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 📚 Additional Documentation

* [CHANGELOG.md](CHANGELOG.md) - Version history and changes

---

<div align="center">
  <sub>Built with ❤️ by the Thordata Developer Team.</sub>
</div>
