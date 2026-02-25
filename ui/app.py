import streamlit as st
import requests
import os


# CONFIG

st.set_page_config(
    page_title="Personal Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Personal Assistant")
st.caption("You are sorted !!")

# BACKEND URL (from Streamlit secrets)

BACKEND_URL = st.secrets["https://personalassist-1.onrender.com/"]

# SESSION STATE

if "messages" not in st.session_state:
    st.session_state.messages = []

# DISPLAY CHAT HISTORY

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# USER INPUT

user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Render backend instead of local RAG
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/chat",
                    json={"query": user_input},
                    timeout=60
                )

                if response.status_code == 200:
                    answer = response.json()["answer"]
                else:
                    answer = f"❌ Backend error: {response.status_code}"

            except Exception as e:
                answer = "⚠️ Could not connect to backend."

            st.markdown(answer)

    # Store assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )