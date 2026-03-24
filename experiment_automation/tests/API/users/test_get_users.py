# from src.cl.user_client import get_all_users
from src.clients.user_cleint import get_all_users

# def test_get_all_users(admin_token):

#     response = get_all_users(admin_token)


#     assert response.status_code == 200

# def test_get_all_users(admin_token):

#     response = get_all_users(admin_token)

#     assert response.status_code == 200
#     assert isinstance(response.json(), list)

def test_get_all_users(admin_token):

    response = get_all_users(admin_token)

    assert response.status_code == 200
    assert "data" in response.json()
    assert "users" in response.json()["data"]