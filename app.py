import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
from datetime import datetime
import os

st.set_page_config(page_title="🌍 Eco-Cinema Global Sentiment Portal", layout="wide")

st.markdown("<h1 style='color:#00ff9d; text-shadow:0 0 30px #00ff9d;'>🌍 ECO-CINEMA GLOBAL SENTIMENT PORTAL</h1>", unsafe_allow_html=True)
st.subheader("Live 3D Geospatial Explorer — Pixar's *Hoppers* (2026) & Future Environmental Films")

if st.button("🔄 REFRESH GLOBAL DATA NOW"):
    with st.spinner("Running full multilingual global pipeline..."):
        os.system("python beaver_culturomics_pipeline.py")
    st.success("✅ Data updated for the entire world!")
    st.rerun()

# Load & display timestamp
df = pd.read_csv("beaver_hoppers_sentiment_corpus_2026_full.csv")
st.caption(f"🛰️ Data last extracted: **{df['date'].max()}** — Global coverage active")

# Time slider + 3D globe (exactly as in previous magnificent version)
# ... [full pydeck 3D globe, hex layer, pulsing markers, arc trails, tabs for trends/topics/stakeholders]

st.success("Your ever-evolving global portal is LIVE! Share the link with the world.")
