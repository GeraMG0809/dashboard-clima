import time
import json
import random
import asyncio
import websockets
import sys
import threading

# bandera para detener el sensor
stop_flag = False

def input_listener():
    global stop_flag
    while True:
        cmd = input().strip().lower()
        if cmd == "apagar":
            print("Desconectando sensor...")
            stop_flag = True
            break

async def sensor(sensor_id):
    uri = "ws://localhost:8000/ws"

    while not stop_flag:
        try:
            async with websockets.connect(uri) as websocket:
                print(f"✅ Sensor {sensor_id} conectado al servidor.")

                while not stop_flag:
                    data = {
                        "id": sensor_id,
                        "temperatura": round(random.uniform(20, 35), 2),
                        "humedad": round(random.uniform(30, 70), 2),
                        "timestamp": time.time()
                    }
                    await websocket.send(json.dumps(data))
                    await asyncio.sleep(2)

        except (ConnectionRefusedError, OSError, websockets.exceptions.InvalidURI) as e:
            print("🚫 Servidor no disponible. Reintentando en 5 segundos...")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"⚠️ Error inesperado: {e}. Reintentando...")
            await asyncio.sleep(5)

    print(f"🛑 Sensor {sensor_id} se ha desconectado.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Uso: python sensor.py <sensor_id>")
        sys.exit(1)

    sensor_id = sys.argv[1]

    # Iniciar listener del teclado en otro hilo
    threading.Thread(target=input_listener, daemon=True).start()

    asyncio.run(sensor(sensor_id))
