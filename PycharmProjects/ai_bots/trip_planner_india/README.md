# 🌍 India Trip Planner Chatbot

A beautiful, AI-powered chatbot application for planning perfect trips across India. Get personalized recommendations for transportation, hotels, attractions, and budgets based on your preferences.

## ✨ Features

### 🚀 Transportation Planning
- **✈️ Flight Planning**: Flight routes, airlines, best booking times, airport information
- **🚂 Train Travel**: Train classes (Sleeper, AC, First Class), booking guides, popular routes
- **🚌 Bus Services**: Luxury bus operators, AC/non-AC options, routes, and timings
- **🚗 Road Trips**: Scenic routes, highway information, fuel stops, car rental options

### 💰 Budget-Friendly Options
- **Budget Friendly** (₹1000-2000/night): Hostels, budget hotels, street food
- **Affordable** (₹2000-5000/night): 3-star hotels, local restaurants
- **Mid-Range** (₹5000-10000/night): 4-star hotels, good dining options
- **Premium** (₹10000+/night): 5-star hotels, fine dining
- **Luxury**: Ultimate premium experience with all amenities

### 👨‍👩‍👧‍👦 Trip Types
- **Family Trips**: Kid-friendly activities, family hotels, safety tips
- **Solo Travel**: Budget options, safe neighborhoods, social activities
- **Couple Trips**: Romantic destinations, special experiences
- **Friends Group**: Adventure activities, budget-friendly group accommodations

### 🌤️ Weather-Aware Planning
- Seasonal recommendations (monsoon, summer, winter)
- Packing suggestions based on weather
- Best times to visit specific regions
- Weather-appropriate activity suggestions

### 🗺️ Regional Coverage
- **North India**: Delhi, Rajasthan, Himalayas, Agra
- **South India**: Kerala, Tamil Nadu, Karnataka, Telangana
- **East India**: Bengal, Odisha, Jharkhand
- **West India**: Gujarat, Goa, Maharashtra, Rajasthan
- **Northeast India**: Assam, Meghalaya, Manipur
- **All India**: National wide tours

## 📋 Quick Start

