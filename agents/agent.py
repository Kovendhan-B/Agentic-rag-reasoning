from config.llm import generate
from agents.tools import search_knowledge_base

class AgenticRAGAgent:
    def run(self, question: str):
        thoughts = []

        # --------------------------------------------------
        # Step 1: Enforced retrieval policy (system rule)
        # --------------------------------------------------
        thoughts.append({
            "step": "retrieval_policy",
            "decision": "Retrieval enforced by system design to ensure grounded answers"
        })

        # --------------------------------------------------
        # Step 2: Generate search query
        # --------------------------------------------------
        search_prompt = f"""
You are an agent tasked with retrieving information from a knowledge base.

Generate a short, precise search query that would retrieve
relevant information for the question below.

Question:
{question}

Search query:
"""
        search_query = generate(search_prompt).strip()
        thoughts.append({
            "step": "search_query",
            "query": search_query
        })

        # --------------------------------------------------
        # Step 3: Retrieve documents
        # --------------------------------------------------
        docs = search_knowledge_base(search_query)
        thoughts.append({
            "step": "retrieval_count",
            "count": len(docs)
        })

        if not docs:
            return {
                "answer": "I could not find sufficient retrieved knowledge to answer.",
                "thoughts": thoughts,
                "sources": []
            }

        # --------------------------------------------------
        # Step 4: Answer using retrieved evidence only
        # --------------------------------------------------
        context = "\n\n".join(d["text"] for d in docs)

        answer_prompt = f"""
Answer the question using ONLY the information below.
Do NOT use prior knowledge.
If the information is insufficient, say so.

Information:
{context}

Question:
{question}

Answer:
"""
        answer = generate(answer_prompt)

        return {
            "answer": answer,
            "thoughts": thoughts,
            "sources": docs
        }
