from sqlalchemy import Column, Integer, String, Numeric
from database import Base


class Insumo(Base):
    __tablename__ = "insumos"

    id_insumo = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre = Column(
        String(100),
        nullable=False
    )

    unidad_medida = Column(
        String(20),
        nullable=False
    )

    stock_actual = Column(
        Numeric(10, 3),
        nullable=False,
        default=0
    )

    stock_minimo = Column(
        Numeric(10, 3),
        nullable=False,
        default=0
    )

    costo_actual = Column(
        Numeric(10, 2),
        nullable=False,
        default=0
    )

    id_proveedor = Column(
        Integer,
        nullable=True
    )

    observaciones = Column(
        String(255),
        nullable=True
    )