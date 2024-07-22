from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.dtos import DragonDTOPeticion,DragonDTORespuesta,JineteDTOPeticion,JineteDTORespuesta,AliadoDTOPeticion,AliadoDTORespuesta
from app.api.models.tablas import Dragon,Jinete,Aliado
from app.database.config import SessionLocal, engine

rutas = APIRouter()

def getDb():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

#ENDPOINTS PARA EL API
def crearDragon():
    pass
def buscarDragones():
    pass
def buscarDragonPorId():
    pass
def modificarDragonPorId():
    pass
def eliminarDragonPorId():
    pass


def crearJinete():
    pass
def buscarJinetes():
    pass
def buscarJinetePorId():
    pass
def modificarJinetePorId():
    pass
def eliminarJinetePorId():
    pass


def crearAliado():
    pass
def buscarAliados():
    pass
def buscarAliadoPorId():
    pass
def modificarAliadoPorId():
    pass
def eliminarAliadoPorId():
    pass