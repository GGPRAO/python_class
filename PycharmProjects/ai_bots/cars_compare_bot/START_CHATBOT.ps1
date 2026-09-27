# Cars Compare Bot Startup Script
# Make sure Ollama is running before starting

Write-Host "Starting Cars Compare Bot..." -ForegroundColor Green
Write-Host ""
Write-Host "Make sure Ollama is installed and running!" -ForegroundColor Yellow
Write-Host "Visit https://ollama.ai to install or start it." -ForegroundColor Yellow
Write-Host ""

streamlit run app.py

Read-Host "Press Enter to exit"

