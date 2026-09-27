# 🗺️ NAVIGATION GUIDE - Project Architecture & Structure

## Project Navigation Map (POM)

```
BIGBASKET PRICE MONITOR AGENT
│
├─ ENTRY POINT: app.py
│  │  ├─ Streamlit web interface
│  │  ├─ User authentication
│  │  ├─ Dashboard orchestration
│  │  └─ Event handling
│  │
│  ├─ LAYER 1: product_config.py
│  │  ├─ Product database configuration
│  │  ├─ BigBasket data fetching
│  │  ├─ Product list management
│  │  └─ API integration
│  │
│  ├─ LAYER 2: clean_products.py
│  │  ├─ Data validation
│  │  ├─ Data standardization
│  │  ├─ Field cleaning
│  │  └─ Error handling
│  │
│  ├─ LAYER 3: price_tracker.py
│  │  ├─ Historical price tracking
│  │  ├─ Price change detection
│  │  ├─ Alert management
│  │  └─ Trend calculation
│  │
│  ├─ LAYER 4: analyze_prices.py
│  │  ├─ AI-powered analysis
│  │  ├─ Price insights generation
│  │  ├─ Trend prediction
│  │  └─ Recommendation engine
│  │
│  └─ LAYER 5: convert_into_agent.py
│     ├─ Agent conversion
│     ├─ Autonomy features
│     ├─ Scheduled tasks
│     └─ Auto-notifications
│
└─ DATA STORAGE
   ├─ products.csv
   ├─ price_history.csv
   └─ alerts.csv
```

---

## Data Flow Diagram

```
START
  │
  ├─→ User Input (Product list, alerts, thresholds)
  │
  ├─→ product_config.py
  │   ├─ Connect to BigBasket
  │   ├─ Fetch product data
  │   └─ Store in memory
  │
  ├─→ clean_products.py
  │   ├─ Validate fields
  │   ├─ Standardize data
  │   └─ Handle errors
  │
  ├─→ price_tracker.py
  │   ├─ Compare with history
  │   ├─ Calculate changes
  │   └─ Detect alerts
  │
  ├─→ analyze_prices.py
  │   ├─ Generate insights
  │   ├─ Predict trends
  │   └─ Create recommendations
  │
  ├─→ convert_into_agent.py
  │   ├─ Autonomously schedule
  │   ├─ Send notifications
  │   └─ Generate reports
  │
  ├─→ app.py (Streamlit)
  │   ├─ Display results
  │   ├─ Show charts
  │   └─ User interaction
  │
  └─→ END
```

---

## Function Call Hierarchy

### Level 1: Main Entry Point
```
app.py
├─ main()
├─ render_sidebar()
├─ render_overview()
├─ render_trends()
├─ render_alerts()
└─ render_settings()
```

### Level 2: Data Fetch Layer
```
product_config.py
├─ fetch_product_data()
│  ├─ connect_to_bigbasket()
│  ├─ search_products()
│  └─ extract_product_info()
│
├─ get_product_by_id()
├─ save_product_data()
└─ load_product_data()
```

### Level 3: Data Clean Layer
```
clean_products.py
├─ validate_product_data()
│  ├─ check_required_fields()
│  ├─ validate_price_format()
│  └─ validate_categories()
│
├─ clean_product_fields()
│  ├─ normalize_strings()
│  ├─ standardize_prices()
│  └─ format_dates()
│
└─ extract_product_features()
   └─ parse_attributes()
```

### Level 4: Tracking Layer
```
price_tracker.py
├─ track_price_change()
│  ├─ get_previous_price()
│  ├─ calculate_difference()
│  ├─ calculate_percentage()
│  └─ save_to_history()
│
├─ get_price_history()
│  ├─ query_database()
│  └─ return_time_series()
│
└─ check_price_alerts()
   ├─ compare_with_threshold()
   ├─ detect_price_drop()
   └─ trigger_notification()
```

### Level 5: Analysis Layer
```
analyze_prices.py
├─ analyze_price_trends()
│  ├─ calculate_moving_average()
│  ├─ detect_patterns()
│  └─ forecast_future_price()
│
├─ generate_insights()
│  ├─ call_ollama_api()
│  ├─ process_ai_response()
│  └─ format_insights()
│
└─ calculate_savings()
   ├─ find_lowest_price()
   └─ estimate_monthly_savings()
```

### Level 6: Agent Layer
```
convert_into_agent.py
├─ enable_autonomous_mode()
├─ schedule_price_checks()
├─ send_auto_notifications()
├─ generate_periodic_reports()
└─ manage_agent_state()
```

---

## Module Specifications

### 1. app.py - Streamlit Main Application
**Purpose:** Web interface and orchestration
**Dependencies:** streamlit, pandas, plotly
**Key Functions:**
- `main()` - Application entry point
- `render_sidebar()` - Sidebar controls
- `render_overview()` - Dashboard overview
- `render_trends()` - Price trend charts

**Data Flow:** 
- Input: User interactions
- Output: Web page updates

---

### 2. product_config.py - Product Management
**Purpose:** Fetch and manage product data
**Dependencies:** requests, beautifulsoup4, pandas
**Key Functions:**
- `fetch_product_data()` - Get products from BigBasket
- `get_product_by_id(product_id)` - Retrieve specific product
- `save_product_data(products)` - Persist data

