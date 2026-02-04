# 🐧 IncognitoAI - Linux Setup Guide

A complete Linux setup for IncognitoAI with both Streamlit and Flask-based Cyberpunk interfaces.

## 📋 Contents

- `setup.sh` - Automated Linux setup script
- `start.sh` - Launch Streamlit version
- `start_cyberpunk.sh` - Launch Flask Cyberpunk version
- `app_cyberpunk.py` - Flask-based cyberpunk AI interface
- `templates/` - HTML templates for Flask app
- `static/` - CSS and JavaScript for Flask app

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- ✅ Check/install Python 3
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Check/install Ollama
- ✅ Download AI models

### Option 2: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r ../requirements.txt

# Pull models
ollama pull llama3.2:1b
ollama pull all-minilm
```

## 🎯 Running the Apps

### Streamlit Version (Original)
```bash
chmod +x start.sh
./start.sh
```
- Opens at `http://localhost:8501`
- Clean, simple interface
- Drag-and-drop document upload

### Flask Cyberpunk Version (New!)
```bash
chmod +x start_cyberpunk.sh
./start_cyberpunk.sh
```
- Opens at `http://localhost:5000`
- Neon cyberpunk aesthetic
- Modern, sleek design
- RAG mode toggle

## ⚙️ Prerequisites

- **Linux** (Ubuntu 20.04+, Debian, Fedora, etc.)
- **Python 3.8+**
- **Ollama** (will be installed automatically)
- **Internet** (for initial model download)

## 📦 System Dependencies

The setup script will auto-install:
- `python3`
- `python3-pip`
- `python3-venv`

## 🦙 Ollama Setup

Ollama must be running in a separate terminal:

```bash
ollama serve
```

The setup script installs Ollama if not present. If you need to install manually:

```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

## 📖 Usage

### Starting the Assistant

1. **Terminal 1 - Start Ollama:**
   ```bash
   ollama serve
   ```

2. **Terminal 2 - Start IncognitoAI:**
   ```bash
   cd linux
   ./start.sh          # For Streamlit
   # or
   ./start_cyberpunk.sh # For Flask
   ```

3. Open your browser:
   - Streamlit: `http://localhost:8501`
   - Cyberpunk: `http://localhost:5000`

### Chat with Documents (RAG Mode)

1. **Upload a document** (PDF, TXT, or Markdown)
2. **Enable RAG toggle** in the UI
3. **Ask questions** about your document

The AI will use your documents for context.

## 🎨 Flask Cyberpunk Features

- 🌐 Modern web interface
- 💜 Neon cyberpunk aesthetic
- ⚡ Real-time chat
- 📁 Document upload (RAG)
- 🔄 RAG mode toggle
- 🟢 System status indicator
- 📱 Responsive design

## 🔧 Troubleshooting

### Ollama Not Found
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Python Not Found
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Permission Denied
```bash
chmod +x setup.sh start.sh start_cyberpunk.sh
```

### Port Already in Use

**Streamlit (8501):**
```bash
streamlit run ../app.py --server.port 8502
```

**Flask (5000):**
Edit `app_cyberpunk.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Models Not Loading
```bash
ollama pull llama3.2:1b
ollama pull all-minilm
```

## 📝 Configuration

### Using Different Models

Edit the top of `app_cyberpunk.py` or `../app.py`:

```python
MODEL_NAME = "llama2:7b"  # or your preferred model
EMBEDDING_MODEL = "nomic-embed-text:latest"
```

### Changing Flask Port

In `app_cyberpunk.py`, line ~155:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000
```

## 🔐 Privacy & Security

- ✅ 100% Offline - No data leaves your computer
- ✅ Zero Telemetry - No tracking or analytics
- ✅ Open Source - Transparent and auditable
- ✅ Local Storage - All data stored locally

## 📚 Dependencies

Key Python packages installed:
- `flask` - Web framework
- `langchain` - AI orchestration
- `langchain-ollama` - Ollama integration
- `chromadb` - Vector database
- `requests` - HTTP client
- And more in `requirements.txt`

## 💡 Tips

- Streamlit (original) is simpler and great for quick testing
- Flask Cyberpunk is modern and great for daily use
- Both share the same AI models and vector database
- You can run both simultaneously (different ports)
- RAG mode is powerful - use it for document analysis

## 🚀 Next Steps

1. Customize the cyberpunk CSS in `static/cyberpunk.css`
2. Modify Flask app in `app_cyberpunk.py` for custom features
3. Add more models: `ollama pull [model-name]`
4. Experiment with different embedding models

## 📞 Support

For issues, refer to:
- Main README: `../README.md`
- Ollama docs: https://ollama.ai
- Flask docs: https://flask.palletsprojects.com
- LangChain docs: https://python.langchain.com

---

**Happy chatting with your private AI! 🌐✨**
