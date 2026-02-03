# Agentic RAG System

A local, agentic Retrieval-Augmented Generation (RAG) system designed to produce **grounded, explainable, and hallucination-resistant answers**.

This project focuses on **AI system architecture**, not prompt engineering.

---

## Overview

This system:

- Enforces retrieval before answering  
- Generates its own search queries  
- Answers **only** from retrieved evidence  
- Refuses to answer when knowledge is missing  
- Exposes reasoning steps and sources  

The entire pipeline runs **locally**, with no paid APIs.

---

## Why Agentic RAG

Traditional RAG pipelines retrieve once and answer once.

This project introduces an **agentic control loop** where:

- Retrieval is a system-level guarantee  
- The model decides *how* to retrieve, not *whether*  
- Reasoning and tool usage are explicit and inspectable  

This design prevents confident hallucinations and enables debugging and evaluation.

---

## Architecture

User Question
->
Agent Controller
->
Search Query Generation
->
Vector Retrieval (LanceDB)
->
Evidence-Constrained Answering
->
Answer + Reasoning + Sources


---

## Knowledge Ingestion

Knowledge is ingested explicitly via the UI.

- Input: `.txt` upload or pasted text  
- Chunking: paragraph-based  
- Embeddings: local sentence-transformer  
- Storage: LanceDB (vectors + metadata)  
- Mode: overwrite (single active knowledge base)  

This ensures deterministic and reproducible behavior.

---

## Hallucination Safety

The system is designed to **fail safely**.

If relevant knowledge is not found:

- Retrieval still occurs  
- The system **refuses to answer**  
- No speculative or plausible-sounding output is produced  

This behavior has been validated using out-of-knowledge and adversarial queries.

---

## Explainability

The UI exposes:

- Retrieval policy  
- Generated search query  
- Number of retrieved documents  
- Source text used for answering  

All decisions are visible and inspectable.

---

## Tech Stack

- Python  
- Streamlit (UI)  
- Sentence-Transformers (local embeddings)  
- LanceDB (vector database)  
- Custom agent loop (Agno-style)  
- No paid APIs  

---

## Running the Project

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

