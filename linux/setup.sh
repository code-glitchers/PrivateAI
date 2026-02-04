#!/bin/bash

# IncognitoAI Linux Setup Script
# Simple one-click setup for Linux users

echo "🛠️  Setting up IncognitoAI Linux Environment..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Check if Python is installed
echo -e "${BLUE}📋 Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${YELLOW}❌ Python 3 not found. Installing...${NC}"
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip python3-venv
else
    echo -e "${GREEN}✅ Python 3 found${NC}"
fi

# 2. Create Virtual Environment
if [ ! -d "venv" ]; then
    echo -e "${BLUE}📦 Creating virtual environment...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

# 3. Activate Virtual Environment and Install Dependencies
echo -e "${BLUE}⬇️  Installing Python dependencies...${NC}"
source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r ../requirements.txt
echo -e "${GREEN}✅ Dependencies installed${NC}"

# 4. Check if Ollama is installed
echo ""
echo -e "${BLUE}🦙 Checking Ollama installation...${NC}"
if ! command -v ollama &> /dev/null; then
    echo -e "${YELLOW}❌ Ollama not found. Installing...${NC}"
    curl -fsSL https://ollama.ai/install.sh | sh
    echo -e "${GREEN}✅ Ollama installed${NC}"
else
    echo -e "${GREEN}✅ Ollama found${NC}"
fi

# 5. Pull Ollama Models
echo ""
echo -e "${BLUE}📥 Pulling Ollama models (this may take a while)...${NC}"
echo -e "   Pulling llama3.2:1b..."
ollama pull llama3.2:1b
echo -e "   Pulling all-minilm (embeddings)..."
ollama pull all-minilm

echo ""
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${BLUE}🚀 Run './start.sh' to launch the assistant.${NC}"
echo ""
