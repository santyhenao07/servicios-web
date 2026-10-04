from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from crud import estudiante as crud
from database import get_db
from schemas.estudiante import EstudianteCreate, EstudianteResponse, EstudianteUpdate

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

@router.get("", response_model=list[EstudianteResponse])
def listar_estudiantes(db: Session = Depends(get_db)):
    return crud.get_all(db)

@router.get("/{estudiante_id}", response_model=EstudianteResponse)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = crud.get(db, estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="El estudiante no existe")
    return estudiante

@router.post("", response_model=EstudianteResponse, status_code=status.HTTP_201_CREATED)
def agregar_estudiante(data: EstudianteCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)

@router.put("/{estudiante_id}", response_model=EstudianteResponse)
def reemplazar_estudiante(estudiante_id: int, data: EstudianteCreate, db: Session = Depends(get_db)):
    estudiante = crud.get(db, estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="El estudiante no existe")
    return crud.update(db, estudiante, EstudianteUpdate(**data.model_dump()))

@router.patch("/{estudiante_id}", response_model=EstudianteResponse)
def actualizar_estudiante(estudiante_id: int, data: EstudianteUpdate, db: Session = Depends(get_db)):
    estudiante = crud.get(db, estudiante_id)
    if estudiante is None:
        raise HTTPException(status_code=404, detail="El estudiante no existe")
    return crud.update(db, estudiante, data)


