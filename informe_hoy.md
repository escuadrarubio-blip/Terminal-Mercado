# INFORME ESTRATÉGICO SEMANAL: FONTANERÍA MACRO Y MICROESTRUCTURA DE MERCADO

**Fecha de Ejecución:** 2026-11-22  
**Destinatario:** Mesa Institucional de Trading y Asignación de Capital  
**Preparado por:** Dirección de Estrategia Macro y Microestructura Financiera  

---

## 1. Titular Operativo y Diagnóstico de 1 Frase

> **TITULAR:** *Falla Mecánica de Soporte y Agotamiento del Colchón de Fondeo: Ruptura del Muro de Puts abre Vórtice de Gamma Corta.*  
> **DIAGNÓSTICO:** Con el VIX en 35.89 y el SPY (689.81) habiendo perforado a la baja el mayor soporte de interés abierto de Puts (695.0), el mercado entra en un régimen de desapalancamiento forzado por cobertura dinámica en un contexto donde el colchón de liquidez del Repo Inverso se encuentra formalmente agotado ($0.401M).

---

## 2. Estado de la Liquidez y Macro (FED, Balance, Tipos)

Para entender por qué el mercado pierde tracción, debemos mirar los engranajes de la fontanería monetaria (*Filtro 1: Régimen de Liquidez Base*):

$$\text{Liquidez Neta FED} = \text{Balance FED} - \text{TGA} - \text{ON RRP} = 6.741 - 0.916 - 0.000 = \$5.825 \text{ Billones (USD)}$$

```
+-------------------------------------------------------------------------+
|                  DESGLOSE DEL BALANCE DE LA FED ($6.741T)               |
|                                                                         |
|  [ Reservas Bancarias Netas Efectivas ] ~ $5.825T                       |
|  [ Cuenta General del Tesoro (TGA)   ] = $916,613 M (Drenaje Activo)   |
|  [ Facilidad Repo Inverso (ON RRP)   ] = $0.401 M   (Buffer Extinto)    |
+-------------------------------------------------------------------------+
```

### Mecánica de Transmisión:
1. **Extinción del Colchón del ON RRP ($0.401M):** La facilidad de Repo Inverso Nocturno está prácticamente a **cero**. Esto reviste una gravedad de primer orden: durante trimestres pasados, las emisiones de deuda del Tesoro estadounidense eran absorbidas por los fondos del mercado monetario (MMF) drenando el ON RRP sin tocar las reservas bancarias. Hoy ese amortiguador ha desaparecido.
2. **Impacto de la TGA ($916,613M):** El saldo de la cuenta corriente del Tesoro en la Fed supera los $916.000 millones. Cada dólar estacionado en la TGA representa liquidez retirada de la circulación interbancaria. Con el ON RRP en niveles residuales, cualquier subasta de deuda del Tesoro extrae reservas de forma directa y pura de los bancos comerciales.
3. **Coste del Dinero (Fed Funds a 3.88%):** Con un tipo de intervención en el 3.88% y reservas drenadas, los balances mayoristas de los *primary dealers* se vuelven restrictivos. La capacidad para financiar inventarios y sostener posiciones apalancadas en el mercado repo se contrae, elevando la fragilidad microestructural del sistema.

---

## 3. Amplitud y Régimen de Mercado (SPY vs RSP, VIX, Cobre/Oro)

La dispersión de los datos intermercado revela una contracción sincronizada del apetito por riesgo y una microestructura sumamente vulnerable:

```
+-----------------------------------------------------------------------+
|                       MATRIZ DE TENSIÓN DE MERCADO                    |
+------------------------------+---------+------------------------------+
| Indicador                    | Valor   | Interpretación de Régimen    |
+------------------------------+---------+------------------------------+
| VIX Index                    | 35.89   | Estrés Severo / Pánico       |
| Ratio SPY / RSP              | 3.3253  | Concentración Extrema        |
| Ratio High Yield (HYG/IEI)   | 0.6626  | Tensión en Crédito Corp.     |
| Ratio Cobre / Oro (COPX/GLD) | 0.1745  | Deflación / Contracción      |
+------------------------------+---------+------------------------------+
```

