from agno import Agent
from config.llm import get_gemini
from agents.tools import search_knowledge_base

rag_agent = Agent(
    name = "Gemini Agentic RAG",
    model = get_gemini,
    reasoning = True,
    tools = [search_knowledge_base],
    instructions = """
    You are an agentic RAG system.

    Think step-by-step.
    Decide what information is missing.
    Retrieve iteratively.
    Cite sources.
    """
)