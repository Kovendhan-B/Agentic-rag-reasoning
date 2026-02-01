import lancedb
from rag.embeddings import embed

db = lancedb.connect("db/lancedb")

def ingest_text_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    
    chunks = [c for c in text.split("\n\n") if c.strip()]

    
    embeddings = embed(chunks)

    data = [
        {
            "text": chunk,
            "vector": emb,  
            "source": path
        }
        for chunk, emb in zip(chunks, embeddings)
    ]

    db.create_table("docs", data=data, mode="overwrite")

    print("Knowledge ingested!")
