# AI_Plan – Propuesta para la IA

## 1. Objetivo general del uso de IA
Integrar un sistema de Inteligencia Artificial que permita analizar y clasificar eventos del registro de Windows para apoyar procesos de monitoreo, auditoría y detección de actividades sospechosas de manera automatizada.

---

## 2. Tareas donde se usará IA
- Clasificación automática de eventos del log de seguridad.
- Identificación de patrones o actividades anómalas.
- Distinción entre eventos rutinarios y sospechosos.
- Normalización de categorías para sistemas de monitoreo.

---

## 3. Modelo seleccionado
- **Modelo:** `tngtech/deepseek-r1t2-chimera:free`
- **Proveedor:** OpenRouter
- **Razones de selección:**
  - Acceso gratuito.
  - API REST fácil de integrar.
  - Baja latencia y buena velocidad.
  - Adecuado para clasificación textual.

---

## 4. Puntos de integración dentro del pipeline
1. Extracción de eventos (PowerShell)
2. **Clasificador IA (Python)** – aquí se hace la llamada al modelo.
3. Almacenamiento de resultados
4. Entrega de archivos finales

La IA se usa exclusivamente en el paso 2.

---

## 5. Diseño del Prompt

```
Eres un analista de ciberseguridad experto en Windows. Tu tarea es clasificar 
eventos de logs de Windows (Event IDs 4625, 4672, 4688) basándote en su mensaje.
Tu respuesta debe ser únicamente una de las siguientes categorías:
- Acceso Fallido
- Privilegios Elevados
- Ejecución de Proceso
- Actividad Sospechosa
- Indeterminado
```

---

## 6. Lógica de validación de las respuestas de IA
- La respuesta debe ser una categoría válida.
- Si la IA devuelve otra cosa → asignar **"Indeterminado"**.
- Si ocurre un error en la API → continuar proceso sin detener el pipeline.
- Si se alcanza el límite de uso → detener de forma segura.

---

## 7. Entradas y salidas esperadas

### Entrada:
- Mensaje del evento
- Event ID
- Timestamp

### Salida:
- Categoría final como texto plano

### Ejemplo:
**Entrada:**  
```
An account failed to log on. Logon Type: 3...
```

**Salida:**  
```
Acceso Fallido
```

---

## 8. Manejo de errores
- Conexión fallida → registrar y continuar.
- Respuesta inválida → marcar como Indeterminado.
- API Key faltante → detener ejecución.

---

## 10. Razones para no usar un modelo local
- Alta demanda de hardware (GPU).
- Compleja instalación.
- Mayor tiempo de inferencia.
- OpenRouter ofrece alternativas gratuitas más eficientes.

---

## 11. Impacto esperado en el proyecto
- Mayor velocidad en análisis.
- Clasificación consistente.
- Menor carga manual.
- Mejor trazabilidad de eventos.

---