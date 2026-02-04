# 📁 IncognitoAI Linux Setup - Complete File Structure

```
IncognitoAI/
│
├── 📄 README.md
├── 📄 CHANGELOG.md
├── 📄 LICENSE.md
├── 🐍 app.py                          (Streamlit version - original)
│
├── 🟢 setup.bat                       (Windows setup)
├── 🟢 START_PRIVATEAI.bat             (Windows launcher)
│
├── 🐧 linux/                          ← NEW LINUX FOLDER
│   │
│   ├── 📖 00_START_HERE.txt           ⭐ Read this first!
│   ├── 📖 QUICKSTART.txt              Quick reference guide
│   ├── 📖 README.md                   Complete Linux guide
│   ├── 📖 SETUP_COMPLETE.md           Setup summary
│   │
│   ├── 🔧 setup.sh                    Automated setup script ⚡
│   ├── ▶️  start.sh                    Launch Streamlit version
│   ├── ▶️  start_cyberpunk.sh          Launch Flask Cyberpunk ✨
│   ├── 🚀 quick_install.sh            One-command installer
│   │
│   ├── 🐍 app_cyberpunk.py            Flask Cyberpunk app
│   ├── 📋 requirements_flask.txt       Flask dependencies
│   │
│   ├── 📁 templates/
│   │   └── cyberpunk.html             Web interface (HTML)
│   │
│   └── 📁 static/
│       ├── cyberpunk.css              Neon styling (CSS)
│       └── cyberpunk.js               Interactivity (JavaScript)
│
└── 📋 requirements.txt                Python dependencies (main)
```

---

## 📊 WHAT'S INCLUDED

### 📝 Documentation Files (Start Here!)
| File | Purpose | Read Time |
|------|---------|-----------|
| `00_START_HERE.txt` | Visual overview | 2 min |
| `QUICKSTART.txt` | Quick reference | 1 min |
| `README.md` | Complete guide | 5 min |
| `SETUP_COMPLETE.md` | Detailed summary | 3 min |

### 🔧 Setup & Launch Scripts (Automated!)
| File | Purpose | Executable |
|------|---------|-----------|
| `setup.sh` | One-command setup | Yes ⚡ |
| `start.sh` | Streamlit launcher | Yes |
| `start_cyberpunk.sh` | Flask launcher | Yes ✨ |
| `quick_install.sh` | All-in-one installer | Yes |

### 🐍 Application Files (Python & Web)
| File | Purpose | Type |
|------|---------|------|
| `app_cyberpunk.py` | Flask backend | Python |
| `templates/cyberpunk.html` | Web interface | HTML |
| `static/cyberpunk.css` | Neon styling | CSS |
| `static/cyberpunk.js` | Interactive features | JavaScript |

### 📋 Configuration Files
| File | Purpose |
|------|---------|
| `requirements_flask.txt` | Flask dependencies |

---

## 🎯 WHERE TO START

### For First-Time Users:
1. **Read:** `00_START_HERE.txt` (visual overview)
2. **Read:** `QUICKSTART.txt` (quick reference)
3. **Run:** `./setup.sh` (automated setup)
4. **Launch:** `./start_cyberpunk.sh` (Flask Cyberpunk)
5. **Visit:** `http://localhost:5000` (in browser)

### For Experienced Users:
1. `chmod +x setup.sh && ./setup.sh`
2. In another terminal: `ollama serve`
3. In another terminal: `./start_cyberpunk.sh`
4. Open `http://localhost:5000`

---

## 🌟 TWO INTERFACES

### Flask Cyberpunk (Recommended) ✨
- Modern, beautiful neon design
- Real-time web interface
- Document upload with RAG
- Status monitoring
- Responsive layout

### Streamlit (Original) 📊
- Simple, clean interface
- Perfect for data science
- Drag-and-drop files
- Configuration options

---

## ⚙️ QUICK REFERENCE

### Setup (One Time)
```bash
cd linux
chmod +x *.sh
./setup.sh
```

### Running (Ongoing)
```bash
# Terminal 1
ollama serve

# Terminal 2
cd linux
./start_cyberpunk.sh    # Flask - Recommended!
# OR
./start.sh              # Streamlit
```

### Access
- **Flask Cyberpunk:** `http://localhost:5000`
- **Streamlit:** `http://localhost:8501`

---

## 📦 KEY FEATURES

✅ **100% Offline** - No data leaves your machine  
✅ **Automated Setup** - One script does everything  
✅ **Two Interfaces** - Choose your favorite  
✅ **Beautiful Design** - Cyberpunk aesthetic  
✅ **RAG Support** - Chat with documents  
✅ **Privacy First** - Zero telemetry  
✅ **Well Documented** - Multiple guides  
✅ **Easy to Use** - Simple shell scripts  

---

## 🚀 INSTALLATION SIZE

| Component | Size | Notes |
|-----------|------|-------|
| Linux folder | ~500 KB | Just code |
| Python packages | ~200 MB | Virtual env |
| Models | ~2.5 GB | Ollama AI models |
| **TOTAL** | **~2.7 GB** | One-time download |

---

## 🔒 PRIVACY & SECURITY

✅ All data stored locally  
✅ No accounts or login  
✅ No tracking or analytics  
✅ No third-party services  
✅ Open source (MIT License)  
✅ 100% offline after setup  

---

## 📞 NEED HELP?

1. **Quick answers:** See `QUICKSTART.txt`
2. **Setup issues:** See `README.md` - Troubleshooting section
3. **Error messages:** Read the terminal output carefully
4. **Main docs:** See `../README.md`

---

## 🎓 WHAT TO DO NEXT

1. Read `00_START_HERE.txt` (this folder)
2. Run `./setup.sh` to set up everything
3. Launch `./start_cyberpunk.sh` to start
4. Open `http://localhost:5000` in your browser
5. Try uploading a PDF and asking questions!

---

## 📋 SYSTEM REQUIREMENTS

- **OS:** Linux (Ubuntu 20.04+, Debian, Fedora, etc.)
- **Python:** 3.8+
- **RAM:** 4GB minimum
- **Disk:** 3GB free space
- **Internet:** For setup only

The `setup.sh` script will handle all installations!

---

## 🎉 YOU'RE ALL SET!

Your complete Linux setup is ready to go.

**Start with:** `00_START_HERE.txt`  
**Then run:** `./setup.sh`  
**Finally:** `./start_cyberpunk.sh`

Enjoy your private, offline AI assistant! 🌐✨

---

*Made with ❤️ for privacy-conscious users*  
*IncognitoAI - MIT License - Open Source*
