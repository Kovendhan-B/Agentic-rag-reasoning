from config.llm import generate
from agents.tools import search_knowledge_base

class AgenticRAG:
    def run(self, question: str):
        # Decide
        retrieval_prompt = f"""
You are an expert researcher.

Analyze the question and produce a short search query
that would retrieve the most relevant knowledge.

Question: {question}

Respond with ONLY the search query.
"""

        search_query = generate(retrieval_prompt).strip()

        # Retrieve
        docs = search_knowledge_base(search_query)

        context = "\n\n".join(d["text"] for d in docs)

        # Synth
        answer_prompt = f"""
You must answer the question using ONLY the information below.
If the information is insufficient, say so.

Information:
{context}

Question:
{question}

Answer clearly and concisely.
"""

        answer = generate(answer_prompt)

        return {
            "question": question,
            "search_query": search_query,
            "answer": answer,
            "sources": docs
        }
