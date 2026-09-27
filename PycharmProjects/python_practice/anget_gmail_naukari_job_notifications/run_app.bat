@echo off
REM Streamlit Application Launcher
REM Naukri Job Mail Agent

cd /d "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"

echo.
echo ============================================
echo Starting Naukri Job Mail Agent
echo ============================================
echo.
echo Launching Streamlit at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

python -m streamlit run ai_streamlit.py

pause

