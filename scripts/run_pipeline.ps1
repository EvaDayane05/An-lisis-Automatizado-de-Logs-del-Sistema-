powershell -ExecutionPolicy Bypass -File src/extraer_eventos.ps1
python src/clasificar_eventos.py examples/ejemplo_salida.json examples/classified_events.json
