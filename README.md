# 🎨 ArtisticRecSys Pro: Buscador Semántico Multimodal

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Qdrant](https://img.shields.io/badge/VectorDB-Qdrant-red.svg)](https://qdrant.tech/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Infra-Docker-2496ED.svg)](https://www.docker.com/)

**ArtisticRecSys Pro** es un sistema de recomendación de vanguardia que utiliza Inteligencia Artificial Generativa y Bases de Datos Vectoriales para conectar usuarios con el arte (música y cine) a través de la intención semántica, superando las limitaciones de la búsqueda tradicional por palabras clave.

---

## Propuesta de Valor
A diferencia de los buscadores convencionales que dependen de tags o títulos exactos, este motor entiende conceptos abstractos. Puedes buscar "Algo melancólico para una noche de lluvia" y el sistema recuperará tanto canciones de Jazz como películas de cine noir, basándose en la proximidad matemática de sus significados.



---

##  Stack Tecnológico
- **Lenguaje:** Python 3.11+
- **IA/ML:** Google Gemini Pro (Modelo `text-embedding-004`) para generación de embeddings.
- **Base de Datos Vectorial:** Qdrant Corriendo en contenedor Docker.
- **Frontend:** Streamlit con diseño UI/UX personalizado.
- **Arquitectura:** Hexagonal (Domain Driven Design Lite) para asegurar la modularidad.
- **Gestión de Dependencias:** Poetry.
- **Validación de Datos:** Pydantic V2.

---

##  Arquitectura del Sistema
El proyecto sigue principios de Limpia Arquitectura, separando la lógica de negocio de la infraestructura:

* **Core:** Definición de esquemas y modelos de datos (Pydantic).
* **Infrastructure:** Clientes para servicios externos (Gemini API, Qdrant DB).
* **Shared:** Configuraciones globales y sistema de logging profesional.
* **App:** Interfaz de usuario y orquestación de servicios.

---

##  Desafíos Técnicos y Soluciones

### 1. Normalización de Señal (Score Tuning)
**Problema:** Los modelos de embedding modernos suelen concentrar los resultados en un rango de similitud de coseno muy estrecho (ej. 0.5 a 0.7), lo que resulta contraintuitivo para el usuario final.
**Solución:** Implementé una capa de post-procesamiento utilizando **Min-Max Scaling** para mapear los scores matemáticos a una escala humana de 0-100%, mejorando drásticamente la percepción de relevancia en el Dashboard.

$$S_{norm} = \frac{S_{raw} - Umbral_{min}}{Umbral_{max} - Umbral_{min}} \times 100$$

### 2. Integridad de Datos Multimodal
**Problema:** Gestionar diferentes tipos de medios (películas/música) en una misma colección vectorial.
**Solución:** Uso de **Pydantic** para forzar un contrato de datos estricto, asegurando que cada entrada posea metadatos enriquecidos que la IA pueda procesar sin errores de ejecución.

---

##  Instalación y Uso

1. **Clonar y Entorno:**
   ```bash
   git clone [https://github.com/tu-usuario/movie-recsys-pro.git](https://github.com/tu-usuario/movie-recsys-pro.git)
   cd movie-recsys-pro
   poetry install

2. **Infraestructura:**
   ```bash
docker-compose up -d

3. **Variables de Entorno: Configura tu .env con tu GEMINI_API_KEY.**

4. **Ejecución:**
   ```bash
poetry run streamlit run app.py


## Próximos Pasos:

[ ] Implementación de tests unitarios y de integración.
[ ] Despliegue en la nube mediante CI/CD (GitHub Actions).
[ ] Soporte para búsqueda por imágenes (Multimodalidad real).

Desarrollado por Felix Lezama - 2026