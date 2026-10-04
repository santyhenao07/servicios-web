from sqlalchemy import select
from sqlalchemy.orm import Session
from models.estudiante import Estudiante
from schemas.estudiante import EstudianteCreate, EstudianteUpdate

def get_all(db: Session) -> list[Estudiante]:
    return list(db.scalars(select(Estudiante).order_by(Estudiante.id)).all())

def get(db: Session, estudiante_id: int) -> Estudiante | None:
    return db.get(Estudiante, estudiante_id)

def create(db: Session, data: EstudianteCreate) -> Estudiante:
    estudiante = Estudiante(**data.model_dump())
    db.add(estudiante)
    db.commit()
    db.refresh(estudiante)
    return estudiante

def update(db: Session, estudiante: Estudiante, data: EstudianteUpdate) -> Estudiante:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(estudiante, field, value)
    db.commit()
    db.refresh(estudiante)
    return estudiante

def delete(db: Session, estudiante: Estudiante) -> None:
    db.delete(estudiante)
    db.commit()

