from database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship


class Medicion(Base):
    __tablename__ = "mediciones"

    id = Column(Integer, primary_key=True, index=True)
    estudiante_id = Column(
        Integer, ForeignKey("estudiantes.id"), nullable=False
    )
    variable = Column(String(50), nullable=False)
    valor = Column(Numeric, nullable=False)
    unidad = Column(String(20), nullable=False)
    fecha_hora = Column(DateTime(timezone=True), nullable=False)

    estudiante = relationship("Estudiante")