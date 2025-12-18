from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

input_1 = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input_1.send_keys('Sky')
input_1.clear()
input_1.send_keys('Pro')

# Задержка для просмотра результатов
sleep(3)

# Закрытие драйвера
driver.quit()