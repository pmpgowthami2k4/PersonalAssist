# # Streamlit chat UI
# import streamlit as st
# import requests




# # PAGE CONFIG


# st.set_page_config(
#     page_title="Personal Assistant",
#     page_icon="💬",
#     layout="centered"
# )

# st.title("💬 Personal Assistant")
# st.caption("You are sorted !!")

# BACKEND_URL = "http://127.0.0.1:8000/chat"


# # SESSION STATE (CHAT MEMORY)


# if "messages" not in st.session_state:
#     st.session_state.messages = []


# # DISPLAY CHAT HISTORY


# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # USER INPUT


# user_input = st.chat_input("Type your message...")

# if user_input:
#     # Show user message (RIGHT)
#     st.session_state.messages.append(
#         {"role": "user", "content": user_input}
#     )

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # Call backend
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             try:
#                 response = requests.post(
#                     BACKEND_URL,
#                     json={"query": user_input},
#                     timeout=60
#                 )

#                 if response.status_code == 200:
#                     answer = response.json()["answer"]
#                 else:
#                     answer = "⚠️ Error communicating with backend."

#             except Exception as e:
#                 answer = "⚠️ Backend is not reachable."

#             st.markdown(answer)

#     # Save assistant message (LEFT)
#     st.session_state.messages.append(
#         {"role": "assistant", "content": answer}
#     )




# Streamlit chat UI (direct RAG call, no backend server)

import streamlit as st
import sys
import os

# --------------------------------------------------
# Allow Streamlit (ui/) to import backend files
# --------------------------------------------------

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from backend.rag import generate_answer

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Personal Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Personal Assistant")
st.caption("You are sorted !!")

# --------------------------------------------------
# SESSION STATE (CHAT MEMORY)
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_input = st.chat_input("Type your message...")

if user_input:
    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate answer using RAG directly
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                answer = generate_answer(user_input)
            except Exception as e:
                answer = "⚠️ Something went wrong while generating the answer."

            st.markdown(answer)

    # Store assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
