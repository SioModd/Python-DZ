from  selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class AutorizationShop():
    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def user_name(self,name):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)

    def password(self, passw):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(passw)

    def start(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

