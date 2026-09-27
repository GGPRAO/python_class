# 🔬 Science Bot - Project Index

Complete file structure and documentation map for the Science Formula & Concept Bot.

## 📁 Project Structure

```
science_bot/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── START_CHATBOT.ps1        # PowerShell launcher (Windows)
├── START_CHATBOT.bat        # Batch launcher (Windows)
├── README.md                # Full project documentation
├── SETUP_GUIDE.md           # Installation & setup instructions
├── QUICK_REFERENCE.md       # Quick answers & formulas
├── PROJECT_INDEX.md         # This file
├── FILE_INDEX.md            # Detailed file descriptions
├── LAUNCH_CHECKLIST.md      # Pre-launch verification
└── CUSTOMER_GUIDE.md        # User guide & features
```

## 📄 File Descriptions

### Core Application Files

**`app.py`** (248 lines)
- Main Streamlit application
- Handles UI/UX and chat interface
- Manages session state and conversation history
- Communicates with Ollama AI backend
- Features:
  - Sidebar preferences for difficulty, subject, learning style
  - Chat message display (user & bot)
  - Formula derivation toggle
  - Real-world applications toggle
  - Quick example questions
  - Error handling for Ollama connection

**`requirements.txt`** (3 dependencies)
- Streamlit 1.28.1 - Web app framework
- Ollama 0.0.12 - AI backend connector
- Python-dateutil 2.8.2 - Date/time utilities

### Launcher Scripts

**`START_CHATBOT.ps1`** (Windows PowerShell)
- Cross-platform launcher for PowerShell
- Checks if Streamlit is installed
- Verifies Ollama is running
- Provides friendly status messages
- Automatically opens browser at localhost:8501

**`START_CHATBOT.bat`** (Windows Command Prompt)
- Batch script launcher for Windows CMD
- Alternative to PowerShell version
- Same functionality as .ps1 version
- User-friendly error handling

### Documentation Files

**`README.md`** (Complete Guide)
- Project overview and features
- Comprehensive feature list
- Installation instructions (all platforms)
- Usage guide with examples
- Troubleshooting section
- Science formulas reference
- System requirements
- Credits and support info

**`SETUP_GUIDE.md`** (Step-by-Step)
- Detailed installation walkthrough
- System requirements checklist
- Python installation guide
- Ollama installation (Windows, Mac, Linux)
- Three different launch methods
- First-time usage tips
- Advanced troubleshooting
- Verification checklist

**`QUICK_REFERENCE.md`** (Fast Lookup)
- 30-second quick start
- FAQ section (10+ common questions)
- Formula quick reference tables
- Physics, Chemistry, Biology formulas
- Keyboard shortcuts
- Example questions by subject
- Common fixes
- Tips & tricks

**`PROJECT_INDEX.md`** (This File)
- Project structure overview
- File descriptions and contents
- Navigation guide
- Links to related documents
- Development notes

**`FILE_INDEX.md`** (Detailed Reference)
- Deep dive into each file
- Line counts and purposes
- Dependencies mapping
- Function descriptions
- Configuration options

**`LAUNCH_CHECKLIST.md`** (Pre-Launch)
- Pre-launch verification steps
- System requirements check
- Installation verification
- Ollama setup verification
- Python package verification
- Port availability check
- Quick troubleshooting
- Success indicators

**`CUSTOMER_GUIDE.md`** (User Manual)
- Getting started guide
- Feature explanations
- UI walkthrough
- Settings configuration
- Best practices
- Common use cases
- Advanced features
- Support resources

## 🗺️ Navigation Guide

### For First-Time Users
1. Start here: [README.md](README.md) - Overview
2. Then go to: [SETUP_GUIDE.md](SETUP_GUIDE.md) - Installation
3. Before launching: [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md) - Verification
4. After launch: [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md) - How to use

### For Quick Answers
- **How do I start?** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **Something not working?** → [SETUP_GUIDE.md](SETUP_GUIDE.md) - Troubleshooting section
- **How do I use X feature?** → [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md)

### For Developers/Customizers
1. [FILE_INDEX.md](FILE_INDEX.md) - Understand each file
2. [app.py](app.py) - Main code
3. [requirements.txt](requirements.txt) - Dependencies

### For Project Overview
- [PROJECT_INDEX.md](PROJECT_INDEX.md) - This navigation guide
- [README.md](README.md) - Full feature list and requirements

## 🔍 Key Concepts

### Difficulty Levels
- **Elementary (K-5)**: Basic concepts, no advanced math
- **Middle School (6-8)**: Foundational principles, simple formulas
- **High School (9-12)**: Complex formulas, mathematical derivations
- **College Level**: University-level science, advanced math
- **Advanced Research**: Specialized topics, research-oriented content

### Science Subjects
1. 🔋 Physics - Motion, forces, energy, waves, electricity
2. ⚗️ Chemistry - Reactions, bonding, states of matter
3. 🧬 Biology - Cells, genetics, evolution, ecosystems
4. 🌍 Earth & Environmental - Geology, weather, climate
5. 🔭 Astronomy & Space - Celestial mechanics, stars, galaxies
6. 💡 Quantum Mechanics - Uncertainty, superposition, duality
7. 🌊 Thermodynamics - Heat, entropy, energy transfer
8. ⚛️ Atomic & Nuclear - Radioactivity, fission, fusion

### Learning Styles
- **Quick Formula** - Fast reference
- **Formula Explained** - Formula + definitions
- **Detailed Theory** - Full derivation + context
- **Lab Simulation** - Experimental approach

## 🛠️ Customization Points

### In `app.py`:
- **Color scheme**: Change CSS in `st.markdown("""<style>...`
- **AI Model**: Change `model="qwen2:1.5b"` to another Ollama model
- **Page icon/title**: Edit `st.set_page_config(...)`
- **Science subjects**: Add to `st.selectbox()` options
- **Quick questions**: Edit `quick_queries` list

### In `requirements.txt`:
- Update version numbers as needed
- Add new dependencies as required

### Launcher Scripts:
- Modify paths if needed
- Change port number in ps1/bat files if 8501 is busy

## 📊 Statistics

| File | Purpose | Size |
|------|---------|------|
| app.py | Main application | 248 lines |
| README.md | Full documentation | 260+ lines |
| SETUP_GUIDE.md | Installation guide | 400+ lines |
| QUICK_REFERENCE.md | Quick reference | 300+ lines |
| CUSTOMER_GUIDE.md | User manual | 300+ lines |
| requirements.txt | Dependencies | 3 packages |
| START_CHATBOT.ps1 | Windows launcher | Script |
| START_CHATBOT.bat | Windows launcher | Script |

## 🚀 Quick Links

- **Installation Help**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **How to Use**: See [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md)
- **Quick Answers**: See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **File Details**: See [FILE_INDEX.md](FILE_INDEX.md)
- **Pre-Launch Check**: See [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md)

## 💻 System Requirements Recap

- Python 3.8+
- 4GB RAM (8GB recommended)
- 3GB disk space (for Ollama model)
- Windows/Mac/Linux
- Internet connection (for setup only)

## 🎯 Next Steps

1. **Just downloaded?** → Read [README.md](README.md)
2. **Ready to install?** → Follow [SETUP_GUIDE.md](SETUP_GUIDE.md)
3. **Need to check setup?** → Use [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md)
4. **Ready to launch?** → Run `START_CHATBOT.ps1` or `START_CHATBOT.bat`
5. **How do I use it?** → See [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md)
6. **Quick question?** → Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

**Last Updated:** April 2026
**Version:** 1.0
**Status:** Ready for use

For detailed information, see the individual documentation files listed above.

