from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    apellido: Mapped[str] = mapped_column(String(150), nullable=False)
    correo: Mapped[str] = mapped_column(String(200), nullable=False)
    programa: Mapped[str] = mapped_column(String(200), nullable=False)
    grupo: Mapped[str] = mapped_column(String(100), nullable=False)
