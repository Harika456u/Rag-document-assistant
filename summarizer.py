from langchain_ollama import ChatOllama 

llm = ChatOllama(temperature=0)

def summarize(text):
    return llm.predict(f"Summarize clearly:\n{text}")