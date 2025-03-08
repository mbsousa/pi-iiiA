from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .models import Produto

router = APIRouter()

@router.post("/produtos/")
def adicionar_produto(nome: str, descricao: str, quantidade: int, db: Session = Depends(get_db)):
    produto = Produto(nome=nome, descricao=descricao, quantidade=quantidade)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto

@router.delete("/produtos/{produto_id}")
def remover_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
    return {"message": "Produto removido"}

@router.get("/produtos/")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()
