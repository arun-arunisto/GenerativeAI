from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage

llm = ChatOllama(
    model = "llama3",
    temperature = 0.8,
    num_predict = 256,
    # other params ...
)

messages = [
    ("human", "What is the capital of France?"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)