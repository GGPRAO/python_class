# 🔬 Science Bot - File Index

Detailed reference for every file in the Science Bot project.

## 📋 Complete File List

### 1. `app.py` - Main Application

**Purpose**: Core Streamlit application with UI and AI integration

**Size**: 248 lines of Python code

**Key Sections**:
- **Lines 1-5**: Imports (streamlit, ollama, datetime, json, re)
- **Lines 7-56**: Page configuration and CSS styling
- **Lines 58-65**: Title and header
- **Lines 67-70**: Session state initialization
- **Lines 72-97**: Sidebar configuration
  - Difficulty level selector (5 options)
  - Science subject selector (8 subjects)
  - Learning style radio buttons (4 options)
  - Formula derivation checkbox
  - Applications checkbox
  - Current topic text input
- **Lines 99-118**: Chat history display
  - User message rendering
  - Bot response rendering
- **Lines 120-130**: User input section
  - Text input field
  - Send button
- **Lines 132-170**: User input processing
  - Message history management
  - System prompt generation
  - Query enhancement
  - Ollama API call
  - Response handling
- **Lines 172-180**: Error handling
  - Connection error messages
  - Ollama installation guidance
- **Lines 182-196**: Quick suggestion buttons
  - 4 example questions
- **Lines 198-204**: Footer

**Dependencies**:
- streamlit==1.28.1
- ollama==0.0.12
- python-dateutil==2.8.2

**Configuration Points**:
- `model="qwen2:1.5b"` - Change AI model
- Colors in CSS (lines 19-50) - Customize appearance
- Quick questions (line 189) - Add/remove examples
- Page title/icon (line 10-11) - Customize header

**Functions Implemented**:
- Streamlit session state management
- CSS styling injection
- Sidebar widget configuration
- Chat message rendering
- Ollama API integration
- Error handling

---

### 2. `requirements.txt` - Python Dependencies

**Purpose**: Lists required Python packages and versions

**Size**: 3 lines (3 dependencies)

**Content**:
```
streamlit==1.28.1      # Web UI framework
ollama==0.0.12         # AI backend connector
python-dateutil==2.8.2 # Date/time utilities
```

**What Each Does**:
- **streamlit**: Creates interactive web interface
- **ollama**: Enables communication with Ollama AI service
- **python-dateutil**: Provides date/time utilities for timestamps

**Installation**:
```bash
pip install -r requirements.txt
```

**Version Info**:
- Streamlit 1.28.1: Stable, tested version
- Ollama 0.0.12: Compatible with Ollama service
- python-dateutil 2.8.2: Standard utility library

**Can Be Updated**:
- Yes, newer versions may be compatible
- Before updating, test thoroughly
- Downgrade if issues occur

---

### 3. `START_CHATBOT.ps1` - PowerShell Launcher

**Purpose**: Windows PowerShell script to launch the Science Bot

**Size**: ~40 lines of PowerShell code

**Key Features**:
- Friendly console output with colors
- Checks if Streamlit is installed
- Verifies Ollama is running
- Provides installation guidance
- Automatically opens browser

**Usage**:
```powershell
.\START_CHATBOT.ps1
```

**Execution Policy Note**:
May need to run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**What It Does**:
1. Displays colorful header (cyan)
2. Checks Streamlit installation
3. Checks Ollama service status
4. Launches `streamlit run app.py`
5. Catches and displays errors

**System Requirements**:
- Windows PowerShell v3.0+
- .NET Framework 4.5+
- Internet for downloading packages

---

### 4. `START_CHATBOT.bat` - Batch Launcher

**Purpose**: Windows Command Prompt batch script to launch the Science Bot

**Size**: ~30 lines of batch code

**Key Features**:
- Works in Windows Command Prompt
- Checks Streamlit installation
- Verifies Ollama service
- User-friendly messages
- Alternative to PowerShell

**Usage**:
```cmd
START_CHATBOT.bat
```

Or simply double-click the file in File Explorer.

**What It Does**:
1. Sets console color to blue/yellow (0B)
2. Displays startup messages
3. Verifies Streamlit installed
4. Checks Ollama running
5. Launches Streamlit app
6. Catches errors

**System Requirements**:
- Windows Command Prompt
- Administrative access (optional)
- Python in PATH

---

### 5. `README.md` - Complete Documentation

**Purpose**: Full project overview and feature documentation

**Size**: 260+ lines of Markdown

**Main Sections**:

1. **Title & Intro** (Lines 1-5)
   - Project name and description

2. **Features** (Lines 7-60)
   - 8 Science subjects
   - 5 Difficulty levels
   - 4 Learning styles
   - 11 Smart features

3. **Quick Start** (Lines 62-100)
   - Prerequisites checklist
   - Installation steps (5 steps)
   - Launch methods (3 options)

4. **Usage Guide** (Lines 102-170)
   - Getting started process
   - Feature explanations
   - Customization options

5. **Example Topics** (Lines 172-210)
   - Physics examples (9 formulas)
   - Chemistry examples (5 formulas)
   - Biology examples (4 concepts)
   - Earth Science examples (5 concepts)

6. **System Requirements** (Lines 212-220)
   - OS options
   - Python version
   - RAM, Storage, Internet needs

7. **Troubleshooting** (Lines 222-240)
   - 5 Common problems
   - Solutions for each

8. **Resources & Credits** (Lines 242-260)
   - Documentation links
   - Attribution

**For Whom**:
- New users wanting overview
- Understanding features
- Installation guidance
- Troubleshooting help

**Related**: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed installation

---

### 6. `SETUP_GUIDE.md` - Installation Guide

**Purpose**: Step-by-step installation and setup instructions

**Size**: 400+ lines of detailed guide

**Main Sections**:

1. **System Requirements** (Lines 1-30)
   - Minimum specs
   - Recommended specs

2. **Python Installation** (Lines 32-65)
   - Download link
   - Installation steps (5 steps)
   - Verification

3. **Python Package Installation** (Lines 67-95)
   - Navigation to folder
   - Pip installation command
   - Verification

4. **Ollama Installation** (Lines 97-160)
   - Windows (5 steps)
   - macOS (3 steps)
   - Linux (3 commands)
   - Model pulling (qwen2:1.5b)

5. **Launching the Bot** (Lines 162-210)
   - Method 1: PowerShell Script
   - Method 2: Batch File
   - Method 3: Direct Command

6. **First Time Usage** (Lines 212-250)
   - Browser access
   - Interface orientation
   - Configuration steps
   - Tips for best results

7. **Troubleshooting** (Lines 252-350)
   - 8 Common problems with solutions
   - Verification commands
   - Recovery steps

8. **Checklist** (Lines 352-365)
   - 8-item verification checklist

**For Whom**:
- New users installing for first time
- Having installation problems
- Setting up on new computer

**Related**: See [README.md](README.md) for overview

---

### 7. `QUICK_REFERENCE.md` - Quick Lookup

**Purpose**: Fast answers to common questions and formula lookup

**Size**: 300+ lines of quick reference

**Main Sections**:

1. **Quick Start** (Lines 1-10)
   - 30-second launch guide

2. **FAQ** (Lines 12-40)
   - 10 Common questions with answers

3. **Formula Reference** (Lines 42-80)
   - Physics formulas (13 entries)
   - Chemistry formulas (7 entries)
   - Biology formulas (4 entries)
   - All with variables and units

4. **Keyboard Shortcuts** (Lines 82-95)
   - Windows shortcuts
   - Mac shortcuts

5. **Example Questions** (Lines 97-130)
   - Physics questions (5)
   - Chemistry questions (5)
   - Biology questions (5)
   - Earth Science questions (5)

6. **Common Fixes** (Lines 132-155)
   - 3 Common problems with quick solutions

7. **Difficulty Levels** (Lines 157-175)
   - Explanation of each level

8. **Learning Styles** (Lines 177-190)
   - What each style provides

9. **Tips & Tricks** (Lines 192-210)
   - 6 Helpful tips

10. **Resources** (Lines 212-220)
    - External links

**For Whom**:
- Existing users needing quick help
- Formula lookup
- Common question answers
- Quick troubleshooting

**Related**: See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed help

---

### 8. `PROJECT_INDEX.md` - Project Navigation

**Purpose**: High-level project overview and navigation guide

**Size**: 300+ lines of navigation reference

**Main Sections**:

1. **Project Structure** (Lines 1-30)
   - File tree view
   - All 10 main files listed

2. **File Descriptions** (Lines 32-100)
   - Brief overview of each file

3. **Navigation Guide** (Lines 102-140)
   - First-time user path
   - Quick answer paths
   - Developer paths

4. **Key Concepts** (Lines 142-180)
   - Difficulty levels
   - Science subjects
   - Learning styles

5. **Customization Points** (Lines 182-210)
   - Where to modify colors
   - Where to change AI model
   - Where to add subjects

6. **Statistics** (Lines 212-230)
   - File sizes and line counts

7. **Quick Links** (Lines 232-250)
   - Direct links to resources

8. **Next Steps** (Lines 252-270)
   - Action items based on status

**For Whom**:
- Users needing project overview
- Finding specific files
- Understanding structure
- Navigation reference

**Related**: All other documentation files

---

### 9. `FILE_INDEX.md` - Detailed File Reference

**Purpose**: Deep dive into each file (this file)

**Size**: 400+ lines of detailed reference

**Contains**:
- Detailed description of every file
- Line numbers and line counts
- Purpose and content breakdown
- Key features and configuration points
- Usage instructions

**For Whom**:
- Developers modifying code
- Understanding file structure deeply
- Customization reference
- Development reference

---

### 10. `LAUNCH_CHECKLIST.md` - Pre-Launch Verification

**Purpose**: Verify everything is ready before launching

**Size**: 250+ lines of checklist and verification

**Main Sections**:

1. **System Requirements Verification** (Lines 1-30)
   - OS check
   - Python version check
   - RAM check
   - Disk space check

2. **Installation Verification** (Lines 32-65)
   - Python packages check
   - Ollama installation check
   - Model availability check

3. **Configuration Verification** (Lines 67-95)
   - Ollama service check
   - Network connectivity check
   - Port availability check

4. **Final Checks** (Lines 97-130)
   - File structure check
   - Permissions check
   - Configuration check

5. **Troubleshooting** (Lines 132-180)
   - Common issues and solutions
   - Verification commands

6. **Success Checklist** (Lines 182-200)
   - Verification checklist
   - Success indicators
   - Next steps

**For Whom**:
- Before first launch
- Before sharing with others
- Troubleshooting launch issues
- Verification of setup

**Related**: [SETUP_GUIDE.md](SETUP_GUIDE.md) for fixes

---

### 11. `CUSTOMER_GUIDE.md` - User Manual

**Purpose**: How to use the Science Bot for end users

**Size**: 300+ lines of user guide

**Main Sections**:

1. **Getting Started** (Lines 1-50)
   - First launch steps
   - Interface overview
   - Initial configuration

2. **Features Explained** (Lines 52-120)
   - Sidebar options
   - Chat interface
   - Settings

3. **How to Ask Questions** (Lines 122-180)
   - Question formatting
   - Effective queries
   - Follow-up questions

4. **Learning Styles** (Lines 182-220)
   - When to use each style
   - What to expect

5. **Tips for Learning** (Lines 222-270)
   - Best practices
   - Study strategies
   - Effective use

6. **Troubleshooting** (Lines 272-310)
   - Common user issues
   - Quick solutions
   - Support resources

7. **Advanced Features** (Lines 312-340)
   - Custom topics
   - Conversation history
   - Settings adjustment

8. **Frequently Asked Questions** (Lines 342-370)
   - User-focused FAQs

**For Whom**:
- End users learning how to use
- Getting most from the bot
- Learning strategies
- Troubleshooting problems

**Related**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md) for quick answers

---

## 🔗 File Dependencies

```
app.py
├── Requires: requirements.txt
├── Imports from: streamlit, ollama, datetime, json, re
└── Uses: Ollama service (external)

requirements.txt
├── streamlit==1.28.1
├── ollama==0.0.12
└── python-dateutil==2.8.2

START_CHATBOT.ps1
├── Requires: Python, Streamlit
├── Checks: Ollama service
└── Runs: app.py

START_CHATBOT.bat
├── Requires: Python, Streamlit
├── Checks: Ollama service
└── Runs: app.py

Documentation Files
├── README.md (Project overview)
├── SETUP_GUIDE.md (Installation)
├── QUICK_REFERENCE.md (Quick answers)
├── PROJECT_INDEX.md (Navigation)
├── FILE_INDEX.md (This file)
├── LAUNCH_CHECKLIST.md (Verification)
└── CUSTOMER_GUIDE.md (User manual)
```

## 📊 File Statistics

| File | Type | Size | Purpose |
|------|------|------|---------|
| app.py | Python | 248 lines | Main application |
| requirements.txt | Config | 3 lines | Dependencies |
| START_CHATBOT.ps1 | Script | 40 lines | PowerShell launcher |
| START_CHATBOT.bat | Script | 30 lines | Batch launcher |
| README.md | Docs | 260+ lines | Full overview |
| SETUP_GUIDE.md | Docs | 400+ lines | Installation |
| QUICK_REFERENCE.md | Docs | 300+ lines | Quick lookup |
| PROJECT_INDEX.md | Docs | 300+ lines | Navigation |
| FILE_INDEX.md | Docs | 400+ lines | Detailed reference |
| LAUNCH_CHECKLIST.md | Docs | 250+ lines | Pre-launch check |
| CUSTOMER_GUIDE.md | Docs | 300+ lines | User manual |

## 🎯 Quick File Finder

**I want to...**
- Learn what this project does → [README.md](README.md)
- Install the project → [SETUP_GUIDE.md](SETUP_GUIDE.md)
- Find quick answers → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- Navigate the project → [PROJECT_INDEX.md](PROJECT_INDEX.md)
- Verify my setup → [LAUNCH_CHECKLIST.md](LAUNCH_CHECKLIST.md)
- Learn how to use it → [CUSTOMER_GUIDE.md](CUSTOMER_GUIDE.md)
- Understand the code → [FILE_INDEX.md](FILE_INDEX.md)
- Modify the app → [app.py](app.py)
- Update dependencies → [requirements.txt](requirements.txt)
- Launch the app → [START_CHATBOT.ps1](START_CHATBOT.ps1) or [START_CHATBOT.bat](START_CHATBOT.bat)

---

**Last Updated:** April 2026
**Version:** 1.0
**Complete Index:** ✅ All files documented

