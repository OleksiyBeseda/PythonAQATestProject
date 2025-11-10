from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    crome_browser = webdriver.Chrome()
    crome_browser.implicitly_wait(10)
    return crome_browser
