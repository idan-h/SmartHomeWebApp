@echo off
cd /d %~dp0
waitress-serve --port=5000 server:app
