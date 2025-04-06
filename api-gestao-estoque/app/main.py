from fastapi import FastAPI
from sqlalchemy import text
from app.database import SessionLocal
from app.routers import categoria, produto, mov_estoque

app = FastAPI()

@app.get("/")
def testar_conexao():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # Teste simples de conexão
        return {"status": "Conexão com o banco de dados bem-sucedida!"}
    except Exception as e:
        return {"erro": str(e)}
    finally:
        db.close()

app.include_router(categoria.router)
app.include_router(produto.router)
app.include_router(mov_estoque.router)
