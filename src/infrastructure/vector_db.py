from qdrant_client import QdrantClient
from qdrant_client.http import models
from loguru import logger
from src.shared.config import settings

class VectorStorage:
    def __init__(self):
        try:
            # SI HAY UNA API KEY EN EL .ENV, CONECTAMOS A LA NUBE
            if settings.QDRANT_API_KEY:
                self.client = QdrantClient(
                    url=settings.QDRANT_URL,
                    api_key=settings.QDRANT_API_KEY
                )
                logger.info(f"🚀 CONEXIÓN EXITOSA A QDRANT CLOUD")
            else:
                # SI NO HAY API KEY, CONECTAMOS AL DOCKER LOCAL
                self.client = QdrantClient(
                    host=settings.QDRANT_HOST, 
                    port=settings.QDRANT_PORT,
                    https=False 
                )
                logger.info(f"🏠 Conexión local a Qdrant exitosa")
        except Exception as e:
            logger.error(f"Error conectando a Qdrant: {str(e)}")
            raise e

    def create_collection(self, collection_name: str, vector_size: int):
        try:
            if not self.client.collection_exists(collection_name):
                self.client.create_collection(
                    collection_name=collection_name,
                    vectors_config=models.VectorParams(
                        size=vector_size, 
                        distance=models.Distance.COSINE
                    ),
                )
                logger.success(f"Colección '{collection_name}' creada.")
        except Exception as e:
            logger.error(f"Error al crear colección: {e}")

vector_db = VectorStorage()