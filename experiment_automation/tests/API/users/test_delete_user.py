import pytest
import random
from src.clients import base_client

USERS_ENDPOINT = "/users"

@pytest.mark.smoke
def test_delete_user(admin_token):

    unique_email = f"deleteuser{random.randint(1000,9999)}@example.com"

    payload = {
        "name": "delete_user",
        "email": unique_email,
        "password": "Password123!",
        "role": "user",
        "age": 22
    }

    create_response = base_client.post(
        endpoint=USERS_ENDPOINT,
        token=admin_token,
        data=payload
    )

    assert create_response.status_code == 201

    print("CREATE BODY:", create_response.json())
    user_id = create_response.json()["data"]["id"]

    delete_response = base_client.delete(
        endpoint=f"/users/{user_id}",
        token=admin_token
    )
    

    assert delete_response.status_code == 200