@echo off
REM PyArrow DLL Fix - Run this batch file to start the app safely
REM This sets the environment variable BEFORE Python starts

echo Setting PyArrow fix...
set PYARROW_IGNORE_TIMEZONE=1

echo.
echo Verifying imports...
python verify_imports.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Import verification failed!
    echo Please check your Python installation.
    pause
    exit /b 1
)

echo.
echo Starting Streamlit app...
echo.
streamlit run chatgpt_ui.py

pause

