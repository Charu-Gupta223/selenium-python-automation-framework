from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver


class LoginCredsPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    UserName_In_Field="//input[@placeholder='Username']"
    Password_In_Field="//input[@placeholder='Password']"
    Click_Submit_Button="login-button"

    def getusernamefield(self):
        try:
            return self.driver.find_element(By.XPATH,self.UserName_In_Field)
        except:
            self.take_screenshot()

    def getpasswordfield(self):
        try:
            return self.driver.find_element(By.XPATH,self.Password_In_Field)
        except:
            self.take_screenshot()

    def clicksubmitbtn(self):
        try:
            return self.check_element_to_be_clickable(By.ID,self.Click_Submit_Button)
        except:
            self.take_screenshot()

    def enterusernamefiled(self,userlocation):
        self.getusernamefield().click()
        self.getusernamefield().send_keys(userlocation)
        time.sleep(1)


    def enterpassword_field(self,passwdlocation):
        time.sleep(2)
        self.getpasswordfield().click()
        self.getpasswordfield().send_keys(passwdlocation)
        time.sleep(1)

    def click_submit(self):
        self.clicksubmitbtn().click()


    def clear_out(self):
        self.getpasswordfield().clear()
        self.getusernamefield().clear()

    def loginintopage(self,username,password):
        self.clear_out()
        self.enterusernamefiled(username)
        self.enterpassword_field(password)
        self.click_submit()




