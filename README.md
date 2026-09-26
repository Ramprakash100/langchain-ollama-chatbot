# 🤖 LangChain Gemma 2B Streamlit Chatbot

A simple AI chatbot built using **LangChain**, **Gemma 2B**, **Ollama**, and **Streamlit**. This project demonstrates how to build a lightweight chatbot using a locally running open-source Large Language Model (LLM).

The application uses **LangChain Expression Language (LCEL)** to connect a prompt template, Ollama's Gemma 2B model, and an output parser into a simple processing chain. **LangSmith** is also configured for tracing and monitoring the LangChain workflow.

---

## ✨ Features

- 💬 Interactive chatbot interface using Streamlit
- 🦜🔗 LangChain prompt templates
- 🔗 LangChain Expression Language (LCEL) chain
- 🤖 Gemma 2B running locally through Ollama
- 📊 LangSmith integration for tracing and monitoring
- 🔐 Environment variable support using `python-dotenv`
- ⚡ Lightweight and easy-to-understand implementation
- 🖥️ Local LLM inference without requiring a paid LLM API

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Programming language |
| 🦜🔗 LangChain | LLM application framework |
| 🤖 Gemma 2B | Large language model |
| 🦙 Ollama | Local LLM runtime |
| 🎈 Streamlit | Web application interface |
| 📊 LangSmith | LangChain tracing and monitoring |
| 🔐 python-dotenv | Environment variable management |

---

## 🏗️ Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Streamlit    │
                    │       UI        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ ChatPromptTemplate│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Gemma 2B     │
                    │     Ollama      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ StrOutputParser │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    Response     │
                    └─────────────────┘
