@echo off
REM Quick Start Chat Bot - Windows Batch Script
REM No admin needed, fixes PyArrow DLL issue automatically

echo.
echo ================================================================================
echo.
echo    Gmail Job Chat Bot - Quick Start (Fixes PyArrow DLL Issue)
echo.
echo ================================================================================
echo.

REM Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)

echo Step 1: Removing Streamlit (fixes PyArrow issue)...
python -m pip uninstall -y streamlit > nul 2>&1

echo Step 2: Installing Flask web framework...
python -m pip install flask flask-cors > nul 2>&1

echo Step 3: Launching chat bot...
echo.
echo Waiting 2 seconds...
timeout /t 2 /nobreak > nul

echo Opening browser...
start http://localhost:5000

echo.
echo ================================================================================
echo.
echo    Chat Bot Starting!
echo.
echo    Open your browser: http://localhost:5000
echo    Commands: help, examples, clear, status
echo    Try: "Python developer jobs"
echo.
echo ================================================================================
echo.

python lightweight_chat_bot.py

echo.
echo Chat bot stopped. Thank you!
pause

