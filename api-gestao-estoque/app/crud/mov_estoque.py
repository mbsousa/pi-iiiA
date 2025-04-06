from sqlalchemy.orm import Session, joinedload
from app.models.models import MovEstoque
from app.schemas.mov_estoque import MovEstoqueCreate

def criar_movimentacao(db: Session, movimentacao: MovEstoqueCreate):
    nova_mov = MovEstoque(**movimentacao.dict())
    db.add(nova_mov)
    db.commit()
    db.refresh(nova_mov)
    return nova_mov

def listar_movimentacoes(db: Session):
    return db.query(MovEstoque).options(joinedload(MovEstoque.produto)).all()


def buscar_movimentacao_por_id(db: Session, id_est: int):
    return db.query(MovEstoque).filter(MovEstoque.id_est == id_est).first()

def deletar_movimentacao(db: Session, id_est: int):
    mov = buscar_movimentacao_por_id(db, id_est)
    if mov:
        db.delete(mov)
        db.commit()
        return True
    return False