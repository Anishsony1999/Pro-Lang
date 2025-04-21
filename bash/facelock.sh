@echo off
wsl python3 face.py

if %errorlevel% equ 0 (
    start "" "C:\App.exe"
) else (
    echo "Your not a admin"
)