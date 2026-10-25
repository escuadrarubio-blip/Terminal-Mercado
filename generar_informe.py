import os
import json
import glob
from datetime import datetime
from pypdf import PdfReader
from google import genai

def cargar_datos_cuantitativos():
    if not os.path.exists("datos_hoy.json"):
        raise FileNotFoundError("No se encontró el archivo datos_hoy.json.")
    with open("datos_hoy.json", "r", encoding="utf-8") as f:
        return json.load(f)

def extraer_texto_docs():
    texto_acumulado = ""
    archivos_pdf = glob.glob("docs/*.pdf")
    print(f"Documentos detectados en docs/: {archivos_pdf}")
    
    for ruta in archivos_pdf:
        try:
            lector = PdfReader(ruta)
            texto_archivo = ""
            for pagina in lector.pages:
                t = pagina.extract_text()
                if t:
                    texto_archivo += t + "\n"
            texto_acumulado += f"\n--- DOCUMENTO: {os.path.basename(ruta)} ---\n" + texto_archivo
        except Exception as e:
            print(f"Aviso: No se pudo leer {ruta}: {e}")
            
    return texto_acumulado

def generar_reporte():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY.")

    datos = cargar_datos_cuantitativos()
    contexto_teorico = extraer_texto_docs()
    contexto_recortado = contexto_teorico[:40000] if contexto_teorico else "Sin marco documental cargado."

    # Detección de día: 6 corresponde a domingo en Python
    es_domingo = datetime.now().weekday() == 6
    tipo_informe = "Informe Semanal (Perspectiva Estratégica)" if es_domingo else "Informe Matutino de Inteligencia de Mercado (Sesión Diaria)"

    # System Prompt formal según Hoja de Ruta Maestra (Punto 2.2)
    system_instruction = f"""
Eres el Director de Estrategia Macro y Analista Senior del Terminal de Mercados.
Tu base metodológica, axiomas analíticos y reglas deductivas provienen estrictamente de los DOS TOMOS adjuntos en tu contexto.

Tu tarea consiste en:
1. Analizar la matriz cuantitativa suministrada (VIX, ratio SPY/RSP, liquidez neta FED, niveles de opciones y ratios intermercado).
2. Generar el "{tipo_informe}".
3. Interpretar la acción del precio y la liquidez con la profundidad de un estratega macroeconómico institucional (al estilo de José Luis Cava y análisis de liquidez global), explicando siempre el "por qué" en lenguaje sencillo, directo y pedagógico.
4. Respetar la verdad de los datos: Si los datos no muestran tendencia clara, concluye neutralidad; jamás inventes datos numéricos.

Estructura requerida del informe (en Markdown limpio):
- 1. Titular Operativo y Diagnóstico de 1 Frase.
- 2. Estado de la Liquidez y Macro (FED, Balance, Tipos).
- 3. Amplitud y Régimen de Mercado (SPY vs RSP, VIX, Cobre/Oro).
- 4. Mapeo de Posicionamiento de Opciones (Zonas de dolor, muros de Puts y Calls).
- 5. Conclusión y Escenario Más Probable para la Sesión / Semana.
- 6. Bloque JSON de salida estructurada para el sistema de trading.

MARCO METODOLÓGICO Y TEÓRICO (TOMOS):
{contexto_recortado}
"""

    prompt_usuario = f"""
FECHA DE EJECUCIÓN: {datetime.now().strftime('%Y-%m-%d')}
TIPO DE INFORME: {tipo_informe}

MATRIZ CUANTITATIVA DEL DÍA:
{json.dumps(datos, indent=2, ensure_ascii=False)}

Por favor, elabora el reporte respetando estrictamente los 6 puntos de la estructura requerida.
"""

    print("Enviando matriz y sustrato a Gemini 3.8 Flash...")
    cliente = genai.Client(api_key=api_key)
    respuesta = cliente.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt_usuario,
        config={
            "system_instruction": system_instruction
        }
    )

    contenido_informe = respuesta.text
    with open("informe_hoy.md", "w", encoding="utf-8") as f:
        f.write(contenido_informe)

    print("\n--- INFORME GENERADO EXITOSAMENTE EN 'informe_hoy.md' ---")
    return contenido_informe

if __name__ == "__main__":
    generar_reporte()
