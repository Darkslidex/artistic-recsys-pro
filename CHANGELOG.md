# CHANGELOG

Toda la posteridad de este proyecto será registrada aquí bajo el estándar de "Keep a Changelog".

## [0.3.0] - 2026-01-07

### Added
- **Interfaz Gráfica Profesional (Dashboard):** Implementación de una aplicación web moderna utilizando `Streamlit`, con diseño oscuro personalizado y tarjetas de resultados con efectos visuales.
- **Visualización Analítica:** Integración de gráficos de barras interactivos con `Altair` para comparar visualmente los niveles de confianza de la IA en cada recomendación.
- **Navegación por Pestañas:** Organización del contenido en vistas separadas de "Tarjetas Visuales" y "Radar de Similitud" para una mejor experiencia de usuario.

### Changed
- **Calibración de Relevancia (UX-Driven):** Implementación de un algoritmo de normalización (Min-Max Scaling) para transformar los scores matemáticos crudos en porcentajes de similitud más intuitivos y humanos.
- **Refactorización del Motor de Búsqueda:** Optimización de la lógica de visualización para soportar metadatos enriquecidos y filtrado por tipo de obra (Película/Música).

### Fixed
- **Percepción de Acierto:** Ajuste de los umbrales de confianza para eliminar el "ruido" semántico y resaltar las coincidencias conceptuales más fuertes.


## [0.2.2] - 2026-01-06

### Added
- **Script de Mantenimiento:** Creación de `reset_db.py` para la depuración controlada de colecciones, permitiendo reinicios limpios del entorno de datos.
- **Dataset Masivo:** Integración de un catálogo curado de 100 obras (50 películas y 50 canciones) con diversidad de géneros y metadatos completos.

### Fixed
- **Integridad Referencial:** Solución definitiva al `KeyError: 'artista_o_director'` mediante la purga de datos antiguos (legacy) y la re-ingesta bajo el nuevo esquema validado.

### Changed
- **Pipeline de Ingesta:** Optimización del proceso de carga masiva utilizando la librería `tqdm` para monitorización de progreso en tiempo real y generación de IDs únicos basados en el contenido (UUID5).


## [0.2.1] - 2026-01-06

### Fixed
- **Consistencia de Esquemas:** Corrección de `KeyError` en el motor de búsqueda al sincronizar los nombres de los campos con el esquema de validación `ObraArtistica`.
- **Integridad de Datos:** Sustitución del campo efímero `desc` por el campo validado `descripcion` en todo el pipeline.

### Changed
- **Visualización de Resultados:** Mejora en la interfaz de terminal del buscador para incluir el nombre del artista/director y el género, enriqueciendo la experiencia de usuario.
- **Formateo de Salida:** Implementación de separadores visuales y centrado de texto en los resultados de búsqueda para una lectura más clara.


## [0.2.0] - 2026-01-06

### Added
- **Integración con Gemini Pro:** Implementación de `GeminiClient` para la generación de embeddings de alta fidelidad (modelo `text-embedding-004`).
- **Pipeline de Ingesta:** Creación de script de siembra automatizada para transformar descripciones de texto en vectores y almacenarlos en Qdrant.
- **Buscador Semántico:** Desarrollo de motor de búsqueda basado en "intención" del usuario, permitiendo consultas en lenguaje natural.

### Fixed
- **Actualización de API Qdrant:** Migración del método deprecado `client.search()` al nuevo estándar `client.query_points()` para compatibilidad con la SDK 2026.
- **Manejo de Resultados:** Ajuste en la estructura de desempaquetado de puntos para procesar la nueva respuesta `.points` de Qdrant.


## [0.1.0] - 2026-01-06

### Added
- **Gestión de dependencias:** Configuración inicial con Poetry 2.2.1 para un entorno determinístico.
- **Infraestructura de Datos:** Orquestación de base de datos vectorial Qdrant mediante Docker Compose.
- **Arquitectura Base:** Creación de estructura de carpetas bajo principios de Arquitectura Hexagonal (`src/api`, `src/core`, `src/infrastructure`).
- **Sistema de Auditoría:** Implementación de logging profesional con la librería `loguru`, incluyendo rotación de archivos de error.
- **Seguridad:** Configuración de variables de entorno mediante archivos `.env` y validación con `pydantic-settings`.

### Fixed
- **Permisos en Windows:** Solución al error de ejecución de scripts en PowerShell (`Set-ExecutionPolicy`).
- **PATH de Poetry:** Configuración manual de la ruta de binarios de Python para reconocer el comando `poetry` en el terminal de VS Code.