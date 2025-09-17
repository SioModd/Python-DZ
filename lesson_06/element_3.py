from  selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://demoqa.com/radio-button")
is_enab = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(is_enab)
is_enab = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(is_enab)

driver.quit()