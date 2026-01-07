from src.infrastructure.gemini_client import ai_brain
from src.infrastructure.vector_db import vector_db
from src.shared.config import setup_logging
from loguru import logger

def buscar_recomendacion(consulta_usuario: str):
    setup_logging()
    
    logger.info(f"Buscando arte para: '{consulta_usuario}'")

    # 1. El Alquimista genera el vector de la pregunta
    query_vector = ai_brain.generar_embedding(consulta_usuario)

    if query_vector:
        # 2. Buscamos en la galería (Qdrant)
        respuesta = vector_db.client.query_points(
            collection_name="peliculas_test",
            query=query_vector,
            limit=3
        )

        print("\n" + "="*40)
        print("🎨 RECOMENDACIONES DE TU IA".center(40))
        print("="*40)

        for i, res in enumerate(respuesta.points, 1):
            puntuacion = round(res.score * 100, 2)
            p = res.payload # Aquí están nuestros datos validados
            
            # Usamos los nombres del esquema: 'descripcion' y 'artista_o_director'
            print(f"{i}. {p['titulo']} ({p['artista_o_director']})")
            print(f"   Tipo: {p['tipo'].upper()} | Género: {p['genero']}")
            print(f"   Similitud: {puntuacion}%")
            print(f"   Resumen: {p['descripcion']}") # <--- Cambio clave aquí
            print("-" * 40)

if __name__ == "__main__":
    pregunta = "Busco una pelicula de una persona que se enamore de una sistema operativo inteligente."
    buscar_recomendacion(pregunta)