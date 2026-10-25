import os
import json
import yfinance as yf
from fredapi import Fred

def obtener_datos_mercado():
    print("Descargando tickers de mercado...")
    spy_data = yf.Ticker("SPY").history(period="5d")
    rsp_data = yf.Ticker("RSP").history(period="5d")
    vix_data = yf.Ticker("^VIX").history(period="5d")
    
    ultimo_spy = float(spy_data['Close'].dropna().iloc[-1])
    ultimo_rsp = float(rsp_data['Close'].dropna().iloc[-1])
    ultimo_vix = float(vix_data['Close'].dropna().iloc[-1])
    
    ratio_spy_rsp = round(ultimo_spy / ultimo_rsp, 4)
    
    return {
        "SPY": round(ultimo_spy, 2),
        "RSP": round(ultimo_rsp, 2),
        "VIX": round(ultimo_vix, 2),
        "Ratio_SPY_RSP": ratio_spy_rsp
    }

def obtener_datos_fred():
    print("Consultando series macroeconomicas de la FRED...")
    api_key = os.environ.get("FRED_API_KEY")
    
    if not api_key:
        raise ValueError("Error: No se encontro la variable de entorno FRED_API_KEY.")
        
    fred = Fred(api_key=api_key)
    
    # Descarga de series oficiales (en millones de USD)
    # WALCL: Balance total de la FED
    # WTREGEN: Cuenta General del Tesoro (TGA)
    # RRPONTSYD: Operaciones de Repo Inverso
    # FEDFUNDS: Tasa efectiva de fondos federales (%)
    walcl = fred.get_series('WALCL').dropna().iloc[-1]
    tga = fred.get_series('WTREGEN').dropna().iloc[-1]
    rrp = fred.get_series('RRPONTSYD').dropna().iloc[-1]
    fedfunds = fred.get_series('FEDFUNDS').dropna().iloc[-1]
    
    # Formula de Liquidez Neta = Balance FED - (TGA + RRP)
    liquidez_neta_millones = walcl - (tga + rrp)
    liquidez_neta_billones = round(liquidez_neta_millones / 1_000_000, 3)
    
    return {
        "Tasa_FEDFUNDS": float(fedfunds),
        "Balance_FED_Millones": float(walcl),
        "TGA_Millones": float(tga),
        "Repo_Inverso_Millones": float(rrp),
        "Liquidez_Neta_Billones_USD": liquidez_neta_billones
    }

def main():
    try:
        mercado = obtener_datos_mercado()
        macro = obtener_datos_fred()
        
        resultado_consolidado = {
            "mercado": mercado,
            "macro_fred": macro
        }
        
        print("\n--- MATRIZ CUANTITATIVA EXTRAIDA CON EXITO ---")
        print(json.dumps(resultado_consolidado, indent=2))
        return resultado_consolidado
        
    except Exception as e:
        print(f"Error durante la ejecucion: {str(e)}")
        raise e

if __name__ == "__main__":
    main()
