from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


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


if __name__ == '__main__':
    page_link = "https://suninjuly.github.io/math.html"
    with SeleniumWebDriverChrom(page_link) as browser:
        x_element = browser.find_element(By.XPATH, '//div[@class="form-group"]/label/span[2]')
        input_field = browser.find_element(By.XPATH, "//input[@id='answer']")
        input_field.send_keys(calc(x_element.text))
        check_box_robot = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']")
        check_box_robot.click()
        radiobutton_robot = browser.find_element(By.XPATH, "//label[@for='robotsRule']")
        radiobutton_robot.click()
        button = browser.find_element(By.XPATH, "//button[@type='submit']")
        button.click()
        time.sleep(10)
