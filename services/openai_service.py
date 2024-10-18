from typing import Optional
from fastapi import HTTPException, status
from openai import OpenAI
from utils.config import settings
from utils.logger import logger
from models.response import ModelResponse

# Initialize OpenAI client
openai = OpenAI(api_key=settings.OPENAI_API_KEY)

# Define a custom exception for OpenAI errors
class OpenAIError(Exception):
    pass

async def get_openai_service():
    return OpenAIService()

class OpenAIService:
    async def generate_text(self, model: str = "text-davinci-003", prompt: str = "", temperature: float = 0.5, max_tokens: int = 100, top_p: float = 1.0) -> str:
        """Generates text using the specified OpenAI model."""
        try:
            response = await openai.completions.create(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
            )
            return response.choices[0].text
        except Exception as e:
            logger.error(f"Error generating text: {e}")
            raise OpenAIError("Error generating text.") from e

    async def translate_text(self, source_language: str, target_language: str, text: str) -> str:
        """Translates text between languages."""
        try:
            response = await openai.translations.create(
                model="gpt-3.5-turbo",
                source_language=source_language,
                target_language=target_language,
                text=text,
            )
            return response.text
        except Exception as e:
            logger.error(f"Error translating text: {e}")
            raise OpenAIError("Error translating text.") from e

    async def answer_question(self, model: str = "text-davinci-003", question: str = "") -> str:
        """Answers a question using the specified OpenAI model."""
        try:
            response = await openai.completions.create(
                model=model,
                prompt=question,
                temperature=0.0,
                max_tokens=1000,
                top_p=1.0,
            )
            return response.choices[0].text
        except Exception as e:
            logger.error(f"Error answering question: {e}")
            raise OpenAIError("Error answering question.") from e

    async def generate_code(self, model: str = "code-davinci-002", prompt: str = "", language: str = "python", temperature: float = 0.5, max_tokens: int = 100, top_p: float = 1.0) -> str:
        """Generates code in the specified language using the specified OpenAI model."""
        try:
            response = await openai.completions.create(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
            )
            return response.choices[0].text
        except Exception as e:
            logger.error(f"Error generating code: {e}")
            raise OpenAIError("Error generating code.") from e

    async def get_models(self) -> list[str]:
        """Retrieves a list of available OpenAI models."""
        try:
            models = await openai.models.list()
            return [model.id for model in models.data]
        except Exception as e:
            logger.error(f"Error retrieving models: {e}")
            raise OpenAIError("Error retrieving models.") from e