import lancedb
from rag.embeddings import embed

db = lancedb.connect("db/lancedb")
def ingest(docs):
    table = db.create_table(
        "docs",
        data=[{"text": d, "vector": embed(d)[0].embedding} for d in docs],
        mode="overwrite"
    )