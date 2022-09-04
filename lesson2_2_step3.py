from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element(By.ID, 'num1').text)
    b = int(browser.find_element(By.ID, 'num2').text)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_visible_text(str(a + b))
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()
finally:
    time.sleep(10)
    browser.quit()