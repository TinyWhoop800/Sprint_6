from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locator_base = BaseLocators()

    @allure.step('Открыть страницу: {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент по локатору: {locator}')
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Найти кликабельный элемент по локатору: {locator}')
    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Кликнуть по элементу: {locator}')
    def click(self, locator):
        element = self.find_clickable(locator)
        element.click()

    @allure.step('Ввести текст "{text}" в элемент: {locator}')
    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Проскроллить к элементу: {locator}')
    def scroll_to_element(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Найти все элементы по локатору: {locator}')
    def find_all_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step('Проверить отображение всех элементов из списка')
    def are_elements_displayed(self, locators_list):
        for locator in locators_list:
            if not self.find(locator).is_displayed():
                return False
        return True

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url