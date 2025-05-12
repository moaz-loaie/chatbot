#!/bin/bash
echo "Starting Python Client..."
cd client_python
python -m venv venv_client
source venv_client/bin/activate  # Use .\venv_client\Scripts\activate on Windows
pip install -r requirements.txt
python src/main_client.py