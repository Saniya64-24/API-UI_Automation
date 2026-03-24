import pytest
from src.clients.auth_client import login


# @pytest.fixture(scope="session")
def get_admin_token():

    payload = {
        "email": "admin@example.com",
        "password": "Admin@123"
    }

    # print(response.json())   
    response = login(payload)
    
    # token = response.json()["token"]
    # token = response.json()["access_token"]
    token = response.json()["data"]["token"]

    return token