from  selenium import webdriver
from selenium.webdriver.common.by import By
import allure

class AutorizationShop():
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открыть сайт https://www.saucedemo.com/")
    def open(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        with allure.step("Открыть в панорамном окне"):
            self._driver.maximize_window()
    
    @allure.step("Ввести в поле Username: {name}")
    def user_name(self,name):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)

    @allure.step("Ввести в поле Password: {passw}")
    def password(self, passw):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(passw)
    
    @allure.step("Нажать на кнопку Login")
    def start(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

