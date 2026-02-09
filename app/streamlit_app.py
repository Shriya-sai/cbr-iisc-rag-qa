import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.rag.rag_pipeline import ask_question

st.set_page_config(page_title="CBR Annual Report QA", page_icon="🧠")

st.title("🧠 CBR IISc Annual Report Assistant")
st.write("Ask questions about the last 3 years of CBR Annual Reports.")

st.markdown("### Try a sample question 👇")

sample_questions = [
    "What is the GenomeIndia project?",
    "What is the YLOPD study?",
    "What research does CBR conduct on aging?",
]

cols = st.columns(len(sample_questions))

for i, q in enumerate(sample_questions):
    if cols[i].button(q):
        st.session_state.sample_question = q


# Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
# If user clicked a suggestion button, use it
default_question = st.session_state.get("sample_question", "")

question = st.chat_input(
    "Ask a question about CBR reports...",
    key="chat_input"
)

if default_question and not question:
    question = default_question
    st.session_state.sample_question = ""

if question:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = ask_question(question)

            st.markdown(answer)

            st.markdown("**Sources:**")

            for year, page, link in sources:
                if link:
                    st.markdown(
                        f"- [CBR Annual Report {year} — Page {page}]({link})"
                    )
                else:
                    st.markdown(f"- CBR Annual Report {year} — Page {page}")

    st.session_state.messages.append({"role": "assistant", "content": answer})
