<<<<<<< HEAD
import json, sys, uuid, requests
from datetime import datetime
 
# Importamos la clave desde nuestro archivo config.py
try:
    from config import OPENROUTER_API_KEY
except ImportError:
    print("Error: No se encontró el archivo 'config.py'.", file=sys.stderr)
    print("Asegúrate de crearlo en la carpeta 'src/' con tu OPENROUTER_API_KEY.", file=sys.stderr)
    sys.exit(1)
 
# --- PARÁMETROS DE LA API Y PROMPT ---
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODELO_IA = "tngtech/deepseek-r1t2-chimera:free"
 
PROMPT_SISTEMA = """
Eres un analista de ciberseguridad experto en Windows. Tu tarea es clasificar 
eventos de logs de Windows (Event IDs 4625, 4672, 4688) basándote en su mensaje.
Tu respuesta debe ser ÚNICAMENTE una de las siguientes categorías, 
sin saludos, explicaciones ni texto adicional:
- 'Acceso Fallido'
- 'Privilegios Elevados'
- 'Ejecución de Proceso'
- 'Actividad Sospechosa'
- 'Indeterminado'
"""
 
def clasificar_evento_con_ia(evento, silent=False):
    """
    Clasifica un evento usando la API de OpenRouter.
    """
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "sk-or-....tu-clave-secreta-aqui":
        print("Error: La OPENROUTER_API_KEY no está configurada en 'src/config.py'.", file=sys.stderr)
        return "Error: API Key no configurada"
 
    mensaje = evento.get("Mensaje", "")
    event_id = evento.get("EventID", "N/A")
    prompt_usuario = f"Clasifica el siguiente evento (Event ID: {event_id}):\n\n{mensaje}"
 
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:8080",
        "X-Title": "Proyecto Clasificador de Eventos"
    }
    data = { "model": MODELO_IA, "messages": [ {"role": "system", "content": PROMPT_SISTEMA}, {"role": "user", "content": prompt_usuario} ], "temperature": 0.1 }
 
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=15)
        response.raise_for_status()
        resultado_ia = response.json()
        categoria = resultado_ia['choices'][0]['message']['content'].strip()
        categorias_validas = ['Acceso Fallido', 'Privilegios Elevados', 'Ejecución de Proceso', 'Actividad Sospechosa', 'Indeterminado']
        if categoria not in categorias_validas:
            if not silent:
                print(f"Advertencia: La IA devolvió '{categoria}'. Se marcará como 'Indeterminado'.", file=sys.stderr)
            categoria = 'Indeterminado'
        return categoria
 
    except requests.exceptions.RequestException as e:
        print(f"Error en la llamada a la API: {e}", file=sys.stderr)
        return "Error: Falla de API"
    except (KeyError, IndexError):
        print(f"Error al parsear la respuesta de la IA: {response.text}", file=sys.stderr)
        return "Error: Respuesta IA inválida"
    except Exception as e:
        print(f"Error inesperado en clasificación: {e}", file=sys.stderr)
        return "Error: Desconocido"
 
def main(input_file, output_file, silent=False):
    run_id = str(uuid.uuid4())
    try:
        #  Ahora se abre con utf-8-sig
        with open(input_file, "r", encoding="utf-8-sig") as f:
            contenido = f.read().strip()
            if not contenido:
                if not silent:
                    print(f"El archivo '{input_file}' está vacío.")
                return
            eventos = json.loads(contenido)
    except Exception as e:
        print(f"Error al leer el archivo: {e}", file=sys.stderr)
        return
 
    if not isinstance(eventos, list) or len(eventos) == 0:
        if not silent:
            print(f"El archivo no contiene eventos válidos.")
        return
 
    clasificados = []
    if not silent:
        print(f"Iniciando clasificación con IA para {len(eventos)} eventos... (Esto puede tardar)")
    for i, evento in enumerate(eventos, 1):
        if not silent:
            print(f" -> Procesando evento {i}/{len(eventos)} (ID: {evento.get('EventID')})")
        categoria_ia = clasificar_evento_con_ia(evento, silent) # Pasa el flag 'silent'
        evento_clasificado = evento.copy()
        evento_clasificado["Categoria"] = categoria_ia
        evento_clasificado["run_id"] = run_id
        evento_clasificado["timestamp_clasificacion"] = datetime.utcnow().isoformat()
        clasificados.append(evento_clasificado)
 
    #  También se guarda con utf-8-sig
    with open(output_file, "w", encoding="utf-8-sig") as f:
        json.dump(clasificados, f, indent=2, ensure_ascii=False)
 
    if not silent:
        print(f" Clasificación con IA completada. Se procesaron {len(clasificados)} eventos.")
 
if __name__ == "__main__":
    # Revisa si --silent está en los argumentos
    silent_mode = "--silent" in sys.argv
    # Filtra los argumentos para que solo queden los nombres de archivo
    args = [arg for arg in sys.argv[1:] if arg != "--silent"]
    if len(args) != 2:
        print("Uso: python clasificar_eventos.py <archivo_entrada> <archivo_salida> [--silent]", file=sys.stderr)
        sys.exit(1)
    input_file = args[0]
    output_file = args[1]
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "sk-or-....tu-clave-secreta-aqui":
        print(" Error: Tu OPENROUTER_API_KEY no está configurada.", file=sys.stderr)
        print("Por favor, edita el archivo 'src/config.py' y añade tu clave.", file=sys.stderr)
        sys.exit(1)
    main(input_file, output_file, silent=silent_mode)
=======
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
                print(f" El archivo '{input_file}' está vacío.")
                return
            eventos = json.loads(contenido)
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return

    if not isinstance(eventos, list) or len(eventos) == 0:
        print(f" El archivo no contiene eventos válidos.")
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
>>>>>>> 28b4c6fdc5b0679a50353144f2bca62e456ab3b3
