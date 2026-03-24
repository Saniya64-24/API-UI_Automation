
from src.clients.base_client import post

def login(payload):
    return post("/login", data=payload)


