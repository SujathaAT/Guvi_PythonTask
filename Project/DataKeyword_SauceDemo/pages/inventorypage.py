import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.basepage import BasePage


class InventoryPage(BasePage):
    # Locators
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_random_products_and_add(self, count=4):
        """TC-5 & TC-6: Extract data and add random items."""
        all_items = self.find_elements(self.PRODUCT_ITEMS)
        selected_items = random.sample(all_items, count)

        data_list = []
        for item in selected_items:
            name = item.find_element(*self.ITEM_NAME).text
            price = item.find_element(*self.ITEM_PRICE).text
            data_list.append({"name": name, "price": price})
            item.find_element(*self.ADD_TO_CART_BTN).click()
        return data_list

    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"

    def logout(self):
        self.click_element(self.MENU_BTN)

        # Wait for the animation to finish (approx 1 second)
        import time
        time.sleep(1)

        # Use JavaScript click if standard click still fails
        try:
            logout_link = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_LINK))
            self.driver.execute_script("arguments[0].click();", logout_link)
        except Exception as e:
            print(f"Standard click failed, attempting JavaScript click: {e}")

    def sort_products(self, option_text):
        """ Sort by visible text (e.g., 'Price (low to high)')"""
        select = Select(self.find_element(self.SORT_DROPDOWN))
        select.select_by_visible_text(option_text)

    def get_all_product_names(self):
        elements = self.find_elements(self.ITEM_NAME)
        return [prod.text for prod in elements]

    def select_sort_option(self, option_text):
        dropdown = Select(self.find_element(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def get_all_product_prices(self):
        """Returns a list of all product prices removing '$'."""
        elements = self.find_elements(self.ITEM_PRICE)
        # Remove symbol $ in price
        return [float(el.text.replace('$', '')) for el in elements]

    def reset_app_state(self):
        """TC-10: Clear cart and reset app."""
        self.click_element(self.MENU_BTN)
        self.click_element(self.RESET_LINK)