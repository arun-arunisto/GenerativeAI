import streamlit as st
import time
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# App title and header
st.title("ChatBot Clone using Gemini-2.0-Flash")
st.write("Arun Arunisto")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What can I help you with?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant reply using GPT4All
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Streaming output
        response = model.invoke(prompt)
        for chunk in response.content:
            full_response += chunk
            time.sleep(0.03)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add assistant reply to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})