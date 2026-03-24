from src.clients import base_client

USERS_ENDPOINT = "/users"

def test_get_users_with_valid_token(admin_token):
    response = base_client.get(
        endpoint=USERS_ENDPOINT,
        token=admin_token
    )

    assert response.status_code == 200
    # assert response.json()["role"] == "admin"
    # assert isinstance(response.json(), list)