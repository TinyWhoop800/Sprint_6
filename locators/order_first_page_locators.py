from selenium.webdriver.common.by import By

class OrderFirstPageLocators:
    def __init__(self):
        # Поля ввода
        self.NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
        self.SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
        self.ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
        self.PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

        # Кнопка "Далее"
        self.NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

        # Выпадающий список станций метро
        self.METRO_DROPDOWN = (By.CLASS_NAME, "select-search__select")