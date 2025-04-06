# routers/mov_estoque.py

from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import mov_estoque as crud_mov, produto as crud_prod
from app.schemas.mov_estoque import MovEstoqueCreate
from datetime import datetime, date, time
from app.models.models import TipoMovEnum

router = APIRouter(prefix="/movimentacoes", tags=["Movimentações"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/criar")
def form_criar_movimentacao(request: Request, db: Session = Depends(get_db)):
    produtos = crud_prod.listar_produtos(db)
    return templates.TemplateResponse("mov_estoque/criar.html", {"request": request, "produtos": produtos})

@router.get("/")
def listar_movimentacoes(request: Request, db: Session = Depends(get_db)):
    movimentacoes = crud_mov.listar_movimentacoes(db)
    return templates.TemplateResponse("mov_estoque/listar.html", {"request": request, "movimentacoes": movimentacoes})


@router.post("/criar")
def criar_movimentacao(
    request: Request,
    dt: str = Form(...),
    qtd: int = Form(...),
    hr: str = Form(...),
    tipo_mov: str = Form(...),
    id_prod: int = Form(...),
    obs: str = Form(""),
    db: Session = Depends(get_db),
):
    data_convertida = datetime.strptime(dt, "%Y-%m-%d").date()
    hora_convertida = datetime.strptime(hr, "%H:%M").time()
    tipo_enum = TipoMovEnum(tipo_mov)  # <-- aqui sim

    nova_mov = MovEstoqueCreate(
        dt=data_convertida,
        qtd=qtd,
        hr=hora_convertida,
        tipo_mov=tipo_enum,
        id_prod=id_prod,
        obs=obs
    )

    crud_mov.criar_movimentacao(db, nova_mov)
    return RedirectResponse(url="/movimentacoes", status_code=303)