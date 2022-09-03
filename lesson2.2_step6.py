from math import *

def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = 'http://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    x = calc(x_element)
    input1 = browser.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(x)
    option1 = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()