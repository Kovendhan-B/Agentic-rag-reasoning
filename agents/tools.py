from rag.retriever import retrieve

def search_knowledge_base(query: str):
    """
    Search internal knowledge base
    
    """
    return retrieve(query)