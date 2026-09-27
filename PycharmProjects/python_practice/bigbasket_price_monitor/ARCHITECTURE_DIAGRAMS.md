# 🎨 ARCHITECTURE DIAGRAMS & VISUAL GUIDES

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     BIGBASKET PRICE MONITOR                      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      PRESENTATION LAYER                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Streamlit Web Interface (app.py)                        │   │
│  │  - Dashboard / Analytics / Alerts / Settings            │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Product      │  │ Price        │  │ Analysis     │           │
│  │ Config       │  │ Tracker      │  │ Engine       │           │
│  │ (Layer 1)    │  │ (Layer 3)    │  │ (Layer 4)    │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
│          ↓                 ↓                 ↓                    │
│  ┌──────────────────────────────────────────────────┐            │
│  │ Data Processing Layer (Layer 2)                  │            │
│  │ - Validation / Cleaning / Transformation        │            │
│  └──────────────────────────────────────────────────┘            │
│          ↓                 ↓                 ↓                    │
│  ┌──────────────────────────────────────────────────┐            │
│  │ Agent Layer (Layer 5)                            │            │
│  │ - Autonomous Scheduling / Notifications         │            │
│  └──────────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   DATA PERSISTENCE LAYER                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ Products DB  │  │ Price History│  │ Alerts Log   │           │
│  │ (products.  │  │ (price_      │  │ (alerts.csv) │           │
│  │ csv)         │  │ history.csv) │  │              │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   EXTERNAL SERVICES                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │
│  │ BigBasket    │  │ Ollama AI    │  │ Notifications│           │
│  │ (Products)   │  │ (Insights)   │  │ (Email/SMS)  │           │
│  └──────────────┘  └──────────────┘  └──────────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Request-Response Cycle

```
CLIENT REQUEST
    │
    ├─→ User opens dashboard
    ├─→ Loads sidebar options
    ├─→ Selects product or action
    │
    ↓
STREAMLIT (app.py)
    ├─→ Parse user input
    ├─→ Route to appropriate function
    ├─→ Prepare parameters
    │
    ↓
MODULE LAYER
    ├─→ product_config.py (if fetching)
    ├─→ clean_products.py (if validating)
    ├─→ price_tracker.py (if tracking)
    ├─→ analyze_prices.py (if analyzing)
    │
    ↓
DATA PROCESSING
    ├─→ Validate data
    ├─→ Clean and normalize
    ├─→ Transform to needed format
    │
    ↓
PERSISTENCE
    ├─→ Save to CSV/Database
    ├─→ Update cache
    ├─→ Log changes
    │
    ↓
RESPONSE GENERATION
    ├─→ Format data for display
    ├─→ Create visualizations
    ├─→ Prepare UI elements
    │
    ↓
STREAMLIT RENDER
    ├─→ Update dashboard
    ├─→ Refresh charts
    ├─→ Show notifications
    │
    ↓
CLIENT DISPLAY
    └─→ User sees results
```

---

## Price Processing Pipeline

```
FETCH STAGE
    │
    ├─→ Connect to BigBasket
    ├─→ Search for products
    ├─→ Extract product details
    ├─→ Parse prices and availability
    │
    ↓
VALIDATION STAGE
    │
    ├─→ Check required fields
    ├─→ Validate price format
    ├─→ Verify product data
    ├─→ Error handling & logging
    │
    ↓
CLEANING STAGE
    │
    ├─→ Normalize product names
    ├─→ Standardize prices
    ├─→ Format dates
    ├─→ Remove duplicates
    │
    ↓
TRACKING STAGE
    │
    ├─→ Get previous price
    ├─→ Calculate change
    ├─→ Store in history
    ├─→ Check alerts
    │
    ↓
ANALYSIS STAGE
    │
    ├─→ Calculate trends
    ├─→ Generate insights
    ├─→ Call AI (Ollama)
    ├─→ Create recommendations
    │
    ↓
NOTIFICATION STAGE
    │
    ├─→ Check alert criteria
    ├─→ Format messages
    ├─→ Send notifications
    ├─→ Log activity
    │
    ↓
DISPLAY STAGE
    │
    └─→ Update dashboard
    └─→ Show in UI
```

---

## Component Dependencies

```
app.py (Main Entry)
    │
    ├─→ product_config.py
    │   ├─ Requires: requests, beautifulsoup4
    │   └─ Provides: Product data
    │
    ├─→ clean_products.py
    │   ├─ Requires: pandas, regex
    │   └─ Provides: Validated data
    │
    ├─→ price_tracker.py
    │   ├─ Requires: pandas, datetime, CSV files
    │   └─ Provides: Price history, alerts
    │
    ├─→ analyze_prices.py
    │   ├─ Requires: ollama, numpy, pandas
    │   └─ Provides: Insights, predictions
    │
    └─→ convert_into_agent.py
        ├─ Requires: schedule, threading
        └─ Provides: Autonomous features

EXTERNAL DEPENDENCIES
    │
    ├─→ streamlit (Web framework)
    ├─→ ollama (AI model)
    ├─→ requests (HTTP calls)
    ├─→ pandas (Data handling)
    ├─→ plotly (Visualizations)
    └─→ beautifulsoup4 (Web scraping)
```

---

## Data Persistence Flow

