import pytest
from src.clients.user_cleint import create_users


@pytest.mark.parametrize(
    "name,email,password,role,age",
    [
        ("Alice", "alice12@example.com", "Password123!", "user", 22),
        ("Bob", "bob1@example.com", "Password123!", "user", 25),
        ("Charlie", "charlie1@example.com", "Password123!", "admin", 30),
    ]
)
def test_create_multiple_users(admin_token, name, email, password, role, age):

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "role": role,
        "age": age
    }

    response = create_users(payload, admin_token)

    assert response.status_code == 201 # (409)conflict becuse already created .if not replace it with 201

    response_data = response.json()["data"]

    assert response_data["name"] == name
    assert response_data["email"] == email
    assert response_data["role"] == role
    assert response_data["age"] == age

    