from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class MedicionBase(BaseModel):
    estudiante_id: int = Field(..., description="ID del estudiante relacionado")
    variable: str = Field(..., max_length=50, description="Nombre de la medición")
    valor: float = Field(..., description="Valor registrado")
    unidad: str = Field(..., max_length=20, description="Unidad de medida")
    fecha_hora: datetime = Field(..., description="Fecha y hora de la medición")


class MedicionCreate(MedicionBase):
    pass


class MedicionUpdate(BaseModel):
    estudiante_id: Optional[int] = None
    variable: Optional[str] = Field(default=None, max_length=50)
    valor: Optional[float] = None
    unidad: Optional[str] = Field(default=None, max_length=20)
    fecha_hora: Optional[datetime] = None


class MedicionResponse(MedicionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)