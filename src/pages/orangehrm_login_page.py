from conftest import page
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.locator("div.oxd-form-actions.orangehrm-login-action")

    def enter_username(self, username: str):
        self.username_input.fill(username)

    def enter_password(self, password: str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()
        self.page.wait_for_url("**/dashboard/index")
        
    def login(self, username: str, password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        