# Maths Problem Solver Bot - PowerShell Launcher
# This script sets up and launches the Maths Solver chatbot

Clear-Host

Write-Host "================================" -ForegroundColor Cyan
Write-Host "🧮 Maths Problem Solver Bot" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "📋 Checking prerequisites..." -ForegroundColor Yellow

try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+" -ForegroundColor Red
    Write-Host "Download from: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit
}

# Check if Ollama is running
Write-Host "Checking Ollama service..." -ForegroundColor Yellow

$ollamaProcess = Get-Process ollama -ErrorAction SilentlyContinue
if ($ollamaProcess) {
    Write-Host "✓ Ollama is running" -ForegroundColor Green
} else {
    Write-Host "⚠ Ollama is not running" -ForegroundColor Yellow
    Write-Host "Please ensure:" -ForegroundColor Yellow
    Write-Host "  1. Ollama is installed from https://ollama.ai" -ForegroundColor Yellow
    Write-Host "  2. Run 'ollama serve' in another terminal" -ForegroundColor Yellow
    Write-Host "  3. Pull model with: 'ollama pull qwen2:1.5b'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Continuing anyway... (the app may not work if Ollama is not available)" -ForegroundColor Cyan
}

Write-Host ""

# Install requirements
Write-Host "📦 Installing/Updating dependencies..." -ForegroundColor Yellow
Write-Host "This may take a minute..." -ForegroundColor Gray

python -m pip install -q --upgrade pip
python -m pip install -q -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "✗ Failed to install dependencies" -ForegroundColor Red
    exit
}

Write-Host ""
Write-Host "🚀 Launching Maths Solver Bot..." -ForegroundColor Cyan
Write-Host "Opening in browser at http://localhost:8501" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Launch Streamlit app
streamlit run app.py

# Cleanup
Write-Host ""
Write-Host "================================" -ForegroundColor Cyan
Write-Host "Bot stopped. Thank you for using Maths Solver!" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan

