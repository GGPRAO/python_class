# 🗺️ Navigation & Architecture Guide

## Project Navigation Map (POM Structure)

```
NAUKRI JOB MAIL AGENT
│
├─ 📌 ENTRY POINT
│  └─ ai_streamlit.py (Main Web Application)
│
├─ 📋 MODULE LAYERS
│  ├─ Layer 1: Configuration & Fetching
│  │  └─ mail_config.py
│  │     └─ fetch_naukri_emails(email, password, limit)
│  │
│  ├─ Layer 2: Data Processing & Cleaning
│  │  └─ clean_email.py
│  │     ├─ clean_html(html)
│  │     └─ clean_emails(emails_data)
│  │
│  ├─ Layer 3: AI Intelligence
│  │  └─ summarize_emails.py
│  │     ├─ summarize_email(content)
│  │     └─ process_and_summarize(cleaned_emails)
│  │
│  └─ Layer 4: Advanced Features
│     └─ convert_into_agent.py (Future)
│
└─ 📦 DEPENDENCIES
   ├─ Streamlit (UI)
   ├─ Gmail API (Email Fetching)
   ├─ Ollama (LLM)
   └─ BeautifulSoup (HTML Parsing)
```

---

## 📊 Data Flow Diagram

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          USER INTERFACE (Streamlit)        ┃
┃  ✓ Input Gmail credentials & preferences  ┃
┃  ✓ Display results in expandable cards    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                       ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   LAYER 1: FETCH (mail_config.py)         ┃
┃  • Connect to Gmail via IMAP              ┃
┃  • Search for Naukri emails               ┃
┃  • Extract subject & HTML body            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        [emails_data: List[Dict]]
                       ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃   LAYER 2: CLEAN (clean_email.py)         ┃
┃  • Parse HTML content                     ┃
┃  • Remove tags & formatting               ┃
┃  • Extract plain text                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        [cleaned_emails: List[Dict]]
                       ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  LAYER 3: SUMMARIZE (summarize_emails.py) ┃
┃  • Send to Ollama LLM                     ┃
┃  • Extract job details                    ┃
┃  • Generate structured summary            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        [summaries: List[Str]]
                       ↓
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          BACK TO UI (Display)             ┃
┃  • Show job role, company, location       ┃
┃  • Format in expander cards               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

---

## 🔄 Function Call Hierarchy

```
ai_streamlit.main()
│
├─ st.title()                              [Display title]
├─ st.sidebar inputs                       [Get user input]
│
└─ IF fetch_button clicked:
   │
   ├─ mail_config.fetch_naukri_emails()    [Fetch raw emails]
   │  ├─ imaplib.IMAP4_SSL()               [Connect to Gmail]
   │  ├─ mail.search()                     [Find Naukri emails]
   │  ├─ mail.fetch()                      [Download email content]
   │  └─ email.message_from_bytes()        [Parse email structure]
   │
   ├─ clean_email.clean_emails()           [Clean HTML content]
   │  ├─ BeautifulSoup()                   [Parse HTML]
   │  └─ soup.get_text()                   [Extract text]
   │
   └─ FOR each email:
      ├─ summarize_emails.summarize_email()[Generate AI summary]
      │  ├─ ollama.chat()                  [Call LLM]
      │  └─ response["message"]["content"] [Get summary]
      │
      └─ st.expander()                     [Display result]
         ├─ st.markdown()                  [Show subject]
         └─ st.write()                     [Show summary]
```

---

## 📝 Module Specifications

### 1️⃣ **ai_streamlit.py** (UI Layer)
**Role:** User Interface & Orchestration

| Component | Purpose |
|-----------|---------|
| Sidebar | Email credentials input |
| Buttons | Trigger fetch operation |
| Expanders | Display email summaries |
| Spinners | Show loading status |

**Key Functions:**
- Page configuration
- User input handling
- Data coordination
- Result display

---

### 2️⃣ **mail_config.py** (Fetch Layer)
**Role:** Gmail Integration

