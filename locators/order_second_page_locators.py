from selenium.webdriver.common.by import By

class OrderSecondPageLocators:
    def __init__(self):
        self.DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.RENTAL_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-control")
        self.BLACK_COLOR_CHECKBOX = (By.ID, "black")
        self.GREY_COLOR_CHECKBOX = (By.ID, "grey")
        self.COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

        self.ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

        # Календарь (появляется после клика на поле даты)
        self.CALENDAR = (By.CLASS_NAME, "react-datepicker")
        self.CALENDAR_DAY = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{}']")

        # Выпадающий список срока аренды
        self.RENTAL_DROPDOWN = (By.CLASS_NAME, "Dropdown-menu")
        self.RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")