@echo off
cd /d %~dp0
call venv\Scripts\activate
chcp 65001
waitress-serve --port=5000 server:app
