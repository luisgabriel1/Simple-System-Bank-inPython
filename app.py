from fastapi import FastAPI
from routes.routesTransferencia import router as transferencia_router
from routes.routesErro import router as erros_router

# Cria a aplicação FastAPI
app = FastAPI(
    title="API Viabilizze",
    description="API para transferências e gestão de erros 🚀",
    version="1.0.0"
)

# Inclui os módulos de rotas
app.include_router(transferencia_router, prefix="/transferencias", tags=["Transferências"])
app.include_router(erros_router, prefix="/erros", tags=["Erros"])

# Rota principal
@app.get("/")
def home():
    return {"message": "Bem-vindo à API da Viabilizze 🚀"}
