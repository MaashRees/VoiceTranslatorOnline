import asyncio
import edge_tts
import os

# --- CATALOGUE DES VOIX ---
VOIX_DISPONIBLES = {
    "fr-Femme": "fr-FR-VivienneMultilingualNeural",  # Voix très naturelle
    "fr-Homme": "fr-FR-RemyMultilingualNeural",  # Voix calme et posée
    "en-Femme": "en-US-AnaNeural",  # Voix enfantine/jeune
    "en-Homme": "en-US-GuyNeural",  # Voix standard professionnelle
    "en-Deep": "en-US-ChristopherNeural",  # Voix plus grave
    "es-Femme": "es-ES-ElviraNeural",
    "es-Homme": "es-ES-AlvaroNeural"
}

project_root = os.path.abspath(os.path.dirname(__file__))
dir_tts = os.path.join(project_root, "voices")

# Fonction principale (important : Asynchrone)
async def _generer_audio_async(texte, voix, chemin_sortie):
    try:
        communicate = edge_tts.Communicate(texte, voix)
        await communicate.save(chemin_sortie)
        return True
    except Exception as e:
        print(f"❌ Erreur Edge-TTS : {e}")
        return False


# Fonction "Wrapper" (à appeler depuis l'app)
def synthetiser_audio(texte, langue_cible="Anglais", genre="Homme", fichier_sortie="output_tts.mp3"):
    """
    Transforme le texte en fichier audio MP3.
    langue_cible: "Anglais", "Français", "Espagnol"
    genre: "Homme" ou "Femme"
    """
    if not texte:
        return None

    code_langue = "en"
    if "fr" in langue_cible.lower(): code_langue = "fr"
    if "es" in langue_cible.lower() or "sp" in langue_cible.lower(): code_langue = "es"
    cle_voix = f"{code_langue}-{genre}"

    # Si la clé n'existe pas, on prend une voix par défaut
    voix_choisie = VOIX_DISPONIBLES.get(cle_voix, "fr-FR-RemyMultilingualNeural")

    print(f"🗣️ Génération audio ({voix_choisie})...")
    # 2. Exécution de la tâche asynchrone
    try:
        dir_cible = os.path.join(dir_tts, cle_voix)
        os.makedirs(dir_cible, exist_ok=True)
        chemin_complet_sortie = os.path.join(dir_cible, fichier_sortie)
        asyncio.run(_generer_audio_async(texte, voix_choisie, chemin_complet_sortie))

        if os.path.exists(chemin_complet_sortie):
            return chemin_complet_sortie
        else:
            return None
    except Exception as e:
        print(f"❌ Erreur Wrapper TTS : {e}")
        return None


if __name__ == "__main__":
    print("--- TEST TTS ---")
    texte_test = "Hello! I am your AI translator. This voice is generated locally."

    fichier = synthetiser_audio(texte_test, "Anglais", "Homme")

    if fichier:
        print(f"✅ Fichier généré : {fichier}")
        # Sur Windows, ça joue le fichier
        os.system(f"start {fichier}")