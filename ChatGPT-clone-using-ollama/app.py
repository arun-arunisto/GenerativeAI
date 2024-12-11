import streamlit as st
import time
from langchain_ollama import ChatOllama

st.title("ChatGPT-clone-using-ollama")
st.write("Arun Arunisto")

llm = ChatOllama(
    model = "llama3",
    temperature = 0.8,
    num_predict = 256,
)

#initializing the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#displaying the chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#accepting user input
if prompt := st.chat_input("What Can I help with?"):
    #adding user message to chat history
    st.session_state.messages.append({"role":"User", "content":prompt})
    #displaying user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #displaying the assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        stream = llm.stream(prompt)
        full_response = ""
        for chunk in stream:
            full_response += chunk.content
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    #adding assistant response to chat history
    st.session_state.messages.append({"role":"Assistant", "content":full_response})