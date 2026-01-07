from src.infrastructure.vector_db import vector_db
from loguru import logger

def limpiar_galeria():
    nombre_coleccion = "peliculas_test"
    try:
        # Borramos la colección con los datos viejos
        vector_db.client.delete_collection(collection_name=nombre_coleccion)
        logger.warning(f"Colección '{nombre_coleccion}' eliminada. Limpiando datos antiguos...")
        
        # La creamos de nuevo (768 es el tamaño de Gemini)
        vector_db.create_collection(nombre_coleccion, 768)
        logger.success("¡Galería lista para las nuevas 100 obras!")
    except Exception as e:
        logger.error(f"Error al limpiar: {e}")

if __name__ == "__main__":
    limpiar_galeria()