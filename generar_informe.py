import os
import json
import glob
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
    print(f"Documentos encontrados en docs/: {archivos_pdf}")
    
    for ruta in archivos_pdf:
        try:
            lector = PdfReader(ruta)
            texto_archivo = ""
            for pagina in lector.pages:
                t = pagina.extract_text()
                if t:
                    texto_archivo += t + "\n"
            texto_acumulado += f"\n--- CONTENIDO: {os.path.basename(ruta)} ---\n" + texto_archivo
        except Exception as e:
            print(f"Aviso: No se pudo leer {ruta}: {e}")
            
    return texto_acumulado

def generar_reporte():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la variable de entorno GEMINI_API_KEY.")

    datos = cargar_datos_cuantitativos()
    contexto_teorico = extraer_texto_docs()
    
    # Si los documentos son muy extensos, tomamos los primeros 40.000 caracteres para asegurar agilidad
    contexto_recortado = contexto_teorico[:40000] if contexto_teorico else "Sin marco documental adicional."

    prompt = f"""
Eres un analista macrofinanciero senior. Tu tarea es generar el informe diario de mercado combinando la matriz cuantitativa del día con el marco metodológico de referencia provisto en los documentos base.

MARCO METODOLÓGICO / BASE TEÓRICA:
{contexto_recortado}

MATRIZ CUANTITATIVA DEL DÍA:
{json.dumps(datos, indent=2, ensure_ascii=False)}

INSTRUCCIONES DE REDACCIÓN:
1. Resumen Ejecutivo del Pulso de Mercado (SPY, RSP y Amplitud).
2. Diagnóstico de Liquidez Neta de la FED (WALCL, TGA, Repo Inverso).
3. Estructura de Derivados (Put/Call Ratio y niveles de Open Interest).
4. Relaciones Intermercado (Riesgo crediticio con HYG/IEI y pulso con COPX/GLD).
5. Conclusión Operativa y Niveles Críticos para la sesión.

Entrega el informe directamente en formato Markdown limpio y profesional.
"""

    print("Enviando solicitud a Gemini...")
    cliente = genai.Client(api_key=api_key)
    respuesta = cliente.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    contenido_informe = respuesta.text
    with open("informe_hoy.md", "w", encoding="utf-8") as f:
        f.write(contenido_informe)

    print("\n--- INFORME DIARIO GENERADO Y GUARDADO EN 'informe_hoy.md' ---")
    return contenido_informe

if __name__ == "__main__":
    generar_reporte()
