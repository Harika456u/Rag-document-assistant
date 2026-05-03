# app.py

import streamlit as st
from rag import build_rag
from mcq import generate_mcq

st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📄 RAG Document Assistant")

# -------------------------------
# Session State Init
# -------------------------------
if "db" not in st.session_state:
    st.session_state.db = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "qa" not in st.session_state:
    st.session_state.qa = None
if "file_name" not in st.session_state:
    st.session_state.file_name = None

# -------------------------------
# Upload PDF (FIXED)
# -------------------------------
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:

    # Only rebuild if new file uploaded
    if st.session_state.file_name != uploaded_file.name:

        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        with st.spinner("Processing PDF..."):
            db, retriever, qa = build_rag("temp.pdf")

            st.session_state.db = db
            st.session_state.retriever = retriever
            st.session_state.qa = qa
            st.session_state.file_name = uploaded_file.name

        st.success("✅ PDF processed successfully!")

# -------------------------------
# Mode Selection
# -------------------------------
mode = st.selectbox(
    "Choose Mode",
    ["Ask Questions", "Generate MCQs (Page Range)"]
)

# -------------------------------
# ASK QUESTIONS
# -------------------------------
if mode == "Ask Questions":

    query = st.text_input("Ask your question")

    if st.button("Submit"):

        if st.session_state.qa is None:
            st.warning("⚠️ Upload PDF first")

        else:
            answer = st.session_state.qa(query)
            st.subheader("💬 Answer")
            st.write(answer)

# -------------------------------
# MCQ GENERATION (FIXED PROPERLY)
# -------------------------------
elif mode == "Generate MCQs (Page Range)":

    start_page = st.number_input("Start Page", min_value=1, value=1)
    end_page = st.number_input("End Page", min_value=1, value=5)

    topic = st.text_input("Enter topic (optional)")

    if st.button("Generate MCQs"):

        if st.session_state.db is None:
            st.warning("⚠️ Upload PDF first")

        else:
            # 🔥 Get ALL chunks
            all_docs = st.session_state.db.docstore._dict.values()

            # 🔥 Filter by page
            filtered_docs = [
                d for d in all_docs
                if start_page <= d.metadata.get("page", 0) + 1 <= end_page
            ]

            if not filtered_docs:
                st.warning("No content found in this page range")

            else:
                # Limit size to avoid overload
                limited_docs = filtered_docs[:10]

                context = "\n\n".join([d.page_content for d in limited_docs])

                if topic:
                    context = f"Focus on topic: {topic}\n\n{context}"

                mcqs = generate_mcq(context)

                st.subheader("📝 Generated MCQs")
                st.write(mcqs)