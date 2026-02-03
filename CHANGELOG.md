# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-02-03

### 🚀 Initial Release
**PrivateAI Version 1.0** is now officially released! This version brings a fully private, offline AI chat experience to Windows.

### ✨ Features
- **100% Offline Architecture**: No data leaves your machine. Privacy first.
- **RAG Capability**: Upload PDF, TXT, or MD files and chat with them instantly.
- **Fast Inference**: Integrated `llama3.2:1b` (1B parameters) for rapid responses even on lower-end hardware.
- **Vector Memory**: Uses ChromaDB for persistent document storage and retrieval.
- **Easy Launcher**: Includes `START_PRIVATEAI.bat` for one-click startup.
- **Automatic Diagnostics**: Built-in verification scripts to ensure Ollama and Python are running correctly.

### 🛠️ Technical Details
- **Frontend**: Streamlit
- **LLM Engine**: Ollama (Llama 3.2)
- **Embeddings**: all-minilm
- **Database**: ChromaDB
- **OS Support**: Windows 10/11

---
*For installation instructions, please refer to the README.*
