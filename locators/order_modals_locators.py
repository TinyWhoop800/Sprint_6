from selenium.webdriver.common.by import By

class OrderModalLocators:
    def __init__(self):
        # Первое модальное окно - подтверждение заказа
        self.CONFIRM_MODAL = (By.XPATH, "//div[text()='Хотите оформить заказ?']")
        self.CONFIRM_BTN = (By.XPATH, "//button[text()='Да']")

        # Второе модальное окно - успешное оформление
        self.SUCCESS_TITLE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
        self.ORDER_NUMBER = (By.XPATH, "//div[contains(text(), 'Номер заказа')]")
        self.VIEW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")