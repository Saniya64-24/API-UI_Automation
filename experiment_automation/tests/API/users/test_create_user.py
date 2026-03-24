from src.clients import base_client
import pytest

USERS_ENDPOINT = "/users"

# need  tp change mail every time we run because we cannot enter dublicate email data 
@pytest.mark.smoke
def test_create_user(admin_token):
    payload = {
        "name": "test_user",
        "email": "uniquemail4@example.com",
        "password": "Passworrd123!",
        "role": "user",
        "age": 25
    }
    response = base_client.post(
    endpoint=USERS_ENDPOINT,
    token=admin_token,
    data=payload
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 409 #conflict 
    # assert response.json()["name"] == "Test User"
