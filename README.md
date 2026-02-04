# 🛡️ IncognitoAI – Local Offline RAG Assistant

<p align="center">
  <img src="https://github.com/code-glitchers/IncognitoAI/blob/main/IncognitoAI.png" alt="IncognitoAI Logo" >
</p>

A fully private, **100% offline AI chat assistant** that runs on your local machine using [Ollama](https://ollama.com) and [Streamlit](https://streamlit.io) or [Flask](https://flask.palletsprojects.com/).  
Chat with your **PDF, TXT, and Markdown** files safely and locally.

![Offline](https://img.shields.io/badge/Mode-100%25%20Offline-success?style=for-the-badge)
![Privacy](https://img.shields.io/badge/Privacy-Zero%20Telemetry-green?style=for-the-badge)
![RAG](https://img.shields.io/badge/AI-RAG%20Enabled-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Tested-Linux-black?style=for-the-badge&logo=linux)
![Windows](https://img.shields.io/badge/Tested-Windows-0078D6?style=for-the-badge&logo=windows)


---

## ✨ Features

- 📴 **100% Offline** – No data leaves your computer
- 📄 **RAG (Retrieval Augmented Generation)** – Chat with your documents
- ⚡ **Fast & Efficient** – Uses `llama3.2:1b` model
- 🧠 **Persistent Memory** – Local storage via `ChromaDB`
- 🖱️ **Multiple Interfaces** – Streamlit (web) & Flask Cyberpunk (modern UI)
- 🐧 **Cross-Platform** – Works on Windows, macOS, and Linux

---



## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** 
- **Ollama** ([ollama.com](https://ollama.com))
- **Git** (to clone the repository)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/code-glitchers/IncognitoAI.git
   cd IncognitoAI
   ```

2. **Run Setup** (Choose your platform)
   - **Windows:** Double-click `START_PRIVATEAI.bat`
   - **Linux/macOS:** `cd linux && chmod +x setup.sh && ./setup.sh`

3. **Start Ollama** (in a separate terminal)
   ```bash
   ollama serve
   ```

4. **Launch the App**
   - **Streamlit Version:**
     ```bash
     streamlit run app.py
     ```
   - **Flask Cyberpunk Version (Linux):**
     ```bash
     cd linux && chmod +x bot.sh && ./bot.sh
     ```

---

## 🖥️ Platform-Specific Setup

### 🪟 Windows
Run the one-click installer:
```batch
START_PRIVATEAI.bat
```

### 🐧 Linux / macOS
Follow the **[Linux/macOS Installation & Setup Guide](linux/README.md)**

--- 
## 📚 Usage

### Streamlit Interface (app.py)
- Open `http://localhost:8501`
- Upload PDF, TXT, or Markdown files
- Toggle RAG mode to search documents or ask general questions

### Flask Cyberpunk Interface (bot.py - Linux)
- Open `http://localhost:5000`
- Dark-themed neon aesthetic
- Real-time streaming responses
- Toggle between RAG and general chat modes

---

## 📦 Project Structure

```
IncognitoAI/
├── app.py                    # Streamlit application
├── requirements.txt          # Python dependencies
├── START_PRIVATEAI.bat       # Windows launcher
├── linux/
│   ├── bot.py               # Flask Cyberpunk app
│   ├── setup.sh             # Linux setup script
│   ├── start.sh             # Start Streamlit (Linux)
│   ├── bot.sh               # Start Flask app (Linux)
│   ├── templates/           # Flask HTML templates
│   ├── static/              # CSS and JavaScript
│   └── README.md            # Linux-specific guide
└── .chroma_db/              # Local vector database (auto-created)
```

---

## 🛠️ Models Used

- **LLM:** `llama3.2:1b` - Fast, efficient language model
- **Embeddings:** `all-minilm:latest` - Fast embedding model for RAG

Models are automatically downloaded on first run via Ollama.

---

## 🤝 Contributing

We welcome contributions! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 👥 Contributors and Developers

[<img src="https://avatars.githubusercontent.com/u/67865621?s=64&v=4" width="64" height="64" alt="haybnzz">](https://github.com/h9zdev)
[<img src="https://avatars.githubusercontent.com/u/108749445?s=64&v=4" width="64" height="64" alt="VaradScript">](https://github.com/varadScript)

---

## 📝 License

MIT License - feel free to modify and distribute!

For questions or support, open an issue on [GitHub](https://github.com/code-glitchers/IncognitoAI/issues).
