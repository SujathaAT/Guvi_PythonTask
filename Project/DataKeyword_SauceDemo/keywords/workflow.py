from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.inventorypage import InventoryPage

class SaucedemoKeywords:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.inventory_page = InventoryPage(driver)
        self.cart_page = CartPage(driver)

    def keyword_login_and_verify(self, username, password):
        """Keyword for TC-1: Login and verify successful navigation."""
        # 1. LOGIN
        self.login_page.login(username, password)

        # 2. Redirection of Page
        try:
            # Waits for redirect of page
            WebDriverWait(self.login_page.driver, 10).until(
                EC.url_contains("inventory.html")
            )
            return True
        except:
            # locked_out_user or a failed login
            return False

    def keyword_verify_sorting(self, sort_type):
        """Keyword for TC-9: Applies sort and returns the list for assertion."""
        self.inventory_page.select_sort_option(sort_type)

        if "Price" in sort_type:
            return self.inventory_page.get_all_product_prices()
        else:
            return self.inventory_page.get_all_product_names()


    def keyword_reset_app(self):
        """Keyword for TC-10: Reset application state."""
        # self.inventory_page.open_menu()
        # self.inventory_page.click_reset_app()