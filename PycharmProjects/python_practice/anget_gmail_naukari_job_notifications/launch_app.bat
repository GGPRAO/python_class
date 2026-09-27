@echo off
REM ChatGPT-Like Email Assistant - Setup and Run

echo.
echo =====================================================
echo ChatGPT-Like Email Assistant - Launching
echo =====================================================
echo.

echo Installing dependencies...
pip install streamlit==1.28.1
pip install flask==2.3.2
pip install flask-cors==4.0.0
pip install google-auth-oauthlib==1.1.0
pip install google-auth-httplib2==0.2.0
pip install google-api-python-client==2.100.0
pip install ollama==0.1.0
pip install beautifulsoup4==4.12.2
pip install lxml==4.9.3
pip install requests==2.31.0
pip install python-dotenv==1.0.0

echo.
echo Dependencies installed!
echo.
echo Launching application...
python chatgpt_like_interface.py

pause

