@echo off
REM Installation batch file for Naukri Job Mail Agent
REM This bypasses Application Control Policy restrictions

echo.
echo ============================================
echo Installing Naukri Job Mail Agent Dependencies
echo ============================================
echo.

cd /d "C:\Users\USER\PycharmProjects\python_practice\anget_gmail_naukari_job_notifications"

echo Installing Streamlit...
python -m pip install --user -q streamlit

echo Installing Google Libraries...
python -m pip install --user -q google-auth-oauthlib
python -m pip install --user -q google-auth-httplib2
python -m pip install --user -q google-api-python-client

echo Installing Ollama Client...
python -m pip install --user -q ollama

echo Installing HTML Parser...
python -m pip install --user -q beautifulsoup4
python -m pip install --user -q lxml

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Start Ollama: ollama serve
echo 2. Run app: python -m streamlit run ai_streamlit.py
echo.
pause

