import streamlit as st
import time
from agents.agent import AgenticRAGAgent
from rag.ingest import ingest_text_content

st.set_page_config(
    page_title="Agentic RAG System",
    page_icon="🧠",
    layout="centered"
)

agent = AgenticRAGAgent()

st.markdown("## 🧠 Agentic RAG System")
st.caption("Local · Free · Explainable")
st.divider()

st.markdown("### 📥 Upload Knowledge")

uploaded_file = st.file_uploader(
    "Upload a .txt file",
    type=["txt"]
)

pasted_text = st.text_area(
    "Or paste text directly",
    height=180,
    placeholder="Paste knowledge text here..."
)

if st.button("Ingest Knowledge"):
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        ingest_text_content(content, source=uploaded_file.name)
        st.success("✅ Knowledge ingested from uploaded file")

    elif pasted_text.strip():
        ingest_text_content(pasted_text, source="pasted_text")
        st.success("✅ Knowledge ingested from pasted text")

    else:
        st.warning("Please upload a file or paste text before ingesting.")

st.divider()

question = st.text_input(
    "Ask a question",
    placeholder="What defines the Safdie Brothers filmmaking style?"
)

if question:
    with st.spinner("Agent is thinking and retrieving knowledge..."):
        time.sleep(0.4)
        result = agent.run(question)

    st.markdown("### ✅ Answer")

    if result["sources"]:
        st.write(result["answer"])
    else:
        st.info("The agent could not find sufficient retrieved knowledge to answer.")

    with st.expander("🧠 Agent Reasoning (Step-by-step)"):
        LABELS = {
            "retrieval_policy": "Retrieval policy",
            "search_query": "Generated search query",
            "retrieval_count": "Documents retrieved"
        }

        for step in result["thoughts"]:
            key = step["step"]
            value = list(step.values())[-1]
            label = LABELS.get(key, key)
            st.markdown(f"- **{label}** → `{value}`")

    if result["sources"]:
        st.markdown("### 📚 Sources")

        for i, src in enumerate(result["sources"], 1):
            st.markdown(
                f"**{i}.** `{src['source']}`",
                help=src["text"][:300]
            )
