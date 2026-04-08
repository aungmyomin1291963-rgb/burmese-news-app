import streamlit as st
import pandas as pd
from supabase import create_client

st.set_page_config(page_title="Burmese News OSINT", layout="wide")

@st.cache_resource
def init_connection():
    return create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

supabase = init_connection()

@st.cache_data(ttl=600)
def load_data():
    response = supabase.table("news_articles").select("*").execute()
    return pd.DataFrame(response.data)

df = load_data()

st.title("📊 Burmese Open-Source News Analysis")

if not df.empty:
    st.metric("Total Articles Tracked", len(df))
    
    st.subheader("Latest Articles")
    st.dataframe(df[['published_date', 'source', 'title', 'link']].sort_values(by="published_date", ascending=False))
    
    st.subheader("Articles by Source")
    source_counts = df['source'].value_counts()
    st.bar_chart(source_counts)
else:
    st.warning("No data found. Run the scraper first!")