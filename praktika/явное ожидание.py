#элемент с текстом A/B Testing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")


driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
driver.implicitly_wait(20)


element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#content')))
txt = element.text
print(txt)