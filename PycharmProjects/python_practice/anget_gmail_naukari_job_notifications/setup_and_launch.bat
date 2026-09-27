@echo off
REM ChatGPT-Like Email Assistant - Complete Setup & Launch
REM This script installs all dependencies and launches the web UI

echo.
echo ======================================================================
echo  ChatGPT-Like Email Assistant - Setup & Launch
echo ======================================================================
echo.
echo Step 1: Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)
echo OK - Python found

echo.
echo Step 2: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 3: Installing dependencies...
echo Installing Flask and extensions...
pip install flask==2.3.2
pip install flask-cors==4.0.0

echo Installing utility packages...
pip install requests==2.31.0
pip install python-dotenv==1.0.0

echo Installing Gmail packages...
pip install google-auth-oauthlib==1.1.0
pip install google-auth-httplib2==0.2.0
pip install google-api-python-client==2.100.0

echo Installing other packages...
pip install ollama==0.1.0
pip install beautifulsoup4==4.12.2
pip install lxml==4.9.3

echo.
echo ======================================================================
echo  Installation Complete!
echo ======================================================================
echo.
echo Step 4: Launching ChatGPT-Like Email Assistant...
echo.
echo Starting web server...
echo   - Opening at: http://localhost:5000
echo   - Browser will open automatically
echo   - Press Ctrl+C to stop the server
echo.
pause

cd /d "%~dp0"
python chatgpt_like_interface.py

pause

