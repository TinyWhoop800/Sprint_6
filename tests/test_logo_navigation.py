import allure
from pages.main_page import MainPage

@allure.suite('Навигация по логотипам')
class TestLogoNavigation:

    @allure.title('Переход на главную через логотип Самоката со страницы заказа')
    def test_scooter_logo_navigation_from_order_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_order_btn('top')
        main_page.click_scooter_logo()
        main_page.is_scooter_main_page()

    @allure.title('Переход на Дзен через логотип Яндекса с главной страницы')
    def test_yandex_logo_navigation_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_yandex_logo()
        main_page.is_dzen_page_opened()