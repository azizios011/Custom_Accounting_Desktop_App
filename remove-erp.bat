@echo off
REM Force remove the container named erp-app, ignore errors if not found
docker rm -f erp-app 2>nul

REM Recursively search for symlinks named "public" up to 10 levels deep and delete them
for /r %%i in (public) do (
    if exist "%%i" (
        echo Deleting symlink: %%i
        rmdir "%%i" 2>nul
        del "%%i" 2>nul
    )
)

REM Pause so you can see the result
pause
