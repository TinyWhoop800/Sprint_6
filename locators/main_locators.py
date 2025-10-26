from selenium.webdriver.common.by import By

class MainLocators:
    def __init__(self):
        self.FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")

        self.QUESTION_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemButton']")
        self.ANSWER_LOCATOR = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']/p")

        self.TOP_ORDER_BTN = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[1]")
        self.BOTTOM_ORDER_BTN = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]/button")