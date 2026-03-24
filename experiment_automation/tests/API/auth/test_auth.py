from src.clients.base_client import post, put, get, delete
from src.clients.auth_client import login


def test_login_admin_check(admin_token):
    assert admin_token is not None
    
    assert isinstance(admin_token, str)
    assert len(admin_token) > 0