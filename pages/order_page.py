from locators.order_first_page_locators import OrderFirstPageLocators
from locators.order_second_page_locators import OrderSecondPageLocators
from locators.order_modals_locators import OrderModalLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from config import Config

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators_first_order = OrderFirstPageLocators()
        self.locators_second_order = OrderSecondPageLocators()
        self.locators_modal_order = OrderModalLocators()
        self.config = Config()


    def _get_confirmation_modal_elements(self):
        """Внутренний метод для получения списка элементов подтверждения заказа"""
        return [
            self.locators_modal_order.SUCCESS_TITLE,
            self.locators_modal_order.ORDER_NUMBER,
            self.locators_modal_order.VIEW_STATUS_BUTTON
        ]

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.send_keys(self.locators_first_order.NAME_FIELD, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, surname):
        self.send_keys(self.locators_first_order.SURNAME_FIELD, surname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.send_keys(self.locators_first_order.ADDRESS_FIELD, address)

    @allure.step('Выбрать станцию метро: {station_name}')
    def select_metro_station(self, station_name):
        self.click(self.locators_first_order.METRO_FIELD)
        station_locator = (By.XPATH, f"//div[text()='{station_name}']")
        self.click(station_locator)

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, phone):
        self.send_keys(self.locators_first_order.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next(self):
        self.click(self.locators_first_order.NEXT_BUTTON)

    @allure.step('Заполнить первую страницу формы заказа')
    def fill_first_page(self, user_data):
        self.set_name(user_data['name'])
        self.set_surname(user_data['surname'])
        self.set_address(user_data['address'])
        self.select_metro_station(user_data['metro'])
        self.set_phone(user_data['phone'])
        self.click_next()

    @allure.step('Выбрать дату: {day}')
    def set_date(self, day):
        self.click(self.locators_second_order.DATE_FIELD)
        day_locator = (self.locators_second_order.CALENDAR_DAY[0], self.locators_second_order.CALENDAR_DAY[1].format(day))
        self.click(day_locator)

    @allure.step('Выбрать срок аренды: {period}')
    def select_rental_period(self, period):
        self.click(self.locators_second_order.RENTAL_PERIOD_FIELD)
        period_locator = (self.locators_second_order.RENTAL_OPTION[0], self.locators_second_order.RENTAL_OPTION[1].format(period))
        self.click(period_locator)

    @allure.step('Выбрать цвет самоката: {color}')
    def select_color(self, color):
        if color == 'black':
            self.click(self.locators_second_order.BLACK_COLOR_CHECKBOX)
        elif color == 'grey':
            self.click(self.locators_second_order.GREY_COLOR_CHECKBOX)

    @allure.step('Заполнить комментарий: {comment}')
    def set_comment(self, comment):
        self.send_keys(self.locators_second_order.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order(self):
        self.click(self.locators_second_order.ORDER_BUTTON)

    @allure.step('Заполнить вторую страницу формы заказа')
    def fill_second_page(self, user_data):
        self.set_date(user_data['date'])
        self.select_rental_period(user_data['rental_period'])
        self.select_color(user_data['color'])
        self.set_comment(user_data['comment'])
        self.click_order()

    @allure.step('Ожидаем появление окна "Хотите оформить заказ?"')
    def wait_for_confirmation(self):
        self.find(self.locators_modal_order.CONFIRM_MODAL)

    @allure.step('Подтверждение заказа')
    def click_confirm_order_modal(self):
        self.click(self.locators_modal_order.CONFIRM_BTN)

    @allure.step('Проверить все элементы окна подтверждения заказа')
    def are_confirmation_elements_displayed(self):
        return self.are_elements_displayed(self._get_confirmation_modal_elements())

    @allure.step('Тап по кнопке "Посмотреть статус"')
    def click_view_status_btn(self):
        self.click(self.locators_modal_order.VIEW_STATUS_BUTTON)