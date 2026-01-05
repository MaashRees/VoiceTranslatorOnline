import sys
import torch
import sounddevice as sd

print("--- DIAGNOSTIC DU SYSTÈME ---")

# 1. Vérification Python
print(f"✅ Python version : {sys.version.split()[0]}")

# 2. Vérification GPU (CUDA)
try:
    if torch.cuda.is_available():
        print(f"✅ GPU détecté : {torch.cuda.get_device_name(0)}")
        print("🚀 Tout est prêt pour une performance maximale !")
    else:
        print("⚠️  ATTENTION : Pas de GPU détecté. Whisper tournera sur le CPU (plus lent).")
except ImportError:
    print("❌ Erreur : PyTorch n'est pas installé correctement.")

# 3. Vérification des bibliothèques clés
try:
    import faster_whisper

    print("✅ Faster-Whisper installé.")
except ImportError:
    print("❌ Faster-Whisper MANQUANT.")

try:
    import edge_tts

    print("✅ Edge-TTS installé.")
except ImportError:
    print("❌ Edge-TTS MANQUANT.")

try:
    import gradio

    print("✅ Gradio installé.")
except ImportError:
    print("❌ Gradio MANQUANT.")

# 4. Vérification Audio
print("\n--- PÉRIPHÉRIQUES AUDIO ---")
try:
    devices = sd.query_devices()
    # On affiche juste les noms pour ne pas spammer
    input_devs = [d['name'] for d in devices if d['max_input_channels'] > 0]
    output_devs = [d['name'] for d in devices if d['max_output_channels'] > 0]

    print(f"🎤 Micros trouvés ({len(input_devs)}) : {', '.join(input_devs[:3])}...")
    print(f"🔊 Sorties trouvées ({len(output_devs)}) : {', '.join(output_devs[:3])}...")

    if len(input_devs) > 0:
        print("✅ Système audio OK.")
    else:
        print("⚠️  Aucun micro détecté !")

except Exception as e:
    print(f"❌ Erreur Audio : {e}")

print("\n---------------------------")