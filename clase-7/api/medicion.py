from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from crud import estudiante as crud_estudiante
from crud import medicion as crud
from schemas.medicion import MedicionCreate, MedicionResponse, MedicionUpdate

router = APIRouter(prefix="/mediciones", tags=["Mediciones"])


def validar_estudiante(db: Session, estudiante_id: int) -> None:
    if crud_estudiante.get(db, estudiante_id) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El estudiante no existe",
        )


@router.get("", response_model=List[MedicionResponse])
def listar_mediciones(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return crud.get_all(db, skip=skip, limit=limit)


@router.get("/{medicion_id}", response_model=MedicionResponse)
def obtener_medicion(medicion_id: int, db: Session = Depends(get_db)):
    db_medicion = crud.get(db, medicion_id)
    if not db_medicion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medición no encontrada",
        )
    return db_medicion


@router.post(
    "", response_model=MedicionResponse, status_code=status.HTTP_201_CREATED
)
def crear_medicion(medicion: MedicionCreate, db: Session = Depends(get_db)):
    validar_estudiante(db, medicion.estudiante_id)
    return crud.create(db, medicion)


@router.put("/{medicion_id}", response_model=MedicionResponse)
def reemplazar_medicion(
    medicion_id: int, medicion: MedicionCreate, db: Session = Depends(get_db)
):
    validar_estudiante(db, medicion.estudiante_id)
    db_medicion = crud.update(
        db, medicion_id, MedicionUpdate(**medicion.model_dump())
    )
    if not db_medicion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medición no encontrada",
        )
    return db_medicion


@router.patch("/{medicion_id}", response_model=MedicionResponse)
def actualizar_medicion(
    medicion_id: int, medicion: MedicionUpdate, db: Session = Depends(get_db)
):
    if medicion.estudiante_id is not None:
        validar_estudiante(db, medicion.estudiante_id)
    db_medicion = crud.update(db, medicion_id, medicion)
    if not db_medicion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medición no encontrada",
        )
    return db_medicion


@router.delete("/{medicion_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_medicion(medicion_id: int, db: Session = Depends(get_db)):
    db_medicion = crud.delete(db, medicion_id)
    if not db_medicion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medición no encontrada",
        )
    return None