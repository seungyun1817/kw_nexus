from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
_state = {}
STATIC_DIR = Path(__file__).resolve().parent / "static"

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

app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
