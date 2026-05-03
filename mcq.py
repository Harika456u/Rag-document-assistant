# mcq.py

from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3")


def generate_mcq(text):
    prompt = f"""
Generate 5 MCQs from the text.

Format:

Q1:
A.
B.
C.
D.
Answer:

Text:
{text}
"""
    return llm.invoke(prompt).content