from datetime import datetime, timedelta
import _datetime
import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AddToCart(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    Addtocartbutton= (By.XPATH, "//button[@class='add-to-cart btn btn-floward m-0 w-100']")
    Continue = (By.XPATH,"//button[@class='btn btn-floward']")
    success_message =(By.XPATH,"//p[@class='fontcolor font-weight-bold text-left']")

    def additem(self):
        self.driver.find_element(*AddToCart.Addtocartbutton).click()
        time.sleep(10)
        self.driver.find_element(*AddToCart.Continue).click()
        msg = self.driver.find_element(By.XPATH,"//p[@class='fontcolor font-weight-bold text-left']").get_attribute('textContent')
        print(msg)
        time.sleep(10)
        assert "Congrats" in msg
        print('Item Added Successfully')
        self.driver.get_screenshot_as_file("Order.png")

