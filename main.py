import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

try:
    # Streamlit page config
    st.set_page_config(
        page_title="Dhurkesh B",
        page_icon="favicon.ico",
        layout="centered",
        initial_sidebar_state="auto",
    )

    # Load environment variables
    load_dotenv()

    # Set up Groq LLM (e.g., using Mixtral)
    llm = ChatGroq(
        model_name="llama3-70b-8192",  # or 'llama3-70b-8192', 'mistral-7b-32768'
        groq_api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', 'You are a chatbot trained on the following data:\n{data}'),
            ('human', 'Question: {question}')
        ]
    )

    def fetch_data_from_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            st.error(f"File not found: {file_path}")
            return None

    st.title('Hello Friends👋')

    file_path = "info.txt"

    if file_path:
        data = fetch_data_from_file(file_path)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt_text := st.chat_input("Ask your question"):
        st.session_state.messages.append({"role": "user", "content": prompt_text})

        with st.chat_message("user"):
            st.markdown(prompt_text)

        if data:
            output_parse = StrOutputParser()
            chain = prompt_template | llm | output_parse
            response = chain.invoke({'question': prompt_text, 'data': data})

            with st.chat_message("assistant"):
                st.markdown(response)

            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.warning("Please ensure the file exists and contains valid data before asking a question.")
except:
    st.warning('Server busy...')
