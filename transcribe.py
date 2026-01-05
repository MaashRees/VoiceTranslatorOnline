import os
import config
from faster_whisper import WhisperModel

print(f"⚙️  Initialisation de Whisper ({config.WHISPER_SIZE}) sur CPU...")

# 1. Chargement du modèle (Optimisé CPU/Int8)
try:
    model = WhisperModel(
        config.WHISPER_SIZE,
        device="cpu",
        compute_type="int8"  # Force le mode CPU compatible
    )
    print("✅ Moteur Whisper chargé et prêt (Mode Français 🇫🇷).")
except Exception as e:
    print(f"❌ Erreur critique Whisper : {e}")
    exit(1)


def transcrire_audio(chemin_fichier, vocab=False):
    """
    Prend un fichier WAV et retourne le texte en Français.
    """
    if not os.path.exists(chemin_fichier):
        return "❌ Erreur : Fichier introuvable."
    dico = None
    if vocab:  # avoir une liste de mots clés
        dico = config.get_prompt_whisper()
        print(f"On a le dictionnaire avec ces mots-clés : {dico}")
    try:
        segments, info = model.transcribe(
            chemin_fichier,
            language="fr", # on force le français ici
            beam_size=5, # precision
            temperature=0.3,
            initial_prompt=dico
        )
        # avoir le texte complet
        texte_complet = " ".join([segment.text for segment in segments])
        return texte_complet.strip()

    except Exception as e:
        return f"❌ Erreur lors de la transcription : {e}"