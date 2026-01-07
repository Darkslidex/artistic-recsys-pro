# 🎨 ArtisticRecSys Pro
### Buscador Semántico Multimodal de Cine y Música

A diferencia de los buscadores convencionales que dependen de tags o títulos exactos, este motor entiende **conceptos abstractos**. Puedes buscar *"Algo melancólico para una noche de lluvia"* y el sistema recuperará tanto canciones de Jazz como películas de cine noir, basándose en la proximidad matemática de sus significados.

---

##  Stack Tecnológico

* **Lenguaje:** Python 3.11+
* **IA/ML:** Google Gemini Pro (`text-embedding-004`).
* **Base de Datos Vectorial:** Qdrant (Docker).
* **Frontend:** Streamlit.
* **Arquitectura:** Hexagonal (DDD Lite).

---

##  Arquitectura del Sistema

* **Core:** Definición de esquemas y modelos de datos (Pydantic).
* **Infrastructure:** Clientes para Gemini API y Qdrant DB.
* **Shared:** Configuraciones globales y sistema de logging.
* **App:** Interfaz de usuario (Streamlit).

---

##  Desafíos Técnicos y Soluciones

### 1. Normalización de Señal (Score Tuning)
Implementé una capa de post-procesamiento utilizando **Min-Max Scaling** para mapear los scores matemáticos (0.4 - 0.7) a una escala humana de 0-100%, mejorando la percepción de relevancia.

### 2. Integridad de Datos Multimodal
Uso de **Pydantic** para forzar un contrato de datos estricto, asegurando que cada entrada posea metadatos enriquecidos para su procesamiento.

---

##  Instalación y Uso

### 1. Clonar y Entorno
```bash
git clone [https://github.com/Darkslidex/artistic-recsys-pro.git](https://github.com/Darkslidex/artistic-recsys-pro.git)
cd artistic-recsys-pro
poetry install
```

### 2. Infraestructura
Levanta la base de datos vectorial con Docker:
```bash
docker-compose up -d
```

### 3. Configuración
Crea un archivo `.env` en la raíz y añade tu llave:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

### 4. Ejecución
Inicia la interfaz gráfica:
```bash
poetry run streamlit run app.py
```

---

##  Próximos Pasos
- [ ] Implementación de tests unitarios.
- [ ] Despliegue en la nube mediante CI/CD.

**Desarrollado por Felix Lezama - 2026**



# 🎨 ArtisticRecSys Pro v1.0.0
### Buscador Semántico Multimodal en la Nube

Este proyecto ha evolucionado de un prototipo local a una aplicación **SaaS (Software as a Service)** que utiliza IA para conectar conceptos abstractos entre cine y música.

---

##  Despliegue en Vivo
Puedes probar la aplicación aquí: **https://moviemusicsearch.streamlit.app/**

## 🛠️ Evolución Técnica y Stack
* **Cerebro:** Google Gemini Pro (`text-embedding-004`) para embeddings vectoriales.
* **Memoria:** Qdrant Cloud (Vector Database) con persistencia global.
* **Frontend:** Streamlit Cloud.
* **Arquitectura:** Hexagonal (DDD Lite) preparada para escalabilidad.

##  Hitos de Desarrollo (Fixes Críticos)
Durante la fase de despliegue, se resolvieron los siguientes retos:
1. **Compatibilidad Pydantic V2:** Migración de esquemas de validación para entornos modernos.
2. **Protocolo de Red:** Implementación de conexión segura vía REST/HTTPS para Qdrant Cloud.
3. **Gestión de Entornos:** Configuración de `package-mode = false` en Poetry para despliegues CI/CD.

##  Configuración de Secretos
Para replicar este proyecto, se requieren las siguientes variables de entorno:
* `GEMINI_API_KEY`: Acceso a la API de Google AI Studio.
* `QDRANT_URL`: Endpoint de tu cluster en la nube.
* `QDRANT_API_KEY`: Llave de autenticación de Qdrant.

**Desarrollado por Felix Lezama - Enero 2026**
