from pages.base_page import BasePage
from selenium.webdriwer.common.by import By


button_selector = (By.ID, 'submit-id-submit')
result_selector = (By.ID, 'result-text')

class SimpleButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def button(self):
        return self.find(button_selector)

    def result(self):
        return self.find(result_selector)
