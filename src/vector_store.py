from langchain_community.vectorstores import FAISS
from src.embeddings import get_embeddings


def build_vector_store(chunks):
    embeddings = get_embeddings()
    return FAISS.from_documents(chunks, embeddings)
