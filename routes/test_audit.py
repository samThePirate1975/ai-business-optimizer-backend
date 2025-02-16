import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_audit():
    print("\n🛠️ **TEST : Envoi de la requête d'audit...**\n")

    data = {
        "business_name": "Agence de Marketing Digital",
        "description": "Agence spécialisée dans la publicité en ligne et le growth hacking.",
        "challenges": "Acquisition clients, ROI sur publicité, fidélisation"
    }

    try:
        response = requests.post(f"{BASE_URL}/api/audit", json=data)
        response_json = response.json()

        if response.status_code == 200:
            print("\n✅ **Succès :**\n")
            print("🔹 **JSON brut reçu :**")  # 🔎 Voir le JSON brut avant formatage
            print(response_json)  # Vérifions la structure exacte

            # 🔥 Affichage propre
            print("\n📌 **Résultat formaté :**")
            print(json.dumps(response_json, indent=4, ensure_ascii=False, sort_keys=False))
        else:
            print("\n❌ **Échec :**\n", json.dumps(response_json, indent=4, ensure_ascii=False, sort_keys=False))

    except Exception as e:
        print("\n❌ **Erreur lors de la requête :**", str(e))

if __name__ == "__main__":
    test_audit()
