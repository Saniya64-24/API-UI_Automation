import pytest
from src.clients import base_client
from src.config.config import LOGIN_ENDPOINT


# @pytest.mark.parametrize(
#     "email,password,expected_status,expected_message",
#     [
#         ("admin@example.com", "wrongpass", 200, "Login successful"),
#         ("wrong@example.com", "admin123", 404, None),
#         ("", "admin123", 400, None),
#         ("admin@example.com", "", 200, "Login successful"),
#     ]
# )
# def test_invalid_login(email, password, expected_status, expected_message):

#     payload = {
#         "email": email,
#         "password": password
#     }

#     response = base_client.post(
#         endpoint=LOGIN_ENDPOINT, 
#         data=payload
#     )
    
#     assert response.status_code == expected_status

#     if expected_message:
#         assert response.json()["message"] == expected_message


@pytest.mark.parametrize(
    "email,password,expected_status",
    [
        ("admin@example.com", "wrongpass", 401),
        ("wrong@example.com", "admin123", 401),
        ("", "admin123", 400),
        ("admin@example.com", "", 400),
    ]
)

def test_invalid_login(email, password, expected_status):

    payload = {
        "email": email,
        "password": password
    }

    response = base_client.post(
        endpoint=LOGIN_ENDPOINT,
        data=payload
    )

    assert response.status_code == expected_status