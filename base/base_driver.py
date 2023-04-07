import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import datetime

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def scroll_page(self):
        try:
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
            time.sleep(1)
        except:
            self.take_screenshot()


    def check_element_to_be_clickable(self,locator_type,locator):
        try:
            wait = WebDriverWait(self.driver, 10)
            ele= wait.until(EC.element_to_be_clickable((locator_type, locator)))
            return ele
        except Exception as e:
            self.take_screenshot()
            print(e)

    def take_screenshot(self):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        time_stamp = f"{time}"
        file_name=self.driver.title
        self.driver.get_screenshot_as_file(f"C:/Users/new/PycharmProjects/TestDemoAutomation/screenshots/{file_name}_{time_stamp}.png")




