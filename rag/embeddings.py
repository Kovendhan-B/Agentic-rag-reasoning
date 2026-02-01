# rag/embeddings.py
from sentence_transformers import SentenceTransformer

# Load once at import time
_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    """
    Convert list of texts into embedding vectors
    """
    embeddings = _model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embeddings