### Prerequisites
- Python 3.8+
- Ollama (for AI responses)
- Internet connection

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd ai_bots/trip_planner_india
```

2. **Install required Python packages:**
```bash
pip install streamlit ollama
```

3. **Install and run Ollama:**
   - Download from: https://ollama.ai
   - Install and run: `ollama run qwen2:1.5b`
   
   (Or use another model like `mistral`, `llama2`, etc.)

### Running the Chatbot

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 🎯 How to Use

### 1. **Set Your Preferences** (Sidebar)
   - Select trip type (Family, Solo, Couple, Group)
   - Choose transportation modes
   - Set budget level
   - Select number of days
   - Choose region of interest
   - Enable/disable weather considerations

### 2. **Ask Questions**
   - Type your query in the input box
   - Examples:
     - "Plan a 5-day family trip to Kerala by car on a budget"
     - "What are the best trains from Mumbai to Goa?"
     - "Recommend luxury hotels in Jaipur"
     - "Flight options from Delhi to Bangalore?"
     - "Best places for a 3-day road trip from Pune"

### 3. **Get Personalized Recommendations**
   - Detailed itineraries with day-by-day breakdown
   - Hotel recommendations with prices
   - Transportation options with costs
   - Attractions and visiting times
   - Food recommendations
   - Safety tips and local customs

### 4. **Use Quick Buttons**
   - "Best places to visit?"
   - "Hotel recommendations?"
   - "Travel costs estimate?"
   - "Weather forecast?"

## 📱 Example Queries

```
"5-day family trip to Rajasthan by car, budget friendly"
"Best trains from Delhi to Kerala for luxury travel"
"Budget bus routes from Mumbai to Goa for solo travelers"
"Flight deals to Bangalore for a 3-day trip"
"10-day northeast India adventure trip"
"Weekend getaway near Delhi by car for families"
"Best monsoon destinations in South India"
"Luxury Kerala backwater cruise experience"
```

## 🏗️ Architecture

```
app.py
├── UI Configuration (Streamlit)
├── Custom Styling (CSS)
├── Sidebar Preferences
├── Chat Interface
├── AI Integration (Ollama)
└── Session State Management
```

## 📊 Hotel Price Guide

| Category | Price Range (per night) | Features |
|----------|------------------------|----------|
| Budget Friendly | ₹1000-2000 | Basic amenities, shared bathrooms |
| Affordable | ₹2000-5000 | Private rooms, decent facilities |
| Mid-Range | ₹5000-10000 | Good service, good locations |
| Premium | ₹10000-20000 | 5-star quality, excellent service |
| Luxury | ₹20000+ | Ultra-luxury, world-class |

## 🚆 Transportation Comparison

| Mode | Best For | Avg Cost | Time | Comfort |
|------|----------|----------|------|---------|
| Flight | Long distances | High | Fast | Very Good |
| Train | Medium distances | Medium | Medium | Good |
| Bus | Short-medium | Low | Slow | Fair |
| Car | Flexibility | Medium | Flexible | Excellent |

## 🌤️ Seasonal Guide

| Season | Best Regions | Weather | Packing |
|--------|-------------|---------|---------|
| Winter (Oct-Mar) | North, East | Cool & Dry | Sweaters, Jackets |
| Summer (Apr-Jun) | Hills, Northeast | Hot | Light clothes, Sunscreen |
| Monsoon (Jul-Sep) | West Coast | Rainy | Rain gear, Waterproofs |
| Spring (Feb-Mar) | All India | Pleasant | Light layers |

## 🔧 Troubleshooting

### "No module named 'streamlit'"
```bash
pip install streamlit
```

### "No module named 'ollama'"
```bash
pip install ollama
```

### "Connection refused" error
- Ensure Ollama is installed from https://ollama.ai
- Run: `ollama run qwen2:1.5b`
- Check if Ollama service is running

### Slow responses
- Use a lighter model: `ollama run mistral` or `ollama run neural-chat`
- Ensure sufficient system RAM (4GB+ recommended)

## 🎨 Customization

### Changing the AI Model
Edit line 126 in `app.py`:
```python
model="qwen2:1.5b",  # Change to: "mistral", "llama2", "neural-chat", etc.
```

### Adding More Regions
Update the region list in sidebar (line 63):
```python
region = st.selectbox(
    "Region Interest:",
    ["North India", "Your New Region", ...]
)
```

## 🤝 Contributing

Feel free to enhance the chatbot with:
- More regions and attractions
- Additional transportation modes
- Better hotel databases
- Real-time weather integration
- Booking integrations

## 📝 License

This project is open source and available for personal and commercial use.

## 💡 Tips for Best Results

1. **Be Specific**: Include dates, number of people, and specific interests
2. **Mention Budget**: Help the bot tailor recommendations
3. **Ask Follow-ups**: Refine suggestions with additional questions
4. **Check Weather**: Enable weather consideration for seasonal accuracy
5. **Verify Details**: Cross-check recommendations with official sources

## 🌐 Popular Destinations by Season

### Winter (Best Time): Oct-Mar
- Rajasthan, Jaipur, Agra, Delhi
- Goa beaches
- Kerala backwaters
- Himalayas trekking

### Summer: Apr-Jun
- Himachal Pradesh mountains
- Kashmir valleys
- Northeast India
- Nilgiri Hills

### Monsoon: Jul-Sep
- Western Ghats
- Coastal roads (car trips)
- Waterfall season
- Tea plantations (Darjeeling)

### Spring: Feb-Mar
- Entire North India
- Desert festivals (Rajasthan)
- Flower season in Himalayas

## 📞 Support

For issues or suggestions, please check:
1. Ollama is properly installed and running
2. All Python packages are installed
3. Your internet connection is stable
4. Your system meets minimum requirements

---

**Enjoy planning your perfect Indian adventure! 🎉✈️🌏**

*Last Updated: April 2026*