| Function | Input | Output |
|----------|-------|--------|
| `fetch_naukri_emails()` | email, password, limit | List[Dict] |

**Dictionary Structure:**
```python
{
    "subject": "Naukri Job Alert: Python Developer",
    "body": "<html>...job details...</html>"
}
```

**Error Handling:**
- Connection failures
- Login errors
- No emails found

---

### 3️⃣ **clean_email.py** (Processing Layer)
**Role:** HTML Parsing & Text Extraction

| Function | Input | Output |
|----------|-------|--------|
| `clean_html()` | HTML string | Plain text |
| `clean_emails()` | emails_data | cleaned_emails |

**Transformations:**
```
<html><body><p>Job: Developer</p></body></html>
                    ↓
                Job: Developer
```

---

### 4️⃣ **summarize_emails.py** (Intelligence Layer)
**Role:** AI-Powered Summarization

| Function | Input | Output |
|----------|-------|--------|
| `summarize_email()` | Email body text | AI Summary |
| `process_and_summarize()` | cleaned_emails | Prints summaries |

**AI Configuration:**
- **Model:** Qwen2 1.5B (lightweight, fast)
- **Speed:** ~2-5 seconds per email
- **Memory:** ~3GB required
- **Accuracy:** High for job extraction

**AI Extraction Pattern:**
```
Extract job details from this email:
- Job Role
- Company
- Location
- Experience
```

---

## 🎯 Usage Scenarios

### Scenario 1: Quick Job Check
```
User clicks "Fetch Jobs" 
→ Fetches 5 latest Naukri emails 
→ Displays quick summaries 
→ User reads important details
```

### Scenario 2: Detailed Analysis
```
User sets limit to 20 emails 
→ Fetches all recent jobs 
→ Generates full AI summaries 
→ Expands for detailed information
```

### Scenario 3: Automated Processing
```
Script mode (convert_into_agent.py) 
→ Runs without UI 
→ Processes emails automatically 
→ Exports results
```

---

## 🔌 Integration Points

### External APIs
- **Gmail IMAP** - Port 993
- **Ollama API** - Port 11434 (default)

### Python Libraries
- `imaplib` - Email protocol
- `email` - Email parsing
- `beautifulsoup4` - HTML parsing
- `ollama` - LLM client
- `streamlit` - Web framework

---

## 🧪 Testing Points

Each module can be tested independently:

```python
# Test mail_config
emails = fetch_naukri_emails("email@gmail.com", "password", 5)
assert len(emails) > 0

# Test clean_email
cleaned = clean_emails(emails)
assert "html" not in cleaned[0]["body"]

# Test summarize_emails
summary = summarize_email(cleaned[0]["body"])
assert len(summary) > 0
```

---

## 🚀 Performance Considerations

| Layer | Bottleneck | Optimization |
|-------|-----------|--------------|
| Fetch | Gmail IMAP latency | Cache results |
| Clean | HTML parsing time | Batch processing |
| Summarize | LLM response time | Parallel requests |
| UI | Rendering | Lazy loading |

---

## 📚 Quick Reference

### Start Application
```bash
streamlit run ai_streamlit.py
```

### Test Individual Module
```bash
python -m mail_config
python -m clean_email
python -m summarize_emails
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### View Project Structure
```bash
tree /F
```

---

## 🎓 Learning Path

1. **Understand Email Fetching** → Study `mail_config.py`
2. **Learn Text Processing** → Review `clean_email.py`
3. **Explore AI Integration** → Examine `summarize_emails.py`
4. **Master UI Creation** → Analyze `ai_streamlit.py`
5. **Build Advanced Features** → Develop `convert_into_agent.py`

---

## 📞 Debug Checklist

- [ ] Gmail credentials correct?
- [ ] Ollama service running?
- [ ] IMAP enabled in Gmail?
- [ ] Dependencies installed?
- [ ] Firewall blocking connections?
- [ ] API rate limits exceeded?
- [ ] Model file downloaded?

---

*Last Updated: 2026-04-25*
*Version: 1.0*

