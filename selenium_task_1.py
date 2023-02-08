from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[@name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.XPATH, "//input[@id='country']")
    input4.send_keys("Ukraine")
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла