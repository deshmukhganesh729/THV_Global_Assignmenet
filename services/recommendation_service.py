import pandas as pd

def load_fbt_data(path="data/dummy_purchases.csv"):
    return pd.read_csv(path)

def recommend_fbt(product_id, fbt_df, top_k=3):
    subset = fbt_df[fbt_df["product_id"] == product_id]
    if subset.empty:
        return []
    return subset["bought_together"].value_counts().head(top_k).index.tolist()
