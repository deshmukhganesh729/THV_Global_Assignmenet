from .embedding_service import get_collection
from rapidfuzz import fuzz

def semantic_search(query, top_k=5):
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=top_k)
    return results

def hybrid_search(query, products_df, top_k=5):
    semantic_results = semantic_search(query, top_k)
    candidates = []
    for i, doc in enumerate(semantic_results["documents"][0]):
        meta = semantic_results["metadatas"][0][i]
        candidates.append((meta["product_id"], doc, 100 - i*10))
    
    for _, row in products_df.iterrows():
        score = fuzz.partial_ratio(query.lower(), row["description"].lower())
        if score > 60:
            candidates.append((row["product_id"], row["description"], score))
    
    sorted_candidates = sorted(candidates, key=lambda x: x[2], reverse=True)[:top_k]
    return sorted_candidates
