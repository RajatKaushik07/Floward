from selenium.webdriver.common.by import By

from pageObjects.HomePage import AddItem
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver



    UserName = (By.XPATH,"//input[@id='login']")
    Password = (By.XPATH, "//input[@id='login-psw']")
    Login = (By.XPATH, "//button[@type='submit']/span")

    def EnterCreds(self):
        self.wait()
        self.driver.find_element(*HomePage.UserName).send_keys("kaushikmohit62@gmail.com")
        self.wait()
        self.driver.find_element(*HomePage.Password).send_keys("Satish@123")
        self.wait()
        self.driver.find_element(*HomePage.Login).click()
        self.wait()
        Homepage = AddItem(self.driver)
        return Homepage