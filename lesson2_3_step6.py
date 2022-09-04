from selenium import webdriver
from selenium.webdriver.common.by import By
from math import *
import time

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    element = browser.find_element(By.ID, 'input_value').text
    x = calc(element)
    input1 = browser.find_element(By.ID, 'answer').send_keys(x)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button2.click()
finally:
    time.sleep(10)
    browser.quit()