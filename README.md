# Audio to Text - Docker Container

Questo progetto converte file audio in testo utilizzando il modello Whisper di OpenAI, tutto containerizzato con Docker.

## Prerequisiti

- Docker
- Docker Compose

## Struttura del progetto

```
audio-to-text/
├── audio_to_text.py      # Script principale
├── Dockerfile            # Configurazione Docker
├── docker-compose.yml    # Configurazione Docker Compose
├── requirements.txt      # Dipendenze Python
├── run.sh               # Script di avvio (Linux/Mac)
├── run.bat              # Script di avvio (Windows)
├── input/               # Directory per i file audio
└── output/              # Directory per i risultati
```

## Utilizzo

### 1. Build del container

```bash
docker-compose build
```

### 2. Esecuzione

#### Opzione A: Usando gli script di avvio

**Windows:**
```cmd
run.bat input/audio.mp3
run.bat input/audio.wav --model large
run.bat input/audio.m4a --output output/transcription.txt
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh input/audio.mp3
./run.sh input/audio.wav --model large
./run.sh input/audio.m4a --output output/transcription.txt
```

#### Opzione B: Usando Docker Compose direttamente

```bash
# Trascrizione base
docker-compose run --rm audio-to-text input/audio.mp3

# Con modello specifico
docker-compose run --rm audio-to-text input/audio.wav --model large

# Con file di output


```

#### Opzione C: Usando Docker direttamente

```bash
# Build dell'immagine
docker build -t audio-to-text .

# Esecuzione
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" audio-to-text input/audio.mp3
```

## Modelli disponibili

- `tiny`: Più veloce, meno accurato
- `base`: Bilanciato (default)
- `small`: Più accurato, più lento
- `medium`: Ancora più accurato
- `large`: Più accurato, più lento

## Formati audio supportati

- MP3
- WAV
- M4A
- FLAC
- OGG
- E molti altri formati supportati da FFmpeg

## Note

- I file audio vanno messi nella directory `input/`
- I risultati vengono salvati nella directory `output/`
- Il primo avvio potrebbe richiedere più tempo per scaricare il modello Whisper
- I modelli più grandi (`large`) richiedono più memoria e tempo di elaborazione