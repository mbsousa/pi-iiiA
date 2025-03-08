from sqlalchemy import Column, Integer, String, Float, Date, Time, Enum, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id_cat = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20), nullable=False)

    produtos = relationship("Produto", back_populates="categoria", cascade="all, delete")

class Produto(Base):
    __tablename__ = "produto"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    nome = Column(String(30), nullable=False)
    descricao = Column(String(100), nullable=True) 
    quantidade = Column(Integer, nullable=False)  
    preco = Column(Float, nullable=False)
    dt_entrada = Column(Date, nullable=False)
    id_cat = Column(Integer, ForeignKey("categoria.id_cat", ondelete="CASCADE"), nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")
    movimentacoes = relationship("MovEstoque", back_populates="produto", cascade="all, delete")

class MovEstoque(Base):
    __tablename__ = "mov_estoque"

    id_est = Column(Integer, primary_key=True, autoincrement=True)
    dt = Column(Date, nullable=False)
    qtd = Column(Integer, nullable=False)
    hr = Column(Time, nullable=False)
    tipo_mov = Column(Enum("E", "S"), nullable=False)  
    id_prod = Column(Integer, ForeignKey("produto.id", ondelete="CASCADE"), nullable=False)
    obs = Column(String(100), nullable=True)

    produto = relationship("Produto", back_populates="movimentacoes")
