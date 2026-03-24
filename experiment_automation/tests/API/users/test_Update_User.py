import random
import pytest
from src.clients import base_client

USERS_ENDPOINT = "/users"

@pytest.mark.smoke
def test_update_user(admin_token):

    # Step 1: Create user first
    unique_email = f"updateuser{random.randint(1000,9999)}@example.com"

    create_payload = {
        "name": "Original User",
        "email": unique_email,
        "password": "Password123!",
        "role": "user",
        "age": 23
    }

    create_response = base_client.post(
        endpoint=USERS_ENDPOINT,
        token=admin_token,
        data=create_payload
    )

    assert create_response.status_code == 201

    user_id = create_response.json()["data"]["id"]

    # Step 2: Update that user
    update_payload = {
        "name": "Updated User",
        "age": 30
    }

    response = base_client.put(
        endpoint=f"{USERS_ENDPOINT}/{user_id}",
        token=admin_token,
        data=update_payload
    )

    assert response.status_code == 200
    assert response.json()["status"] == "success"