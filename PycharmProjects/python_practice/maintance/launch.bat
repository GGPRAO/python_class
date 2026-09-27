@echo off
REM Quick launch script for Prajay Water Front Phase 2 Maintenance Management System

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Running database migration...
python migrate_db.py

echo.
echo ======================================
echo ✅ System Ready!
echo ======================================
echo.
echo Starting Flask app on http://127.0.0.1:5000/
echo Press CTRL+C to stop the server
echo.

python app.py

