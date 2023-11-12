@echo off
cd /d %~dp0
call venv\Scripts\activate
waitress-serve --port=5000 server:app
