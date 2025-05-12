import unittest
from unittest.mock import Mock

from src.client_handler import handle_client


class TestClientHandler(unittest.TestCase):
    def test_handle_client_empty_data(self):
        """Test client handler exits cleanly on empty data."""
        mock_socket = Mock()
        mock_socket.recv.side_effect = [b"", b""]
        handle_client(mock_socket, ("127.0.0.1", 12345))
        mock_socket.close.assert_called_once()

    def test_handle_client_invalid_json(self):
        """Test client handler handles invalid JSON gracefully."""
        mock_socket = Mock()
        mock_socket.recv.side_effect = [
            (4).to_bytes(4, "big"),  # Length
            b"abcd",  # Invalid JSON
            b"",  # End connection
        ]
        mock_socket.sendall = Mock()
        handle_client(mock_socket, ("127.0.0.1", 12345))
        mock_socket.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
