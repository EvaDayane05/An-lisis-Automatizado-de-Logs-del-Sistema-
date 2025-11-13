import json, sys, uuid
from datetime import datetime

def clasificar_evento(evento):
    mensaje = evento.get("Mensaje", "").lower()
    if "logon failure" in mensaje or "failed" in mensaje:
        categoria = "Acceso fallido"
    elif "privilege" in mensaje or "elevated" in mensaje:
        categoria = "Privilegios elevados"
    elif "process" in mensaje or "execution" in mensaje:
        categoria = "Ejecución sospechosa"
    else:
        categoria = "Otro"
    evento["Categoria"] = categoria
    return evento

def main(input_file, output_file):
    run_id = str(uuid.uuid4())
    try:
        with open(input_file, encoding="utf8") as f:
            contenido = f.read().strip()
            if not contenido:
                print(f"⚠️ El archivo '{input_file}' está vacío.")
                return
            eventos = json.loads(contenido)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return

    if not isinstance(eventos, list) or len(eventos) == 0:
        print(f"⚠️ El archivo no contiene eventos válidos.")
        return

    clasificados = []
    for evento in eventos:
        evento_clasificado = clasificar_evento(evento)
        evento_clasificado["run_id"] = run_id
        evento_clasificado["timestamp_clasificacion"] = datetime.utcnow().isoformat()
        clasificados.append(evento_clasificado)

    with open(output_file, "w", encoding="utf8") as f:
        json.dump(clasificados, f, indent=2, ensure_ascii=False)

    print(f"✅ Clasificación completada. Se procesaron {len(clasificados)} eventos.")