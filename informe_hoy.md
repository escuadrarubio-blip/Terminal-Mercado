# INFORME MATUTINO DE INTELIGENCIA DE MERCADO (SESIÓN DIARIA)
**Fecha:** 24 de noviembre de 2026  
**Autor:** Director de Estrategia Macro & Analista Senior de Microestructura

---

### 1. Titular Operativo y Diagnóstico de 1 Frase
**Titular:** Fontanería en Tensión Extrema: Drenaje Total de Colateral Pasivo y Régimen de Gamma Defensiva  
**Diagnóstico:** El agotamiento absoluto del Repo Inverso ($0.301M) traslada íntegramente el drenaje fiscal de la TGA ($916.6B) a las reservas bancarias, induciendo un régimen de volatilidad reactiva (VIX 26.36) donde la concentración artificial del índice disfraza un mercado en repliegue crediticio y macroeconómico.

---

### 2. Estado de la Liquidez y Macro (FED, Balance, Tipos)
Para entender la acción del precio de hoy, debemos mirar las tuberías del sistema financiero:
* **Tasa FEDFUNDS:** 3.88%
* **Balance de la Reserva Federal:** $6,741,452 M ($6.74 Billones / Trillions)
* **Cuenta General del Tesoro (TGA):** $916,613 M ($916.6B)
* **Facilidad de Repo Inverso Nocturno (ON RRP):** $0.301 M (~$300,000 USD, nivel residual nulo)
* **Liquidez Neta Calculada:** **$5.825 Billones USD** ($\text{Balance} - \text{TGA} - \text{ON RRP}$)

**Mecanismo de transmisión institucional:**  
Tal como dictamina el marco de balances mayoristas, mientras el saldo de la ventanilla ON RRP se mantenía inflado, absorbía las emisiones del Tesoro actuando como un colchón amortiguador sin restar un solo dólar del sistema bancario comercial. Hoy ese amortiguador **se ha extinguido por completo** ($0.301M). 

Con una TGA drenando la colosal cifra de **$916,613 M**, cada nueva necesidad de financiamiento del gobierno estadounidense o liquidación de impuestos se ejecuta restando directamente liquidez de las reservas de los bancos comerciales. La liquidez neta del sistema ha descendido a **$5.825 Billones**, racionando la capacidad de balance de los intermediarios primarios (*dealers*). Hay menos combustible en la fontanería interbancaria para financiar inventarios y sostener el apalancamiento colateralizado en el mercado monetario repo.

---

### 3. Amplitud y Régimen de Mercado (SPY vs RSP, VIX, Cobre/Oro)
La lectura cruzada de activos confirma una fractura estructural profunda:

* **Concentración del Mercado (SPY 718.78 vs. RSP 213.96 | Ratio 3.3594):**  
  El diferencial entre el índice ponderado por capitalización (SPY) y el equiponderado (RSP) se encuentra en niveles de asimetría crítica. El mercado en general está descolgado; un puñado mínimo de megacapitalizaciones sostiene la fachada del SPY, mientras que la subasta agregada (RSP) languidece.
* **Régimen de Volatilidad (VIX en 26.36):**  
  Hemos roto holgadamente el umbral de contención pasiva (20.0). Cotizar en 26.36 sitúa a los creadores de mercado en una postura defensiva inmediata. La superficie de volatilidad denota demanda inelástica de protección y ensanchamiento de horquillas (*spreads bid-ask*).
* **Pulso Macroeconómico Cobre/Oro (COPX/GLD en 0.1769):**  
  El dinero institucional prefiere el oro (reserva de valor sin riesgo de contrapartida) frente al cobre industrial (reflejo de la actividad fabril). El ciclo global está desacelerando.
* **Apetito por Riesgo Crediticio (HYG/IEI en 0.6637):**  
  La compresión del ratio entre crédito corporativo de alto rendimiento y bonos del Tesoro de corta duración refleja aversión al riesgo en los libros de crédito corporativo, confirmando la transmisión del encarecimiento del fondeo hacia los balances de las empresas.

