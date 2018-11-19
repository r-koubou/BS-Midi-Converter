@echo off

echo Create venv to ./venv/
python -m venv venv
call .\venv\Scripts\activate.bat

echo # Update pip
python -m pip install --upgrade pip

echo done
