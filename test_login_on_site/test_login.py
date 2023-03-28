import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    return browser


class TestLoginStepic:
    link = "https://stepik.org/lesson/236895/step/1"
    login = ''
    password = ''

    def test_login(self, browser):
        browser.get(self.link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        browser.quit()
