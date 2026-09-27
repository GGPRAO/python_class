# 🚀 India Trip Planner Chatbot - Quick Reference Card

## 📋 Quick Start (2 Minutes)

### Prerequisites
- Python 3.8+
- Ollama installed
- 4GB+ RAM

### 1️⃣ Install Dependencies
```powershell
pip install -r requirements.txt
```

### 2️⃣ Start Ollama (Keep Running)
```powershell
ollama run qwen2:1.5b
```

### 3️⃣ Start Chatbot
```powershell
streamlit run app.py
```
**Browser opens at: http://localhost:8501**

---

## 🎯 3-Step Usage

### Step 1: Set Preferences (Sidebar)
```
✓ Trip Type (Family/Solo/Couple/Group)
✓ Transportation (Flight/Train/Bus/Car)
✓ Budget Level (Budget-Luxury)
✓ Duration (Days)
✓ Region (North/South/East/West/Northeast)
✓ Number of People
✓ Budget Amount (₹)
✓ Weather Consideration
```

### Step 2: Ask Question
```
Type: "Plan a 5-day family trip to Kerala by car"
Or use quick buttons: 
  • Best places to visit?
  • Hotel recommendations?
  • Travel costs estimate?
  • Weather forecast?
```

### Step 3: Get Response
```
Receive AI-powered recommendations:
• Day-by-day itinerary
• Hotel suggestions with prices
• Transportation options & costs
• Attractions & activities
• Safety tips & local customs
• Practical advice
```

---

## 🚗🚂🚌✈️ Transportation Guides

### 🚗 Road Trip
Ask: "Best road trip from X to Y"
Get: Scenic routes, fuel costs, toll info, stop locations

### 🚂 Train
Ask: "Best trains from X to Y for [type]"
Get: Train options, classes, prices, booking tips

### 🚌 Bus
Ask: "AC buses from X to Y overnight"
Get: Operators, timings, costs, comfort features

### ✈️ Flight
Ask: "Cheapest flights from X to Y"
Get: Airlines, prices, booking windows, connections

---

## 💰 Budget Reference

| Level | Hotel/Night | Food/Day | Transport |
|-------|------------|----------|-----------|
| 🔵 Budget | ₹1-2K | ₹300-500 | ₹200-500 |
| 🟢 Affordable | ₹2-5K | ₹500-1K | ₹500-2K |
| 🟡 Mid-Range | ₹5-10K | ₹1-2K | ₹2-5K |
| 🔴 Premium | ₹10-20K | ₹2-5K | ₹5-10K |
| 💎 Luxury | ₹20K+ | ₹5K+ | ₹10K+ |

---

## 🌍 Regions at a Glance

| Region | Famous For | Best Time |
|--------|-----------|-----------|
| 🏜️ **North** | Taj Mahal, Deserts | Oct-Mar |
| 🏖️ **South** | Beaches, Backwaters | Oct-May |
| 🌄 **East** | Tea Gardens, Wildlife | Sep-Mar |
| 🏛️ **West** | Forts, Beaches | Oct-May |
| 🌲 **Northeast** | Tribal Culture | Sep-Feb |

---

## 📱 Common Queries

**Family Planning**
```
"5-day family trip to Rajasthan by car"
"Kid-friendly activities in South India"
"Budget hotels near Taj Mahal"
```

**Couple Getaway**
```
"Romantic destinations in Kerala"
"Honeymoon packages in Goa"
"Couples' adventure activities"
```

**Solo Travel**
```
"Safe solo destinations for women"
"Budget backpacking routes"
"Solo travelers' community spots"
```

**Group Adventure**
```
"Trekking for 10-person group"
"Group discount travel packages"
"Adventure activities for groups"
```

**Budget Travel**
```
"₹20,000 for 5-day trip"
"Cheapest transportation options"
"Free attractions in major cities"
```

**Luxury Travel**
```
"5-star experiences in Jaipur"
"Premium train journeys"
"Luxury resorts in Kerala"
```

---

## ⚡ Quick Tips

### Get Better Responses
✅ Be specific (dates, people, budget)
✅ Set preferences first
✅ Ask follow-up questions
✅ Mention constraints
✅ Enable weather consideration

### Optimize Performance
✅ Keep Ollama running
✅ Use lighter model if needed
✅ Close unnecessary apps
✅ Ensure stable internet
✅ Allocate 4GB+ RAM

### Troubleshoot Issues
❌ Slow response? → Change model or restart
❌ No response? → Check Ollama running
❌ Irrelevant reply? → Be more specific
❌ Port error? → Use different port

---

## 📂 File Quick Reference

| File | Purpose | Run |
|------|---------|-----|
| app.py | Main app | `streamlit run app.py` |
| app_advanced.py | Enhanced version | `streamlit run app_advanced.py` |
| START_CHATBOT.bat | Windows launcher | Double-click |
| START_CHATBOT.ps1 | PowerShell launcher | `.\START_CHATBOT.ps1` |
| trip_data.json | Data reference | For customization |
| requirements.txt | Dependencies | `pip install -r` |

---

## 📚 Documentation Guide

