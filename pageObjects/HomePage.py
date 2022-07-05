import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pageObjects.AddToCart import AddToCart
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AddItem(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    Category = (By.XPATH, "//div[@class='first-category']")
    search = "Pink Stripe Phalaenopsis"
    search_XPATH = "//input[@id='search-mobile']"

    def ItemSelect(self):
        self.wait()
        self.driver.find_element(By.XPATH,"//div[@class='first-category']").click()
        self.wait()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search-mobile']"))).send_keys("Pink Stripe Phalaenopsis")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search-mobile']"))).send_keys(Keys.RETURN)
        time.sleep(15)
        action = ActionChains(self.driver)
        item_select = self.driver.find_element(By.XPATH, "//img[@alt='Pink Stripe Phalaenopsis']")
        time.sleep(10)
        action.move_to_element(item_select).perform()
        time.sleep(4)
        item_select.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(15)
        addtocart =AddToCart(self.driver)
        return addtocart

