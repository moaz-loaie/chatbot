import unittest
from unittest.mock import Mock, patch

from src.interface import Interface


class MockSocket:
    def __init__(self):
        self.sent_data = []

    def sendall(self, data):
        self.sent_data.append(data)

    def recv(self, size):
        return b""

    def close(self):
        pass


class TestInterface(unittest.TestCase):
    def setUp(self):
        self.mock_socket = MockSocket()
        self.ui = Interface(self.mock_socket)

    def test_handle_command_help(self):
        """Test help command displays without crashing."""
        with patch("sys.stdout"):
            self.ui.handle_command("/help")

    def test_exit_chat(self):
        """Test exit command terminates program."""
        with self.assertRaises(SystemExit):
            self.ui.exit_chat()

    def test_get_mood_invalid(self):
        """Test invalid mood defaults to 'default'."""
        with patch("builtins.input", return_value="invalid"):
            mood = self.ui.get_mood()
            self.assertEqual(mood, "default")


if __name__ == "__main__":
    unittest.main()
