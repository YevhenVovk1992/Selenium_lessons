import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Loger:
    def __init__(self) -> None:
        self.init_loger = logging.getLogger('Task process')
        self.handler = logging.StreamHandler()
        self.handler.setLevel(logging.WARNING)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.init_loger.addHandler(self.handler)

    def console_info(self, msg: str) -> None:
        self.init_loger.warning(msg)


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
    log = Loger()
    with SeleniumWebDriverChrom(link) as driver:
        log.console_info('Start')
        driver.find_element(By.XPATH, ".//a[@class='blinkingText']").click()
        driver.switch_to.window(driver.window_handles[1])
        log.console_info('Switch to second window')
        wait = WebDriverWait(driver, 10)
        log.console_info('Get email')
        email = wait.until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//a[normalize-space()='mentor@rahulshettyacademy.com']")
            )).text
        driver.switch_to.window(driver.window_handles[0])
        log.console_info('Enter username and password')
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys(email)
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password")
        driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
        log.console_info('Wait and get text of the alert')
        wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, ".alert-danger")
            ))
        print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


if __name__ == '__main__':
    page_link = "https://rahulshettyacademy.com/loginpagePractise/"
    run_selenium_task(page_link)
