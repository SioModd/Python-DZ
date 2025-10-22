from selenium.webdriver.common.by import By
import allure

class ResultShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
    
    @allure.step("Ввести в поле {form_field_locator} значение {filling}")
    def fill_form(self,filling, form_field_locator):
        self._driver.find_element(By.CSS_SELECTOR, "#" + form_field_locator).send_keys(filling)

    @allure.step("Нажать на кнопку 'Continue'")
    def contin(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    @allure.step("Стоимость выбранных товаров")
    def total_summ(self):
        total= self._driver.find_element(By.CSS_SELECTOR, "[class = 'summary_total_label']").text
        return float(total.split("$")[1])