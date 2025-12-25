import yfinance as yf
import pandas as pd
import time
import os

# --- CONFIGURACIÓN ---
SIMBOLO = "BTC-USD"
TEMPORALIDAD = "1m"   
VENTANA_EMA = 7       
# ---------------------

# Variable global para rastrear el estado
estado_actual = None # Puede ser 'ARRIBA' o 'DEBAJO'

def enviar_notificacion_mac(titulo, mensaje):
    """Comando directo al sistema macOS"""
    os.system(f'osascript -e "display notification \\"{mensaje}\\" with title \\"{titulo}\\""')

def ejecutar_estrategia():
    global estado_actual
    
    # 1. DESCARGA DE DATOS (Forzamos 2d para tener histórico siempre)
    try:
        df = yf.download(tickers=SIMBOLO, period="2d", interval=TEMPORALIDAD, progress=False, auto_adjust=True)
    except:
        return

    if df is None or df.empty or len(df) < (VENTANA_EMA + 1):
        return

    # Aplanar columnas por si acaso
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 2. CÁLCULO DE LA EMA 7
    df['EMA_7'] = df['Close'].ewm(span=VENTANA_EMA, adjust=False).mean()
    
    try:
        # Tomamos los últimos valores cerrados (la última posición del DataFrame)
        precio = float(df['Close'].iloc[-1])
        ema = float(df['EMA_7'].iloc[-1])
        
        hora = time.strftime('%H:%M:%S')
        print(f"[{hora}] {SIMBOLO} | Precio: {precio:.2f} | EMA 7: {ema:.2f}")

        # 3. LÓGICA DE CRUCE SIN ERRORES
        # Determinamos dónde está el precio ahora mismo
        nuevo_estado = 'ARRIBA' if precio > ema else 'DEBAJO'

        # Si el estado es distinto al que teníamos guardado, es un CRUCE
        if estado_actual is not None and nuevo_estado != estado_actual:
            if nuevo_estado == 'ARRIBA':
                print(f"--- ¡CRUCE ALCISTA DETECTADO! ---")
                enviar_notificacion_mac(f"ALERTA ALCISTA", f"{SIMBOLO} cruzó arriba de EMA 7")
            else:
                print(f"--- ¡CRUCE BAJISTA DETECTADO! ---")
                enviar_notificacion_mac(f"ALERTA BAJISTA", f"{SIMBOLO} cruzó debajo de EMA 7")

        # Actualizamos el estado para la siguiente vuelta
        estado_actual = nuevo_estado
                
    except Exception as e:
        print(f"Error en datos: {e}")

if __name__ == "__main__":
    print(f"*** INICIANDO MONITOR {SIMBOLO} (EMA 7 / 1m) ***")
    
    while True:
        try:
            ejecutar_estrategia()
            # 20 segundos para no perder el movimiento de la vela de 1m
            time.sleep(20) 
        except KeyboardInterrupt:
            print("\nBot apagado.")
            break
        except Exception as e:
            time.sleep(10)
