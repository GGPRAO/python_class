# 🚀 ChatGPT-Like Email Assistant - Installation & Usage Flowchart

## 📋 Installation Flowchart

```
START
  ↓
[Check Python 3.8+]
  ├─ YES → Continue
  └─ NO  → Install Python from python.org
           └→ Continue
  ↓
[Install Dependencies]
  Command: pip install -r requirements.txt
  └→ Wait for installation
  ↓
[Get Gmail App Password]
  1. Go to: https://myaccount.google.com/apppasswords
  2. Select "Mail" + "Windows Computer"
  3. Copy 16-character password
  └→ Have password ready
  ↓
[Optional: Create .env file]
  File content:
    GMAIL_USER=your_email@gmail.com
    GMAIL_PASSWORD=your_app_password
  └→ Or just use console input
  ↓
[Verify Installation]
  Command: python verify_chatgpt_setup.py
  └→ Should show ✅ ALL CHECKS PASSED!
  ↓
✅ READY TO USE!
```

---

## 🎮 Usage Flowchart - CLI Interface

```
START
  ↓
[Run Program]
  Command: python chatgpt_like_interface.py
  └→ Shows welcome screen
  ↓
[Choose Action]
  ├─ Type Query → Search emails
  │  └─ e.g., "Python developer Bangalore"
  │     ↓
  │  [Process Query]
  │     ↓
  │  [Display Results]
  │     ↓
  │  [Continue?] → YES → Back to [Choose Action]
  │              → NO  → [Exit]
  │
  ├─ Type Command → Execute command
  │  ├─ help     → Show commands
  │  ├─ examples → Show examples
  │  ├─ limit N  → Set search depth
  │  ├─ status   → Check Gmail
  │  ├─ history  → Show history
  │  ├─ clear    → Clear history
  │  └─ exit     → Quit
  │
  └─ Invalid → Show error, try again

END
```

---

## 🌐 Usage Flowchart - Web Interface

```
START
  ↓
[Run Program]
  Command: python chatgpt_web_interface.py
  └→ Server starts
  ↓
[Open Browser]
  URL: http://localhost:5000
  └→ Chat interface loads
  ↓
[User Interface Ready]
  ┌─────────────────────────────┐
  │    Chat Window              │
  │  ┌─────────────────────┐    │
  │  │  Chat History       │    │
  │  │                     │    │
  │  │  Bot: Hi!           │    │
  │  │  User: ...          │    │
  │  └─────────────────────┘    │
  │  ┌─────────────────────┐    │
  │  │ Input: [Text] [Send]│    │
  │  └─────────────────────┘    │
  └─────────────────────────────┘
  ↓
[User Types Query]
  ├─ Type naturally
  └─ Examples:
     • "Python developer"
     • "Remote jobs"
     • "15-20 lpa"
  ↓
[Send Message]
  Click Send or Press Enter
  ↓
[Processing]
  Show: 🤔 Processing...
  ↓
[Display Results]
  Show emails matching query
  ↓
[Continue or Exit]
  ├─ Continue → Type another query
  └─ Exit     → Close browser

END
```

---

## 🎯 Query Building Guide

```
Build Your Query
  ↓
[Step 1: Choose a Role (Optional)]
  ├─ Python developer
  ├─ Backend engineer
  ├─ Frontend developer
  ├─ Data scientist
  ├─ DevOps engineer
  └─ Or any role...
  ↓
[Step 2: Choose Location (Optional)]
  ├─ Bangalore
  ├─ Mumbai
  ├─ Remote
  ├─ Pune
  ├─ Delhi
  └─ Or any city...
  ↓
[Step 3: Choose Salary (Optional)]
  ├─ 10-15 lpa
  ├─ 15-20 lpa
  ├─ 20-25 lpa
  ├─ 25+ lpa
  └─ Or any range...
  ↓
[Step 4: Choose Experience (Optional)]
  ├─ Fresher
  ├─ 1-2 years
  ├─ 2-4 years
  ├─ 5+ years
  └─ Or any requirement...
  ↓
[Step 5: Choose Company (Optional)]
  ├─ Google
  ├─ TCS
  ├─ Amazon
  ├─ Infosys
  └─ Or any company...
  ↓
[Build Final Query]
  Combine selected criteria naturally
  
  Examples:
  • Role only: "Python jobs"
  • Role + Location: "Backend in Mumbai"
  • Role + Salary: "Frontend 20 lpa"
  • All 5: "Python developer Mumbai 15-20 lpa 3-5 years"
  ↓
✅ Ready to Search!
```

---

## 🆘 Troubleshooting Decision Tree

```
Problem Occurred?
  ↓
[Identify Issue]
  ├─ Installation Issue
  │  └─ [Go to Installation Troubleshooting]
  │
  ├─ Gmail Issue
  │  └─ [Go to Gmail Troubleshooting]
  │
  ├─ Search Issue
  │  └─ [Go to Search Troubleshooting]
  │
  └─ Other Issue
     └─ [Go to General Troubleshooting]

INSTALLATION TROUBLESHOOTING:
  ├─ "Module not found"
  │  └─ Solution: pip install -r requirements.txt --upgrade
  │
  ├─ "Python not found"
  │  └─ Solution: Install Python 3.8+ from python.org
  │
  └─ "pip not working"
     └─ Solution: python -m pip install --upgrade pip

GMAIL TROUBLESHOOTING:
  ├─ "Gmail connection failed"
  │  └─ Solution: Check app password in .env or console
  │
  ├─ "Gmail login error"
  │  └─ Solution: Verify 2-Factor Auth is enabled
  │
  └─ "Connection timeout"
     └─ Solution: Check internet connection, try again

SEARCH TROUBLESHOOTING:
  ├─ "No results found"
  │  └─ Solution: Try 'limit 50' to search more emails
  │
  ├─ "Results too many"
  │  └─ Solution: Try 'limit 10' to limit results
  │
  └─ "Slow search"
     └─ Solution: Lower limit value, try fewer criteria

GENERAL TROUBLESHOOTING:
  ├─ "Port already in use"
  │  └─ Solution: Close other apps or change port
  │
  ├─ "Cannot connect to Gmail"
  │  └─ Solution: Verify credentials, try 'status'
  │
  └─ "Still having issues?"
     └─ Solution: Run verify_chatgpt_setup.py
```

---

## 📊 Command Flow

```
User Input
  ↓
[Analyze Input]
  ├─ Special Command?
  │  ├─ YES → Execute command
  │  │        ├─ help   → Show commands
  │  │        ├─ limit  → Update settings
  │  │        ├─ status → Check Gmail
  │  │        └─ ...
  │  │
  │  └─ NO → Continue
  │
  ↓
[Process as Query]
  ├─ Extract criteria
  │  ├─ Role
  │  ├─ Location
  │  ├─ Salary
  │  ├─ Experience
  │  └─ Company
  │
  ↓
[Search Emails]
  ├─ Fetch from Gmail
  ├─ Filter based on criteria
  ├─ Format results
  │
  ↓
[Display Results]
  ├─ Show count
  ├─ Show email details
  ├─ Show job info
  │
  ↓
[Add to History]
  ├─ Record query
  ├─ Record results
  │
  ↓
[Ready for Next Input]
```

---

## 🎯 Quick Reference Flowchart

```
┌─────────────────────────────────────────────┐
│     ChatGPT-Like Email Assistant v3.0       │
├─────────────────────────────────────────────┤
│                                             │
│  Install:                                   │
│    pip install -r requirements.txt          │
│                                             │
│  CLI:                                       │
│    python chatgpt_like_interface.py          │
│                                             │
│  Web:                                       │
│    python chatgpt_web_interface.py           │
│    Open: http://localhost:5000              │
│                                             │
│  Verify:                                    │
│    python verify_chatgpt_setup.py            │
│                                             │
│  Example Query:                             │
│    "Python developer Bangalore 15-20 lpa"   │
│                                             │
│  Commands:                                  │
│    help, examples, limit, status, exit      │
│                                             │
│  Documentation:                             │
│    CHATGPT_QUICK_START.md (read first!)    │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ⏱️ Time Estimate

```
Installation:
  ├─ Install Python: 5 min (if needed)
  ├─ Install dependencies: 3 min
  ├─ Get App Password: 2 min
  └─ Total: 10 min

First Use:
  ├─ Run program: < 1 sec
  ├─ First search: 5 sec
  └─ Total: < 10 sec

Typical Usage:
  ├─ Query time: 2-5 sec
  ├─ Per search: < 10 sec
  └─ Total time for 5 searches: < 1 min
```

---

## 🎓 Learning Path

```
Level 1: Beginner
  ├─ Read: CHATGPT_QUICK_START.md
  ├─ Do: Run CLI interface
  ├─ Try: Simple queries
  └─ Time: 15 min

Level 2: Intermediate
  ├─ Read: CHATGPT_SETUP_GUIDE.md
  ├─ Do: Configure settings
  ├─ Try: Complex queries
  └─ Time: 30 min

Level 3: Advanced
  ├─ Read: CHATGPT_COMPLETE_README.md
  ├─ Do: Explore web interface
  ├─ Try: All features
  └─ Time: 60 min

Level 4: Expert
  ├─ Read: Source code
  ├─ Do: Customize
  ├─ Try: Extend features
  └─ Time: Variable
```

---

## ✅ Success Checklist

```
□ Python 3.8+ installed
□ Dependencies installed
□ Gmail App Password ready
□ .env file created (optional)
□ verify_chatgpt_setup.py passes
□ Program runs without errors
□ Can search emails
□ Results display correctly
□ Commands work
□ Documentation reviewed

✅ All done? You're ready to use it!
```

---

## 🎉 You're Ready!

```
Ready to Start?
  ↓
1. Open terminal/command prompt
2. Go to project folder
3. Run: python chatgpt_like_interface.py
4. Type: Python developer Bangalore
5. See results!

That's it! Happy job hunting! 🚀
```

---

**Created: April 25, 2026**
**Version: 3.0**
**Status: ✅ Ready to Use**

