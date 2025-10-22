from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalcPage import CalcPage
import allure
@allure.epic("Урок10")
@allure.feature("Калькулятор")
@allure.title("Проверка работу калькулятора")
@allure.description("ПРоверить вычисление калькулятора с учетом задержки ")
@allure.severity("critical")
def test_cal():

    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    calc_page = CalcPage(driver)
    calc_page.open_calc()
    calc_page.delay_calc(45)
    calc_page.click_calculator_button('7')
    calc_page.click_calculator_button("'+'")
    calc_page.click_calculator_button('8')
    calc_page.click_calculator_button("'='")
    otv = calc_page.otvet()

    with allure.step("Проверить правильность ответа"):
        assert otv == 15

    with allure.step("Закрыть браузер"):
        driver.quit()