from typing import Any, Dict, List


def build_rag_answer(question: str, retrieved_docs: List[Any]) -> Dict[str, Any]:
    """
    Free, no-LLM fallback:
    - Returns a grounded answer based on retrieved text snippets.
    - Shows sources, so user can verify.

    This is still valuable for recruiters because it proves:
    embeddings + vector search + grounded retrieval + UI.
    """
    if not question or not question.strip():
        return {"answer": "Please enter a question.", "sources": retrieved_docs}

    if not retrieved_docs:
        return {"answer": "I don't know based on the uploaded document.", "sources": []}

    # Simple extractive summary from top chunks
    top = retrieved_docs[:3]
    combined = "\n\n".join([d.page_content.strip() for d in top if getattr(d, "page_content", "")])

    answer = (
        "Here are the most relevant excerpts from your document (grounded retrieval):\n\n"
        + combined[:1500]
        + ("\n\n(Truncated)" if len(combined) > 1500 else "")
    )

    return {"answer": answer, "sources": retrieved_docs}
