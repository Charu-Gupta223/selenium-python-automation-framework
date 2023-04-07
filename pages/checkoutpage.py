from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
import time
from utilities.utils import Utils

class CheckoutPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    Product_Inside_the_Cart="//*[text()='Test.allTheThings() T-Shirt (Red)']"
    Check_out_Button="checkout"

    def check_out_product(self):
        prod = self.driver.find_element(By.XPATH, self.Product_Inside_the_Cart).text
        ut = Utils()
        ut.assertProductVerification(prod, "Test.allTheThings() T-Shirt (Red)")

    def click_checkout_option(self):
        try:
            return self.check_element_to_be_clickable(By.ID, self.Check_out_Button)
        except:
            self.take_screenshot()

    def entercheckoutbutton(self):
        self.click_checkout_option().click()

