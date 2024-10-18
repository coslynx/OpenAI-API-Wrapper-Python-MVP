from unittest import TestCase
from unittest.mock import patch, MagicMock

from utils.config import settings
from utils.logger import logger
from services.openai_service import OpenAIService, OpenAIError


class TestUtils(TestCase):

    @patch("openai.OpenAI")
    def test_generate_text(self, mock_openai):
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(text="Generated Text")]
        mock_openai.completions.create.return_value = mock_completion

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        generated_text = openai_service.generate_text(
            model="text-davinci-003", prompt="Test prompt", temperature=0.7
        )

        self.assertEqual(generated_text, "Generated Text")
        mock_openai.completions.create.assert_called_once_with(
            model="text-davinci-003",
            prompt="Test prompt",
            temperature=0.7,
            max_tokens=100,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_generate_text_error(self, mock_openai):
        mock_openai.completions.create.side_effect = Exception("OpenAI API Error")

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        with self.assertRaisesRegex(OpenAIError, "Error generating text."):
            openai_service.generate_text(
                model="text-davinci-003", prompt="Test prompt"
            )

        mock_openai.completions.create.assert_called_once_with(
            model="text-davinci-003",
            prompt="Test prompt",
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_translate_text(self, mock_openai):
        mock_translation = MagicMock(text="Translated Text")
        mock_openai.translations.create.return_value = mock_translation

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        translated_text = openai_service.translate_text(
            source_language="en", target_language="fr", text="Test text"
        )

        self.assertEqual(translated_text, "Translated Text")
        mock_openai.translations.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            source_language="en",
            target_language="fr",
            text="Test text",
        )

    @patch("openai.OpenAI")
    def test_translate_text_error(self, mock_openai):
        mock_openai.translations.create.side_effect = Exception("OpenAI API Error")

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        with self.assertRaisesRegex(OpenAIError, "Error translating text."):
            openai_service.translate_text(
                source_language="en", target_language="fr", text="Test text"
            )

        mock_openai.translations.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            source_language="en",
            target_language="fr",
            text="Test text",
        )

    @patch("openai.OpenAI")
    def test_answer_question(self, mock_openai):
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(text="Answer to the question")]
        mock_openai.completions.create.return_value = mock_completion

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        answer = openai_service.answer_question(
            model="text-davinci-003", question="What is the capital of France?"
        )

        self.assertEqual(answer, "Answer to the question")
        mock_openai.completions.create.assert_called_once_with(
            model="text-davinci-003",
            prompt="What is the capital of France?",
            temperature=0.0,
            max_tokens=1000,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_answer_question_error(self, mock_openai):
        mock_openai.completions.create.side_effect = Exception("OpenAI API Error")

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        with self.assertRaisesRegex(OpenAIError, "Error answering question."):
            openai_service.answer_question(
                model="text-davinci-003", question="What is the capital of France?"
            )

        mock_openai.completions.create.assert_called_once_with(
            model="text-davinci-003",
            prompt="What is the capital of France?",
            temperature=0.0,
            max_tokens=1000,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_generate_code(self, mock_openai):
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(text="Generated Code")]
        mock_openai.completions.create.return_value = mock_completion

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        code = openai_service.generate_code(
            model="code-davinci-002",
            prompt="Write a function to print Hello World",
            language="python",
        )

        self.assertEqual(code, "Generated Code")
        mock_openai.completions.create.assert_called_once_with(
            model="code-davinci-002",
            prompt="Write a function to print Hello World",
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_generate_code_error(self, mock_openai):
        mock_openai.completions.create.side_effect = Exception("OpenAI API Error")

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        with self.assertRaisesRegex(OpenAIError, "Error generating code."):
            openai_service.generate_code(
                model="code-davinci-002",
                prompt="Write a function to print Hello World",
                language="python",
            )

        mock_openai.completions.create.assert_called_once_with(
            model="code-davinci-002",
            prompt="Write a function to print Hello World",
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
        )

    @patch("openai.OpenAI")
    def test_get_models(self, mock_openai):
        mock_models = MagicMock()
        mock_models.data = [MagicMock(id="model-1"), MagicMock(id="model-2")]
        mock_openai.models.list.return_value = mock_models

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        models = openai_service.get_models()

        self.assertEqual(models, ["model-1", "model-2"])
        mock_openai.models.list.assert_called_once()

    @patch("openai.OpenAI")
    def test_get_models_error(self, mock_openai):
        mock_openai.models.list.side_effect = Exception("OpenAI API Error")

        openai_service = OpenAIService(api_key=settings.OPENAI_API_KEY)
        with self.assertRaisesRegex(OpenAIError, "Error retrieving models."):
            openai_service.get_models()

        mock_openai.models.list.assert_called_once()

    @patch("logging.getLogger")
    def test_logger(self, mock_logger):
        logger.info("Test Info Message")
        mock_logger.assert_called_once_with(__name__)
        mock_logger.return_value.info.assert_called_once_with("Test Info Message")

        logger.debug("Test Debug Message")
        mock_logger.return_value.debug.assert_called_once_with("Test Debug Message")

        logger.warning("Test Warning Message")
        mock_logger.return_value.warning.assert_called_once_with("Test Warning Message")

        logger.error("Test Error Message")
        mock_logger.return_value.error.assert_called_once_with("Test Error Message")

        logger.critical("Test Critical Message")
        mock_logger.return_value.critical.assert_called_once_with("Test Critical Message")

    @patch("utils.config.settings.LOG_LEVEL")
    def test_logger_level(self, mock_log_level):
        mock_log_level.return_value = logging.DEBUG
        logger.info("Test Info Message")
        logger.debug("Test Debug Message")

        mock_log_level.assert_called_once()
        mock_logger.return_value.info.assert_called_once_with("Test Info Message")
        mock_logger.return_value.debug.assert_called_once_with("Test Debug Message")

    @patch("logging.getLogger")
    def test_logger_extra(self, mock_logger):
        logger.info("Test Info Message", extra={"key": "value"})
        mock_logger.assert_called_once_with(__name__)
        mock_logger.return_value.info.assert_called_once_with(
            "Test Info Message", extra={"key": "value"}
        )

        logger.debug("Test Debug Message", extra={"key": "value"})
        mock_logger.return_value.debug.assert_called_once_with(
            "Test Debug Message", extra={"key": "value"}
        )

        logger.warning("Test Warning Message", extra={"key": "value"})
        mock_logger.return_value.warning.assert_called_once_with(
            "Test Warning Message", extra={"key": "value"}
        )

        logger.error("Test Error Message", extra={"key": "value"})
        mock_logger.return_value.error.assert_called_once_with(
            "Test Error Message", extra={"key": "value"}
        )

        logger.critical("Test Critical Message", extra={"key": "value"})
        mock_logger.return_value.critical.assert_called_once_with(
            "Test Critical Message", extra={"key": "value"}
        )