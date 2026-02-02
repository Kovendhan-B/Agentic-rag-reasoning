import lancedb
from rag.embeddings import embed

db = lancedb.connect("db/lancedb")

def retrieve(query: str, k: int = 3):
    table = db.open_table("docs")
    query_vector = embed([query])[0]

    return (
        table.search(query_vector)
        .limit(k)
        .to_list()
    )
