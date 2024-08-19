import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate   
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import requests

# Load environment variables
load_dotenv()

# Set up the model and chain
llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-pro',
    temperature=0,
    max_tokens=None,
    Timeout=None,
    max_retries=2
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a chatbot trained on the following data:\n{data}'),
        ('human', 'Question: {question}')
    ]
)

# Function to fetch data from a URL
def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        st.error(f"Failed to fetch data from the URL: {url}")
        return None

# Set up Streamlit app
st.title('Hello Friends')

# Get the URL from the user
url = "https://ofkace.github.io/Info/main.html"

# Fetch and display the data
if url:
    data = fetch_data_from_url(url)
    # if data:
    #     st.text_area("Data Loaded from URL", data, height=200)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt_text := st.chat_input("Ask your question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt_text)
        
    # Process the user input through the LangChain
    if data:
        output_parse = StrOutputParser()
        chain = prompt_template | llm | output_parse
        response = chain.invoke({'question': prompt_text, 'data': data})
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.warning("Please enter a valid URL and load the data before asking a question.")
