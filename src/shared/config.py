from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger
import sys
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "ArtisticRecSys"
    GEMINI_API_KEY: str
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    
    # Buscamos el archivo .env en la raíz
    model_config = SettingsConfigDict(env_file=".env")

def setup_logging():
    logger.remove()
    logger.add(sys.stdout, colorize=True, format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>")
    # Creamos la carpeta logs si no existe para evitar errores
    if not os.path.exists("logs"):
        os.makedirs("logs")
    logger.add("logs/error_audit.log", rotation="10 MB", level="ERROR")

settings = Settings()