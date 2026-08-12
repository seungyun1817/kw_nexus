"""WSGI entry point for Azure App Service's automatic Python detection."""

from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import safe_join


STATIC_DIR = Path(__file__).resolve().parent / "static"
app = Flask(__name__, static_folder=None)
_state = {}


@app.get("/api/health")
def health():
    return jsonify(ok=True)


@app.post("/api/state")
def put_state():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(detail="Request body must be a JSON object"), 400
    _state.update(payload)
    return jsonify(ok=True)


@app.get("/api/state")
def get_state():
    return jsonify(_state)


@app.get("/")
@app.get("/<path:path>")
def static_files(path="index.html"):
    safe_path = safe_join(str(STATIC_DIR), path)
    if safe_path and Path(safe_path).is_file():
        return send_from_directory(STATIC_DIR, path)
    return send_from_directory(STATIC_DIR, "index.html")
