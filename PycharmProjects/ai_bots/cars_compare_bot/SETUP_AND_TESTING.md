# 🚗 Cars Compare Bot - Setup & Testing Guide

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Ollama (for AI responses)
- Required Python packages

### Step 1: Install Ollama
1. Download from: https://ollama.ai
2. Install and start Ollama service
3. Pull the required model:
```bash
ollama pull qwen2:1.5b
```

### Step 2: Install Python Packages
Navigate to the project directory and install dependencies:

```bash
cd C:\Users\USER\PycharmProjects\ai_bots\cars_compare_bot
pip install -r requirements.txt
```

**Or manually install:**
```bash
pip install streamlit ollama pandas
```

### Step 3: Verify Installation
Check that everything is installed:
```bash
python -c "import streamlit; import ollama; import pandas; print('✅ All packages installed!')"
```

---

## Running the Application

### Method 1: Using PowerShell Script (Recommended for Windows)
```bash
.\START_CHATBOT.ps1
```

### Method 2: Using Command Prompt Batch File
```bash
START_CHATBOT.bat
```

### Method 3: Manual Launch
```bash
streamlit run app.py
```

The app will open in your browser at: `http://localhost:8501`

---

## Testing the Updates

### Test 1: Verify Indian Rupee Pricing ✅

**Test Question**: "Compare Maruti Swift vs Hyundai Venue"

**Expected Output**:
- Maruti Swift: ₹5,50,000 - ₹6,50,000
- Hyundai Venue: ₹6,50,000 - ₹9,50,000
- Both prices in Indian Rupees

**Pass**: ✅ Prices display with ₹ symbol

---

### Test 2: Verify Features Display ✅

**Test Question**: "What features does Hyundai Creta have?"

**Expected Output**:
- Touchscreen (7-10.25 inch)
- Bluetooth
- USB
- Rear Camera
- Sunroof (top variant)

**Pass**: ✅ Features clearly listed

---

### Test 3: Verify Safety Features ✅

**Test Question**: "Compare safety features of Tata Nexon and Honda City"

**Expected Output**:
- **Tata Nexon**: 
  - 6 Airbags
  - ABS
  - Electronic Stability Program
  - Rear Parking Sensors

- **Honda City**: 
  - 6 Airbags
  - ABS
  - VSC (Vehicle Stability Control)
  - Hill Start Assist
  - Rear Parking Sensors

**Pass**: ✅ Safety features clearly compared

---

### Test 4: Verify Specifications ✅

**Test Question**: "Compare engine and performance specs"

**Expected Output**:
- Engine type and displacement
- Horsepower (hp)
- Torque (Nm)
- 0-100 acceleration time
- Top speed
- Fuel efficiency

**Pass**: ✅ All specs displayed with units

---

### Test 5: Verify Pros & Cons ✅

**Test Question**: "What are pros and cons of Mahindra XUV700?"

**Expected Output**:
- **Pros**: Premium features, 7-seater, powerful engine, advanced tech, excellent performance
- **Cons**: Higher price, expensive maintenance, lower fuel efficiency

**Pass**: ✅ Pros and cons listed clearly

---

### Test 6: Verify Price Range Slider ✅

**Manual Test**:
1. Open sidebar
2. Find "Price Range (₹ Lakhs):" slider
3. Set to 7-15 lakhs
4. Ask: "Show me cars in this price range"

**Expected Output**:
- Hyundai Creta (₹9,50,000 - ₹14,50,000) ✅
- Tata Nexon (₹7,50,000 - ₹11,50,000) ✅
- Kia Seltos (₹9,50,000 - ₹15,50,000) ✅

**Pass**: ✅ Cars filtered by price range

---

### Test 7: Verify Sample Table ✅

**Manual Test**:
1. Open the app
2. Scroll down to "📊 Sample Car Specifications Table"
3. Check if table displays

**Expected Output**:
| Model | Price | Engine | Horsepower | 0-100 | Fuel Eff |
|-------|-------|--------|------------|-------|----------|
| Tesla Model 3 | ₹42,90,000 | Electric Motor | 357 hp | 5.1s | 6.2 km/kWh |
| Mahindra XUV700 | ₹14,50,000 | 2.0L Diesel | 185 hp | 7.8s | 12.5 km/l |

**Pass**: ✅ Table displays with Indian data

---

### Test 8: Verify Quick Suggestions ✅

**Manual Test**:
1. Scroll to "💡 Popular Car Comparisons (Indian Cars)"
2. Look for quick buttons

**Expected Output**:
- "Compare Hyundai Creta vs Tata Nexon"
- "Best compact SUVs under ₹10 lakhs"
- "Tesla Model 3 vs premium sedans in India"
- "Budget-friendly cars with best features"

**Pass**: ✅ All suggestions are Indian car related

---

### Test 9: Test Comparison Query ✅

