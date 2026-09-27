# 🛒 BigBasket Price Monitor Agent

An AI-powered Streamlit application that monitors product prices from BigBasket, tracks price changes, and provides intelligent notifications using Ollama LLM.

## 🎯 Project Overview

This application automates the process of:
- 🛍️ Fetching product data from BigBasket
- 💰 Tracking price changes and trends
- 🧹 Cleaning and validating product information
- 🤖 Generating insights using AI (Ollama LLM)
- 📊 Displaying analytics in an interactive web interface
- 🔔 Smart notifications for price drops

---

## 📁 Project Structure

```
bigbasket_price_monitor/
│
├── app.py                       # Main Streamlit web application
├── product_config.py            # BigBasket product configuration & data fetching
├── clean_products.py            # Data cleaning & validation
├── analyze_prices.py            # Price analysis & insights generation
├── price_tracker.py             # Price history & trend tracking
├── convert_into_agent.py        # Agent conversion utilities
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── data/
    ├── products.csv             # Product database
    └── price_history.csv        # Historical price data
```

---

## 🔧 Setup Instructions

### Prerequisites
- **Python:** 3.8 or higher
- **Ollama:** Latest version (for LLM functionality)
- **Internet Connection:** For BigBasket API/Web scraping

### Step 1: Create Virtual Environment

```bash
# Windows PowerShell
python -m venv venv
venv\Scripts\Activate.ps1

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure BigBasket Products

Edit `product_config.py` and add products to monitor:

```python
PRODUCTS_TO_MONITOR = [
    {"name": "Product Name", "category": "Category", "price_threshold": 500},
    # Add more products...
]
```

### Step 4: Start Ollama

```bash
# Pull a lightweight model
ollama pull qwen2:1.5b

# Start Ollama service
ollama serve
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will automatically open at `http://localhost:8501`

---

## 🚀 Features

### 📊 Price Monitoring
- Real-time price tracking
- Historical price trends
- Price change notifications
- Comparative analysis

### 🤖 AI-Powered Insights
- Smart price recommendations
- Trend analysis
- Savings predictions
- Market insights

### 📈 Analytics Dashboard
- Price charts and graphs
- Product comparison
- Savings summary
- Alert management

### 🔔 Notifications
- Price drop alerts
- Out of stock warnings
- Restock notifications
- Custom thresholds

---

## 🔑 API Reference

### `product_config.py`
```python
fetch_product_data()          # Fetch latest product data from BigBasket
get_product_by_id(product_id) # Get specific product information
save_product_data(products)   # Save product data locally
```

### `clean_products.py`
```python
validate_product_data(data)   # Validate product information
clean_product_fields(products) # Standardize data format
extract_product_features(data) # Extract key features
```

### `analyze_prices.py`
```python
analyze_price_trends(history)  # Analyze historical prices
generate_insights(products)    # Generate AI insights
calculate_savings(original, current) # Calculate potential savings
```

### `price_tracker.py`
```python
track_price_change(product_id, new_price) # Track price updates
get_price_history(product_id)  # Retrieve historical prices
check_price_alerts(products)   # Check for price drop alerts
```

---

## ⚙️ Configuration Options

### Model Selection
Modify `analyze_prices.py` to change LLM model:

```python
MODEL = "qwen2:1.5b"      # Lightweight (recommended)
MODEL = "llama3"          # Powerful
MODEL = "mistral"         # Fast & accurate
```

### Alert Thresholds
Set price drop percentage in app sidebar:
- Default: 10% decrease
- Min: 5%, Max: 50%

### Update Frequency
Modify update interval in `product_config.py`:
- Default: 6 hours
- Minimum: 1 hour
- Maximum: 24 hours

---

## 🧪 Testing

### Run Tests
```bash
python -m pytest tests/
```

### Manual Testing Checklist
- [ ] Products load correctly
- [ ] Prices update without errors
- [ ] AI insights generate properly
- [ ] Alerts trigger on price drops
- [ ] Dashboard displays correctly

---

## 🐛 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| "Connection failed" | Check internet connection and BigBasket availability |
| "Ollama error" | Ensure `ollama serve` is running in background |
| "No products found" | Verify product configuration is correct |
| "Page not loading" | Check `http://localhost:8501` manually |
| "Memory issues" | Reduce number of products being tracked |

### Debug Mode

Enable debug logging in app:
```bash
streamlit run app.py --logger.level=debug
```

---

## 🔐 Security & Privacy

### Best Practices
- Store credentials in `.env` file (not in code)
- Use secure API tokens if available
- Limit data retention to 90 days
- Don't store sensitive user information

### Data Protection
- All data processed locally
- No data sent to third parties
- Price history stored locally
- API calls encrypted (HTTPS)

---

## 📦 Dependencies

See `requirements.txt` for complete list:

- **streamlit** - Web UI framework
- **pandas** - Data manipulation
- **ollama** - LLM integration
- **requests** - HTTP requests
- **beautifulsoup4** - Web scraping (if needed)
- **plotly** - Interactive charts
- **python-dotenv** - Environment variables

---

## 🚀 Performance Optimization

### Tips for Better Performance
1. Reduce number of products monitored
2. Increase update frequency intervals
3. Use lighter model (qwen2:1.5b)
4. Cache price data locally
5. Implement pagination for large datasets

### Performance Metrics
- Fetch time: ~2-3 seconds per 100 products
- Analysis time: ~1-2 seconds per product
- Memory usage: ~200-300 MB typical
- Update cycle: 6 hours default

---

## 📞 Support & Contributing

### Issues
Found a bug? Please report it with:
- Steps to reproduce
- Error message
- Python version
- OS information

### Contributing
Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Test thoroughly
4. Submit pull request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 FAQ

**Q: Can I monitor multiple platforms?**
A: Currently BigBasket only. Can be extended to other platforms.

**Q: How accurate are price predictions?**
A: Based on historical data. More data = better predictions.

**Q: Can I export data?**
A: Yes, export to CSV/Excel through the dashboard.

**Q: Is there a mobile app?**
A: Not yet. Web interface is responsive and mobile-friendly.

---

**Last Updated:** April 2026
**Version:** 1.0.0

