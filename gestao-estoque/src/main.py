from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .models import Base
from .routers import produtos


app = FastAPI()

# Middleware para permitir acesso ao frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="src/assets"), name="static")

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Incluir as rotas de produtos
app.include_router(produtos.router, prefix="")
