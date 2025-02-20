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
    allow_origins=[
        "http://127.0.0.1:5173",  # Local React
        "http://localhost:5173",  # Local React
        "https://ai-business-optimizer.netlify.app",  # Front déployé
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
