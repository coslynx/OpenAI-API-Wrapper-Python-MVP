from pydantic import BaseModel, Field
from typing import Optional, List

class GenerateRequest(BaseModel):
    """
    Defines the request model for text generation requests.

    Attributes:
        model (str): The name of the OpenAI model to use for text generation. Defaults to "text-davinci-003".
        prompt (str): The text prompt to use for generating text.
        temperature (float): Controls the randomness of the generated text. Higher values (up to 1) result in more creative and unpredictable text. Defaults to 0.5.
        max_tokens (int): The maximum number of tokens to generate. Defaults to 100.
        top_p (float): Controls the diversity of the generated text. Defaults to 1.0.
        stop (Optional[List[str]]): A list of strings to stop the generation at. Defaults to None.
    """
    model: str = Field("text-davinci-003", description="The name of the OpenAI model to use for text generation.")
    prompt: str = Field(..., description="The text prompt to use for generating text.")
    temperature: float = Field(0.5, description="Controls the randomness of the generated text.")
    max_tokens: int = Field(100, description="The maximum number of tokens to generate.")
    top_p: float = Field(1.0, description="Controls the diversity of the generated text.")
    stop: Optional[List[str]] = Field(None, description="A list of strings to stop the generation at.")

class TranslateRequest(BaseModel):
    """
    Defines the request model for translation requests.

    Attributes:
        source_language (str): The language code of the source text.
        target_language (str): The language code of the target language.
        text (str): The text to translate.
    """
    source_language: str = Field(..., description="The language code of the source text.")
    target_language: str = Field(..., description="The language code of the target language.")
    text: str = Field(..., description="The text to translate.")

class QuestionRequest(BaseModel):
    """
    Defines the request model for question answering requests.

    Attributes:
        question (str): The question to answer.
        model (str): The name of the OpenAI model to use for question answering. Defaults to "text-davinci-003".
    """
    question: str = Field(..., description="The question to answer.")
    model: str = Field("text-davinci-003", description="The name of the OpenAI model to use for question answering.")

class CodeRequest(BaseModel):
    """
    Defines the request model for code generation requests.

    Attributes:
        language (str): The programming language to generate code in.
        prompt (str): The text prompt to use for generating code.
        temperature (float): Controls the randomness of the generated code. Defaults to 0.5.
        max_tokens (int): The maximum number of tokens to generate. Defaults to 100.
        top_p (float): Controls the diversity of the generated code. Defaults to 1.0.
        stop (Optional[List[str]]): A list of strings to stop the generation at. Defaults to None.
    """
    language: str = Field(..., description="The programming language to generate code in.")
    prompt: str = Field(..., description="The text prompt to use for generating code.")
    temperature: float = Field(0.5, description="Controls the randomness of the generated code.")
    max_tokens: int = Field(100, description="The maximum number of tokens to generate.")
    top_p: float = Field(1.0, description="Controls the diversity of the generated code.")
    stop: Optional[List[str]] = Field(None, description="A list of strings to stop the generation at.")