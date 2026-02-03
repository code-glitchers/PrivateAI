import streamlit as st
import os
import requests
import shutil

# --- Configuration ---
OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "llama3.2:1b"
EMBEDDING_MODEL = "all-minilm:latest"  # Faster embedding model
DB_DIR = "./.chroma_db"
CACHE_DIR = "./.cache"

os.makedirs(CACHE_DIR, exist_ok=True)

st.set_page_config(page_title="PrivateAI - Local RAG Assistant", layout="wide")

# --- Cached Resources (Lazy Loading) ---

@st.cache_resource(show_spinner=False)
def get_embeddings():
    from langchain_ollama import OllamaEmbeddings
    return OllamaEmbeddings(model=EMBEDDING_MODEL)

@st.cache_resource(show_spinner=False)
def get_vector_db():
    from langchain_community.vectorstores import Chroma
    return Chroma(persist_directory=DB_DIR, embedding_function=get_embeddings())

@st.cache_resource(show_spinner=False)
def get_llm():
    from langchain_ollama import ChatOllama
    return ChatOllama(model=MODEL_NAME, temperature=0, streaming=True)

# --- Logic Functions ---

def check_ollama():
    try:
        return requests.get(OLLAMA_URL, timeout=2).status_code == 200
    except:
        return False

def process_document(uploaded_file):
    from langchain_community.document_loaders import PyPDFLoader, TextLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    try:
        file_path = os.path.join(CACHE_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        if uploaded_file.name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path, encoding="utf-8")
        
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = splitter.split_documents(docs)
        
        get_vector_db().add_documents(splits)
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

# --- UI ---

st.title("🛡️ PrivateAI")

if not check_ollama():
    st.error("❌ Ollama not running! Run `ollama serve` first.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("📄 Documents")
    files = st.file_uploader("Upload PDF, TXT, MD", type=["pdf", "txt", "md"], accept_multiple_files=True)
    
    if st.button("Process") and files:
        for f in files:
            if process_document(f):
                st.success(f"✅ {f.name}")
    
    if st.button("Clear All"):
        st.session_state.messages = []
        if os.path.exists(DB_DIR):
            shutil.rmtree(DB_DIR)
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        
        try:
            docs = get_vector_db().similarity_search(prompt, k=4)
        except Exception as e:
            st.error(f"Search failed: {e}")
            st.stop()
        context = "\n\n".join([d.page_content for d in docs])
        
        system = f"Answer based on context. If not in context, say you don't know.\n\nContext:\n{context}"
        
        response = ""
        for chunk in get_llm().stream([("system", system), ("human", prompt)]):
            response += chunk.content
            placeholder.markdown(response + "▌")
        
        placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
