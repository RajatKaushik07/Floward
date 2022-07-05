import webbrowser
import time

import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )



@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\KAUSHIK's\\Desktop\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://floward.com")
    time.sleep(15)
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[@class='col-3 col-md-2 text-center p-0 ng-star-inserted']/span[text()='United Kingdom']").click()
    time.sleep(15)
    driver.find_element(By.XPATH, "//a[@class='nav-link flw-color pointer']").click()
    time.sleep(15)

    request.cls.driver = driver
    yield
    driver.close()
    #chromedriver = "C:\\Users\\rajat_mohit_kaushik\\PycharmProjects\\UdemyLearning\\chromedriver.exe"
    #ptions = Options()
    #options.add_argument("download.default_directory=C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    #driver = webbrowser.Chrome(chromedriver, chrome_options=options)
    #driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.maximize_window()
    #request.cls.driver = driver
    #yield
    #driver.close    #Teardown fixture fter class will run