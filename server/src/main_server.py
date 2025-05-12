import socket
import threading

from client_handler import handle_client
from logger import log_message


def start_server(host="0.0.0.0", port=12345):
    """Start the server to listen for client connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # Allow port reuse
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        log_message("server", f"Server started on {host}:{port}")
        print(f"Server listening on {host}:{port}")
        while True:
            client_socket, client_address = server_socket.accept()
            log_message("server", f"New connection from {client_address}")
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, client_address)
            )
            client_thread.daemon = True  # Ensure threads exit when main program does
            client_thread.start()
    except OSError as e:
        log_message("error", f"Server error: {e}")
        print(f"Failed to start server: {e}")
    except KeyboardInterrupt:
        log_message("server", "Server shutting down")
        print("Shutting down server...")
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server()
