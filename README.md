# 📄 RAG Document Assistant

An AI-powered application that allows users to **interact with PDF documents**, ask questions, and **generate MCQs from specific page ranges** using Retrieval-Augmented Generation (RAG).
---
## 🚀 Features

* 📄 Upload PDF documents (books, notes, guides)
* 💬 Ask questions from the document (RAG-based)
* 📝 Generate MCQs from **selected page ranges**
* 🎯 Optional topic-based MCQ generation
* ⚡ Fully local AI (no API key required)
* 🧠 Uses vector database for accurate retrieval
---
## 🛠 Tech Stack

* Python
* Streamlit (UI)
* LangChain (RAG pipeline)
* FAISS (Vector Database)
* Ollama (Local LLM & embeddings)
---
## 🧩 How It Works

1. PDF is uploaded
2. Text is split into chunks
3. Chunks are converted into embeddings
4. Stored in FAISS vector database
5. User query → relevant chunks retrieved
6. LLM generates answer or MCQs

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/rag-document-assistant.git
cd rag-document-assistant
```
---
### 2. Install dependencies

```bash
pip install -r requirements.txt
```
---
### 3. Install Ollama
Download and install: https://ollama.com/
---
### 4. Pull required models

```bash
ollama pull phi3
ollama pull nomic-embed-text
```
---
## ▶️ Run the Application
```bash
streamlit run app.py
```
------

## 📌 Usage
### 💬 Ask Questions
* Upload a PDF
* Enter a question
* Get answers directly from the document
### 📝 Generate MCQs
* Select page range (e.g., 1–5)
* Enter topic (optional)
* Click **Generate MCQs**
---
## ⚠️ Notes
* Large PDFs are processed using chunking for efficiency
* There is no strict file size limit, but performance depends on system memory
* Uses local models → no internet/API cost
---
## 💡 Use Cases
* 📚 Study assistant for textbooks
* 📝 Exam preparation (MCQ generation)
* 📄 Document analysis
* 🎓 Academic projects
---
## 🔮 Future Improvements
* Export MCQs as PDF
* Highlight source text
* Chat-style UI
* Chapter-wise MCQ generation
---
## 👩‍💻 Author
Harika Yanamandram
---
## 📜 License
This project is for educational purposes.
