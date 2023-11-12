@echo off
SETLOCAL

REM Assuming NSSM is in the system PATH
REM Replace YourServiceName with your desired service name

REM Install the service
nssm install cHBServer "%CD%\start_server.bat"

REM Set the directory of the Flask application as the working directory of the service
nssm set cHBServer AppDirectory "%CD%"

REM Optional: Configure stdout and stderr logs
nssm set cHBServer AppStdout "%CD%\stdout.log"
nssm set cHBServer AppStderr "%CD%\stderr.log"

REM Start the service
nssm start cHBServer

echo Flask service installed and started.
ENDLOCAL
