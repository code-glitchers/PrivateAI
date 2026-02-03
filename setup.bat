@echo off
echo 🛠️  Setting up PrivateAI Environment...

REM 1. Create Virtual Environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM 2. Install Dependencies
echo ⬇️  Installing Python dependencies...
.\venv\Scripts\pip install -q -r requirements.txt

REM 3. Pull Ollama Models
echo 🦙 Pulling Ollama models (this may take a while if not cached)...
echo    - Pulling llama3...
ollama pull llama3
echo    - Pulling all-minilm (embeddings)...
ollama pull all-minilm

echo.
echo ✅ Setup Complete! 
echo 🚀 Run 'start_app.bat' to launch the assistant.
pause
