# 🛡️ IncognitoAI – Local Offline RAG Assistant

A fully private, **100% offline AI chat assistant** that runs on your local machine using [Ollama](https://ollama.com) and [Streamlit](https://streamlit.io).  
Chat with your **PDF, TXT, and Markdown** files safely and locally.

![Offline](https://img.shields.io/badge/Mode-100%25%20Offline-success?style=for-the-badge)
![Privacy](https://img.shields.io/badge/Privacy-Zero%20Telemetry-green?style=for-the-badge)
![RAG](https://img.shields.io/badge/AI-RAG%20Enabled-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## ✨ Features

- 📴 **100% Offline** – No data leaves your computer
- 📄 **RAG (Retrieval Augmented Generation)** – Chat with your documents
- ⚡ **Fast & Efficient** – Uses `llama3.2:1b`
- 🧠 **Persistent Memory** – Local storage via `ChromaDB`
- 🖱️ **One-Click Run** – Windows `.bat` launcher

---
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

  
## 👥 Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haybnzz">](https://github.com/h9zdev)
 [<img src="https://avatars.githubusercontent.com/u/108749445?s=64&v=4"  width="64" height="64" alt="VaradScript">](https://github.com/varadScript)

## 📝 License

MIT License - feel free to modify and distribute!
