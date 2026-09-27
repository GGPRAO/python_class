# QUICK REFERENCE CARD - CLI Chatbot

## ⚡ START HERE

### Run the Chatbot:
```bash
python chatbot_cli.py
```

### Or Double-Click:
```
start_chatbot.bat
```

---

## 💬 AVAILABLE COMMANDS

| Command | Purpose |
|---------|---------|
| `help` | Show all commands |
| `examples` | Show 10 example queries |
| `status` | Check Gmail connection |
| `settings` | Show current settings |
| `limit N` | Set email limit (1-50) |
| `clear` | Clear chat history |
| `exit` | Quit chatbot |

---

## 🎯 EXAMPLE QUERIES

### Simple (Single Filter)
```
Python developer jobs
Jobs in Bangalore
15-20 lpa salary
Remote positions
5+ years experience
TCS jobs
```

### Intermediate (2-3 Filters)
```
Python developer in Bangalore
Backend engineer 15-20 lpa
Remote jobs 5+ years
Frontend at TCS
```

### Advanced (All 5 Filters!)
```
Python developer in Bangalore with 15-20 lpa and 3-5 years
Backend engineer remote 20 lpa 5+ years
Frontend developer Mumbai 10-15 lpa 2-4 years
```

---

## 🧭 NAVIGATION

```
start_chatbot.bat        ← Click to run (Windows)
chatbot_cli.py           ← Run with Python
test_cli_chatbot.py      ← Test first
CLI_SOLUTION.md          ← Detailed guide
PYARROW_ERROR_FIXED.md   ← Solution info
```

---

## ✨ FILTERS AVAILABLE

### By Role
```
"Python developer"
"Backend engineer"
"Data scientist"
"DevOps engineer"
Any technical role
```

### By Location
```
"Bangalore"
"Mumbai"
"Remote"
"Hybrid"
"Pune"
Any Indian city
```

### By Salary
```
"10-15 lpa"
"20 lpa"
"15-20 lpa"
"₹10 lakh"
Any range
```

### By Experience
```
"5+ years"
"3-5 years"
"2 years"
"Fresher"
Any requirement
```

### By Company
```
"TCS"
"Infosys"
"Google"
"Amazon"
Any company name
```

---

## ⚙️ SETTINGS

### Email Limit
```
limit 5      → Quick search (few results)
limit 15     → Default (balanced)
limit 30     → More results
limit 50     → All results (comprehensive)
```

### Check Settings
```
settings     → Show current settings
status       → Check Gmail connection
```

---

## 🧪 TEST FIRST (Optional)

```bash
python test_cli_chatbot.py
```

Expected output:
```
✅ ALL TESTS PASSED!
🚀 CLI Chatbot is ready to use!
```

---

## 📊 FEATURES

| Feature | Status |
|---------|--------|
| Natural Language | ✅ |
| Multi-Filter | ✅ |
| Job Extraction | ✅ |
| Email Search | ✅ |
| Result Formatting | ✅ |
| Error Handling | ✅ |
| Performance | ⚡ |

---

## 🔴 TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| No jobs found | `limit 30` |
| Gmail error | `status` |
| See help | `help` |
| Clear history | `clear` |
| Exit | `exit` |

---

## 📋 FILE STRUCTURE

```
anget_gmail_naukari_job_notifications/
├── chatbot_cli.py              ← Main (RUN THIS!)
├── start_chatbot.bat           ← Windows launcher
├── test_cli_chatbot.py         ← Test suite
├── CLI_SOLUTION.md             ← Guide
├── gmail/
│   ├── job_filter.py           ← Filtering engine
│   ├── chatbot_adapter.py      ← Adapter
│   └── ...other files
└── ...other files
```

---

## 🎮 TYPICAL SESSION

```
$ python chatbot_cli.py

Welcome! Type queries naturally.

You: examples
[Shows 10 examples]

You: Python developer in Bangalore
✅ Found 3 jobs!
[Shows results with details]

You: limit 30
✅ Email limit set to 30!

You: Backend engineer 20 lpa
✅ Found 1 job!
[Shows result]

You: exit
Goodbye!
```

---

## 💡 TIPS & TRICKS

### Tip 1: Use natural language
```
Good:  "Python developer Bangalore"
Bad:   "developer bangalore python"
```

### Tip 2: Combine filters
```
"Role + Location"
"Role + Salary"
"All 5 filters!"
```

### Tip 3: Increase results
```
limit 10  → 10 emails
limit 30  → 30 emails
limit 50  → 50 emails (max)
```

### Tip 4: Try examples first
```
"examples" command shows 10 working queries
```

---

## ✅ STATUS

```
Error: ✅ FIXED
Working: ✅ YES
Ready: ✅ NOW
Documentation: ✅ COMPLETE
```

---

## 🚀 START NOW!

```bash
python chatbot_cli.py
```

Then try:
```
Python developer in Bangalore
```

**That's it! Happy job hunting! 🎉**

---

**Quick Reference v1.0**
**April 25, 2026**
**Status: ✅ Production Ready**

