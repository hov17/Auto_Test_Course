from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'example.txt'
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    for elements in ['/html/body/div/form/div/input[1]', '/html/body/div/form/div/input[2]',
                     '/html/body/div/form/div/input[3]']:
        browser.find_element(By.XPATH, elements).send_keys('Answer')
    button = browser.find_element(By.ID, 'file')
    button.send_keys(file_path)
    button1 = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button1.click()
finally:
    time.sleep(10)
    browser.quit()