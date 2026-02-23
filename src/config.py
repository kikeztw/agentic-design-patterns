from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
  """
  System configuration using Pydantic Settings.
  Read automatically from .env file.
  """

  # OpenAI
  openai_api_key: Optional[str] = None
  model_name: str = "gpt-4o-mini"
  
  # Agent parameters
  max_iterations: int = 3
  quality_threshold: float = 8.0
  temperature: float = 0.
  
  class Config:
    env_file = "../.env"
    env_file_encoding = "utf-8"

# Global configuration instance
settings = Settings()