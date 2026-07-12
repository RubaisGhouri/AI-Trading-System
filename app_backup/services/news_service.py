"""
News Service
"""

import feedparser


class NewsService:

    FEEDS = [
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        "https://cointelegraph.com/rss",
        "https://decrypt.co/feed",
    ]

    @classmethod
    def get_news(cls):

        news = []

        for feed_url in cls.FEEDS:

            try:

                feed = feedparser.parse(feed_url)

                for item in feed.entries[:5]:

                    news.append(
                        {
                            "title": item.get("title", "No Title"),
                            "source": feed.feed.get("title", "Unknown"),
                            "link": item.get("link", "#"),
                        }
                    )

            except Exception:
                continue

        return news[:15]