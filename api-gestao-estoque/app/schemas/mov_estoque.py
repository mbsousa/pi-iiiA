from pydantic import BaseModel
from datetime import date, time
from typing import Optional
from app.models.models import TipoMovEnum

class MovEstoqueBase(BaseModel):
    dt: date
    qtd: int
    hr: time
    tipo_mov: TipoMovEnum
    id_prod: int
    obs: Optional[str] = None


class MovEstoqueCreate(MovEstoqueBase):
    pass

class MovEstoqueOut(MovEstoqueBase):
    id_est: int

    class Config:
        orm_mode = True
