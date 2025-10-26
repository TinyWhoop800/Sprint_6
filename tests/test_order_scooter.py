import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data.order_data import OrderData

@allure.suite('Заказ самоката')
class TestOrderScooter:

    @allure.title('Заказ самоката: {user_data[name]} через {button_type} кнопку')
    @pytest.mark.parametrize('button_type,user_data', [
        ('top', OrderData.USER_1),
        ('bottom', OrderData.USER_2)
    ])
    def test_order_scooter(self, driver, button_type, user_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.click_order_btn(button_type)
        order_page.fill_first_page(user_data)
        order_page.fill_second_page(user_data)
        order_page.wait_for_confirmation()
        order_page.click_confirm_order_modal()
        order_page.are_confirmation_elements_displayed()
        order_page.click_view_status_btn()
        main_page.click_scooter_logo()
        main_page.is_scooter_main_page()
        main_page.click_yandex_logo()
        main_page.is_dzen_page_opened()