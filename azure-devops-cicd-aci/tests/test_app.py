import json
from app import app

def test_healthz():
    client = app.test_client()
    res = client.get("/healthz")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_root():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert "message" in data

def test_echo():
    client = app.test_client()
    res = client.post("/api/v1/echo", json={"a": 1, "b": 2})
    assert res.status_code == 200
    data = res.get_json()
    assert data["count"] == 2
