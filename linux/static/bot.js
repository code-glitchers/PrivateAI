/* IncognitoAI Cyberpunk JavaScript */

const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const ragMode = document.getElementById('rag-mode');
const uploadBtn = document.getElementById('upload-btn');
const fileInput = document.getElementById('file-input');
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');

// Auto-focus input
userInput.focus();

// Check Ollama status
async function checkStatus() {
    try {
        const response = await fetch('/api/status');
        const data = await response.json();
        
        if (data.ollama_running) {
            statusDot.classList.remove('offline');
            statusText.textContent = 'ONLINE';
        } else {
            statusDot.classList.add('offline');
            statusText.textContent = 'OLLAMA OFFLINE';
        }
    } catch (e) {
        statusDot.classList.add('offline');
        statusText.textContent = 'ERROR';
    }
}

// Check status on load and periodically
checkStatus();
setInterval(checkStatus, 10000);

// Send message
async function sendMessage() {
    const message = userInput.value.trim();
    if (!message) return;

    // Add user message to chat
    addMessage(message, 'user');
    userInput.value = '';
    userInput.focus();

    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message ai typing';
    typingDiv.innerHTML = '<div class="message-content"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>';
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                use_rag: ragMode.checked
            })
        });

        const data = await response.json();
        typingDiv.remove();

        if (response.ok) {
            addMessage(data.response, 'ai');
        } else {
            addMessage(`❌ Error: ${data.error}`, 'ai');
        }
    } catch (error) {
        typingDiv.remove();
        addMessage(`❌ Error: ${error.message}`, 'ai');
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.innerHTML = `<div class="message-content">${escapeHtml(text)}</div>`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Escape HTML
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Event listeners
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// File upload
uploadBtn.addEventListener('click', () => fileInput.click());

fileInput.addEventListener('change', async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    addMessage(`📁 Uploading ${file.name}...`, 'system-message');

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        if (response.ok) {
            addMessage(`✅ ${data.message}`, 'system-message');
            ragMode.checked = true; // Auto-enable RAG
        } else {
            addMessage(`❌ Upload failed: ${data.error}`, 'system-message');
        }
    } catch (error) {
        addMessage(`❌ Error: ${error.message}`, 'system-message');
    }

    fileInput.value = '';
});

// Add CSS for typing animation
const style = document.createElement('style');
style.textContent = `
    .typing-dot {
        display: inline-block;
        width: 4px;
        height: 4px;
        margin: 0 2px;
        background: currentColor;
        border-radius: 50%;
        animation: typing 1.4s infinite;
    }
    
    .typing-dot:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dot:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing {
        0%, 60%, 100% { opacity: 0.3; transform: translateY(0); }
        30% { opacity: 1; transform: translateY(-4px); }
    }
`;
document.head.appendChild(style);
