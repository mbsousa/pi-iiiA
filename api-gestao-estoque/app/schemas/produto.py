from pydantic import BaseModel
from datetime import date

class ProdutoBase(BaseModel):
    nome: str
    qtd_est: int
    preco: float
    dt_ent: date
    id_cat: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoOut(ProdutoBase):
    id_prod: int

    class Config:
        orm_mode = True
