@echo off
echo.
echo ======================================
echo   Qwen AI Chat - ChatGPT Style UI
echo ======================================
echo.

:: Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing Flask...
    python -m pip install flask
)

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

python flask_chatgpt_ui.py

pause

