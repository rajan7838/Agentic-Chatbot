# 🤖 End-To-End Agentic AI Chatbot

An advanced, stateful AI chatbot built using **LangGraph**, **LangChain**, and **Streamlit**. This project demonstrates how to build agentic workflows where the AI can autonomously decide to use external tools (like Web Search) to answer user queries in real-time.

---

## 🚀 Features
- **Basic Chatbot:** A standard LLM-powered conversational agent.
- **Chatbot With Web:** An agentic chatbot equipped with **Tavily Web Search** that autonomously decides when to search the web for real-time information and synthesizes the answer.
- **Stateful Execution:** Uses LangGraph's `StateGraph` to maintain conversation history and seamlessly manage execution loops between the LLM and external tools.
- **Dynamic UI:** Streamlit-based sidebar for choosing LLM providers, selecting models, and entering API keys securely.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Framework:** LangChain & LangGraph
- **LLM Provider:** Groq (Llama 3, GPT-OSS models)
- **Tools:** Tavily Search API

---

## 📂 Project Structure
```text
AgentiChatbot/
├── app.py                  # Entry point of the application
├── requirements.txt        # Project dependencies
└── src/
    └── LanggraphAgenticai/
        ├── main.py         # Orchestrator / Application flow
        ├── graph/          # LangGraph state & workflow builder
        ├── LLM/            # Groq model initialization
        ├── nodes/          # Chatbot & Tool nodes execution
        ├── state/          # State schema definition
        ├── tools/          # Tavily search tool configuration
        └── ui/             # Streamlit UI custom components
```

---

## ⚙️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/rajan7838/Agentic-Chatbot.git
cd Agentic-Chatbot
```

### 2. Setup Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```
> **Note:** Enter your **Groq API Key** and **Tavily API Key** in the Streamlit sidebar to start chatting!

---

## 🔐 Environment Variables (For Cloud Deployment)
If deploying on **Streamlit Cloud**, add these lines to your **App Secrets**:

```toml
GROQ_API_KEY = "your_groq_key_here"
TAVILY_API_KEY = "your_tavily_key_here"
```
