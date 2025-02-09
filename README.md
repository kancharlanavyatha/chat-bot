# 🏛️ LangChain-Based Museum Chatbot

Welcome to the **MuseuAI Chatbot**, a conversational AI designed to answer queries about museums using **LangChain** and **OllamaLLM**. This chatbot processes user input, maintains a conversation history, and provides intelligent responses.

## 🚀 Features
- Uses **LangChain** to structure prompts and manage conversation flow.
- Powered by **OllamaLLM**, with support for models like **LLaMA3, Gemma2**, and more.
- Retains conversation history for context-aware responses.
- Simple command-line interface for easy interaction.

## 📂 Project Structure
- `main.py` – The chatbot's core logic and conversation handling.
- `requirements.txt` – Dependencies needed to run the chatbot.

## 🛠️ Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed, then run:
```bash
pip install langchain langchain_ollama
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 3️⃣ Run the Chatbot
```bash
python main.py
```

## 💬 How to Use
- Start the chatbot and ask any museum-related questions.
- The bot maintains a conversation history for better responses.
- Type **'exit'** to quit the chat.

## 🏗️ Customization
- Modify `model = OllamaLLM(model="llama3")` to use a different LLM.
- Edit the `template` variable to adjust the chatbot’s prompt format.



Enjoy using **MuseuAI**!If you have any suggestions or issues, feel free to contribute or reach out. 😊

