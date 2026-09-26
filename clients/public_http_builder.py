from httpx import Client

def get_public_httpx_client()-> Client:
    return Client(timeout=100, base_url = "http://192.168.0.10:8000")

