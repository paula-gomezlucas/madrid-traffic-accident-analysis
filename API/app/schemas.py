from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Bomberos(BaseModel):
    año: int
    mes: int
    distrito: int
    fuegos: int
    agua: int
    construccion: int
    salvamento: int
    otros: int
    sin_intervencion: int
    total: int

class Localizacion(BaseModel):
    id: int
    latitud: str
    longitud: str
    direccion: str
    distrito: int

class TipoPersona(BaseModel):
    id: int
    sexo: bool
    rango_edad: str
    tipo: str

class Radares(BaseModel):
    id: int
    localizacion: int
    tipo: str
    nombre: str

class Accidentes(BaseModel):
    id: int
    num_expediente: str
    fecha: datetime
    localizacion: int
    lesividad: int
    accidente: int
    alcohol: bool
    droga: bool
    persona: int

class AccidentesCreate(BaseModel):
    num_expediente: str
    fecha: datetime
    localizacion: int
    lesividad: int
    accidente: int
    alcohol: bool
    droga: bool
    persona: int