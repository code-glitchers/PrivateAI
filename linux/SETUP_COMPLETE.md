# 🐧 IncognitoAI Linux Setup - COMPLETE ✅

## 📦 What Was Created

A complete Linux setup folder with **TWO interfaces** for IncognitoAI:

### Folder Structure
```
linux/
├── 📄 QUICKSTART.txt              ← START HERE! Quick reference guide
├── 📄 README.md                   ← Full documentation
├── 🔧 setup.sh                    ← Automated setup script (make executable)
├── ▶️  start.sh                    ← Launch Streamlit version
├── ▶️  start_cyberpunk.sh          ← Launch Flask Cyberpunk version
├── 🐍 app_cyberpunk.py            ← Flask application
├── 📝 requirements_flask.txt       ← Flask dependencies
├── 📁 templates/
│   └── cyberpunk.html             ← Web interface
└── 📁 static/
    ├── cyberpunk.css              ← Neon cyberpunk styling
    └── cyberpunk.js               ← Interactive features
```

---

## 🎯 TWO INTERFACES AVAILABLE

### 1️⃣ **STREAMLIT VERSION** (Original)
- **File:** `start.sh`
- **Port:** `http://localhost:8501`
- **Features:** Simple, clean interface
- **Best for:** Quick testing

### 2️⃣ **FLASK CYBERPUNK VERSION** (New!) ✨
- **File:** `start_cyberpunk.sh`
- **Port:** `http://localhost:5000`
- **Features:**
  - 🌐 Beautiful neon cyberpunk aesthetic
  - 💬 Real-time chat interface
  - 📁 Document upload with RAG
  - 🔄 RAG mode toggle
  - 🟢 System status indicator
  - 📱 Responsive design

**Recommended:** Use Flask Cyberpunk version for best experience!

---

## 🚀 QUICK START (3 Steps)

### Step 1: Initial Setup (ONE TIME)
```bash
cd linux
chmod +x *.sh
./setup.sh
```

This will:
- ✅ Install Python 3 (if needed)
- ✅ Create virtual environment
- ✅ Install dependencies
- ✅ Install Ollama (if needed)
- ✅ Download AI models (5-10 minutes)

### Step 2: Start Ollama (New Terminal)
```bash
ollama serve
```

### Step 3: Launch IncognitoAI (New Terminal)
```bash
cd linux
./start_cyberpunk.sh    # Flask Cyberpunk (recommended!)
# OR
./start.sh              # Streamlit version
```

---

## 🎨 Flask Cyberpunk Features

### Interface Design
- **Dark Theme:** Cyberpunk aesthetic with neon accents
- **Neon Colors:** Pink, cyan, purple, green glows
- **Responsive:** Works on desktop and mobile
- **Animations:** Smooth transitions and effects

### Functionality
- 💬 **Real-time Chat:** Type and get instant responses
- 📁 **Upload Documents:** PDF, TXT, Markdown support
- 🧠 **RAG Mode:** Chat with your documents
- 🔍 **Status Monitor:** See if Ollama is running
- 📊 **System Info:** Model details and features

### User Experience
- Auto-focus on input field
- Enter to send, Shift+Enter for newline
- Typing indicator while waiting for response
- Scroll to latest message
- Clean message history

---

## 📋 FILES EXPLAINED

| File | Purpose |
|------|---------|
| `setup.sh` | Automated Linux setup - installs everything |
| `start.sh` | Launches Streamlit interface |
| `start_cyberpunk.sh` | Launches Flask Cyberpunk interface |
| `app_cyberpunk.py` | Flask app with AI logic |
| `cyberpunk.html` | Web page HTML |
| `cyberpunk.css` | Neon cyberpunk styling |
| `cyberpunk.js` | Interactive chat functionality |
| `QUICKSTART.txt` | Quick reference guide |
| `README.md` | Complete documentation |

---

## 🔧 REQUIREMENTS

### System Requirements
- **OS:** Linux (Ubuntu 20.04+, Debian, Fedora, etc.)
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Disk:** 2GB+ free space
- **Internet:** For initial setup only

### Auto-Installed by Setup Script
- Python packages (Flask, LangChain, ChromaDB, etc.)
- Ollama (AI runtime)
- AI models (llama3.2:1b, all-minilm)

