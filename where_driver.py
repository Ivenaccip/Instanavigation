from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = ChromeDriverManager().install()
print(path)
driver = webdriver.Chrome(service = Service(path))
driver.get("https://www.google.com")