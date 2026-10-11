from playwright.sync_api import Page
from src.pages.orangehrm_login_page import LoginPage


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.heading_message = page.get_by_role("heading", name="Dashboard")
        self.logout_dropdown_button = page.locator("p.oxd-userdropdown-name")
        self.logout_btn = page.get_by_text("Logout")

    def click_logout_dropdown(self):
        self.logout_dropdown_button.click()

    def click_logout_button(self):
        self.logout_btn.click()
        return LoginPage(self.page)