---

## 🌟 KEY FEATURES

### IncognitoAI Linux Setup
✅ **One-click setup** - Fully automated  
✅ **Two interfaces** - Streamlit + Flask Cyberpunk  
✅ **Beautiful design** - Modern cyberpunk aesthetic  
✅ **Fast performance** - Optimized for Linux  
✅ **RAG support** - Chat with documents  
✅ **100% offline** - No data leaves your machine  
✅ **Easy to use** - Simple shell scripts  
✅ **Well documented** - Multiple guides included  

---

## ⚙️ HOW IT WORKS

### Architecture
```
Your Computer (Linux)
    ↓
Ollama (AI Engine) - Port 11434
    ↓
Flask App (Web Interface) - Port 5000
    ↓
Browser (http://localhost:5000)
```

### Data Flow
1. **User Input** → Web browser sends message
2. **Processing** → Flask app prepares query
3. **AI Response** → Ollama generates response
4. **Display** → Flask sends response to browser
5. **ALL LOCAL** → Nothing leaves your computer

---

## 📝 USAGE EXAMPLES

### Basic Chat
1. Open http://localhost:5000
2. Type your question
3. Press Enter
4. Get instant response

### RAG Mode (Chat with Documents)
1. Click 📁 button
2. Select PDF/TXT/Markdown file
3. Upload completes automatically
4. Enable "RAG" toggle
5. Ask questions about your document

### Models
- **llama3.2:1b** - Fast, efficient AI model
- **all-minilm** - Embedding model for document search

---

## 🐛 TROUBLESHOOTING

### Setup Issues

**Q: "ollama: command not found"**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Q: "Python not found"**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

**Q: "Permission denied on script"**
```bash
chmod +x setup.sh start.sh start_cyberpunk.sh
```

### Runtime Issues

**Q: "Connection refused" on port 5000**
```bash
# Port already in use - edit app_cyberpunk.py:
# Change: app.run(debug=True, host='0.0.0.0', port=5000)
# To:     app.run(debug=True, host='0.0.0.0', port=5001)
```

**Q: "Ollama offline" warning**
- Make sure to run `ollama serve` in another terminal

**Q: "Models not loading"**
```bash
ollama pull llama3.2:1b
ollama pull all-minilm
```

---

## 🔒 PRIVACY & SECURITY

✅ **100% Offline** - No data sent anywhere  
✅ **No Tracking** - Zero telemetry  
✅ **No Ads** - Clean interface  
✅ **Open Source** - MIT License  
✅ **Your Data** - Stored only on your machine  
✅ **No Account** - No login required  

---

## 📚 DOCUMENTATION

- **[QUICKSTART.txt](QUICKSTART.txt)** - Quick reference (read first!)
- **[README.md](README.md)** - Complete guide
- **[../README.md](../README.md)** - Main project docs
- Ollama: https://ollama.ai
- Flask: https://flask.palletsprojects.com

---

## 💡 TIPS & TRICKS

1. **Use both interfaces** - Try Streamlit and Cyberpunk
2. **Upload documents** - Test RAG with your PDFs
3. **Clear cache** - Delete `.chroma_db` folder to reset
4. **Change theme** - Edit `static/cyberpunk.css`
5. **Different models** - Change `MODEL_NAME` in `app_cyberpunk.py`

---

## 🎓 LEARNING PATH

1. Run setup script
2. Open QUICKSTART.txt
3. Try Flask Cyberpunk version
4. Upload a test document
5. Explore RAG mode
6. Read full README.md
7. Customize and extend

---

## 📞 SUPPORT

Having issues? Check:
1. QUICKSTART.txt (this file) - Common issues
2. README.md - Detailed guide
3. ../README.md - Main documentation
4. Terminal error messages - Usually very helpful

---

## 🎉 YOU'RE ALL SET!

Your Linux IncognitoAI setup is complete and ready to use.

### Next Steps:
1. Run `./setup.sh` in the linux folder
2. Start Ollama in another terminal
3. Launch the Cyberpunk interface
4. Start chatting!

**Enjoy your private, offline AI assistant!** 🌐✨

---

*IncognitoAI - Made with ❤️ for privacy-conscious users*
*MIT License - Open Source*
