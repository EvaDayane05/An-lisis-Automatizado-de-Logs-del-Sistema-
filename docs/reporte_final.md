# Reporte final

> Este documento forma parte del entregable final del proyecto PIA. Su propósito es dejar constancia de los ajustes significativos realizados durante el desarrollo del proyecto que afectaron el resultado final.

---

## Cambios en tareas técnicas

Durante el desarrollo del proyecto se realizaron varios ajustes respecto a la planeación inicial. Los cambios principales fueron:

### 1. Cambio en la forma de extraer eventos
Originalmente se planeaba utilizar únicamente Python para interactuar con los logs de Windows.  
Sin embargo, el acceso directo al *Windows Event Log* desde Python presentó limitaciones y requería librerías externas o dependencias adicionales.

**Cambio realizado:**  
Se sustituyó el módulo de extracción en Python por un script de PowerShell (`extraer_eventos.ps1`), permitiendo:

- Acceso nativo y directo a los eventos del log.
- Filtrado eficiente por Event ID.
- Escritura inmediata de logs en formato JSON y JSONL.

**Motivo del cambio:**  
Compatibilidad, menor complejidad y mejor integración con sistemas Windows.

---

### 2. Ajuste al pipeline general
La planeación original contemplaba ejecutar manualmente cada parte del proyecto.

**Cambio realizado:**  
Se integró un pipeline automático (`run_pipeline.ps1`) que orquesta la extracción y clasificación completa.

**Motivo:**  
Reducir errores manuales, estandarizar el flujo y permitir ejecución silenciosa.

---

## Cambios en el uso de IA

### 1. Cambio de modelo IA
Inicialmente se planeaba usar GPT-4 o un modelo estándar de OpenAI.

**Cambio realizado:**  
No se realizo algun cambio, OpenRouter fue nuestra opción preferida para el trabajo, usando el modelo:  
`tngtech/deepseek-r1t2-chimera:free`

**Ventajas de quedarse con la opcion anterior:**
- Acceso gratuito sin credit-card.
- Límite de peticiones más flexible.
- Integración más sencilla mediante API REST.
- Ahorro de costos para el equipo.

---

### 2. Ajuste en diseño de prompts
Al inicio se intentó utilizar prompts largos con explicación y análisis detallado del evento.  
Esto generó respuestas extensas, inconsistentes y difíciles de validar.

**Cambio realizado:**
Se diseñó un prompt rígido en formato de “clasificación cerrada”, pidiendo únicamente devolver:

- Acceso Fallido  
- Privilegios Elevados  
- Ejecución de Proceso  
- Actividad Sospechosa  
- Indeterminado  

**Resultado:**  
Respuestas más consistentes, fáciles de validar y aptas para procesamiento automático.

---

### 3. Cambio en el punto de integración de IA
Originalmente se planeaba procesar eventos en lote.  
Esto generaba errores cuando la IA no seguía el formato esperado.

**Cambio realizado:**  
Se clasifican los eventos **uno por uno**, lo que facilita recuperar errores y continuar el proceso.

---

## Cambios en roles o distribución del trabajo

Durante el desarrollo se ajustaron varias responsabilidades:

- **Renata** — Responsable del módulo Python, diseño del clasificador de IA y validación del prompt.  
- **René** — Implementación del pipeline PowerShell e integración final del proyecto.  
- **Edgar** — Depuración de errores en el extractor, estructura de logs y pruebas locales.  
- **Sofía** — Documentación técnica, estructura del repositorio y generación de entregables.  
- **Eva** — Pruebas de usuario, validación del flujo completo y evidencia reproducible.

**Motivo de la reorganización:**  
Aprovechar mejor las habilidades individuales del equipo y dividir trabajo según especialidades técnicas.

---

## Decisiones técnicas relevantes

Las siguientes decisiones influyeron directamente en el diseño y calidad del sistema:

### 1. Uso de PowerShell en lugar de Python para extraer eventos
Facilitó acceso directo al log de seguridad.

### 2. Uso de JSONL para logs de auditoría
Permitió:
- Registrar cada evento línea por línea.
- Mantener historial claro de ejecuciones.
- Asegurar reproducibilidad del proyecto.

### 3. Implementación de modo silencioso
Se agregó una bandera `--silent` y `-Silent` para:
- Evitar sobrecarga de salida en consola.
- Facilitar automatización.

### 4. Validación de categorías devueltas por IA
Debido a inconsistencias iniciales en las respuestas del modelo, se implementó un filtro que fuerza un valor válido.

### 5. Uso de un pipeline único para garantizar consistencia
`run_pipeline.ps1` asegura que:
- Todo el proceso sea reproducible.
- No dependan pasos manuales.
- Se conserve la estructura del proyecto.

---

## Impacto en el entregable final

Los cambios aplicados tuvieron el siguiente impacto:

### Aspectos positivos logrados
- Flujo totalmente automatizado.
- Clasificación estable y reproducible.
- Documentación clara y modular.
- Extracción de eventos confiable en Windows.
- Mejor manejo de errores gracias al pipeline.

### Elementos pendientes o simplificados
- No se incluyó una interfaz gráfica como se consideró inicialmente.  
- El sistema depende de conexión a Internet para el módulo IA.  
- La IA podría mejorarse con modelos más robustos si se cuenta con créditos en un futuro.

### Aprendizajes clave del equipo
- Validar modelos IA antes de integrarlos es fundamental.  
- El uso de JSONL facilita trazabilidad.  
- PowerShell y Python pueden integrarse exitosamente en un solo flujo.  
- La automatización evita errores humanos y mantiene consistencia.

---

## Confirmación de cierre

Confirmamos que la última actualización del repositorio fue realizada **antes del 18 de noviembre a las 23:59 hrs (hora local de Monterrey)**.

- **Fecha del último commit:** 2025-11-18 09:21 PM 
- **Usuario responsable del cierre:** Edgar


