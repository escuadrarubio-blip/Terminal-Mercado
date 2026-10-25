import os
import json
import yfinance as yf
from fredapi import Fred

def obtener_datos_mercado_y_ratios():
    print("Descargando activos base y ratios intermercado...")
    tickers_requeridos = ["SPY", "RSP", "^VIX", "HYG", "IEI", "COPX", "GLD"]
    precios = {}
    
    for t in tickers_requeridos:
        try:
            hist = yf.Ticker(t).history(period="5d")
            precios[t] = float(hist['Close'].dropna().iloc[-1])
        except Exception as e:
            print(f"Aviso: No se pudo obtener precio para {t}: {e}")
            precios[t] = None

    # Amplitud de mercado (SPY/RSP)
    ratio_spy_rsp = None
    if precios.get("SPY") and precios.get("RSP"):
        ratio_spy_rsp = round(precios["SPY"] / precios["RSP"], 4)

    # Ratios intermercado
    ratio_high_yield = None
    if precios.get("HYG") and precios.get("IEI"):
        ratio_high_yield = round(precios["HYG"] / precios["IEI"], 4)

    ratio_cobre_oro = None
    if precios.get("COPX") and precios.get("GLD"):
        ratio_cobre_oro = round(precios["COPX"] / precios["GLD"], 4)

    return {
        "SPY": round(precios["SPY"], 2) if precios.get("SPY") else None,
        "RSP": round(precios["RSP"], 2) if precios.get("RSP") else None,
        "VIX": round(precios["^VIX"], 2) if precios.get("^VIX") else None,
        "Ratio_SPY_RSP": ratio_spy_rsp,
        "Ratio_High_Yield_HYG_IEI": ratio_high_yield,
        "Ratio_Cobre_Oro_COPX_GLD": ratio_cobre_oro
    }

def obtener_niveles_opciones_spy():
    print("Procesando cadena de derivados de SPY...")
    try:
        spy = yf.Ticker("SPY")
        vencimientos = spy.options
        if not vencimientos:
            print("Aviso: Cadena de opciones no disponible.")
            return {"error": "Sin vencimientos disponibles"}

        # Vencimiento más cercano
        vencimiento_cercano = vencimientos[0]
        cadena = spy.option_chain(vencimiento_cercano)
        calls = cadena.calls
        puts = cadena.puts

        # Volúmenes y cálculo del Put/Call Ratio
        vol_calls = calls['volume'].fillna(0).sum()
        vol_puts = puts['volume'].fillna(0).sum()
        pcr = round(vol_puts / vol_calls, 4) if vol_calls > 0 else None

        # Soporte (Mayor concentración de Open Interest en Puts)
        idx_max_put_oi = puts['openInterest'].idxmax()
        soporte_put = float(puts.loc[idx_max_put_oi, 'strike'])

        # Resistencia (Mayor concentración de Open Interest en Calls)
        idx_max_call_oi = calls['openInterest'].idxmax()
        resistencia_call = float(calls.loc[idx_max_call_oi, 'strike'])

        return {
            "Vencimiento_Evaluado": vencimiento_cercano,
            "Put_Call_Ratio_Volumen": pcr,
            "Soporte_Max_Put_OI": soporte_put,
            "Resistencia_Max_Call_OI": resistencia_call
        }
    except Exception as e:
        print(f"Error procesando opciones: {e}")
        return {
            "Vencimiento_Evaluado": None,
            "Put_Call_Ratio_Volumen": None,
            "Soporte_Max_Put_OI": None,
            "Resistencia_Max_Call_OI": None
        }

def obtener_datos_fred():
    print("Consultando series macroeconomicas de la FRED...")
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        raise ValueError("No se encontro la variable de entorno FRED_API_KEY.")
        
    fred = Fred(api_key=api_key)
    
    walcl = fred.get_series('WALCL').dropna().iloc[-1]
    tga = fred.get_series('WTREGEN').dropna().iloc[-1]
    rrp = fred.get_series('RRPONTSYD').dropna().iloc[-1]
    fedfunds = fred.get_series('FEDFUNDS').dropna().iloc[-1]
    
    # Formula: Liquidez Neta = Balance FED - (TGA + Repo Inverso)
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
        mercado = obtener_datos_mercado_y_ratios()
        opciones = obtener_niveles_opciones_spy()
        macro = obtener_datos_fred()
        
        resultado_consolidado = {
            "mercado": mercado,
            "opciones_spy": opciones,
            "macro_fred": macro
        }
        
        # Persistencia en archivo JSON para consumo del frontend/pipeline
        with open("datos_hoy.json", "w", encoding="utf-8") as f:
            json.dump(resultado_consolidado, f, indent=2, ensure_ascii=False)
            
        print("\n--- MATRIZ CUANTITATIVA COMPLETA Y EXPORTADA A 'datos_hoy.json' ---")
        print(json.dumps(resultado_consolidado, indent=2))
        return resultado_consolidado
        
    except Exception as e:
        print(f"Fallo en la ejecucion: {e}")
        raise e

if __name__ == "__main__":
    main()
