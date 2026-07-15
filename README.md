# Audio to Text

Questo progetto converte file audio in testo utilizzando il modello Whisper di OpenAI. 
Scansiona automaticamente la cartella `input/` e salva le trascrizioni nella cartella `output/`.

## Installazione

Assicurati di avere Python 3 installato e installa le dipendenze:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> È necessario installare `ffmpeg` sul sistema affinché Whisper possa elaborare i file audio.
> - **Linux (Ubuntu/Debian):** `sudo apt install ffmpeg`
> - **macOS:** `brew install ffmpeg`
> - **Windows:** installare tramite scoop/winget o scaricare da ffmpeg.org.

## Utilizzo

1. Inserisci i file audio (es. `.mp3`, `.wav`, `.m4a`, ecc.) nella cartella `input/`.
2. Avvia lo script:
   ```bash
   python audio_to_text.py
   ```
3. Troverai i file di testo corrispondenti nella cartella `output/`.

## Configurazione

È possibile personalizzare il comportamento tramite il file `config.json`:

```json
{
  "model": "base",
  "language": "it",
  "overwrite": false
}
```

* `model`: Dimensione del modello Whisper (`tiny`, `base`, `small`, `medium`, `large`). Più è grande, più è accurato ma richiede più risorse e tempo.
* `language`: La lingua dell'audio (es. `it` per l'italiano, `en` per l'inglese, oppure `null` per il rilevamento automatico).
* `overwrite`: Se impostato su `false`, i file audio già elaborati in precedenza verranno saltati per risparmiare tempo.