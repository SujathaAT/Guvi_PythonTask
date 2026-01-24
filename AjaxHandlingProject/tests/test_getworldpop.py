
from pages.homePage import HomePage


def test_fetchpopcount(driver):

    homePage = HomePage(driver)
    homePage.check_popcount(driver)

