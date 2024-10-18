import unittest
from unittest.mock import patch, MagicMock

from services.openai_service import OpenAIService, OpenAIError
from utils.config import settings
from models.request import GenerateRequest, TranslateRequest, QuestionRequest, CodeRequest
from models.response import GenerateResponse, TranslateResponse, QuestionResponse, CodeResponse

class TestModels(unittest.TestCase):

    @patch("openai.OpenAI")
    def test_generate_text_request_validation(self, mock_openai):
        # Test valid request
        valid_request = GenerateRequest(model="text-davinci-003", prompt="Test prompt", temperature=0.7, max_tokens=100)
        self.assertIsNone(valid_request.model_validate())

        # Test invalid request - missing prompt
        invalid_request = GenerateRequest(model="text-davinci-003", temperature=0.7, max_tokens=100)
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_request.model_validate()

    @patch("openai.OpenAI")
    def test_translate_text_request_validation(self, mock_openai):
        # Test valid request
        valid_request = TranslateRequest(source_language="en", target_language="fr", text="Test text")
        self.assertIsNone(valid_request.model_validate())

        # Test invalid request - missing source language
        invalid_request = TranslateRequest(target_language="fr", text="Test text")
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_request.model_validate()

    @patch("openai.OpenAI")
    def test_answer_question_request_validation(self, mock_openai):
        # Test valid request
        valid_request = QuestionRequest(question="What is the capital of France?")
        self.assertIsNone(valid_request.model_validate())

        # Test invalid request - missing question
        invalid_request = QuestionRequest()
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_request.model_validate()

    @patch("openai.OpenAI")
    def test_generate_code_request_validation(self, mock_openai):
        # Test valid request
        valid_request = CodeRequest(language="python", prompt="Write a function to print Hello World", temperature=0.5, max_tokens=100)
        self.assertIsNone(valid_request.model_validate())

        # Test invalid request - missing language
        invalid_request = CodeRequest(prompt="Write a function to print Hello World", temperature=0.5, max_tokens=100)
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_request.model_validate()

    @patch("openai.OpenAI")
    def test_generate_response_validation(self, mock_openai):
        # Test valid response
        valid_response = GenerateResponse(text="Generated Text")
        self.assertIsNone(valid_response.model_validate())

        # Test invalid response - missing text
        invalid_response = GenerateResponse()
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_response.model_validate()

    @patch("openai.OpenAI")
    def test_translate_response_validation(self, mock_openai):
        # Test valid response
        valid_response = TranslateResponse(translated_text="Translated Text")
        self.assertIsNone(valid_response.model_validate())

        # Test invalid response - missing translated_text
        invalid_response = TranslateResponse()
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_response.model_validate()

    @patch("openai.OpenAI")
    def test_question_response_validation(self, mock_openai):
        # Test valid response
        valid_response = QuestionResponse(answer="Answer to the question")
        self.assertIsNone(valid_response.model_validate())

        # Test invalid response - missing answer
        invalid_response = QuestionResponse()
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_response.model_validate()

    @patch("openai.OpenAI")
    def test_code_response_validation(self, mock_openai):
        # Test valid response
        valid_response = CodeResponse(code="Generated Code")
        self.assertIsNone(valid_response.model_validate())

        # Test invalid response - missing code
        invalid_response = CodeResponse()
        with self.assertRaisesRegex(ValueError, "field required"):
            invalid_response.model_validate()

if __name__ == '__main__':
    unittest.main()