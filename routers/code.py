from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from services.openai_service import OpenAIService
from utils.logger import logger

from models.request import CodeRequest
from models.response import CodeResponse

router = APIRouter(prefix="/code", tags=["Code Generation"])

# Initialize the OpenAI service from `utils.config`
openai_service = OpenAIService()

# Define the request model for code generation requests. 
# Refer to `models/request.py` for more details.
class CodeRequest(BaseModel):
    language: str
    prompt: str
    temperature: float = 0.5
    max_tokens: int = 100

# Define the response model for code generation responses.
# Refer to `models/response.py` for more details.
class CodeResponse(BaseModel):
    code: str

@router.post("/", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    """Generates code in a specific programming language using OpenAI's API.

    Args:
        request (CodeRequest): The request body containing the language, prompt, and optional parameters.

    Returns:
        CodeResponse: The generated code in a CodeResponse object.

    Raises:
        HTTPException: If an error occurs during code generation.
    """
    try:
        # Validate the request data using the CodeRequest model.
        # Refer to `models/request.py` for validation rules. 
        logger.info(f"Received code generation request: {request}")
        
        # Generate code using the OpenAI service. 
        # Refer to `services/openai_service.py` for the implementation.
        response = await openai_service.generate_code(
            model="code-davinci-002",  # Choose a suitable OpenAI code model. 
            prompt=request.prompt, 
            language=request.language,
            temperature=request.temperature, 
            max_tokens=request.max_tokens
        )

        # Format the response data into the CodeResponse model. 
        # Refer to `models/response.py` for model details.
        return CodeResponse(code=response)

    except Exception as e:
        # Log the error and return an error response.
        logger.error(f"Error generating code: {e}")
        raise HTTPException(status_code=500, detail="Error generating code.")