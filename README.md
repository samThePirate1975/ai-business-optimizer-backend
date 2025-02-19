🚀 AI Business Optimizer - Backend

Bienvenue dans le backend de AI Business Optimizer, une API construite avec FastAPI pour générer des audits intelligents sur les entreprises.

📌 Technologies utilisées
🐍 Python 3.12
⚡ FastAPI - Framework rapide pour l'API
🤖 OpenAI API - Pour l'analyse des données
🌱 Uvicorn - Serveur ASGI performant
🗄 Dotenv - Gestion des variables d'environnement
🧪 Pytest - Tests unitaires

🚀 Installation & Lancement

1️⃣ Cloner le projet
git clone https://github.com/ton-profil/ton-repo.git
cd ton-repo/backend

2️⃣ Installer les dépendances
Assurez-vous d’avoir Python 3.10+ installé.
Créez un environnement virtuel et installez les packages :

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3️⃣ Configurer les variables d’environnement
Créez un fichier .env (ou copiez .env.example) et ajoutez vos clés :

cp .env.example .env
nano .env  # Modifier avec vos vraies clés

4️⃣ Lancer le serveur
uvicorn main:app --reload
L’API sera accessible sur http://127.0.0.1:8000/docs pour tester les endpoints.

📜 API Endpoints
Méthode	Endpoint	Description
POST	/api/audit	Analyse un business avec l’IA
Exemple de requête :

{
  "business_name": "Startup AI",
  "description": "Plateforme SaaS qui automatise l'analyse des données commerciales.",
  "challenges": "Trouver de nouveaux clients, optimiser l'onboarding utilisateur."
}

🤝 Contribuer
Clone, fork, propose une PR ! 💡 Toute aide est la bienvenue.
