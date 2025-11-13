# Analisis-Automatizado-de-Logs-del-Sistema-

# Proyecto Final PIA – Auditoría Forense Automatizada

Este proyecto forma parte del Entregable 4 del Proyecto Final PIA. Desarrolla un istema automatizado para la recoleccion, analisis y clasificacion de eventos de seguridad de windows, utilizando scripts en POWERSHELL y PYTHON, ademas de intregar un modelo de inteligencia artificial (IA) para mejorar la deteccion de eventos relevantes. 

---

 Componentes del Proyecto

 Extracción de eventos (PowerShell)
El script `extraer_eventos.ps1` recolecta eventos críticos del log de seguridad (IDs 4625, 4672, 4688) ocurridos en los últimos 7 días. Los resultados se guardan en formato JSON y se registran en un log estructurado (`logs.jsonl`) para trazabilidad.

Clasificación semántica (Python)
El script `clasificar_eventos.py` analiza cada evento y lo clasifica en categorías como:
- Acceso fallido
- Privilegios elevados
- Ejecución sospechosa
- Otro

Se añaden metadatos como `run_id` y `timestamp_clasificacion` para auditoría.

 Orquestación funcional
El script `run_pipeline.ps1` ejecuta ambos módulos en secuencia, permitiendo una operación automatizada desde un solo punto de entrada.

---

 Plan de IA

Se ha documentado un plan de uso de IA en `docs/ai_plan.md`, que describe cómo se podría integrar un modelo semántico (GPT o heurístico) para mejorar la clasificación de eventos. La plantilla de prompt se encuentra en `prompts/prompt_v1.json`.
La IA se integra en src/clasificar_eventos.py y se uso el modelo tngtech/deepseek-r1t2-chimera:free 

---

## 📁 Estructura del Proyecto

An-lisis-Automatizado-de-Logs-del-Sistema-/ ├── src/ │ ├── extraer_eventos.ps1 │ └── clasificar_eventos.py ├── scripts/ │ └── run_pipeline.ps1 ├── examples/ │ ├── ejemplo_salida.json │ ├── classified_events.json │ └── logs.jsonl ├── docs/ │ ├── ai_plan.md │ └── entregable_3.md ├── prompts/ │ └── prompt_v1.json └── README.md

An-lisis-Automatizado-de-Logs-del-Sistema-/
├── docs/
│   └──ai_plan.md
│   └──docss.md
│   └──entregable_2.md
│   └──entregable_3.md
│   
├── examples/
│   └── README2.md
│   └──classified_events.json
│   └──ejemplo_salida.json
│   └──logs.json
│   └──logs.jsonl
│
├── prompt/
│   └──prompt_v1.json
│
├── prompts/
│   └──prompt_v1.json
│
├── proposals/
│   └──propuesta.md
│
├── scripts/
│   └──clasificar_eventos.py
│   └──extraer_eventos.ps1
│   └──run_pipeline.ps1
│ 
├── src/
│   └──_pycache_/
│     └────config-cpython-312.pyc
│     └────config.cpython-313.pyc
│   └── clasificar_eventos.py              (El nuevo archivo para tu API key)
│   └── detectar_eventos.ps1    (El script que saca los logs de Windows)
│   └── extraer_eventos.ps1  (El script de Python con la IA)
│   └── tarea_1.py
│
├── tests/
│   └──Scripts de Validacion y pruebas
└── run_pipeline.ps1           (El script principal que ejecutarás)


Código

---

## 🚀 Ejecución del Pipeline

Desde PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/run_pipeline.ps1
Esto ejecuta la extracción de eventos y su clasificación automática.

. Estado del Proyecto
. Extracción de eventos de seguridad (PowerShell)

 . Clasificación semántica de eventos (Python)

 . Orquestación funcional con PowerShell

 . Logging estructurado en JSONL

 . Plan de IA documentado

 . Prompt inicial definido

 . Flujo reproducible y modular

 Evidencia de colaboración
Repositorio compartido en MS Teams

Captura del flujo funcional enviada

Commits y pull requests en GitHub

Código


 
