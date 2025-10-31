from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

browser.get("https://sky.pro")
current_title = browser.title
print(current_title)

browser.quit()