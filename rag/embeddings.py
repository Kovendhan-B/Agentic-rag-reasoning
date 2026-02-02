from sentence_transformers import SentenceTransformer
import logging
logging.getLogger("transformers").setLevel(logging.ERROR)

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(texts):
    return _model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
