from pydantic import BaseModel, Field
from typing import List, Optional

class ModelResponse(BaseModel):
    """
    Defines the response model for retrieving a list of available OpenAI models.

    Attributes:
        models (List[str]): A list of available OpenAI model names.
    """
    models: List[str] = Field(..., description="A list of available OpenAI models.")

class GenerateResponse(BaseModel):
    """
    Defines the response model for text generation requests.

    Attributes:
        text (str): The generated text.
    """
    text: str = Field(..., description="The generated text.")

class TranslateResponse(BaseModel):
    """
    Defines the response model for translation requests.

    Attributes:
        translated_text (str): The translated text.
    """
    translated_text: str = Field(..., description="The translated text.")

class QuestionResponse(BaseModel):
    """
    Defines the response model for question answering requests.

    Attributes:
        answer (str): The answer to the question.
    """
    answer: str = Field(..., description="The answer to the question.")

class CodeResponse(BaseModel):
    """
    Defines the response model for code generation requests.

    Attributes:
        code (str): The generated code.
    """
    code: str = Field(..., description="The generated code.")