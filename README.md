# 🎙️ VoiceTranslatorOnline | Local AI Voice Translator (S2ST)

**Un traducteur vocal temps réel pour réunions vidéo, propulsé par l'IA locale.**

Ce projet permet de parler dans une langue (ex: Français) et de faire entendre une traduction synthétique (ex: Anglais) directement dans vos applications de réunion (Zoom, Teams, Meet) via un câble audio virtuel.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Gradio](https://img.shields.io/badge/GUI-Gradio-orange) ![Local AI](https://img.shields.io/badge/AI-Local-green)

## ✨ Points Forts
- **100% Local & Privé :** Utilise `Faster-Whisper` et votre propre serveur LLM (Oobabooga/WebUI). Aucune donnée ne quitte votre réseau.
- **Intégration Universelle :** Fonctionne avec tout logiciel acceptant un microphone via VB-Cable.
- **Multi-Modèles :** Compatible avec Llama 3, Mistral, etc. via API locale.
- **Gratuit :** Utilise la bibliothèque `Edge-TTS` pour une synthèse vocale de haute qualité sans frais.

## 🛠️ Architecture
1.  **Input :** Capture micro (SoundDevice).
2.  **ASR :** Transcription rapide avec `Faster-Whisper`.
3.  **Translation :** Traduction contextuelle via API `Text-Generation-WebUI`.
<!--
4.  **TTS :** Synthèse vocale avec `Edge-TTS`.
5.  **Output :** Injection audio dans `Virtual Audio Cable`.
-->
## 🚀 Pré-requis
- Python 3.10+
- Carte graphique NVIDIA (Recommandé pour Whisper et LLM).
<!--
- [VB-CABLE Driver](https://vb-audio.com/Cable/) installé.
- Un serveur [Text-Generation-WebUI](https://github.com/oobabooga/text-generation-webui) qui tourne avec le flag `--api`.
-->
## 📦 Installation

```bash
# Cloner le repo
git clone [https://github.com/MaashRees/VoiceTranslatorOnline.git](https://github.com/MaashRees/VoiceTranslatorOnline.git)
cd VoiceTranslatorOnline

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt
# (Assurez-vous d'avoir torch et torchaudio compatibles avec votre CUDA)
