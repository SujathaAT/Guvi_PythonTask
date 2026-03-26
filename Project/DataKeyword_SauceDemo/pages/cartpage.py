from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def proceed_to_checkout(self, fname, lname, pcode):
        """TC-8: Complete the checkout flow."""
        self.click_element(self.CHECKOUT_BTN)
        self.type_text(self.FIRST_NAME, fname)
        self.type_text(self.LAST_NAME, lname)
        self.type_text(self.POSTAL_CODE, pcode)
        self.click_element(self.CONTINUE_BTN)
        # Capture screenshot logic would be called here in the test script
        # self.click_element(self.FINISH_BTN)

    def finish_order(self):
        self.click_element(self.FINISH_BTN)

    def get_cart_item_names(self):
        items = self.find_elements(self.CART_ITEM_NAME)
        return [it.text for it in items]

    def get_confirmation_msg(self):
        return self.get_text(self.COMPLETE_HEADER)