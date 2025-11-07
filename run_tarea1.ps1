# Permitir ejecución temporal del script (no modifica configuración del sistema)
Set-ExecutionPolicy Bypass -Scope Process -Force

# Ruta al script principal
$scriptPath = "./src/detectar_eventos.ps1"

# Carpeta donde se guardarán los ejemplos de salida
$outputDir = "./examples"

# Crear carpeta si no existe
if (-not (Test-Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir | Out-Null
}

# Ejecutar el script principal
Write-Host "Ejecutando análisis de eventos..."
powershell -ExecutionPolicy Bypass -File $scriptPath

Write-Host "Análisis completado. Revisa la carpeta /examples para ver los resultados." -ForegroundColor Green
