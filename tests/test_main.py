import unittest
from unittest.mock import patch, MagicMock

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

from main import app
from routers import models, generate, translate, question, code
from services.openai_service import OpenAIService, OpenAIError
from utils.config import settings
from models.request import GenerateRequest, TranslateRequest, QuestionRequest, CodeRequest
from models.response import GenerateResponse, TranslateResponse, QuestionResponse, CodeResponse

class TestMain(unittest.TestCase):

    @patch("openai.OpenAI")
    def setUp(self, mock_openai):
        """
        Setup for test cases:
        - Initializes a FastAPI test client.
        - Creates a mock OpenAI service for API interaction.
        """
        self.client = TestClient(app)
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(text="Generated Text")]
        mock_openai.completions.create.return_value = mock_completion
        mock_translation = MagicMock(text="Translated Text")
        mock_openai.translations.create.return_value = mock_translation
        mock_models = MagicMock()
        mock_models.data = [MagicMock(id="model-1"), MagicMock(id="model-2")]
        mock_openai.models.list.return_value = mock_models

    def test_root(self):
        """
        Tests the root endpoint (`/`)
        - Verifies that it returns a welcome message.
        - Checks for proper status code and response format.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the AI Wrapper MVP!"})
    
    def test_get_models(self):
        """
        Tests the `/models` endpoint:
        - Verifies that it returns a list of available OpenAI models.
        - Checks for proper status code and response format.
        """
        response = self.client.get("/models")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"models": ["model-1", "model-2"]})
    
    def test_generate_text(self):
        """
        Tests the `/generate` endpoint:
        - Sends a valid text generation request.
        - Verifies that it returns the generated text.
        - Checks for proper status code and response format.
        """
        request_data = GenerateRequest(
            model="text-davinci-003", prompt="Test prompt", temperature=0.7
        ).dict()
        response = self.client.post("/generate", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"text": "Generated Text"})
    
    def test_generate_text_error(self):
        """
        Tests error handling in the `/generate` endpoint:
        - Sends an invalid request (missing prompt).
        - Verifies that it returns a 400 Bad Request error.
        - Checks for a specific error message in the response.
        """
        request_data = GenerateRequest(model="text-davinci-003", temperature=0.7).dict()
        response = self.client.post("/generate", json=request_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Invalid request data.")
    
    def test_translate_text(self):
        """
        Tests the `/translate` endpoint:
        - Sends a valid translation request.
        - Verifies that it returns the translated text.
        - Checks for proper status code and response format.
        """
        request_data = TranslateRequest(
            source_language="en", target_language="fr", text="Test text"
        ).dict()
        response = self.client.post("/translate", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"translated_text": "Translated Text"})
    
    def test_translate_text_error(self):
        """
        Tests error handling in the `/translate` endpoint:
        - Sends an invalid request (missing source language).
        - Verifies that it returns a 400 Bad Request error.
        - Checks for a specific error message in the response.
        """
        request_data = TranslateRequest(target_language="fr", text="Test text").dict()
        response = self.client.post("/translate", json=request_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Invalid request data.")
    
    def test_answer_question(self):
        """
        Tests the `/question` endpoint:
        - Sends a valid question answering request.
        - Verifies that it returns the answer to the question.
        - Checks for proper status code and response format.
        """
        request_data = QuestionRequest(question="What is the capital of France?").dict()
        response = self.client.post("/question", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"answer": "Generated Text"})
    
    def test_answer_question_error(self):
        """
        Tests error handling in the `/question` endpoint:
        - Sends an invalid request (missing question).
        - Verifies that it returns a 400 Bad Request error.
        - Checks for a specific error message in the response.
        """
        request_data = QuestionRequest().dict()
        response = self.client.post("/question", json=request_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Invalid request data.")
    
    def test_generate_code(self):
        """
        Tests the `/code` endpoint:
        - Sends a valid code generation request.
        - Verifies that it returns the generated code.
        - Checks for proper status code and response format.
        """
        request_data = CodeRequest(
            language="python", prompt="Write a function to print Hello World"
        ).dict()
        response = self.client.post("/code", json=request_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"code": "Generated Text"})
    
    def test_generate_code_error(self):
        """
        Tests error handling in the `/code` endpoint:
        - Sends an invalid request (missing language).
        - Verifies that it returns a 400 Bad Request error.
        - Checks for a specific error message in the response.
        """
        request_data = CodeRequest(prompt="Write a function to print Hello World").dict()
        response = self.client.post("/code", json=request_data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["message"], "Invalid request data.")
    
    def test_generate_text_error_handling(self):
        """
        Tests error handling in the `/generate` endpoint:
        - Triggers an OpenAIError during text generation.
        - Verifies that it returns a 500 Internal Server Error.
        - Checks for a specific error message in the response.
        """
        with patch.object(OpenAIService, "generate_text", side_effect=OpenAIError("Error generating text.")):
            request_data = GenerateRequest(
                model="text-davinci-003", prompt="Test prompt", temperature=0.7
            ).dict()
            response = self.client.post("/generate", json=request_data)
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json()["detail"], "Error generating text.")
    
    def test_translate_text_error_handling(self):
        """
        Tests error handling in the `/translate` endpoint:
        - Triggers an OpenAIError during translation.
        - Verifies that it returns a 500 Internal Server Error.
        - Checks for a specific error message in the response.
        """
        with patch.object(OpenAIService, "translate_text", side_effect=OpenAIError("Error translating text.")):
            request_data = TranslateRequest(
                source_language="en", target_language="fr", text="Test text"
            ).dict()
            response = self.client.post("/translate", json=request_data)
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json()["detail"], "Error translating text.")
    
    def test_answer_question_error_handling(self):
        """
        Tests error handling in the `/question` endpoint:
        - Triggers an OpenAIError during question answering.
        - Verifies that it returns a 500 Internal Server Error.
        - Checks for a specific error message in the response.
        """
        with patch.object(OpenAIService, "answer_question", side_effect=OpenAIError("Error answering question.")):
            request_data = QuestionRequest(question="What is the capital of France?").dict()
            response = self.client.post("/question", json=request_data)
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json()["detail"], "Error answering question.")
    
    def test_generate_code_error_handling(self):
        """
        Tests error handling in the `/code` endpoint:
        - Triggers an OpenAIError during code generation.
        - Verifies that it returns a 500 Internal Server Error.
        - Checks for a specific error message in the response.
        """
        with patch.object(OpenAIService, "generate_code", side_effect=OpenAIError("Error generating code.")):
            request_data = CodeRequest(
                language="python", prompt="Write a function to print Hello World"
            ).dict()
            response = self.client.post("/code", json=request_data)
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json()["detail"], "Error generating code.")

if __name__ == "__main__":
    unittest.main()