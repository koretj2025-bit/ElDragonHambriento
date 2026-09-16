from fastapi import FastAPI

from routers import insumos


app = FastAPI(
    title="El Dragón Hambriento API",
    description="API para gestionar el emprendimiento de pizzetas",
    version="1.0.0"
)


# Registrar rutas
app.include_router(insumos.router)


@app.get("/")
def inicio():
    return {
        "mensaje": "API de El Dragón Hambriento funcionando 🐉🍕"
    }