import json
import socket

from logger import log_message


def send_message(sock, message):
    """Send a JSON message to the server with a length prefix."""
    try:
        message_data = json.dumps(message).encode("utf-8")
        length = len(message_data)
        sock.sendall(length.to_bytes(4, "big") + message_data)
        log_message("network", f"Sent message: {message}")
    except Exception as e:
        log_message("error", f"Send error: {e}")
        raise


def receive_message(sock):
    """Receive a JSON message from the server."""
    try:
        length_data = sock.recv(4)
        if not length_data:
            return None  # Connection closed
        length = int.from_bytes(length_data, "big")
        if length <= 0:
            return None  # Invalid length

        message_data = sock.recv(length)
        if not message_data:
            return None  # Connection closed

        message = json.loads(message_data.decode("utf-8"))
        log_message("network", f"Received message: {message}")
        return message
    except (ConnectionError, json.JSONDecodeError) as e:
        log_message("error", f"Receive error: {e}")
        return None
    except Exception as e:
        log_message("error", f"Unexpected receive error: {e}")
        raise
