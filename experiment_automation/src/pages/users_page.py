from src.pages.base_page import BasePage
from src.config.UI.settings import BASE_URL

class UsersPage(BasePage):

    def open_users_page(self):

        self.driver.get(BASE_URL)

    def verify_users_page(self):

        # demo validation
        return "vercel" in self.driver.current_url