@echo off

:check_st_running
REM Check if sublime is still running. 
wmic process list brief | find /i "sublime_text.exe"
set result=%ERRORLEVEL%
if "%result%"=="1" (
  REM Break out of the loop
  echo "not running"
) else (
  timeout 1
  goto check_st_running
)

REM When sublime process no longer exists, loop through the input pids, the 
REM input arguements, and kill each one.
REM This taskkill will force kill the process and all its children. 
:kill_spawned_processes
  taskkill /pid %1 /f /t
  shift
  if not "%~1"=="" goto kill_spawned_processes 

exit /b
