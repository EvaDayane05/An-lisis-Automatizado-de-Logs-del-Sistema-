##########Pipeline actualizado 
 
 
[CmdletBinding()]
param(
    # Agrega esta bandera para ejecutar todo el proceso en silencio.
    # Ejemplo: ./run_pipeline.ps1 -Silent
    [switch]$Silent
)
 
# --- 1. Definición de Rutas ---
$ExtractorScript = "src/extraer_eventos.ps1"
$ClassifierScript = "src/clasificar_eventos.py"
$EventFile = "examples/ejemplo_salida.json"
$ClassifiedFile = "examples/classified_events.json"
 
# --- 2. Preparar Argumentos Silenciosos ---
$PSCommonArgs = @{
    ErrorAction = "Stop" # Detener el script si hay un error
}
$PythonArgs = @($EventFile, $ClassifiedFile)
 
if ($Silent) {
    # Suprime la salida de PowerShell (Advertencias, Información)
    $PSCommonArgs["WarningAction"] = "SilentlyContinue"
    $PSCommonArgs["InformationAction"] = "SilentlyContinue"
    # Agrega la bandera para el script de Python
    $PythonArgs += "--silent"
}
 
# --- 3. Ejecución del Flujo ---
try {
    if (-not $Silent) {
        Write-Host "Paso 1: Extrayendo eventos de Windows..."
    }
    # Ejecuta el extractor de eventos
    # Pasamos los argumentos comunes (que incluyen los de silencio)
    powershell -ExecutionPolicy Bypass -File $ExtractorScript -OutputFile $EventFile @PSCommonArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Falló la extracción de eventos."
    }
 
    if (-not $Silent) {
        Write-Host "Paso 2: Clasificando eventos con IA..."
    }
 
    # Ejecuta el clasificador de Python
    # $PythonArgs ya contiene "--silent" si es necesario
    python $ClassifierScript $PythonArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Falló la clasificación con IA."
    }
 
    if (-not $Silent) {
        Write-Host " Proceso de automatización completado."
        Write-Host "Resultados guardados en: $ClassifiedFile"
    }
} catch {
    Write-Error " Error en el pipeline: $_"
    exit 1
}