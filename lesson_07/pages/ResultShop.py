from selenium.webdriver.common.by import By

class ResultShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
    
    def first_name(self,f_name):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(f_name)

    def last_name(self, l_name):
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(l_name)

    def zip_code(self, code):
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(code)

    def contin(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total_summ(self):
        total= self._driver.find_element(By.CSS_SELECTOR, "[class = 'summary_total_label']").text
        return float(total.split("$")[1])
