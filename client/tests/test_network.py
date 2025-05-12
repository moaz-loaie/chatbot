import unittest
from unittest.mock import Mock

from src.network import receive_message, send_message


class TestNetwork(unittest.TestCase):
    def test_send_message_success(self):
        """Test sending a message calls sendall."""
        mock_socket = Mock()
        message = {"mood": "default", "message": "test"}
        send_message(mock_socket, message)
        mock_socket.sendall.assert_called_once()

    def test_receive_message_empty(self):
        """Test empty receive returns None."""
        mock_socket = Mock()
        mock_socket.recv.side_effect = [b""]
        result = receive_message(mock_socket)
        self.assertIsNone(result)

    def test_receive_message_valid(self):
        """Test valid message reception."""
        mock_socket = Mock()
        mock_socket.recv.side_effect = [
            (15).to_bytes(4, "big"),  # Length
            b'{"response":"Hi"}',  # Payload
        ]
        result = receive_message(mock_socket)
        self.assertEqual(result, {"response": "Hi"})


if __name__ == "__main__":
    unittest.main()
