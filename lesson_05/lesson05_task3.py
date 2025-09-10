from  selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
poisk = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
poisk.send_keys("Sky")
poisk = driver.find_element(By.CSS_SELECTOR, '[type="number"]').clear()
poisk = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
poisk.send_keys("Pro")
driver.quit()
