# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-02-05

### Added
- **AI News Briefing**: One-command feature to get latest AI industry news (`--ai-brief`)
- **AI Breakthroughs**: Dedicated command for AI breakthroughs (`--ai-breakthroughs`)
- **Response Caching**: In-memory cache with 5-minute TTL for instant repeated queries
- **Retry Mechanism**: Exponential backoff retry (up to 3 attempts) for reliable requests
- **Progress Indicators**: Visual feedback for long-running operations
- **Enhanced Error Handling**: Better error messages and graceful degradation
- **Comprehensive Test Suite**: 8 tests covering all major functionality
- **Use Case Examples**: 6 real-world usage scenarios
- **Full English Internationalization**: All code, comments, and documentation in English

### Changed
- Upgraded to `thordata-sdk>=1.7.0`
- Migrated from `serp_search()` to `serp_search_advanced()` with `SerpRequest`
- Improved data parsing to handle multiple response formats
- Enhanced output formatting and user experience
- Better error messages and logging

### Performance
- **99%+ faster** for cached queries (<0.1s vs ~3s)
- Average response time: ~2-4s (first request), <0.1s (cached)
- Improved reliability with automatic retry mechanism

### Fixed
- Windows encoding issues (GBK compatibility)
- Test failures in country parameter tests
- Result count limiting (API may return more than requested)
- Error handling for edge cases

### Documentation
- Comprehensive README with AI news feature highlights
- Detailed usage examples and use cases
- API documentation in docstrings
- Complete changelog

## [1.0.0] - Initial Release

### Added
- Basic Google News scraping functionality
- Support for country, language, and device parameters
- JSON and CSV output formats
- Basic error handling
