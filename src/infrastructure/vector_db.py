from qdrant_client import QdrantClient
from qdrant_client.http import models
from loguru import logger
from src.shared.config import settings

class VectorStorage:
    def __init__(self):
        try:
            # Forzamos https=False para evitar el bloqueo que viste en el log
            self.client = QdrantClient(
                host=settings.QDRANT_HOST, 
                port=settings.QDRANT_PORT,
                https=False 
            )
            logger.info(f"Conexión exitosa a Qdrant en {settings.QDRANT_HOST}")
        except Exception as e:
            logger.error(f"Error conectando a Qdrant: {str(e)}")
            raise e

    def create_collection(self, collection_name: str, vector_size: int):
        """Crea una colección si no existe."""
        try:
            if not self.client.collection_exists(collection_name):
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=models.VectorParams(
                        size=vector_size, 
                        distance=models.Distance.COSINE
                    ),
                )
                logger.success(f"Colección '{collection_name}' creada con éxito.")
            else:
                logger.info(f"La colección '{collection_name}' ya existe.")
        except Exception as e:
            logger.error(f"Error al crear la colección: {e}")

# Instancia global
vector_db = VectorStorage()