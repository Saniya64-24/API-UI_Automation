# This file will have responsibility of:
# Central place for GET, POST, PUT
# No business logic

# Central API client for GET, POST, PUT, DELETE

import requests
from src.config import config


def build_headers(token=None):
    headers = {
        "Content-Type": "application/json"
    }

    if token:
        headers["Authorization"] = f"Bearer {token}"

    return headers


def get(endpoint, token=None):
    url = f"{config.BASE_URL}{endpoint}"

    return requests.get(
        url=url,
        headers=build_headers(token),
        timeout=5
    )


def post(endpoint, data=None, token=None):
    url = f"{config.BASE_URL}{endpoint}"

    return requests.post(
        url=url,
        json=data,
        headers=build_headers(token),
        timeout=5
    )


def put(endpoint, data=None, token=None):
    url = f"{config.BASE_URL}{endpoint}"

    return requests.put(
        url=url,
        json=data,
        headers=build_headers(token),
        timeout=5
    )


def delete(endpoint, token=None):
    url = f"{config.BASE_URL}{endpoint}"

    return requests.delete(
        url=url,
        headers=build_headers(token),
        timeout=5
    )