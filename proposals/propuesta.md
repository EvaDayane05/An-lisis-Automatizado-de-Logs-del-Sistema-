Tarea 1: Extracción de eventos del sistema

Propósito: Obtener eventos recientes de los registros de Seguridad, Sistema y Aplicación, y detectar eventos sospechosos por ID.

Área: SOC / Blue Team

Entradas esperadas: Logs del sistema (Security, System, Application)

Salidas esperadas: Archivos CSV con eventos generales y sospechosos

Procedimiento: Uso de Get-WinEvent con filtros por fecha e ID, exportación a CSV

Complejidad técnica: Media – requiere manejo de eventos, filtrado y exportación

Dependencias: Librerias agregadas de Python (pandas, requests, csv, os, logging)


Tarea 2: Mostrar conexiones y procesos

Propósito: Identificar conexiones activas y procesos sin firma digital válida

Área: SOC / Blue Team

Entradas esperadas: Estado actual del sistema (conexiones TCP, procesos)

Salidas esperadas: Listado en consola de conexiones y procesos sin firma

Procedimiento: Uso de Get-NetTCPConnection y Get-Process con verificación de firmas

Complejidad técnica: Media – requiere comprensión de procesos y conexiones

Dependencias: PowerShell, acceso a funciones del sistema


Tarea 3: Investigación de direcciones IP

Propósito: Verificar la reputación de IPs públicas conectadas al sistema usando AbuseIPDB

Área: SOC / Threat Intelligence / Blue Team

Entradas esperadas: Lista de IPs manual o detectadas automáticamente

Salidas esperadas: Clasificación por riesgo (bajo, medio, alto) en consola

Procedimiento: Consulta a API de AbuseIPDB con clave segura, filtrado de IPs privadas

Complejidad técnica: Alta – requiere manejo de API, validación de IPs y clasificación

Dependencias: PowerShell, clave API de AbuseIPDB, conexión a internet 
