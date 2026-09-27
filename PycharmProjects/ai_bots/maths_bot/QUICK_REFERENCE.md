# 🧮 Quick Reference Guide

## Fast Setup

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Install Ollama
- Download: https://ollama.ai
- Run model: `ollama run qwen2:1.5b`

### 3. Start Bot
```bash
streamlit run app.py
```
or double-click `START_CHATBOT.bat` (Windows)

## Math Categories & Examples

### 🔢 Arithmetic
- "What is 15% of 480?"
- "Simplify 3/4 + 2/5"
- "Convert 0.625 to a fraction"

### 📐 Geometry
- "Area of circle with radius 5?"
- "Volume of cube with side 4?"
- "Find hypotenuse of right triangle (3,4)"

### 📊 Algebra
- "Solve 2x² + 5x - 3 = 0"
- "Factor x² - 9"
- "Find slope through (2,3) and (5,9)"

### 📈 Calculus
- "Derivative of 3x² + 2x - 1"
- "Integral of x² from 0 to 3"
- "Limit of (x²-4)/(x-2) as x→2"

### 🔣 Trigonometry
- "sin(45°) = ?"
- "cos(60°) = ?"
- "Verify: sin²θ + cos²θ = 1"

### 🎲 Probability & Statistics
- "Probability of rolling a 6 on die?"
- "Mean of 2,4,6,8,10"
- "Standard deviation of 1,2,3,4,5"

### 💯 Word Problems
- "Train travels 120 km in 2 hours. Speed?"
- "Store offers 20% off $50 item. Final price?"
- "If 5 workers build in 10 days, 10 workers build in ?"

### 🧩 Logic & Puzzles
- "What number is 1/3 of 30?"
- "What comes next: 2, 4, 8, 16, ?"

## Difficulty Levels

| Level | Best For |
|-------|----------|
| Elementary (K-5) | Basic arithmetic, simple shapes |
| Middle School (6-8) | Pre-algebra, fractions |
| High School (9-12) | Algebra, geometry, trig |
| College | Calculus, linear algebra |
| Advanced | Real analysis, proofs |

## Learning Styles

| Style | Use When |
|-------|----------|
| Quick Solution | Just need the answer |
| Step-by-Step | Want to see the process |
| Detailed Explanation | Need to understand concepts |
| Visual Guide | Prefer diagrams/visualizations |

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Send Message | Enter |
| Clear Chat | Ctrl+L (restart bot) |
| Stop Server | Ctrl+C |

## Troubleshooting

### "Ollama not running"
```bash
ollama serve
```

### "Model not found"
```bash
ollama pull qwen2:1.5b
```

### Port 8501 busy
```bash
streamlit run app.py --server.port 8502
```

### Slow responses
- Close other apps
- Use faster internet
- Ensure 4GB+ RAM available

## Tips & Tricks

1. ✅ **Be Specific**: Include all numbers and operations
2. ✅ **Set Context**: Use the sidebar topic field
3. ✅ **Enable Verification**: Double-check important answers
4. ✅ **Try Examples**: Use quick problem buttons
5. ✅ **Ask Follow-ups**: Clarify anything you don't understand

## File Structure

```
maths_bot/
├── app.py                 # Main app
├── requirements.txt       # Dependencies
├── README.md             # Full documentation
├── QUICK_REFERENCE.md    # This file
├── START_CHATBOT.bat     # Windows launcher
└── START_CHATBOT.ps1     # PowerShell launcher
```

## Common Mathematical Symbols

| Symbol | Name | Example |
|--------|------|---------|
| + | Plus | 2 + 3 = 5 |
| - | Minus | 5 - 2 = 3 |
| × or * | Multiply | 3 × 4 = 12 |
| ÷ or / | Divide | 12 ÷ 3 = 4 |
| ^ | Power | 2^3 = 8 |
| √ | Square Root | √16 = 4 |
| = | Equals | x = 5 |
| ≠ | Not Equal | 2 ≠ 3 |
| < | Less Than | 2 < 5 |
| > | Greater Than | 5 > 2 |

## Common Formulas

### Geometry
- Rectangle Area: A = length × width
- Circle Area: A = πr²
- Triangle Area: A = ½ × base × height
- Pythagorean: a² + b² = c²

### Algebra
- Quadratic Formula: x = (-b ± √(b²-4ac)) / 2a
- Slope: m = (y₂ - y₁) / (x₂ - x₁)
- Distance: d = √((x₂-x₁)² + (y₂-y₁)²)

### Calculus
- Power Rule: d/dx[xⁿ] = nxⁿ⁻¹
- Product Rule: (f×g)' = f'g + fg'
- Chain Rule: (f(g(x)))' = f'(g(x)) × g'(x)

## Supported Problem Types

✅ Arithmetic operations
✅ Fractions and decimals
✅ Percentages
✅ Basic algebra
✅ Quadratic equations
✅ Systems of equations
✅ Geometry calculations
✅ Trigonometry
✅ Basic calculus
✅ Word problems
✅ Logic puzzles

## Response Time

- Typical: 5-15 seconds
- Complex problems: 15-30 seconds
- Very advanced: 30+ seconds

---

**Need more help?** Read the full README.md or check Streamlit docs at https://streamlit.io

