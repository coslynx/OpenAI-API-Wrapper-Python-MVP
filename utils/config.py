from typing import Optional
from pydantic import BaseSettings, Field

from utils.logger import logger


class Settings(BaseSettings):
    """Application configuration settings."""

    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    JWT_SECRET: str = Field(..., env="JWT_SECRET")
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")
    DEBUG: bool = Field(False, env="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
logger.info(f"Loaded settings: {settings.json()}")