from pydantic_settings import BaseSettings, SettingsConfigDict
from loguru import logger
import sys
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "ArtisticRecSys"
    GEMINI_API_KEY: str
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    # Añadimos estos dos para la nube
    QDRANT_URL: str = "https://b2479c56-d225-48cb-973d-dcc50d7d5d3d.us-east4-0.gcp.cloud.qdrant.io" 
    QDRANT_API_KEY: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.CtyMBu4bbXDNbOGWctYQJsOEE-UO3ZbQJO8sQ6xDL4I"

# --- LA CORRECCIÓN ESTÁ AQUÍ ---
    # En Pydantic V2 usamos SettingsConfigDict en lugar de class Config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding='utf-8',
        extra='ignore' # Esto evita errores si hay variables extra en el .env
    )

settings = Settings()

# --- FUNCIÓN QUE FALTABA ---
def setup_logging():
    """Configura el formato de los logs para que se vean profesionales."""
    logger.remove() # Eliminamos el log por defecto
    logger.add(
        sys.stderr, 
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )