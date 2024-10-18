import logging
from logging.handlers import RotatingFileHandler
from typing import Optional

from utils.config import settings

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
file_handler = RotatingFileHandler(
    "logs/app.log",
    maxBytes=1024 * 1024 * 10,  # 10MB
    backupCount=5,  # Keep 5 backup files
)
file_handler.setLevel(settings.LOG_LEVEL)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)

# Format the logs
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Define custom logger methods for different log levels
def info(message: str, extra: Optional[dict] = None):
    logger.info(message, extra=extra)

def debug(message: str, extra: Optional[dict] = None):
    logger.debug(message, extra=extra)

def warning(message: str, extra: Optional[dict] = None):
    logger.warning(message, extra=extra)

def error(message: str, extra: Optional[dict] = None):
    logger.error(message, extra=extra)

def critical(message: str, extra: Optional[dict] = None):
    logger.critical(message, extra=extra)