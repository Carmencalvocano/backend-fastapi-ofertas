from pydantic import BaseModel
from typing import List, Optional

class OfertaBase(BaseModel):
    titulo: str
    descripcion: Optional[str] = None

class OfertaCreate(OfertaBase):
    empresa_id: int

class Oferta(OfertaBase):
    id: int
    empresa_id: int

    class Config:
        orm_mode = True


class EmpresaBase(BaseModel):
    nombre: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int
    ofertas: List[Oferta] = []

    class Config:
        orm_mode = True
