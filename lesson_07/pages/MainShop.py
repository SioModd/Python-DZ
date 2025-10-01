from selenium.webdriver.common.by import By

class MainShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)

    def buy(self,purchase):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-"+ purchase ).click()

    def open_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
