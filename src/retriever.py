def get_retriever(vector_store, k: int = 4):
    """
    Create a retriever from a vector store.
    """
    return vector_store.as_retriever(search_kwargs={"k": k})
