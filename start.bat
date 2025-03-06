@echo off

if not exist hh_clicker_venv (
    echo Virtual environment not found. Creating new one...
    python -m venv hh_clicker_venv
)
call hh_clicker_venv\Scripts\activate

if exist requirements.txt (
    echo Installing requirements.txt...
    pip install -r requirements.txt
) else (
    echo File requirements.txt not found.
)

echo Starting hh-script...
py script.py
cmd /k