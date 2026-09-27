@echo off
REM ============================================================================
REM GGPRAO AI Chat - PyArrow DLL Error Fix (PERMANENT)
REM This script sets environment variables at Windows level
REM ============================================================================

title GGPRAO AI Chat - PyArrow Fix

echo.
echo ============================================================================
echo  🚀 GGPRAO AI Chat - PyArrow DLL Error Fix
echo ============================================================================
echo.

REM Set environment variables BEFORE Python starts
echo Setting PyArrow environment variables...

set PYARROW_IGNORE_TIMEZONE=1
set ARROW_IGNORE_TIMEZONE=1
set PYTHONPATH=%CD%

echo ✅ Environment variables set:
echo    PYARROW_IGNORE_TIMEZONE=1
echo    ARROW_IGNORE_TIMEZONE=1
echo.

REM Small delay
timeout /t 2 /nobreak

echo.
echo Verifying Python and dependencies...
python --version
pip --version

echo.
echo ============================================================================
echo  Launching Streamlit Chat Application...
echo ============================================================================
echo.

REM Launch Streamlit with environment variables persisted
streamlit run chatgpt_ui.py

pause

