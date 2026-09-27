# 🎨 UI Code Snippets & Customization Guide

## 📋 Table of Contents
1. PyArrow Fix Code
2. CSS Styling Code
3. Sidebar Features
4. Color Themes
5. Customization Examples

---

## 1️⃣ PyArrow Fix Code (REQUIRED)

### The Fix:
```python
import os
# Fix PyArrow DLL error - MUST be before any pyarrow imports!
os.environ['PYARROW_IGNORE_TIMEZONE'] = '1'

import streamlit as st
import ollama
from datetime import datetime
```

### Why It Works:
- Sets environment variable before PyArrow imports
- Prevents Windows Application Guard from blocking DLL
- Solves: "DLL load failed while importing lib: An Application Control policy has blocked"

---

## 2️⃣ Beautiful CSS Styling Code

### Header Styling:
```css
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
}
```

### User Message (Purple Gradient):
```css
.user-message {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 14px 18px;
    border-radius: 20px;
    margin: 10px 0;
    max-width: 80%;
    margin-left: auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    animation: slideInRight 0.3s ease-out;
    border: 1px solid rgba(255, 255, 255, 0.2);
}
```

### Assistant Message (Light Gray with Border):
```css
.assistant-message {
    background: linear-gradient(135deg, #f5f7fa 0%, #e9ecef 100%);
    color: #2d3436;
    padding: 14px 18px;
    border-radius: 20px;
    margin: 10px 0;
    max-width: 80%;
    margin-right: auto;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    animation: slideInLeft 0.3s ease-out;
    border-left: 4px solid #667eea;
}
```

### Smooth Animations:
```css
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
```

### Button Styling:
```css
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 12px 24px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.stButton > button:active {
    transform: translateY(0);
}
```

### Input Field Styling:
```css
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
```

---

## 3️⃣ Sidebar Features Code

### Settings Section:
```python
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    st.session_state.model_name = st.text_input(
        "🤖 Model Name",
        value=st.session_state.model_name,
        help="Enter the Ollama model name (e.g., qwen2:1.5b, llama2, mistral)"
    )
```

### Clear History & Message Counter:
```python
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.messages = []
            st.success("✅ Chat cleared!")
    
    with col2:
        msg_count = len(st.session_state.messages)
        st.metric("Messages", msg_count)
```

### About Section:
```python
    st.markdown("---")
    st.markdown("### ℹ️ About This App")
    st.markdown("""
    **Qwen2 AI Chat Interface**
    
    - 🚀 **Model**: GGPRAO via Ollama
    - ⚡ **Speed**: Ultra-fast local inference
    - 🔒 **Privacy**: No data sent online
    - 🎨 **UI**: Beautiful Streamlit interface
    - 📱 **Responsive**: Mobile-friendly design
    """)
```

---

## 4️⃣ Color Theme Options

### 🟣 Current Theme (Purple):
```css
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### 🔵 Blue-to-Purple:
```css
--primary-gradient: linear-gradient(135deg, #4158d0 0%, #c850c0 100%);
```

### 🟢 Green-to-Teal:
```css
--primary-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
```

### 🔴 Pink-to-Red:
```css
--primary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
```

### 🟠 Orange-to-Yellow:
```css
--primary-gradient: linear-gradient(135deg, #f2994e 0%, #f2c94c 100%);
```

### 🔮 Rainbow (Vibrant):
```css
--primary-gradient: linear-gradient(135deg, #ff0000 0%, #ff7f00 25%, #ffff00 50%, #00ff00 75%, #0000ff 100%);
```

### ⚫ Dark Mode (Blue-Black):
```css
--primary-gradient: linear-gradient(135deg, #667eea 0%, #1a1a2e 100%);
```

---

## 5️⃣ Customization Examples

### Example 1: Change Color Theme to Green
```python
# Find this line in CSS:
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Replace with:
--primary-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
```

### Example 2: Add Pulse Animation to Messages
```css
@keyframes pulse {
    0%, 100% { 
        opacity: 1;
        transform: scale(1);
    }
    50% { 
        opacity: 0.8;
        transform: scale(1.02);
    }
}

.assistant-message {
    animation: pulse 2s infinite;
}
```

### Example 3: Make Buttons Larger
```css
.stButton > button {
    padding: 16px 32px;  /* Increased from 12px 24px */
    font-size: 1.1em;     /* Slightly larger text */
}
```

### Example 4: Add Floating Animation
```css
@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-10px);
    }
}

.header-text {
    animation: float 3s ease-in-out infinite;
}
```

### Example 5: Enhanced Shadow Effect
```css
.user-message {
    box-shadow: 
        0 2px 8px rgba(102, 126, 234, 0.2),
        0 8px 16px rgba(102, 126, 234, 0.15),
        inset -2px -2px 5px rgba(0, 0, 0, 0.1);
}
```

---

## 🔧 How to Apply These Changes

### Step 1: Open chatgpt_ui.py
```bash
code chatgpt_ui.py
```

### Step 2: Find the CSS Section
```python
st.markdown("""
    <style>
    /* CSS goes here */
    </style>
""", unsafe_allow_html=True)
```

### Step 3: Replace CSS Rules
Copy and paste new CSS rules into this section

### Step 4: Save File
```bash
Ctrl + S
```

### Step 5: Refresh Streamlit
The app will auto-reload

---

## 📝 Complete Color Palette

### Accent Colors:
```
Purple:     #667eea
Dark Purple: #764ba2
Light Gray: #f5f7fa
Dark Gray:  #e9ecef
Text Dark:  #2d3436
```

### Shadow Colors:
```
Shadow Sm:   rgba(0, 0, 0, 0.1)
Shadow Md:   rgba(0, 0, 0, 0.15)
Shadow Lg:   rgba(0, 0, 0, 0.2)
```

---

## ✨ Pro Tips

1. **Use consistent colors** - Stick to 2-3 main colors
2. **Add transitions** - Make interactions smooth
3. **Use shadows** - Create depth and hierarchy
4. **Keep contrast** - Ensure text is readable
5. **Test on mobile** - Check responsive design
6. **Use animations sparingly** - Don't overdo it
7. **Keep file size small** - CSS should be efficient
8. **Comment your CSS** - Document what each section does

---

## 🚀 Quick Apply Template

Want to change the entire color scheme? Use this template:

```python
st.markdown("""
    <style>
    :root {
        --primary-color: #YOUR_COLOR_HERE;
        --secondary-color: #YOUR_COLOR_HERE;
    }
    
    .user-message {
        background: var(--primary-color);
    }
    
    .stButton > button {
        background: var(--primary-color);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--secondary-color);
    }
    </style>
""", unsafe_allow_html=True)
```

---

## 🎨 Beautiful UI Checklist

- ✅ PyArrow DLL fix applied
- ✅ Gradient backgrounds
- ✅ Smooth animations
- ✅ Shadow effects
- ✅ Color consistency
- ✅ Responsive design
- ✅ Better button styling
- ✅ Improved input fields
- ✅ Clean typography
- ✅ Professional appearance

---

**All code snippets are ready to copy & paste!** 🚀

