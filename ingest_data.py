import json
import uuid
from tqdm import tqdm
from loguru import logger
from src.infrastructure.gemini_client import ai_brain
from src.infrastructure.vector_db import vector_db
from src.core.schemas import ObraArtistica
from src.shared.config import setup_logging

def ejecutar_ingesta_masiva():
    setup_logging()

    # --- NUEVA LÍNEA PARA CREAR LA COLECCIÓN ---
    # Gemini text-embedding-004 usa 768 dimensiones
    logger.info("Verificando colección en la nube...")
    vector_db.create_collection(collection_name="peliculas_test", vector_size=768)
    # -------------------------------------------
    
    # 1. Cargar el "Lienzo" de datos
    try:
        with open('data/art_collection.json', 'r', encoding='utf-8') as f:
            dataset = json.load(f)
    except FileNotFoundError:
        logger.error("No se encontró el archivo de datos. Asegúrate de crear data/art_collection.json")
        return

    logger.info(f"🎨 Iniciando la siembra masiva de {len(dataset)} obras...")

    # Usamos tqdm para una barra de progreso profesional
    for data in tqdm(dataset, desc="Procesando arte"):
        try:
            # Validación con nuestro esquema Pydantic
            obra = ObraArtistica(**data)
            
            # Evitamos duplicados: Podríamos buscar antes de insertar, 
            # pero por ahora usaremos upsert con ID basado en el título
            obra_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, obra.titulo))
            
            # Generar Embedding
            vector = ai_brain.generar_embedding(obra.a_texto_para_embedding())

            if vector:
                vector_db.client.upsert(
                    collection_name="peliculas_test",
                    points=[{
                        "id": obra_id,
                        "vector": vector,
                        "payload": obra.model_dump()
                    }]
                )
        except Exception as e:
            logger.error(f"Error procesando {data.get('titulo')}: {e}")

    logger.success("✅ ¡Galería completada! El sistema está listo para cualquier búsqueda.")

if __name__ == "__main__":
    ejecutar_ingesta_masiva()