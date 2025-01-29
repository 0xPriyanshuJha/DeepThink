import streamlit as st
from ollama import chat

@st.cache_resource
def get_chat_model():
    return lambda messages: chat(
        model = "deepseek-r1",
        messages = messages,
        stream = True
    )

def handle_user_input():
    if user_input := st.chat_input("Type your message here..."):
        st.session_state['messages'].append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)
        
        with st.chat_message("assistant"):
            chat_model = get_chat_model()
            stream = chat_model(st.session_state["message"])
            
            thinking_content = process_thinking_phase(stream)
            response_content = process_response_phase(stream)

            st.session_state["messages"].append({"role": "assistant", "content": thinking_content + response_content})

def process_thinking_phase(stream):
    thinking_content = ""
    with st.status("Thinking...", expanded=True) as status:
        thinking_placeholder = st.empty()

        for chunk in stream:
            content = chunk[]