import streamlit as st
from agents.rag_agent import rag_agent
 
st.title("Agentic RAG")

query = st.text_input("Ask a question")

if query:
    result = rag_agent.run(query)
    st.subheader("Answer")
    st.write(result.answer)

    st.subheader("Reasoning")
    st.json(result.reasoning)