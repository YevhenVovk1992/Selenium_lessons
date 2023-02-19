import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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


def calc(x: str) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


def run_selenium_task(link: str) -> None:
    with SeleniumWebDriverChrom(link) as browser:
        price = WebDriverWait(browser, 13).until(
            expected_conditions.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '100'))
        browser.find_element(By.XPATH, "//button[@id='book']").click()
        x = browser.find_element(By.CSS_SELECTOR, "#input_value")
        browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x.text))
        browser.find_element(By.XPATH, "//button[@id='solve']").click()


if __name__ == '__main__':
    page_link = "http://suninjuly.github.io/explicit_wait2.html"
    run_selenium_task(page_link)
