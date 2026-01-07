from google import genai
from loguru import logger
from src.shared.config import settings

class GeminiClient:
    def __init__(self):
        """Inicializa la conexión con el motor de IA de Google."""
        try:
            # Usamos la SDK más reciente (v2.0+) de 2026
            self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
            logger.info("Cerebro de Gemini Pro inicializado correctamente.")
        except Exception as e:
            logger.error(f"Error crítico al conectar con Gemini: {e}")
            raise e

    def generar_embedding(self, texto: str):
        """
        Convierte una descripción de película o música en un vector de 768 dimensiones.
        Este vector es la 'huella dactilar' del significado del texto.
        """
        try:
            # text-embedding-004 es el estándar de alta precisión en 2026
            result = self.client.models.embed_content(
                model="text-embedding-004",
                contents=texto
            )
            # Retornamos solo la lista de números (el vector)
            return result.embeddings[0].values
        except Exception as e:
            logger.error(f"Error al transformar texto en vector: {e}")
            return None

# Instancia global: Nuestra herramienta de alquimia
ai_brain = GeminiClient()