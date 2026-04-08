import os
import feedparser
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

RSS_FEEDS = {
   "The Irrawaddy (Burmese)": "https://burma.irrawaddy.com/feed"
}

def fetch_news():
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries:
            data = {
                "title": entry.title,
                "link": entry.link,
                "published_date": entry.published,
                "content": entry.summary,
                "source": source
            }
            
            try:
                supabase.table("news_articles").insert(data).execute()
                print(f"Added: {entry.title}")
            except Exception as e:
                pass 

if __name__ == "__main__":
    fetch_news()
