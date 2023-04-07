from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
import time

from utilities.utils import Utils


class ProductOverview(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    Check_Product_Info="//div[@class='summary_info_label summary_total_label']"
    Click_on_Finish_Button = "finish"

    def get_product_overview(self):
        total_amount = self.driver.find_element(By.XPATH, self.Check_Product_Info).text
        ut = Utils()
        ut.assertAmountVerification(total_amount, "Total: $17.27")

    def get_finish_button(self):
        try:
            return self.driver.find_element(By.ID,self.Click_on_Finish_Button)
        except:
            self.take_screenshot()

    def enter_finish_btn(self):
        self.get_finish_button().click()
        time.sleep(2)

    def product_overview_case(self):
        self.get_product_overview()
        self.enter_finish_btn()
        print("\nThank you for your order!")
        print("Thankyou for shopping with us")
