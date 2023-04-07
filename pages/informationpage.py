from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
import time

class CustomerInfo(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    First_Name_Field="//input[@placeholder='First Name']"
    Last_Name_Field="last-name"
    Zipcode_Field="postal-code"
    Continue_Button= "continue"

    def getistnameinfo(self):
        try:
            return self.driver.find_element(By.XPATH,self.First_Name_Field)
        except:
            self.take_screenshot()

    def getlastnameinfo(self):
        try:
            return self.driver.find_element(By.ID,self.Last_Name_Field)
        except:
            self.take_screenshot()

    def getzipcode(self):
        try:
            return self.driver.find_element(By.ID,self.Zipcode_Field)
        except:
            self.take_screenshot()

    def get_continue_btn(self):
        try:
            return self.driver.find_element(By.ID, self.Continue_Button)
        except:
            self.take_screenshot()

    def enter_istname(self,istname):
        self.getistnameinfo().click()
        self.getistnameinfo().send_keys(istname)
        time.sleep(1)


    def enter_lastname(self,lastname):
        self.getlastnameinfo().click()
        self.getlastnameinfo().send_keys(lastname)
        time.sleep(1)

    def enter_zipcode(self,zipcode):
        self.getzipcode().click()
        self.getzipcode().send_keys(zipcode)
        time.sleep(1)

    def enter_continue_btn(self):
        self.get_continue_btn().click()
        time.sleep(1)

    def customer_information(self,first_name,last_name,zip_code):
        self.enter_istname(first_name)
        self.enter_lastname(last_name)
        self.enter_zipcode(zip_code)
        self.enter_continue_btn()
