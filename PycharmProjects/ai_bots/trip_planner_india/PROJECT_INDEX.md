# 🌍 India Trip Planner Chatbot - Project Files Overview

## 📁 Project Structure

```
trip_planner_india/
├── app.py                    # Main Streamlit chatbot application
├── app_advanced.py           # Advanced version with JSON data integration
├── trip_data.json            # Database of hotels, routes, costs, attractions
├── requirements.txt          # Python dependencies
├── START_CHATBOT.bat         # Quick start batch file (Windows)
│
├── 📚 Documentation:
│   ├── README.md             # Main project overview
│   ├── SETUP_GUIDE.md        # Complete setup and installation guide
│   ├── CUSTOMER_GUIDE.md     # How to use chatbot effectively
│   └── PROJECT_INDEX.md      # This file
```

---

## 🚀 Quick Start (5 Minutes)

### Option 1: Using Batch File (Easiest for Windows)
1. Double-click `START_CHATBOT.bat`
2. Wait for browser to open
3. Set preferences in sidebar
4. Start chatting!

### Option 2: Using PowerShell (Advanced)
```powershell
# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running
ollama run qwen2:1.5b

# Start chatbot
streamlit run app.py
```

---

## 📄 File Details

### 1. **app.py** (Main Application)
- **Purpose**: Core Streamlit chatbot
- **Features**:
  - Beautiful gradient UI
  - Chat history management
  - Sidebar preferences (trip type, transport, budget, etc.)
  - Quick suggestion buttons
  - AI-powered responses via Ollama
- **Run**: `streamlit run app.py`
- **Best for**: Basic usage, standard trip planning

### 2. **app_advanced.py** (Enhanced Version)
- **Purpose**: Advanced version with JSON database integration
- **Additional Features**:
  - Uses trip_data.json for enhanced context
  - Budget per person calculations
  - Expandable information hub
  - More detailed hotel and transport info
  - Better response contextualization
- **Run**: `streamlit run app_advanced.py`
- **Best for**: More detailed planning, reference information

### 3. **trip_data.json** (Data Repository)
- **Purpose**: Database of Indian trip information
- **Contains**:
  ```json
  {
    "regions": {...},           // 5 regions with attractions, best months
    "hotel_categories": {...},  // Hotel types with price ranges
    "transportation_costs": {...}, // Cost estimates for each mode
    "seasonal_guide": {...},    // Seasonal information
    "popular_routes": {...},    // Road, train, and flight routes
    "family_friendly_activities": {...}, // Activities by region
    "budget_travel_tips": [...]  // Money-saving tips
  }
  ```
- **Usage**: Referenced by app_advanced.py for better context

### 4. **requirements.txt** (Dependencies)
- **Purpose**: Lists Python packages needed
- **Packages**:
  - `streamlit==1.28.1` - Web UI framework
  - `ollama==0.0.12` - AI model interface
  - `python-dateutil==2.8.2` - Date utilities
- **Installation**: `pip install -r requirements.txt`

### 5. **START_CHATBOT.bat** (Windows Launcher)
- **Purpose**: One-click startup script
- **Does**:
  1. Checks Python installation
  2. Verifies Ollama is running
  3. Installs dependencies
  4. Launches Streamlit app
  5. Opens browser at localhost:8501
- **Usage**: Double-click the file

---

## 📖 Documentation Files

### 1. **README.md** (Project Overview)
**What's Inside:**
- Feature list with emojis
- Installation instructions
- How to use the chatbot
- Architecture overview
- Hotel price guide
- Transportation comparison
- Seasonal guide
- Troubleshooting section
- Customization options
- Popular destinations

**Who Should Read:**
- First-time users
- Project overview seekers
- Feature reference

### 2. **SETUP_GUIDE.md** (Installation & Usage)
**What's Inside:**
- Step-by-step installation
- Ollama setup
- Complete usage examples
- 💰 Budget breakdown example
- 🚆 Transportation guide
- 🌐 Popular routes & times
- Mobile compatibility notes
- Privacy information
- Advanced usage examples
- Troubleshooting solutions

**Who Should Read:**
- Users installing the app
- First-time setup
- Windows PowerShell users
- Troubleshooting needed

### 3. **CUSTOMER_GUIDE.md** (User Interaction Guide)
**What's Inside:**
- Setting preferences (detailed)
- How to ask effective questions
- Transportation-specific queries
- Destination-specific queries
- Budget-related queries
- Weather & seasonal queries
- Family trip specifics
- Accommodation queries
- Activity queries
- Pro tips for best results
- Common question templates
- Example complete interaction
- Special requests explanation

**Who Should Read:**
- End users (travelers)
- Anyone using the chatbot
- Customers planning trips
- Reference for asking better questions

---

## 🎯 Which File to Use?

### **Use app.py if:**
- You want the simplest, fastest setup
- You're new to the chatbot
- You want basic trip planning
- You prefer lightweight performance
- You're on limited system resources

### **Use app_advanced.py if:**
- You want enhanced, more detailed responses
- You're accessing information hub
- You want budget calculations
- You prefer context-aware recommendations
- You have sufficient system resources

### **Reference trip_data.json if:**
- You want to modify data (add hotels, routes, etc.)
- You need raw data for analysis
- You want to enhance the chatbot
- You're developing custom features

---

## 🔧 Configuration & Customization

