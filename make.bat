@echo off

set PYTHONPATH=%PYTHONPATH%;%CD%

if "%1"=="run" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" http://127.0.0.1:8000/docs
    uvicorn workout_api.main:app --reload
    exit /b
)

if "%1"=="create-migrations" (
    alembic revision --autogenerate -m %2
    exit /b
)

if "%1"=="run-migrations" (
    alembic upgrade head
    exit /b
)

echo Uso: make.bat [run / create-migrations / run-migrations]