**Data Flow:**
- Input: Product names, categories
- Output: Product objects with details

---

### 3. clean_products.py - Data Validation
**Purpose:** Validate and clean product data
**Dependencies:** pandas, regex
**Key Functions:**
- `validate_product_data(data)` - Check data integrity
- `clean_product_fields(products)` - Standardize format
- `extract_product_features(data)` - Parse attributes

**Data Flow:**
- Input: Raw product data
- Output: Cleaned, validated data

---

### 4. price_tracker.py - Price History
**Purpose:** Track and monitor price changes
**Dependencies:** pandas, datetime
**Key Functions:**
- `track_price_change(product_id, new_price)` - Record price update
- `get_price_history(product_id)` - Retrieve history
- `check_price_alerts(products)` - Detect drops

**Data Flow:**
- Input: Current prices
- Output: Historical data, alerts

---

### 5. analyze_prices.py - AI Analysis
**Purpose:** Generate insights and recommendations
**Dependencies:** ollama, pandas, numpy
**Key Functions:**
- `analyze_price_trends(history)` - Statistical analysis
- `generate_insights(products)` - AI-powered insights
- `calculate_savings(original, current)` - Savings estimation

**Data Flow:**
- Input: Price history
- Output: Insights, predictions

---

### 6. convert_into_agent.py - Agent Features
**Purpose:** Autonomous agent capabilities
**Dependencies:** scheduling, threading
**Key Functions:**
- `enable_autonomous_mode()` - Start agent
- `schedule_price_checks()` - Set schedule
- `send_auto_notifications()` - Auto alerts

**Data Flow:**
- Input: Configuration
- Output: Autonomous actions

---

## Usage Scenarios

### Scenario 1: Monitor Single Product
```
User → app.py (Add product)
      → product_config.py (Fetch details)
      → clean_products.py (Validate)
      → price_tracker.py (Initialize)
      → app.py (Display in dashboard)
```

### Scenario 2: Set Price Alert
```
User → app.py (Set threshold)
      → price_tracker.py (Store alert)
      → price_tracker.py (Continuous check)
      → analyze_prices.py (If alert triggered)
      → app.py (Display notification)
```

### Scenario 3: View AI Insights
```
User → app.py (Request insights)
      → price_tracker.py (Get history)
      → analyze_prices.py (Generate insights)
      → analyze_prices.py (Call Ollama)
      → app.py (Display results)
```

### Scenario 4: Compare Products
```
User → app.py (Select products)
      → price_tracker.py (Get current prices)
      → analyze_prices.py (Calculate differences)
      → analyze_prices.py (Generate comparison)
      → app.py (Display comparison chart)
```

---

## Integration Points

### Internal Integrations
- **app.py ↔ all modules** - Command dispatcher
- **price_tracker.py ↔ analyze_prices.py** - Data sharing
- **clean_products.py → price_tracker.py** - Validated data
- **convert_into_agent.py ↔ all modules** - Autonomous execution

### External Integrations
- **BigBasket API/Website** - Product data source
- **Ollama** - AI model for insights
- **Local filesystem** - Data storage
- **Email service** - Notifications (optional)

---

## Testing Points

### Unit Testing
- Test each module independently
- Mock external API calls
- Validate data transformations

### Integration Testing
- Test module interactions
- End-to-end data flow
- Error handling

### System Testing
- Full application flow
- Performance under load
- Data persistence

---

## Performance Considerations

### Optimization Tips
1. **Cache product data** - Reduce API calls
2. **Batch price updates** - Multiple products at once
3. **Use lightweight models** - Faster AI processing
4. **Implement pagination** - Handle large datasets
5. **Compress data** - Reduce storage

### Bottlenecks
- API response time (1-2 sec per product)
- AI model inference (2-5 sec per analysis)
- Data I/O operations
- Streamlit refresh cycle

---

## Learning Path

### Step 1: Understand Data Flow
- Read this guide
- Study data flow diagram
- Map input → output

### Step 2: Explore Modules
- Start with app.py
- Follow function calls
- Understand each layer

### Step 3: Study Integration
- How modules communicate
- Data passing between layers
- Error propagation

### Step 4: Implement Features
- Modify single module
- Test changes
- Integrate with other modules

---

## Debug Checklist

When troubleshooting:

- [ ] Check data at each layer
- [ ] Verify API connectivity
- [ ] Validate data formats
- [ ] Check Ollama availability
- [ ] Review error messages
- [ ] Test module isolation
- [ ] Check data flow
- [ ] Verify file permissions
- [ ] Monitor memory usage
- [ ] Check network connectivity

---

## Common Issues & Solutions

| Issue | Layer | Cause | Solution |
|-------|-------|-------|----------|
| No products fetch | Layer 1 | API error | Check BigBasket connection |
| Invalid data format | Layer 2 | Parsing error | Review clean_products.py |
| Price not tracking | Layer 3 | DB error | Check file permissions |
| AI insights fail | Layer 4 | Ollama down | Start `ollama serve` |
| Agent inactive | Layer 5 | Scheduling issue | Check convert_into_agent.py |

---

**Last Updated:** April 2026
**Version:** 1.0.0

