@echo off
REM ChatGPT-Like Email Assistant - Web UI Launcher
REM This script runs the web interface on http://localhost:5000

echo.
echo ================================================================================
echo   ChatGPT-Like Email Assistant - Web Version
echo ================================================================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo Checking dependencies...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo ================================================================================
echo   Starting ChatGPT-Like Email Assistant Web Interface...
echo ================================================================================
echo.
echo Web interface will be available at: http://localhost:5000
echo Opening browser...
echo.

REM Start Python server in background
start python chatgpt_web_interface.py

REM Wait a moment for server to start
timeout /t 3 /nobreak

REM Try to open browser
start http://localhost:5000

echo.
echo Web interface started! If browser didn't open, go to:
echo http://localhost:5000
echo.
echo Press Ctrl+C in the Python window to stop the server
pause

