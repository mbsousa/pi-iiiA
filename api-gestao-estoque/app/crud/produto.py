from sqlalchemy.orm import Session
from app.models.models import Produto
from app.schemas.produto import ProdutoCreate

def criar_produto(db: Session, produto: ProdutoCreate):
    novo_produto = Produto(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()

def buscar_produto_por_id(db: Session, id_prod: int):
    return db.query(Produto).filter(Produto.id_prod == id_prod).first()

def deletar_produto(db: Session, id_prod: int):
    produto = buscar_produto_por_id(db, id_prod)
    if produto:
        db.delete(produto)
        db.commit()
        return True
    return False
