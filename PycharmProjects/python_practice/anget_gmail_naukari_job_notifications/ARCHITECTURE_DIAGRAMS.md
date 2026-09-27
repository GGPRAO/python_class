# 🎨 Visual Architecture & Diagrams

## System Architecture Diagram

```
┌────────────────────────────────────────────────────────────────────┐
│                        NAUKRI JOB MAIL AGENT                       │
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                   STREAMLIT UI (ai_streamlit.py)             │ │
│  │  ┌─────────────────────────┐  ┌──────────────────────────┐   │ │
│  │  │   Sidebar Configuration │  │    Main Display Area     │   │ │
│  │  │ • Gmail Address        │  │ • Email Cards            │   │ │
│  │  │ • Password Input       │  │ • Job Summaries          │   │ │
│  │  │ • Email Limit Slider   │  │ • Loading Spinners       │   │ │
│  │  │ • Fetch Button         │  │ • Error Messages         │   │ │
│  │  └─────────────────────────┘  └──────────────────────────┘   │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │            MODULE LAYER ARCHITECTURE                         │ │
│  │                                                              │ │
│  │  ┌─────────────────────────────────────────────────────┐   │ │
│  │  │ LAYER 1: FETCH (mail_config.py)                   │   │ │
│  │  │ fetch_naukri_emails(email, password, limit)       │   │ │
│  │  │ Returns: List[Dict] with subject & HTML body      │   │ │
│  │  └─────────────────────────────────────────────────────┘   │ │
│  │                     ▼                                       │ │
│  │  ┌─────────────────────────────────────────────────────┐   │ │
│  │  │ LAYER 2: CLEAN (clean_email.py)                   │   │ │
│  │  │ clean_emails(emails_data)                         │   │ │
│  │  │ Returns: List[Dict] with plain text body          │   │ │
│  │  └─────────────────────────────────────────────────────┘   │ │
│  │                     ▼                                       │ │
│  │  ┌─────────────────────────────────────────────────────┐   │ │
│  │  │ LAYER 3: SUMMARIZE (summarize_emails.py)          │   │ │
│  │  │ summarize_email(content)                          │   │ │
│  │  │ Returns: String with AI-generated summary         │   │ │
│  │  └─────────────────────────────────────────────────────┘   │ │
│  │                     ▼                                       │ │
│  │  ┌─────────────────────────────────────────────────────┐   │ │
│  │  │ LAYER 4: AGENT (convert_into_agent.py)            │   │ │
│  │  │ Future advanced automation features               │   │ │
│  │  └─────────────────────────────────────────────────────┘   │ │
│  │                                                              │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                              ▼                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │            EXTERNAL SERVICES                                 │ │
│  │                                                              │ │
│  │  Gmail IMAP         │         Ollama LLM                    │ │
│  │  (Port 993)         │         (Port 11434)                  │ │
│  │                                                              │ │
│  └──────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘
```

---

## Request-Response Cycle

```
USER INTERACTION
        │
        ├─► [Click "Fetch Jobs" Button]
        │
        └─► StreamLit Page Reloads
            │
            ├─► Validate Input
            │   ├─ Email address check
            │   └─ Password not empty
            │
            ├─► Call mail_config.fetch_naukri_emails()
            │   │
            │   ├─ Connect to Gmail via IMAP
            │   ├─ Login with credentials
            │   ├─ Search for FROM:"naukri"
            │   ├─ Fetch N most recent emails
            │   ├─ Extract subject & HTML body
            │   └─ Return: List[Dict]
            │
            ├─► Call clean_email.clean_emails()
            │   │
            │   ├─ For each email dict
            │   ├─ Parse HTML with BeautifulSoup
            │   ├─ Extract plain text
            │   └─ Return: List[Dict] cleaned
            │
            ├─► For each cleaned email:
            │   │
            │   ├─ Show Spinner: "Generating summary..."
            │   ├─ Call summarize_emails.summarize_email()
            │   │   │
            │   │   ├─ Create LLM prompt
            │   │   ├─ Call ollama.chat()
            │   │   ├─ Wait for LLM response
            │   │   └─ Return: Summary string
            │   │
            │   └─ Display in Expander Card
            │
            └─► Display Success Message
                ✅ Found N job notifications
```

---

## Email Processing Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│ RAW EMAIL (From Gmail IMAP)                                 │
├─────────────────────────────────────────────────────────────┤
│ Subject: Naukri Alert: Senior Python Developer (25 years)   │
│ Body: <html><body><p><b>Job: Senior Python Developer</b>... │
│       <p>Company: TechCorp Inc</p>...                        │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ CLEAN HTML (BeautifulSoup Processing)                       │
├─────────────────────────────────────────────────────────────┤
│ Subject: Naukri Alert: Senior Python Developer (25 years)   │
│ Body: Job: Senior Python Developer                          │
│       Company: TechCorp Inc                                  │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ LLM PROCESSING (Ollama - Qwen2 1.5B Model)                  │
├─────────────────────────────────────────────────────────────┤
│ Prompt: Extract job details:                                │
│   - Job Role                                                │
│   - Company                                                 │
│   - Location                                                │
│   - Experience                                              │
│                                                             │
│ Content: [Full cleaned email text]                          │
│ Model: qwen2:1.5b (Lightweight, ~2-5s per email)           │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ AI-GENERATED SUMMARY                                        │
├─────────────────────────────────────────────────────────────┤
│ Job Role: Senior Python Developer                           │
│ Company: TechCorp Inc                                       │
│ Location: Bangalore, India                                  │
│ Experience: 25 years                                        │
│ Skills: Python, FastAPI, PostgreSQL, Docker                │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ DISPLAYED IN STREAMLIT UI                                   │
├─────────────────────────────────────────────────────────────┤
│ 📧 Naukri Alert: Senior Python Developer (25 years)         │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ 🧠 AI Summary:                                          │ │
│ │                                                         │ │
│ │ Job Role: Senior Python Developer                      │ │
│ │ Company: TechCorp Inc                                  │ │
│ │ Location: Bangalore, India                             │ │
│ │ Experience: 25 years                                   │ │
│ │ Skills: Python, FastAPI, PostgreSQL, Docker            │ │
│ └─────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Component Dependencies

