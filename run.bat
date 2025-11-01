@echo off
REM Script per eseguire lo script audio-to-text in Docker su Windows
REM Uso: run.bat [opzioni]

REM Crea le directory se non esistono
if not exist input mkdir input
if not exist output mkdir output

REM Converte i percorsi Windows in percorsi Docker
set "input_path=%1"
set "output_path=%2"

REM Sostituisce \ con / e aggiunge /app/ per i percorsi
if not "%input_path%"=="" (
    set "input_path=%input_path:\=/%"
    set "input_path=/app/%input_path%"
)

if not "%output_path%"=="" (
    set "output_path=%output_path:\=/%"
    set "output_path=/app/%output_path%"
)

REM Esegue il container con i parametri convertiti
docker-compose run --rm audio-to-text %input_path% %output_path% %3 %4 %5
