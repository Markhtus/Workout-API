@echo off

if "%1"=="run" (
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

echo Comando desconhecido