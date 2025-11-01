@echo off
REM Script semplificato per trascrivere audio con Docker
REM Uso: transcribe.bat nomefile.mp3 [modello] [output]

REM Crea le directory se non esistono
if not exist input mkdir input
if not exist output mkdir output

REM Controlla se è stato fornito un file
if "%1"=="" (
    echo Uso: transcribe.bat nomefile.mp3 [modello] [output]
    echo Esempi:
    echo   transcribe.bat input\audio.mp3
    echo   transcribe.bat input\audio.mp3 large
    echo   transcribe.bat input\audio.mp3 base output\result.txt
    exit /b 1
)

REM Costruisce il comando Docker
set "cmd=docker-compose run --rm audio-to-text /app/%1"

REM Aggiunge il modello se specificato
if not "%2"=="" (
    set "cmd=%cmd% --model %2"
)

REM Aggiunge l'output se specificato
if not "%3"=="" (
    set "cmd=%cmd% --output /app/%3"
)

REM Esegue il comando
echo Eseguendo: %cmd%
%cmd%

