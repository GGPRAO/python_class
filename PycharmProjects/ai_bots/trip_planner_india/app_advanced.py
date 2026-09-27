import streamlit as st
import ollama
from datetime import datetime
import json
import os

# Page Configuration
st.set_page_config(
    page_title="India Trip Planner Bot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load trip data
@st.cache_resource
def load_trip_data():
    try:
        with open('trip_data.json', 'r') as f:
            return json.load(f)
    except:
        return {}

trip_data = load_trip_data()

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
        .info-box {
            background-color: rgba(102, 126, 234, 0.15);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.title("🌍 India Trip Planner Chatbot")
st.markdown("### Plan your perfect Indian adventure! 🎒✈️🚗🚂🚌✈️")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for trip preferences
with st.sidebar:
    st.markdown("### 🎯 Trip Preferences")

    trip_type = st.selectbox(
        "Trip Type:",
        ["Family Trip", "Solo Travel", "Couple Trip", "Friends Group", "Adventure Group", "Senior Citizens"]
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

    num_people = st.number_input("Number of People:", min_value=1, value=2, step=1)

    budget_amount = st.number_input("Total Budget (₹):", min_value=5000, value=50000, step=5000)

    weather_concern = st.checkbox("Consider Weather Conditions", value=True)

    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    if num_days and num_people and budget_amount:
        per_person = budget_amount / num_people
        per_day = budget_amount / num_days
        st.info(f"₹{per_person:,.0f} per person | ₹{per_day:,.0f} per day")

# Main chat interface
st.markdown("---")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="chat-message user-query">
                    <b>👤 You:</b> {message["content"]}
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
    send_button = st.button("Send ➤", use_container_width=True)

# Process user input
if send_button and user_query:
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_query
    })

    # Build enhanced prompt with context
    region_info = trip_data.get("regions", {}).get(region, {})
    hotel_info = trip_data.get("hotel_categories", {})

    system_prompt = f"""You are an expert India trip planner chatbot with deep knowledge of Indian destinations, transportation, accommodations, and culture.

CUSTOMER CONTEXT:
- Trip Type: {trip_type}
- Preferred Transportation: {', '.join(transportation)}
- Budget Level: {budget_level}
- Trip Duration: {num_days} days
- Number of People: {num_people}
- Total Budget: ₹{budget_amount:,}
- Budget per person: ₹{budget_amount/num_people:,.0f}
- Budget per day: ₹{budget_amount/num_days:,.0f}
- Region: {region}
- Consider Weather: {weather_concern}
- Current Date: {datetime.now().strftime('%B %d, %Y')}
- Region Details: {json.dumps(region_info)}

GUIDELINES FOR TRANSPORTATION-SPECIFIC RESPONSES:

1. **🚗 ROAD TRIP/CAR PLANNING:**
   - Suggest scenic routes, scenic highways, and best routes for {num_days} days
   - Include: fuel costs, toll information, rest stops, nearby attractions
   - Recommend: car rental options, insurance, GPS apps
   - Provide: distance, duration, and driving tips
   - Safety: highlight safe areas, avoid unsafe routes

2. **🚂 TRAIN PLANNING:**
   - Suggest appropriate train classes: Sleeper, AC 3-Tier, AC 2-Tier, First Class
   - Include: Train numbers, departure times, duration, booking tips
   - Budget: show ticket costs for {num_people} people
   - Comfort: compare train services and amenities
   - Booking: suggest booking in advance, IRCTC website, travel apps

3. **🚌 BUS PLANNING:**
   - Recommend luxury and standard bus operators
   - Include: AC/Non-AC options, sleeper configurations, timings
   - Operators: Volvo, Scania, sleeper coaches
   - Cost: per person cost for {num_people} people
   - Comfort: describe amenities like WiFi, meals, USB charging
   - Routes: major bus routes in {region}

4. **✈️ FLIGHT PLANNING:**
   - Suggest airlines (budget and full-service)
   - Include: flight times, connections, prices for {num_people}
   - Best booking windows and season fares
   - Airports and ground transport
   - Luggage allowance and facilities

5. **🌤️ WEATHER CONSIDERATIONS:**
   - Check current month appropriateness
   - Suggest packing: rain gear, warm clothes, sunscreen
   - Seasonal activities suitable for weather
   - Monsoon safety, summer precautions
   - Best time to visit {region}

6. **💰 BUDGET BREAKDOWN:**
   For {budget_level} level with ₹{budget_amount} total:
   - Accommodation: {hotel_info.get(budget_level, {}).get('price_range', 'N/A')} per night
   - Food: Adjust based on budget level
   - Transportation: {num_people} people
   - Activities: Entry fees and tours
   - Buffer: Keep 10-15% emergency fund

7. **👨‍👩‍👧‍👦 FAMILY TRIP SPECIFIC:**
   - Kid-friendly: Include activities suitable for children
   - Safety: Highlight safe areas, medical facilities
   - Timing: Suggest convenient timings for families
   - Accommodation: Family rooms, nearby amenities
   - Food: Include family-friendly restaurants

8. **💎 LUXURY SPECIFIC:**
   - 5-star hotels and resorts
   - Fine dining and exclusive experiences
   - Private tours and personalized services
   - Premium transportation with comfort

9. **💵 BUDGET FRIENDLY SPECIFIC:**
   - Affordable guest houses and hostels
   - Street food and local eateries
   - Free attractions (parks, temples, beaches)
   - Budget airlines and public transport
   - Money-saving tips

RESPONSE FORMAT:
- Start with quick summary
- Provide day-by-day breakdown
- Include costs and budget breakdown
- Add practical tips and warnings
- Suggest alternatives
- Include contact info if relevant

Be conversational, helpful, and provide actionable information."""

    enhanced_query = f"User Query: {user_query}\n\nBased on my preferences (Trip Type: {trip_type}, {num_days} days, {num_people} people, ₹{budget_amount} budget, {budget_level} level), provide a detailed, personalized trip plan."

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
        error_msg = f"❌ Error: {str(e)}\n\n**Solution:** Make sure Ollama is running! Install from https://ollama.ai and run: `ollama run qwen2:1.5b`"
        st.error(error_msg)
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": "I'm having trouble connecting to the AI service. Please ensure Ollama is installed and running."
        })

