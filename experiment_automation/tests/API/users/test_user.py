import pytest
import uuid
from src.clients.user_cleint import create_users


@pytest.mark.parametrize(
    "name,password,role,age",
    [
        ("Alice123", "Password123!", "user", 22),
        ("Bob123", "Password123!", "user", 25),
        ("Charlie123", "Password123!", "admin", 30),
    ]
)
def test_create_multiple_users(admin_token, name, password, role, age):

    # Generate random email
    random_email = f"{name.lower()}_{uuid.uuid4().hex[:6]}@example.com"

    payload = {
        "name": name,
        "email": random_email,
        "password": password,
        "role": role,
        "age": age
    }

    response = create_users(payload, admin_token)

    assert response.status_code == 201

    response_data = response.json()["data"]

    assert response_data["name"] == name
    assert response_data["email"] == random_email
    assert response_data["role"] == role
    assert response_data["age"] == age