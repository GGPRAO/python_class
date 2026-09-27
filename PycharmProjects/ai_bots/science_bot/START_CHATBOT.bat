@echo off
REM Science Bot Launcher - Batch Script
REM This script starts the Science Formula Chatbot

color 0B
echo.
echo ================================================
echo 🔬 Starting Science Bot...
echo ================================================
echo.

REM Check if streamlit is installed
streamlit --version >nul 2>&1
if errorlevel 1 (
    echo Installing Streamlit...
    pip install streamlit==1.28.1
)

REM Check if ollama is running
echo Checking Ollama service...
timeout /t 1 >nul

powershell -Command "try { [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri http://localhost:11434 -ErrorAction Stop -TimeoutSec 2 | Out-Null; Write-Host '✓ Ollama is running!' -ForegroundColor Green } catch { Write-Host '⚠ Ollama is not running. Please start Ollama!' -ForegroundColor Yellow; Write-Host '  Download from: https://ollama.ai' -ForegroundColor Yellow }"

echo.
echo ================================================
echo 🚀 Launching Science Bot...
echo 📱 App will open in your browser at: http://localhost:8501
echo ================================================
echo.

REM Launch streamlit
streamlit run app.py

if errorlevel 1 (
    echo.
    echo ❌ An error occurred. Press any key to close...
    pause >nul
)

