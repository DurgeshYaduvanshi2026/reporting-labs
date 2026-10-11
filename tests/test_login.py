from playwright.sync_api import Page, expect
import pytest
from config import Config
from reporting_labs import meta, log, test_data, step
from src.pages.orangehrm_login_page import LoginPage
from src.pages.orangehrm_home_page import HomePage


@pytest.mark.meta(
    priority="P1",
    owner="Durgesh Yaduvanshi",
    feature="login",
    story="• As a Returning User, I Can Log In Successfully with Valid Credentials",
)
def test_login(page: Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.login(Config.Username, Config.Password)
    log("Login successfully")

    expect(home_page.heading_message).to_be_visible()
