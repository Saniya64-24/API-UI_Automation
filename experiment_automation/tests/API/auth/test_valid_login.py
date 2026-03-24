import pytest
# from .auth_client import login
from src.clients.auth_client import login

@pytest.mark.smoke
def test_valid_login():

    payload = {
        "email": "admin@example.com",
        "password": "Admin@123"
    }

    response = login(payload)

    data = response.json()

    assert response.status_code == 200
    assert data["status"] == "success"
    assert data["data"]["user"]["role"] == "admin"
    assert "token" in data["data"]