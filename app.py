import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import time

load_dotenv()

# Hugging Face API Model
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=300
)

model = ChatHuggingFace(llm=llm)

# ------------------- UI -------------------

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Streaming AI Chatbot")
st.write("Powered by Mistral-7B (Hugging Face API)")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

# Display chat history (skip system)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(HumanMessage(content=prompt))

    # Streaming response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("Thinking..."):
            result = model.invoke(st.session_state.messages)

        # Simulate word-by-word streaming
        for word in result.content.split():
            full_response += word + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.03)

        message_placeholder.markdown(full_response)

    st.session_state.messages.append(AIMessage(content=full_response))
