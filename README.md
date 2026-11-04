# 🎙️ VoiceTranslatorOnline — Traducteur vocal par IA (S2ST)

Chaîne de **traduction vocale** : parler dans une langue, obtenir une traduction synthétisée dans une autre. L'objectif est de l'utiliser en réunion vidéo (Zoom, Teams, Meet) via un câble audio virtuel.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Whisper](https://img.shields.io/badge/ASR-Faster--Whisper-orange) ![TTS](https://img.shields.io/badge/TTS-Edge--TTS-green)

## Pipeline

```
Voix (WAV) ──► Transcription ──► Traduction ──► Synthèse vocale ──► MP3
              Faster-Whisper     LLM compatible    Edge-TTS
              (local, CPU)       API OpenAI
```

| Module | Rôle |
| :-- | :-- |
| `transcribe.py` | Transcription locale avec Faster-Whisper (français, CPU en int8), avec un vocabulaire métier optionnel pour améliorer la reconnaissance |
| `translate.py` | Traduction par un LLM via une API compatible OpenAI, avec un prompt d'interprète qui ne renvoie que la traduction |
| `tts.py` | Synthèse vocale Edge-TTS, voix françaises, anglaises et espagnoles (homme / femme) |
| `config.py` | Chargement de la configuration depuis `.env` et choix du fournisseur de traduction |
| `check_setup.py` | Diagnostic de l'installation : version de Python, GPU, bibliothèques, micros et sorties audio |
| `Test/` | Tests de la transcription et des connexions aux modèles |

## Fournisseurs de traduction

Le fournisseur se choisit avec `AI_PROVIDER` dans le fichier `.env` :

- **`WEBUI`** (par défaut) : votre propre serveur local ou VPS de type [Text-Generation-WebUI](https://github.com/oobabooga/text-generation-webui) lancé avec `--api`. Les données ne quittent pas votre réseau pour la traduction.
- **`OPENROUTER`** : accès cloud à de nombreux modèles (Llama, Mistral, Gemini...) avec une clé API.

## Installation

```bash
git clone https://github.com/MaashRees/VoiceTranslatorOnline.git
cd VoiceTranslatorOnline

python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt

cp .env_public .env             # puis renseigner l'URL du serveur et/ou la clé OpenRouter
python check_setup.py           # vérifie Python, GPU, bibliothèques et audio
```

> Le fichier `requirements.txt` est encodé en UTF-16. Si `pip` refuse de le lire, convertissez-le d'abord en UTF-8.

Variables principales : `AI_PROVIDER`, `WEBUI_BASE_URL`, `OPENROUTER_API_KEY`, `OPENROUTER_MODEL_NAME`, `WHISPER_MODEL_SIZE` (`tiny` à `large-v2`), `VOCAB_FILE` (liste de mots-clés pour guider Whisper).

## Utilisation

Chaque module peut être testé seul :

```bash
python translate.py   # traduit une phrase d'exemple
python tts.py         # génère un MP3 de démonstration
```

En code, les trois fonctions s'enchaînent :

```python
from transcribe import transcrire_audio
from translate import translate_text
from tts import synthetiser_audio

texte = transcrire_audio("mon_audio.wav")
traduction = translate_text(texte, "Français", "Anglais")
fichier = synthetiser_audio(traduction, "Anglais", "Homme")
```

## État d'avancement et suite

- ✅ Transcription, traduction et synthèse vocale fonctionnent module par module.
- 🚧 À venir : boucle temps réel avec capture du micro, interface Gradio et injection de l'audio dans un câble audio virtuel (type VB-Cable).
- ℹ️ La transcription tourne aujourd'hui sur CPU en int8 et force le français en entrée ; le passage sur GPU et le choix de la langue source sont prévus.

## Licence

Voir [LICENSE](LICENSE).
