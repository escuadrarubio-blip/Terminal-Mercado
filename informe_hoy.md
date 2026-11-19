# INFORME MATUTINO DE INTELIGENCIA DE MERCADO
**Sesión Diaria — 19 de noviembre de 2026**  
*Mesa de Estrategia Macro y Microestructura de Fondeo Global*

---

### 1. Titular Operativo y Diagnóstico de 1 Frase
**Régimen de Fricción de Balances y Contracción de Colateral:** El colapso del amortiguador del Repo Inverso traslada íntegramente la acumulación fiscal de la TGA al drenaje de reservas, detonando un régimen de aversión al riesgo con volatilidad estructural (`VIX 28.03`) y sesgo netamente defensivo.

---

### 2. Estado de la Liquidez y Macro (FED, Balance, Tipos)
La arquitectura de la fontanería monetaria revela una dislocación crítica:
* **Balance de la Reserva Federal:** $6,758,867M ($6.76B).
* **Cuenta General del Tesoro (TGA):** $914,370M ($914.37B).
* **Facilidad de Reporto Inverso (ON RRP):** Prácticamente vaciada en $0.405M (convergencia a cero técnico).
* **Liquidez Neta Efectiva del Sistema:** **$5.844 Billones de USD** ($\text{Balance} - \text{TGA} - \text{ON RRP}$).

**Interpretación de Fontanería Institucional:**  
Como establece la identidad contable del pasivo del banco central, el colchón pasivo del ON RRP ha quedado completamente extenuado. Mientras dicho saldo se mantuvo con fondos, los fondos del mercado monetario (MMF) absorbían las emisiones de Letras del Tesoro vaciando el ON RRP, protegiendo las reservas bancarias comerciales. Hoy, con el ON RRP en niveles marginales insignificantes, **cada dólar que el Tesoro mantiene en la TGA ($914,370M) drena directamente el nivel de reservas del sistema bancario**. 

Con la tasa de Fondos Federales en 3.88% y la curva operando bajo absorción fiscal forzosa, el sistema se sitúa en el umbral donde la elasticidad de la demanda de reservas comienza a verticalizarse, reduciendo la capacidad de los *primary dealers* para intermediar y expandir balance sin penalizaciones de apalancamiento regulatorio.

---

### 3. Amplitud y Régimen de Mercado (SPY vs RSP, VIX, Cobre/Oro)
* **SPY (715.83) vs. RSP (211.71) — Ratio 3.3812:**  
  La relación ponderada por capitalización frente a la equiponderada confirma una estrechez patológica en el liderazgo de los índices. El mercado se sostiene en una concentración artificial en mega-caps; la masa del mercado (RSP) exhibe un rezago agudo, lo que denota una divergencia bajista clásica donde la liquidez no irriga el tejido corporativo amplio.
* **Índice VIX (28.03):**  
  Por encima del umbral de régimen neutral-calmo (habitualmente sub-18/20), una lectura de 28.03 clasifica al mercado en un **régimen de volatilidad expandida y gamma corta estructural**. Bajo este entorno, los creadores de mercado (*market makers*) se ven obligados a vender en las caídas y recomprar en las subidas para ajustar sus deltas dinámicos, exacerbando el rango intradiario.
* **Ratios Intermercado:**
  * **Cobre/Oro (`COPX/GLD = 0.1769`):** Compresión severa de la demanda cíclica industrial frente al valor de refugio y colateral pristino que representa el oro. El mercado descuenta una desaceleración en la actividad global o enfriamiento manufacturero.
  * **Crédito de Alto Rendimiento (`HYG/IEI = 0.6688`):** Los diferenciales corporativos de riesgo evidencian cautela frente a la deuda soberana a corto plazo; no hay complacencia crediticia.

---

### 4. Mapeo de Posicionamiento de Opciones (SPY)
* **Vencimiento Evaluado:** 2026-11-19 (Sesión en curso).
* **Put/Call Ratio Volumen (1.2094):**  
  Dominancia explícita de volumen de protección en puts institucionales (> 1.20), lo que denota compra de coberturas activas y liquidación forzada de posiciones alcistas.
* **Muro Estructural de Puts (Soporte OI):** **$700.00**.  
  Representa el principal nivel de amortiguación técnica y concentración de interés abierto vendedor/comprador. Si el SPY testea esta zona, la absorción por cobertura gamma puede actuar como suelo transitorio intradía.
* **Muro Estructural de Calls (Resistencia OI):** **$748.00**.  
  Techo delimitado del régimen actual; nivel en el cual la expiración y desintegración del valor extrínseco bloquea extensiones alcistas impulsivas.
* **Dinámica Operativa:**  
  Con el subyacente en **$715.83**, el precio cotiza en la mitad inferior de la estructura de posicionamiento, relativamente próximo a su soporte crítico de $700.00. La prima por volatilidad implícita encarecida castiga a compradores de opciones fuera de dinero y expone a los partícipes a barridos de liquidez hacia los strikes de mayor fricción.

---

### 5. Conclusión y Escenario Más Probable para la Sesión / Semana
* **Escenario Principal (Probabilidad 65%):**  
  **Rebote técnico vulnerable o consolidación errática con sesgo bajista.** El subyacente oscilará entre los $710.00 y los $725.00. Con VIX en 28.03, cualquier amago alcista hacia la media intradía será utilizado por institucionales para descargar riesgo o cerrar patas de coberturas. La proximidad del soporte de puts en $700.00 ejercerá atracción magnética en caso de quiebre de mínimos locales.
* **Escenario Alternativo (Probabilidad 35%):**  
  Si el drenaje de reservas presiona las tasas de fondeo interbancario intradiarias forzando liquidaciones de carteras de riesgo, un quiebre sostenido de los $710.00 desencadenará un barrido de gamma en cascada con destino inmediato en el muro de soporte en **$700.00**.
* **Directriz Táctica:**  
  Prohibido perseguir rebotes sin confirmación de descompresión en el VIX (retroceso bajo 24-25). Mantener exposición neta moderada, favorecer coberturas asimétricas y respetar el nivel pivote defensivo de balance.

---

### 6. Bloque JSON de Salida Estructurada

```json
{
  "fecha": "2026-11-19",
  "regimen_macro": "Restrictivo / Fricción de Reservas",
  "liquidez_neta_usd_billones": 5.844,
  "vix": 28.03,
  "estado_volatilidad": "Alta / Régimen de Gamma Corta",
  "amplitud_mercado": {
    "ratio_spy_rsp": 3.3812,
    "diagnostico": "Divergencia bajista por concentración extrema en mega-caps",
    "ratio_cobre_oro": 0.1769,
    "ratio_hyg_iei": 0.6688
  },
  "posicionamiento_opciones": {
    "spy_spot": 715.83,
    "put_call_ratio": 1.2094,
    "muro_soporte_put": 700.0,
    "muro_resistencia_call": 748.0,
    "sesgo_distribucion": "Defensivo / Demanda de cobertura neta"
  },
  "escenario_sesion": {
    "direccion_predominante": "Rango defensivo / Presión bajista latente",
    "soporte_clave": 700.0,
    "resistencia_inmediata": 725.0,
    "probabilidad_escenario_bajista_neutro": 0.65
  }
}
```