from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *
import time


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, 'book')
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()
    element = browser.find_element(By.ID, 'input_value').text
    x = calc(element)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    button2 = browser.find_element(By.ID, 'solve')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()
