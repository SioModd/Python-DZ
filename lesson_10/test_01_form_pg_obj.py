from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage import FormPage
import allure

@allure.epic("Урок10")
@allure.feature("Форма")
@allure.title("Проверка заполнения формы")
@allure.description("Проверить что при вводе валидных данных в поля формы при отправке будут подсвечены" \
" зеленым, а при отправке невалидных данных - красным цветом ")
@allure.severity("critical")
def test_form_first_name():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form(fields)
    form_page.submit()
    assert form_page.check_fields_success()
    assert form_page.check_zip_code_error()
    with allure.step("Закрыть браузер"):
        driver.quit()
