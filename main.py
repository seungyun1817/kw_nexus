from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
_state = {}

@app.get("/api/health")
def health():
    return {"ok": True}

@app.post("/api/state")
def put_state(payload: dict):
    _state.update(payload)
    return {"ok": True}

@app.get("/api/state")
def get_state():
    return _state

app.mount("/", StaticFiles(directory="static", html=True), name="static")
