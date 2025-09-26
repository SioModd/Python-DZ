from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage
def test_cal():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calc_page = CalcPage(driver)
    calc_page.open_calc()
    calc_page.delay_calc(45)
    calc_page.click_calculator_button('7')
    calc_page.click_calculator_button("'+'")
    calc_page.click_calculator_button('8')
    calc_page.click_calculator_button("'='")
    otv = calc_page.otvet()
    assert otv == 15

    driver.quit()