
import streamlit as st
from chatbot import create_chat, ask_ai

st.title("Fresh Cuts AI Assistant")
st.caption("Ask us about our services, prices, and hours.")

if "chat" not in st.session_state:
    st.session_state.chat = create_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask a question..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_ai(st.session_state.chat, prompt)
            st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
