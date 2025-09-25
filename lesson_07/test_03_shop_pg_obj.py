from  selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.AutorizationShop import AutorizationShop
from pages.MainShop import MainShop
from pages.CartShop import CartShop
from pages.ResultShop import ResultShop

def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    autorization = AutorizationShop(driver)
    autorization.open()
    autorization.user_name("standard_user")
    autorization.password("secret_sauce")
    autorization.start()

    main_shop = MainShop(driver)
    main_shop.buy("sauce-labs-backpack")
    main_shop.buy("sauce-labs-bolt-t-shirt")
    main_shop.buy("sauce-labs-onesie")
    main_shop.open_cart()

    cart_shop = CartShop(driver)
    actual_content = cart_shop.cart()
    expected_content = "Sauce Labs Backpack\nSauce Labs Bolt T-Shirt\nSauce Labs Onesie"
    assert actual_content == expected_content
    cart_shop.checkout()

    result_shop = ResultShop(driver)
    result_shop.first_name("Anton")
    result_shop.last_name("Petrov")
    result_shop.zip_code("ghrrdv")
    result_shop.contin()
    value = result_shop.total_summ()
    assert value == 58.29

    driver.quit()
