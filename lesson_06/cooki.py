from  selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
cooki = {
    'name' : 'cookie_policy',
    'value': '1'
}
driver.get("https://www.labirint.ru/")
driver.add_cookie(cooki)

driver.refresh()
driver.delete_all_cookies
driver.refresh()
all_cooki = driver.get_cookies()
print(all_cooki)
sleep(10)
driver.quit
