from rag.retriever import retrieve

def search_knowledge_base(query: str):
    """
    Search the internal knowledge base.
    """
    return retrieve(query, k=3)