| Document | Read When |
|----------|-----------|
| README.md | First time setup |
| SETUP_GUIDE.md | Need detailed steps |
| CUSTOMER_GUIDE.md | Want to ask better questions |
| PROJECT_INDEX.md | Need file reference |
| LAUNCH_CHECKLIST.md | Before going live |

---

## 🔧 Customization Quick Start

### Change AI Model
```python
# In app.py, line 126:
model="qwen2:1.5b",  # → Change to "mistral", "neural-chat", etc.
```

### Add New Region
```json
// In trip_data.json:
"Your Region": {
  "popular_destinations": [...],
  "best_months": [...],
  "attractions": [...],
  "avg_temp": "..."
}
```

### Update Sidebar
```python
# In app.py, line 63:
region = st.selectbox("Region:", ["Your New Region", ...])
```

---

## 🌟 Feature Checklist

- ✅ 4 Transportation modes (Car, Train, Bus, Flight)
- ✅ 5 Budget levels (Budget to Luxury)
- ✅ 6 Trip types (Family, Solo, Couple, Group, Adventure, Senior)
- ✅ 6 Regions (N, S, E, W, NE, All India)
- ✅ Weather-aware planning
- ✅ Chat history
- ✅ Budget calculations (per person, per day)
- ✅ Beautiful gradient UI
- ✅ Quick suggestion buttons
- ✅ Multi-turn conversations

---

## 💡 Pro Tips

### For Best Trip Plans
1. Set exact travel dates
2. Mention group composition (2 adults, 1 child)
3. Specify must-see attractions
4. Ask about alternatives
5. Request budget breakdown

### For Group Bookings
1. Mention total group size
2. Note any special needs
3. Ask for group discounts
4. Request bulk booking tips

### For Budget Planning
1. State total budget
2. Clarify what's included
3. Ask for money-saving tips
4. Request free attractions

### For Weather Planning
1. Enable weather consideration
2. Specify travel month/dates
3. Ask for packing suggestions
4. Request seasonal activities

---

## 🎯 Sample Conversation

**User (Sidebar):**
- Trip Type: Family Trip
- Transport: Car + Train
- Budget: Mid-Range
- Days: 7
- Region: North India
- People: 4
- Budget: ₹150,000
- Weather: ✅

**Query 1:**
> "Plan a 7-day family trip from Delhi covering Agra and Jaipur"

**Bot Response:**
> Detailed itinerary with:
> - Day-by-day plan
> - Hotels (Mid-Range prices)
> - Transportation options
> - Kid activities
> - Budget breakdown
> - Safety tips

**Query 2:**
> "Are there train options instead of all car?"

**Bot Response:**
> Revised plan with:
> - Train route suggestions
> - Cost comparison
> - Booking tips
> - Comfort information

---

## 🆘 Emergency Support

### Ollama Won't Start
```powershell
1. Verify installed: ollama --version
2. Restart: ollama serve
3. Try: ollama pull qwen2:1.5b
```

### App Won't Launch
```powershell
1. Check Python: python --version
2. Reinstall: pip install -r requirements.txt
3. Check port: netstat -ano | findstr 8501
```

### No Response from Bot
```
1. Check Ollama running (http://localhost:11434)
2. Wait 30+ seconds (first response slower)
3. Check browser console (F12)
4. Verify internet connection
```

---

## 📞 Helpful Links

- **Ollama**: https://ollama.ai
- **Streamlit**: https://streamlit.io
- **Python**: https://python.org
- **India Tourism**: https://incredibleindia.org
- **Train Booking**: https://www.irctc.co.in
- **Bus Booking**: https://www.redbus.in
- **Flight Booking**: https://www.makemytrip.com

---

## ⏱️ Time Estimates

| Task | Time |
|------|------|
| Install Python packages | 2 min |
| Install Ollama | 10 min |
| Download model | 10-30 min |
| Start chatbot | 1 min |
| Set preferences | 30 sec |
| Generate first plan | 20-30 sec |
| Generate follow-up | 10-20 sec |
| **Total Setup** | **25-45 min** |

---

## 📊 System Requirements

- **OS**: Windows 10/11, Mac, Linux
- **Python**: 3.8+
- **RAM**: 4GB min, 8GB recommended
- **Disk**: 3GB for model + 500MB app
- **Network**: Required for setup only
- **Browser**: Any modern browser

---

## 🎓 Learning Path

1. Read README.md (5 min)
2. Follow SETUP_GUIDE.md (10 min)
3. Run chatbot (5 min)
4. Try basic query (5 min)
5. Read CUSTOMER_GUIDE.md (15 min)
6. Try advanced queries (10 min)
7. Explore all features (15 min)
8. **Total**: ~65 minutes to mastery

---

## 🎊 You're Ready!

Everything is set up. Time to start planning amazing Indian trips!

**Quick Access:**
- Main App: `streamlit run app.py`
- Advanced: `streamlit run app_advanced.py`
- Quick Start: Double-click `START_CHATBOT.bat`

**Browser:** http://localhost:8501

---

**Version:** 1.0 | **Date:** April 26, 2026 | **Status:** Production Ready ✅

*Bookmark this page for quick reference while using the chatbot!*

