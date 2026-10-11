import pytest

from playwright.sync_api import Playwright, sync_playwright ,expect


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, base_url):
    page = browser.new_page()
    page.goto(base_url)
    yield page
    page.close()
