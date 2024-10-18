from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from routers import models, generate, translate, question, code
from services.openai_service import OpenAIService
from services.auth_service import AuthService
from utils.config import settings
from utils.logger import logger

app = FastAPI(
    title="AI Wrapper MVP",
    description="Simplified Python backend for seamless OpenAI API interactions",
    version="1.0.0",
)

# Add CORS middleware to allow requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency injection for OpenAI service
@app.on_event("startup")
async def startup_event():
    app.state.openai_service = OpenAIService(settings.OPENAI_API_KEY)
    app.state.auth_service = AuthService(settings.JWT_SECRET)

# Custom exception handler for validation errors
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    logger.error(f"Validation error: {exc}")
    return JSONResponse(
        status_code=400,
        content={"message": "Invalid request data.", "details": exc.errors()},
    )

# Include routers for different API endpoints
app.include_router(models.router, prefix="/models")
app.include_router(generate.router, prefix="/generate")
app.include_router(translate.router, prefix="/translate")
app.include_router(question.router, prefix="/question")
app.include_router(code.router, prefix="/code")

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Wrapper MVP!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG
    )