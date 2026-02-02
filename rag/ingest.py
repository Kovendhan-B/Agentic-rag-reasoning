import lancedb
from rag.embeddings import embed

db = lancedb.connect("db/lancedb")


def _ingest_text(text: str, source: str):
    chunks = [c for c in text.split("\n\n") if c.strip()]
    embeddings = embed(chunks)

    data = [
        {
            "text": chunk,
            "vector": emb,
            "source": source
        }
        for chunk, emb in zip(chunks, embeddings)
    ]

    db.create_table("docs", data=data, mode="overwrite")


def ingest_text_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    _ingest_text(text, source=path)
    print("✅ Knowledge ingested from file")


def ingest_text_content(text: str, source: str = "ui_upload"):
    _ingest_text(text, source=source)
