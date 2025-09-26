from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage():

    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open_calc(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    def delay_calc(self, taimer):
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(taimer)
    
    def click_calculator_button(self, button):
        self._driver.find_element(By.XPATH, "//span[text()="+ button +"]").click()

    def otvet(self):
        spinner = self._driver.find_element(By.CSS_SELECTOR, "#spinner")
        self.wait.until(
            EC.invisibility_of_element_located(spinner))
        return int(self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text)
    
