# Análisis Automatizado de Logs del Sistema – Proyecto PIA
# Descripción General del Entregable 4

Este entregable corresponde a la fase en la que se integran las primeras tareas del proyecto y se valida el flujo funcional casi completo, incluyendo:

- Extracción automatizada de eventos del sistema (PowerShell)
- Clasificación de eventos usando IA (Python + OpenRouter)
- Logging estructurado
- Pipeline funcional y reproducible
- Evidencia generada en /examples

----

# Avance Técnico Consolidado

## Extracción de Eventos (PowerShell)

Script:
|__scripts/extraer_eventos.ps1


Obtiene eventos de seguridad relevantes (IDs 4625, 4672, 4688) y los guarda en:
|__examples/ejemplo_salida.json


El proceso también genera logs en:
|__examples/logs.jsonl

## Clasificación con Inteligencia Artificial (Python)

Script:
|__src/clasificar_eventos.py

La IA clasifica los eventos en:

- Acceso Fallido
- Privilegios Elevados
- Ejecución de Proceso
- Actividad Sospechosa
- Indeterminado

**Modelo usado:**
|__tngtech/deepseek-r1t2-chimera:free

**Proveedor:**
|__OpenRouter API


**La clave API se gestiona mediante:**
|__src/config.py (NO incluido en GitHub)

## Orquestación del Pipeline

El flujo completo se ejecuta mediante:
|__scripts/run_pipeline.ps1


Este script:

- Ejecuta la extracción de eventos
- Llama al clasificador en Python
- Genera evidencia en /examples
- Registra el proceso en logs.jsonl

## Ejecución del Pipeline

Ejecutar desde PowerShell:
|__powershell -ExecutionPolicy Bypass -File scripts/run_pipeline.ps1


Al finalizar, se generan:

Archivo	                               |       Descripción
examples/ejemplo_salida.json	          |       Eventos extraídos
examples/classified_events.json	       |       Eventos clasificados con IA
examples/logs.jsonl	                   |       Log del pipeline

## Plan de IA (versión para Entregable 4)

La IA se integra únicamente para clasificar eventos.

**El prompt utilizado se encuentra en:**
|__prompts/prompt_v1.json

**La IA se invoca con:**
|__requests.post(API_URL, headers, json=data)


El sistema valida que las respuestas sean coherentes y recuperables (en caso contrario dira "INDETERMINADO").

## Estructura del Proyecto (Entregable 4)
```plaintext
Análisis-Automatizado-de-Logs-del-Sistema/
├── docs/
│   ├── ai_plan.md
│   └── entregable_4.md
│
├── examples/
│   ├── ejemplo_salida.json
│   ├── classified_events.json
│   └── logs.jsonl
│
├── prompts/
│   └── prompt_v1.json
│
├── scripts/
│   ├── extraer_eventos.ps1
│   ├── clasificar_eventos.py
│   └── run_pipeline.ps1
│
├── src/
│   ├── clasificar_eventos.py
│   ├── extraer_eventos.ps1
│   └── config.py
│
└── README.md
```
 
### Evidencia 
La carpeta /examples incluye evidencia real generada por la ejecución del pipeline:
- Eventos originales extraídos
- Eventos clasificados por IA
- Log estructurado del proceso

### Estado Actual del Proyecto (Entregable 4)
- Flujo técnico consolidado
- IA integrada y funcionando
- Logging estructurado implementado
- Pipeline reproducible
- Documentación técnica actualizada
- Archivos generados correctamente

  
