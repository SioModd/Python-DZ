from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class FormPage():
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открыть сайт https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    def open(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
    
    @allure.step("Заполнить форму данными {fields}")
    def fill_form(self, fields):
        for field, value in fields.items():
            self.wait.until(EC.presence_of_element_located((By.NAME, field))).send_keys(value)

    @allure.step("Нажать на кнопку 'Submit'")
    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button").click()

    @allure.step("Проверить поле {field_id}")
    def get_field_class(self, field_id):
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))).get_attribute("class")
        return element
    
    @allure.step("Проверить что поле в поле Zip code допущена ошибка (подсвечивается красным)")
    def check_zip_code_error(self):
        return "alert-danger" in self.get_field_class("zip-code")
    
    @allure.step("Проверить что поля заполнены верны(подсвечиваються зеленым)")
    def check_fields_success(self):
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone','city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True
    
