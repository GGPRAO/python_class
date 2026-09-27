#!/usr/bin/env python3
"""
Simple Gmail Naukri Job Chatbot UI
A clean, straightforward Streamlit app for fetching and viewing job notifications.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Naukri Job Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
        padding: 0.75rem;
        font-size: 1rem;
        font-weight: 600;
    }
    .job-card {
        padding: 1.5rem;
        border-left: 4px solid #1f77b4;
        background-color: #f8f9fa;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #e8f5e9;
        color: #2e7d32;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'jobs' not in st.session_state:
    st.session_state.jobs = None
if 'status' not in st.session_state:
    st.session_state.status = None
if 'error' not in st.session_state:
    st.session_state.error = None

# Header
st.title("💼 Naukri Job Assistant")
st.markdown("Fetch and view your latest Naukri job notifications")
st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    limit = st.slider(
        "Number of emails to fetch",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    st.divider()
    st.markdown("### 📋 Info")
    st.info("This chatbot fetches job notifications from your Gmail inbox using hardcoded credentials.")

# Main content area
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔄 Fetch Jobs", key="fetch_btn", use_container_width=True):
        with st.spinner("Fetching jobs from Gmail..."):
            try:
                from gmail import get_chatbot_adapter

                adapter = get_chatbot_adapter()
                result = adapter.fetch_jobs(limit=limit)

                st.session_state.jobs = result.get('emails', [])
                st.session_state.status = result.get('status')
                st.session_state.error = None

                if result['status'] == 'success':
                    st.success(f"✅ Found {result['count']} jobs!")
                else:
                    st.warning(f"⚠️ {result.get('message', 'Could not fetch jobs')}")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.session_state.error = str(e)

with col2:
    if st.button("ℹ️ Service Status", key="status_btn", use_container_width=True):
        try:
            from gmail import get_chatbot_adapter

            adapter = get_chatbot_adapter()
            status = adapter.get_status()

            st.session_state.status = status

            with st.popover("Service Status", use_container_width=True):
                st.markdown(f"**Email:** {status.get('email')}")
                st.markdown(f"**Service:** {status.get('service')}")
                st.markdown(f"**Authenticated:** {'✅ Yes' if status.get('authenticated') else '❌ No'}")
                st.markdown(f"**Available:** {'✅ Yes' if status.get('available') else '❌ No'}")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

with col3:
    if st.button("🔧 Available Commands", key="commands_btn", use_container_width=True):
        try:
            from gmail import get_chatbot_adapter

            adapter = get_chatbot_adapter()
            options = adapter.get_options()

            with st.popover("Available Commands", use_container_width=True):
                for opt in options.get('options', []):
                    st.markdown(f"**{opt['name']}**")
                    st.caption(opt['description'])
                    st.divider()

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

st.divider()

# Display jobs
if st.session_state.jobs:
    st.subheader(f"📧 Jobs Found ({len(st.session_state.jobs)})")

    for idx, job in enumerate(st.session_state.jobs, 1):
        with st.container():
            st.markdown(f"""
            <div class="job-card">
                <h4>#{idx} - {job.get('subject', 'No Subject')}</h4>
                <p>{job.get('body', 'No content')[:200]}...</p>
            </div>
            """, unsafe_allow_html=True)

    # Export option
    if st.button("💾 Download as Text"):
        jobs_text = "\n".join([
            f"Job #{idx}\nSubject: {job.get('subject')}\n\n{job.get('body')}\n\n---\n"
            for idx, job in enumerate(st.session_state.jobs, 1)
        ])
        st.download_button(
            label="Download Jobs",
            data=jobs_text,
            file_name=f"naukri_jobs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain"
        )

elif st.session_state.error:
    st.error(f"❌ Error fetching jobs: {st.session_state.error}")
    st.info("Make sure Gmail is accessible and the service is running.")

else:
    st.info("👈 Click 'Fetch Jobs' to get started!")

# Footer
st.divider()
with st.expander("ℹ️ About"):
    st.markdown("""
    ### Gmail Naukri Job Chatbot
    
    This simple chatbot helps you fetch and view job notifications from your Naukri emails.
    
    **Features:**
    - ✅ Fetch latest job notifications
    - ✅ View service status
    - ✅ Download jobs as text
    - ✅ Customizable fetch limit
    
    **How it works:**
    1. Click "Fetch Jobs" to retrieve notifications
    2. View job details inline
    3. Download or copy job information
    
    **Credentials:** Uses hardcoded Gmail credentials (ggpsmo@gmail.com)
    """)

