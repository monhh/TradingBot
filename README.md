# TradingBot (BTC-USD / EMA 7)

Este es un bot de trading simple escrito en Python que monitorea el precio de **Bitcoin (BTC)** frente al Dólar (USD) en tiempo real. Utiliza la estrategia de cruce de medias móviles exponenciales (EMA) para detectar y notificar posibles cambios de tendencia.

## 🚀 Funcionalidades

-   **Monitoreo en tiempo real**: Verifica el precio de BTC-USD cada 20 segundos.
-   **Indicador Técnico**: Calcula la **EMA de 7 periodos** en velas de 1 minuto.
-   **Alertas de Cruce**:
    -   **Alerta Alcista**: Cuando el precio cruza por encima de la EMA 7.
    -   **Alerta Bajista**: Cuando el precio cruza por debajo de la EMA 7.
-   **Notificaciones Nativas**: Envía notificaciones de escritorio en macOS (`osascript`).

## 📋 Requisitos

-   Python 3.8+
-   Un entorno macOS (para las notificaciones nativas).

## 🛠️ Instalación

1.  **Clonar el repositorio**:

    ```bash
    git clone https://github.com/monhh/TradingBot.git
    cd TradingBot
    ```

2.  **Crear un entorno virtual** (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install yfinance pandas
    ```

## ▶️ Uso

Ejecuta el script principal:

```bash
python estrategia.py
```

Verás en la consola la salida del precio y la EMA actual. Cuando ocurra un cruce, recibirás una notificación en tu sistema.

## ⚠️ Disclaimer

Este software es para fines educativos y de prueba. El trading de criptomonedas conlleva riesgos significativos. El autor no se hace responsable de pérdidas financieras.
