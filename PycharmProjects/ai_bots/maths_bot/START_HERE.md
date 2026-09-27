# 🎯 Maths Bot Overview & Quick Start

## What is Maths Bot?

An **AI-powered mathematics tutor chatbot** that:
- Solves math problems instantly
- Explains solutions step-by-step
- Adapts to your learning style
- Provides practice problems
- Verifies answers

Built like `trip_planner_india` with Streamlit + Ollama + Python

## File Structure

```
maths_bot/
├── 📱 APP.PY (The Bot)
│   └── Main Streamlit application with AI
│
├── 📚 DOCUMENTATION
│   ├── README.md ..................... Full guide
│   ├── SETUP_GUIDE.md ............... Installation steps
│   ├── QUICK_REFERENCE.md ........... Quick tips
│   ├── LAUNCH_CHECKLIST.md .......... Pre-launch check
│   ├── CUSTOMER_GUIDE.md ............ User guide
│   ├── PROJECT_INDEX.md ............ Navigation
│   └── FILE_INDEX.md ............... File details
│
├── ⚙️ CONFIGURATION
│   └── requirements.txt ............. Dependencies
│
└── 🚀 LAUNCHERS
    ├── START_CHATBOT.bat ........... Windows batch
    └── START_CHATBOT.ps1 ........... Windows PowerShell
```

## 5-Minute Quick Start

### Windows (Easiest)
1. Open folder: `C:\Users\USER\PycharmProjects\ai_bots\maths_bot`
2. Double-click: `START_CHATBOT.bat`
3. Wait for browser to open
4. Start asking math problems!

### All Systems (Manual)
```bash
cd maths_bot
pip install -r requirements.txt
streamlit run app.py
```

## Prerequisites

### Must Have
✅ Python 3.8+ → https://python.org
✅ Ollama → https://ollama.ai
✅ Model → `ollama pull qwen2:1.5b`

### Before Launching
1. Ensure Python is installed: `python --version`
2. Ensure Ollama is running: `ollama serve`
3. Navigate to maths_bot folder
4. Run launcher

## What You Can Do

### Problem Solving
Ask any math question:
- "Solve 2x² + 5x - 3 = 0"
- "What is 15% of 480?"
- "Area of circle with radius 5?"

### Learning Styles
Choose how to learn:
- ⚡ Quick Solution (just the answer)
- 📝 Step-by-Step (show process)
- 📖 Detailed (explain concepts)
- 🎨 Visual (use diagrams)

### Difficulty Levels
Pick your level:
- Elementary (K-5)
- Middle School (6-8)
- High School (9-12)
- College Level
- Advanced

### Math Categories
8 types of math:
- 🔢 Arithmetic
- 📐 Geometry
- 📊 Algebra
- 📈 Calculus
- 🎲 Probability & Statistics
- 🔣 Trigonometry
- 💯 Word Problems
- 🧩 Logic & Puzzles

### Extra Features
✅ Answer verification (double-check solutions)
✅ Practice problems (similar problems)
✅ Topic context (for better answers)
✅ Chat history (all conversations saved)

## Documentation Files Explained

### For Setup
| File | Time | Purpose |
|------|------|---------|
| SETUP_GUIDE.md | 25 min | Installation steps |
| LAUNCH_CHECKLIST.md | 5 min | Pre-launch check |

### For Using
| File | Time | Purpose |
|------|------|---------|
| README.md | 15 min | Complete guide |
| QUICK_REFERENCE.md | 5 min | Quick examples |
| CUSTOMER_GUIDE.md | 10 min | User guide |

### For Navigation
| File | Time | Purpose |
|------|------|---------|
| PROJECT_INDEX.md | 5 min | Find things |
| FILE_INDEX.md | 5 min | File details |

## Example Conversation

```
YOU: "Solve 2x + 5 = 15"

BOT:
Step 1: Start with equation → 2x + 5 = 15

Step 2: Subtract 5 from both sides → 2x = 10

Step 3: Divide by 2 → x = 5

Answer: x = 5

Verification: 2(5) + 5 = 15 ✓

Practice Problems:
1. Solve: 3x + 2 = 11
2. Solve: 4x - 3 = 9
```

