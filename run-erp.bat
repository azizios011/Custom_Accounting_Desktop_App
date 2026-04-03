@echo off
REM Build the Docker image (downloads Node 24)
docker build -t tunisian-erp -f docker/Dockerfile .

REM Run the container with ports mapped
docker run -it -p 8000:8000 -p 9000:9000 --name erp-app tunisian-erp

REM Pause so the window doesn’t close immediately
pause
