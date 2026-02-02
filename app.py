import streamlit as st
import time
from agents.agent import AgenticRAGAgent

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Agentic RAG System",
    page_icon="🧠",
    layout="centered"
)

agent = AgenticRAGAgent()

# -----------------------------
# Header
# -----------------------------
st.markdown("## 🧠 Agentic RAG System")
st.caption("Local · Free · Explainable")
st.divider()

# -----------------------------
# Input
# -----------------------------
question = st.text_input(
    "Ask a question",
    placeholder="What defines the Safdie Brothers filmmaking style?"
)

# -----------------------------
# Run agent
# -----------------------------
if question:
    with st.spinner("Agent is thinking and retrieving knowledge..."):
        time.sleep(0.4)  # intentional UX pause
        result = agent.run(question)

    # -------------------------
    # Answer
    # -------------------------
    st.markdown("### ✅ Answer")

    if result["sources"]:
        st.write(result["answer"])
    else:
        st.info("The agent could not find sufficient retrieved knowledge to answer.")

    # -------------------------
    # Reasoning (collapsible)
    # -------------------------
    with st.expander("🧠 Agent Reasoning (Step-by-step)"):
        LABELS = {
            "need_retrieval": "Decide whether retrieval is required",
            "search_query": "Generated search query",
            "retrieval_count": "Documents retrieved"
        }

        for step in result["thoughts"]:
            key = step["step"]
            value = list(step.values())[-1]
            label = LABELS.get(key, key)

            st.markdown(f"- **{label}** → `{value}`")

    # -------------------------
    # Sources
    # -------------------------
    if result["sources"]:
        st.markdown("### 📚 Sources")

        for i, src in enumerate(result["sources"], 1):
            st.markdown(
                f"**{i}.** `{src['source']}`",
                help=src["text"][:300]
            )
