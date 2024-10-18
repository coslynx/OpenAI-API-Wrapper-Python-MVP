from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from services.openai_service import OpenAIService
from utils.logger import logger

from models.request import QuestionRequest
from models.response import QuestionResponse

router = APIRouter(prefix="/question", tags=["Question Answering"])

# Initialize the OpenAI service (already initialized in `utils.config`)
openai_service = OpenAIService()

# Define the request model for question answering requests. 
# Refer to `models/request.py` for more details.
class QuestionRequest(BaseModel):
    question: str
    model: str = "text-davinci-003"  # Default model, can be overridden by user

# Define the response model for question answering responses.
# Refer to `models/response.py` for more details.
class QuestionResponse(BaseModel):
    answer: str

@router.post("/", response_model=QuestionResponse)
async def answer_question(request: QuestionRequest):
    """Answers a question using OpenAI's API.

    Args:
        request (QuestionRequest): The request body containing the question and optional model.

    Returns:
        QuestionResponse: The answer to the question in a QuestionResponse object.

    Raises:
        HTTPException: If an error occurs during question answering.
    """
    try:
        # Validate the request data using the QuestionRequest model.
        # Refer to `models/request.py` for validation rules. 
        logger.info(f"Received question answering request: {request}")

        # Answer the question using the OpenAI service.
        # Refer to `services/openai_service.py` for the implementation.
        response = await openai_service.answer_question(
            model=request.model,  # Use the user-specified model or the default
            question=request.question
        )

        # Format the response data into the QuestionResponse model.
        # Refer to `models/response.py` for model details.
        return QuestionResponse(answer=response)

    except Exception as e:
        # Log the error and return an error response.
        logger.error(f"Error answering question: {e}")
        raise HTTPException(status_code=500, detail="Error answering question.")