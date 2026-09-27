# 🧮 Maths Problem Solver Bot

An intelligent, AI-powered chatbot application for solving math problems with detailed explanations. Get step-by-step solutions, understand concepts, and improve your math skills across all levels.

## ✨ Features

### 📚 Comprehensive Math Categories
- **🔢 Arithmetic**: Basic operations, fractions, decimals, percentages
- **📐 Geometry**: Shapes, areas, volumes, angles, theorems
- **📊 Algebra**: Equations, polynomials, factoring, functions
- **📈 Calculus**: Derivatives, integrals, limits, optimization
- **🎲 Probability & Statistics**: Distributions, probability, data analysis
- **🔣 Trigonometry**: Angles, identities, applications
- **💯 Word Problems**: Real-world problem solving
- **🧩 Logic & Puzzles**: Brain teasers and logical reasoning

### 🎓 Difficulty Levels
- **Elementary (K-5)**: Basic arithmetic and shapes
- **Middle School (6-8)**: Pre-algebra and basic geometry
- **High School (9-12)**: Algebra, geometry, trigonometry, precalculus
- **College Level**: Calculus, linear algebra, advanced statistics
- **Advanced**: Real analysis, abstract algebra, advanced calculus

### 💡 Learning Styles
- **Quick Solution**: Fast answer with minimal steps for quick reference
- **Step-by-Step**: Numbered steps showing the complete solution process
- **Detailed Explanation**: In-depth theory, formulas, and reasoning behind each step
- **Visual Guide**: ASCII representations and visual descriptions

### 🎯 Smart Features
- ✅ **Solution Verification**: Cross-check answers using alternate methods
- 📝 **Practice Problems**: Generated similar problems for additional practice
- 🔍 **Common Mistakes**: Highlighted typical errors to avoid
- 🌍 **Real-World Applications**: Connect math to practical scenarios
- 📖 **Concept Explanations**: Understand the "why" behind the math
- 💬 **Interactive Dialogue**: Follow-up questions welcome for clarification

## 📋 Quick Start

### Prerequisites
- Python 3.8 or higher
- Ollama (for AI responses)
- Internet connection
- 4GB RAM minimum

### Installation

1. **Clone or navigate to the project directory:**
```bash
cd C:\Users\USER\PycharmProjects\ai_bots\maths_bot
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Install Ollama:**
   - Download from https://ollama.ai
   - Follow installation instructions for your OS
   - Pull the required model: `ollama run qwen2:1.5b`

### Usage

#### Option 1: PowerShell (Windows)
```powershell
.\START_CHATBOT.ps1
```

#### Option 2: Command Prompt (Windows)
```bash
START_CHATBOT.bat
```

#### Option 3: Manual Start
```bash
streamlit run app.py
```

The bot will open in your default web browser at `http://localhost:8501`

## 🎮 How to Use

1. **Select Your Preferences** (left sidebar):
   - Choose your difficulty level
   - Select the math category
   - Pick your preferred learning style
   - Enable/disable verification and practice problems
   - Enter your current topic (optional)

2. **Ask a Question**:
   - Type your math problem in the input box
   - Click "Send" or press Enter
   - The bot will solve and explain your problem

3. **Learn & Practice**:
   - Review the step-by-step solution
   - Understand the concepts explained
   - Try the practice problems provided
   - Ask follow-up questions

## 📝 Example Problems

### Algebra
- "Solve 2x² + 5x - 3 = 0"
- "Simplify: (x² - 4) / (x + 2)"
- "Find the slope of the line through (2,3) and (5,9)"

### Geometry
- "What is the area of a circle with radius 5?"
- "Find the volume of a cube with side length 4 cm"
- "Calculate the hypotenuse of a right triangle with legs 3 and 4"

### Arithmetic & Percentages
- "Calculate: 25% of 480"
- "What is 3/4 divided by 2/5?"
- "Convert 0.375 to a fraction"

### Calculus
- "Find the derivative of f(x) = 3x² + 2x - 1"
- "Evaluate the integral of x² from 0 to 3"
- "Find the limit as x approaches 2 of (x² - 4)/(x - 2)"

### Word Problems
- "If a train travels 120 km in 2 hours, what is its average speed?"
- "A store offers a 20% discount on a $50 item. What is the final price?"

