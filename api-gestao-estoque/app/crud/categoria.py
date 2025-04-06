from sqlalchemy.orm import Session
from app.models import models
from app.schemas import categoria as schema

def criar_categoria(db: Session, categoria: schema.CategoriaCreate):
    nova_categoria = models.Categoria(**categoria.dict())
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria

def listar_categorias(db: Session):
    return db.query(models.Categoria).all()

def buscar_categoria_por_id(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def deletar_categoria(db: Session, categoria_id: int):
    categoria = buscar_categoria_por_id(db, categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()
        return True
    return False
