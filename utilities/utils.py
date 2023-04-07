import softest
from base.base_driver import BaseDriver

class Utils(softest.TestCase,BaseDriver):

    def assertAmountVerification(self, amount,value):
        self.soft_assert(self.assertEqual,amount,value)
        if amount==value:
            print("amount:", amount)
            print("value:", value)
            assert True
        else:
            self.take_screenshot()
            assert False


    def assertProductVerification(self,product,availableproduct):
        self.soft_assert(self.assertEqual, product, availableproduct)
        if product == availableproduct:
            assert True
        else:
            self.take_screenshot()
            assert False

