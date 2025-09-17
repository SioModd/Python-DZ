from  selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.labirint.ru/")
element = driver.find_element(By.CSS_SELECTOR, "#search-field")
element.send_keys("text pro")
print(element)
driver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
sleep(5)
driver.quit()