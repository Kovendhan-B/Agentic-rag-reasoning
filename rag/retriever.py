# rag/retriever.py
import lancedb
from rag.embeddings import embed

db = lancedb.connect("db/lancedb")

def retrieve(query: str, k: int = 3):
    table = db.open_table("docs")

    # Embed query (returns numpy array)
    query_vector = embed([query])[0]

    results = (
        table.search(query_vector)
        .limit(k)
        .to_list()
    )

    return results
