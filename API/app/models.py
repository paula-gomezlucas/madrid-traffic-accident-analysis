from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from .database import Base

class Bomberos(Base):
    __tablename__ = "bomberos"
    año = Column(Integer, primary_key=True)
    mes = Column(Integer, primary_key=True)
    distrito = Column(Integer, primary_key=True)
    fuegos = Column(Integer)
    agua = Column(Integer)
    construccion = Column(Integer)
    salvamento = Column(Integer)
    otros = Column(Integer)
    sin_intervencion = Column(Integer)
    total = Column(Integer)

class Localizacion(Base):
    __tablename__ = "localizacion"
    id = Column(Integer, primary_key=True, index=True)
    latitud = Column(String(255), unique=True)
    longitud = Column(String(255), unique=True)
    direccion = Column(String(255))
    distrito = Column(Integer)

class TipoPersona(Base):
    __tablename__ = "tipopersona"
    id = Column(Integer, primary_key=True, index=True)
    sexo = Column(Boolean)
    rango_edad = Column(String(20))
    tipo = Column(String(9))

class Radares(Base):
    __tablename__ = "radares"
    id = Column(Integer, primary_key=True, index=True)
    localizacion = Column(Integer, ForeignKey("localizacion.id"))
    tipo = Column(String(23))
    nombre = Column(String(255))

class Accidentes(Base):
    __tablename__ = "accidentes"
    id = Column(Integer, primary_key=True, index=True)
    num_expediente = Column(String(12), unique=True)
    fecha = Column(DateTime)
    localizacion = Column(Integer, ForeignKey("localizacion.id"))
    lesividad = Column(Integer)
    accidente = Column(Integer)
    alcohol = Column(Boolean)
    droga = Column(Boolean)
    persona = Column(Integer, ForeignKey("tipopersona.id"))
