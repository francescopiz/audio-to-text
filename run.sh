#!/bin/bash

# Script per eseguire lo script audio-to-text in Docker
# Uso: ./run.sh [opzioni]

# Crea le directory se non esistono
mkdir -p input output

# Esegue il container con i parametri passati
docker-compose run --rm audio-to-text "$@"
