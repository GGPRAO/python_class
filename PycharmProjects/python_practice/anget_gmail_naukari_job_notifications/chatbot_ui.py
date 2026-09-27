#!/usr/bin/env python3
"""
Interactive Chatbot UI for Naukri Job Notifications
Uses Streamlit to provide a ChatGPT-like interface for fetching and discussing job notifications.
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from gmail import get_chatbot_adapter
from datetime import datetime
import json

# Page config
st.set_page_config(
    page_title="💼 Naukri Job Assistant - ChatGPT Style",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI - ChatGPT style
st.markdown("""
<style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.75rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
        animation: fadeIn 0.3s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .chat-message.user {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        flex-direction: row-reverse;
        border-radius: 1rem;
    }
    .chat-message.assistant {
        background-color: #f5f5f5;
        border-left: 4px solid #667eea;
    }
    .chat-message.system {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
    }
    .message-content {
        flex: 1;
        line-height: 1.6;
    }
    .message-avatar {
        font-size: 1.5rem;
        min-width: 2.5rem;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .job-card {
        background: #f9f9f9;
        border: 1px solid #e0e0e0;
        border-radius: 0.5rem;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .job-role {
        font-weight: bold;
        color: #667eea;
        font-size: 1.1rem;
    }
    .job-company {
        color: #666;
        font-size: 0.95rem;
    }
    .job-details {
        font-size: 0.9rem;
        color: #888;
        margin-top: 0.5rem;
    }
    .filter-badge {
        display: inline-block;
        background: #e3f2fd;
        color: #1976d2;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.85rem;
        margin-right: 0.5rem;
        margin-bottom: 0.25rem;
    }
    .input-area {
        position: sticky;
        bottom: 0;
        background: white;
        padding: 1rem;
        border-top: 2px solid #f0f0f0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """🤖 **Welcome to Naukri Job Assistant!** 

I'm here to help you find the perfect job! You can ask me anything in natural language:

✨ **Example queries:**
- "Show me Python developer jobs in Bangalore"
- "Find jobs with 10-15 lpa salary"
- "Get me backend engineer roles in Mumbai"
- "Show all remote jobs for 5+ years experience"
- "Filter jobs by company TCS"
- "Find 3-5 years experience requirement jobs"

Just type naturally, and I'll search through your Naukri notifications to find matching opportunities!""",
            "timestamp": datetime.now()
        }
    ]

if "adapter" not in st.session_state:
    try:
        st.session_state.adapter = get_chatbot_adapter()
        st.session_state.adapter_ready = True
    except Exception as e:
        st.session_state.adapter_ready = False
        st.session_state.adapter_error = str(e)

if "search_history" not in st.session_state:
    st.session_state.search_history = []

# Header
col1, col2 = st.columns([4, 1])
with col1:
    st.title("💼 Naukri Job Assistant")
with col2:
    if st.session_state.adapter_ready:
        st.success("🟢 Connected")
    else:
        st.error("🔴 Disconnected")

st.markdown("---")

# Sidebar for settings and info
with st.sidebar:
    st.header("⚙️ Settings & Information")

    # Status check
    if st.session_state.adapter_ready:
        st.success("✅ Gmail Service Connected")
        status = st.session_state.adapter.get_status()
        st.write(f"📧 **Email:** `{status['email']}`")
        st.write(f"🔗 **Status:** `{status['status'].upper()}`")
    else:
        st.error(f"❌ Connection Error: {st.session_state.adapter_error}")

    st.markdown("---")

    # Quick settings
    st.subheader("⚡ Quick Settings")
    email_limit = st.slider(
        "📊 Emails to search",
        min_value=1,
        max_value=50,
        value=15,
        help="Number of recent emails to search through"
    )

    st.markdown("---")

    # Search history
    if st.session_state.search_history:
        st.subheader("📜 Recent Searches")
        for i, search in enumerate(st.session_state.search_history[-5:], 1):
            if st.button(f"{i}. {search[:40]}...", key=f"hist_{i}"):
                st.session_state.new_query = search
                st.rerun()

    st.markdown("---")

    # Chat controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "👋 Chat cleared! Ready to help. What job are you looking for?",
                    "timestamp": datetime.now()
                }
            ]
            st.rerun()

    with col2:
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()

    st.markdown("---")

    st.subheader("💡 Quick Examples")
    examples = [
        "Python developer in Bangalore",
        "Backend engineer 5+ years",
        "10-15 lpa salary jobs",
        "Remote work positions",
        "Frontend roles at TCS",
        "Full stack developer Mumbai"
    ]
    st.markdown("\n".join([f"• {ex}" for ex in examples]))

# Main chat area
st.subheader("💬 Job Search Chat")

# Display chat messages
chat_container = st.container(border=True, height=500)

