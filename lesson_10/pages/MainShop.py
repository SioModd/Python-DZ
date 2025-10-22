from selenium.webdriver.common.by import By
import allure

class MainShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
    
    @allure.step("Добавить товар  {purchase}  в корзину")
    def buy(self,purchase):
        with allure.step("Нажать кнопку 'Add to cart'"):
            self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-"+ purchase ).click()
    
    @allure.step("перейти в корзину")
    def open_cart(self):
        with allure.step("Нажать на иконку тележки"):
            self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