## 🛠️ Troubleshooting

### Issue: "Error: Ollama not running"
**Solution**: 
- Make sure Ollama is installed from https://ollama.ai
- Run `ollama serve` in a terminal
- Then start the bot

### Issue: "Model not found: qwen2:1.5b"
**Solution**:
- Run: `ollama pull qwen2:1.5b`
- Wait for download to complete
- Restart the bot

### Issue: "Port 8501 is already in use"
**Solution**:
- Close other Streamlit apps running on the same port
- Or run with: `streamlit run app.py --server.port 8502`

### Issue: Slow responses
**Solution**:
- Ensure you have at least 4GB free RAM
- Close other resource-heavy applications
- Use a faster model if available

## 📊 Model Information

- **Model**: Qwen 2 (1.5B parameters)
- **Language**: Python
- **Framework**: Streamlit (UI), Ollama (AI Backend)
- **Optimization**: Lightweight yet accurate for most math problems

## 🚀 Advanced Features

### Customization
Edit `app.py` to:
- Change the model (line 140): `model="qwen2:1.5b"`
- Adjust UI colors and styling (lines 19-45)
- Add more math categories in the sidebar
- Create custom learning styles

### Integration
This bot can be:
- Deployed on Streamlit Cloud
- Integrated with educational platforms
- Used as an API backend for other applications
- Extended with additional AI models

## 📚 Categories Explained

| Category | Topics |
|----------|--------|
| 🔢 Arithmetic | Addition, subtraction, multiplication, division, fractions, decimals, percentages |
| 📐 Geometry | Shapes, areas, perimeters, volumes, surface areas, angles, theorems |
| 📊 Algebra | Linear equations, quadratic equations, polynomials, functions, factoring |
| 📈 Calculus | Limits, derivatives, integrals, optimization, differential equations |
| 🎲 Probability & Statistics | Probability, distributions, mean, median, mode, standard deviation |
| 🔣 Trigonometry | Sine, cosine, tangent, identities, applications |
| 💯 Word Problems | Real-world scenarios, multi-step problems, critical thinking |
| 🧩 Logic & Puzzles | Pattern recognition, logical reasoning, mathematical puzzles |

## 🎓 Learning Levels

| Level | Topics | Examples |
|-------|--------|----------|
| Elementary (K-5) | Basic arithmetic, simple shapes | 5+3, area of squares |
| Middle School (6-8) | Pre-algebra, basic geometry, integers | Solving x+2=5, triangle areas |
| High School (9-12) | Algebra, geometry, trigonometry | Quadratic equations, sine/cosine |
| College | Calculus, linear algebra, proofs | Derivatives, matrix operations |
| Advanced | Real analysis, abstract algebra | Epsilon-delta proofs, group theory |

## 💾 Project Structure

```
maths_bot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── START_CHATBOT.bat      # Windows batch launcher
└── START_CHATBOT.ps1      # Windows PowerShell launcher
```

## 🤝 Tips for Best Results

1. **Be Specific**: Include all relevant information in your problem
2. **Choose Right Difficulty**: Match your learning level for optimal explanations
3. **Use Topic Field**: Help the bot understand context better
4. **Request Practice**: Enable practice problems to solidify learning
5. **Ask for Verification**: Use the verification feature for important problems
6. **Follow-up Questions**: Don't hesitate to ask for clarification

## ⚙️ System Requirements

- **OS**: Windows, macOS, Linux
- **Python**: 3.8+
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 3GB (for Ollama model)
- **Internet**: Required for first model download

## 📝 Notes

- This bot is designed for educational purposes
- Always verify answers independently for critical work
- For competition mathematics, refer to official resources
- The accuracy improves with clearer problem statements

## 🌟 Features Roadmap

- [ ] Upload image of handwritten problems
- [ ] LaTeX equation rendering
- [ ] Save solved problems
- [ ] Create custom problem sets
- [ ] Progress tracking
- [ ] Multiple language support

## 📞 Support

For issues or suggestions:
1. Check the Troubleshooting section above
2. Review Ollama documentation at https://ollama.ai
3. Check Streamlit documentation at https://streamlit.io

## 📄 License

This project is provided as-is for educational use.

---

**Made with ❤️ for students and math enthusiasts**

**Last Updated**: April 2026

