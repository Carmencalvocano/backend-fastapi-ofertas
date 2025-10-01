from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
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
    ofertas = db.query(models.Oferta).options(joinedload(models.Oferta.empresa)).offset(skip).limit(limit).all()
    
    # Añadir nombre de la empresa a cada objeto
    for oferta in ofertas:
        oferta.empresa_nombre = oferta.empresa.nombre if oferta.empresa else None
    return ofertas

# ---- Estudiantes ----
@app.post("/estudiantes/", response_model=schemas.Estudiante)
def create_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return crud.create_estudiante(db=db, estudiante=estudiante)

@app.get("/estudiantes/", response_model=list[schemas.Estudiante])
def read_estudiantes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_estudiantes(db, skip=skip, limit=limit)

@app.get("/matching/{estudiante_id}")
def match_ofertas(estudiante_id: int, db: Session = Depends(get_db)):
    estudiante = db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    if not estudiante:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    estudiante_skills = set(estudiante.skills.lower().split(","))
    ofertas = db.query(models.Oferta).all()

    resultado = []
    for oferta in ofertas:
        score = 0
        for skill in estudiante_skills:
            if skill.strip() in oferta.descripcion.lower() or skill.strip() in oferta.titulo.lower():
                score += 1
        if score > 0:
            resultado.append({
                "oferta": oferta.titulo,
                "descripcion": oferta.descripcion,
                "empresa": oferta.empresa.nombre,
                "score": score
            })

    return sorted(resultado, key=lambda x: x["score"], reverse=True)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
