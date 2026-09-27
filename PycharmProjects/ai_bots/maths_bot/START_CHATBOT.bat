@echo off
REM Maths Problem Solver Bot - Batch Launcher
REM This script sets up and launches the Maths Solver chatbot

cls
color 0B
echo.
echo ================================
echo.
echo  ^C  Maths Problem Solver Bot
echo.
echo ================================
echo.

REM Check if Python is installed
echo 📋 Checking prerequisites...

python --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python not found. Please install Python 3.8+
    echo Download from: https://www.python.org/downloads/
    pause
    exit /b 1
) else (
    for /f "tokens=*" %%i in ('python --version') do (
        echo ✓ Python found: %%i
    )
)

REM Check if Ollama is installed
tasklist /FI "IMAGENAME eq ollama.exe" 2>nul | find /I /N "ollama.exe">nul
if "%ERRORLEVEL%"=="0" (
    echo ✓ Ollama is running
) else (
    echo.
    echo ⚠  Ollama is not currently running
    echo.
    echo Please ensure:
    echo   1. Ollama is installed from https://ollama.ai
    echo   2. Run 'ollama serve' in another Command Prompt
    echo   3. Pull model with: 'ollama pull qwen2:1.5b'
    echo.
    echo Continuing anyway... (the app may not work if Ollama is not available)
)

echo.
echo 📦 Installing/Updating dependencies...
echo This may take a minute...
echo.

python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt >nul 2>&1

if errorlevel 1 (
    echo ✗ Failed to install dependencies
    pause
    exit /b 1
) else (
    echo ✓ Dependencies installed successfully
)

echo.
echo 🚀 Launching Maths Solver Bot...
echo Opening in browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

REM Launch Streamlit app
streamlit run app.py

echo.
echo ================================
echo Bot stopped. Thank you for using Maths Solver!
echo ================================
echo.
pause

