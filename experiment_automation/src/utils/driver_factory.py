from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.config.UI.settings import GRID_URL


def create_driver():

    options = Options()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.maximize_window()

    return driver