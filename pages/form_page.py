import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_fields_and_submit(self):

        # first_name = 'Hello'
        # last_name = 'World'
        # email = "hello@world.com"

        person = generated_person()
        path = generated_file()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        # self.element_is_visible(Locators.MOBILE).send_keys('5423423423')
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        # subject.send_keys('English')
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        # self.element_is_visible(Locators.FILE_INPUT).send_keys(r'/Users/oleksiybeseda/PycharmProjects/PythonAQATestProject/.venv311/test.txt')
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        # self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys('City, 1231, USA')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        # time.sleep(5)
        # return first_name, last_name, email
        return person

    def form_result(self):
        result_list = self.element_is_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

    # result_text = []
    #     for i in result_list:
    #         result_text.append(i.text)

        return result_text

# if there are a lot of locators in the project => insert locators inside each page test file