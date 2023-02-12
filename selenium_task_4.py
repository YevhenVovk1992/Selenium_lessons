from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support.select import Select


class SeleniumWebDriverChrom:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()

    def __enter__(self):
        self.browser.get(self.link)
        return self.browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_val:
            self.browser.quit()


def run_selenium_task(link: str) -> None:
    with SeleniumWebDriverChrom(link) as browser:
        x1 = browser.find_element(By.XPATH, '//*[@id="num1"]').text
        x2 = browser.find_element(By.XPATH, '//*[@id="num2"]').text
        s = int(x1) + int(x2)
        Select(browser.find_element(By.XPATH, "//select[@id='dropdown']")).select_by_value(str(s))
        browser.find_element(By.XPATH, "//button[@type='submit']")

        time.sleep(10)


if __name__ == '__main__':
    page_link = "http://suninjuly.github.io/selects1.html"
    run_selenium_task(page_link)