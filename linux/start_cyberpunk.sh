#!/bin/bash

# IncognitoAI Cyberpunk Version Starter (Linux Flask)
# Launch the cyberpunk Flask app

echo "🚀 Starting IncognitoAI Cyberpunk Edition..."
echo ""

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run setup.sh first!"
    exit 1
fi

source venv/bin/activate

# Check if Ollama is running
echo "🔍 Checking if Ollama is running..."
if ! curl -s http://localhost:11434 > /dev/null 2>&1; then
    echo "⚠️  Ollama is not running. Please start Ollama in another terminal with:"
    echo "   ollama serve"
    echo ""
    read -p "Press Enter to continue anyway, or Ctrl+C to cancel..."
fi

# Start the Flask app
echo "🌐 Launching IncognitoAI Cyberpunk Edition..."
echo "📱 Open browser and go to: http://localhost:5000"
echo ""
python app_cyberpunk.py
