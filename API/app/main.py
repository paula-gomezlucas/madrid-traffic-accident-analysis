from fastapi import FastAPI, Depends, HTTPException
from typing import List 
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/accidentes/{num_expediente}", response_model=schemas.Accidentes)
def read_accidente(num_expediente: str, db: Session = Depends(get_db)):
    db_accidente = crud.get_accidente_by_num_expediente(db, num_expediente=num_expediente)
    if db_accidente is None:
        raise HTTPException(status_code=404, detail="Accidente not found")
    return db_accidente

@app.post("/accidentes/", response_model=schemas.Accidentes)
def create_accidente(accidente: schemas.Accidentes, db: Session = Depends(get_db)):
    return crud.create_accidente(db=db, accidente=accidente)

@app.delete("/accidentes/{accidente_id}")
def delete_accidente(accidente_id: int, db: Session = Depends(get_db)):
    crud.delete_accidente(db=db, accidente_id=accidente_id)
    return {"msg": "Accidente deleted"}

@app.get("/accidentes/count")
def read_accidentes_count(db: Session = Depends(get_db)):
    count = crud.get_accidentes_count(db)
    return {"count": count}

@app.get("/accidentes/lesividad/{lesividad}", response_model=List[schemas.Accidentes])
def read_accidentes_by_lesividad(lesividad: int, db: Session = Depends(get_db)):
    accidentes = crud.get_accidentes_by_lesividad(db, lesividad=lesividad)
    return accidentes
