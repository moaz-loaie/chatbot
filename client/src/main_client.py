import socket

from interface import Interface
from logger import log_message


def start_client(host="127.0.0.1", port=12345):
    """Start the client and connect to the server."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        log_message("client", f"Connected to server at {host}:{port}")
        print("Connected to server.")
        ui = Interface(client_socket)
        ui.run()
    except ConnectionRefusedError as e:
        log_message("error", f"Connection failed: {e}")
        print(f"Failed to connect to server: {e}")
    except Exception as e:
        log_message("error", f"Unexpected error: {e}")
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        log_message("client", "Client socket closed")


if __name__ == "__main__":
    start_client()
