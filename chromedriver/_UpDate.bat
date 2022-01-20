@echo off
rem  Download the right ChromeDriver version & keep it up to date on Windows/Linux/macOS using C# .NET - https://bit.ly/3uR7V6E
rem  PowerShell - https://bit.ly/3BmgAAK

@echo.
@echo ChromeDriver Update
@echo.

rem Save this code to a file named 'InstallChromeDriver.ps1' and invoke the script from PowerShell like this:
cd /d d:\Utils\chromedriver\

rem  cd d:\Utils\chromedriver\
rem  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
rem  .\_UpDateCmd.ps1 -ChromeDriverOutputPath .\chromedriver.exe

rem Powershell.exe -executionpolicy remotesigned -File  _UpDate.ps1
    Powershell.exe -NoProfile  -ExecutionPolicy Bypass -File "_UpDate.ps1"

@echo.
pause
