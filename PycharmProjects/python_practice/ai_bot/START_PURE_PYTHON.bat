@echo off
REM ============================================================================
REM GGPRAO AI Chat - Pure Python Web App Launcher
REM Works without Streamlit/PyArrow - Perfect for restricted systems
REM ============================================================================

title GGPRAO AI Chat - Pure Python

echo.
echo ============================================================================
echo  ^🚀 GGPRAO AI Chat - Pure Python Web App
echo ============================================================================
echo.
echo This version requires NO Streamlit or PyArrow!
echo Works on systems with strict Windows security policies.
echo.

REM Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Starting web server...
echo.

REM Launch the pure Python web app
python simple_web_app.py

pause

