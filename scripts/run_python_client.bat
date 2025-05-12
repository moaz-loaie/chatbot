@echo off
echo Starting Python Client...
cd client_python
python -m venv venv_client
call venv_client\Scripts\activate
pip install -r requirements.txt
python src/main_client.py