@echo off
echo.
echo ======================================
echo   Qwen AI Chat - Lightweight UI
echo ======================================
echo.

:: Check if ollama is installed
python -c "import ollama" >nul 2>&1
if errorlevel 1 (
    echo Installing Ollama Python library...
    python -m pip install ollama
)

echo.
echo Starting the application...
echo.
echo Access the UI at: http://localhost:5000
echo Press Ctrl+C to stop
echo.

python simple_http_ui.py

pause

