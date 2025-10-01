from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 👉 Aquí pones tu usuario/contraseña correctos
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:password@localhost:5432/ofertas_db"

# Motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()
