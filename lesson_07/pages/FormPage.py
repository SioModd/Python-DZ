from  selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
    

    





def test_form_first_name():
    edge_driver_path = r"C:\Users\Anton\Desktop\sox\crom\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
    
    driver.find_element(By.CSS_SELECTOR, "[name = 'first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name = 'last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name = 'address']").send_keys("Ленина 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name = 'e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name = 'phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name = 'zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "[name = 'city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name = 'country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name = 'job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name = 'company']").send_keys("SkyPro")
    
    driver.find_element(By.CSS_SELECTOR, "button").click()

    value_zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    print( value_zip_code)
    assert value_zip_code == "alert py-2 alert-danger"
    
    values = ["#first_name", "#last_name", "#addres", "#email", "#phone_number", "#city", "#country", "#job_position", "#company"]
    for value in values:
        green = driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        assert green == "alert py-2 alert-success"

    driver.quit()
