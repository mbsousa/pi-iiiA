# app/models.py
from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class Categoria(Base):
    __tablename__ = 'categoria'

    id_cat = Column(Integer, primary_key=True, index=True)
    nome = Column(String(20), nullable=False)
    descricao = Column(Text(), nullable=False)

    produtos = relationship("Produto", back_populates="categoria")

class Produto(Base):
    __tablename__ = 'produto'

    id_prod = Column(Integer, primary_key=True, index=True)
    nome = Column(String(30), nullable=False)
    qtd_est = Column(Integer, nullable=False)
    preco = Column(Float, nullable=False)
    dt_ent = Column(Date, nullable=False)
    id_cat = Column(Integer, ForeignKey('categoria.id_cat', ondelete="CASCADE"), nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")
    movimentos = relationship("MovEstoque", back_populates="produto")

class TipoMovEnum(str, enum.Enum):
    entrada = 'entrada'
    saida = 'saida'

class MovEstoque(Base):
    __tablename__ = 'mov_estoque'

    id_est = Column(Integer, primary_key=True, index=True)
    dt = Column(Date, nullable=False)
    qtd = Column(Integer, nullable=False)
    hr = Column(Time, nullable=False)
    tipo_mov = Column(Enum(TipoMovEnum), nullable=False)
    id_prod = Column(Integer, ForeignKey('produto.id_prod', ondelete="CASCADE"), nullable=False)
    obs = Column(String(100))

    produto = relationship("Produto", back_populates="movimentos")
