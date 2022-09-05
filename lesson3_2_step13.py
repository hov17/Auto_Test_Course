import unittest  # подключаем юнит тест
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


# создаем функцию на возврат текста после успешной регистрации
def registration(link):
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    first_name.send_keys('Answer')
    last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
    last_name.send_keys('Answer')
    email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    email.send_keys('Answer')
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text


# создаем класс для юнит тестов
class TestRegistration(unittest.TestCase):
    def test_registration1(self):  # проверяем первую ссылку
        self.assertEqual(registration(link1), 'Congratulations! You have successfully registered!',
                         'Registration failed!')

    def test_registration2(self):  # проверяем вторую ссылку
        self.assertEqual(registration(link2), 'Congratulations! You have successfully registered!',
                         'Registration failed!')


if __name__ == '__main__':
    unittest.main()
