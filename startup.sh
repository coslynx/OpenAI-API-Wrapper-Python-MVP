#!/bin/bash

# Author: AI
# Description: Startup script for AI Wrapper MVP

# Set color codes for logging
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

# Define error handling function
error() {
  echo -e "${RED}Error: $1${NC}"
  exit 1
}

# Define success logging function
success() {
  echo -e "${GREEN}Success: $1${NC}"
}

# Define warning logging function
warn() {
  echo -e "${YELLOW}Warning: $1${NC}"
}

# Define main function for script execution
main() {
  # Source environment variables from .env
  source .env

  # Check if required environment variables are set
  if [ -z "$OPENAI_API_KEY" ]; then
    error "OPENAI_API_KEY is not set in .env file!"
  fi

  # Check if required environment variables are set
  if [ -z "$DEBUG" ]; then
    error "DEBUG is not set in .env file!"
  fi

  # Install project dependencies
  success "Installing project dependencies..."
  pip install -r requirements.txt

  # Start the FastAPI application
  success "Starting FastAPI application..."
  if [ "$DEBUG" == "True" ]; then
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  else
    uvicorn main:app --host 0.0.0.0 --port 8000
  fi

  # Display success message
  success "AI Wrapper MVP is running! Access it at http://localhost:8000"
}

# Define trap handler for script interruption
trap "echo -e '${RED}Interrupted!${NC}'; exit" INT TERM

# Main script execution
main

# End of script