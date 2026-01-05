import config
from openai import OpenAI

# Initialisation du client une seule fois au lancement
try:
    client = OpenAI(
        base_url=config.BASE_URL,
        api_key=config.API_KEY
    )
    print(f"✅ Service Traduction connecté sur : {config.PROVIDER}")
except Exception as e:
    print(f"❌ Erreur de connexion client : {e}")


def translate_text(text, source_lang="Français", target_lang="Anglais"):
    """
    Envoie le texte à l'IA pour traduction.
    Retourne la traduction (str) ou un message d'erreur.
    """
    if not text or len(text.strip()) < 2:
        return ""

    # mettre en anglais universelle pour la plupart des modèles
    system_prompt = (
        f"You are a professional interpreter. "
        f"Translate the following text from {source_lang} to {target_lang}. "
        f"Output ONLY the translation. No quotes, no explanations, no notes."
    )

    try:
        response = client.chat.completions.create(
            model=config.MODEL_NAME,

            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.3,
        )

        traduction = response.choices[0].message.content.strip()

        if traduction.startswith('"') and traduction.endswith('"'):
            traduction = traduction[1:-1]

        return traduction

    except Exception as e:
        print(f"❌ Erreur Traduction : {e}")
        return "[Erreur de service]"


if __name__ == "__main__":
    print("--- TEST MODULE TRADUCTION ---")
    phrase = "Bonjour, ceci est un test pour vérifier que tout fonctionne."
    print(f"📥 Entrée : {phrase}")

    resultat = translate_text(phrase, "Français", "Anglais")
    print(f"📤 Sortie : {resultat}")