---

### 4. Mapeo de Posicionamiento de Opciones (Zonas de Dolor, Muros de Puts y Calls)
En la estructura de derivados del SPY (con vencimiento evaluado para la sesión presente 2026-11-24):

* **Precio Actual SPY:** 718.78
* **Put/Call Ratio por Volumen:** **1.2437**
* **Resistencia Estructural (Call Wall / Max Call OI):** **740.0**
* **Soporte Estructural (Put Wall / Max Put OI):** **620.0**

**Dinámica Microestructural:**  
1. **Flujo Agresivo Defensivo:** Un Put/Call ratio de volumen de 1.2437 demuestra que los operadores institucionales e intradiarios están adquiriendo primas de puts agresivamente. 
2. **Impacto en los Dealers:** Con el VIX en 26.36 y un flujo comprador de Puts, las mesas de negociación (*dealers*) se encuentran en régimen de **Gamma Corta** o en la antesala de cobertura acelerada. Cada caída en el subyacente obliga a los algoritmos de cobertura delta a vender futuros a mercado para mantener su delta neutral, transformando el libro de órdenes en un mecanismo procíclico.
3. **Límites de la Subasta:** El nivel 740.0 actúa como un techo inexpugnable para la sesión (los creadores de mercado desarmarán coberturas si el precio se acerca, amortiguando subidas). Hacia abajo, el abismo de volumen se abre con un soporte masivo en 620.0, dejando un vacío de liquidez intermedia donde los deslizamientos (*slippage*) pueden ser severos si se perforan mínimos locales.

---

### 5. Conclusión y Escenario Más Probable para la Sesión / Semana
* **Diagnóstico Táctico:** Régimen de alta vulnerabilidad. El mercado carece de soporte pasivo institucional debido al colapso de las reservas excedentes y a una TGA absorbente.
* **Escenario Más Probable (Sesión Intradiaria):** Sesgo correctivo y de contención nerviosa. Mientras el SPY cotice por debajo de los 725-730, los rebotes serán vendidos por coberturas automáticas. Cualquier rotura intradiaria a la baja se verá amplificada por liquidaciones mecánicas y coberturas dinámicas derivadas del flujo 0DTE (Put/Call 1.2437).
* **Guía Operativa:** Prudencia extrema en posiciones largas. Reducción obligatoria del tamaño de posición por incremento del VaR intradía (VIX > 26). La toma de posiciones alcistas carece de respaldo en la liquidez neta estructural.

---

### 6. Bloque JSON de Salida Estructurada

```json
{
  "fecha_informe": "2026-11-24",
  "diagnostico_macro": {
    "regimen_liquidez": "Tensión de Fondeo",
    "liquidez_neta_billones": 5.825,
    "on_rrp_estado": "Agotado",
    "presion_tga": "Drenaje Severo",
    "tasa_fedfunds": 3.88
  },
  "microestructura_y_volatilidad": {
    "vix": 26.36,
    "regimen_vix": "Alta Volatilidad / Estrés",
    "regimen_gamma_estimado": "Gamma Corta / Transición Defensiva",
    "put_call_ratio_volumen": 1.2437,
    "muro_call_resistencia": 740.0,
    "muro_put_soporte": 620.0
  },
  "amplitud_mercado": {
    "spy_spot": 718.78,
    "rsp_spot": 213.96,
    "ratio_spy_rsp": 3.3594,
    "evaluacion_amplitud": "Desconexión Crítica / Concentración en Megacaps",
    "ratio_hyg_iei": 0.6637,
    "ratio_copx_gld": 0.1769,
    "sesgo_ciclo_economico": "Aversión al Riesgo / Contracción"
  },
  "directriz_estrategica": {
    "sesgo_direccional": "Bajista / Defensivo",
    "probabilidad_ruptura_alcista": "Baja",
    "riesgo_impacto_mecanico": "Elevado",
    "accion_sugerida": "Reducir apalancamiento, favorecer coberturas delta-neutrales o táctica vendedora en resistencias (Call Wall)."
  }
}
```