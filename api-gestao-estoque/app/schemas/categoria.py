from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str
    descricao: str 

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaOut(CategoriaBase):
    id_cat: int  

    class Config:
        orm_mode = True
