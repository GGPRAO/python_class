# 🚗 Cars Compare Bot

An intelligent AI-powered chatbot for comparing cars, specifications, features, and models in an easy-to-understand tabular format.

## 🎯 Features

- **Compare Multiple Cars**: Get detailed side-by-side comparisons
- **Specifications in Tables**: View specs in clean, organized table format
- **Performance Analysis**: Compare 0-60 times, top speed, horsepower
- **Fuel Efficiency**: Compare consumption and range
- **Price Comparison**: Find cars within your budget
- **Model Variants**: Explore different trim levels and engine options
- **Smart Recommendations**: Get personalized car suggestions
- **Real-time AI Chat**: Ask any car-related question and get instant answers

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Ollama installed ([Download here](https://ollama.ai))
- Ollama model: `qwen2:1.5b`

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd cars_compare_bot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start Ollama (in a separate terminal):**
   ```bash
   ollama run qwen2:1.5b
   ```

4. **Run the chatbot:**
   
   **Windows (PowerShell):**
   ```bash
   .\START_CHATBOT.ps1
   ```
   
   **Windows (Command Prompt):**
   ```bash
   START_CHATBOT.bat
   ```
   
   **Linux/Mac:**
   ```bash
   streamlit run app.py
   ```

The chatbot will open in your browser at `http://localhost:8501`

## 💻 How to Use

### Basic Comparison
Ask questions like:
- "Compare Tesla Model 3 vs BMW 3 Series"
- "What's the difference between Honda Civic and Toyota Corolla?"
- "Show me cars under $30,000"

### Specification Lookup
- "Show me the 0-60 time for Ford Mustang"
- "Which car has the best fuel efficiency?"
- "Compare electric vehicles available"

### Smart Recommendations
- "Best sports car under $50,000?"
- "I want a fuel-efficient family car"
- "Compare luxury sedans with good range"

## 🎨 Interface Features

### Sidebar Options
- **Comparison Type**: Choose what aspect to compare (price, performance, etc.)
- **Vehicle Category**: Filter by car type (sedan, SUV, sports car, electric, etc.)
- **Price Range**: Set your budget constraints
- **Top Priorities**: Select what matters most (performance, fuel economy, comfort, etc.)
- **Display Format**: View comparisons in table format

### Quick Action Buttons
Popular comparisons are available as quick buttons:
- "Compare Tesla Model 3 vs BMW 3 Series"
- "Best cars under $30,000"
- "Electric vs Hybrid - which is better?"
- "Compare Honda Civic vs Toyota Corolla"

### Sample Specifications Table
View a quick reference table of popular car models with key specs

## 📊 Comparison Features

### Performance Specs
- Horsepower and Torque
- 0-60 Acceleration Time
- Top Speed
- Transmission Type

### Efficiency Metrics
- Fuel Consumption (L/100km)
- Electric Range (for EVs)
- Tank/Battery Capacity
- Estimated Range

### Practical Information
- Price Range
- Seating Capacity
- Cargo Space
- Engine Type
- Transmission

## 🛠️ Troubleshooting

### Error: "Ollama connection failed"
- Make sure Ollama is installed: https://ollama.ai
- Make sure Ollama is running in a separate terminal
- Run: `ollama run qwen2:1.5b`

### Slow Responses
- Check your internet connection
- Ensure Ollama has enough system resources
- Close other applications to free up memory

### Missing Model
If the model doesn't exist, install it:
```bash
ollama pull qwen2:1.5b
```

## 📋 Project Structure

```
cars_compare_bot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── START_CHATBOT.bat       # Windows batch startup script
├── START_CHATBOT.ps1       # Windows PowerShell startup script
├── README.md               # This file
├── SETUP_GUIDE.md          # Detailed setup instructions
├── QUICK_REFERENCE.md      # Quick reference guide
├── CUSTOMER_GUIDE.md       # User guide
├── LAUNCH_CHECKLIST.md     # Pre-launch checklist
├── FILE_INDEX.md           # File documentation
└── PROJECT_INDEX.md        # Project overview
```

## 📚 Sample Car Data

The bot has access to a database with specifications for:
- Tesla Model 3 (Electric)
- BMW 3 Series (Luxury Sedan)
- Honda Civic (Compact Sedan)
- Toyota Corolla (Hybrid Compact)
- Ford Mustang (Sports Car)

## 🔧 Customization

### Add More Car Models
Edit the `cars_database` dictionary in `app.py` to add more vehicles with their specifications.

### Change UI Colors
Modify the CSS gradients in the `st.markdown()` styling section to match your brand colors.

### Adjust AI Model
Change the model from `qwen2:1.5b` to any other Ollama-supported model:
```python
response = ollama.chat(
    model="your-model-name",
    ...
)
```

## 🎓 Technologies Used

- **Streamlit**: Web UI framework
- **Ollama**: Local AI models
- **Pandas**: Data manipulation and tables
- **Python**: Core language

## ⚡ Performance Tips

- For faster responses, use lighter models or increase system RAM
- Keep Ollama running in the background
- Close browser tabs to reduce memory usage
- For multiple concurrent users, deploy on a server

## 📞 Support

If you encounter issues:
1. Check the SETUP_GUIDE.md for detailed setup instructions
2. Review the QUICK_REFERENCE.md for common commands
3. Ensure Ollama is properly installed and running
4. Check system resources and memory usage

## 📄 License

This project is part of the AI Bots collection.

## 🌟 Features Roadmap

- [ ] Real-time market data integration
- [ ] User reviews and ratings
- [ ] Financing calculator
- [ ] Trade-in valuation
- [ ] Insurance cost estimator
- [ ] Service record tracking
- [ ] Maintenance reminder system

---

**Made with ❤️ for car enthusiasts | Powered by AI**

