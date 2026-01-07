import os
from dotenv import load_dotenv

load_dotenv()


def get_embeddings():
    """
    Choose embeddings provider.

    Set in .env:
      EMBEDDINGS_PROVIDER=local   -> free, no OpenAI calls
      EMBEDDINGS_PROVIDER=openai  -> uses OpenAI (needs quota/billing)
    """
    provider = (os.getenv("EMBEDDINGS_PROVIDER") or "local").lower().strip()

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env but EMBEDDINGS_PROVIDER=openai")
        return OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)

    # Default: FREE local embeddings
    from langchain_community.embeddings import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
