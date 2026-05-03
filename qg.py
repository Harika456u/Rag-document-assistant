from langchain_ollama import ChatOllama 

llm = ChatOllama(temperature=0)

def generate_questions(text):
    return llm.predict(f"Generate 5 important questions:\n{text}")