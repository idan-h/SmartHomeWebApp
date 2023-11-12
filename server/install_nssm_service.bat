@echo off
SETLOCAL

REM Set the path to your NSSM executable and the service name
SET NSSM_PATH=.\nssm-2.24\win32\nssm.exe
SET SERVICE_NAME=cHBService

REM Install the service
"%NSSM_PATH%" install %SERVICE_NAME% "%CD%\start_server.bat"

REM Set the directory of the Flask application as the working directory of the service
"%NSSM_PATH%" set %SERVICE_NAME% AppDirectory "%CD%"

REM Optional: Configure stdout and stderr logs
"%NSSM_PATH%" set %SERVICE_NAME% AppStdout "%CD%\stdout.log"
"%NSSM_PATH%" set %SERVICE_NAME% AppStderr "%CD%\stderr.log"

REM Start the service
"%NSSM_PATH%" start %SERVICE_NAME%

echo Flask service %SERVICE_NAME% installed and started.
ENDLOCAL
