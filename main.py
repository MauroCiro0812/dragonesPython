from fastapi import FastAPI
from app.database.config import engine
from app.api.models.tablas import Base
from starlette.responses import RedirectResponse
from app.api.routers.endPoints import rutas

from starlette.middleware.cors import CORSMiddleware

#alistar el ambiente para desarrollar y probar
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def main():
    return RedirectResponse(url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen. Ajusta según sea necesario.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP. Ajusta según sea necesario.
    allow_headers=["*"],  # Permite todas las cabeceras. Ajusta según sea necesario.
)

app.include_router(rutas)