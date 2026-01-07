def retrieve_docs(retriever, query: str):
    """
    Works across LangChain versions:
    - New retrievers: retriever.invoke(query)
    - Older retrievers: retriever.get_relevant_documents(query)
    """
    if hasattr(retriever, "invoke"):
        return retriever.invoke(query)

    if hasattr(retriever, "get_relevant_documents"):
        return retriever.get_relevant_documents(query)

    raise AttributeError("Retriever has neither invoke() nor get_relevant_documents().")