## Technical Details

- **Framework**: Streamlit (web interface)
- **AI**: Ollama (local model)
- **Model**: Qwen 2 1.5B (fast, lightweight)
- **Language**: Python
- **UI**: Beautiful gradient styling
- **Speed**: 5-30 seconds per response

## Troubleshooting

### Common Issues

**"Python not found"**
→ Install from https://python.org

**"Ollama not running"**
→ Open terminal: `ollama serve`

**"Model not found"**
→ Run: `ollama pull qwen2:1.5b`

**"Port 8501 in use"**
→ Run: `streamlit run app.py --server.port 8502`

## Key Differences from Trip Planner

| Feature | Trip Planner | Maths Bot |
|---------|--------------|-----------|
| Purpose | Travel planning | Math solving |
| Sidebar | Trip preferences | Math preferences |
| Categories | Regions + transport | Math categories |
| Output | Travel tips | Solutions + explanations |
| Learning Styles | No | Yes (4 styles) |
| Difficulty Levels | No | Yes (5 levels) |

## Popular Questions

**Q: What OS does it work on?**
A: Windows, macOS, Linux (with Python & Ollama)

**Q: Can I use it offline?**
A: Once model is downloaded, yes! Ollama runs locally.

**Q: How fast is it?**
A: 5-30 seconds per response depending on problem complexity

**Q: Does it save my conversations?**
A: During session only. Closes when you exit.

**Q: Can I customize it?**
A: Yes! Edit app.py to change colors, categories, model, etc.

**Q: Is it accurate?**
A: Very good for K-12 and college math. Verify for critical work.

**Q: Can teachers use it?**
A: Perfect teaching tool! Check CUSTOMER_GUIDE.md section for teachers.

## Pro Tips

1. **Set Your Level** → Choose correct difficulty for better explanations
2. **Be Specific** → Include all numbers and operations
3. **Use Topic** → Helps bot understand context
4. **Enable Verification** → Double-check important answers
5. **Practice Actively** → Do problems yourself, use bot for help
6. **Ask Follow-ups** → Clarify anything you don't understand
7. **Review Solutions** → Don't just copy, understand concepts

## Next Steps

1. ✅ Review this file (2 min)
2. ✅ Run START_CHATBOT.bat (Windows) or app.py
3. ✅ Set preferences in sidebar
4. ✅ Try example problems
5. ✅ Read QUICK_REFERENCE.md for more examples

## File Reading Quick Guide

```
New User? Start here:
1. This file (2 min)
2. README.md (15 min)
3. SETUP_GUIDE.md (25 min)
4. Start using!

Quick Reference?
→ QUICK_REFERENCE.md

Need Help?
→ LAUNCH_CHECKLIST.md → Troubleshooting

Lost?
→ PROJECT_INDEX.md
```

## Command Cheat Sheet

```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama service
ollama serve

# Pull model
ollama pull qwen2:1.5b

# Start bot
streamlit run app.py

# Different port
streamlit run app.py --server.port 8502

# Stop bot
Ctrl+C
```

## What's Installed

- **streamlit==1.28.1** - Web interface
- **ollama==0.0.12** - AI integration
- **python-dateutil==2.8.2** - Date utilities

Total size: ~50 MB

## Success Indicators

✅ Bot starts and opens browser
✅ Can ask math questions
✅ Get responses within 30 seconds
✅ Responses are formatted nicely
✅ Sidebar controls work
✅ Chat history shows

If all above work → You're good to go! 🎉

## Resources

- Python: https://python.org
- Ollama: https://ollama.ai
- Streamlit: https://streamlit.io
- Docs: See README.md

## Summary

You now have a complete AI math tutor that:
- ✅ Solves problems instantly
- ✅ Explains step-by-step
- ✅ Adapts to learning style
- ✅ Provides practice
- ✅ Has beautiful UI
- ✅ Is fully documented
- ✅ Easy to launch
- ✅ Ready to use

**Happy solving!** 🧮✨

---

For detailed information, see README.md
For setup issues, see SETUP_GUIDE.md
For usage tips, see QUICK_REFERENCE.md

