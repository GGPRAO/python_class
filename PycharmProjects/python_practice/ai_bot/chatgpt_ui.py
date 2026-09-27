#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GGPRAO AI Chat Application
Fixed: PyArrow DLL error with environment variable

IMPORTANT: This fix MUST come before ANY imports
"""

import os
import sys

# ============================================================================
# PYARROW DLL ERROR FIX - MUST BE FIRST
# ============================================================================
# Set this BEFORE importing anything that depends on PyArrow
# This prevents: ImportError: DLL load failed - Application Control policy
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'
os.environ['ARROW_IGNORE_TIMEZONE'] = '1'

# Alternative workarounds (uncomment if needed)
# os.environ['PYARROW_OVERRIDE_TIMEZONE_DB_PATH'] = '1'
# ============================================================================

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
    /* Root variables */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* Main background */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #fff;
    }
    
    /* Page container */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    
    /* Chat container styling */
    .chat-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 25px;
        box-shadow: var(--shadow);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* User message styling */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 14px 18px;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 80%;
        margin-left: auto;
        word-wrap: break-word;
        box-shadow: var(--shadow-sm);
        animation: slideInRight 0.3s ease-out;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    /* Assistant message styling */
    .assistant-message {
        background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
        color: #2d3436;
        padding: 14px 18px;
        border-radius: 20px;
        margin: 10px 0;
        max-width: 80%;
        margin-right: auto;
        word-wrap: break-word;
        box-shadow: var(--shadow-sm);
        animation: slideInLeft 0.3s ease-out;
        border-left: 4px solid #667eea;
    }
    
    /* Animations */
    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 12px 16px;
        background: rgba(255, 255, 255, 0.9);
        color: #333;
        font-size: 1em;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
        background: white;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 24px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: var(--shadow-sm);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Header styling */
    .header-text {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3em;
        font-weight: 900;
        text-align: center;
        margin-bottom: 20px;
        letter-spacing: 2px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Info text */
    .info-text {
        text-align: center;
        color: #999;
        font-size: 1em;
        margin-bottom: 15px;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    
    .sidebar-content {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 20px 0;
    }
    
    /* Loading indicator */
    .loading {
        animation: pulse 1.5s infinite;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #aaa;
        font-size: 0.85em;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model_name" not in st.session_state:
    st.session_state.model_name = "qwen2:1.5b"

# Header
st.markdown('<div class="header-text">🤖 GGPRAO AI Chat</div>', unsafe_allow_html=True)
st.markdown("""
    <div class="info-text">
        ✨ Chat with your local Qwen2 model - Powered by Ollama & Streamlit ✨
    </div>
""", unsafe_allow_html=True)

# Sidebar for settings
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    st.session_state.model_name = st.text_input(
        "🤖 Model Name",
        value=st.session_state.model_name,
        help="Enter the Ollama model name (e.g., qwen2:1.5b, llama2, mistral)"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.messages = []
            st.success("✅ Chat cleared!")

    with col2:
        msg_count = len(st.session_state.messages)
        st.metric("Messages", msg_count)

    st.markdown("---")

    st.markdown("### ℹ️ About This App")
    st.markdown("""
    **Qwen2 AI Chat Interface**
    
    - 🚀 **Model**: GGPRAO via Ollama
    - ⚡ **Speed**: Ultra-fast local inference
    - 🔒 **Privacy**: No data sent online
    - 🎨 **UI**: Beautiful Streamlit interface
    - 📱 **Responsive**: Mobile-friendly design
    
    **Tips:**
    - Use natural language
    - Be specific for better responses
    - Clear history to start fresh
    """)

    st.markdown("---")

    st.markdown("### 📚 Features")
    st.markdown("""
    ✅ Real-time chat responses
    ✅ Message history tracking
    ✅ Custom model selection
    ✅ Beautiful animations
    ✅ Error handling
    ✅ Responsive UI
    """)

# Display chat history
st.markdown("---")

if len(st.session_state.messages) == 0:
    st.markdown("""
        <div style="text-align: center; padding: 40px; color: #999;">
            <h3>👋 Welcome to GGPRAO AI Chat</h3>
            <p>Start a conversation by typing your message below</p>
        </div>
    """, unsafe_allow_html=True)

chat_container = st.container()

with chat_container:
    for i, message in enumerate(st.session_state.messages):
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">🤖 {message["content"]}</div>', unsafe_allow_html=True)

# Input section
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

                    st.success("✅ Response received!")

                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}\n\n💡 Make sure Ollama is running and the model '{st.session_state.model_name}' is installed."
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg
                    })
                    st.error(f"⚠️ Connection Error: {str(e)}")

            # Rerun to update
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #999; font-size: 0.8em;">
        Made with ❤️ | Streamlit + Ollama + Qwen2
    </div>
""", unsafe_allow_html=True)

