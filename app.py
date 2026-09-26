import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

## LangSmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##Prompt template
prompt = ChatPromptTemplate.from_messages(
  [
    ("system","You are a helpful Assistant. Please respond to the questions asked"),
    ("user","Question:{question}")
  ]
)

##Streamlit Framework
st.title("Langchain Demo with LLM model")
input_text = st.text_input("What Question you have in mind?")

##Ollama gemma:2b model
llm = OllamaLLM(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))