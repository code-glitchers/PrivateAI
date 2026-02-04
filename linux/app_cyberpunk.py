"""
IncognitoAI - Cyberpunk Flask Edition
A sleek, dark-themed AI assistant with neon aesthetics
"""

from flask import Flask, render_template, request, jsonify
import requests
import os
from pathlib import Path
import json
from datetime import datetime

# Configuration
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "llama3.2:1b"
EMBEDDING_MODEL = "all-minilm:latest"
DB_DIR = "./.chroma_db"
CACHE_DIR = "./.cache"

os.makedirs(CACHE_DIR, exist_ok=True)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize LangChain components
try:
    from langchain_ollama import OllamaEmbeddings, ChatOllama
    from langchain_community.vectorstores import Chroma
    
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vector_db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    llm = ChatOllama(model=MODEL_NAME, temperature=0, streaming=False)
except Exception as e:
    print(f"⚠️  Warning: LangChain initialization failed: {e}")
    print("Some features will be limited.")

# Helper Functions
def check_ollama():
    """Check if Ollama is running"""
    try:
        response = requests.get(OLLAMA_URL, timeout=2)
        return response.status_code == 200
    except:
        return False

def get_ai_response(query, use_rag=False):
    """Get response from Ollama"""
    try:
        context = ""
        
        if use_rag:
            # Search vector database
            results = vector_db.similarity_search(query, k=3)
            context = "\n".join([doc.page_content for doc in results])
        
        full_prompt = f"""You are a cyberpunk AI assistant named INCOGNITO. 
You have a futuristic, tech-savvy personality.
Keep responses concise and use tech terminology where appropriate.
Your responses should feel like they're coming from a neon-lit digital world.

User Query: {query}
{f"Context: {context}" if context else ""}

Respond as INCOGNITO:"""
        
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": full_prompt,
                "stream": False
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return "⚠️ Error: Could not connect to Ollama"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Routes
@app.route('/')
def index():
    """Main page"""
    ollama_status = check_ollama()
    return render_template('cyberpunk.html', ollama_status=ollama_status)

@app.route('/api/status')
def status():
    """Get system status"""
    return jsonify({
        "ollama_running": check_ollama(),
        "model": MODEL_NAME,
        "embedding_model": EMBEDDING_MODEL,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Chat endpoint"""
    data = request.json
    query = data.get('message', '').strip()
    use_rag = data.get('use_rag', False)
    
    if not query:
        return jsonify({"error": "Empty message"}), 400
    
    if not check_ollama():
        return jsonify({"error": "Ollama is not running"}), 503
    
    response = get_ai_response(query, use_rag)
    return jsonify({"response": response})

@app.route('/api/upload', methods=['POST'])
def upload():
    """Upload document for RAG"""
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    try:
        from langchain_community.document_loaders import PyPDFLoader, TextLoader
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        
        file_path = os.path.join(CACHE_DIR, file.filename)
        file.save(file_path)
        
        # Load document
        if file.filename.endswith('.pdf'):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path)
        
        docs = loader.load()
        
        # Split and store
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(docs)
        vector_db.add_documents(chunks)
        
        return jsonify({
            "success": True,
            "message": f"Uploaded {file.filename} - {len(chunks)} chunks indexed"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║           🌐 IncognitoAI - Cyberpunk Edition 🌐           ║
    ║                   Flask-based AI Assistant                ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    if not check_ollama():
        print("⚠️  WARNING: Ollama is not running!")
        print("   Start Ollama with: ollama serve")
        print("")
    
    print("🚀 Starting Flask server...")
    print("📱 Open http://localhost:5000 in your browser")
    print("")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
