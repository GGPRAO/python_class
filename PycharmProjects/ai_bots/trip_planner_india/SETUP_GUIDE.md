# India Trip Planner Chatbot - Complete Setup Guide

## 📦 Installation & Setup

### Step 1: Install Python Packages

Open PowerShell and run:

```powershell
cd C:\Users\USER\PycharmProjects\ai_bots\trip_planner_india
pip install -r requirements.txt
```

Or install individually:

```powershell
pip install streamlit ollama
```

### Step 2: Install Ollama

1. Download from: https://ollama.ai
2. Run the installer
3. Open PowerShell and verify installation:
   ```powershell
   ollama --version
   ```

### Step 3: Download AI Model

Run one of these commands in PowerShell:

**Recommended (Fast & Accurate):**
```powershell
ollama run qwen2:1.5b
```

**Alternative Models:**
```powershell
ollama run mistral        # Fast, lightweight
ollama run neural-chat    # Optimized for conversation
ollama run llama2         # More capable, slower
```

Wait for the model to download completely (1-3 GB).

### Step 4: Run the Chatbot

In PowerShell, navigate to the project folder and run:

```powershell
streamlit run app.py
```

This will open the chatbot in your default browser at: `http://localhost:8501`

---

## 🎮 Using the Chatbot

### Main Features:

1. **Sidebar Preferences** (Left Panel)
   - Trip Type: Family, Solo, Couple, or Friends
   - Transportation: Select multiple modes (Flight, Train, Bus, Car)
   - Budget Level: From Budget Friendly to Luxury
   - Duration: 1-30 days
   - Region: Choose from 6 regions or All India
   - Weather: Enable weather-aware planning

2. **Chat Interface** (Main Area)
   - Type your trip query
   - Get AI-powered recommendations
   - Chat history stored for reference

3. **Quick Buttons**
   - Pre-defined questions for quick help

---

## 💬 Example Queries

### 1. Family Road Trips
```
"Plan a 5-day family road trip from Mumbai to Goa by car on a budget"
"Best highway routes from Delhi to Shimla for families"
"Where to stop for lunch and snacks on the Pune-Bangalore highway"
```

### 2. Train Journeys
```
"Best trains from Delhi to Kerala for families"
"Luxury train experience in Rajasthan"
"Train fare comparison for 2 adults and 1 child to Varanasi"
```

### 3. Bus Travels
```
"Comfortable AC buses from Bangalore to Coorg"
"Budget bus options from Delhi to Jaipur for groups"
"Sleeper buses with good reviews to Goa"
```

### 4. Flight Plans
```
"Cheapest flights from Mumbai to Goa in April"
"Direct flight options from Delhi to Srinagar"
"Flight + hotel packages for couples to Ladakh"
```

### 5. Budget Planning
```
"₹20,000 budget for 5-day family trip to Kerala"
"Cheapest possible trip to Rajasthan for solo travelers"
"Budget accommodation near monuments in Agra"
```

### 6. Luxury Travel
```
"Luxury 7-day trip to Kerala with premium hotels"
"Best 5-star hotels in Mumbai with beachfront views"
"Private car + luxury hotel package for Jaipur trip"
```

### 7. Weather-Based
```
"Best destinations in India during monsoon season"
"Where to go in summer that's not too hot"
"Cold weather destinations for winter holidays"
```

### 8. Adventure & Activities
```
"Best trekking spots in Himalayas for beginners"
"Water sports activities in South India"
"Wildlife tours in central India for families"
```

---

## 🌟 Tips for Best Experience

### 1. Be Specific
**Instead of:** "Plan my trip"  
**Say:** "Plan a 5-day family trip to Kerala by car in April with a ₹50,000 budget"

### 2. Set Preferences First
Use the sidebar to set your:
- Trip type (the bot will tailor recommendations)
- Budget level (hotels and activities will match)
- Transportation preference (if any)

### 3. Ask Follow-ups
First query: "What are the best destinations for a 5-day trip?"  
Follow-up: "Tell me about accommodation options in that area"  
Next: "How much would transportation cost?"

### 4. Specify Numbers
Always mention:
- Number of people
- Number of days
- Budget range
- Preferred season

### 5. Check Weather First
Enable "Consider Weather Conditions" for:
- Packing lists
- Best travel times
- Seasonal activities

---

## 🗺️ Transportation Guide

### When to Use Each Mode:

#### ✈️ Flight
- Best for: Long distances (1000+ km)
- Duration: 2-5 hours flight time
- Cost: ₹5,000-15,000+ per person
- Comfort: Very high
- **Example Query:** "Flights from Mumbai to Bangalore for weekend trip"

#### 🚂 Train
- Best for: Medium distances (500-2000 km)
- Duration: 8-40 hours depending on distance
- Cost: ₹1,000-10,000 per person
- Comfort: Good (better in higher classes)
- **Example Query:** "AC 2-tier trains from Delhi to Agra for families"

