@echo off
REM Force remove the container named erp-app, ignore errors if not found
docker rm -f erp-app 2>nul

REM Pause so you can see the result
pause
