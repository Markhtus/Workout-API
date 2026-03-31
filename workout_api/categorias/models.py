from sqlalchemy import String, Integer
from workout_api.contrib import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CategoriaModel(BaseModel):
    __tablename__ = "categorias"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    atletas = relationship("AtletaModel", back_populates="categoria", lazy='selectin')