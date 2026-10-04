from pydantic import BaseModel, ConfigDict

class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    correo: str
    programa: str
    grupo: str

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    correo: str | None = None
    programa: str | None = None
    grupo: str | None = None

class EstudianteResponse(EstudianteBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
