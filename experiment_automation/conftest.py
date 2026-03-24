import pytest
from src.fixtures.auth_fixtures import get_admin_token
from src.utils.driver_factory import create_driver
from src.config.UI.settings import BASE_URL

# @pytest.fixture
# def admin_token():
#     return get_admin_token()


@pytest.fixture
def driver():

    driver = create_driver()

    driver.get(BASE_URL)

    yield driver

    driver.quit()

@pytest.fixture(scope="session")
def admin_token():
    return get_admin_token()