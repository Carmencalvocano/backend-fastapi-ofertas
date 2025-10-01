from sqlalchemy.orm import Session
import models, schemas

# ---- Empresas ----
def get_empresas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Empresa).offset(skip).limit(limit).all()

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nombre=empresa.nombre)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

# ---- Ofertas ----
def get_ofertas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Oferta).offset(skip).limit(limit).all()

def create_oferta(db: Session, oferta: schemas.OfertaCreate):
    db_oferta = models.Oferta(**oferta.dict())
    db.add(db_oferta)
    db.commit()
    db.refresh(db_oferta)
    return db_oferta
