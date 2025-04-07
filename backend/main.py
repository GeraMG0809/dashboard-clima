# backend.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# CORS para frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients = []
last_heartbeat = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            timestamp = time.time()
            for client in clients:
                if client != websocket:
                    await client.send_text(data)

            # Guardar última señal del sensor
            data_json = eval(data)
            last_heartbeat[data_json["id"]] = timestamp
    except WebSocketDisconnect:
        clients.remove(websocket)

# Ruta para ver sensores vivos
@app.get("/sensors/alive")
def get_alive():
    now = time.time()
    alive = []
    for sensor_id, t in last_heartbeat.items():
        if now - t < 5:  # Si envió datos hace menos de 5 segundos
            alive.append(sensor_id)
    return {"active_sensors": alive}
