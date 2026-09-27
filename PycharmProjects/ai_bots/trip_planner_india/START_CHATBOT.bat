@echo off
REM India Trip Planner Chatbot - Quick Start Script
REM Run this batch file to start the chatbot automatically

echo.
echo ========================================
echo  India Trip Planner Chatbot
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Download Python from: https://www.python.org
    pause
    exit /b 1
)

REM Check if Ollama is running
timeout /t 1 /nobreak >nul 2>&1

echo Checking if Ollama is running...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo WARNING: Ollama doesn't appear to be running!
    echo.
    echo To start Ollama:
    echo 1. Install from https://ollama.ai
    echo 2. Open PowerShell and run: ollama run qwen2:1.5b
    echo.
    echo Then return here and run this script again.
    pause
    exit /b 1
)

echo ✓ Ollama is running!
echo.

REM Install requirements if needed
echo Installing/updating dependencies...
pip install -q streamlit ollama >nul 2>&1

echo.
echo ========================================
echo  Starting Chatbot Application
echo ========================================
echo.
echo Opening browser at: http://localhost:8501
echo.
echo Press Ctrl+C to stop the chatbot
echo.

REM Run streamlit
streamlit run app.py

pause