```
IN-MEMORY STATE
    │
    ├─→ Pandas DataFrames
    ├─→ Session variables
    └─→ Cache dictionaries
    │
    ↓
FILE STORAGE
    │
    ├─→ products.csv
    │   ├─ Product ID, Name, Category, Price
    │   └─ Stock Status, Availability
    │
    ├─→ price_history.csv
    │   ├─ Product ID, Date, Price
    │   ├─ Change %, Trend
    │   └─ Alert Status
    │
    └─→ alerts.csv
        ├─ Alert ID, Product ID, Threshold
        ├─ Status, Date Created
        └─ Notifications Sent

RETRIEVAL FLOW
    │
    ├─→ Read from disk
    ├─→ Load into memory
    ├─→ Process as needed
    └─→ Cache for performance
```

---

## Error Handling Tree

```
ERRORS
    │
    ├─→ CONNECTION ERRORS
    │   ├─ BigBasket unreachable
    │   │   └─ Retry after delay
    │   ├─ Ollama not running
    │   │   └─ Display warning, use cache
    │   └─ File I/O error
    │       └─ Log and skip
    │
    ├─→ VALIDATION ERRORS
    │   ├─ Missing fields
    │   │   └─ Skip product
    │   ├─ Invalid format
    │   │   └─ Clean and continue
    │   └─ Type mismatch
    │       └─ Convert and log
    │
    ├─→ PROCESSING ERRORS
    │   ├─ AI model error
    │   │   └─ Use fallback
    │   ├─ Calculation error
    │   │   └─ Log and show default
    │   └─ Data error
    │       └─ Handle gracefully
    │
    └─→ UI ERRORS
        ├─ Display error
        │   └─ Show error message
        ├─ Chart generation
        │   └─ Show placeholder
        └─ Session error
            └─ Reinitialize session
```

---

## State Management Flow

```
APPLICATION START
    │
    ├─→ Initialize Streamlit
    ├─→ Load configuration
    ├─→ Connect to data sources
    └─→ Initialize session state
    │
    ↓
USER INTERACTION
    │
    ├─→ Sidebar input
    ├─→ Update session state
    ├─→ Trigger callbacks
    ├─→ Fetch/process data
    └─→ Update display
    │
    ↓
DATA UPDATES
    │
    ├─→ Price changes detected
    ├─→ Alerts triggered
    ├─→ New insights generated
    └─→ Notifications sent
    │
    ↓
STATE PERSISTENCE
    │
    ├─→ Save to CSV
    ├─→ Update cache
    ├─→ Log changes
    └─→ Refresh UI
    │
    ↓
APPLICATION END
    │
    └─→ Close connections
    └─→ Save state
```

---

## Technology Stack

```
FRONTEND
├─ Streamlit (Web UI)
├─ Plotly (Charts & Graphs)
├─ HTML/CSS (Custom styling)
└─ JavaScript (Interactions)

BACKEND
├─ Python 3.8+
├─ Pandas (Data manipulation)
├─ NumPy (Numerical computation)
└─ Requests (HTTP calls)

AI/ML
├─ Ollama (Local LLM)
├─ Qwen2/Llama3 (Models)
└─ Natural Language Processing

DATA
├─ CSV Files (Local storage)
├─ In-Memory DataFrames
└─ Session Cache

EXTERNAL
├─ BigBasket (Data source)
├─ Email Service (Notifications)
└─ Network APIs
```

---

## Network Communication

```
CLIENT BROWSER (127.0.0.1:8501)
    │
    ↓ HTTP/WebSocket (Streamlit)
    │
STREAMLIT SERVER (localhost)
    │
    ├─→ HTTP GET/POST (BigBasket)
    │   └─ Product data
    │
    ├─→ gRPC (Ollama Local)
    │   └─ AI inference
    │
    └─→ File I/O (Local filesystem)
        └─ CSV data persistence
```

---

## Scalability Potential

```
CURRENT STATE
├─ Single-user web app
├─ Local data storage
├─ Single Ollama instance
└─ Limited concurrent operations

SCALING OPTIONS
│
├─ HORIZONTAL SCALING
│   ├─ Multiple Streamlit instances
│   ├─ Load balancer
│   └─ Shared data backend
│
├─ VERTICAL SCALING
│   ├─ Larger models
│   ├─ More RAM
│   └─ Better CPU
│
├─ DATA SCALING
│   ├─ Database (PostgreSQL)
│   ├─ Caching layer (Redis)
│   └─ Data warehouse
│
└─ PROCESSING SCALING
    ├─ Async processing
    ├─ Queue system (Celery)
    └─ Distributed computing
```

---

## Performance Characteristics

```
OPERATION TIMES (Approximate)
│
├─ Fetch single product: 0.5-1s
├─ Fetch 10 products: 5-10s
├─ Validate data: 0.1-0.5s
├─ Generate insights: 2-5s
├─ Price comparison: 0.5-1s
├─ Dashboard render: 1-2s
└─ Alert check: 0.2-0.5s

RESOURCE USAGE
│
├─ Memory: 200-500 MB
├─ CPU: 20-40% (normal), 80%+ (processing)
├─ Disk: 10-50 MB (data storage)
└─ Network: 1-5 Mbps (API calls)

BOTTLENECKS
│
├─ API response time (BigBasket)
├─ AI model inference (Ollama)
├─ Streamlit refresh cycle
└─ CSV I/O operations
```

---

## Deployment Architecture

```
DEVELOPMENT
├─ Local Python environment
├─ Local Ollama instance
├─ CSV file storage
└─ Streamlit dev server

PRODUCTION
├─ Python Docker container
├─ Ollama Docker container
├─ PostgreSQL database
├─ Nginx reverse proxy
├─ Redis cache
└─ Systemd service management
```

---

**Last Updated:** April 2026
**Version:** 1.0.0

