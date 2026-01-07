from src.infrastructure.vector_db import vector_db
from src.shared.config import settings, setup_logging
from loguru import logger

def main():
    # 1. Iniciamos los logs hermosos
    setup_logging()
    
    logger.info(f"Iniciando verificación para el proyecto: {settings.PROJECT_NAME}")
    
    # 2. Intentamos hablar con Qdrant
    try:
        # 768 es el tamaño estándar de los vectores de Gemini
        vector_db.create_collection("peliculas_test", 768)
        logger.success("--- SPRINT 1 COMPLETADO CON ÉXITO ---")
        logger.info("Python, Docker, Qdrant y .env están sincronizados.")
    except Exception as e:
        logger.critical(f"El sistema falló en la conexión: {e}")

if __name__ == "__main__":
    main()