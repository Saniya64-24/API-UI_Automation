from src.clients.base_client import post, put, get, delete

# def get_all_users():
#     return get("/users")
import requests
# from src.config.token import TOKEN
from src.config.config import BASE_URL



def get_all_users(token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(
        f"{BASE_URL}/users",
        headers=headers
    )

    return response

USERS_ENDPOINT="/users"
# def get_user_by_id(user_id):
#     return get(f"/users/{user_id}")

def get_user_by_id(user_id, token):
    return get(
        endpoint=f"{USERS_ENDPOINT}/{user_id}",
        token=token
    )

def create_users(payload, token):
    return post("/users", data=payload, token=token)

def update_user(user_id, payload, token):
    return put(f"/users/{user_id}", data=payload, token=token)

def delete_user(user_id, token):
    return delete(f"/users/{user_id}", token=token)