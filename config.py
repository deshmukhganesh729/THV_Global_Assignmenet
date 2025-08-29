import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # set in environment
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
CHROMA_DB_DIR = "chroma_index"
