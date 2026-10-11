from playwright.sync_api import Page, expect
import pytest
from config import Config
from reporting_labs import meta, log, test_data, step
from src.pages.orangehrm_login_page import LoginPage
from src.pages.orangehrm_home_page import HomePage


@pytest.mark.meta(
    priority="P2",
    owner="Durgesh Yaduvanshi",
    feature="logout",
    story="As a Logged-in User, I Can Log Out of the Platform",
)
def test_logout_functionality(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login(Config.Username, Config.Password)
    home_page.click_logout_dropdown()
    home_page.click_logout_button()

    expect(login_page.login_button).to_be_visible()
