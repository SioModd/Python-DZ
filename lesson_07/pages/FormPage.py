from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage():
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(EC.presence_of_element_located((By.NAME, field))).send_keys(value)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button").click()

    def get_field_class(self, field_id):
        element = self.wait.until(
            EC.presence_of_element_located((By.ID, field_id))).get_attribute("class")
        return element

    def check_zip_code_error(self):
        return "alert-danger" in self.get_field_class("zip-code")

    def check_fields_success(self):
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone','city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True
    
