import streamlit as st
import ollama
from datetime import datetime
import json

# Page Configuration
st.set_page_config(
    page_title="India Trip Planner Bot",
    page_icon="🚀",
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
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.title("🌍 India Trip Planner Chatbot")
st.markdown("### Plan your perfect Indian adventure! 🎒✈️")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for trip preferences
with st.sidebar:
    st.markdown("### 🎯 Trip Preferences")

    trip_type = st.selectbox(
        "Trip Type:",
        ["Family Trip", "Solo Travel", "Couple Trip", "Friends Group"]
    )

    transportation = st.multiselect(
        "Transportation Mode:",
        ["✈️ Flight", "🚂 Train", "🚌 Bus", "🚗 Car/Road Trip"],
        default=["🚗 Car/Road Trip"]
    )

    budget_level = st.select_slider(
        "Budget Level:",
        options=["Budget Friendly", "Affordable", "Mid-Range", "Premium", "Luxury"],
        value="Mid-Range"
    )

    num_days = st.slider(
        "Number of Days:",
        min_value=1,
        max_value=30,
        value=5,
        step=1
    )

    region = st.selectbox(
        "Region Interest:",
        ["North India", "South India", "East India", "West India", "Northeast India", "All India"]
    )

    weather_concern = st.checkbox("Consider Weather Conditions", value=True)

# Main chat interface
st.markdown("---")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-query">
                    <b>You:</b> {message["content"]}
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="chat-message bot-response">
                    <b>🤖 Trip Planner Bot:</b><br>{message["content"]}
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# User Input
col1, col2 = st.columns([4, 1])
with col1:
    user_query = st.text_input(
        "Ask me about your trip:",
        placeholder="e.g., 'I want a 5-day family trip to Kerala by car on a budget'",
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
    system_prompt = f"""You are an expert India trip planner chatbot. Provide detailed, personalized trip recommendations.

CONTEXT:
- Trip Type: {trip_type}
- Preferred Transportation: {', '.join(transportation)}
- Budget Level: {budget_level}
- Duration: {num_days} days
- Region: {region}
- Consider Weather: {weather_concern}
- Current Date: {datetime.now().strftime('%B %d, %Y')}

IMPORTANT GUIDELINES:
1. **Road Trip (Car)**: Suggest scenic routes, best highways, fuel stops, toll information, car rental options
2. **Bus Travel**: Recommend luxury bus operators, routes, timings, AC/non-AC options
3. **Train Travel**: Suggest train classes (Sleeper, AC, First Class), bookings, popular routes
4. **Flight Options**: Mention flight routes, airlines, best times to book, airport info
5. **Weather Considerations**: Check season appropriateness (monsoon, summer, winter), packing suggestions
6. **Budget-Friendly**: Include affordable accommodations, street food, free attractions, budget airlines
7. **Luxury/Premium**: Suggest 5-star hotels, fine dining, private tours, premium transportation
8. **Family-Friendly**: Include kid activities, family hotels, safety tips, timings suitable for families
9. **Hotel Options**: Categorize by budget level (Affordable: ₹1000-2000, Mid-Range: ₹2000-5000, Premium: ₹5000-10000, Luxury: ₹10000+)
10. **Places to Visit**: Suggest attractions, best visiting times, entry fees, travel duration between places

Provide a well-structured, actionable plan with specific details, addresses, and costs where possible."""

    enhanced_query = f"User Query: {user_query}\n\nBased on my preferences ({trip_type}, {num_days} days, {budget_level}), provide a detailed trip plan."

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
st.markdown("### 💡 Quick Questions")
col1, col2, col3, col4 = st.columns(4)

quick_queries = [
    "Best places to visit?",
    "Hotel recommendations?",
    "Travel costs estimate?",
    "Weather forecast?"
]

for idx, query in enumerate(quick_queries):
    if idx < 4:
        cols = [col1, col2, col3, col4]
        if cols[idx].button(query):
            st.session_state.chat_history.append({
                "role": "user",
                "content": query
            })
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white;'>
    <p>🌟 Made with ❤️ for Indian travelers | Powered by AI</p>
    <p><small>For best results, ensure Ollama is installed and running</small></p>
</div>
""", unsafe_allow_html=True)
