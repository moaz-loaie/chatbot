#!/bin/bash
echo "Starting Server..."
cd server
python -m venv venv_server
source venv_server/bin/activate  # Use .\venv_server\Scripts\activate on Windows
pip install -r requirements.txt
python src/main_server.py