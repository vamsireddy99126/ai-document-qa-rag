import os
import streamlit as st
from dotenv import load_dotenv

from src.loader import load_document
from src.splitter import split_documents
from src.vector_store import build_vector_store
from src.retriever import get_retriever
from src.retrieve import retrieve_docs
from src.qa_chain import build_rag_answer

load_dotenv()

st.set_page_config(page_title="AI Document Q&A (RAG)", layout="wide")
st.title("📄 AI Document Question-Answering Assistant (RAG)")
st.write(
    "Upload a document (PDF/TXT/DOCX), build the index, then ask questions grounded only in your document."
)

UPLOAD_DIR = "data/uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "doc_name" not in st.session_state:
    st.session_state.doc_name = None
if "messages" not in st.session_state:
    st.session_state.messages = []  # chat history

with st.sidebar:
    st.header("⚙️ Settings")
    k = st.slider("Top-K chunks to retrieve", 2, 10, 4)
    st.caption("Higher K may increase recall but can add noise.")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "docx"])

if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("📌 Build Index (Embeddings + FAISS)"):
        with st.spinner("Loading and chunking document..."):
            docs = load_document(file_path)
            chunks = split_documents(docs)

        with st.spinner("Building FAISS vector store..."):
            vector_store = build_vector_store(chunks)
            retriever = get_retriever(vector_store, k=k)

        st.session_state.vector_store = vector_store
        st.session_state.retriever = retriever
        st.session_state.doc_name = uploaded_file.name
        st.success("✅ Index built! Ask questions below.")

st.divider()

if st.session_state.retriever is None:
    st.info("Upload a document and click **Build Index** to start.")
else:
    st.subheader(f"Chat about: **{st.session_state.doc_name}**")

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat input (only exists inside the else block)
    question = st.chat_input("Ask a question from the uploaded document...")

    if question:
        # Add user message
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # Retrieve + answer
        with st.spinner("Retrieving relevant chunks + generating answer..."):
            retrieved_docs = retrieve_docs(st.session_state.retriever, question)
            result = build_rag_answer(question, retrieved_docs)

        answer = result["answer"]
        sources = result["sources"]

        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.write(answer)

            with st.expander("📌 Sources (retrieved chunks)"):
                for i, doc in enumerate(sources, start=1):
                    meta = getattr(doc, "metadata", {}) or {}
                    page = meta.get("page", None)
                    source = meta.get("source", None)

                    header_parts = [f"Source {i}"]
                    if page is not None:
                        header_parts.append(f"page {page}")
                    if source:
                        header_parts.append(str(source))

                    st.markdown("**" + " — ".join(header_parts) + "**")
                    snippet = (doc.page_content or "")[:700]
                    st.caption(
                        snippet + ("..." if len(doc.page_content or "") > 700 else "")
                    )
