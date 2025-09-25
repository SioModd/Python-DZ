from  selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.FormPage import FormPage

def test_form_first_name():
    edge_driver_path = r"C:\Users\Anton\Desktop\sox\crom\edge\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit()
    assert form_page.check_fields_success()
    assert form_page.check_zip_code_error()

    driver.quit()
