@echo off

echo Checking for updates...

REM Get the current commit hash
for /f %%H in ('git rev-parse HEAD') do set "current_commit=%%H"

REM Pull the latest changes from the Git repository
for /f "delims=" %%I in ('git pull') do (
    set "git_output=%%I"
)

REM Get the new commit hash after pulling
for /f %%H in ('git rev-parse HEAD') do set "new_commit=%%H"

if "%new_commit%" == "%current_commit%" (
    echo Food ^& Drink Generator is already up to date.
) else (
    echo Food ^& Drink Generator updated successfully.
)

cd src

python main.py

pause