# Quick suggestion buttons
st.markdown("---")
st.markdown("### 💡 Quick Questions")
col1, col2, col3, col4 = st.columns(4)

quick_queries = {
    col1: "🏨 Hotel recommendations?",
    col2: "💰 Total cost estimate?",
    col3: "🗺️ Best places to visit?",
    col4: "🌤️ Weather & packing?"
}

for col, query in quick_queries.items():
    if col.button(query):
        st.session_state.chat_history.append({
            "role": "user",
            "content": query
        })
        st.rerun()

# Additional Info Section
st.markdown("---")
with st.expander("📚 Trip Information Hub"):
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏨 Hotel Categories")
        for category, details in trip_data.get("hotel_categories", {}).items():
            st.markdown(f"**{category}:** {details.get('price_range', 'N/A')}")

    with col2:
        st.markdown("### 🚗 Transportation Options")
        costs = trip_data.get("transportation_costs", {})
        for mode, details in costs.items():
            if mode != "notes":
                st.markdown(f"**{mode}:** See cost details in chat")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white;'>
    <p>🌟 Made with ❤️ for Indian travelers | Powered by AI</p>
    <p><small>Supports: Car/Road Trips 🚗 | Trains 🚂 | Buses 🚌 | Flights ✈️ | Weather-Aware 🌤️</small></p>
    <p><small>Budget-Friendly to Luxury | Family to Adventure | 1-30 Days</small></p>
    <p><small>For best results, ensure Ollama is installed and running</small></p>
</div>
""", unsafe_allow_html=True)

