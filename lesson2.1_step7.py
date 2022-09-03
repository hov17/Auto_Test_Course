from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elemenet = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    x = calc(elemenet)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(x)
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()

""" -
    for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
    browser.find_element_by_css_selector(selector).click()
    -
    можно написать с помощью цикла
                                    """