from fastapi import FastAPI
from routes import analyze, automate, optimize, decision, audit
import sys
import os
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(
    title="AI Business Optimizer 🚀",
    description="API pour optimiser et automatiser les processus business avec l'IA.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # On limite aux requêtes venant du frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes (POST, GET, etc.)
    allow_headers=["*"],  # Permet tous les headers nécessaires
)

# Inclusion des routers
app.include_router(analyze.router, prefix="/analyze-business", tags=["Analyse"])
app.include_router(automate.router, prefix="/automate-task", tags=["Automatisation"])
app.include_router(optimize.router, prefix="/optimize-content", tags=["Optimisation"])
app.include_router(decision.router, prefix="/decision-support", tags=["Prise de décision"])
# Inclusion du routeur Audit IA Express
app.include_router(audit.router, prefix="/api", tags=["Audit"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Bienvenue sur AI Business Optimizer 🚀"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)