import yfinance as yf
import json

def obtener_datos_mercado():
    print("Iniciando descarga individual de tickers...")
    
    # Descargar datos recientes de cada activo por separado
    spy_data = yf.Ticker("SPY").history(period="5d")
    rsp_data = yf.Ticker("RSP").history(period="5d")
    vix_data = yf.Ticker("^VIX").history(period="5d")
    
    # Extraer el último precio de cierre disponible
    ultimo_spy = float(spy_data['Close'].dropna().iloc[-1])
    ultimo_rsp = float(rsp_data['Close'].dropna().iloc[-1])
    ultimo_vix = float(vix_data['Close'].dropna().iloc[-1])
    
    # Calcular el cociente de amplitud
    ratio_spy_rsp = round(ultimo_spy / ultimo_rsp, 4)
    
    resumen = {
        "SPY": round(ultimo_spy, 2),
        "RSP": round(ultimo_rsp, 2),
        "VIX": round(ultimo_vix, 2),
        "Ratio_SPY_RSP": ratio_spy_rsp
    }
    
    print("\n--- DATOS DE MERCADO EXTRAÍDOS CON ÉXITO ---")
    print(json.dumps(resumen, indent=2))
    return resumen

if __name__ == "__main__":
    obtener_datos_mercado()
