# app.py
import requests

def fetch_example():
    r = requests.get("https://example.com")
    return r.status_code, r.headers.get("content-type")

if __name__ == "__main__":
    status, ctype = fetch_example()
    print("status:", status, "content-type:", ctype)
