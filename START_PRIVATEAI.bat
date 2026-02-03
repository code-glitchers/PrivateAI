@echo off
TITLE PrivateAI Launcher
echo Starting PrivateAI...
echo.

REM --- LOGGING START ---
echo %DATE% %TIME% > launch_log.txt

REM --- CHECK OLLAMA ---
echo [1] Checking AI Brain (Ollama)...
tasklist /FI "IMAGENAME eq ollama.exe" 2>NUL | find /I /N "ollama.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo    Build-in AI is running. >> launch_log.txt
    echo    AI is ready.
) else (
    echo    Starting AI... >> launch_log.txt
    echo    Starting AI Service...
    start "" "ollama" serve
    timeout /t 5 > NUL
)

REM --- START APP ---
echo [2] Launching Interface...
if exist "venv\Scripts\streamlit.exe" (
    echo    Found Streamlit. >> launch_log.txt
    .\venv\Scripts\streamlit run app.py --server.headless false
) else (
    echo    CRITICAL ERROR: venv not found! >> launch_log.txt
    echo.
    echo    ERROR: Could not find 'venv'.
    echo    Please run setup.bat first.
    echo.
    pause
    exit /b
)

echo.
echo Application Closed.
pause
