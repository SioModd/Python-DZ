from selenium.webdriver.common.by import By

class CartShop():
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)

    def cart(self):
        items = self._driver.find_elements(By.CSS_SELECTOR, "div.inventory_item_name")
        content = "\n".join([item.text for item in items])
        return content
    
    
    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
