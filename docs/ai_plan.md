# Plan de uso de IA

## Propósito
Clasificar eventos de seguridad en categorías semánticas.

## Punto de integración
Después de la extracción con PowerShell.

## Tipo de modelo/API
GPT-4 o heurísticas locales.

## Ejemplo de prompt
"Clasifica los eventos en acceso fallido, privilegios elevados, ejecución sospechosa."

## Datos de entrada
Archivo JSON con: Timestamp, EventID, Level, Mensaje.

## Plantilla
Ver `/prompts/prompt_v1.json`
