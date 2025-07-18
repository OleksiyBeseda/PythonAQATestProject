from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        # first_name, last_name, email = form_page.fill_fields_and_submit()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()


        # print(first_name, last_name, email)

        # print(person)
        # print(result)

        # assert f'{first_name} {last_name}' == result[0], 'the first or last has not been filled'
        # assert  email == result[1], 'the email has not been filled'

        assert f'{person.first_name} {person.last_name}' == result[0], 'the first or last has not been filled'
        assert  person.email == result[1], 'the email has not been filled'