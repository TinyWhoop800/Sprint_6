from pages.base_page import BasePage
from locators.main_locators import MainLocators
import allure
from config import Config

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators_main = MainLocators()
        self.config = Config()

    @allure.step('Открываем страницу "Главная"')
    def open_main_page(self):
        self.open(self.config.main_url)
        self._assert_cookies()

    @allure.step('Соглашаемся с принятием кук')
    def _assert_cookies(self):
        try:
            self.click(self.locator_base.COOKIE_BUTTON)
        except:
            pass

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_to_important_questions_section(self):
        self.scroll_to_element(self.locators_main.FAQ_SECTION)

    @allure.step('Нажимаем на вопрос номер {index} и открываем ответ')
    def expand_question(self, index):
        questions = self.find_all_elements(self.locators_main.QUESTION_LOCATOR)
        question = questions[index]
        self.scroll_to_element(self.locators_main.QUESTION_LOCATOR)
        question.click()
        answers = self.find_all_elements(self.locators_main.ANSWER_LOCATOR)
        self.wait.until(lambda driver: answers[index].is_displayed())

    @allure.step('Получаем текст ответа на вопрос номер {index}')
    def get_answer_text(self, index):
        answers = self.find_all_elements(self.locators_main.ANSWER_LOCATOR)
        return answers[index].text

    @allure.step('Проверяем, что ответ на вопрос номер {index} отображается')
    def is_answer_expanded(self, index):
        answers = self.find_all_elements(self.locators_main.ANSWER_LOCATOR)
        return answers[index].is_displayed()

    @allure.step('Скролл до нижней кнопки "Заказать"')
    def _scroll_to_bottom_order_btn(self):
        self.scroll_to_element(self.locators_main.BOTTOM_ORDER_BTN)

    @allure.step('Тап по кнопке "Заказать" на главной странице')
    def click_order_btn(self, button_type = "top"):
        if button_type == "top":
            self.click(self.locators_main.TOP_ORDER_BTN)
        elif button_type == "bottom":
            self._scroll_to_bottom_order_btn()
            self.click(self.locators_main.BOTTOM_ORDER_BTN)

    @allure.step('Тап по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(self.locator_base.SCOOTER_LOGO)

    @allure.step('Тап по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(self.locator_base.YANDEX_LOGO)

    @allure.step('Проверить, что открыта главная страница Самоката')
    def is_scooter_main_page(self):
        return self.get_current_url() == self.config.main_url

    @allure.step('Проверить, что открыта страница Дзена')
    def is_dzen_page_opened(self):
        return "dzen.ru" in self.get_current_url()