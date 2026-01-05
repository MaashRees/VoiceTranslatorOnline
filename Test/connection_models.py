import sys
from openai import OpenAI
import config

print(f"--- TEST DE CONNEXION : {config.PROVIDER} ---")
print(f"📍 URL : {config.BASE_URL}")
print(f"🧠 Modèle : {config.MODEL_NAME}")

try:
    # 1. Initialisation du client
    client = OpenAI(
        base_url=config.BASE_URL,
        api_key=config.API_KEY
    )

    messages = [
        {"role": "system", "content": "Tu es un traducteur expert. Traduis le texte suivant en Français. Réponds seulement avec la traduction."},
        {"role": "user", "content": "Hello world, I am ready to code."}
    ]

    print("\n⏳ Envoi de la requête en cours...")

    response = client.chat.completions.create(
        model=config.MODEL_NAME,
        messages=messages,
        temperature=0.3, # toujours choisir une température pour l'instant à 0.3 pour la précision des réponses
    )

    resultat = response.choices[0].message.content
    print("\n✅ RÉPONSE REÇUE :")
    print("------------------------------------------------")
    print(resultat)
    print("------------------------------------------------")

except Exception as e:
    print("\n❌ ÉCHEC DU TEST")
    print(f"Erreur : {e}")
    print("\n💡 Pistes de solution :")
    if config.PROVIDER == "WEBUI":
        print("- Vérifie que ton serveur WebUI est bien lancé.")
        print("- Vérifie que le flag '--api' est bien activé sur ton serveur.")
        print("- Vérifie l'URL dans ton .env (http vs https, port 5000 vs 8000).")
    else:
        print("- Vérifie tes crédits OpenRouter.")
        print("- Vérifie que ta clé API dans .env est correcte.")