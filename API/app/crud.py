from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas

def get_accidente_by_num_expediente(db: Session, num_expediente: str):
    return db.query(models.Accidentes).filter(models.Accidentes.num_expediente == num_expediente).first()

def create_accidente(db: Session, accidente: schemas.AccidentesCreate):
    db_accidente = models.Accidentes(**accidente.dict())
    db.add(db_accidente)
    db.commit()
    db.refresh(db_accidente)
    return db_accidente

def delete_accidente(db: Session, accidente_id: int):
    db.query(models.Accidentes).filter(models.Accidentes.id == accidente_id).delete()
    db.commit()


def get_accidentes_count(db: Session):
    return db.query(func.count(models.Accidentes.id)).scalar()

def get_accidentes_by_lesividad(db: Session, lesividad: int):
    return db.query(models.Accidentes).filter(models.Accidentes.lesividad == lesividad).all()