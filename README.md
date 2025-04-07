# 🌐 IoT Dashboard

Este es un panel de control para monitorear dispositivos IoT (sensores), mostrando datos en tiempo real como temperatura y humedad. Los sensores envían datos al servidor utilizando WebSockets, y el dashboard muestra la información de forma dinámica.

## 📦 Dependencias

Este proyecto utiliza **Python** y **FastAPI** para el backend, y **HTML**, **CSS** y **JavaScript** para el frontend. A continuación, se listan las dependencias necesarias:

### Backend (Servidor)
1. **FastAPI**: Para crear una API rápida y eficiente.
2. **Websockets**: Para establecer una comunicación en tiempo real con los sensores IoT.
3. **Uvicorn**: Para ejecutar el servidor ASGI (FastAPI).

Para instalar las dependencias del backend, puedes usar:

```bash
pip install fastapi uvicorn websockets
