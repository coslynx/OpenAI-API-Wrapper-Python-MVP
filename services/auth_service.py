from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional

from utils.config import settings
from utils.logger import logger
from utils.auth import create_access_token, verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    username: str = None

async def get_current_user(token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends(get_auth_service)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await auth_service.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_auth_service():
    return AuthService(settings.JWT_SECRET)

class AuthService:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    async def authenticate_user(self, username: str, password: str):
        user = await self.get_user(username)
        if user is None:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return True

    async def get_user(self, username: str):
        # Replace with your actual user retrieval logic
        # Example: Query a database
        return {"username": username}

    async def create_access_token(self, data: dict):
        return create_access_token(data, settings.JWT_SECRET, settings.ALGORITHM)

    async def create_refresh_token(self, data: dict):
        # Replace with your actual refresh token generation logic
        return "refresh_token"