### Changing the AI Model
Edit line 126 in `app.py`:
```python
model="qwen2:1.5b",  # Change to: "mistral", "neural-chat", "llama2"
```

Available models (download first with `ollama pull`):
- `qwen2:1.5b` - Small, fast (recommended)
- `mistral` - Slightly larger, better quality
- `neural-chat` - Optimized for conversations
- `llama2` - Larger, more capable but slower

### Adding New Regions
1. Edit `trip_data.json`
2. Add new region under "regions" key
3. Include attractions, best months, avg_temp
4. Update sidebar in `app.py` (line 63)

### Modifying Hotel Categories
Edit `trip_data.json` → `hotel_categories`

---

## 🌟 Features Explained

### Transportation Support
- ✈️ **Flights**: Airlines, prices, booking tips
- 🚂 **Trains**: Classes, routes, comfort levels
- 🚌 **Buses**: Operators, AC/non-AC options
- 🚗 **Car**: Scenic routes, fuel costs, toll info

### Budget Levels
1. **Budget Friendly** (₹1000-2000/night)
2. **Affordable** (₹2000-5000/night)
3. **Mid-Range** (₹5000-10000/night)
4. **Premium** (₹10000-20000/night)
5. **Luxury** (₹20000+/night)

### Trip Types
- 👨‍👩‍👧‍👦 Family Trip
- 🚶 Solo Travel
- 👫 Couple Trip
- 👯 Friends Group
- 🏃 Adventure Group
- 👴👵 Senior Citizens

### Regions Covered
- 🏜️ North India (Taj Mahal, Rajasthan, Himalayas)
- 🏖️ South India (Kerala, Beaches, Temples)
- 🌄 East India (Tea gardens, Wildlife)
- ⛱️ West India (Goa, Forts, Deserts)
- 🌲 Northeast India (Tribal culture, Wildlife)
- 🗺️ All India

---

## 📊 Technology Stack

**Frontend:**
- Streamlit (Web UI framework)
- HTML/CSS (Styling)

**Backend:**
- Python 3.8+
- Ollama (Local AI)
- JSON (Data storage)

**Architecture:**
- Streamlit session state (chat history)
- Ollama API (AI responses)
- Local JSON (Data reference)

---

## 🎓 Learning Resources

### For Using the Chatbot:
1. Read CUSTOMER_GUIDE.md
2. Review example queries
3. Start with simple questions
4. Try transportation-specific queries
5. Explore regional guides

### For Development:
1. Understand Streamlit basics
2. Review Ollama API
3. Study trip_data.json structure
4. Examine app.py code comments
5. Explore customization options

---

## 🚀 How to Use - Quick Steps

### Step 1: Install
```powershell
pip install -r requirements.txt
```

### Step 2: Setup Ollama
```powershell
ollama run qwen2:1.5b
```

### Step 3: Run Chatbot
```powershell
streamlit run app.py
# Or use: app_advanced.py
```

### Step 4: Set Preferences
1. Trip Type
2. Transportation modes
3. Budget level
4. Number of days
5. Region
6. Number of people
7. Budget amount
8. Weather consideration

### Step 5: Ask Questions
- "Plan a 5-day family trip to Kerala by car"
- "Best trains from Delhi to Agra"
- "Budget hotels in Jaipur"
- Use quick buttons for common questions

---

## 💡 Pro Tips

### For Best Results:
1. ✅ Set sidebar preferences first
2. ✅ Be specific (dates, budget, people)
3. ✅ Ask follow-up questions
4. ✅ Mention any constraints
5. ✅ Use weather consideration
6. ✅ Compare options (ask for alternatives)

### Performance Tips:
1. Keep Ollama running in background
2. Use lighter model (qwen2:1.5b) for speed
3. Close unnecessary applications
4. Ensure 4GB+ RAM available
5. Stable internet connection

---

## 🆘 Troubleshooting

### Issue: "Connection refused"
```
Solution:
1. Ensure Ollama is installed (https://ollama.ai)
2. Run: ollama run qwen2:1.5b
3. Check if running: http://localhost:11434
```

### Issue: "ModuleNotFoundError"
```
Solution: pip install -r requirements.txt
```

### Issue: Slow responses
```
Solution:
1. Try lighter model: ollama run mistral
2. Close other applications
3. Check system RAM
```

### Issue: Irrelevant responses
```
Solution:
1. Set sidebar preferences first
2. Be more specific in query
3. Include dates, budget, people
4. Ask clearer follow-up questions
```

---

## 📞 Support Resources

- **Ollama Issues**: https://github.com/jmorganca/ollama
- **Streamlit Docs**: https://docs.streamlit.io
- **Python Help**: https://docs.python.org
- **India Travel**: https://www.incredibleindia.org

---

## 🎉 You're Ready!

You now have a complete, AI-powered India trip planning chatbot with:
- ✅ Beautiful web interface
- ✅ Multiple transportation modes
- ✅ Regional coverage across India
- ✅ Budget level customization
- ✅ Weather-aware planning
- ✅ AI-powered recommendations
- ✅ Chat history management
- ✅ Complete documentation

### Next Steps:
1. Install requirements
2. Run `ollama run qwen2:1.5b`
3. Execute `streamlit run app.py`
4. Set your preferences
5. Start planning your perfect Indian adventure! 🌏✈️

---

**Last Updated:** April 26, 2026
**Version:** 1.0
**Status:** Production Ready ✅

🌟 **Happy Trip Planning!** 🌟

