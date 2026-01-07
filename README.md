## 📑 Proof of Work

A full proof document (architecture, tools, skills, and evidence):

➡️ [RAG Project – Proof Document (PDF)](docs/RAG_Project_Proof_Document.pdf)




# 📄 AI Document Question-Answering Assistant (RAG)

GitHub: https://github.com/vamsireddy99126/ai-document-qa-rag

A Retrieval-Augmented Generation (RAG) web app where users upload documents (PDF/TXT/DOCX) and ask questions. The app retrieves relevant chunks via vector search and responds using only document context (hallucination reduction).

---

## ✅ Features
- Upload **PDF, TXT, DOCX**
- Document parsing + chunking
- Embeddings (supports **free local embeddings** and OpenAI-ready mode)
- Vector similarity search using **FAISS**
- Retrieval + grounded answering
- Source chunks shown in UI
- Streamlit web UI (chat-style)

---

## 🧠 What this proves (GenAI concepts)
- Retrieval-Augmented Generation (RAG)
- Text embeddings + semantic search
- Vector DB similarity search (FAISS)
- Prompt grounding / hallucination reduction
- Modular Python engineering for AI apps

---

## 🛠️ Tools & Software Used

### Programming / Dev
- **Python 3.11**
- **Git & GitHub**
- **VS Code / Terminal**
- **python-dotenv** for environment management

### GenAI / RAG
- **LangChain (modular)**: loaders / splitters / vector store adapters
- **FAISS**: vector database for similarity search
- **SentenceTransformers** (free local embeddings): `all-MiniLM-L6-v2`
- (Optional) OpenAI-ready mode: OpenAI embeddings + chat model when quota/billing is available

### Document Processing
- **pypdf**: PDF text extraction
- **docx2txt**: DOCX extraction

### UI
- **Streamlit**: upload, index build, chat UI, sources view

---

## 🧩 Project Structure

```
.
├── app.py
├── requirements.txt
├── src/
│   ├── loader.py         # PDF/TXT/DOCX loading
│   ├── splitter.py       # chunking
│   ├── embeddings.py     # embeddings provider (local/openai)
│   ├── vector_store.py   # FAISS build
│   ├── retriever.py      # retriever wrapper
│   ├── retrieve.py       # compatibility helper (invoke vs legacy)
│   └── qa_chain.py       # grounded answering + sources
└── .gitignore
```

---

## ▶️ Run Locally (copy/paste)

```bash
git clone https://github.com/vamsireddy99126/ai-document-qa-rag.git
cd ai-document-qa-rag
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## ⚙️ Configuration

Create `.env` (do NOT commit it):

### Free local mode (recommended)
```env
EMBEDDINGS_PROVIDER=local
```

### OpenAI mode (requires quota/billing)
```env
EMBEDDINGS_PROVIDER=openai
OPENAI_API_KEY=YOUR_KEY
```

---

## 🧪 Demo Test Questions
- "Summarize the document in 5 bullet points."
- "What are the key skills mentioned?"
- "List projects and tools used."
- "What is the candidate's experience?"

---

## 📌 Skills Demonstrated (for CV/LinkedIn)
- RAG (Retrieval-Augmented Generation)
- Vector databases (FAISS)
- Semantic search + embeddings
- Document ingestion and preprocessing
- Streamlit deployment
- Debugging and dependency management
- GitHub portfolio packaging

---

## License
MIT
