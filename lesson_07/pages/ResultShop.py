from selenium.webdriver.common.by import By

class ResultShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
    
    def fill_form(self,filling, form_field_locator):
        self._driver.find_element(By.CSS_SELECTOR, "#" + form_field_locator).send_keys(filling)

    def contin(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total_summ(self):
        total= self._driver.find_element(By.CSS_SELECTOR, "[class = 'summary_total_label']").text
        return float(total.split("$")[1])
