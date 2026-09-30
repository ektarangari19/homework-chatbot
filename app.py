import streamlit as st
from dotenv import load_dotenv
from chatbot import get_answer

load_dotenv()

st.set_page_config(
    page_title="Homework Helper AI",
    page_icon="📚"
)

st.title("📚 Homework Helper AI")
st.write("Ask any homework question!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Enter your homework question...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_answer(question)

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })