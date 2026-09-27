# 🚀 HOW TO RUN - SIMPLE GUIDE

## Fastest Way to Run (Copy & Paste)

Open Command Prompt and run:

```bash
cd C:\Users\USER\PycharmProjects\python_practice
python anget_gmail_naukari_job_notifications/gmail/run_quick_test.py
```

**That's it!** The test will run and show results.

---

## Three Ways to Use

### Way 1: Direct Python Command (Fastest)
```bash
python -c "from gmail import get_chatbot_adapter; print(get_chatbot_adapter().get_status())"
```

### Way 2: Run Test Suite
```bash
python anget_gmail_naukari_job_notifications/gmail/test_gmail_module.py
```

### Way 3: Run Quick Test
```bash
python anget_gmail_naukari_job_notifications/gmail/run_quick_test.py
```

---

## In Your Python Code

```python
from gmail import get_chatbot_adapter

# Create adapter
adapter = get_chatbot_adapter()

# Fetch jobs
result = adapter.fetch_jobs(limit=5)
print(result['message'])

# Check status
status = adapter.get_status()
print(f"Connected: {status['email']}")

# Get options
options = adapter.get_options()
print(options)
```

---

## What You'll See

When you run it, you'll see output like:

```
✅ Module imported successfully!
✅ Adapter created!
✅ Status: connected
   Email: ggpsmo@gmail.com
   Authenticated: True
✅ Available commands:
   • Fetch Naukri Jobs
   • Get Status
✅ ALL TESTS PASSED!
```

---

## Three Quick Commands

**1. Fetch Jobs:**
```python
from gmail import fetch_jobs_for_chatbot
jobs = fetch_jobs_for_chatbot(limit=5)
```

**2. Get Status:**
```python
from gmail import get_gmail_status
status = get_gmail_status()
```

**3. Get Options:**
```python
from gmail import get_gmail_options
options = get_gmail_options()
```

---

## That's All!

You now have everything you need to use the Gmail module. 

**Next:** Read `gmail/QUICK_REFERENCE.md` for more details.

Good luck! 🎉

