from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# CONFIGURACIÓN DE LA BASE DE DATOS

DATABASE_URL = "mysql+pymysql://root:kore123@localhost/dragon_hambriento"

# Crear conexión
engine = create_engine(
    DATABASE_URL,
    echo=True
)

# Crear sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Clase base para nuestros modelos
Base = declarative_base()


# FUNCIÓN PARA OBTENER UNA SESIÓN


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()