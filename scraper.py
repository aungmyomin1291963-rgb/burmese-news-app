import os
import feedparser
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

RSS_FEEDS = {
    "Than Lwin Times": "https://rss.app/feeds/lCOwAQkTVNl5FV75.xml",
    "သံလွင်ခက် - Than Lwin Khet News": "https://rss.app/feeds/B09BS1AKoqer7B7X.xml",
    "Khit Thit Media": "https://rss.app/feeds/lncVLsVlJO4D60zy.xml",
    "People's Spring": "https://rss.app/feeds/YjnmcNNpbEmkl10U.xml",
    "Mizzima's News in Burmese": "https://rss.app/feeds/Np8bG9QYljXkMOuM.xml",
    "DVB TV News": "https://rss.app/feeds/NCiKje4M6LSPgFjD.xml",
    "Karen Information Center KIC": "https://rss.app/feeds/LoGQLuxeGbid815U.xml",
    "The Tainintharyi Times": "https://rss.app/feeds/p9cIetU60H0Z7IO7.xml",
    "Dawei Watch": "https://rss.app/feeds/V9fbhD9ZJS7DD2Au.xml",
    "Ayeyarwaddy Times": "https://rss.app/feeds/RashFJzAK86Zhi1Z.xml",
    "The Irrawaddy - Burmese Edition": "https://rss.app/feeds/diubzFFiNipBkKo2.xml",
    "BETV Business": "https://rss.app/feeds/CNm1kih3gMAxw79A.xml",
    "Myanmar Pressphoto Agency": "https://rss.app/feeds/Q0S74hyW0fRA5FNf.xml",
    "Myanmar Now": "https://rss.app/feeds/zJycV7bSZJfYR4La.xml",
    "BBC Burmese": "https://rss.app/feeds/E0mkJM9g5XBkJt3Z.xml",
    "The Voice of Spring": "https://rss.app/feeds/BJt18TdAghRkjz71.xml",
    "Tharyarwaddy 8 City": "https://rss.app/feeds/hKSxNSniUZJPhSJP.xml",
    "မြေလတ်အသံ - Myaelatt Athan": "https://rss.app/feeds/DYBHIqk597c4RpC4.xml",
    "ဒို့ပြည် - Doh Pyay": "https://rss.app/feeds/sDyIGrVGeoX3fzyx.xml"
}

def fetch_news():
    for source, url in RSS_FEEDS.items():
        print(f"Checking {source}...")
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                # Safely grab data even if the news site formatted it badly
                data = {
                    "title": getattr(entry, 'title', 'No Title'),
                    "link": getattr(entry, 'link', ''),
                    "published_date": getattr(entry, 'published', None),
                    "content": getattr(entry, 'summary', ''),
                    "source": source
                }
                
                try:
                    supabase.table("news_articles").insert(data).execute()
                    print(f"  -> Added: {data['title']}")
                except Exception as e:
                    print(f"  -> Database Error: {e}") 
        except Exception as e:
            print(f"  -> FAILED to read {source}. Skipping...")
            continue 

if __name__ == "__main__":
    fetch_news()
