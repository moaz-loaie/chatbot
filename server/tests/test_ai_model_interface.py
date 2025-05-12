import unittest
from unittest.mock import patch

from src.ai_model_interface import get_ai_response


class TestAIModelInterface(unittest.TestCase):
    @patch("src.ai_model_interface.model.generate")
    def test_get_ai_response_valid(self, mock_generate):
        """Test AI response generation with valid input."""
        mock_generate.return_value = [50256]  # Dummy token ID
        with patch(
            "src.ai_model_interface.tokenizer.decode", return_value="Mocked response"
        ):
            response = get_ai_response("Hello", "default")
            self.assertEqual(response, "Mocked response")

    def test_get_ai_response_empty(self):
        """Test AI response with empty input."""
        response = get_ai_response("", "default")
        self.assertEqual(response, "No input provided.")


if __name__ == "__main__":
    unittest.main()
