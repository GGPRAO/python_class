⚡ QUICK START GUIDE

## 🚀 Get Running in 5 Minutes

### Step 1: Install Dependencies (1 min)
```bash
pip install -r requirements.txt
```

### Step 2: Start Ollama (Required for AI)
```bash
# Pull the Qwen2 1.5B model (lightweight, fast)
ollama pull qwen2:1.5b

# Start Ollama service
ollama serve
```
Keep this terminal open!

### Step 3: Configure Products (1 min)

Edit `product_config.py` and add products:
```python
PRODUCTS_TO_MONITOR = [
    {"name": "Milk - Amul 1L", "category": "Dairy", "price_threshold": 60},
    {"name": "Bread - Britannia", "category": "Bakery", "price_threshold": 40},
]
```

### Step 4: Run the App (1 min)
```bash
streamlit run app.py
```

### Step 5: Open in Browser
- Automatically opens at `http://localhost:8501`
- Or manually visit that address

---

## ✅ Verify Setup

Run this quick test:

```bash
# Test imports
python -c "import streamlit; import ollama; import pandas; print('✅ All imports OK')"

# Test Ollama
ollama list
```

---

## 📊 Common Tasks

### Monitor New Product
1. Click "➕ Add Product" in sidebar
2. Enter product name and price threshold
3. Click "Save"

### View Price Trends
1. Select product from dropdown
2. See price history chart
3. Read AI insights below

### Set Price Alerts
1. Use slider to set alert threshold (e.g., 10% drop)
2. Products matching criteria will show 🔔
3. View all alerts in "Alerts" tab

### Export Data
1. Click "📊 Export" button
2. Select date range
3. Download as CSV/Excel

---

## 🔔 Notification Settings

Configure alerts:
- **Price Drop %:** Set minimum percentage for alerts
- **Frequency:** How often to check prices (hourly/daily/weekly)
- **Categories:** Select which product categories to monitor
- **Price Range:** Set min/max price thresholds

---

## 📈 Dashboard Overview

| Section | Purpose |
|---------|---------|
| **Overview** | Summary of all products and alerts |
| **Price Trends** | Historical charts and analysis |
| **Alerts** | Active price drop notifications |
| **Insights** | AI-generated recommendations |
| **Reports** | Detailed analytics and comparisons |
| **Settings** | Configuration and preferences |

---

## 📊 Common Tasks

| Task | Steps |
|------|-------|
| Add product | Sidebar → Add Product → Fill details → Save |
| View price history | Select product → View chart → Check trends |
| Enable alerts | Sidebar → Alert settings → Set threshold → Save |
| Compare products | Select 2+ products → Click "Compare" → View analysis |
| Export data | Click "Export" → Select format → Download |
| View insights | Select product → Read "AI Insights" section |

---

## ⚠️ Troubleshoot Issues

| Problem | Solution |
|---------|----------|
| "Connection failed" | Check internet connection |
| "Ollama error" | Run `ollama serve` in background terminal |
| "No products found" | Add products in `product_config.py` |
| "Page not loading" | Visit `http://localhost:8501` manually |
| "Slow performance" | Reduce number of products monitored |
| "Missing price data" | Run initial fetch with "🔄 Fetch All Prices" button |

---

## 🎯 Next Steps

1. ✅ Complete this quick start
2. 📖 Read [NAVIGATION_GUIDE.md](NAVIGATION_GUIDE.md) for architecture
3. 🎨 Check [ARCHITECTURE_DIAGRAMS.md](ARCHITECTURE_DIAGRAMS.md) for visuals
4. ⚙️ Configure AI model in [MODEL_CONFIG_GUIDE.md](MODEL_CONFIG_GUIDE.md)
5. 📚 Reference full docs in [README.md](README.md)

---

## 💡 Pro Tips

✨ **Tip 1:** Use price threshold alerts to get notifications automatically
✨ **Tip 2:** Compare products to find best deals
✨ **Tip 3:** Check trends to identify seasonal price patterns
✨ **Tip 4:** Export data for further analysis
✨ **Tip 5:** Use AI insights for smart shopping decisions

---

**Ready?** Run `streamlit run app.py` and start monitoring! 🎉

