from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv
import json

# Charger les variables d'environnement
if not os.getenv("OPENAI_API_KEY"):
    load_dotenv()  # Charge uniquement si la clé n'est pas déjà en variable d'env


# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#if not OPENAI_API_KEY:
#    raise ValueError("⚠️ OPENAI_API_KEY est manquante. Vérifie les variables d’environnement !")


# Config OpenAI
#openai.api_key = OPENAI_API_KEY
router = APIRouter()

# Modèle de requête pour l'Audit IA
class AuditRequest(BaseModel):
    business_name: str
    description: str
    challenges: str

@router.post("/audit", summary="Audit IA Express pour un business")
async def generate_audit(request: AuditRequest):
    try:
        print("🔍 Données reçues:", request.dict())  # DEBUG

        business_name = request.business_name.strip()
        description = request.description.strip()
        challenges = request.challenges.strip()

        # Vérification des entrées pour éviter des audits vides
        if len(business_name) < 5 or len(description) < 5 or len(challenges) < 5:
            raise HTTPException(status_code=400, detail="⚠️ Les champs doivent contenir au moins 5 caractères pour un audit pertinent.")

        # Construction du prompt avec des consignes strictes
        prompt = f"""
        Analyse et optimise ce business en te basant sur ses forces, faiblesses et opportunités.

        **Business:** {business_name}
        **Description:** {description}
        **Défis:** {challenges}

        Fournis un rapport structuré et exploitable sous ce format JSON:
        {{
            "forces": ["..."],
            "faiblesses": ["..."],
            "opportunites": ["..."],
            "conseils_ia": ["..."],
            "score_evaluation": 50,  
            "recommandation_finale": "..."
        }}

        - Assure-toi que le **score** est toujours compris entre **30 et 100**.
        - N'invente pas de données, reste factuel.
        """

        # 🔥 Appel OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un consultant IA expert en business et analyses SWOT."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=450,  # 🔥 Optimisation des tokens pour vitesse et coût
            temperature=0.6  # 🔥 Réduction pour plus de fiabilité
        )

        ai_response = response["choices"][0]["message"]["content"]
        print("🔍 Résultat brut avant parsing:", ai_response)

        # Vérification si OpenAI a bien renvoyé un JSON valide
        try:
            audit_report = json.loads(ai_response)
            if "score_evaluation" in audit_report and audit_report["score_evaluation"] < 30:
                audit_report["score_evaluation"] = 30  # 🔥 Correction du score trop bas
            return audit_report
        except json.JSONDecodeError:
            print("🔥 ERREUR : OpenAI a renvoyé un format incorrect.")
            return {"error": "Format de réponse invalide de l'IA."}

    except Exception as e:
        print("🔥 ERREUR :", str(e))  # 🔥 LOG erreur
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'analyse : {str(e)}")