* **VIX en 35.89 (Zona de Disrupción y Ruptura de VaR):** Por encima del umbral de 30-35, los modelos cuantitativos de *Value-at-Risk* (VaR) intradía de los fondos de paridad de riesgo (*Risk Parity*) y CTAs fuerzan la reducción de exposición bruta. No hay análisis fundamental aquí; son órdenes de venta algorítmicas ejecutadas a mercado (*sweep-to-fill*).
* **Ratio SPY/RSP en 3.3253 (Amplitud Anémica):** La divergencia entre el índice ponderado por capitalización (SPY: 689.81) y el equiponderado (RSP: 207.44) confirma que el mercado depende exclusivamente de un grupo microscópico de megacaps. Cuando el promedio de las empresas (RSP) claudica, la estructura se desploma por falta de profundidad en la subasta amplia.
* **Confirmación Intermercado (HYG/IEI en 0.6626 y COPX/GLD en 0.1745):** 
  * El deterioro en el ratio de crédito corporativo de alto rendimiento frente a bonos del Tesoro de corta duración (0.6626) evidencia ensanchamiento de diferenciales de crédito (*spread widening*). El capital mayorista exige una prima superior para financiar deuda privada.
  * La debilidad del ratio Cobre/Oro (0.1745) certifica la huida hacia el refugio monetario (Oro) frente a la demanda de materias primas vinculadas a la actividad industrial cíclica (Cobre).

---

## 4. Mapeo de Posicionamiento de Opciones (Zonas de Dolor, Muros de Puts y Calls)

El análisis del libro de derivados para el vencimiento del **2026-11-23** arroja la clave operativa de la sesión:

```
[Zona de Resistencia] Call Wall: 720.0
        ^
        |
=== PRECIO SUBYACENTE ACTUAL: SPY 689.81 ===
        |  (ZONA DE GAMMA CORTA - ACELERADOR BAJISTA)
        v
[Muro Perforado]     Put Wall:  695.0  (Soporte Vulnerado)
```

* **Ruptura Mecánica del Muro de Puts (Put Wall en 695.0 vs SPY 689.81):**
  * El mayor bloque de interés abierto de opciones *Put* se ubica en el strike **695.0**. El subyacente cotiza actualmente en **689.81**.
  * **La Física de la Cobertura Dinámica:** Al cotizar por debajo del nivel de máximo *Open Interest* de Puts, los creadores de mercado (*dealers*) han pasado a estar formalmente en **Gamma Corta (*Short Gamma*)**. En este régimen, para mantener la neutralidad de delta frente a caídas adicionales del subyacente, los algoritmos de los creadores de mercado están obligados a vender contratos de futuros o acciones del SPY a medida que el precio desciende.
  * Lejos de actuar como suelo elástico, el soporte roto se convierte en un acelerador procíclico de caídas mecánicas.
* **Put/Call Ratio de Volumen (1.0482):** Muestra una demanda agresiva de protección bajista inmediata, saturando la capacidad de inventario de las mesas de derivados.
* **Resistencia Teórica en Calls (720.0):** El *Call Wall* se encuentra a más de 30 puntos por encima del precio actual. En el entorno actual de convexidad distorsionada, este nivel queda totalmente desconectado como referencia operativa inmediata.

---

## 5. Conclusión y Escenario Más Probable para la Sesión / Semana

### Diagnóstico de Balance y Flujo:
El sistema se encuentra atrapado entre dos fuerzas contractivas:
1. **A nivel macro:** Reservas bancarias bajo asedio continuo por una TGA abultada sin el amortiguador del ON RRP.
2. **A nivel microestructural:** Transmisión mecánica bajista activada al cruzar el umbral crítico de Gamma en 695.0, agravada por liquidaciones obligadas por volatilidad (VIX > 35).

### Escenarios Operativos Proyectados:

