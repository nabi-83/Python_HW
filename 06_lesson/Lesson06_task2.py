from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

#зайти на сайт
driver.get("http://uitestingplayground.com/textinput")

input_1 = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input_1.send_keys('Skypro')
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

flash = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

print(flash.text)

driver.quit()