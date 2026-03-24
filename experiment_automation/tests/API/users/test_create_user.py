from src.clients import base_client
import pytest
import random

USERS_ENDPOINT = "/users"

# need  tp change mail every time we run because we cannot enter dublicate email data 
@pytest.mark.smoke
def test_create_user(admin_token):
    unique_email = f"updateuser{random.randint(1000,9999)}@example.com"

    create_payload = {
        "name": "Original User",
        "email": unique_email,
        "password": "Password123!",
        "role": "user",
        "age": 23
    }

    response = base_client.post(
    endpoint=USERS_ENDPOINT,
    token=admin_token,
    data=create_payload
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    assert response.status_code == 201 #conflict 
    # assert response.json()["name"] == "Test User"
