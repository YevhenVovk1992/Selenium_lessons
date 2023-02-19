import os.path
import re
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

def print_answer(driver):
    alert = driver.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
                      alert_text)
    print(text)


def run_selenium_task(link: str) -> None:
    with SeleniumWebDriverChrom(link) as browser:
        browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
        browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        browser.switch_to.window(browser.window_handles[1])
        x = browser.find_element(By.XPATH, "//span[@id='input_value']")
        browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x.text))
        browser.find_element(By.XPATH, "//button[@type='submit']").click()

        print_answer(browser)


if __name__ == '__main__':
    page_link = "http://suninjuly.github.io/redirect_accept.html"
    run_selenium_task(page_link)
