@echo off
cd /d %~dp0
call venv\Scripts\activate
chcp 65001
set PYTHONIOENCODING=utf-8
waitress-serve --port=5000 server:app
