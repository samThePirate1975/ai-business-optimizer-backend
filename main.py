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
        "http://127.0.0.1:8000",  # Local React
        "http://localhost:8000",  # Local React
        "https://ai-business-optimizer.netlify.app",  # Front déployé
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
openai_key = os.getenv("OPENAI_API_KEY")
print(f"🔍 OpenAI Key détectée ? {'Oui' if openai_key else 'Non'}")
if not openai_key:
    raise ValueError("⚠️ La clé API OpenAI est toujours manquante dans Railway ! Vérifie la config.")





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
