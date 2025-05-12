@echo off
echo Starting Server...
cd server
python -m venv venv_server
call venv_server\Scripts\activate
pip install -r requirements.txt
python src/main_server.py