**Test Question**: "Give me a detailed comparison of Hyundai Creta and Tata Nexon with all specifications and features"

**Expected Output Should Include**:
- 💰 Price Comparison (in ₹)
- 🔧 Specifications & Engine (engine type, hp, torque)
- ⚡ Performance Metrics (0-100, top speed)
- 🛢️ Fuel Efficiency & Range (km/l and km/kWh)
- 🎨 Features & Technology (touchscreen, sunroof, etc.)
- 🛡️ Safety Features (airbags, stability, sensors)
- ✅ Pros & Cons (advantages and disadvantages)
- 🎯 Recommendation (which one is better for whom)

**Pass**: ✅ Complete formatted response with all sections

---

### Test 10: Test Table Format Option ✅

**Manual Test**:
1. Uncheck "Show comparison in table format" in sidebar
2. Ask a comparison question
3. Re-check the option
4. Ask same question again

**Expected Output**:
- Without table: Formatted text response
- With table: Includes markdown tables for comparison

**Pass**: ✅ Both formats work as expected

---

## Troubleshooting

### Issue: "Error: Ollama is not running"
**Solution**:
```bash
# Start Ollama service
# On Windows: Open Ollama application
# Or run: ollama serve
```

### Issue: "Module not found: streamlit"
**Solution**:
```bash
pip install streamlit ollama pandas
```

### Issue: "Model not found: qwen2:1.5b"
**Solution**:
```bash
ollama pull qwen2:1.5b
ollama list  # To verify
```

### Issue: "Port 8501 already in use"
**Solution**:
```bash
streamlit run app.py --server.port 8502
```

### Issue: "Prices showing as USD instead of ₹"
**Solution**:
- Restart the app: `streamlit run app.py`
- Clear cache: Press `C` key in streamlit terminal
- Verify app.py was saved correctly

### Issue: "Features/Safety not showing"
**Solution**:
- Check that qwen2 model pulled successfully
- Update system prompt in code
- Restart Ollama service

---

## Performance Benchmarks

### Expected Response Times
- First query: 5-10 seconds (model initialization)
- Subsequent queries: 3-5 seconds

### Sample Comparison Query Time
```
Time to generate:
Hyundai Creta vs Tata Nexon comparison
Expected: 4-6 seconds
```

---

## Testing Checklist

- [ ] Ollama is installed and running
- [ ] Python packages installed
- [ ] App starts without errors
- [ ] Indian Rupee prices display correctly
- [ ] Features list shows for each car
- [ ] Safety features are compared
- [ ] Sample table displays with ₹ prices
- [ ] Quick suggestion buttons work
- [ ] Price range slider functions
- [ ] Comparison includes all sections
- [ ] Pros and cons are listed
- [ ] Recommendations are provided
- [ ] Chat history displays correctly
- [ ] Multiple queries can be processed

---

## Advanced Testing

### Test Edge Cases

1. **Very specific query**:
   - "Show only electric cars under ₹50 lakhs"
   - Expected: Tesla Model 3 information

2. **Feature comparison**:
   - "Which car has the best infotainment?"
   - Expected: Detailed feature comparison

3. **Budget constraint**:
   - "Best SUV under ₹10 lakhs"
   - Expected: Tata Nexon, Maruti Brezza highlighted

4. **Performance focus**:
   - "Fastest cars in India"
   - Expected: Tesla Model 3, Mahindra XUV700 highlighted

---

## Production Checklist

Before deploying to production:

- [ ] All syntax errors fixed
- [ ] All required packages in requirements.txt
- [ ] Documentation updated
- [ ] Test cases passed
- [ ] Error handling working
- [ ] Database validated
- [ ] UI responsive
- [ ] Performance acceptable
- [ ] Security checked
- [ ] Backup created

---

## Support & Updates

### Getting Help
1. Check the README.md file
2. Review UPDATES.md for recent changes
3. Check INDIAN_FEATURES_GUIDE.md for features
4. Review DATABASE_STRUCTURE.md for data

### Reporting Issues
Include:
- [ ] Error message
- [ ] Query that caused error
- [ ] Screenshot
- [ ] Python version
- [ ] Ollama version
- [ ] Steps to reproduce

---

## Version Information

- **App Version**: 2.0 (Updated with Indian Rupees & Features)
- **Python Version**: 3.8+
- **Streamlit Version**: Latest
- **Ollama Model**: qwen2:1.5b
- **Database**: 11 Indian vehicles
- **Last Updated**: April 26, 2026

---

## Quick Start Commands

```bash
# Navigate to project
cd C:\Users\USER\PycharmProjects\ai_bots\cars_compare_bot

# Install dependencies
pip install -r requirements.txt

# Start Ollama (if not running)
ollama serve

# Pull model (one time)
ollama pull qwen2:1.5b

# Run the app
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 8502
```

---

**Version**: 2.0
**Status**: ✅ Ready for Testing
**Last Updated**: April 26, 2026

