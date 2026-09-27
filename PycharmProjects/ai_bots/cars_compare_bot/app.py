import streamlit as st
import ollama
from datetime import datetime
import json
import pandas as pd
import re

# Page Configuration
st.set_page_config(
    page_title="Cars Compare Bot",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI
st.markdown("""
    <style>
        .main {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
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
            border-left: 4px solid #ff6b6b;
        }
        h1 {
            text-align: center;
            color: white;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .bot-response {
            background-color: rgba(255, 107, 107, 0.2);
            border-left-color: #ff6b6b;
        }
        .user-query {
            background-color: rgba(238, 90, 111, 0.2);
            border-left-color: #ee5a6f;
        }
        .comparison-box {
            background-color: rgba(255, 107, 107, 0.15);
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #4CAF50;
            margin: 10px 0;
        }
        .specs-box {
            background-color: rgba(255, 193, 7, 0.15);
            padding: 15px;
            border-radius: 8px;
            border-left: 5px solid #FFC107;
            margin: 10px 0;
        }
        .table-container {
            overflow-x: auto;
            margin: 15px 0;
            background-color: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.title("🚗 Cars Compare Bot")
st.markdown("### Find your perfect car match! Compare specs, features & models 🏎️⚡")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sample car database for context - Indian Cars with Indian Rupees
cars_database = {
    "Maruti Swift": {
        "brand": "Maruti Suzuki",
        "type": "Compact Hatchback",
        "price": "₹5,50,000 - ₹6,50,000",
        "engine": "1.2L Petrol",
        "horsepower": "83 hp",
        "torque": "113 Nm",
        "0-100": "10.2s",
        "top_speed": "175 km/h",
        "fuel_efficiency": "19.1 km/l",
        "range": "700 km",
        "transmission": "Manual/Automatic (AMT)",
        "seats": "5",
        "cargo": "268L",
        "features": "Touchscreen, Power Steering, ABS, Dual Airbags, Infotainment System",
        "safety": "ABS, Dual Airbags, Rear Parking Sensors, Seatbelt Reminder",
        "pros": "Fuel efficient, affordable, reliable, good resale value",
        "cons": "Small cargo space, basic features, loud engine"
    },
    "Hyundai Creta": {
        "brand": "Hyundai",
        "type": "Compact SUV",
        "price": "₹9,50,000 - ₹14,50,000",
        "engine": "1.5L Petrol/Diesel",
        "horsepower": "113-113 hp",
        "torque": "144-250 Nm",
        "0-100": "10.5s",
        "top_speed": "190 km/h",
        "fuel_efficiency": "16.5-18.5 km/l",
        "range": "900 km",
        "transmission": "Manual/Automatic",
        "seats": "5",
        "cargo": "480L",
        "features": "Touchscreen (7-10.25 inch), Bluetooth, USB, Rear Camera, Sunroof (top variant)",
        "safety": "ABS, 6 Airbags, ESC, Hill Assist, Rear Parking Sensors",
        "pros": "Great styling, good ground clearance, features-rich, powerful diesel engine",
        "cons": "Higher price, average fuel economy on petrol, maintenance costs"
    },
    "Tata Nexon": {
        "brand": "Tata Motors",
        "type": "Compact SUV",
        "price": "₹7,50,000 - ₹11,50,000",
        "engine": "1.2L Petrol/1.5L Diesel",
        "horsepower": "110-110 hp",
        "torque": "170-260 Nm",
        "0-100": "10.4s",
        "top_speed": "185 km/h",
        "fuel_efficiency": "16.8-20.5 km/l",
        "range": "850 km",
        "transmission": "Manual/Automatic",
        "seats": "5",
        "cargo": "425L",
        "features": "Touchscreen, Bluetooth Connectivity, Rear Camera, Climate Control",
        "safety": "ABS, 6 Airbags, Electronic Stability Program, Rear Parking Sensors",
        "pros": "Affordable, good safety features, spacious interior, great ground clearance",
        "cons": "Interior quality, basic infotainment in lower variants"
    },
    "Honda City": {
        "brand": "Honda",
        "type": "Compact Sedan",
        "price": "₹11,50,000 - ₹14,50,000",
        "engine": "1.5L Petrol",
        "horsepower": "121 hp",
        "torque": "145 Nm",
        "0-100": "9.6s",
        "top_speed": "200 km/h",
        "fuel_efficiency": "16.5-17.7 km/l",
        "range": "850 km",
        "transmission": "Manual/Automatic (CVT)",
        "seats": "5",
        "cargo": "506L",
        "features": "Touchscreen, Apple CarPlay/Android Auto, Sunroof (top variant), Cruise Control",
        "safety": "ABS, 6 Airbags, VSC, Hill Start Assist, Rear Parking Sensors",
        "pros": "Excellent reliability, good build quality, spacious, comfortable ride",
        "cons": "No diesel option, higher price point, average acceleration"
    },
    "Mahindra XUV700": {
        "brand": "Mahindra",
        "type": "Premium 7-Seater SUV",
        "price": "₹14,50,000 - ₹20,50,000",
        "engine": "2.0L Turbo Petrol/2.0L Diesel",
        "horsepower": "185-185 hp",
        "torque": "380-450 Nm",
        "0-100": "7.8s",
        "top_speed": "210 km/h",
        "fuel_efficiency": "12.5-15.2 km/l",
        "range": "800 km",
        "transmission": "Automatic (6-speed)",
        "seats": "7",
        "cargo": "635L",
        "features": "Panoramic Sunroof, ADAS, 360-Degree Camera, Touchscreen (10.25 inch), Connected Car Tech",
        "safety": "8 Airbags, ABS, ESC, 6-Point Seatbelts, Autonomous Emergency Braking",
        "pros": "Premium features, 7-seater, powerful engine, advanced tech, excellent performance",
        "cons": "Higher price, expensive maintenance, lower fuel efficiency"
    },
    "Kia Seltos": {
        "brand": "Kia",
        "type": "Compact SUV",
        "price": "₹9,50,000 - ₹15,50,000",
        "engine": "1.5L Petrol/Diesel",
        "horsepower": "115-115 hp",
        "torque": "144-250 Nm",
        "0-100": "10.8s",
        "top_speed": "188 km/h",
        "fuel_efficiency": "16.8-19.2 km/l",
        "range": "900 km",
        "transmission": "Manual/Automatic",
        "seats": "5",
        "cargo": "433L",
        "features": "10.25-inch Touchscreen, Wireless Charging, Panoramic Sunroof, ADAS",
        "safety": "6 Airbags, ABS, ESC, Hill Assist, Rear Camera with Parking Sensors",
        "pros": "Good warranty, latest tech, stylish design, value-for-money",
        "cons": "New brand in India, higher maintenance costs, average performance"
    },
    "Skoda Kushaq": {
        "brand": "Skoda",
        "type": "Compact SUV",
        "price": "₹10,50,000 - ₹17,50,000",
        "engine": "1.0L TSI Petrol/1.5L TSI Petrol",
        "horsepower": "113-150 hp",
        "torque": "200-250 Nm",
        "0-100": "10.2s",
        "top_speed": "195 km/h",
        "fuel_efficiency": "15.5-18.2 km/l",
        "range": "850 km",
        "transmission": "Manual/Automatic (6-speed)",
        "seats": "5",
        "cargo": "405L",
        "features": "8-inch Touchscreen, Bluetooth, Rear Camera, Cruise Control",
        "safety": "6 Airbags, ABS, ESC, Rear Parking Sensors, Seatbelt Reminder",
        "pros": "European engineering, good performance, reliable, fun to drive",
        "cons": "Limited service centers, higher parts cost, average fuel efficiency"
    },
    "Renault Duster": {
        "brand": "Renault",
        "type": "Compact SUV",
        "price": "₹8,50,000 - ₹12,50,000",
        "engine": "1.5L Petrol/Diesel",
        "horsepower": "106-110 hp",
        "torque": "142-200 Nm",
        "0-100": "10.9s",
        "top_speed": "180 km/h",
        "fuel_efficiency": "16.5-18.8 km/l",
        "range": "900 km",
        "transmission": "Manual/Automatic",
        "seats": "5",
        "cargo": "475L",
        "features": "Touchscreen, Bluetooth, Rear Camera, Power Steering, Air Conditioning",
        "safety": "ABS, Dual Airbags, Rear Parking Sensors, Speed Alert System",
        "pros": "Very affordable, good space, reliable diesel engine, easy maintenance",
        "cons": "Basic features, older design, lower build quality"
    },
    "Maruti Brezza": {
        "brand": "Maruti Suzuki",
        "type": "Compact SUV",
        "price": "₹8,00,000 - ₹11,50,000",
        "engine": "1.5L Petrol/Diesel",
        "horsepower": "102-112 hp",
        "torque": "138-200 Nm",
        "0-100": "11.5s",
        "top_speed": "185 km/h",
        "fuel_efficiency": "17.5-22.9 km/l",
        "range": "850 km",
        "transmission": "Manual/Automatic (CVT)",
        "seats": "5",
        "cargo": "405L",
        "features": "Touchscreen (7-inch), Bluetooth, Rear Camera, Power Windows",
        "safety": "ABS, Dual Airbags, Rear Parking Sensors, Seatbelt Reminder",
        "pros": "Fuel efficient, affordable, good warranty, reliable brand",
        "cons": "Small interior, average performance, basic features"
    },
    "Tesla Model 3 (India)": {
        "brand": "Tesla",
        "type": "Electric Sedan",
        "price": "₹42,90,000 - ₹52,90,000",
        "engine": "Electric Motor (AC Induction)",
        "horsepower": "357 hp",
        "torque": "404 Nm",
        "0-100": "5.1s",
        "top_speed": "225 km/h",
        "fuel_efficiency": "6.2 km/kWh",
        "range": "568 km (fully charged)",
        "transmission": "Single-Speed Automatic",
        "seats": "5",
        "cargo": "425L",
        "features": "15-inch Touchscreen, Autopilot, OTA Updates, Glass Roof, Premium Sound System",
        "safety": "8 Airbags, ABS, ESC, Collision Avoidance, Side Impact Protection",
        "pros": "Zero emissions, excellent acceleration, advanced tech, low running costs",
        "cons": "Very expensive, limited charging infrastructure, high maintenance cost"
    },
    "Hyundai Venue": {
        "brand": "Hyundai",
        "type": "Sub-Compact SUV",
        "price": "₹6,50,000 - ₹9,50,000",
        "engine": "1.2L Petrol/1.0L Diesel",
        "horsepower": "82-70 hp",
        "torque": "115-160 Nm",
        "0-100": "11.2s",
        "top_speed": "175 km/h",
        "fuel_efficiency": "18.4-21.8 km/l",
        "range": "800 km",
        "transmission": "Manual/Automatic (iMT/DCT)",
        "seats": "5",
        "cargo": "311L",
        "features": "Touchscreen (7-inch), Bluetooth, Rear Camera, Connected Car Services",
        "safety": "ABS, 6 Airbags, ESP, Rear Parking Sensors, Speed Alert",
        "pros": "Very affordable, good looks, fuel efficient, great warranty",
        "cons": "Limited interior space, basic features, average performance"
    }
}

# Sidebar for comparison preferences
with st.sidebar:
    st.markdown("### 🎯 Comparison Preferences")

    comparison_type = st.selectbox(
        "What would you like to compare?",
        [
            "🚗 Compare Multiple Cars",
            "💰 Price Comparison",
            "⚡ Performance Specs",
            "🛢️ Fuel Efficiency",
            "🎨 Models & Variants",
            "🏅 Brand Comparison",
            "📋 Full Specifications"
        ]
    )

    vehicle_category = st.selectbox(
        "Vehicle Category:",
        [
            "🚗 Sedan",
            "🏎️ Sports Car",
            "🚙 SUV/Crossover",
            "🔋 Electric Vehicle",
            "🏡 Family Car",
            "💼 Luxury Car",
            "🌱 Eco-Friendly"
        ]
    )

    price_range = st.slider(
        "Price Range (₹ Lakhs):",
        min_value=5,
        max_value=50,
        value=(7, 20),
        step=1
    )

    top_priorities = st.multiselect(
        "Top Priorities:",
        [
            "💰 Affordability",
            "⚡ Performance",
            "🛢️ Fuel Economy",
            "🛡️ Safety",
            "🎨 Design",
            "🔋 Electric Range",
            "🪑 Comfort",
            "📱 Tech Features"
        ],
        default=["⚡ Performance", "🛢️ Fuel Economy"]
    )

    show_table_format = st.checkbox("Show comparison in table format", value=True)

    show_recommendations = st.checkbox("Show personalized recommendations", value=True)

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
                    <b>🤖 Cars Compare Bot:</b><br>{message["content"]}
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# User Input
col1, col2 = st.columns([4, 1])
with col1:
    user_query = st.text_input(
        "Ask me about cars:",
        placeholder="e.g., 'Compare Tesla Model 3 vs BMW 3 Series' or 'Best electric cars under $50k?'",
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
    system_prompt = f"""You are an expert automotive consultant and car comparison specialist with extensive knowledge of Indian automobiles. Provide detailed, accurate information about cars with prices in Indian Rupees.

CONTEXT:
- Comparison Type: {comparison_type}
- Vehicle Category: {vehicle_category}
- Price Range: ₹{price_range[0]} lakhs - ₹{price_range[1]} lakhs (₹{price_range[0] * 100000:,} - ₹{price_range[1] * 100000:,})
- Top Priorities: {', '.join(top_priorities) if top_priorities else 'General comparison'}
- Show Table Format: {show_table_format}
- Include Recommendations: {show_recommendations}
- Current Date: {datetime.now().strftime('%B %d, %Y')}
- Currency: All prices in Indian Rupees (₹)

AVAILABLE CAR DATA:
{json.dumps(cars_database, indent=2)}

IMPORTANT GUIDELINES:
1. **Accuracy**: Provide real, accurate car specifications and pricing in Indian Rupees
2. **Specifications**: Always include engine type, horsepower, torque, transmission, seats, cargo space
3. **Features Display**: 
   - List all available features clearly (entertainment, connectivity, comfort)
   - Highlight premium features vs standard features
   - Show infotainment system details
4. **Safety Features**: 
   - Display number of airbags, ABS, stability control
   - Mention advanced safety systems like ADAS, collision avoidance
   - Compare safety ratings when available
5. **Comparison Format**: 
   - If table format enabled, create clear markdown tables with key specs
   - Include Price (in ₹), Engine, Horsepower, Torque, Acceleration (0-100), Top Speed
   - Include Fuel Efficiency, Range, Transmission, Seats, Cargo, Features, Safety
6. **Organization**: Structure information clearly with headers and sections
   - ## 💰 Price Comparison
   - ## 🔧 Specifications & Engine
   - ## ⚡ Performance Metrics
   - ## 🛢️ Fuel Efficiency & Range
   - ## 🎨 Features & Technology
   - ## 🛡️ Safety Features
   - ## ✅ Pros & Cons
7. **Price Analysis**: Compare value-for-money and cost-effectiveness in Indian market
8. **Performance Metrics**: Show 0-100 times, top speed, torque clearly
9. **Fuel Efficiency**: Compare fuel consumption (km/l) and range for long trips
10. **Features**: Highlight unique features, tech, infotainment, and creature comforts
11. **Pros & Cons**: List 3-4 advantages and disadvantages for each car
12. **Recommendations**: Based on priorities, recommend the best choice with reasoning
13. **Practical Advice**: Consider Indian ownership costs, maintenance, service availability, warranty
14. **Visual Presentation**: Use clean formatting with bullet points, emoji icons, and tables

FORMAT YOUR RESPONSE:
- Use markdown tables for spec comparisons
- Create clear section headers with emojis
- Show winner/best choice for each metric with ✨ indicator
- Provide a summary recommendation at the end
- For electric vehicles, emphasize range, charging time, and cost savings
- For performance cars, highlight acceleration and power delivery
- Always mention warranty and after-sales service availability
- Include approximate maintenance costs (annual)"""

    enhanced_query = f"User Query: {user_query}\n\nCategory: {vehicle_category}\nComparison Type: {comparison_type}\nPrice Range: ₹{price_range[0]} lakhs - ₹{price_range[1]} lakhs\n\nPlease provide a detailed comparison with specifications, features, safety ratings, and pros/cons in a clear, easy-to-read format."

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
st.markdown("### 💡 Popular Car Comparisons (Indian Cars)")
col1, col2, col3, col4 = st.columns(4)

quick_queries = [
    "Compare Hyundai Creta vs Tata Nexon",
    "Best compact SUVs under ₹10 lakhs",
    "Tesla Model 3 vs premium sedans in India",
    "Budget-friendly cars with best features"
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

# Sample comparison table
if show_table_format:
    st.markdown("---")
    st.markdown("### 📊 Sample Car Specifications Table (Indian Rupees)")

    # Create a sample comparison dataframe
    sample_data = {
        "Model": ["Tesla Model 3", "Mahindra XUV700", "Honda City", "Hyundai Creta", "Maruti Swift"],
        "Type": ["Electric", "Premium SUV", "Sedan", "Compact SUV", "Hatchback"],
        "Price (₹)": ["₹42,90,000", "₹14,50,000", "₹11,50,000", "₹9,50,000", "₹5,50,000"],
        "Engine": ["Electric Motor", "2.0L Diesel", "1.5L Petrol", "1.5L Diesel", "1.2L Petrol"],
        "Horsepower": ["357 hp", "185 hp", "121 hp", "113 hp", "83 hp"],
        "0-100 (s)": ["5.1s", "7.8s", "9.6s", "10.5s", "10.2s"],
        "Fuel Efficiency": ["6.2 km/kWh", "12.5 km/l", "16.5 km/l", "18.5 km/l", "19.1 km/l"],
        "Range": ["568 km", "800 km", "850 km", "900 km", "700 km"],
        "Seats/Cargo": ["5/425L", "7/635L", "5/506L", "5/480L", "5/268L"]
    }
    
    df = pd.DataFrame(sample_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white;'>
    <p>🌟 Made with ❤️ for car enthusiasts | Powered by AI</p>
    <p><small>For best results, ensure Ollama is installed and running</small></p>
    <p><small>Get unbiased comparisons, specifications, and expert recommendations</small></p>
</div>
""", unsafe_allow_html=True)

