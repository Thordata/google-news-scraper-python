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

## ⚡ Features

*   **📰 Real-Time Data**: Get the latest news as it happens (no cache lag).
*   **🌍 Global Coverage**: Support for any country (`us`, `uk`, `jp`, `cn`, etc.) and language.
*   **🚀 High Speed**: Synchronous API response (<2s average), no polling required.
*   **🧹 Clean Output**: Automatically parses complex JSON into simple lists (JSON/CSV).
*   **🛡️ No Bans**: Full proxy rotation and anti-bot handling managed by Thordata.

## 📦 Sample Output

```json
[
  {
    "title": "Musk says Tesla is moving Full Self-Driving to a monthly subscription",
    "source": "CNBC",
    "date": "21 hours ago",
    "snippet": null,
    "link": "https://www.cnbc.com/2026/01/14/musk-tesla-full-self-driving-subscription-fsd.html",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAllBMVEUAHloADFQAHFkAGFcAGVMAAE4PJl83RnsjO2gAAFIAAFUAGVYAEVkGHV0GIFUGHlUAF1wkMmC2ucqipLeMmK/T19X8/Pp8iJ+yvsxSW4NZX3q8x813gJYACkwAAETW3eZOVG1YZITL1dmxvMK9vsTg4+lGTGdiZonM1N+Gh5bc5OUAGGObpbqGj7Job5CuqcC+uc/BxtMZTvwUAAAAdElEQVQYlWNgoBZgYmZG4rEwsrKxc3BycfNw8vDyMfALCAoJi4iKiUtISknLyPIzMMjJKyiKKikrCauoCioKMDDws8qrKcqrayhpamnxKnIDjdDmkNDRldPTN9CTMpQBms3EwMTIysjLzCjLCDKUjWouRwYA81AHiFv0f4YAAAAASUVORK5CYII="
  },
  {
    "title": "Tesla’s Full Self-Driving System Will Only Be Available Via Subscription, Musk Says",
    "source": "The Wall Street Journal",
    "date": "19 hours ago",
    "snippet": null,
    "link": "https://www.wsj.com/business/autos/teslas-full-self-driving-system-will-only-be-available-via-subscription-musk-says-87a37904?gaa_at=eafs&gaa_n=AWEtsqcBcJlMRjB4Qj-YWvg0eVlUxx5XzvTDlwAMlvgmX2iTeiEl_Ari3vO3&gaa_ts=6968e56c&gaa_sig=Y3WgajAaNUO9NyVGt-c2i84-OkdUjh1N3v_4V2e1ygdM4CkFFH-bKSkOa9SJX9j3MNnUTwRv9-zjj63QIUzVKw%3D%3D",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAYFBMVEX////c3NwAAAC+vr4mJia6urqRkZG0tLTm5ubf39/IyMj7+/uHh4dBQUGsrKxXV1ednZ3w8PA8PDx2dnYcHByjo6PNzc0PDw8yMjJJSUmNjY0qKir19fV1dXWmpqbLy8uWKfoBAAAAc0lEQVQYla3Pyw6DIBCF4V+mgIBY0KpYe3n/tyxt6sZl00kmOfkWkzPwj4m6P2Nc0pY86AqjbS+In5jg5CrYMShkXmgq1MWVJjqhrHwB5Y2pYbnuEJNXtGRF2D7Q9XlDbgz3R3kfxc50+CRWnuuhUvjtkxcBwwPrTWhR4QAAAABJRU5ErkJggg=="
  },
  {
    "title": "Tesla Stock Drops. Elon Musk Makes a Surprise Decision on FSD.",
    "source": "Barron's",
    "date": "16 hours ago",
    "snippet": null,
    "link": "https://www.barrons.com/articles/tesla-stock-elon-musk-full-self-driving-c641e657?gaa_at=eafs&gaa_n=AWEtsqcX5Q5cHorSQ8AiRzIS5OkJPYQskqyFwOEC1T-NyU7geXPI_4i4Mnl2&gaa_ts=6968e56c&gaa_sig=gb4gi9eXeNVCUO-fE86ISNAndc_djddZbe15NKqTG6s8Jt2usDGAuoDunt0xtDu5JfgSVajNbPPTn4kGZS-FOg%3D%3D",
    "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwEBBgEIBwgKCgkBDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNDg8PGjclHxkrKys3NysrNys3KzcrNysrNzcrKysrKzcrKys3KzcrKys3Nys3KzcrKzcrNys3KzcrN//AABEIABAAEAMBIgACEQEDEQH/xAAWAAADAAAAAAAAAAAAAAAAAAADBAb/xAAnEAABAgQEBgMAAAAAAAAAAAABAgMEBxETAAUGCBIhIjFBoRdRgf/EABUBAQEAAAAAAAAAAAAAAAAAAAMC/8QAFREBAQAAAAAAAAAAAAAAAAAAAEH/2gAMAwEAAhEDEQA/AI3ImNLTLRuauQ19ctoRTzSeIjqCkjwe1CcL5+xpSWTsorbK4dzXsOlx1hZJtqJPYnwQAf3A8pjZZy/Z3OoiluJ+YYUsoKEcVCVJNTzHLpwDM8x05qzLdt0AwVuJkBcN1aaElZBoB9Cns4sMf//Z"
  },
  {
    "title": "The $1 trillion reason Elon Musk ended Tesla FSD purchases",
    "source": "Business Insider",
    "date": "16 hours ago",
    "snippet": null,
    "link": "https://www.businessinsider.com/elon-musk-ended-tesla-fsd-purchases-subscriptions-trillion-compensation-2026-1",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAMFBMVEUAJf8AJf8AG/8AD/////+mq/8AAP9rc//i4//Lzf/t7v8+TP+3u/9bZP+Plf+Ah/89RQUyAAAAAXRSTlP+GuMHfQAAAGFJREFUGJV9z8kOgCAMBFDoRsvm//+tdQkBo85t3qGZhhCXhEd3eQNAT4yIcAEkZu6InQucgEyeLJnSgFoyRZ1AjUxmyEq6AHtrMxyBcRQ2M6tFqjW4h4mIj0KBr+m/74Ydk4UDCWigc2cAAAAASUVORK5CYII="
  },
  {
    "title": "Tesla’s India Letdown Spurs Discounts on Unsold Model Y SUVs",
    "source": "Bloomberg.com",
    "date": "21 hours ago",
    "snippet": null,
    "link": "https://www.bloomberg.com/news/articles/2026-01-14/tesla-s-india-letdown-spurs-discounts-on-unsold-model-y-suvs",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB00lEQVQ4jXWTv4viUBDHP8aAwUbBJoWgrYjVdgtCuNrirhfkSq1s7PWfUJurrveusYjFso2ohZ3IbiNaKJbPQvwRzVyxeRJv3YEhMG/m+z4zmQf3ZgBPQBt4A06AB7wDHeA5yHloyaDwAMgXfgK6QEIXRYJvAvgLOLZtk81m75SVUiwWC87nsw69Aj8ApbG7+pZqtSqXy+XmnufJ8XiUyWQi+Xw+TNPW7TwHaAJIrVYTEZF+vy+1Wk3q9bq4riu+78tgMJBoNKoFDsG86IT71ALNZvMWS6VSopSS5XIplmXdURjAt0cTNU0Ty7KIx+M4jkM8Hmc0GoXngK71HhHsdjtZrVay3W7F8zxxXVds2/70VwzAf0SwXC4Zj8cMh0Pm8znFYpFWq4VpmuE0Az4W5hNBo9G4xWKxmPR6PfE8TxzHCRO8G8DLI4KwnU4n1us1pmmSTqfDRy8m8Av4CVjhk1wuR6lUwjAM8vk85XKZ/X7PdDrVKWfgt+6jHW7B933xfV+u16tcr1e5XC6y2WykUqlIJBLR+F3A0KucBP4ATiaToVAo3LWglGI2m6GU0qFX4DuwC+clAtXbVj7wQ0Cb/GpeBh+r3eHjCXuB4FtQ+MR/z/kfQmkSTZadhgoAAAAASUVORK5CYII="
  },
  {
    "title": "Tesla makes two big interior changes to several Model Y vehicles",
    "source": "Teslarati",
    "date": "1 day ago",
    "snippet": null,
    "link": "https://www.teslarati.com/tesla-makes-big-interior-change-several-model-y-vehicles/",
    "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgBBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3NzcrNzc3Nzc3Nzc3N//AABEIABAAEAMBEQACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAAEBwH/xAAiEAACAQMCBwAAAAAAAAAAAAABAgMABBEGEgUTFyEyQYH/xAAYAQACAwAAAAAAAAAAAAAAAAABAwACBv/EAB0RAAICAQUAAAAAAAAAAAAAAAABAgMEERITQVH/2gAMAwEAAhEDEQA/AKTCkmsH2RKWas/CMrHpFFRM9o+hbYyzMudwCqDmn2USrr3SCFsbuHRscom3sJMAqnY4Gff2kY98K09/fgEzL/iHUUqqJy4k8VoZGVytJLRIjZ//2Q=="
  },
  {
    "title": "Tesla offering discounts to clear out excess inventory of Indian Model Y SUVs (TSLA:NASDAQ)",
    "source": "Seeking Alpha",
    "date": "19 hours ago",
    "snippet": null,
    "link": "https://seekingalpha.com/news/4539163-tesla-offering-discounts-to-clear-out-excess-inventory-of-indian-model-y-suvs",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB8UlEQVQ4jZWSP2hTURTGf/fePBWaxFIt5aW2YIlFqlC1SIei4iAI4iIuLqJ1M1PRzbnoYgdBR9csncRJHIyu/ntIa1V0MGpSU2ObPDHt+3Md7st7JAHFA4fzne/c853LuVfoGyMWdvkCgmsEYgyl0/zNAuGi9Cc0t6mMFIW+w0UQdxH/aOw2LVzQhRShmEOTBvFf/UAaIeZSSPIEEeUpyI7C6GkYOgitDXi7CHUHrADs87D+AhqfTS7JS1oqjaeS5lP3TPPSA9gow8l5GJiEzBE4eiWZ7yloqXQKz0rImXkTH98Cvwblksmnr5tYfQU/KkDSI+PpQxMwfAzeP4ffdWL+zUPI7ofxs/CxlPCRp/C3RysZg75+WPtCzAE0f0GjZnBlubMGpPCj63i7Eta36LFGDX5udVw/EogU176buHtPzxSyg0agmwckmxI2JVS/QfUDTJwBZRPzueOQGTQiyobhKeNRXeir4zqWy0/DpZvwdRmeLkJWwqFzsOJA307IDphzziNYegKA0LOHm1hbyTe298GBGbD3QqMOK8/g3Uvoz8CJWXOmdB/Wm+Btc4W+PPUaFUzGAmH0LaXqxO1aGwMEypEgFgiFi2+Z7Yc7jHfjdh5j4YJYkORWi2hVQIQO0nd736977b6LCB20KpBbLf4Bwla1Zn2uvIQAAAAASUVORK5CYII="
  },
  {
    "title": "Tesla launches a seven-seat version of the 2026 Model Y",
    "source": "Engadget",
    "date": "1 day ago",
    "snippet": null,
    "link": "https://www.engadget.com/transportation/evs/tesla-launches-a-seven-seat-version-of-the-2026-model-y-130039385.html",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAGFBMVEUAAAD///8AAAAdHR2AgIA/Pz/u7u6KiopMe+7WAAAAAXRSTlP+GuMHfQAAADtJREFUGJVjYGBCBQxkCjBCABtCgJUZCFgZEQLMICYzkgBEOyO6GUgC7CwgwIxkKBPQUAxr2ShyOjIAAATxAe5S4Oc4AAAAAElFTkSuQmCC"
  },
  {
    "title": "Tesla taps Samsung for 5G modems amid plans of Robotaxi ramp: report",
    "source": "Teslarati",
    "date": "2 hours ago",
    "snippet": null,
    "link": "https://www.teslarati.com/tesla-taps-samsung-for-5g-modems-amid-plans-of-robotaxi-ramp-report/",
    "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgBBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3NzcrNzc3Nzc3Nzc3N//AABEIABAAEAMBEQACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAAEBwH/xAAiEAACAQMCBwAAAAAAAAAAAAABAgMABBEGEgUTFyEyQYH/xAAYAQACAwAAAAAAAAAAAAAAAAABAwACBv/EAB0RAAICAQUAAAAAAAAAAAAAAAABAgMEERITQVH/2gAMAwEAAhEDEQA/AKTCkmsH2RKWas/CMrHpFFRM9o+hbYyzMudwCqDmn2USrr3SCFsbuHRscom3sJMAqnY4Gff2kY98K09/fgEzL/iHUUqqJy4k8VoZGVytJLRIjZ//2Q=="
  },
  {
    "title": "Tesla Stock Rises on Delivery Growth and AI Investments",
    "source": "Yahoo Finance",
    "date": "1 day ago",
    "snippet": null,
    "link": "https://finance.yahoo.com/news/tesla-stock-rises-delivery-growth-174307879.html",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAJ1BMVEX///8De2ZirZ/f7+zA3tkji3mBvbITg3ChzcZCnIyw1s/Q5uNxtanGthbwAAAATElEQVQYlX2OSQ7AMAgDMWHJ0v+/t/RmIaW+eTQyiNwyASiDVcCoj+rOghaYTcD4m/QmWPXFwlbVzcCCfZEA8jD4bgaDbF/J8XzklhdtCwDo22XHCQAAAABJRU5ErkJggg=="
  },
  {
    "title": "Where Will Tesla Stock Be in 1 Year?​",
    "source": "The Motley Fool",
    "date": "3 hours ago",
    "snippet": null,
    "link": "https://www.fool.com/investing/2026/01/15/where-will-tesla-stock-be-in-1-year/",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABjElEQVQ4jdXQv0uVcRTH8df3eR7utaIflhElebsQ0lAiETUI7RWujYVokkNDNbQHQkQRURAkQVhTBEFLa0tDDbXcpTK4gjcJasjyanaf59ugksj9B/xM53DO+3M+HDa8wmoxW7m63MeQCnLEvdO3wKPuBxACabQ8G26MLRt8rV6RtFLoxgUcxSc8nlnaWZtPoi+h8wjOoxfvMYFGkQTZCrwHD3F6TbrBntKPkZf5wZCIEyswDOIYhpMifktCkcDoOhh6F2X3O7TurYFXdQajIZLFpKhgAHewFWexLSAX+lJR/P+sOTzDLwzEoCeLRTgQQrxrofQqbvmThhjquI5k3dUCN2Nwo9Us51nH0qlYhGrWeem1oll6q5WYe3IixyTOtYk9hckQ5ScvvpBmrXflzYuHs3J/Y5x4DW9+Pj0OsyGGWhuDWgzmUar0f1zatP33IYxnoiFCA4Qo5GlLiLdRR2UFnsZzNFF8r++zv+/zBwwFbdSoXrYraar/7Upr+W5TduRdYcHIzFi79Y2uf3u8hJX5NVwzAAAAAElFTkSuQmCC"
  },
  {
    "title": "How Tesla Stock Could Become a ‘DREAM’ Come True",
    "source": "Barron's",
    "date": "2 days ago",
    "snippet": null,
    "link": "https://www.barrons.com/articles/tesla-stock-price-musk-ai-c7ba43a1?gaa_at=eafs&gaa_n=AWEtsqdPg4eD1DAzgpgRTNJpp-Q1rwodTXPJuhSTD5h4VgNBmCbwV928CE3P&gaa_ts=6968e56c&gaa_sig=Jcl6BqLYw37Es6DTtDHNx__KJF4sv95-Sf8V_pIq2GAaVhaTmG5QeY5UuRSjwiCp1k93xEqm5j0LBJUsKjOGhg%3D%3D",
    "thumbnail": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwEBBgEIBwgKCgkBDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNDg8PGjclHxkrKys3NysrNys3KzcrNysrNzcrKysrKzcrKys3KzcrKys3Nys3KzcrKzcrNys3KzcrN//AABEIABAAEAMBIgACEQEDEQH/xAAWAAADAAAAAAAAAAAAAAAAAAADBAb/xAAnEAABAgQEBgMAAAAAAAAAAAABAgMEBxETAAUGCBIhIjFBoRdRgf/EABUBAQEAAAAAAAAAAAAAAAAAAAMC/8QAFREBAQAAAAAAAAAAAAAAAAAAAEH/2gAMAwEAAhEDEQA/AI3ImNLTLRuauQ19ctoRTzSeIjqCkjwe1CcL5+xpSWTsorbK4dzXsOlx1hZJtqJPYnwQAf3A8pjZZy/Z3OoiluJ+YYUsoKEcVCVJNTzHLpwDM8x05qzLdt0AwVuJkBcN1aaElZBoB9Cns4sMf//Z"
  },
  {
    "title": "Tesla: The EV Dream Is Over (NASDAQ:TSLA)",
    "source": "Seeking Alpha",
    "date": "22 hours ago",
    "snippet": null,
    "link": "https://seekingalpha.com/article/4859669-tesla-the-ev-dream-is-over",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB8UlEQVQ4jZWSP2hTURTGf/fePBWaxFIt5aW2YIlFqlC1SIei4iAI4iIuLqJ1M1PRzbnoYgdBR9csncRJHIyu/ntIa1V0MGpSU2ObPDHt+3Md7st7JAHFA4fzne/c853LuVfoGyMWdvkCgmsEYgyl0/zNAuGi9Cc0t6mMFIW+w0UQdxH/aOw2LVzQhRShmEOTBvFf/UAaIeZSSPIEEeUpyI7C6GkYOgitDXi7CHUHrADs87D+AhqfTS7JS1oqjaeS5lP3TPPSA9gow8l5GJiEzBE4eiWZ7yloqXQKz0rImXkTH98Cvwblksmnr5tYfQU/KkDSI+PpQxMwfAzeP4ffdWL+zUPI7ofxs/CxlPCRp/C3RysZg75+WPtCzAE0f0GjZnBlubMGpPCj63i7Eta36LFGDX5udVw/EogU176buHtPzxSyg0agmwckmxI2JVS/QfUDTJwBZRPzueOQGTQiyobhKeNRXeir4zqWy0/DpZvwdRmeLkJWwqFzsOJA307IDphzziNYegKA0LOHm1hbyTe298GBGbD3QqMOK8/g3Uvoz8CJWXOmdB/Wm+Btc4W+PPUaFUzGAmH0LaXqxO1aGwMEypEgFgiFi2+Z7Yc7jHfjdh5j4YJYkORWi2hVQIQO0nd736977b6LCB20KpBbLf4Bwla1Zn2uvIQAAAAASUVORK5CYII="
  },
  {
    "title": "Automakers like Ford and GM are jumping into a whole new business where Tesla is a serious player",
    "source": "CNBC",
    "date": "2 hours ago",
    "snippet": null,
    "link": "https://www.cnbc.com/2026/01/15/ford-gm-tesla-energy-storage.html",
    "thumbnail": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAllBMVEUAHloADFQAHFkAGFcAGVMAAE4PJl83RnsjO2gAAFIAAFUAGVYAEVkGHV0GIFUGHlUAF1wkMmC2ucqipLeMmK/T19X8/Pp8iJ+yvsxSW4NZX3q8x813gJYACkwAAETW3eZOVG1YZITL1dmxvMK9vsTg4+lGTGdiZonM1N+Gh5bc5OUAGGObpbqGj7Job5CuqcC+uc/BxtMZTvwUAAAAdElEQVQYlWNgoBZgYmZG4rEwsrKxc3BycfNw8vDyMfALCAoJi4iKiUtISknLyPIzMMjJKyiKKikrCauoCioKMDDws8qrKcqrayhpamnxKnIDjdDmkNDRldPTN9CTMpQBms3EwMTIysjLzCjLCDKUjWouRwYA81AHiFv0f4YAAAAASUVORK5CYII="
  }
]
```

## 🚀 Quick Start (2 Minutes)

### 1. Get Token
Get your **free** scraping token from the [Thordata Dashboard](https://www.thordata.com/?utm_source=github&utm_medium=readme&utm_campaign=gnews_scraper).

### 2. Install
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

### 4. Run Scraper

**Search for a topic:**
```bash
# Default JSON output
python main.py "Elon Musk"

# CSV output, limit 50, region UK
python main.py "Crypto Market" --limit 50 --country uk --format csv
```

Data will be saved to the `output/` directory.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with ❤️ by the Thordata Developer Team.</sub>
</div>