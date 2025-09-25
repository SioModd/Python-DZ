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

#def t_shop():
    #driver.get("https://www.saucedemo.com/")
    #driver.implicitly_wait(4)
    
    #user_name = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    #password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    
    #button_start = driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    
    #button_buy_backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    #button_buy_bolt_t_shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    #button_buy_onesie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    
    #driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
    
    #driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    #first_name = driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Anton")
    #last_name = driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Petrov")
    #zip_cod = driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("ghrrdv")
    
    #driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    #total = driver.find_element(By.CSS_SELECTOR, "[class = 'summary_total_label']").text
    #value = float(total.split("$")[1])
    
    #assert value == 58.29
    #driver.quit()
