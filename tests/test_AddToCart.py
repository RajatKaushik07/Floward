import pytest

from pageObjects.Login import HomePage
from pageObjects.HomePage import AddItem
from pageObjects.AddToCart import AddToCart
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_AddToCart(BaseClass):
    def test_floward(self):
        log = self.getLogger()
        login = HomePage(self.driver)
        login.EnterCreds()
        homepage = AddItem(self.driver)
        homepage.ItemSelect()
        addtocart = AddToCart(self.driver)
        addtocart.additem()