```
                    ai_streamlit.py
                    (Main Entry)
                          │
              ┌───────────┼───────────┐
              │           │           │
              ▼           ▼           ▼
        mail_config  clean_email  summarize_emails
              │           │           │
              ├─→ Gmail   ├─→ BeautifulSoup
              │  IMAP     │           │
              │  (Port    └─→ ollama.chat()
              │   993)        (Port 11434)
              │
         imaplib
         email
```

---

## State Management Flow

```
START
  │
  ├─ User Input State
  │  ├─ email_input (st.text_input)
  │  ├─ password_input (st.text_input)
  │  └─ email_limit (st.slider)
  │
  └─ Button Click State
     ├─ fetch_button triggered
     │  │
     │  ├─ Fetch Data
     │  │  └─ emails_data = fetch_naukri_emails()
     │  │
     │  ├─ Clean Data
     │  │  └─ cleaned_emails = clean_emails(emails_data)
     │  │
     │  ├─ Process Data
     │  │  ├─ FOR each cleaned_email:
     │  │  │   └─ summary = summarize_email(body)
     │  │  │
     │  │  └─ Display Results
     │  │
     │  └─ Show Success Message
     │
     └─ WAIT for next interaction
```

---

## Error Handling Tree

```
ERROR HANDLING FLOW
│
├─ INPUT VALIDATION
│  ├─ Email empty? → Show error "Please enter email"
│  └─ Password empty? → Show error "Please enter password"
│
├─ EMAIL FETCHING ERRORS
│  ├─ Connection failed? → Show error "Gmail connection failed"
│  ├─ Login failed? → Show error "Authentication failed"
│  └─ No emails found? → Show warning "No Naukri emails found"
│
├─ EMAIL CLEANING ERRORS
│  ├─ HTML parse error? → Fallback to raw text
│  └─ Encoding error? → Skip email and continue
│
└─ AI SUMMARIZATION ERRORS
   ├─ Ollama not running? → Show error "LLM service unavailable"
   ├─ Model not found? → Show error "Pull model: ollama pull llama3"
   └─ API timeout? → Show warning "Summarization timed out"
```

---

## Database-Free Architecture

```
┌─────────────────────────────────────────┐
│  SESSION-BASED STORAGE (Streamlit)      │
├─────────────────────────────────────────┤
│ • No database required                  │
│ • Data cleared on page refresh           │
│ • Real-time processing only              │
│ • Stateless between requests             │
└─────────────────────────────────────────┘
        ▼
┌─────────────────────────────────────────┐
│  PRODUCTION ENHANCEMENT (Optional)      │
├─────────────────────────────────────────┤
│ • Add SQLite for email history          │
│ • Cache summaries for repeat emails      │
│ • Store user preferences                 │
│ • Add export functionality               │
└─────────────────────────────────────────┘
```

---

## Scalability Potential

```
CURRENT ARCHITECTURE        →        FUTURE SCALABILITY
─────────────────────────────────────────────────────────

Single Instance             →        Multi-Instance Load Balancer
│                                    │
├─ One Streamlit app        →        ├─ Multiple Streamlit servers
├─ One user session         →        ├─ Session management
└─ Direct IMAP connection   →        └─ Connection pooling

                                    Database Backend
                                    │
                                    ├─ PostgreSQL/MySQL
                                    ├─ Redis Cache
                                    └─ Message Queue

                                    Advanced Features
                                    │
                                    ├─ Scheduled Jobs
                                    ├─ Email Webhooks
                                    ├─ Notifications
                                    └─ Analytics Dashboard
```

---

## Performance Characteristics

```
OPERATION                   TIME        BOTTLENECK
─────────────────────────────────────────────────────
Gmail IMAP Connect          ~500ms      Network
Email Fetch (5 emails)      ~2-3s       IMAP Protocol
HTML Parsing                ~100ms      CPU/Memory
AI Summarization            ~3-10s      LLM Processing
UI Rendering                ~500ms      Streamlit

TOTAL PER REQUEST           ~6-15s
```

---

## Technology Stack

```
┌─────────────────────────────────────┐
│         TECHNOLOGY STACK            │
├─────────────────────────────────────┤
│ Frontend:   Streamlit               │
│ Backend:    Python                  │
│ Email:      IMAP Protocol           │
│ Parsing:    BeautifulSoup           │
│ AI/ML:      Ollama + Llama3         │
│ Database:   None (Session-based)    │
│ DevOps:     Local Machine           │
└─────────────────────────────────────┘
```

---

## Network Communication Diagram

```
LOCAL MACHINE (Your Computer)
│
├─ OUTBOUND CONNECTIONS
│  ├─ Google: imap.gmail.com:993 (Gmail)
│  ├─ Localhost: 127.0.0.1:8501 (Streamlit UI)
│  └─ Localhost: 127.0.0.1:11434 (Ollama LLM)
│
└─ SECURITY
   ├─ SSL/TLS for Gmail (Port 993)
   ├─ HTTP for Local UI (Port 8501)
   └─ HTTP for Local LLM (Port 11434)
```

---

*Last Updated: 2026-04-25*
*Visual Architecture v1.0*

