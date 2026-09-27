@echo off
REM ============================================================================
REM GGPRAO AI Chat - Automatic Solution Selector
REM This script detects what works and launches the best solution
REM ============================================================================

setlocal enabledelayedexpansion

title GGPRAO AI Chat - Solution Launcher

echo.
echo ============================================================================
echo  ^🚀 GGPRAO AI Chat - Automatic Solution Selector
echo ============================================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo Checking available solutions...
echo.

REM Try pure Python web app
python -c "from http.server import HTTPServer; import json; exit(0)" >nul 2>&1
if errorlevel 0 (
    echo [OPTION 1] Pure Python Web App: AVAILABLE ^✅ ^(RECOMMENDED^)
    set "PURE_PYTHON_AVAILABLE=1"
) else (
    echo [OPTION 1] Pure Python Web App: NOT AVAILABLE ^❌
)

REM Try Streamlit
python -c "import streamlit; exit(0)" >nul 2>&1
if errorlevel 0 (
    echo [OPTION 2] Streamlit: AVAILABLE ^✅
    set "STREAMLIT_AVAILABLE=1"
) else (
    echo [OPTION 2] Streamlit: NOT AVAILABLE ^❌
)

REM Try Flask
python -c "import flask; exit(0)" >nul 2>&1
if errorlevel 0 (
    echo [OPTION 3] Flask: AVAILABLE ^✅
    set "FLASK_AVAILABLE=1"
) else (
    echo [OPTION 3] Flask: NOT AVAILABLE ^❌
)

echo.
echo ============================================================================
echo Selecting best available option...
echo ============================================================================
echo.

REM Launch best option
if "!PURE_PYTHON_AVAILABLE!"=="1" (
    echo Launching: Pure Python Web App ^(RECOMMENDED^)
    echo.
    echo Starting HTTP server on http://127.0.0.1:5000
    echo.
    python simple_web_app.py
    goto :end
)

if "!STREAMLIT_AVAILABLE!"=="1" (
    echo Launching: Streamlit
    echo.
    python -m streamlit run chatgpt_ui.py
    goto :end
)

if "!FLASK_AVAILABLE!"=="1" (
    echo Launching: Flask Web App
    echo.
    python app_flask_alternative.py
    goto :end
)

REM If nothing worked
echo.
echo ============================================================================
echo ERROR: No suitable framework available
echo ============================================================================
echo.
echo Available options:
echo 1. Run diagnostic: python diagnose_system.py
echo 2. Fix Streamlit:  python ultimate_pyarrow_fix.py
echo 3. Use WSL:        wsl python -m streamlit run chatgpt_ui.py
echo.
pause
exit /b 1

:end
pause

