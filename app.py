import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import pandas as pd
from services.embedding_service import index_products
from services.search_service import hybrid_search
from services.recommendation_service import load_fbt_data, recommend_fbt
from services.llm_service import extract_scenario
from utils.data_loader import load_products

st.set_page_config(page_title="TVH Findability Demo", layout="wide")
st.title("TVH Findability Demo")

products_df = load_products("data/products.csv")
fbt_df = load_fbt_data("data/dummy_purchases.csv")

if st.sidebar.button("Reindex Products"):
    index_products(products_df)
    st.sidebar.success("Products reindexed successfully!")

query = st.text_input("What product are you looking for?", "")

if query:
    scenario = extract_scenario(query)
    st.write(f"**Extracted scenario:{scenario}")

    results = hybrid_search(query, products_df)
    st.subheader("🔍 Top Matches")
    for pid, desc, score in results:
        st.markdown(f"- **{pid}** | {desc} _(score {score})_")
        recs = recommend_fbt(pid, fbt_df)
        if recs:
            st.markdown(f"Frequently Bought Together: {', '.join(map(str, recs))}")
