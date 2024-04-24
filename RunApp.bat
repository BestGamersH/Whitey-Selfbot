@echo off
echo Installing Python dependencies from requirements.txt...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Error: Dependency installation failed.
    pause
    exit /b 1
)

echo Dependencies installed successfully.
start cmd /k python main.py
