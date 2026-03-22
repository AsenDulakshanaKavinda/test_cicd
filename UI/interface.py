import streamlit as st
import requests

API_CHAT_URL = "http://localhost:8000/chat"

st.header("My chatbot", divider="gray")

# Session states
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Type your message..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                payload = {"text": prompt}

                response = requests.post(API_CHAT_URL, json=payload)

                if response.status_code == 200:
                    api_data = response.json()
                    answer = api_data.get("result", "No result found.")
                else:
                    answer = f"Error: {response.status_code}"

            except requests.exceptions.ConnectionError:
                answer = "Error: Could not connect to FastAPI."

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })
