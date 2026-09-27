# 📋 File Index - Maths Problem Solver Bot

Detailed description of each file in the project.

## Application Files

### app.py
**Type**: Python Source Code  
**Size**: ~220 lines  
**Description**: Main Streamlit application for the Maths Problem Solver Bot

**Key Components**:
- Page configuration and styling
- Sidebar preferences (difficulty, category, learning style)
- Chat interface and history
- User input processing
- Ollama AI integration
- Quick example buttons

**Key Functions**:
- `st.set_page_config()` - Configure Streamlit page
- `ollama.chat()` - Send query to AI model
- Chat message display and management

**When You Need It**:
- To run the bot: `streamlit run app.py`
- To understand the core logic
- To customize the application

**How to Edit**:
- Change model: Line 140 `model="qwen2:1.5b"`
- Change colors: Lines 19-45 (CSS styling)
- Add categories: Lines 75-88 (selectbox options)

### requirements.txt
**Type**: Python Dependencies File  
**Size**: 3 packages  
**Description**: Lists all required Python packages with versions

**Contents**:
```
streamlit==1.28.1      (Web UI framework)
ollama==0.0.12         (AI model interface)
python-dateutil==2.8.2 (Date/time utilities)
```

**When You Need It**:
- Initial setup: `pip install -r requirements.txt`
- Updating packages: `pip install --upgrade -r requirements.txt`
- Sharing project: For dependency management

**How to Edit**:
- Add packages: `pip install <package>` then update file
- Remove packages: Delete the line
- Update version: Change version number

## Documentation Files

### README.md
**Type**: Markdown Documentation  
**Size**: ~350 lines  
**Description**: Complete project documentation and user guide

**Sections**:
- Project overview and features
- Comprehensive feature list
- Installation instructions (3 options)
- Quick start guide
- Detailed how-to-use guide
- Categories explained (8 types)
- Learning levels (5 levels)
- Troubleshooting guide
- System requirements
- Advanced features

**When You Need It**:
- First time using the project
- Understanding all features
- Detailed setup instructions
- Troubleshooting complex issues

**Reading Time**: 15-20 minutes

### SETUP_GUIDE.md
**Type**: Markdown Tutorial  
**Size**: ~300 lines  
**Description**: Step-by-step installation and configuration guide

**Sections**:
- System requirements (min/recommended)
- Python installation (Windows/Mac/Linux)
- Ollama installation and setup
- Dependency installation
- Model pulling and verification
- Project setup
- Configuration options
- Troubleshooting
- Performance tips
- Advanced: Different models

**When You Need It**:
- Initial setup from scratch
- Setting up on multiple computers
- Resolving installation issues

**Reading Time**: 20-30 minutes

### QUICK_REFERENCE.md
**Type**: Markdown Cheat Sheet  
**Size**: ~200 lines  
**Description**: Quick reference for common tasks and examples

**Sections**:
- Fast setup (3 steps)
- Math categories with examples (8 types)
- Difficulty levels quick reference
- Learning styles quick reference
- Keyboard shortcuts
- Troubleshooting quick fixes
- Mathematical symbols reference
- Common formulas
- Supported problem types

**When You Need It**:
- Quick lookup during use
- Common math examples
- Quick troubleshooting
- Formula reference

**Reading Time**: 5-10 minutes

### LAUNCH_CHECKLIST.md
**Type**: Markdown Checklist  
**Size**: ~250 lines  
**Description**: Pre-launch verification and testing checklist

**Sections**:
- Pre-launch checklist (system & software)
- Launch steps (3 methods)
- Testing procedures
- Troubleshooting during launch
- Post-launch checklist
- Daily use checklist
- Performance optimization
- Emergency reset
- Common commands

**When You Need It**:
- Before each launch (verify systems)
- Testing after installation
- Daily startup routine
- Troubleshooting launch issues

**Reading Time**: 5-10 minutes

### PROJECT_INDEX.md
**Type**: Markdown Index  
**Size**: ~300 lines  
**Description**: Complete project index and navigation guide

**Sections**:
- Documentation overview
- Application files description
- Project structure diagram
- Quick navigation guide
- Reading order by use case
- Key features by category
- File details and statistics
- Common tasks and how-tos
- Search and help guides
- Learning paths
- Update checklist

**When You Need It**:
- Finding specific information
- Understanding project structure
- Navigation between documents
- Quick task reference

**Reading Time**: 5 minutes

## Launch Scripts

### START_CHATBOT.bat
**Type**: Windows Batch Script  
**Size**: ~50 lines  
**OS**: Windows only  
**Description**: Automated launcher for Windows Command Prompt

**Features**:
- Checks for Python installation
- Checks for Ollama service
- Installs/updates dependencies
- Launches the Streamlit app
- Colored output for readability
- Error checking at each step

**How to Use**:
1. Double-click the file, OR
2. Run: `START_CHATBOT.bat` in Command Prompt

**Requirements**:
- Windows operating system
- Python in PATH
- Command Prompt or PowerShell

### START_CHATBOT.ps1
**Type**: Windows PowerShell Script  
**Size**: ~50 lines  
**OS**: Windows only  
**Description**: Enhanced launcher for Windows PowerShell

**Features**:
- Python version checking
- Ollama process detection
- Automatic dependency installation
- Beautiful colored output
- Detailed status messages
- Service running status

**How to Use**:
1. Open PowerShell in the project folder
2. Run: `.\START_CHATBOT.ps1`

**Requirements**:
- Windows operating system
- PowerShell (built-in on Windows 7+)
- Python installed

**Note**: May need to run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned` first

## Project Statistics

| File | Type | Lines | Purpose |
|------|------|-------|---------|
| app.py | Python | 220 | Main application |
| requirements.txt | Config | 3 | Dependencies |
| README.md | Docs | 350 | Full guide |
| SETUP_GUIDE.md | Docs | 300 | Setup steps |
| QUICK_REFERENCE.md | Docs | 200 | Quick tips |
| LAUNCH_CHECKLIST.md | Docs | 250 | Verification |
| PROJECT_INDEX.md | Docs | 300 | Navigation |
| FILE_INDEX.md | Docs | 200 | File details |
| START_CHATBOT.bat | Script | 50 | Windows launcher |
| START_CHATBOT.ps1 | Script | 50 | PS launcher |
| **TOTAL** | | **1973** | |

## File Dependencies

```
START_CHATBOT.bat
    ↓ (launches)
app.py ← requires → requirements.txt
    ↓ (connects to)
Ollama (external service)
```

## File Organization by Purpose

### For Running the Bot
- `app.py` - Main application
- `START_CHATBOT.bat` or `START_CHATBOT.ps1` - Launcher
- `requirements.txt` - Dependencies

### For Setup
- `SETUP_GUIDE.md` - Installation guide
- `requirements.txt` - Package list

### For Using the Bot
- `README.md` - Features and usage
- `QUICK_REFERENCE.md` - Quick examples
- `LAUNCH_CHECKLIST.md` - Daily checklist

### For Navigation
- `PROJECT_INDEX.md` - Overall index
- `FILE_INDEX.md` - File descriptions (this file)

## Key File Sizes

- **Smallest**: `requirements.txt` (3 lines)
- **Largest**: `README.md` (350+ lines)
- **Most Important**: `app.py` (the actual bot)
- **Most Helpful**: `README.md` (complete guide)

## File Edit Frequency

| Frequency | Files |
|-----------|-------|
| Never (after setup) | requirements.txt, launch scripts |
| Rarely | app.py (only for customization) |
| Often (reference) | QUICK_REFERENCE.md |
| During setup | SETUP_GUIDE.md, LAUNCH_CHECKLIST.md |

## File Reading Time Summary

| File | Read Time | Priority |
|------|-----------|----------|
| README.md | 15-20 min | HIGH |
| SETUP_GUIDE.md | 20-30 min | HIGH |
| QUICK_REFERENCE.md | 5-10 min | MEDIUM |
| LAUNCH_CHECKLIST.md | 5-10 min | MEDIUM |
| PROJECT_INDEX.md | 5 min | LOW |
| FILE_INDEX.md | 5 min | LOW |

## File Relationships

### Documentation Reading Path
```
README.md (overview)
    ↓
SETUP_GUIDE.md (installation)
    ↓
LAUNCH_CHECKLIST.md (verification)
    ↓
QUICK_REFERENCE.md (usage tips)
```

### File Dependencies for Running
```
requirements.txt (defines dependencies)
    ↓ (installed with pip)
Python packages installed
    ↓ (used by)
app.py (the bot application)
    ↓ (connects to)
Ollama service
```

## How to Use Each File

### app.py
**Action**: Run it
```bash
streamlit run app.py
```

**Edit it**: For customization (advanced)

### requirements.txt
**Action**: Install from it
```bash
pip install -r requirements.txt
```

**Edit it**: When adding new packages

### README.md
**Action**: Read it for complete information

**Share it**: With others learning about the project

### SETUP_GUIDE.md
**Action**: Follow it step-by-step during initial setup

**Reference it**: If setup issues occur

### QUICK_REFERENCE.md
**Action**: Keep it handy while using the bot

**Reference it**: For problem examples and formulas

### LAUNCH_CHECKLIST.md
**Action**: Check items before launching

**Reference it**: For troubleshooting

### PROJECT_INDEX.md
**Action**: Navigate the project

**Reference it**: To find specific information

### START_CHATBOT.bat / .ps1
**Action**: Double-click (bat) or run in PowerShell (ps1)

**Never edit**: Unless you know batch/PowerShell scripting

## Backup Recommendations

### Essential Files (Backup These)
- `app.py` - Your customized version
- `requirements.txt` - Your dependency list

### Documentation (Optional to Backup)
- All `.md` files - For reference

### Not Worth Backing Up
- `START_CHATBOT.bat/ps1` - Can be easily recreated
- Generated files - Created by the bot

## Troubleshooting Files

**If you see errors, check**:
1. `README.md` → Troubleshooting section
2. `LAUNCH_CHECKLIST.md` → Troubleshooting section
3. `QUICK_REFERENCE.md` → Troubleshooting section

**By issue type**:
- Installation → `SETUP_GUIDE.md`
- Running → `LAUNCH_CHECKLIST.md`
- Using → `README.md`
- Quick fix → `QUICK_REFERENCE.md`

## File Version Information

| File | Version | Last Updated |
|------|---------|--------------|
| All files | 1.0 | April 2026 |

---

**Total Project Size**: ~30 KB (documentation + code)

**Recommended Reading Order**:
1. README.md (15 min)
2. SETUP_GUIDE.md (25 min)
3. LAUNCH_CHECKLIST.md (5 min)
4. Use the bot!


