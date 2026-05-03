# rag.py

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama


def build_rag(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Ensure page metadata
    for doc in documents:
        doc.metadata["page"] = doc.metadata.get("page", 0)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )
    chunks = splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = FAISS.from_documents(chunks, embeddings)

    retriever = db.as_retriever()
    llm = ChatOllama(model="phi3")

    def qa_chain(query):
        docs = retriever.invoke(query)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""
        return llm.invoke(prompt).content

    return db, retriever, qa_chain