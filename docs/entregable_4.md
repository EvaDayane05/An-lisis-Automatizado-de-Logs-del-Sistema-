# Entregable 4  
> Este entregable forma parte del repositorio único del proyecto PIA. La propuesta técnica se encuentra en `/proposals/propuesta.md`.

--- 

## Flujo técnico consolidado

El sistema se compone de dos módulos principales conectados mediante un script de orquestación (pipeline):

### 1. Extracción de eventos (PowerShell) — `src/extraer_eventos.ps1`
- Extrae eventos del *Windows Event Log* (Security) generados en los últimos 7 días.
- Filtra los Event IDs relevantes para ciberseguridad:
  - 4625 — Acceso fallido  
  - 4672 — Privilegios especiales asignados  
  - 4688 — Creación de proceso  
- Genera:
  - `examples/ejemplo_salida.json`
  - `examples/logs.jsonl`

### 2. Clasificación de eventos con IA (Python) — `src/clasificar_eventos.py`
- Lee los eventos extraídos por el módulo PowerShell.
- Construye un prompt para cada evento y lo envía al modelo IA de OpenRouter.
- Clasifica cada evento en una de las categorías:
  - Acceso Fallido  
  - Privilegios Elevados  
  - Ejecución de Proceso  
  - Actividad Sospechosa  
  - Indeterminado  
- Añade `run_id` y timestamp de clasificación.
- Genera `examples/classified_events.json`.

### 3. Orquestación del pipeline — `scripts/run_pipeline.ps1`
- Ejecuta automáticamente:
  1. Extracción de eventos  
  2. Clasificación de eventos  
- Controla errores, rutas y modo silencioso.

---

## IA integrada funcionalmente

### Modelo/API utilizado
- OpenRouter AI  
- Modelo: `tngtech/deepseek-r1t2-chimera:free`

### Punto de integración
La IA se invoca dentro de `clasificar_evento_con_ia()` en `clasificar_eventos.py`.

### Ejemplo de entrada/salida

Entrada enviada al modelo:
Clasifica el siguiente evento (Event ID: 4625):

An account failed to log on. Logon Type: 3. Account Name: user123

Salida esperada:
Acceso Fallido

Ejemplo del resultado final:
{
  "Timestamp": "2025-02-19T12:34:20Z",
  "EventID": 4625,
  "Level": "Information",
  "Mensaje": "An account failed to log on...",
  "Categoria": "Acceso Fallido",
  "run_id": "d8b1d90f-8b98-4c13-b210-e64483b0196f",
  "timestamp_clasificacion": "2025-02-19T19:34:55.123456"
}

---

## Evidencia reproducible

- Archivos de salida: `/examples/`
- Logs estructurados: `/examples/logs.jsonl`
- Script principal de orquestación: `/scripts/run_pipeline.ps1`

---

## Documentación técnica

### Requisitos
- Windows (necesario para `Get-WinEvent`)
- PowerShell 5+
- Python 3.8+
- Librería `requests` para Python  
- Archivo de configuración en `src/config.py` con OPENROUTER_API_KEY

### Ejecución
Ejecutar el pipeline completo:
./scripts/run_pipeline.ps1

Ejecutar en modo silencioso:
./scripts/run_pipeline.ps1 -Silent

### Archivos generados
- `examples/ejemplo_salida.json` — eventos extraídos  
- `examples/classified_events.json` — eventos clasificados por IA  

---

## Colaboración

En esta etapa participaron:

- Renata  
- René  
- Edgar  
- Sofía  
- Eva  

Evidencia en GitHub:
- Commits separados por módulo  
- Issues relacionados con fallas al consultar la API o permisos en Windows  
- Pull requests para integrar el pipeline completo  
- Ajustes finales distribuidos entre los miembros del equipo

---

## Observaciones

### Pendientes antes de la entrega final
- Verificar existencia de directorios antes de escribir archivos.
- Incluir datos sintéticos para pruebas.
- Mejorar manejo de respuestas inesperadas por parte de la IA.
- Optimizar el filtrado de eventos para evitar duplicados.

### Decisiones técnicas tomadas
- Separación de extracción (PowerShell) y clasificación (Python).
- Elección de OpenRouter por disponibilidad de modelos gratuitos.
- Uso de JSONL para logs altamente reproducibles.

### Aprendizajes
- Importancia de logs estructurados para auditorías.
- Integración eficiente entre PowerShell y Python en un mismo pipeline.
- Validar categorizaciones de la IA para garantizar calidad del análisis.
