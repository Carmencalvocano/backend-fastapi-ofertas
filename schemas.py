from pydantic import BaseModel
from typing import List, Optional

# ------------------- OFERTAS -------------------
class OfertaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None

class OfertaCreate(OfertaBase):
    empresa_id: int

class Oferta(OfertaBase):
    id: int
    empresa_id: int
    empresa_nombre: Optional[str] = None  # <-- NUEVO CAMPO

    class Config:
        orm_mode = True

# ------------------- EMPRESAS -------------------
class EmpresaBase(BaseModel):
    nombre: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    ofertas: List[Oferta] = []

    class Config:
        orm_mode = True

# ------------------- ESTUDIANTES -------------------
class EstudianteBase(BaseModel):
    nombre: str
    skills: str

class EstudianteCreate(EstudianteBase):
    pass

class Estudiante(EstudianteBase):
    id: int

    class Config:
        orm_mode = True
