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
@rutas.post("/dragones",response_model=DragonDTORespuesta,summary="Crea un Dragon en la BD",description="Crear Dragon",tags=["Dragones"])

def crearDragon(datosCliente:DragonDTOPeticion,db:Session=Depends(getDb())):
    try:
        dragon = Dragon(
            nombres=datosCliente.nombres,
            edad=datosCliente.edad,
            altura=datosCliente.altura,
            numeroVictorias=datosCliente.numeroVictorias
        )
        db.add(dragon) #orden en bd
        db.commit() #valido la operacion que acabo de realizar
        db.refresh(dragon) #actualizo la variable dragon con los datos de la bd
        return dragon
        
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Tenemos un problema en el servidor: {error}")
    

@rutas.get("/dragones", response_model=List[DragonDTORespuesta], summary="Servicio que lista todos los Dragones en la BD")
def buscarDragones(db:Session=Depends(getDb())):
    try:
        dragones = db.query(Dragon).all()
        return dragones
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Tenemos un problema en el servidor: {error}")


@rutas.get("/dragones/{id}", response_model=DragonDTORespuesta, summary="Servicio que busca un Dragon por su ID en la BD")
def buscarDragonPorId(id:int,db:Session=Depends(getDb())):
    try:
        dragon = db.query(Dragon).get(id)
        return dragon
    
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Tenemos un problema en el servidor: {error}")

    
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