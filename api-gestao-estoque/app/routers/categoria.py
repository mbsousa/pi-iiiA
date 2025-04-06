from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import categoria as crud_categoria
from app.schemas.categoria import CategoriaCreate, CategoriaOut
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND


templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/categorias", tags=["Categorias"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/criar")
def exibir_formulario_criar(request: Request):
    return templates.TemplateResponse("categoria/criar.html", {"request": request})


@router.post("/criar")
def criar_categoria_via_form(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    db: Session = Depends(get_db)
):
    nova = CategoriaCreate(nome=nome, descricao=descricao)
    crud_categoria.criar_categoria(db, nova)
    return RedirectResponse(url="/categorias", status_code=HTTP_302_FOUND)

@router.get("/")
def listar_categorias(request: Request, db: Session = Depends(get_db)):
    categorias = crud_categoria.listar_categorias(db)
    return templates.TemplateResponse("categoria/listar.html", {"request": request, "categorias": categorias})

@router.get("/{categoria_id}", response_model=CategoriaOut)
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud_categoria.buscar_categoria_por_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.post("/", response_model=CategoriaOut)
def criar_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    return crud_categoria.criar_categoria(db, categoria)

@router.post("/{categoria_id}/deletar")
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud_categoria.buscar_categoria_por_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    crud_categoria.deletar_categoria(db, categoria_id)
    return RedirectResponse(url="/categorias", status_code=303)