```
                     [ Escenarios Operativos Semanales ]
                                      |
         +----------------------------+----------------------------+
         |                                                         |
[Escenario A: Base (65%)]                                 [Escenario B: Alternativo (35%)]
Continuación de Liquidación Mecánica                      Rebote Técnico de Corto Plazo (Short Squeeze)
- Resistencia en 695.0 (Pullback rechazado)               - Cierre intradiario sobre 695.0
- Target de búsqueda de liquidez: 680 - 675               - Contracción rápida del VIX < 30
- Forzado por ventas sistemáticas                         - Reabsorción de coberturas hacia 705
```

* **Escenario Principal / Más Probable (Probabilidad: 65% - Continuación de Liquidación Mecánica):**  
  Cualquier intento de rebote intradía hacia la zona de **695.0** (antiguo soporte mayor, ahora resistencia estructural y punto de inflexión de delta) será utilizado por los operadores institucionales para descargar inventario y por los creadores de mercado para rehedgear posiciones cortas. El mercado buscará vacíos de liquidez (*LVN - Low Volume Nodes*) hacia niveles inferiores (rango 680.0 - 675.0) hasta que el VIX frene su aceleración y se restablezca la profundidad pasiva del libro de órdenes.

* **Escenario Alternativo / Invalidation Trigger (Probabilidad: 35% - Cierre Técnico de Cortos / Short Squeeze):**  
  Requiere una reversión inmediata de la volatilidad mediante una caída violenta del VIX por debajo de 30 puntos y la recuperación contundente del strike **695.0** con volumen de iniciativa compradora. Dicha pauta forzaría el desmontaje (*unwind*) de coberturas de delta, habilitando una rotación correctiva hacia los 705.0.

**Pauta de Gestión Táctica:** Prohibido perseguir rebotes en ausencia de absorción pasiva confirmada; el sesgo directivo institucional permanece en **Defensivo / Aversión al Riesgo Extrema** mientras el subyacente permanezca atrapado bajo el Muro de Puts de 695.0.

---

## 6. Bloque JSON de Salida Estructurada para el Sistema de Trading

```json
{
  "timestamp": "2026-11-22T00:00:00Z",
  "horizonte": "Semanal",
  "diagnostico_macro": {
    "liquidez_neta_billones": 5.825,
    "fed_balance_millones": 6741452.0,
    "tga_millones": 916613.0,
    "on_rrp_millones": 0.401,
    "tasa_fedfunds": 3.88,
    "estado_fondeo": "Tension Severa / Buffer de ON RRP Agotado"
  },
  "microestructura_y_regimen": {
    "regimen_volatilidad": "Panico / Short Gamma Dominante",
    "vix_nivel": 35.89,
    "amplitud_mercado": "Anemica / Divergencia Estructural Bajista",
    "ratio_spy_rsp": 3.3253,
    "ratio_credito_hyg_iei": 0.6626,
    "ratio_cobre_oro_copx_gld": 0.1745
  },
  "mapa_derivados": {
    "vencimiento_clave": "2026-11-23",
    "put_call_volume_ratio": 1.0482,
    "put_wall_soporte_critico": 695.0,
    "call_wall_resistencia": 720.0,
    "posicion_relativa_precio_wall": "Subyacente Bajo Muro de Puts (Infraccion de Convexidad)",
    "gamma_regime": "Short Gamma (Acelerador Prociclico)"
  },
  "niveles_operativos_spy": {
    "precio_actual": 689.81,
    "resistencia_inmediata": 695.0,
    "resistencia_secundaria": 705.0,
    "soporte_teorico_proyectado": 680.0,
    "soporte_secundario": 675.0
  },
  "estrategia_sugerida": {
    "sesgo_direccional": "Bajista / Defensivo",
    "escenario_base_probabilidad": 0.65,
    "gatillo_invalidacion": "Recuperacion de 695.0 con VIX < 30.0",
    "accion_recomendada": "Venta en pullbacks hacia 695.0; reduccion estricta de apalancamiento bruto"
  }
}
```