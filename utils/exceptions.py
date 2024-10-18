from fastapi import HTTPException, status

class APIError(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(message)
        self.status_code = status_code

class AuthenticationError(APIError):
    def __init__(self, message: str = "Authentication required."):
        super().__init__(message, status_code=status.HTTP_401_UNAUTHORIZED)

class ValidationError(APIError):
    def __init__(self, message: str = "Invalid request data.", details: dict = None):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST)
        self.details = details

class OpenAIError(APIError):
    def __init__(self, message: str = "OpenAI API error.", details: dict = None):
        super().__init__(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.details = details

class DatabaseError(APIError):
    def __init__(self, message: str = "Database error.", details: dict = None):
        super().__init__(message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        self.details = details

class NotFoundError(APIError):
    def __init__(self, message: str = "Resource not found.", details: dict = None):
        super().__init__(message, status_code=status.HTTP_404_NOT_FOUND)
        self.details = details