import chromadb
from chromadb.utils import embedding_functions
from config import OPENAI_API_KEY, EMBEDDING_MODEL, CHROMA_DB_DIR

# OpenAI embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=OPENAI_API_KEY,
    model_name=EMBEDDING_MODEL
)

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

def get_collection(collection_name="products"):
    return client.get_or_create_collection(
        name=collection_name,
        embedding_function=openai_ef
    )

def index_products(products_df):
    collection = get_collection()
    for _, row in products_df.iterrows():
        collection.add(
            documents=[row["description"]],
            metadatas={"product_id": row["product_id"], "name": row["name"]},
            ids=[str(row["product_id"])]
        )
    return collection
