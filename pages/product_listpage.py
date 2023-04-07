import time

from selenium.webdriver.common.by import By
from pages.saucdemologinpage import LoginCredsPage
from base.base_driver import BaseDriver
from utilities.utils import Utils


class ProductListPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    Select_the_product_Button="add-to-cart-test.allthethings()-t-shirt-(red)"
    Click_on_Cart_option="//*[@id='shopping_cart_container']/a"


    def choose_product(self):
        try:
            return self.driver.find_element(By.ID, self.Select_the_product_Button)
        except:
            self.take_screenshot()

    def selectcartoption(self):
        try:
            return self.driver.find_element(By.XPATH, self.Click_on_Cart_option)
        except:
            self.take_screenshot()

    def enterproductchosed(self):
        self.choose_product().click()
        time.sleep(1)

    def entercartoption(self):
        time.sleep(2)
        self.selectcartoption().click()

    def product_in_cart_case(self):
        self.enterproductchosed()
        self.entercartoption()




