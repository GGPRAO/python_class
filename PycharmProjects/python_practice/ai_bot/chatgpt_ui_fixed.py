import streamlit as st
import ollama
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Chat with GGPRAO AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
    /* Main background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Chat container styling */
    .chat-container {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Message styling */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        margin-left: auto;
        word-wrap: break-word;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .assistant-message {
        background: #f0f0f0;
        color: #333;
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        margin-right: auto;
        word-wrap: break-word;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Header styling */
    .header-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Info text */
    .info-text {
        text-align: center;
        color: #666;
        font-size: 0.9em;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model_name" not in st.session_state:
    st.session_state.model_name = "qwen2:1.5b"

# Header
st.markdown('<div class="header-text">🤖 Qwen AI Chat</div>', unsafe_allow_html=True)
st.markdown('<div class="info-text">Chat with your local Qwen2 model - powered by Ollama</div>', unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.session_state.model_name = st.text_input(
        "Model Name",
        value=st.session_state.model_name,
        help="Enter the Ollama model name (e.g., qwen2:1.5b)"
    )

    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.success("Chat history cleared!")

    st.divider()
    st.markdown("### About")
    st.markdown("""
    - **Model**: Qwen2 via Ollama
    - **Features**: Fast, local inference
    - **Type**: Chat interface
    """)

# Display chat history
st.markdown("---")

# Create a container for messages
with st.container():
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)

# Input section with form
st.markdown("---")

# Use columns for better layout
col1, col2 = st.columns([0.85, 0.15])

with col1:
    user_input = st.text_input(
        label="Message",
        placeholder="Type your message here...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send ➤", use_container_width=True)

# Handle message sending
if send_button or user_input:
    if user_input:
        message_text = user_input.strip()

        if message_text:
            # Add user message to history
            st.session_state.messages.append({
                "role": "user",
                "content": message_text
            })

            # Show thinking indicator
            with st.spinner("🤔 Thinking..."):
                try:
                    # Call Ollama
                    response = ollama.chat(
                        model=st.session_state.model_name,
                        messages=st.session_state.messages
                    )

                    assistant_message = response["message"]["content"]

                    # Add assistant response to history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": assistant_message
                    })

                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
                    st.error(f"Failed to get response: {str(e)}")

            # Rerun to update
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.8em;">
        Made with ❤️ | Streamlit + Ollama + Qwen2
    </div>
""", unsafe_allow_html=True)

