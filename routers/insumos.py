from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Insumo
from schemas import InsumoCrear, InsumoRespuesta


router = APIRouter(
    prefix="/insumos",
    tags=["Insumos"]
)


# --------------------------------------------------
# OBTENER TODOS LOS INSUMOS
# GET /insumos
# --------------------------------------------------

@router.get("/", response_model=list[InsumoRespuesta])
def obtener_insumos(
    db: Session = Depends(get_db)
):
    insumos = db.query(Insumo).all()

    return insumos


# --------------------------------------------------
# OBTENER UN INSUMO
# GET /insumos/{id}
# --------------------------------------------------

@router.get("/{id_insumo}", response_model=InsumoRespuesta)
def obtener_insumo(
    id_insumo: int,
    db: Session = Depends(get_db)
):

    insumo = db.query(Insumo).filter(
        Insumo.id_insumo == id_insumo
    ).first()

    if insumo is None:
        raise HTTPException(
            status_code=404,
            detail="Insumo no encontrado"
        )

    return insumo


# --------------------------------------------------
# CREAR UN INSUMO
# POST /insumos
# --------------------------------------------------

@router.post("/", response_model=InsumoRespuesta)
def crear_insumo(
    datos: InsumoCrear,
    db: Session = Depends(get_db)
):

    nuevo_insumo = Insumo(
        nombre=datos.nombre,
        unidad_medida=datos.unidad_medida,
        stock_actual=datos.stock_actual,
        stock_minimo=datos.stock_minimo,
        costo_actual=datos.costo_actual,
        id_proveedor=datos.id_proveedor,
        observaciones=datos.observaciones
    )

    db.add(nuevo_insumo)
    db.commit()
    db.refresh(nuevo_insumo)

    return nuevo_insumo