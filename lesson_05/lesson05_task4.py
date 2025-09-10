from  selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
login = driver.find_element(By.CSS_SELECTOR, "#username")
login.send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")
button = driver.find_element(By.CSS_SELECTOR, "button").click()

flash_text = ""
try:
    flash_text = driver.find_element(By.CSS_SELECTOR, '[class ="flash success"]').text
except:
    flash_text = "Не получилось авторизоваться"
print(flash_text)
driver.quit()
