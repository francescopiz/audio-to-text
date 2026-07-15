#!/usr/bin/env python3
"""
Simple script to convert all audio files in the 'input' directory to text
using OpenAI's Whisper model, saving the transcriptions to the 'output' directory.
Configuration is loaded from 'config.json'.
"""

import json
import sys
from pathlib import Path

import whisper

# Supported audio extensions
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.flac', '.ogg', '.webm', '.aac', '.opus', '.wma'}


def load_config():
    """Load configuration from config.json, falling back to defaults if not found."""
    default_config = {
        "model": "base",
        "language": "it",
        "overwrite": False
    }

    config_path = Path("config.json")
    if not config_path.exists():
        print("⚠️  config.json non trovato, uso della configurazione di default.")
        return default_config

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            # Merge with defaults to ensure all keys exist
            return {**default_config, **config}
    except Exception as e:
        print(f"❌ Errore nel caricamento di config.json: {e}. Uso i default.")
        return default_config


def main():
    # 1. Load config
    config = load_config()
    model_size = config.get("model", "base")
    language = config.get("language", "null")
    overwrite = config.get("overwrite", False)

    # 2. Check input and output directories
    input_dir = Path("input")
    output_dir = Path("output")

    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    # 3. Find audio files in input directory
    audio_files = [
        p for p in input_dir.iterdir()
        if p.is_file() and p.suffix.lower() in AUDIO_EXTENSIONS
    ]

    if not audio_files:
        print("ℹ️  Nessun file audio trovato nella cartella 'input/'.")
        print(f"Supportati: {', '.join(sorted(AUDIO_EXTENSIONS))}")
        print("Inserisci i tuoi file audio nella cartella 'input' e riavvia lo script.")
        return

    print(f"📂 Trovati {len(audio_files)} file audio da elaborare.")

    # Filter files to process depending on overwrite setting
    files_to_process = []
    for audio_file in audio_files:
        output_file = output_dir / f"{audio_file.stem}.txt"
        if output_file.exists() and not overwrite:
            print(f"⏭️  Salto '{audio_file.name}' (già trascritto in '{output_file.name}')")
        else:
            files_to_process.append((audio_file, output_file))

    if not files_to_process:
        print("✅ Tutti i file sono già stati trascritti. Niente da fare.")
        return

    # 4. Load Whisper model
    print(f"🤖 Caricamento del modello Whisper '{model_size}'...")
    try:
        model = whisper.load_model(model_size)
    except Exception as e:
        print(f"❌ Errore durante il caricamento del modello Whisper: {e}")
        sys.exit(1)

    # 5. Process files
    for idx, (audio_file, output_file) in enumerate(files_to_process, 1):
        print(f"\n[{idx}/{len(files_to_process)}] Elaborazione di: {audio_file.name}")

        try:
            # Prepare transcribe arguments
            transcribe_args = {}
            if language:
                transcribe_args["language"] = language

            print(f"⏳ Trascrizione in corso (lingua: {language or 'rilevamento automatico'})...")
            result = model.transcribe(str(audio_file), **transcribe_args)

            transcribed_text = result.get("text", "").strip()

            # Save transcription
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(transcribed_text)

            print(f"💾 Trascrizione salvata con successo in: {output_file}")

        except KeyboardInterrupt:
            print("\n⚠️  Operazione interrotta dall'utente. Uscità...")
            break
        except Exception as e:
            print(f"❌ Errore durante la trascrizione di {audio_file.name}: {e}")

    print("\n🎉 Elaborazione terminata!")


if __name__ == "__main__":
    main()
