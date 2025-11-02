from selenium.webdriver.common.by import By

class MainLocators:
    def __init__(self):
        self.FAQ_SECTION = (By.CSS_SELECTOR, "[data-accordion-component='Accordion']")

        self.QUESTION_LOCATOR = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
        self.ANSWER_LOCATOR = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel'] p")

        self.TOP_ORDER_BTN = (By.XPATH, "//button[text()='Заказать' and not(contains(@class, 'Middle'))]")
        self.BOTTOM_ORDER_BTN = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Middle')]")