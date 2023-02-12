import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


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
        browser.fullscreen_window()
        x = browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[1]/div[1]/label[1]/span[2]")
        res = calc(x.text)
        browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(res)
        browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
        radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
        radiobutton.click()
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(10)


if __name__ == '__main__':
    page_link = "http://suninjuly.github.io/execute_script.html"
    run_selenium_task(page_link)
    