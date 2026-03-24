from src.clients import base_client
USERS_ENDPOINT="/users"

def test_get_users_without_token():

    response = base_client.get(
        endpoint=USERS_ENDPOINT
    )

    assert response.status_code == 401

def test_get_users_with_invalid_token():

    response = base_client.get(
        endpoint=USERS_ENDPOINT,
        token="invalid_token_123"
    )

    assert response.status_code == 401


