import streamlit as st
import ollama
from datetime import datetime
import json
import re

# Page Configuration
st.set_page_config(
    page_title="Maths Problem Solver Bot",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .stTextInput, .stSelectbox, .stNumberInput {
            color: black;
        }
        .chat-message {
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            background-color: rgba(255, 255, 255, 0.1);
            border-left: 4px solid #667eea;
        }
        h1 {
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .bot-response {
            background-color: rgba(102, 126, 234, 0.2);
            border-left-color: #667eea;
        }
        .user-query {
            background-color: rgba(118, 75, 162, 0.2);
            border-left-color: #764ba2;
        }
        .solution-box {
            background-color: rgba(102, 126, 234, 0.15);
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #4CAF50;
            margin: 10px 0;
        }
        .explanation-box {
            background-color: rgba(255, 193, 7, 0.15);
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #FFC107;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.title("🧮 Maths Problem Solver Bot")
st.markdown("### Master mathematics with AI-powered explanations! 📚✨")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for math preferences
with st.sidebar:
    st.markdown("### 🎯 Problem Preferences")

    difficulty_level = st.selectbox(
        "Difficulty Level:",
        ["Elementary (K-5)", "Middle School (6-8)", "High School (9-12)", "College Level", "Advanced"]
    )

    math_category = st.selectbox(
        "Math Category:",
        [
            "🔢 Arithmetic",
            "📐 Geometry",
            "📊 Algebra",
            "📈 Calculus",
            "🎲 Probability & Statistics",
            "🔣 Trigonometry",
            "💯 Word Problems",
            "🧩 Logic & Puzzles"
        ]
    )

    learning_style = st.radio(
        "Learning Style:",
        ["Quick Solution", "Step-by-Step", "Detailed Explanation", "Visual Guide"]
    )

    show_verification = st.checkbox("Verify answer with alternate method", value=True)

    show_practice = st.checkbox("Show practice problems", value=True)

    current_topic = st.text_input(
        "Current Topic (optional):",
        placeholder="e.g., Quadratic Equations, Fractions, Derivatives"
    )

# Main chat interface
st.markdown("---")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-query">
                    <b>📝 You:</b> {message["content"]}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message bot-response">
                    <b>🤖 Maths Solver Bot:</b><br>{message["content"]}
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# User Input
col1, col2 = st.columns([4, 1])
with col1:
    user_query = st.text_input(
        "Ask me a math problem:",
        placeholder="e.g., 'Solve 2x² + 5x - 3 = 0' or 'What is 15% of 480?'",
        key="user_input"
    )

with col2:
    send_button = st.button("Send", use_container_width=True)

# Process user input
if send_button and user_query:
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_query
    })

    # Build enhanced prompt with context
    system_prompt = f"""You are an expert math tutor and problem solver. Provide clear, detailed solutions with explanations.

CONTEXT:
- Difficulty Level: {difficulty_level}
- Category: {math_category}
- Learning Style: {learning_style}
- Topic: {current_topic if current_topic else "General Mathematics"}
- Include Verification: {show_verification}
- Include Practice Problems: {show_practice}
- Current Date: {datetime.now().strftime('%B %d, %Y')}

IMPORTANT GUIDELINES:
1. **Problem Analysis**: Identify the problem type and key concepts needed
2. **Solution Format**: 
   - For "{learning_style}" style, adjust detail level accordingly
   - Quick Solution: Brief answer with key steps
   - Step-by-Step: Numbered steps showing the process
   - Detailed Explanation: Include theory, formulas, and reasoning
   - Visual Guide: Use ASCII art or describe visual representations
3. **Clarity**: Use clear mathematical notation, show all calculations
4. **Verification**: If enabled, verify the answer using an alternate method
5. **Common Mistakes**: Highlight typical errors students make
6. **Formulas & Concepts**: Explain relevant formulas and why they work
7. **Real-World Application**: Connect to practical applications when relevant
8. **Practice Problems**: If enabled, provide 2-3 similar problems for practice
9. **Difficulty Scaling**: Adjust complexity based on "{difficulty_level}"
10. **Encourage Learning**: Be supportive and encourage understanding over memorization

FORMAT YOUR RESPONSE:
- Use clear section headers
- Show mathematical work step-by-step
- Use equations in simple text format (e.g., x = (-b ± √(b²-4ac)) / 2a)
- Conclude with the final answer clearly marked"""

    enhanced_query = f"Problem: {user_query}\n\nCategory: {math_category}\nDifficulty: {difficulty_level}\nPlease solve this problem with a {learning_style} approach."

    try:
        # Get response from Ollama
        response = ollama.chat(
            model="qwen2:1.5b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": enhanced_query}
            ],
            stream=False
        )

        bot_response = response["message"]["content"]

        # Add bot response to history
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": bot_response
        })

        # Rerun to display new messages
        st.rerun()

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}\n\n**Solution:** Make sure Ollama is running! Install it from https://ollama.ai and run: `ollama run qwen2:1.5b`"
        st.error(error_msg)
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "I'm having trouble connecting to the AI service. Please ensure Ollama is installed and running."
        })

# Quick suggestion buttons
st.markdown("---")
st.markdown("### 💡 Example Problems")
col1, col2, col3, col4 = st.columns(4)

quick_queries = [
    "Solve: 3x + 7 = 22",
    "What is the area of a circle with radius 5?",
    "Calculate: 25% of 200",
    "Solve: x² - 5x + 6 = 0"
]

for idx, query in enumerate(quick_queries):
    if idx < 4:
        cols = [col1, col2, col3, col4]
        if cols[idx].button(query, key=f"quick_{idx}"):
            st.session_state.chat_history.append({
                "role": "user",
                "content": query
            })
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white;'>
    <p>🌟 Made with ❤️ for students & learners | Powered by AI</p>
    <p><small>For best results, ensure Ollama is installed and running</small></p>
    <p><small>Perfect for homework help, exam prep, and concept clarity</small></p>
</div>
""", unsafe_allow_html=True)

