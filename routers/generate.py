from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from services.openai_service import OpenAIService
from utils.logger import logger

from models.request import GenerateRequest
from models.response import GenerateResponse

router = APIRouter(prefix="/generate", tags=["Text Generation"])

# Initialize the OpenAI service (already initialized in `utils.config`)
openai_service = OpenAIService()

# Define the request model for text generation requests.
# Refer to `models/request.py` for more details.
class GenerateRequest(BaseModel):
    model: str = "text-davinci-003"  # Default model, can be overridden by user
    prompt: str
    temperature: float = 0.5
    max_tokens: int = 100

# Define the response model for text generation responses.
# Refer to `models/response.py` for more details.
class GenerateResponse(BaseModel):
    text: str

@router.post("/", response_model=GenerateResponse)
async def generate_text(request: GenerateRequest):
    """Generates text using OpenAI's API.

    Args:
        request (GenerateRequest): The request body containing the prompt, model, and optional parameters.

    Returns:
        GenerateResponse: The generated text in a GenerateResponse object.

    Raises:
        HTTPException: If an error occurs during text generation.
    """
    try:
        # Validate the request data using the GenerateRequest model.
        # Refer to `models/request.py` for validation rules. 
        logger.info(f"Received text generation request: {request}")

        # Generate text using the OpenAI service.
        # Refer to `services/openai_service.py` for the implementation.
        response = await openai_service.generate_text(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )

        # Format the response data into the GenerateResponse model.
        # Refer to `models/response.py` for model details.
        return GenerateResponse(text=response)

    except Exception as e:
        # Log the error and return an error response.
        logger.error(f"Error generating text: {e}")
        raise HTTPException(status_code=500, detail="Error generating text.")