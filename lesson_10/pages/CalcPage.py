from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage():

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 45)
    
    @allure.step("Открыть сайт https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    def open_calc(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Установить задержку калькулятора = {taimer}")
    def delay_calc(self, taimer):
        with allure.step("Выбрать поле таймера"):
            delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        with allure.step("Очистить предыдущие значение таймера"):
            delay.clear()
        with allure.step("Установить задержку с которой будет работать калькулятор"):
            delay.send_keys(taimer)
    
    @allure.step("Нажать на кнопку = {button}")
    def click_calculator_button(self, button):
        self._driver.find_element(By.XPATH, "//span[text()="+ button +"]").click()

    @allure.step("Получить ответ после задержки операции")
    def otvet(self):
        spinner = self._driver.find_element(By.CSS_SELECTOR, "#spinner")
        self.wait.until(
            EC.invisibility_of_element_located(spinner))
        return int(self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text)
    