#### 🚌 Bus
- Best for: Short to medium distances (200-1000 km)
- Duration: 6-15 hours
- Cost: ₹500-3,000 per person
- Comfort: Fair to Good
- **Example Query:** "Luxury AC buses from Pune to Mumbai overnight"

#### 🚗 Car/Road Trip
- Best for: Flexibility and scenic routes
- Duration: As per route
- Cost: ₹5-10 per km (fuel + toll)
- Comfort: Excellent
- **Example Query:** "Scenic road trip from Delhi to Jaipur stopping at interesting places"

---

## 💰 Budget Breakdown Example

### 5-Day Trip for 2 People, Budget Friendly:

```
Transportation:
- Train ticket Delhi-Agra: ₹1,200 x 2 = ₹2,400
- Local travel: ₹200 x 5 = ₹1,000
Subtotal: ₹3,400

Accommodation:
- Budget hotel ₹1,500/night x 5 = ₹7,500
Subtotal: ₹7,500

Food:
- Street food & local ₹400/day x 5 = ₹2,000
Subtotal: ₹2,000

Activities:
- Taj Mahal entry: ₹50 x 2 = ₹100
- Local sightseeing: ₹500
Subtotal: ₹600

TOTAL: ₹13,500 (₹6,750 per person)
```

---

## 🔧 Troubleshooting

### Issue: "Connection refused"
**Solution:**
1. Ensure Ollama is installed
2. Open PowerShell and run: `ollama run qwen2:1.5b`
3. Wait for it to load, then refresh your browser

### Issue: Slow responses
**Solution:**
1. Try a lighter model: `ollama run mistral`
2. Close other applications to free up RAM
3. Ensure your internet is stable

### Issue: "ModuleNotFoundError"
**Solution:**
```powershell
pip install streamlit ollama
```

### Issue: Chatbot gives irrelevant responses
**Solution:**
1. Set your preferences in the sidebar first
2. Be more specific in your query
3. Include dates, budget, and number of people

---

## 🎯 Sample Conversation Flow

**User (Sidebar):**
- Trip Type: Family Trip
- Transportation: Car/Road Trip
- Budget: Mid-Range
- Days: 5
- Region: South India
- Weather: Enabled

**User (Chat):**
> "We want to visit Kerala in December for 5 days with our two kids"

**Bot Response:**
Gets family-friendly Kerala recommendations, mid-range hotels, road-trip routes, December weather info, kid activities, etc.

**User Follow-up:**
> "What are the best beaches for children?"

**Bot Response:**
Lists safe, family-friendly beaches with amenities, entry times, facilities, etc.

---

## 🌐 Popular Routes & Times

### North India
- **Delhi to Agra**: 3.5 hours by car, 3 hours by train
- **Delhi to Jaipur**: 4.5 hours by car, 4.5 hours by train
- **Delhi to Shimla**: 7 hours by car (scenic)
- Best time: Oct-Mar

### South India
- **Bangalore to Mysore**: 2 hours by car
- **Chennai to Ooty**: 8 hours by car (scenic hills)
- **Cochin to Munnar**: 4 hours by car (tea plantations)
- Best time: Oct-May

### East India
- **Kolkata to Darjeeling**: 7-8 hours by car (mountain scenery)
- **Guwahati to Shillong**: 3 hours by car
- **Ranchi to Jamshedpur**: 4 hours by car
- Best time: Sep-Mar

### West India
- **Mumbai to Goa**: 10-12 hours by car or bus (coastal route)
- **Ahmedabad to Rajkot**: 5 hours by car
- **Mumbai to Lonavala**: 1.5 hours by car (weekend getaway)
- Best time: Oct-May

---

## 📱 Mobile Compatibility

The chatbot works on mobile browsers but for best experience:
1. Use landscape mode on phones
2. Use tablets for better sidebar visibility
3. Desktop recommended for full features

---

## 🔒 Privacy & Data

- Chat history is stored locally in your browser session
- No data is sent to external servers except to Ollama (local)
- Clear browser cache to delete chat history
- All information stays on your device

---

## 🎓 Learning More

To improve chatbot responses:
1. Be as detailed as possible
2. Ask one question at a time
3. Use the sidebar preferences
4. Specify budget clearly
5. Mention any constraints (time, mobility, etc.)

---

## 🚀 Advanced Usage

### Combining Modes
```
"Plan a trip using flight from Delhi to Bangalore, then car rental for local sightseeing"
```

### Multi-City Tours
```
"Design a 10-day tour: Delhi → Agra → Rajasthan by train and car"
```

### Group Planning
```
"Plan for a group of 8 friends, mix of vegetarians and non-vegetarians, ₹30,000 budget each"
```

### Special Needs
```
"Accessible travel plan for a person with mobility issues"
```

---

## 📞 Getting Help

1. **Check README.md** for feature overview
2. **Read this guide** for setup and usage
3. **Enable Weather** for seasonal recommendations
4. **Set Sidebar Preferences** before asking
5. **Be Specific** in your queries

---

**Happy Traveling! 🌏✈️🎒**

For the best AI responses, keep Ollama running and be as specific as possible with your queries!

