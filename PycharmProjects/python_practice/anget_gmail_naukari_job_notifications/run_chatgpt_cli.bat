@echo off
REM ChatGPT-Like Email Assistant - CLI Launcher
REM This script runs the conversational CLI interface

echo.
echo ================================================================================
echo   ChatGPT-Like Email Assistant - CLI Version
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
echo   Starting ChatGPT-Like Email Assistant...
echo ================================================================================
echo.

python chatgpt_like_interface.py

pause

