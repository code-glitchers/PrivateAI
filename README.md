# 🛡️ PrivateAI - Local Offline RAG Assistant

A fully private, 100% offline AI chat assistant that runs on your local machine using [Ollama](https://ollama.com) and [Streamlit](https://streamlit.io). Chat with your PDF, TXT, and Markdown files safely.

![PrivateAI](https://img.shields.io/badge/Privacy-100%25%20Offline-green) ![License](https://img.shields.io/badge/License-MIT-blue)

## ✨ Features

- **100% Offline**: No data leaves your computer.
- **RAG (Retrieval Augmented Generation)**: Upload documents and chat with them.
- **Fast & Efficient**: Uses `llama3.2:1b` for quick responses on standard hardware.
- **Persistent Memory**: Documents are stored locally in a vector database (`ChromaDB`).
- **One-Click Run**: Simple `.bat` launcher for Windows.

## 🚀 Quick Start (Windows)

### Prerequisites
1. **Install Python 3.8+**: [python.org](https://www.python.org/downloads/)
2. **Install Ollama**: [ollama.com](https://ollama.com/download/windows)

### Installation

1. Clone or download this repository.
2. Run `START_PRIVATEAI.bat`
   - It will automatically set up the virtual environment, install dependencies, download AI models, and launch the app!

## 🛠️ Manual Installation

If you prefer using the command line:

```bash
# 1. Create venv
python -m venv venv
.\venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull models
ollama pull llama3.2:1b
ollama pull all-minilm

# 4. Run app
streamlit run app.py
```

## 📦 Project Structure

- `app.py`: Main Streamlit application.
- `START_PRIVATEAI.bat`: One-click launcher.
- `requirements.txt`: Python dependencies.
- `.chroma_db/`: Local database (created on first run).

## 📝 License

MIT License - feel free to modify and distribute!
