import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from keywords.workflow import SaucedemoKeywords

@pytest.fixture
def keywords(driver):
    """Provides a fresh SaucedemoKeywords instance to every test function."""
    return SaucedemoKeywords(driver)

# 1. Add command-line option to select browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome or firefox")


# 2. WebDriver Fixture (Setup and Teardown)
@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser").lower()

    # Load URL from YAML config
    with open("testdata/common_data.yaml", "r") as f:
        config = yaml.safe_load(f)

    # Initialize the specific browser
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-save-password-bubble")

        # options.add_argument("--headless") # Uncomment for Jenkins/CI
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")

    driver.maximize_window()
    driver.implicitly_wait(10)  # Backup implicit wait
    driver.get(config['url'])

    yield driver  # This is where the test execution happens

    # 3. Teardown: Ensure browser is properly closed
    driver.quit()


# 4. Automatic Screenshot on Failure (for Reports)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            # Check if 'driver' is in the test function arguments
            if "driver" in item.fixturenames:
                web_driver = item.funcargs['driver']
                screenshot_path = f"screenshots/{item.name}.png"
                web_driver.save_screenshot(screenshot_path)
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")