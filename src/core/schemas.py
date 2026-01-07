from pydantic import BaseModel, Field
from typing import Literal, Optional

class ObraArtistica(BaseModel):
    """Esquema profesional para validar películas y música."""
    titulo: str = Field(..., min_length=1)
    artista_o_director: str
    genero: str
    descripcion: str = Field(..., max_length=1000)
    tipo: Literal["pelicula", "musica"]
    año: Optional[int] = None

    def a_texto_para_embedding(self) -> str:
        """Prepara el texto para que la IA lo entienda mejor."""
        return f"{self.tipo.upper()} - {self.titulo} ({self.artista_o_director}). Género: {self.genero}. Descripción: {self.descripcion}"