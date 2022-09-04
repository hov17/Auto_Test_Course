from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(y)
    option1 = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    option2.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()