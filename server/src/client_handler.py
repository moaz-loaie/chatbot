import json
import socket

from ai_model_interface import get_ai_response
from logger import log_message


def handle_client(client_socket, client_address):
    """Handle communication with a single client in a separate thread."""
    try:
        while True:
            # Receive message length (4 bytes)
            length_data = client_socket.recv(4)
            if not length_data:
                break  # Client disconnected
            length = int.from_bytes(length_data, "big")
            if length <= 0:
                continue  # Invalid length, skip

            # Receive message payload
            message_data = client_socket.recv(length)
            if not message_data:
                break  # Client disconnected

            # Parse JSON message
            try:
                message = json.loads(message_data.decode("utf-8"))
                mood = message.get("mood", "default")
                user_input = message.get("message", "")
                if not user_input:
                    continue  # Empty message, skip
                log_message(
                    "client",
                    f"Received from {client_address}: {user_input} (mood: {mood})",
                )

                # Generate and send AI response
                response = get_ai_response(user_input, mood)
                response_message = json.dumps({"response": response})
                response_length = len(response_message)
                client_socket.sendall(
                    response_length.to_bytes(4, "big")
                    + response_message.encode("utf-8")
                )
                log_message("server", f"Sent to {client_address}: {response}")
            except json.JSONDecodeError as e:
                log_message("error", f"Invalid JSON from {client_address}: {e}")
                continue
    except ConnectionError as e:
        log_message("error", f"Connection error with {client_address}: {e}")
    except Exception as e:
        log_message("error", f"Unexpected error with {client_address}: {e}")
    finally:
        client_socket.close()
        log_message("server", f"Connection closed with {client_address}")
