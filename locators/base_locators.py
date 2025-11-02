from selenium.webdriver.common.by import By

class BaseLocators:
    def __init__(self):
        # Кнопка принятия куков
        self.COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

        # Логотипы
        self.SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
        self.YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")