import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


@pytest.mark.parametrize('number_of_page', ['236895', '236896', '236897', '236898', '236899', '236903', '236904',
                                            '236905'])
def test_message(browser, number_of_page):
    link = f'https://stepik.org/lesson/{number_of_page}/step/1'
    browser.implicitly_wait(10)
    browser.get(link)
    answer = browser.find_element(By.CSS_SELECTOR, '.ember-text-area')
    answer.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element(By.CSS_SELECTOR, '.attempt__actions > .submit-submission')
    button.click()
    text = browser.find_element(By.CSS_SELECTOR, 'div.lesson__hint > .smart-hints__hint').text
    assert text == 'Correct!', f'Text "{text}" is not "Correct!"'
