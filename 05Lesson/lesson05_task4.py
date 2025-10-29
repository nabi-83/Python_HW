from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("http://the-internet.herokuapp.com/login")

input_1 = driver.find_element(By.CSS_SELECTOR, 'input[id="username"]')
input_1.send_keys('tomsmith')

input_2 = driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
input_2.send_keys('SuperSecretPassword!')

button = driver.find_element(By.CLASS_NAME, "fa-sign-in")
button.click()

flash = driver.find_element(By.CSS_SELECTOR, "div#flash")

print(flash.text)

# Задержка для просмотра результатов
sleep(3)

# Закрытие драйвера
driver.quit()