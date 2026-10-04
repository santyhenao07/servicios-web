from typing import List, Optional
from models.medicion import Medicion
from schemas.medicion import MedicionCreate, MedicionUpdate
from sqlalchemy.orm import Session


def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Medicion]:
    return db.query(Medicion).offset(skip).limit(limit).all()


def get(db: Session, medicion_id: int) -> Optional[Medicion]:
    return db.query(Medicion).filter(Medicion.id == medicion_id).first()


def create(db: Session, medicion: MedicionCreate) -> Medicion:
    db_medicion = Medicion(**medicion.model_dump())
    db.add(db_medicion)
    db.commit()
    db.refresh(db_medicion)
    return db_medicion


def update(
    db: Session, medicion_id: int, medicion: MedicionUpdate
) -> Optional[Medicion]:
    db_medicion = get(db, medicion_id)
    if not db_medicion:
        return None
    # Todas las columnas son obligatorias: un null explícito se ignora
    update_data = medicion.model_dump(exclude_unset=True, exclude_none=True)
    for key, value in update_data.items():
        setattr(db_medicion, key, value)
    db.commit()
    db.refresh(db_medicion)
    return db_medicion


def delete(db: Session, medicion_id: int) -> Optional[Medicion]:
    db_medicion = get(db, medicion_id)
    if not db_medicion:
        return None
    db.delete(db_medicion)
    db.commit()
    return db_medicion