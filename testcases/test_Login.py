import pytest
import time
import softest
from selenium.webdriver.common.by import By

from pages.informationpage import CustomerInfo
from pages.productoverviewpage import ProductOverview
from pages.saucdemologinpage import LoginCredsPage
from pages.product_listpage import ProductListPage
from pages.checkoutpage import CheckoutPage
from utilities.utils import Utils
from base.base_driver import BaseDriver

@pytest.mark.usefixtures('setup_login')


class TestSauceDemoShopping(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginCredsPage(self.driver)
        self.pl = ProductListPage(self.driver)
        self.chk = CheckoutPage(self.driver)
        self.cust_details = CustomerInfo(self.driver)
        self.prod_ovr = ProductOverview(self.driver)


    def test_sauce_demo(self):
        #self.lp.loginintopage("abccc", "bjnmkn")
        time.sleep(2)
        self.lp.loginintopage("standard_user","secret_sauce")
        self.lp.scroll_page()
        self.pl.product_in_cart_case()
        self.chk.entercheckoutbutton()
        self.cust_details.customer_information("Charu","Gupta","136033")
        self.prod_ovr.product_overview_case()


