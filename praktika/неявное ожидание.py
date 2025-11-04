from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

# Найти элемент "Check All" и проверить его наличие
check_all_button = driver.find_element(By.ID, "check1")
check_all_button.click()

print("Элемент 'Check All' найден и кликнут")

driver.quit()