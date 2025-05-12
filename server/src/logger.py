import json
import os
from datetime import datetime
from threading import Lock

LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
SESSION_ID = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = os.path.join(LOG_DIR, f"server_log_{SESSION_ID}.json")
LOG_LOCK = Lock()


def log_message(role: str, message: str):
    """Log a message to a JSON file in a thread-safe manner."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "message": message,
    }
    try:
        with LOG_LOCK:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except IOError as e:
        print(f"Failed to write log: {e}")
