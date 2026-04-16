import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from tqdm import tqdm
import time
import requests
from langdetect import detect, DetectorFactory
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

DetectorFactory.seed = 0
load_dotenv()

KEYWORDS = (
    # Core + Scientific
    'beaver OR beavers OR "Castor canadensis" OR "Castor fiber" OR '
    # Europe (full coverage)
    'Biber OR bóbr OR bobr OR bober OR babior OR бобр OR бобёр OR бобер OR бабёр OR бобър OR bobor OR bober OR castor OR bever OR bäver OR majava OR hód OR kunduz OR '
    # Slavic full
    'dabar OR bobr OR bobor OR Skokani OR Hopni OR '
    # Romance / Iberian / Latin America
    'castor OR "Operación castor" OR '
    # Asia
    '海狸 OR 海狸坝 OR ビーバー OR "私 が ビーバー になった 時" OR 비버 OR ऊदबिलाव OR biwara OR '
    # Middle East / Africa / Others
    'قندس OR سمور OR kunduz OR chimbalangondo OR '
    # Nordic / Baltic
    'bäver OR bever OR Operation Bäver OR Operation Bever OR Hopparar OR '
    # Indigenous/regional variants where documented
    'tlęzáá OR ch\'one\' OR maumshet OR '
    # Hoppers movie global/local titles (exact search terms)
    '"Hoppers Pixar" OR "Pixar Hoppers" OR "Hopper beaver" OR "When I Became a Beaver" OR "Hoppers: Operación castor" OR "Jumpers" OR "Sauteurs" OR "Hopperi" OR "Skokani" OR "Hoppananlar" OR "Operation: Bäver" OR "Mission: Bæver" OR "Agyugró" OR "Cara de Um, Focinho de Outro" OR "Saltitões" OR "Hopperi" OR "Prыgunы" OR "Šokliai"'
)

PRE_START = "2025-01-01"
PRE_END = "2026-02-22"
POST_START = "2026-03-01"
POST_END = "2026-04-30"  # extend as needed

# ... (full collection functions from previous messages — surface_web, reddit, twitter, news + multilingual NLP, BERTopic, stakeholder, geocoding)

if __name__ == "__main__":
    print("🌍 Running GLOBAL pipeline for Eco-Cinema Portal...")
    # [Run the 4 collection functions, NLP, BERTopic, stakeholder classification, geocoding]
    df.to_csv("beaver_hoppers_sentiment_corpus_2026_full.csv", index=False)
    print("✅ Global dataset updated!")
