import streamlit as st
import ollama
from datetime import datetime
import json
import re

# Page Configuration
st.set_page_config(
    page_title="Science Formula Bot",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
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
            border-left: 4px solid #2a5298;
        }
        h1 {
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .bot-response {
            background-color: rgba(42, 82, 152, 0.2);
            border-left-color: #2a5298;
        }
        .user-query {
            background-color: rgba(30, 60, 114, 0.2);
            border-left-color: #1e3c72;
        }
        .formula-box {
            background-color: rgba(42, 82, 152, 0.15);
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
st.title("🔬 Science Formula & Concept Bot")
st.markdown("### Explore science with AI-powered formulas and explanations! 🧪✨")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for science preferences
with st.sidebar:
    st.markdown("### 🎯 Science Preferences")

    difficulty_level = st.selectbox(
        "Difficulty Level:",
        ["Elementary (K-5)", "Middle School (6-8)", "High School (9-12)", "College Level", "Advanced Research"]
    )

    science_subject = st.selectbox(
        "Science Subject:",
        [
            "🔋 Physics",
            "⚗️ Chemistry",
            "🧬 Biology",
            "🌍 Earth & Environmental Science",
            "🔭 Astronomy & Space",
            "💡 Quantum Mechanics",
            "🌊 Thermodynamics",
            "⚛️ Atomic & Nuclear Science"
        ]
    )

    learning_style = st.radio(
        "Learning Style:",
        ["Quick Formula", "Formula Explained", "Detailed Theory", "Lab Simulation"]
    )

    show_derivation = st.checkbox("Show formula derivation", value=True)

    show_applications = st.checkbox("Show real-world applications", value=True)

    current_topic = st.text_input(
        "Current Topic (optional):",
        placeholder="e.g., Newton's Laws, Photosynthesis, Chemical Bonding"
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
                    <b>🤖 Science Bot:</b><br>{message["content"]}
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# User Input
col1, col2 = st.columns([4, 1])
with col1:
    user_query = st.text_input(
        "Ask me a science question:",
        placeholder="e.g., 'What is Einstein's E=mc²?' or 'Explain DNA structure' or 'How does photosynthesis work?'",
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
    system_prompt = f"""You are an expert science educator and researcher. Provide clear, accurate scientific explanations with formulas.

CONTEXT:
- Difficulty Level: {difficulty_level}
- Subject: {science_subject}
- Learning Style: {learning_style}
- Topic: {current_topic if current_topic else "General Science"}
- Include Formula Derivation: {show_derivation}
- Include Applications: {show_applications}
- Current Date: {datetime.now().strftime('%B %d, %Y')}

IMPORTANT GUIDELINES:
1. **Accuracy First**: Provide scientifically accurate information with proper units and notation
2. **Formula Presentation**:
   - Write formulas clearly with all variables explained
   - For "{learning_style}" style, adjust detail level accordingly
   - Quick Formula: Just the formula with brief explanation
   - Formula Explained: Formula + what each variable means
   - Detailed Theory: Full derivation, theory, and context
   - Lab Simulation: Experimental approach and expected results
3. **Scientific Notation**: Use proper SI units and scientific notation where appropriate
4. **Variables Explanation**: Define all symbols and variables (e.g., F = force in Newtons, m = mass in kg)
5. **Constants**: Include relevant physical constants (e.g., G = 6.674×10⁻¹¹ N⋅m²/kg²)
6. **Derivation**: If enabled, show mathematical derivation step-by-step
7. **Real-World Applications**: Connect concepts to practical, real-world examples
8. **Common Misconceptions**: Address typical misunderstandings in the topic
9. **Difficulty Scaling**: Adjust mathematical complexity based on "{difficulty_level}"
10. **Lab Notes**: Suggest experimental methods or observations for verification
11. **Related Concepts**: Mention connected topics and formulas that relate
12. **Encouragement**: Be supportive and make science engaging

FORMAT YOUR RESPONSE:
- Use clear section headers
- Show mathematical derivations step-by-step
- Use equation format: F = ma (where F is force in Newtons, m is mass in kg, a is acceleration in m/s²)
- Include diagrams description where helpful (use ASCII art if needed)
- Conclude with key takeaways clearly marked

SUBJECT EXPERTISE:
- **Physics**: Motion, Forces, Energy, Waves, Electricity, Magnetism, Optics, Relativity
- **Chemistry**: Atomic Structure, Chemical Bonds, Reactions, States of Matter, Equilibrium
- **Biology**: Cells, Genetics, Evolution, Ecosystems, Human Body Systems
- **Earth Science**: Geology, Weather, Climate, Plate Tectonics, Oceanography
- **Astronomy**: Celestial Mechanics, Stars, Galaxies, Cosmology
- **Quantum Mechanics**: Uncertainty Principle, Superposition, Wave-Particle Duality
- **Thermodynamics**: Heat, Entropy, Laws of Thermodynamics, Energy Transfer
- **Nuclear Science**: Radioactivity, Fission, Fusion, Atomic Physics"""

    enhanced_query = f"Science Question: {user_query}\n\nSubject: {science_subject}\nDifficulty: {difficulty_level}\nPlease explain this using a {learning_style} approach, including relevant formulas and their applications."

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
st.markdown("### 💡 Example Questions")
col1, col2, col3, col4 = st.columns(4)

quick_queries = [
    "What is E=mc²?",
    "Explain photosynthesis formula",
    "How does gravity work?",
    "What is the pH formula?"
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
    <p>🌟 Made with ❤️ for science enthusiasts & students | Powered by AI</p>
    <p><small>For best results, ensure Ollama is installed and running</small></p>
    <p><small>Perfect for homework help, research, concept clarity, and science exploration</small></p>
</div>
""", unsafe_allow_html=True)

