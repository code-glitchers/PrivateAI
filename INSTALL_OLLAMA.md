# PrivateAI - Installation Guide

## ⚠️ Ollama Not Found

You need to install Ollama to run this AI assistant.

## 📥 Installation Steps

### 1. Download Ollama
Visit: **https://ollama.com/download/windows**

Or use this direct link:
**https://ollama.com/download/OllamaSetup.exe**

### 2. Install Ollama
- Run the downloaded `OllamaSetup.exe`
- Follow the installation wizard
- It will install to: `C:\Users\[YourName]\AppData\Local\Programs\Ollama\`

### 3. Verify Installation
Open PowerShell and run:
```powershell
ollama --version
```

You should see the version number.

### 4. Download AI Models
```powershell
ollama pull llama3.2:1b
ollama pull all-minilm
```

### 5. Start Ollama Service
```powershell
ollama serve
```

Keep this terminal window open (Ollama must run in the background).

### 6. Launch PrivateAI
Open a NEW PowerShell window and run:
```powershell
cd "C:\Users\gamin\OneDrive\Desktop\private ai\PrivateAI"
.\start_app.bat
```

### 7. Access the App
Open your browser to: **http://localhost:8501**

---

## 🔧 Quick Troubleshooting

**If Ollama won't start:**
- Check Windows Firewall isn't blocking it
- Run PowerShell as Administrator

**If models won't download:**
- Check your internet connection
- Models are large (1-5GB each)

**If the app shows "Ollama not running":**
- Make sure `ollama serve` is running in a separate terminal
- Check http://localhost:11434 in your browser (should show "Ollama is running")

---

## 📞 Need Help?
The app is 100% local and offline once set up. No API keys needed!
