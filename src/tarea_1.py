import json
import logging
from datetime import datetime

# Configurar logging en formato JSON Lines
logging.basicConfig(
    filename='examples/log_ejecucion.jsonl',
    level=logging.INFO,
    format='%(message)s'
)

def log_event(event_type, details):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "details": details
    }
    logging.info(json.dumps(log_entry))

def analizar_sentimiento(texto):
    """Clasifica el sentimiento del texto de forma simple."""
    positivo = ['bueno', 'excelente', 'genial', 'feliz']
    negativo = ['malo', 'horrible', 'triste', 'terrible']

    score = sum(word in texto.lower() for word in positivo) - sum(word in texto.lower() for word in negativo)
    sentimiento = 'positivo' if score > 0 else 'negativo' if score < 0 else 'neutral'
    return sentimiento

def main(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    log_event("inicio_proceso", {"num_textos": len(data)})

    resultados = []
    for item in data:
        resultado = {
            "texto": item["texto"],
            "sentimiento": analizar_sentimiento(item["texto"])
        }
        resultados.append(resultado)
        log_event("analisis", resultado)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)

    log_event("fin_proceso", {"num_resultados": len(resultados)})


if __name__ == "__main__":
    main("examples/input_ejemplo.json", "examples/output_resultado.json")
