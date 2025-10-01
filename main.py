from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Ofertas 🚀")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- Empresas ----
@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db=db, empresa=empresa)

@app.get("/empresas/", response_model=list[schemas.Empresa])
def read_empresas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_empresas(db, skip=skip, limit=limit)

# ---- Ofertas ----
@app.post("/ofertas/", response_model=schemas.Oferta)
def create_oferta(oferta: schemas.OfertaCreate, db: Session = Depends(get_db)):
    return crud.create_oferta(db=db, oferta=oferta)

@app.get("/ofertas/", response_model=list[schemas.Oferta])
def read_ofertas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_ofertas(db, skip=skip, limit=limit)
