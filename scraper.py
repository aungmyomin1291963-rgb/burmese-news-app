import feedparser
import requests
from supabase import create_client

SUPABASE_URL = "loyowilpsjueoqoejfnc"
SUPABASE_KEY= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxveW93aWxwc2p1ZW9xb2VqZm5jIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2NzM2MTksImV4cCI6MjA5MTI0OTYxOX0.sE7C1is_rSQYwv6kpX--QIEGyI2CBekHOygw4RS8ihs"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

RSS_FEEDS = {
"Than Lwin Times": "https://rss.app/feeds/lCOwAQkTVNl5FV75.xml"
"သံလွင်ခက် - Than Lwin Khet News": "https://rss.app/feeds/B09BS1AKoqer7B7X.xml"
"Khit Thit Media": "https://rss.app/feeds/lncVLsVlJO4D60zy.xml"
"People's Spring": "https://rss.app/feeds/YjnmcNNpbEmkl10U.xml"
"Mizzima's News in Burmese": "https://rss.app/feeds/Np8bG9QYljXkMOuM.xml"
"DVB TV News": "https://rss.app/feeds/NCiKje4M6LSPgFjD.xml"
"Karen Information Center KIC": "https://rss.app/feeds/LoGQLuxeGbid815U.xml"
"The Tainintharyi Times": "https://rss.app/feeds/p9cIetU60H0Z7IO7.xml"
"Dawei Watch": "https://rss.app/feeds/V9fbhD9ZJS7DD2Au.xml"
"Ayeyarwaddy Times": "https://rss.app/feeds/RashFJzAK86Zhi1Z.xml"
"The Irrawaddy - Burmese Edition": "https://rss.app/feeds/diubzFFiNipBkKo2.xml"
"BETV Business": "https://rss.app/feeds/CNm1kih3gMAxw79A.xml"
"Myanmar Pressphoto Agency": "https://rss.app/feeds/Q0S74hyW0fRA5FNf.xml"
"Myanmar Now": "https://rss.app/feeds/zJycV7bSZJfYR4La.xml"
"BBC Burmese": "https://rss.app/feeds/E0mkJM9g5XBkJt3Z.xml"
"The Voice of Spring": "https://rss.app/feeds/BJt18TdAghRkjz71.xml"
"Tharyarwaddy 8 City": "https://rss.app/feeds/hKSxNSniUZJPhSJP.xml"
"မြေလတ်အသံ - Myaelatt Athan": "https://rss.app/feeds/DYBHIqk597c4RpC4.xml"
"ဒို့ပြည် - Doh Pyay": "https://rss.app/feeds/sDyIGrVGeoX3fzyx.xml"
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

from google.myanmar_tools import ZawgyiDetector
from rabbit import Rabbit
from deep_translator import GoogleTranslator

detector = ZawgyiDetector()

def normalize_burmese(text):
    score = detector.get_zawgyi_probability(text)
    if score > 0.9:
        return Rabbit.zg2uni(text)
    return text

def analyze_sentiment(text):
    try:
        en_text = GoogleTranslator(source='my', target='en').translate(text)
        return 0.0 
    except:
        return 0.0