with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user">
                <div class="message-avatar">👤</div>
                <div class="message-content">
                    <strong>You:</strong><br>
                    {message['content']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif message["role"] == "assistant":
            st.markdown(f"""
            <div class="chat-message assistant">
                <div class="message-avatar">🤖</div>
                <div class="message-content">
                    {message['content']}
                </div>
            </div>
            """, unsafe_allow_html=True)

# Input section
st.markdown("---")

col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Ask me anything about Naukri jobs...",
        placeholder="e.g., 'Python developer roles in Bangalore' or 'Show me 10-15 lpa jobs'",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("Send ➤", use_container_width=True, key="send_btn")

# Process user input
if send_button and user_input.strip():
    # Add user message to chat
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now()
    })

    # Add to search history
    if user_input not in st.session_state.search_history:
        st.session_state.search_history.append(user_input)

    response = None

    try:
        if not st.session_state.adapter_ready:
            response = "❌ **Gmail service is not connected.** Please check your configuration."

        else:
            # Parse user query
            query_info = st.session_state.adapter.parse_user_query(user_input)
            intent = query_info["intent"]
            criteria = query_info["criteria"]

            if intent == "status":
                # Status check
                status = st.session_state.adapter.get_status()
                response = f"""
✅ **Gmail Connection Status**

- **Connection:** {status['status'].upper()}
- **Email:** {status['email']}
- **Service:** {status['service']}
- **Authenticated:** {status['authenticated']}

Everything is working perfectly! You can search for jobs now.
"""

            elif intent == "help":
                response = """
🎯 **How to Use This Job Assistant**

**I understand natural language queries like:**

1. **By Role**
   - "Show me Python developer jobs"
   - "Find data scientist positions"
   - "Backend engineer roles"

2. **By Location**
   - "Jobs in Bangalore"
   - "Remote positions"
   - "Hybrid roles in Mumbai"

3. **By Salary**
   - "Jobs with 10-15 lpa salary"
   - "Roles paying 20+ lpa"
   - "Budget-friendly positions"

4. **By Experience**
   - "Jobs for 3-5 years experience"
   - "Fresher positions"
   - "Senior roles for 10+ years"

5. **By Company**
   - "Jobs at TCS"
   - "Roles from top companies"

6. **Combined Queries** (my favorite!)
   - "Python developer in Bangalore with 15-20 lpa salary"
   - "Remote backend engineer jobs for 2-4 years experience"
   - "Frontend developer roles in Mumbai at top companies"

💡 **Pro Tips:**
- Be specific with numbers (salaries, experience)
- Use natural language - I understand many variations
- Ask me to refine results if needed
- I can fetch up to 50 recent job emails

What job are you looking for?
"""

            elif intent == "search":
                # Smart job search with filtering
                with st.spinner("🔍 Searching through your job notifications..."):
                    result = st.session_state.adapter.search_jobs(
                        query=user_input,
                        limit=email_limit
                    )

                    if result["status"] == "success":
                        jobs = result.get("emails", [])
                        total = result.get("total_found", 0)
                        matched = result.get("count", 0)
                        criteria = result.get("criteria", {})

                        if not jobs:
                            response = f"""
❌ **No jobs found matching your criteria!**

I searched through {total} recent job notifications, but couldn't find matches for:
"""
                            for key, val in criteria.items():
                                response += f"\n- {key}: {val}"

                            response += """

💡 **Try:**
- Being less specific with filters
- Searching for different roles
- Increasing the email limit in settings
- Asking for all recent jobs
"""
                        else:
                            response = f"""
✅ **Found {matched} matching job(s)!**

"""
                            if criteria:
                                response += "**Filters Applied:**\n"
                                for key, val in criteria.items():
                                    response += f"  • {key.replace('_', ' ').title()}: {val}\n"
                                response += "\n"

                            response += "**Job Opportunities:**\n\n"

                            for i, job in enumerate(jobs[:10], 1):
                                role = job.get('role') or "Not Specified"
                                company = job.get('company', 'Unknown')
                                locations = ", ".join(job.get('locations', ['Not Specified']))

                                salary_info = ""
                                if job.get('salary'):
                                    sal = job['salary']
                                    salary_info = f"\n  💰 **Salary:** ₹{sal['min']:,} - ₹{sal['max']:,} LPA"

                                exp_info = ""
                                if job.get('experience'):
                                    exp = job['experience']
                                    exp_info = f"\n  📊 **Experience:** {exp['min']}-{exp['max']} years"

                                response += f"""
{i}. **{role}**
   🏢 Company: {company}
   📍 Location: {locations}{salary_info}{exp_info}

"""

                            if matched > 10:
                                response += f"\n📌 *Showing 10 out of {matched} matches*"

                            response += "\n\n💬 **Want to:**\n- Refine the search?\n- See more details?\n- Try different criteria?"

                    else:
                        response = f"❌ **Error:** {result.get('message', 'Unable to fetch jobs')}"

            else:
                # Default: treat as search
                with st.spinner("🔍 Searching..."):
                    result = st.session_state.adapter.search_jobs(
                        query=user_input,
                        limit=email_limit
                    )

                    if result["status"] == "success" and result.get("count", 0) > 0:
                        jobs = result.get("emails", [])
                        response = f"✅ Found {len(jobs)} job(s). Here are the top results:\n\n"

                        for i, job in enumerate(jobs[:5], 1):
                            role = job.get('role') or "Position"
                            company = job.get('company', 'Company')
                            response += f"{i}. **{role}** @ {company}\n"
                    else:
                        response = "🤔 I couldn't find jobs matching that description. Try being more specific or ask for help!"

    except Exception as e:
        response = f"❌ **Error:** {str(e)}\n\nPlease try again."

    # Add assistant response
    if response:
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now()
        })
        st.rerun()

# Footer
st.markdown("---")
st.caption("💼 Naukri Job Assistant v2.0 | Powered by Gmail, Streamlit & Intelligent Filtering")

