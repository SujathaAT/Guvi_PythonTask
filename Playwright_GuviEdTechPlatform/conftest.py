import pytest
import os
import logging
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.header_page import HeaderPage


# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def setup_guvi(page):
    """
    This runs automatically before every test case
    Uses plugins built-in page fixture.
    """
    page.goto("https://www.guvi.in")
    yield
    # No need of manual close browser, plugin handles it

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
   return {
        **browser_context_args,
        "record_video_dir": "reports/videos/",
        "viewport": {"width": 1280, "height": 720},
        # "default_navigation_timeout": 60000
    }
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {"width": 1920, "height": 1080}
#     }
@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def header_page(page):
    return HeaderPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Automatically capture screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            if not os.path.exists("reports/screenshots"):
                os.makedirs("reports/screenshots")
            page.screenshot(path=f"reports/screenshots/{item.name}_failed.png")
            logger.error(f"Test {item.name} failed. Screenshot captured.")
