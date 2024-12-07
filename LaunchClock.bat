@echo off
:: This batch file launches the customizable lock screen clock and keeps it always on top using NirCmd.

:: Set the path to your Python executable and your script
set PYTHON_PATH="C:\path\to\python.exe"
set SCRIPT_PATH="C:\path\to\CustomizableClockTemplate.py"

:: Set the path to NirCmd (make sure NirCmd.exe is in the same folder as this batch file or provide full path)
set NIRCMD_PATH="C:\path\to\nircmd.exe"

:: Run the Python script
start "" %PYTHON_PATH% %SCRIPT_PATH%

:: Use NirCmd to set the clock window to always stay on top
start "" %NIRCMD_PATH% win settopmost class "TkClockWindow" 1

:: End the batch file
exit
