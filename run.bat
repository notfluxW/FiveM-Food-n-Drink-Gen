@echo off
REM Navigate to the script directory

REM Get the current commit hash
setlocal
for /f %%H in ('git rev-parse HEAD') do set "current_commit=%%H"
endlocal

REM Pull the latest changes from the Git repository
git pull

setlocal
REM Get the new commit hash after pulling
for /f %%H in ('git rev-parse HEAD') do set "new_commit=%%H"
endlocal

if "%new_commit%" == "%current_commit%" (
    echo Food & Drink Generator is already up to date.
) else (
    echo Food & Drink Generator updated successfully.
)

cd src
python main.py

pause