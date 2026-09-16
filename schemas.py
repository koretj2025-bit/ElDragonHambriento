from pydantic import BaseModel
from typing import Optional


class InsumoBase(BaseModel):
    nombre: str
    unidad_medida: str
    stock_actual: float = 0
    stock_minimo: float = 0
    costo_actual: float = 0
    id_proveedor: Optional[int] = None
    observaciones: Optional[str] = None


class InsumoCrear(InsumoBase):
    pass


class InsumoRespuesta(InsumoBase):
    id_insumo: int

    class Config:
        from_attributes = True