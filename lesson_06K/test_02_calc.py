from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_cal():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
  
    waiter = WebDriverWait(driver, 45)
    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")
    buuton_7 = driver.find_element(By.XPATH, "//span[text()='7']").click()
    plus = driver.find_element(By.XPATH, "//span[text()='+']").click()  
    buuton_8 = driver.find_element(By.XPATH, "//span[text()='8']").click() 
    ravno = driver.find_element(By.XPATH, "//span[text()='=']").click()
    spinner = driver.find_element(By.CSS_SELECTOR, "#spinner")

    waiter.until(
        EC.invisibility_of_element_located(spinner))
    
    otvet = driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
    
    assert otvet == '15'

    driver.quit()
