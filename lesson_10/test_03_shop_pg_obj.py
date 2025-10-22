from  selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.AutorizationShop import AutorizationShop
from pages.MainShop import MainShop
from pages.CartShop import CartShop
from pages.ResultShop import ResultShop
import allure
@allure.epic("Урок10")
@allure.feature("Магазин")
@allure.title("Проверка оформление заказа")
@allure.description("Проверить правильность оформление заказа - Аторизироваться, выбрать несколько товаров," \
" перейти в корзину, вести данные получателя, проверить стоимость заказа")
@allure.severity("critical")
def test_shop():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    with allure.step("Авторизация"):
        autorization = AutorizationShop(driver)
        autorization.open()
        autorization.user_name("standard_user")
        autorization.password("secret_sauce")
        autorization.start()
    
    with allure.step("Главная страница магазина"):
        main_shop = MainShop(driver)
        main_shop.buy("sauce-labs-backpack")
        main_shop.buy("sauce-labs-bolt-t-shirt")
        main_shop.buy("sauce-labs-onesie")
        main_shop.open_cart()

    with allure.step("Корзина"):
        cart_shop = CartShop(driver)
        actual_content = cart_shop.cart()
        expected_content = "Sauce Labs Backpack\nSauce Labs Bolt T-Shirt\nSauce Labs Onesie"
        with allure.step("Проверить наличие всех товаров"):
            assert actual_content == expected_content
            cart_shop.checkout()
    
    with allure.step("Оформление заказа"):
        result_shop = ResultShop(driver)
        result_shop.fill_form("Anton", "first-name")
        result_shop.fill_form("Petrov", "last-name")
        result_shop.fill_form("ghrrdv", "postal-code")
        result_shop.contin()
        value = result_shop.total_summ()
        with allure.step("Проверить, что стоимость товаров = 58.29"):
            assert value == 58.29

    with allure.step("Закрыть браузер"):
        driver.quit()
