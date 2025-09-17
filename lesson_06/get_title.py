from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.labirint.ru/")
currrent_title = driver.title

print(currrent_title)
driver.quit()