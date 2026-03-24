from src.clients.user_cleint import create_users,delete_user,get_all_users,get,get_user_by_id,delete,update_user,post,put
import random

def test_user_e2e_flow(admin_token):
    # Step 1:  Create a new user
    unique_email = f"updateuser{random.randint(10000,99999)}@example.com"
    payload = {
        "name": "Test User122",
        "email": unique_email,
        "password": "Password123!",
        "age": 30,
        "role": "user"
    }
    create_response = create_users(
        payload, admin_token)
    assert create_response.status_code == 201
    assert "data" in create_response.json()
    assert "id" in create_response.json()["data"]
    user_id = create_response.json()["data"]["id"]


    # Step 2: Get the created user by ID
    get_response = get_user_by_id(user_id,admin_token)
    assert get_response.status_code == 200
    assert get_response.json()["data"]["id"] == user_id


    # Step 3: Update the user's information
    update_payload = {
        "name": "Updated Test User123",
        "age": 45
    }

    update_response = update_user(user_id, update_payload, admin_token)
    assert update_response.status_code == 200
    assert update_response.json()["data"]["name"] == "Updated Test User123"
    assert update_response.json()["data"]["age"] == 45

    # Step 4: Delete the user
    delete_response = delete_user(user_id, admin_token)
    assert delete_response.status_code == 200
    