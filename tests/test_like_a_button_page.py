from selenium.webdriver.common.by import By



def test_button2_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/like-a-button')
    assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()

def test_button2_clicked(browser):
    browser.get('https://www.qa-practice.com/elements/button/like-a-button')
    browser.find_element(By.LINK_TEXT, 'Click').click()
    assert 'Submitted' == browser.find_element(By.ID, 'result-text').text
