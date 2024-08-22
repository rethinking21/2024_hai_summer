import streamlit as st
import openai
from openai import OpenAI

def ask(key):
    client = OpenAI(api_key = key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages,
    )
    return response.choices[0].message.content

def main():
    st.title("Chat Window")

    # Add input field for API key
    api_key = st.text_input("API Key (hidden)", type="password")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Say something")
    if prompt:
        st.chat_message("user").markdown(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})

        res = ask(api_key)

        with st.chat_message("assistant"):
            st.markdown(res)
        
        st.session_state.messages.append({"role": "assistant", "content": res})

if __name__ == "__main__":
    main()