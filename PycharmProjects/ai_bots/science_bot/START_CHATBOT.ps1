# Science Bot Launcher - PowerShell Script
# This script starts the Science Formula Chatbot

Write-Host "🔬 Starting Science Bot..." -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Check if streamlit is installed
try {
    $streamlitCheck = streamlit --version 2>&1
    Write-Host "✓ Streamlit found: $streamlitCheck" -ForegroundColor Green
}
catch {
    Write-Host "✗ Streamlit not found. Installing..." -ForegroundColor Yellow
    pip install streamlit==1.28.1
}

# Check if ollama is running
Write-Host ""
Write-Host "Checking Ollama service..." -ForegroundColor Cyan
try {
    $response = Invoke-WebRequest -Uri "http://localhost:11434" -ErrorAction Stop -TimeoutSec 2
    Write-Host "✓ Ollama is running!" -ForegroundColor Green
}
catch {
    Write-Host "⚠ Ollama is not running. Please start Ollama!" -ForegroundColor Yellow
    Write-Host "  Download from: https://ollama.ai" -ForegroundColor Yellow
    Write-Host ""
}

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "🚀 Launching Science Bot..." -ForegroundColor Green
Write-Host "📱 App will open in your browser at: http://localhost:8501" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Launch streamlit
streamlit run app.py

# Keep window open if there's an error
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ An error occurred. Press Enter to close..." -ForegroundColor Red
    Read-Host
}

