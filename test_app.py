# tests/test_app.py
from app import fetch_example

def test_fetch_example(monkeypatch):
    class DummyResp:
        status_code = 200
        headers = {"content-type": "text/html"}
    def fake_get(url):
        return DummyResp()
    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    status, ctype = fetch_example()
    assert status == 200
    assert "text" in ctype
