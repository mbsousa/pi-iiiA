from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import produto as crud_produto, categoria as crud_categoria
from app.schemas.produto import ProdutoCreate, ProdutoOut

router = APIRouter(prefix="/produtos", tags=["Produtos"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def listar_produtos(request: Request, db: Session = Depends(get_db)):
    produtos = crud_produto.listar_produtos(db)
    return templates.TemplateResponse("produto/listar.html", {"request": request, "produtos": produtos})


@router.get("/criar")
def form_criar_produto(request: Request, db: Session = Depends(get_db)):
    categorias = crud_categoria.listar_categorias(db)
    return templates.TemplateResponse("produto/criar.html", {"request": request, "categorias": categorias})

@router.post("/criar")
def criar_produto(
    request: Request,
    nome: str = Form(...),
    qtd_est: int = Form(...),
    preco: float = Form(...),
    dt_ent: str = Form(...),
    id_cat: int = Form(...),
    db: Session = Depends(get_db),
):
    novo_produto = ProdutoCreate(
        nome=nome,
        qtd_est=qtd_est,
        preco=preco,
        dt_ent=dt_ent,
        id_cat=id_cat
    )
    crud_produto.criar_produto(db, novo_produto)
    return RedirectResponse(url="/produtos", status_code=303)
