@echo off
REM Ultra-Quick Launch - Chat Bot with PyArrow Fix

python -m pip uninstall -y streamlit > nul 2>&1
python -m pip install flask flask-cors > nul 2>&1
start http://localhost:5000
python lightweight_chat_bot.py

