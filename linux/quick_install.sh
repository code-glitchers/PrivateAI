#!/bin/bash

# IncognitoAI Linux - Simple One-Command Install
# Copy this entire script to your terminal or run: bash quick_install.sh

cat << "EOF"
╔══════════════════════════════════════════════════════════════════╗
║     IncognitoAI - Linux Installation (One Command Setup)         ║
╚══════════════════════════════════════════════════════════════════╝
EOF

set -e

cd "$(dirname "$0")" || exit

# Make scripts executable
chmod +x setup.sh start.sh start_cyberpunk.sh

# Run setup
echo ""
echo "🚀 Starting automated setup..."
echo ""

./setup.sh

echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                   ✅ SETUP COMPLETE! ✅                          ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""
echo "📋 NEXT STEPS:"
echo ""
echo "  1️⃣  Start Ollama (in a new terminal):"
echo "     ollama serve"
echo ""
echo "  2️⃣  Launch IncognitoAI (choose one):"
echo "     OPTION A - Flask Cyberpunk (Recommended):"
echo "     ./start_cyberpunk.sh"
echo ""
echo "     OPTION B - Streamlit (Original):"
echo "     ./start.sh"
echo ""
echo "  3️⃣  Open in browser:"
echo "     Cyberpunk: http://localhost:5000"
echo "     Streamlit: http://localhost:8501"
echo ""
echo "💡 For more info, see README.md or QUICKSTART.txt"
echo ""
