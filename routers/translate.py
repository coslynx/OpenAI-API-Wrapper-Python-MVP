from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from services.openai_service import OpenAIService
from utils.logger import logger

from models.request import TranslateRequest
from models.response import TranslateResponse

router = APIRouter(prefix="/translate", tags=["Translation"])

# Initialize the OpenAI service (already initialized in `utils.config`)
openai_service = OpenAIService()

# Define the request model for translation requests. 
# Refer to `models/request.py` for more details.
class TranslateRequest(BaseModel):
    source_language: str
    target_language: str
    text: str

# Define the response model for translation responses.
# Refer to `models/response.py` for more details.
class TranslateResponse(BaseModel):
    translated_text: str

@router.post("/", response_model=TranslateResponse)
async def translate_text(request: TranslateRequest):
    """Translates text between languages using OpenAI's API.

    Args:
        request (TranslateRequest): The request body containing the source language, target language, and text to translate.

    Returns:
        TranslateResponse: The translated text in a TranslateResponse object.

    Raises:
        HTTPException: If an error occurs during translation.
    """
    try:
        # Validate the request data using the TranslateRequest model.
        # Refer to `models/request.py` for validation rules. 
        logger.info(f"Received translation request: {request}")

        # Translate the text using the OpenAI service.
        # Refer to `services/openai_service.py` for the implementation.
        response = await openai_service.translate_text(
            source_language=request.source_language,
            target_language=request.target_language,
            text=request.text
        )

        # Format the response data into the TranslateResponse model.
        # Refer to `models/response.py` for model details.
        return TranslateResponse(translated_text=response)

    except Exception as e:
        # Log the error and return an error response.
        logger.error(f"Error translating text: {e}")
        raise HTTPException(status_code=500, detail="Error translating text.")