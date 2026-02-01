import lancedb

db = lancedb.connect("db/lancedb")

def retrieve(query, k=5):
    table = db.open_table("docs")
    return table.search(query).limit(k).to_list()
