from  selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

def test_form_first_name():
    edge_driver_path = r"C:\Users\Anton\Desktop\sox\crom\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
    
    driver.find_element(By.CSS_SELECTOR, "[name = 'first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name = 'last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name = 'address']").send_keys("Ленина 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name = 'e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name = 'phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name = 'zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "[name = 'city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name = 'country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name = 'job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name = 'company']").send_keys("SkyPro")
    
    driver.find_element(By.CSS_SELECTOR, "button").click()

    value_zip_code = driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    print( value_zip_code)
    assert value_zip_code == "alert py-2 alert-danger"
    
    values = ["#first_name", "#last_name", "#addres", "#email", "#phone_number", "#city", "#country", "#job_position", "#company"]
    for value in values:
        green = driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        assert green == "alert py-2 alert-success"

    driver.quit()
