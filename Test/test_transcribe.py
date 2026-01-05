import os
import sounddevice as sd
from scipy.io.wavfile import write
from datetime import datetime
import transcribe  # On importe notre moteur configuré


# --- FONCTION D'ENREGISTREMENT ---
def enregistrer_audio_live(dossier="enregistrements", duree=5):
    # 1. Préparation du dossier et du nom
    if not os.path.exists(dossier):
        os.makedirs(dossier)

    maintenant = datetime.now()
    # Format demandé : [test]_2024-01-05_16-30.wav
    nom_fichier = f"[test]_{maintenant.strftime('%Y-%m-%d')}_{maintenant.strftime('%H-%M-%S')}.wav"
    chemin_complet = os.path.join(dossier, nom_fichier)

    # 2. Capture Audio
    print(f"\n🎤 ENREGISTREMENT ({duree}s) dans : {nom_fichier}")
    print("🔴 PARLEZ MAINTENANT (Français)...")

    fs = 44100  # Fréquence standard
    # Capture en int16 (léger et compatible)
    audio_data = sd.rec(int(duree * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Attente de la fin

    print("⏹️ Terminé.")

    # 3. Sauvegarde
    write(chemin_complet, fs, audio_data)
    return chemin_complet


# --- MENU PRINCIPAL ---
if __name__ == "__main__":
    print("\n--- TESTEUR WHISPER (FRANÇAIS) ---")
    print("1. 🎤 Enregistrer ma voix maintenant")
    print("2. 📁 Tester un fichier existant (.wav)")

    choix = input("\nVotre choix (1 ou 2) : ").strip()

    fichier_cible = ""

    if choix == "1":
        try:
            duree = input("Durée en secondes (défaut 5) : ")
            duree = int(duree) if duree.isdigit() else 5
            fichier_cible = enregistrer_audio_live(duree=duree)
        except Exception as e:
            print(f"Erreur micro : {e}")

    elif choix == "2":
        fichier_cible = input("Chemin du fichier (ex: test.wav) : ").strip().strip('"')
        # fichier_cible = r"data\online\Comptearebours.wav"

    # Lancement de la transcription via notre service
    if fichier_cible:
        print(f"\n🧠 Analyse par Whisper en cours...")
        resultat = transcribe.transcrire_audio(fichier_cible)

        print("\n" + "=" * 40)
        print("📝 RÉSULTAT :")
        print(resultat)
        print("=" * 40 + "\n")