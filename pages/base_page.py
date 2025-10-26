from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locator_base = BaseLocators()

    def _assert_cookies(self):
        """ Тап принятия кук """
        try:
            self.click(self.locator_base.COOKIE_BUTTON)
        except:
            pass

    def open(self, url):
        """ Открытие страницы """
        self.driver.get(url)
        self._assert_cookies()

    def find(self, locator):
        """ Поиск элемента """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        """ Поиск кликабельного элемента """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """ Тап по элементу """
        element = self.find_clickable(locator)
        element.click()

    def send_keys(self, locator, text):
        """ Ввод тексте """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        """ Скролл до определенного элемента """
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_all_elements(self, locator):
        """ Поиск всех элементов по локатору """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def are_elements_displayed(self, locators_list):
        """Проверить, что все локторы из списка есть"""
        for locator in locators_list:
            if not self.find(locator).is_displayed():
                return False
        return True