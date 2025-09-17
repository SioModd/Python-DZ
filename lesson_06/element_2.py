from  selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/visibility")
its_disp = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
print(its_disp)
sleep(2)
driver.find_element(By.CSS_SELECTOR, '#hideButton').click()
sleep(2)
its_disp = driver.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
print(its_disp)

driver.quit()