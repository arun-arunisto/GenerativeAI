import streamlit as st
import time
from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

st.title("Chatbot using GPT4All")
st.write("Arun Arunisto")

#initializing the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#displaying the chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What Can I help with?"):
    #adding user message to chat history
    st.session_state.messages.append({"role":"User", "content":prompt})
    #displaying user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #displaying the assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in model.generate(prompt, max_tokens=1024):
            full_response += chunk
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    #adding assistant response to chat history
    st.session_state.messages.append({"role":"Assistant", "content":full_response})