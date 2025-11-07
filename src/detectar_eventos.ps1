param(
    [string]$OutputFile = "examples/ejemplo_salida.json",
    [string]$LogFile = "examples/logs.jsonl",
    [int]$MaxEvents = 50
)

$eventos = Get-WinEvent -LogName Security -FilterXPath "*[System[TimeCreated[timediff(@SystemTime) <= 86400000]]]"


$resultados = @()

foreach ($evento in $eventos) {
    if ($evento.Id -eq 4625 -or $evento.Id -eq 4672 -or $evento.Id -eq 4688) {

        $obj = [PSCustomObject]@{
            Timestamp = $evento.TimeCreated
            EventID = $evento.Id
            Level = $evento.LevelDisplayName
            Mensaje = $evento.Message
        }

        $resultados += $obj

        # Logging en formato JSONL
        $logLine = $obj | ConvertTo-Json -Compress
        Add-Content -Path $LogFile -Value $logLine
    }
}

$resultados | ConvertTo-Json -Depth 4 | Out-File -Encoding utf8 $OutputFile

Write-Host "Análisis finalizado. Revisar carpeta /examples"

