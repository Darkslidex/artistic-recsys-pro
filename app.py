import streamlit as st
import pandas as pd
import altair as alt
from src.infrastructure.gemini_client import ai_brain
from src.infrastructure.vector_db import vector_db
from loguru import logger

# --- Configuración de la Página ---
st.set_page_config(
    page_title="ArtisticRecSys Pro",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilo CSS Personalizado ---
st.markdown("""
<style>
    /* Fondo principal y colores de texto */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Títulos y encabezados */
    h1, h2, h3 {
        color: #f0f2f6;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Tarjetas de resultados mejoradas */
    .result-card {
        background-color: #262730;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #ff4b4b; /* Línea de acento roja */
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s; /* Animación suave al pasar el mouse */
    }
    .result-card:hover {
        transform: translateY(-3px); /* Efecto de elevación */
    }
    .result-title {
        color: #ff4b4b;
        margin-bottom: 5px;
    }
    .result-meta {
        color: #a3a8b8;
        font-size: 0.9em;
    }
    /* Barra de búsqueda */
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #ffffff;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- Encabezado Principal ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("🎨 ArtisticRecSys Pro")
    st.markdown("### Tu curador de arte personal impulsado por IA.")
    st.write("Descubre música y películas que conecten con tus ideas, emociones o recuerdos. No busques por palabras, busca por **intención**.")

with col2:
    # Un toque visual extra: una imagen o logo
    st.image("https://cdn-icons-png.flaticon.com/512/2997/2997443.png", width=120)

st.markdown("---")

# --- Barra de Búsqueda y Filtros ---
with st.container():
    search_col, filter_col = st.columns([4, 1])
    with search_col:
        query = st.text_input("🔍 ¿Qué estás buscando hoy?", placeholder="Ej: Algo melancólico que suene a lluvia en una ciudad futurista...")
    with filter_col:
        # Filtro opcional para el futuro, por ahora es visual
        filtro_tipo = st.selectbox("Filtrar por:", ["Todo", "Películas", "Música"], index=0)
        
    buscar = st.button("✨ Explorar Galería", use_container_width=True, type="primary")

# --- Lógica de Búsqueda y Visualización ---
if buscar and query:
    with st.spinner("🧠 La IA está analizando tu petición y recorriendo la galería..."):
        # 1. Generar el vector de la consulta
        query_vector = ai_brain.generar_embedding(query)
        
        if query_vector:
            respuesta = vector_db.client.query_points(
                collection_name="peliculas_test",
                query=query_vector,
                limit=6
            )
            
            resultados_data = []
            
            # --- NUEVOS UMBRALES MÁS AGRESIVOS ---
            # Si el modelo da 0.40, para nosotros es "inicio de interés" (0%)
            # Si el modelo da 0.70, para nosotros es "perfecto" (100%)
            UMBRAL_MIN = 0.40 
            UMBRAL_MAX = 0.70 

            for res in respuesta.points:
                p = res.payload
                raw_score = res.score  # El valor de la IA (ej: 0.608)
                
                # Cálculo de la nueva escala humana
                if raw_score <= UMBRAL_MIN:
                    score_final = 0.0
                elif raw_score >= UMBRAL_MAX:
                    score_final = 100.0
                else:
                    # Esta fórmula "estira" la diferencia
                    score_final = ((raw_score - UMBRAL_MIN) / (UMBRAL_MAX - UMBRAL_MIN)) * 100
                
                # USAMOS ESTA VARIABLE 'score' PARA TODO LO SIGUIENTE
                score = round(score_final, 1)
                
                titulo_corto = f"{p['titulo'][:20]}..." if len(p['titulo']) > 20 else p['titulo']
                
                # MUY IMPORTANTE: Asegúrate de que aquí diga 'score' y no 'res.score'
                resultados_data.append({
                    "Título": titulo_corto,
                    "Similitud (%)": score,  # <--- ESTA ES LA CLAVE
                    "Tipo": p['tipo'].upper(),
                    "Payload": p 
                })
            
            df_resultados = pd.DataFrame(resultados_data)

            # --- Visualización: Tarjetas y Gráfico ---
            tab_tarjetas, tab_grafico = st.tabs(["🎴 Tarjetas Visuales", "📊 Radar de Similitud"])
            
            with tab_tarjetas:
                st.markdown("#### Recomendaciones Destacadas")
                cols = st.columns(2)
                for i, item in enumerate(resultados_data):
                    p = item["Payload"]
                    score = item["Similitud (%)"]
                    with cols[i % 2]:
                        st.markdown(f"""
                            <div class="result-card">
                                <h3 class="result-title">{p['titulo']}</h3>
                                <p class="result-meta"><strong>{p['tipo'].upper()}</strong> | {p['genero']}</p>
                                <p class="result-meta"><i>👤 {p['artista_o_director']}</i></p>
                                <hr style="margin: 10px 0; border-color: #30363d;">
                                <p>{p['descripcion']}</p>
                                <div style="margin-top: 10px; text-align: right;">
                                    <span style="background-color: #ff4b4b; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em;">
                                        Similitud: {score}%
                                    </span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

            with tab_grafico:
                st.markdown("#### Comparativa de Confianza de la IA")
                # Crear el gráfico de barras interactivo con Altair
                chart = alt.Chart(df_resultados).mark_bar().encode(
                    x=alt.X('Similitud (%)', title='Porcentaje de Similitud'),
                    y=alt.Y('Título', sort='-x', title='Obra'), # Ordenar por similitud descendente
                    color=alt.Color('Similitud (%)', scale=alt.Scale(scheme='reds'), legend=None), # Degradado de color rojo
                    tooltip=['Título', 'Similitud (%)', 'Tipo']
                ).properties(
                    height=400
                ).interactive() # Hacer el gráfico interactivo (zoom, pan)
                
                st.altair_chart(chart, use_container_width=True)

        else:
            st.error("❌ Hubo un problema al conectar con el cerebro de la IA (Gemini).")

# --- Barra Lateral ---
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/117303427?v=4", width=100) # Puedes poner tu foto o logo aquí
    st.title("Acerca del Proyecto")
    st.info(
        """
        Este es un sistema de recomendación multimodal de última generación.
        
        **Tecnologías Clave:**
        * 🧠 **IA:** Google Gemini Pro (Embeddings)
        * 🗄️ **Base de Datos Vectorial:** Qdrant
        * 🏗️ **Arquitectura:** Hexagonal & Microservicios (Docker)
        * 💻 **Frontend:** Streamlit
        
        Desarrollado como parte de un portafolio de Arquitectura de Software y MLOps.
        """
    )
    st.markdown("---")
    st.write("© 2026 Félix Lezama Project")