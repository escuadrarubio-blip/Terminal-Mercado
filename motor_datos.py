import yfinance as yf
import pandas as pd
import json

def obtener_datos_mercado():
    print("Descargando tickers principales...")
    tickers = yf.download(["SPY", "RSP", "^VIX"], period="1mo", interval="1d")
    
    # Extraer precios de cierre recientes
    cierre = tickers['Close']
    ultimo_spy = float(cierre['SPY'].dropna().iloc[-1])
    ultimo_rsp = float(cierre['RSP'].dropna().iloc[-1])
    ultimo_vix = float(cierre['^VIX'].dropna().iloc[-1])
    
    # Cálculo del ratio de amplitud de mercado
    ratio_spy_rsp = round(ultimo_spy / ultimo_rsp, 4)
    
    resumen = {
        "spy": round(ultimo_spy, 2),
        "rsp": round(ultimo_rsp, 2),
        "vix": round(ultimo_vix, 2),
        "ratio_amplitud": ratio_spy_rsp
    }
    
    print("Datos obtenidos con éxito:")
    print(json.dumps(resumen, indent=2))
    return resumen

if __name__ == "__main__":
    obtener_datos_mercado()
