from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.params import Depends
from pydantic import BaseModel

from services.openai_service import OpenAIService, get_openai_service
from utils.logger import logger

from models.response import ModelResponse

router = APIRouter(prefix="/models", tags=["Models"])

# Define the response model for retrieving models.
# Refer to `models/response.py` for more details.
class ModelResponse(BaseModel):
    models: list[str]

@router.get("/", response_model=ModelResponse)
async def get_models(openai_service: OpenAIService = Depends(get_openai_service)):
    """Retrieves a list of available OpenAI models.

    Args:
        openai_service (OpenAIService): The OpenAI service instance.

    Returns:
        ModelResponse: A list of available model names.
    """
    try:
        models = await openai_service.get_models()
        return ModelResponse(models=models)
    except Exception as e:
        logger.error(f"Error retrieving models: {e}")
        raise HTTPException(status_code=500, detail="Error retrieving models.")