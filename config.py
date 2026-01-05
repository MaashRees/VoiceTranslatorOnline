import os
import sys
from dotenv import load_dotenv


# 1. Déterminez la racine du projet (par exemple, le dossier parent du dossier courant)
project_root = os.path.abspath(os.path.dirname(__file__))

# 2. Chemin vers le fichier .env à la racine
env_path = os.path.join(project_root, ".env")

if os.path.exists(env_path):
    load_dotenv(env_path)
elif os.path.exists(os.path.join(project_root, ".env_public")):
    print("⚠️  ATTENTION : Fichier de configuration '.env' introuvable.")
    print("👉 Veuillez copier '.env_public' en '.env' et ajouter vos clés.")
    print("   Commande : cp .env_public .env (ou renommez-le manuellement)")
    sys.exit(1)
else:
    print("❌ ERREUR CRITIQUE : Aucun fichier de configuration (.env ou .env_public) trouvé.")
    sys.exit(1)

PROVIDER = os.getenv("AI_PROVIDER", "WEBUI").upper()

if PROVIDER == "OPENROUTER":
    print("🌍 Mode: OPENROUTER activé")
    BASE_URL = os.getenv("OPENROUTER_BASE_URL")
    API_KEY = os.getenv("OPENROUTER_API_KEY")
    MODEL_NAME = os.getenv("OPENROUTER_MODEL_NAME")
else:
    # Par défaut : WEBUI
    print("🏠 Mode: WEBUI LOCAL (VPS) activé")
    BASE_URL = os.getenv("WEBUI_BASE_URL")
    API_KEY = os.getenv("WEBUI_API_KEY", "sk-dummy") # Clé par défaut si vide
    MODEL_NAME = os.getenv("WEBUI_MODEL_NAME", "default-model")

# 3. Paramètres Whisper
WHISPER_SIZE = os.getenv("WHISPER_MODEL_SIZE", "small")
WHISPER_TYPE = os.getenv("COMPUTE_TYPE", "float16")

# Petit check de sécurité
if not API_KEY or not BASE_URL:
    raise ValueError(f"❌ Erreur de config : API_KEY ou BASE_URL manquant pour le mode {PROVIDER}")

def get_prompt_whisper():
    """
    Lit le fichier vocab.txt et génère un prompt pour Whisper.
    """
    fichier_vocab = os.path.join(project_root, os.getenv("VOCAB_FILE"))
    mots_cles = []

    # Vérifie si le fichier existe
    if os.path.exists(fichier_vocab):
        try:
            with open(fichier_vocab, "r", encoding="utf-8") as f:
                lignes = f.readlines()

            for ligne in lignes:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"):
                    continue
                if "," in ligne:
                    mots = [m.strip() for m in ligne.split(",")]
                    mots_cles.extend(mots)
                else:
                    mots_cles.append(ligne)

        except Exception as e:
            print(f"⚠️ Erreur lecture vocab.txt : {e}")

    if not mots_cles:
        return "Conversation technique."

    prompt_final = f"Vocabulaire et contexte : {', '.join(mots_cles)}."

    # les prompts de whisper sont limités (je pense 224 tokens)
    return prompt_final[:1000]