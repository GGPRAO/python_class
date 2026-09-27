# India Trip Planner Chatbot - PowerShell Launcher
# Run this script to start the chatbot: .\START_CHATBOT.ps1

Write-Host "`n" -ForegroundColor White
Write-Host "╔════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   India Trip Planner Chatbot          ║" -ForegroundColor Cyan
Write-Host "║   Powered by Streamlit & Ollama      ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host "`n" -ForegroundColor White

# Check if Python is installed
Write-Host "🔍 Checking Python installation..." -ForegroundColor Yellow
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "📥 Download Python from: https://www.python.org" -ForegroundColor Cyan
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✅ Python found: $pythonCheck" -ForegroundColor Green

# Check if Ollama is running
Write-Host "`n🔍 Checking Ollama service..." -ForegroundColor Yellow
try {
    $response = Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -ErrorAction Stop
    Write-Host "✅ Ollama is running!" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Ollama doesn't appear to be running" -ForegroundColor Yellow
    Write-Host "`n📋 To start Ollama:" -ForegroundColor Cyan
    Write-Host "   1. Install from https://ollama.ai" -ForegroundColor White
    Write-Host "   2. Open PowerShell and run: ollama run qwen2:1.5b" -ForegroundColor White
    Write-Host "   3. Return here and run this script again" -ForegroundColor White
    Read-Host "`nPress Enter to exit"
    exit 1
}

# Install/Update requirements
Write-Host "`n📦 Installing/updating Python dependencies..." -ForegroundColor Yellow
pip install -q streamlit ollama 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Start Streamlit
Write-Host "`n" -ForegroundColor White
Write-Host "╔════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║   Starting Chatbot Application...     ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Green
Write-Host "`n" -ForegroundColor White
Write-Host "🌐 Opening browser at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "⏹️  Press Ctrl+C to stop the chatbot" -ForegroundColor Yellow
Write-Host "`n" -ForegroundColor White

# Run Streamlit
streamlit run app.py

Write-Host "`nChatbot stopped." -ForegroundColor Yellow
Read-Host "Press Enter to exit"

