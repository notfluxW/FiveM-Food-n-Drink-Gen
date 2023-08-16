@echo off

@REM echo Checking for updates...

@REM REM Get the current commit hash
@REM for /f %%H in ('git rev-parse HEAD') do set "current_commit=%%H"

@REM REM Pull the latest changes from the Git repository
@REM for /f "delims=" %%I in ('git pull') do (
@REM     set "git_output=%%I"
@REM )

@REM REM Get the new commit hash after pulling
@REM for /f %%H in ('git rev-parse HEAD') do set "new_commit=%%H"

@REM if "%new_commit%" == "%current_commit%" (
@REM     echo Food ^& Drink Generator is already up to date.
@REM ) else (
@REM     echo Food ^& Drink Generator updated successfully.
@REM )

cd src

python main.py

pause
